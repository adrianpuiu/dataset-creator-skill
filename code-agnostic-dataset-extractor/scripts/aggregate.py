#!/usr/bin/env python3
"""Aggregate and validate JSONL dataset entries."""

import argparse
import json
import hashlib
from pathlib import Path
from collections import defaultdict


def validate_entry(entry: dict) -> tuple[bool, str | None]:
    """Validate a single JSONL entry.

    Returns (is_valid, error_message).
    """
    # Check required fields
    required_fields = ["instruction", "input", "output"]
    for field in required_fields:
        if field not in entry:
            return False, f"Missing required field: {field}"

    # Check field types
    for field in required_fields:
        if not isinstance(entry[field], str):
            return False, f"Field '{field}' must be a string"

    # Check for empty output
    if not entry["output"].strip():
        return False, "Output field is empty"

    # Check instruction quality
    if len(entry["instruction"]) < 10:
        return False, "Instruction too short"

    return True, None


def compute_hash(entry: dict) -> str:
    """Compute hash for deduplication."""
    content = f"{entry['instruction']}|{entry['output']}"
    return hashlib.md5(content.encode()).hexdigest()


def aggregate_files(input_dir: Path, pattern: str = "*.jsonl") -> list[dict]:
    """Aggregate all JSONL files from a directory."""
    entries = []

    for file_path in input_dir.rglob(pattern):
        try:
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            entry = json.loads(line)
                            entry["_source_file"] = str(file_path)
                            entries.append(entry)
                        except json.JSONDecodeError:
                            continue
        except Exception:
            continue

    return entries


def deduplicate(entries: list[dict]) -> list[dict]:
    """Remove duplicate entries based on content hash."""
    seen = set()
    unique = []

    for entry in entries:
        entry_hash = compute_hash(entry)
        if entry_hash not in seen:
            seen.add(entry_hash)
            unique.append(entry)

    return unique


def quality_score(entry: dict) -> float:
    """Calculate quality score for an entry.

    Higher is better. Considers:
    - Instruction length and clarity
    - Output length
    - Presence of input context
    - Code-like patterns in output
    """
    score = 0.0

    # Instruction length (ideal: 20-100 chars)
    instr_len = len(entry["instruction"])
    if 20 <= instr_len <= 100:
        score += 10
    elif instr_len > 10:
        score += 5

    # Output length
    output_len = len(entry["output"])
    if output_len > 50:
        score += 10
    elif output_len > 20:
        score += 5

    # Has meaningful input
    if entry["input"].strip():
        score += 5

    # Instruction starts with action verb
    action_verbs = ["create", "define", "implement", "add", "write", "build",
                   "make", "generate", "construct", "initialize", "declare"]
    if entry["instruction"].lower().split()[0] in action_verbs:
        score += 10

    # Output looks like code
    code_indicators = ["def ", "function", "class ", "import ", "interface",
                      "struct ", "fn ", "type ", "const ", "let ", "var "]
    if any(ind in entry["output"] for ind in code_indicators):
        score += 15

    return score


def filter_by_quality(entries: list[dict], min_score: float = 20.0) -> list[dict]:
    """Filter entries by quality score."""
    return [e for e in entries if quality_score(e) >= min_score]


def split_dataset(entries: list[dict], train_ratio: float = 0.8,
                  val_ratio: float = 0.1) -> dict[str, list[dict]]:
    """Split dataset into train/validation/test sets."""
    import random

    shuffled = entries.copy()
    random.shuffle(shuffled)

    n = len(shuffled)
    train_end = int(n * train_ratio)
    val_end = train_end + int(n * val_ratio)

    return {
        "train": shuffled[:train_end],
        "validation": shuffled[train_end:val_end],
        "test": shuffled[val_end:],
    }


def write_jsonl(entries: list[dict], output_path: Path):
    """Write entries to JSONL file."""
    with open(output_path, "w") as f:
        for entry in entries:
            # Remove internal metadata fields
            clean_entry = {k: v for k, v in entry.items()
                          if not k.startswith("_")}
            f.write(json.dumps(clean_entry) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Aggregate and validate JSONL datasets")
    parser.add_argument("--input_dir", type=str, help="Input directory with JSONL files")
    parser.add_argument("--input", type=str, help="Input JSONL file")
    parser.add_argument("--output", type=str, default="training_dataset.jsonl", help="Output file")
    parser.add_argument("--split", action="store_true", help="Create train/val/test splits")
    parser.add_argument("--deduplicate", action="store_true", default=True, help="Remove duplicates")
    parser.add_argument("--min-quality", type=float, default=0.0, help="Minimum quality score")
    parser.add_argument("--validate", action="store_true", default=True, help="Validate entries")
    parser.add_argument("--pattern", type=str, default="*.jsonl", help="File pattern for directory input")

    args = parser.parse_args()

    # Load entries
    if args.input_dir:
        entries = aggregate_files(Path(args.input_dir), args.pattern)
    elif args.input:
        entries = []
        with open(args.input, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    else:
        parser.error("Either --input_dir or --input is required")

    print(f"Loaded {len(entries)} entries")

    # Validate
    if args.validate:
        valid = []
        invalid = []

        for entry in entries:
            is_valid, error = validate_entry(entry)
            if is_valid:
                valid.append(entry)
            else:
                invalid.append((entry, error))

        entries = valid
        print(f"Validation: {len(valid)} valid, {len(invalid)} invalid")

        if invalid and len(invalid) <= 10:
            for entry, error in invalid[:10]:
                print(f"  - {error}: {entry.get('instruction', '')[:50]}...")

    # Deduplicate
    if args.deduplicate:
        original = len(entries)
        entries = deduplicate(entries)
        print(f"Deduplication: {original} -> {len(entries)} entries")

    # Quality filter
    if args.min_quality > 0:
        original = len(entries)
        entries = filter_by_quality(entries, args.min_quality)
        print(f"Quality filter: {original} -> {len(entries)} entries")

    # Write output
    if args.split:
        splits = split_dataset(entries)
        output_base = Path(args.output).stem
        output_dir = Path(args.output).parent

        for split_name, split_entries in splits.items():
            split_path = output_dir / f"{output_base}_{split_name}.jsonl"
            write_jsonl(split_entries, split_path)
            print(f"Wrote {len(split_entries)} entries to {split_path}")
    else:
        write_jsonl(entries, Path(args.output))
        print(f"Wrote {len(entries)} entries to {args.output}")


if __name__ == "__main__":
    main()
