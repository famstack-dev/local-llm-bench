"""
Backend adapters for LLM inference servers.

This module provides streaming functions for different LLM backends.
Each function sends a chat completion request, streams the response,
and returns a standardized metrics dictionary.

WHY MULTIPLE BACKENDS?
  Different inference servers expose different APIs:
  - LM Studio and llama-server use the OpenAI-compatible API (SSE streaming)
  - Ollama has its own native API with extra features (think control, eval stats)

  Each backend returns the same metrics shape so the benchmark runner
  doesn't need to know which backend it's talking to.

WHAT WE MEASURE:
  Every LLM response has two phases:
  1. Prefill — processing the input prompt (measured as TTFT: Time To First Token)
  2. Generation — producing the output tokens (measured as tok/s)

  We measure both by tracking timestamps during streaming:
  - t_start: when we send the HTTP request
  - first_token_time: when we receive the first content token
  - t_end: when streaming completes

  TTFT = first_token_time - t_start  (includes network + prefill)
  gen_time = t_end - first_token_time (pure generation)

RETURN FORMAT:
  {
      "ttft": float,            # seconds waiting before first token appeared
      "gen_time": float,        # seconds of token generation
      "gen_tps": float,         # generation speed: output_tokens / gen_time
      "total": float,           # total wall clock: ttft + gen_time
      "output_tokens": int,     # how many content tokens we received
      "response": str,          # the full response text (for context accumulation)
      "prompt_eval_count": int, # total prompt tokens evaluated (Ollama only)
      "prompt_eval_duration_ms": float,  # prefill compute time in ms (Ollama only)
  }
"""

import json
import os
import time
import urllib.request


# Default ports for each backend. These are the standard defaults:
# - Ollama runs on 11434 (brew service)
# - LM Studio runs on 1234 (desktop app)
# - llama-server defaults to 8080, but we use 8090 to avoid conflicts
DEFAULT_URLS = {
    "ollama": "http://localhost:11434",
    "lmstudio": "http://localhost:1234",
    "llama-server": "http://localhost:8090",
    "minimax": "https://api.minimax.io",
}


