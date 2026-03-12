#!/usr/bin/env python3
"""
Generate a markdown results overview table from all benchmark results.

Scans results/ for JSON files in the new directory structure
(results/<model>/<scenario>/<chip>_<backend>.json) and builds
a hardware x scenario matrix showing what's been tested.

Run this to update the results table:
  python3 results-table.py

Paste the output into README.md or pipe it:
  python3 results-table.py > RESULTS.md
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(SCRIPT_DIR, "results")

# Scenarios in display order
SCENARIOS = ["ops-agent", "doc-summary", "prefill-test", "creative-writing"]


def scan_results():
    """
    Scan the results directory and collect metadata.

    Returns a dict: {model: {chip_backend: {scenario: summary_dict}}}
    """
    data = {}

    for model_dir in sorted(os.listdir(RESULTS_DIR)):
        model_path = os.path.join(RESULTS_DIR, model_dir)
        if not os.path.isdir(model_path):
            continue

        for scenario_dir in sorted(os.listdir(model_path)):
            scenario_path = os.path.join(model_path, scenario_dir)
            if not os.path.isdir(scenario_path):
                continue

            for filename in sorted(os.listdir(scenario_path)):
                if not filename.endswith(".json"):
                    continue

                filepath = os.path.join(scenario_path, filename)
                try:
                    with open(filepath) as f:
                        envelope = json.load(f)
                except (json.JSONDecodeError, IOError):
                    continue

                if not isinstance(envelope, dict) or "meta" not in envelope:
                    continue

                meta = envelope["meta"]
                results = envelope.get("results", [])
                valid = [r for r in results if "error" not in r]
                if not valid:
                    continue

                # Build hardware key
                system = meta.get("system", {})
                chip = system.get("chip", "Unknown")
                mem = system.get("memory_gb", "?")
                gpu = system.get("gpu_cores", "?")
                backend = meta.get("backend", "?")
                hw_key = f"{chip} ({mem}GB, {gpu} GPU) / {backend}"

                # Calculate summary stats
                total_time = sum(r["total"] for r in valid)
                total_output = sum(r["output_tokens"] for r in valid)
                avg_gen_tps = sum(r["gen_tps"] for r in valid) / len(valid)
                avg_eff_tps = total_output / total_time if total_time > 0 else 0

                summary = {
                    "avg_gen_tps": round(avg_gen_tps, 1),
                    "avg_eff_tps": round(avg_eff_tps, 1),
                    "total_time": round(total_time, 1),
                }

                data.setdefault(model_dir, {}).setdefault(hw_key, {})[scenario_dir] = summary

    return data


def format_cell(summary):
    """Format a single table cell: effective tok/s (gen tok/s)"""
    if summary is None:
        return " "
    return f"**{summary['avg_eff_tps']}** ({summary['avg_gen_tps']})"


def generate_table(data):
    """Generate the full markdown output."""
    lines = []

    lines.append("## Results Overview")
    lines.append("")
    lines.append("Numbers show **effective tok/s** (generation tok/s in parentheses).")
    lines.append("Effective = what you actually experience. Generation = what the UI reports.")
    lines.append("Higher is better. Blank cells need your data.")
    lines.append("")

    for model, hardware_data in sorted(data.items()):
        lines.append(f"### {model}")
        lines.append("")

        # Collect all scenarios that have data for this model
        active_scenarios = []
        for s in SCENARIOS:
            if any(s in hw_scenarios for hw_scenarios in hardware_data.values()):
                active_scenarios.append(s)

        if not active_scenarios:
            continue

        # Table header
        header = "| Hardware | " + " | ".join(active_scenarios) + " |"
        separator = "|---|" + "|".join(["---:" for _ in active_scenarios]) + "|"
        lines.append(header)
        lines.append(separator)

        # Table rows
        for hw_key in sorted(hardware_data.keys()):
            hw_scenarios = hardware_data[hw_key]
            cells = [format_cell(hw_scenarios.get(s)) for s in active_scenarios]
            lines.append(f"| {hw_key} | " + " | ".join(cells) + " |")

        lines.append("")

    # Gap analysis
    lines.append("### Hardware we need")
    lines.append("")
    lines.append("Run the benchmark and open a PR. Five minutes, zero dependencies.")
    lines.append("")
    lines.append("| Hardware | Status |")
    lines.append("|---|---|")

    # Check what chips we have
    all_chips = set()
    for hardware_data in data.values():
        for hw_key in hardware_data:
            chip_part = hw_key.split(" / ")[0]
            all_chips.add(chip_part)

    wanted = [
        "Apple M1 (8GB, 7 GPU)",
        "Apple M1 (16GB, 8 GPU)",
        "Apple M1 Pro (16GB, 14 GPU)",
        "Apple M1 Pro (32GB, 16 GPU)",
        "Apple M1 Max (32GB, 24 GPU)",
        "Apple M1 Max (64GB, 32 GPU)",
        "Apple M2 (8GB, 8 GPU)",
        "Apple M2 (16GB, 10 GPU)",
        "Apple M2 Pro (16GB, 19 GPU)",
        "Apple M2 Pro (32GB, 19 GPU)",
        "Apple M2 Max (32GB, 30 GPU)",
        "Apple M2 Max (64GB, 38 GPU)",
        "Apple M2 Ultra (64GB, 60 GPU)",
        "Apple M2 Ultra (192GB, 76 GPU)",
        "Apple M3 (8GB, 8 GPU)",
        "Apple M3 (16GB, 10 GPU)",
        "Apple M3 Pro (18GB, 14 GPU)",
        "Apple M3 Pro (36GB, 18 GPU)",
        "Apple M3 Max (36GB, 30 GPU)",
        "Apple M3 Max (48GB, 40 GPU)",
        "Apple M4 (16GB, 10 GPU)",
        "Apple M4 (32GB, 10 GPU)",
        "Apple M4 Pro (24GB, 20 GPU)",
        "Apple M4 Pro (48GB, 20 GPU)",
        "Apple M4 Max (36GB, 40 GPU)",
        "Apple M4 Max (64GB, 40 GPU)",
        "Apple M4 Max (128GB, 40 GPU)",
    ]

    for hw in wanted:
        found = any(hw.split(" (")[0] in chip for chip in all_chips)
        if found:
            lines.append(f"| {hw} | Partial data |")
        else:
            lines.append(f"| {hw} | **Needs data** |")

    lines.append("")
    lines.append("```bash")
    lines.append("python3 bench.py --model llama3.1:8b")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    data = scan_results()
    if not data:
        print("No results found in results/ directory.", file=sys.stderr)
        sys.exit(1)
    print(generate_table(data))
