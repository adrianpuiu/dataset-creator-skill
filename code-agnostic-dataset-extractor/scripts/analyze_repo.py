#!/usr/bin/env python3
"""Analyze a codebase to identify languages, files, and patterns for dataset extraction."""

import argparse
import json
from pathlib import Path
from collections import defaultdict
import hashlib


# Language detection by file extension
LANGUAGE_MAP = {
    # Python
    ".py": "python",
    ".pyi": "python",

    # JavaScript/TypeScript
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".mjs": "javascript",
    ".cjs": "javascript",

    # Go
    ".go": "go",

    # Rust
    ".rs": "rust",

    # C/C++
    ".c": "c",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".h": "c",
    ".hpp": "cpp",

    # Java
    ".java": "java",

    # C#
    ".cs": "csharp",

    # Ruby
    ".rb": "ruby",

    # PHP
    ".php": "php",

    # Swift
    ".swift": "swift",

    # Kotlin
    ".kt": "kotlin",
    ".kts": "kotlin",

    # Scala
    ".scala": "scala",

    # Shell
    ".sh": "shell",
    ".bash": "shell",
    ".zsh": "shell",

    # Web
    ".html": "html",
    ".css": "css",
    ".scss": "scss",
    ".less": "less",

    # Config/Data
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".toml": "toml",
    ".xml": "xml",
}

# Directories to exclude
EXCLUDE_DIRS = {
    "node_modules", "venv", "env", ".venv", "virtualenv",
    "__pycache__", ".git", ".hg", ".svn",
    "dist", "build", "target", "bin", "obj",
    ".idea", ".vscode", ".vs",
    "vendor", "third_party",
    ".next", ".nuxt", "coverage",
    "logs", "tmp", "temp",
}


def get_language(file_path: Path) -> str | None:
    """Detect language from file extension."""
    suffix = file_path.suffix.lower()
    return LANGUAGE_MAP.get(suffix)


def should_exclude(path: Path) -> bool:
    """Check if path should be excluded."""
    # Check if any parent directory is in exclude list
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True

    # Check hidden files/directories
    if path.name.startswith(".") and path.name != ".gitignore":
        return True

    return False


def analyze_file(file_path: Path) -> dict:
    """Analyze a single file."""
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        line_count = len(content.splitlines())
        char_count = len(content)

        # Calculate hash for deduplication
        file_hash = hashlib.md5(content.encode()).hexdigest()

        return {
            "path": str(file_path),
            "language": get_language(file_path),
            "size_bytes": char_count,
            "lines": line_count,
            "hash": file_hash,
        }
    except Exception as e:
        return {
            "path": str(file_path),
            "language": get_language(file_path),
            "error": str(e),
        }


def analyze_repository(repo_path: Path, extensions: list[str] | None = None) -> dict:
    """Analyze a repository and return file statistics."""
    repo_path = Path(repo_path).resolve()

    files_by_lang = defaultdict(list)
    all_files = []
    errors = []

    # Find all source files
    for file_path in repo_path.rglob("*"):
        if not file_path.is_file():
            continue

        if should_exclude(file_path):
            continue

        lang = get_language(file_path)
        if lang is None:
            continue

        if extensions and file_path.suffix.lower() not in extensions:
            continue

        file_info = analyze_file(file_path)

        if "error" in file_info:
            errors.append(file_info)
        else:
            files_by_lang[lang].append(file_info)
            all_files.append(file_info)

    # Calculate statistics
    lang_stats = {}
    for lang, files in files_by_lang.items():
        lang_stats[lang] = {
            "file_count": len(files),
            "total_lines": sum(f.get("lines", 0) for f in files),
            "total_bytes": sum(f.get("size_bytes", 0) for f in files),
        }

    return {
        "repository_path": str(repo_path),
        "total_files": len(all_files),
        "languages": lang_stats,
        "files": all_files,
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze a codebase for dataset extraction")
    parser.add_argument("--path", type=str, required=True, help="Path to repository")
    parser.add_argument("--output", type=str, help="Output JSON file")
    parser.add_argument("--extensions", type=str, help="Comma-separated file extensions to include (e.g., .py,.js)")

    args = parser.parse_args()

    extensions = None
    if args.extensions:
        extensions = [ext.strip() for ext in args.extensions.split(",")]

    result = analyze_repository(args.path, extensions)

    output = json.dumps(result, indent=2)

    if args.output:
        Path(args.output).write_text(output)
        print(f"Analysis saved to {args.output}")
    else:
        print(output)

    # Print summary
    print("\n" + "=" * 50)
    print("Repository Analysis Summary")
    print("=" * 50)
    print(f"Path: {result['repository_path']}")
    print(f"Total files: {result['total_files']}")
    print("\nLanguages:")
    for lang, stats in result["languages"].items():
        print(f"  {lang}: {stats['file_count']} files, {stats['total_lines']} lines")


if __name__ == "__main__":
    main()
