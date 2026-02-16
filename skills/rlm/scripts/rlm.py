"""
RLM Engine — helper script for the Recursive Language Model skill.

Indexes files, searches content, and chunks large files for parallel processing.

Original concept by BowTiedSwan (https://github.com/BowTiedSwan/rlm-skill).
Adapted for the Claude Code CLI environment.

License notice: The original repository does not specify a license.
This adaptation is provided with attribution; upstream licensing status is unresolved.
"""

import glob
import json
import math
import argparse
from pathlib import Path
from typing import List, Dict, Any

EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv", ".tox", ".mypy_cache"}


class RLMContext:
    def __init__(self, root_dir: str = "."):
        self.root = Path(root_dir)
        self.index: Dict[str, str] = {}
        self.chunk_size = 5000

    def load_context(self, pattern: str = "**/*", recursive: bool = True) -> str:
        files = glob.glob(str(self.root / pattern), recursive=recursive)
        loaded_count = 0
        total_size = 0
        for f in files:
            path = Path(f)
            if not path.is_file():
                continue
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            try:
                content = path.read_text(errors="ignore")
                self.index[str(path)] = content
                loaded_count += 1
                total_size += len(content)
            except Exception:
                pass
        return f"RLM: Loaded {loaded_count} files. Total size: {total_size} chars."

    def peek(self, query: str, context_window: int = 200) -> List[Dict[str, str]]:
        results = []
        for path, content in self.index.items():
            start = 0
            while True:
                idx = content.find(query, start)
                if idx == -1:
                    break
                snippet_start = max(0, idx - context_window)
                snippet_end = min(len(content), idx + len(query) + context_window)
                snippet = content[snippet_start:snippet_end]
                results.append({"file": path, "snippet": snippet})
                start = idx + 1
                if len(results) >= 30:
                    return results
        return results

    def get_chunks(self, file_pattern: str = None) -> List[Dict[str, Any]]:
        chunks = []
        targets = [
            f for f in self.index.keys() if (not file_pattern or file_pattern in f)
        ]
        for path in targets:
            content = self.index[path]
            total_chunks = math.ceil(len(content) / self.chunk_size)
            for i in range(total_chunks):
                start = i * self.chunk_size
                end = min((i + 1) * self.chunk_size, len(content))
                chunks.append(
                    {"source": path, "chunk_id": i, "content": content[start:end]}
                )
        return chunks


def main():
    parser = argparse.ArgumentParser(description="RLM Engine")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Index files from a directory")
    scan_parser.add_argument("--path", default=".", help="Root directory to scan")

    peek_parser = subparsers.add_parser("peek", help="Search indexed files for a query")
    peek_parser.add_argument("query", help="Search string")
    peek_parser.add_argument("--path", default=".", help="Root directory to scan")

    chunk_parser = subparsers.add_parser("chunk", help="Split files into JSON chunks")
    chunk_parser.add_argument("--pattern", default=None, help="Filter by file pattern")
    chunk_parser.add_argument("--path", default=".", help="Root directory to scan")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    ctx = RLMContext(root_dir=args.path)
    ctx.load_context()

    if args.command == "scan":
        print(ctx.load_context())
    elif args.command == "peek":
        results = ctx.peek(args.query)
        print(json.dumps(results, indent=2))
    elif args.command == "chunk":
        chunks = ctx.get_chunks(args.pattern)
        print(json.dumps(chunks))


if __name__ == "__main__":
    main()
