#!/usr/bin/env python3
"""Extract code patterns from source files and generate instruction-input-output JSONL entries."""

import argparse
import json
import re
from pathlib import Path
from typing import Generator


# Pattern definitions by language
PATTERNS = {
    "python": {
        "function": r'(async\s+)?def\s+(\w+)\s*\((.*?)\)\s*(?:->\s*([^:]+))?:',
        "class": r'class\s+(\w+)(?:\(([^)]+)\))?:',
        "import": r'(?:from\s+(\S+)\s+)?import\s+(.+)',
        "decorator": r'@(\w+)(?:\((.*?)\))?',
        "try_catch": r'try:\s*\n(.*?)\s*except\s+(?:.*?\s+)?as\s+(\w+):',
        "async_for": r'async\s+for\s+(\w+)\s+in\s+.*?:',
        "with": r'with\s+(.+?):',
        "dataclass": r'@dataclass\s*\nclass\s+(\w+):',
    },
    "javascript": {
        "function": r'(?:async\s+)?function\s+(\w+)\s*\((.*?)\)',
        "arrow_function": r'(?:const|let|var)\s+(\w+)\s*=\s*(?:\((.*?)\)|\w+)\s*=>',
        "class": r'class\s+(\w+)(?:\s+extends\s+(\w+))?',
        "import": r"import\s+(?:(\{[^}]+\})|(\w+)|\*\s+as\s+(\w+))\s+from\s+['\"]([^'\"]+)['\"]",
        "export": r"export\s+(?:(default)|(?:const|let|var|function|class))",
        "try_catch": r'try\s*{(.*?)}\s*catch\s*\((\w+)\)\s*{',
        "promise": r'new\s+Promise\s*\((\w+)\s*=>',
    },
    "typescript": {
        "function": r'(?:async\s+)?function\s+(\w+)\s*\((.*?)\)\s*:\s*(\w+)',
        "arrow_function": r'(?:const|let|var)\s+(\w+)\s*(?::\s*\w+)?\s*=\s*(?:\((.*?)\)|\w+)\s*=>',
        "interface": r'interface\s+(\w+)(?:\s+extends\s+([^\{]+))?',
        "type": r'type\s+(\w+)\s*=\s*(.+?);',
        "class": r'class\s+(\w+)(?:\s+extends\s+(\w+))?\s*{',
        "import": r"import\s+(?:(\{[^}]+\})|(\w+)|\*\s+as\s+(\w+))\s+from\s+['\"]([^'\"]+)['\"]",
        "enum": r'enum\s+(\w+)\s*{',
    },
    "go": {
        "function": r'func\s+(?:\((\w+)\s+\*?\w+\)\s+)?(\w+)\s*\((.*?)\)(?:\s*\(([^)]+)\))?',
        "interface": r'type\s+(\w+)\s+interface\s*{',
        "struct": r'type\s+(\w+)\s+struct\s*{',
        "import": r'import\s+(?:(\([\s\S]*?\))|"(.*?)"|(\w+))',
        "goroutine": r'go\s+func\s*\(',
        "defer": r'defer\s+',
        "select": r'select\s*{',
    },
    "rust": {
        "function": r'(?:async\s+)?(?:pub\s+)?fn\s+(\w+)\s*\((.*?)\)(?:\s*->\s*([^\{]+))?',
        "struct": r'struct\s+(\w+)(?:<[^>]+>)?',
        "enum": r'enum\s+(\w+)(?:<[^>]+>)?',
        "trait": r'trait\s+(\w+)(?:<[^>]+>)?',
        "impl": r'impl\s+(?:<[^>]+>\s+)?(\w+)(?:\s+for\s+(\w+))?',
        "use": r'use\s+([^;]+);',
        "macro": r'#\[(\w+)(?:\((.*?)\))?\]',
    },
    "java": {
        "class": r'(?:public\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?(?:\s+implements\s+([^\{]+))?',
        "interface": r'interface\s+(\w+)',
        "method": r'(?:public|private|protected)?\s*(?:static)?\s*(?:\w+(?:<[^>]+>)?)\s+(\w+)\s*\((.*?)\)',
        "annotation": r'@(\w+)(?:\((.*?)\))?',
    },
}


INSTRUCTION_TEMPLATES = {
    "function": "Create a function named {name}",
    "async_function": "Create an async function named {name}",
    "class": "Define a class named {name}",
    "interface": "Define an interface named {name}",
    "struct": "Define a struct named {name}",
    "import": "Import {target} from a module",
    "decorator": "Use the {decorator} decorator",
    "try_catch": "Implement error handling with try-catch",
    "arrow_function": "Create an arrow function",
}