def stream_openai(base_url, model, messages, max_tokens=300, temperature=0.6, timeout=300, extra_headers=None):
    """
    Stream a chat completion via the OpenAI-compatible API.

    Works with LM Studio, llama-server, and cloud APIs that implement
    the OpenAI format (e.g. MiniMax).

    The OpenAI streaming format uses Server-Sent Events (SSE):
      data: {"choices": [{"delta": {"content": "Hello"}}]}
      data: {"choices": [{"delta": {"content": " world"}}]}
      data: [DONE]

    Each "data:" line contains a JSON object with a delta (partial content).
    We count each non-empty content delta as one token. This is approximate —
    some deltas may contain multiple tokens or partial tokens — but it's
    close enough for benchmarking purposes.
    """
    url = f"{base_url}/v1/chat/completions"
    data = {
        "model": model,
        "messages": messages,
        "stream": True,              # Enable SSE streaming
        "max_tokens": max_tokens,    # Cap output length
        "temperature": temperature,  # Lower = more deterministic
    }
    headers = {"Content-Type": "application/json"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(
        url, data=json.dumps(data).encode(),
        headers=headers,
    )

    # Start the clock when we send the request
    t_start = time.time()
    resp = urllib.request.urlopen(req, timeout=timeout)

    first_token_time = None   # When the first content token arrives
    token_count = 0           # Number of content tokens received
    full_response = []        # Accumulate the full response text

    # Read the SSE stream line by line
    for line in resp:
        line = line.decode().strip()

        # SSE lines start with "data: ". Skip empty lines and other SSE fields.
        if not line.startswith("data: "):
            continue
        chunk = line[6:]  # Strip the "data: " prefix

        # The stream ends with a special [DONE] marker
        if chunk == "[DONE]":
            break

        try:
            d = json.loads(chunk)
            content = d["choices"][0]["delta"].get("content", "")
            if content:
                # Record when the first content token arrives — this is our TTFT
                if first_token_time is None:
                    first_token_time = time.time()
                token_count += 1
                full_response.append(content)
        except (json.JSONDecodeError, KeyError, IndexError):
            pass  # Skip malformed chunks

    # Stop the clock
    t_end = time.time()

    # Calculate metrics
    ttft = first_token_time - t_start if first_token_time else t_end - t_start
    gen_time = t_end - first_token_time if first_token_time else 0
    total = t_end - t_start
    gen_tps = token_count / gen_time if gen_time > 0 else 0

    return {
        "ttft": ttft,
        "gen_time": gen_time,
        "gen_tps": gen_tps,
        "total": total,
        "output_tokens": token_count,
        "response": "".join(full_response),
    }


def stream_ollama(base_url, model, messages, max_tokens=300, temperature=0.6, timeout=300):
    """
    Stream a chat completion via Ollama's native /api/chat endpoint.

    WHY NOT USE THE OPENAI ENDPOINT FOR OLLAMA?
      Ollama also exposes /v1/chat/completions (OpenAI-compatible), but:
      1. It doesn't support "think": false — Qwen3.5 burns all tokens on
         invisible <think> blocks, producing empty visible output.
      2. It doesn't return eval stats (prompt_eval_count, eval_duration)
         which we need to analyze caching behavior.

    OLLAMA STREAMING FORMAT:
      Each line is a JSON object. During generation:
        {"message": {"content": "Hello"}, "done": false}
        {"message": {"content": " world"}, "done": false}
      The final line has done=true and includes timing stats:
        {"done": true, "prompt_eval_count": 834, "eval_count": 207, ...}

    THINKING MODE:
      Qwen3.5 models default to thinking enabled (internal <think> blocks).
      We set "think": false to disable it — otherwise the model spends
      all its tokens on invisible reasoning and produces no visible output.
    """
    url = f"{base_url}/api/chat"
    data = {
        "model": model,
        "messages": messages,
        "stream": True,
        "think": False,  # Disable Qwen3.5 thinking mode (see docstring above)
        "options": {
            "num_predict": max_tokens,    # Ollama's equivalent of max_tokens
            "temperature": temperature,
        },
    }
    req = urllib.request.Request(
        url, data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"},
    )

    # Start the clock
    t_start = time.time()
    resp = urllib.request.urlopen(req, timeout=timeout)

    first_token_time = None
    token_count = 0
    full_response = []
    final_stats = {}    # Will hold the eval stats from the done=true message

    # Read JSON objects line by line (Ollama's native streaming format)
    for line in resp:
        line = line.decode().strip()
        if not line:
            continue
        try:
            d = json.loads(line)

            # The final message (done=true) contains timing stats from llama.cpp.
            # prompt_eval_count: total prompt tokens processed
            # prompt_eval_duration: time spent on prefill (nanoseconds)
            # eval_count: output tokens generated
            # eval_duration: time spent on generation (nanoseconds)
            if d.get("done"):
                final_stats = {
                    "prompt_eval_count": d.get("prompt_eval_count"),
                    "prompt_eval_duration_ns": d.get("prompt_eval_duration"),
                    "eval_count": d.get("eval_count"),
                    "eval_duration_ns": d.get("eval_duration"),
                }
                break

            # Content tokens arrive in message.content
            content = d.get("message", {}).get("content", "")
            if content:
                if first_token_time is None:
                    first_token_time = time.time()
                token_count += 1
                full_response.append(content)
        except (json.JSONDecodeError, KeyError):
            pass

    t_end = time.time()

    # Calculate the same metrics as the OpenAI adapter
    ttft = first_token_time - t_start if first_token_time else t_end - t_start
    gen_time = t_end - first_token_time if first_token_time else 0
    total = t_end - t_start
    gen_tps = token_count / gen_time if gen_time > 0 else 0

    return {
        "ttft": ttft,
        "gen_time": gen_time,
        "gen_tps": gen_tps,
        "total": total,
        "output_tokens": token_count,
        "response": "".join(full_response),
        # Ollama-specific: internal stats from llama.cpp
        # NOTE: prompt_eval_count always reports TOTAL prompt tokens, even when
        # the KV cache is reused. It does NOT indicate cache miss. To detect
        # caching, compare wall-clock TTFT across turns — if it stays flat
        # while context grows, the cache is working.
        "prompt_eval_count": final_stats.get("prompt_eval_count"),
        "prompt_eval_duration_ms": (final_stats.get("prompt_eval_duration_ns") or 0) / 1_000_000,
    }


def stream_minimax(base_url, model, messages, max_tokens=300, temperature=0.6, timeout=300):
    """
    Stream a chat completion via MiniMax's OpenAI-compatible API.

    MiniMax exposes an OpenAI-compatible endpoint at https://api.minimax.io/v1.
    The main differences from a local backend:
      - Requires MINIMAX_API_KEY for authentication
      - Temperature must be in (0.0, 1.0] — zero is rejected

    Supported models:
      - MiniMax-M2.5: Peak performance, 204K context
      - MiniMax-M2.5-highspeed: Same quality, faster response

    API docs: https://platform.minimax.io/docs/api-reference/text-openai-api
    """
    api_key = os.environ.get("MINIMAX_API_KEY", "")
    if not api_key:
        raise ValueError(
            "MINIMAX_API_KEY environment variable is required.\n"
            "  Get your key at https://platform.minimax.io/"
        )

    # MiniMax rejects temperature=0. Clamp to a small positive value.
    if temperature <= 0:
        temperature = 0.01
    elif temperature > 1.0:
        temperature = 1.0

    return stream_openai(
        base_url, model, messages, max_tokens, temperature, timeout,
        extra_headers={"Authorization": f"Bearer {api_key}"},
    )


def get_model_info(backend, base_url, model):
    """
    Fetch model details from the backend, if available.

    This makes result files self-documenting — you can see the exact model
    architecture, parameter count, quantization, and format without having
    to remember what you ran.

    Only Ollama provides detailed model info via /api/show. For LM Studio
    and llama-server, we return just the model name.
    """
    info = {"name": model}

    if backend == "minimax":
        # MiniMax model info is static — no discovery endpoint needed.
        models = {
            "MiniMax-M2.5": {"parameter_size": "unknown", "context_window": 204800},
            "MiniMax-M2.5-highspeed": {"parameter_size": "unknown", "context_window": 204800},
        }
        if model in models:
            info.update(models[model])
        return info

    if backend == "ollama":
        try:
            url = f"{base_url}/api/show"
            data = json.dumps({"model": model}).encode()
            req = urllib.request.Request(
                url, data=data,
                headers={"Content-Type": "application/json"},
            )
            resp = urllib.request.urlopen(req, timeout=5)
            d = json.loads(resp.read())
            details = d.get("details", {})
            if details:
                info["format"] = details.get("format")
                info["family"] = details.get("family")
                info["parameter_size"] = details.get("parameter_size")
                info["quantization"] = details.get("quantization_level")
        except Exception:
            pass

    return info


def get_backend(name):
    """
    Look up the streaming function for a backend name.

    Returns a callable with the signature:
      (base_url, model, messages, max_tokens, temperature, timeout) -> metrics dict

    Both functions return the same metrics shape, so the benchmark runner
    can treat all backends identically.
    """
    backends = {
        "ollama": stream_ollama,       # Native API with think:false + eval stats
        "lmstudio": stream_openai,     # OpenAI-compatible SSE
        "llama-server": stream_openai, # OpenAI-compatible SSE (raw llama.cpp)
        "minimax": stream_minimax,     # MiniMax cloud API (OpenAI-compatible)
    }
    if name not in backends:
        raise ValueError(f"Unknown backend: {name}. Choose from: {', '.join(backends)}")
    return backends[name]
