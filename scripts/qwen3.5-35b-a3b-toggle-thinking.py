#!/usr/bin/env python3
"""
Toggle thinking mode for Qwen3.5-35B-A3B in LM Studio or oMLX.

Qwen3.5-35B-A3B defaults to thinking enabled, adding delay before every
response. The /no_think soft switch worked for Qwen3 but appears to have been
removed in Qwen3.5 — it has no effect via OpenAI-compatible endpoints. The only reliable method is patching the
chat template to inject a pre-closed <think></think> block, which tricks
the model into skipping reasoning and producing visible output immediately.

Usage:
  python3 scripts/qwen3.5-35b-a3b-toggle-thinking.py status               # Show current state
  python3 scripts/qwen3.5-35b-a3b-toggle-thinking.py on                    # Enable thinking
  python3 scripts/qwen3.5-35b-a3b-toggle-thinking.py off                   # Disable thinking
  python3 scripts/qwen3.5-35b-a3b-toggle-thinking.py verify                # Check via API
  python3 scripts/qwen3.5-35b-a3b-toggle-thinking.py --models-dir /path status  # Custom models dir

After toggling, reload the model in LM Studio / oMLX for the change to take effect.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Model name as it appears in the model directory
MODEL = "mlx-community/Qwen3.5-35B-A3B-4bit"

# Search these directories in order. First match wins.
MODEL_DIRS = [
    Path.home() / ".lmstudio/models",
    Path.home() / ".omlx/models",
]

# The generation prompt block at the end of the template.
# Thinking OFF: pre-closed <think> block tricks the model into skipping reasoning.
# Thinking ON: no <think> block, model decides naturally.
THINK_OFF_LINE = "    {{- '<think>\\n\\n</think>\\n\\n' }}"
THINK_ON_TAIL = """{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\\n' }}
{%- endif %}"""
THINK_OFF_TAIL = """{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\\n' }}
    {{- '<think>\\n\\n</think>\\n\\n' }}
{%- endif %}"""


def find_template(custom_dir=None):
    """Find the chat template in the first available model directory."""
    if custom_dir:
        p = Path(custom_dir)
        # Accept both the model dir itself and the parent models dir
        direct = p / "chat_template.jinja"
        if direct.exists():
            return direct
        nested = p / MODEL / "chat_template.jinja"
        if nested.exists():
            return nested
        return None
    for model_dir in MODEL_DIRS:
        template = model_dir / MODEL / "chat_template.jinja"
        if template.exists():
            return template
    return None


def detect_state(template):
    """Check whether thinking is on or off in the current template."""
    text = template.read_text()
    if THINK_OFF_LINE in text:
        return "off"
    return "on"


def toggle(template, state):
    """Set thinking to 'on' or 'off' by modifying the chat template."""
    text = template.read_text()
    current = detect_state(template)

    if current == state:
        print(f"Thinking is already {state.upper()}.")
        return

    if state == "off":
        text = text.replace(THINK_ON_TAIL, THINK_OFF_TAIL)
    else:
        text = text.replace(THINK_OFF_TAIL, THINK_ON_TAIL)

    template.write_text(text)

    # Verify the write worked
    new_state = detect_state(template)
    if new_state != state:
        print(f"Error: toggle failed. State is still {new_state.upper()}.", file=sys.stderr)
        sys.exit(1)

    print(f"Thinking is now {state.upper()}.")
    print("Reload the model for the change to take effect.")


def verify(template):
    """Send a test request and check if response contains <think>."""
    base_url = os.environ.get("LMSTUDIO_URL", "http://localhost:1234")
    url = f"{base_url}/v1/chat/completions"

    print(f"\nVerifying against {base_url} ...")
    print("(Make sure the model is reloaded after toggling)\n")

    data = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": "What is 2+2? Reply in one word."}],
        "max_tokens": 200,
        "temperature": 0.6,
    }).encode()

    try:
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        resp = urllib.request.urlopen(req, timeout=60)
        body = json.loads(resp.read())
        content = body["choices"][0]["message"]["content"]
    except (urllib.error.URLError, OSError) as e:
        print(f"Error: Could not reach server at {base_url}: {e}", file=sys.stderr)
        sys.exit(1)
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error: Unexpected response: {e}", file=sys.stderr)
        sys.exit(1)

    if "<think>" in content:
        print("Result: thinking is ON (response contains <think> block)")
    else:
        print("Result: thinking is OFF (no <think> block in response)")

    # Show a truncated preview
    preview = content[:300] + ("..." if len(content) > 300 else "")
    print(f"\nResponse: {preview}")


def main():
    args = sys.argv[1:]
    custom_dir = None

    # Parse --models-dir
    if "--models-dir" in args:
        idx = args.index("--models-dir")
        if idx + 1 >= len(args):
            print("Error: --models-dir requires a path argument", file=sys.stderr)
            sys.exit(1)
        custom_dir = args[idx + 1]
        args = args[:idx] + args[idx + 2:]

    action = args[0] if args else "status"

    template = find_template(custom_dir)
    if not template:
        if custom_dir:
            searched = str(Path(custom_dir) / MODEL)
        else:
            searched = "\n  ".join(str(d / MODEL) for d in MODEL_DIRS)
        print(f"Error: chat_template.jinja not found. Searched:\n  {searched}", file=sys.stderr)
        sys.exit(1)

    print(f"Template: {template}")

    if action == "status":
        state = detect_state(template)
        print(f"Thinking is currently {state.upper()}.")
    elif action in ("on", "off"):
        toggle(template, action)
    elif action == "verify":
        state = detect_state(template)
        print(f"Thinking is currently {state.upper()}.")
        verify(template)
    else:
        print(f"Usage: {sys.argv[0]} [--models-dir PATH] {{status|on|off|verify}}")
        sys.exit(1)


if __name__ == "__main__":
    main()
