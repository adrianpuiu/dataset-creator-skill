#!/usr/bin/env python3
"""Convert between instruction and conversational JSONL formats."""

import argparse
import json
import sys
from typing import Any


# System prompt for conversational format
DEFAULT_SYSTEM_PROMPT = """You are an expert programmer who writes clean, efficient, well-documented code. You understand multiple programming languages and frameworks. When asked to implement something, you provide complete, working code with appropriate imports and structure."""


def instruction_to_conversational(entry: dict, system_prompt: str | None = None) -> dict:
    """Convert instruction format to conversational format.

    Instruction format:
    {"instruction": "...", "input": "...", "output": "..."}

    Conversational format:
    {"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
    """
    instruction = entry.get("instruction", "")
    input_data = entry.get("input", "")
    output = entry.get("output", "")

    # Build user message
    if input_data and input_data.strip():
        user_content = f"{instruction}\n\nContext:\n{input_data}"
    else:
        user_content = instruction

    messages = [
        {"role": "system", "content": system_prompt or DEFAULT_SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": output},
    ]

    return {"messages": messages}


def conversational_to_instruction(entry: dict) -> dict:
    """Convert conversational format to instruction format."""
    messages = entry.get("messages", [])

    # Extract system, user, assistant messages
    system_content = ""
    user_content = ""
    assistant_content = ""

    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")

        if role == "system":
            system_content = content
        elif role == "user":
            user_content = content
        elif role == "assistant":
            assistant_content = content

    # Try to separate context from instruction
    instruction = user_content
    input_data = ""

    if "\n\nContext:" in user_content or "\n\ncontext:" in user_content.lower():
        parts = user_content.split("\n\nContext:", 1)
        if len(parts) == 1:
            parts = user_content.split("\n\ncontext:", 1)
        if len(parts) == 2:
            instruction = parts[0]
            input_data = parts[1]

    return {
        "instruction": instruction,
        "input": input_data,
        "output": assistant_content,
    }


def detect_format(entries: list[dict]) -> str:
    """Detect whether entries are instruction or conversational format."""
    if not entries:
        return "unknown"

    first = entries[0]

    if "messages" in first:
        return "conversational"
    elif "instruction" in first and "output" in first:
        return "instruction"
    else:
        return "unknown"


def convert_entry(entry: dict, target_format: str, system_prompt: str | None = None) -> dict:
    """Convert a single entry to target format."""
    current = detect_format([entry])

    if current == target_format:
        return entry

    if target_format == "conversational":
        return instruction_to_conversational(entry, system_prompt)
    elif target_format == "instruction":
        return conversational_to_instruction(entry)
    else:
        raise ValueError(f"Unknown target format: {target_format}")


def main():
    parser = argparse.ArgumentParser(description="Convert between JSONL formats")
    parser.add_argument("--input", type=str, required=True, help="Input JSONL file")
    parser.add_argument("--output", type=str, help="Output file (default: stdout)")
    parser.add_argument("--format", type=str, choices=["instruction", "conversational"],
                       help="Target format (auto-detect if not specified)")
    parser.add_argument("--system-prompt", type=str, help="Custom system prompt for conversational format")

    args = parser.parse_args()

    # Detect format if not specified
    target_format = args.format
    if not target_format:
        # Read a sample to detect current format
        sample_entries = []
        with open(args.input, "r") as f:
            for i, line in enumerate(f):
                if i >= 10:
                    break
                if line.strip():
                    try:
                        sample_entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass

        current = detect_format(sample_entries)
        target_format = "conversational" if current == "instruction" else "instruction"

    # Open output
    if args.output:
        out_file = open(args.output, "w")
    else:
        out_file = sys.stdout

    try:
        # Convert and write
        with open(args.input, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    entry = json.loads(line)
                    converted = convert_entry(entry, target_format, args.system_prompt)
                    out_file.write(json.dumps(converted) + "\n")
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"Error processing line: {e}", file=sys.stderr)
                    continue
    finally:
        if args.output:
            out_file.close()

    print(f"Converted to {target_format} format", file=sys.stderr)


if __name__ == "__main__":
    main()