def extract_from_code(content: str, language: str, file_path: str) -> Generator[dict, None, None]:
    """Extract patterns from code content."""
    patterns = PATTERNS.get(language, {})

    lines = content.splitlines()

    for pattern_name, pattern in patterns.items():
        try:
            matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)

            for match in matches:
                entry = create_entry_from_match(match, pattern_name, lines, language, file_path)
                if entry:
                    yield entry
        except re.error:
            continue


def create_entry_from_match(match, pattern_name, lines, language, file_path) -> dict | None:
    """Create a JSONL entry from a regex match."""
    start = match.start()
    end = match.end()

    # Find line numbers
    line_num = content_to_line_num(lines, start)
    snippet = get_code_snippet(lines, line_num, context=2)

    matched_text = match.group(0)

    # Generate instruction
    instruction = generate_instruction(pattern_name, match, language)

    if not instruction:
        return None

    return {
        "instruction": instruction,
        "input": "",  # Could be populated with required imports/context
        "output": matched_text.strip(),
        "metadata": {
            "language": language,
            "pattern": pattern_name,
            "file": file_path,
            "line": line_num,
        },
    }


def content_to_line_num(lines, pos):
    """Convert character position to line number."""
    current = 0
    for i, line in enumerate(lines):
        current += len(line) + 1  # +1 for newline
        if current > pos:
            return i + 1
    return len(lines)


def get_code_snippet(lines, line_num, context=2):
    """Get code snippet with context lines."""
    start = max(0, line_num - context - 1)
    end = min(len(lines), line_num + context)
    return "\n".join(lines[start:end])


def generate_instruction(pattern_name, match, language):
    """Generate instruction text from pattern match."""
    template = INSTRUCTION_TEMPLATES.get(pattern_name)

    if template:
        try:
            return template.format(**match.groupdict())
        except (KeyError, IndexError):
            pass

    # Fallback instructions
    instructions = {
        "function": f"Define a function",
        "async_function": "Create an async function",
        "class": f"Define a class",
        "interface": "Define an interface",
        "struct": "Define a struct",
        "import": "Write an import statement",
        "decorator": "Use a decorator",
        "try_catch": "Add error handling with try-catch",
        "arrow_function": "Create an arrow function",
        "enum": "Define an enum",
        "trait": "Define a trait",
        "impl": "Implement a trait for a type",
        "type": "Define a type alias",
        "method": "Define a method",
    }

    return instructions.get(pattern_name, f"Write code: {pattern_name}")


def detect_language(file_path: Path) -> str | None:
    """Detect programming language from file extension."""
    ext_map = {
        ".py": "python",
        ".pyi": "python",
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".go": "go",
        ".rs": "rust",
        ".java": "java",
        ".c": "c",
        ".cpp": "cpp",
        ".h": "c",
        ".hpp": "cpp",
    }
    return ext_map.get(file_path.suffix.lower())


def extract_from_file(file_path: Path) -> Generator[dict, None, None]:
    """Extract patterns from a single file."""
    language = detect_language(file_path)
    if not language:
        return

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return

    yield from extract_from_code(content, language, str(file_path))


def main():
    parser = argparse.ArgumentParser(description="Extract code patterns for training data")
    parser.add_argument("--repo", type=str, required=True, help="Path to repository")
    parser.add_argument("--output", type=str, default="dataset.jsonl", help="Output JSONL file")
    parser.add_argument("--extensions", type=str, help="File extensions to include (comma-separated)")
    parser.add_argument("--max-samples", type=int, help="Maximum samples to extract")
    parser.add_argument("--include-metadata", action="store_true", help="Include metadata in output")

    args = parser.parse_args()

    repo_path = Path(args.repo)
    extensions = set(args.extensions.split(",")) if args.extensions else None

    entries = []
    exclude_dirs = {"node_modules", "venv", ".venv", "__pycache__", ".git", "dist", "build", "target"}

    for file_path in repo_path.rglob("*"):
        if not file_path.is_file():
            continue

        if any(excl in file_path.parts for excl in exclude_dirs):
            continue

        if extensions and file_path.suffix.lower() not in extensions:
            continue

        for entry in extract_from_file(file_path):
            if not args.include_metadata and "metadata" in entry:
                del entry["metadata"]

            entries.append(entry)

            if args.max_samples and len(entries) >= args.max_samples:
                break

        if args.max_samples and len(entries) >= args.max_samples:
            break

    # Write output
    with open(args.output, "w") as f:
        for entry in entries:
            f.write(json.dumps(entry) + "\n")

    print(f"Extracted {len(entries)} patterns to {args.output}")


if __name__ == "__main__":
    main()
