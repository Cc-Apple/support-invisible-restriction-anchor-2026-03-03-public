#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compute_sha256_manifest.py

Purpose:
  Compute SHA256 hashes for preserved private artifacts and generate
  CSV / JSON / Markdown manifests.

What it does:
  - Recursively scans a private artifact directory.
  - Computes SHA256 for files.
  - Records file size, relative path, extension, and category.
  - Produces:
      - sha256_manifest.csv
      - sha256_manifest.json
      - sha256_manifest.md

Safety boundary:
  - Reads local files only.
  - Does not modify artifacts.
  - Does not upload files.
  - Does not connect to network.
  - Does not alter device/account/profile state.

Example:
  python compute_sha256_manifest.py --input private_artifacts --output review_output/sha256_manifest
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List


SKIP_DIR_NAMES = {
    ".git",
    "__pycache__",
    ".DS_Store",
}


@dataclass
class HashRow:
    relative_path: str
    filename: str
    category: str
    extension: str
    size_bytes: int
    sha256: str


def classify(path: Path) -> str:
    name = path.name
    lower = name.lower()

    if lower.endswith(".zip"):
        return "zip_archive"
    if lower.endswith(".tar.gz"):
        return "sysdiagnose_or_tar_gz"
    if lower.endswith(".ips") or lower.endswith(".ips.ca.synced"):
        return "ios_log"
    if lower.endswith(".session"):
        return "session_log"
    if lower.endswith(".spin"):
        return "spin_log"
    if lower.endswith(".plist"):
        return "plist"
    if lower.endswith(".json"):
        return "json"
    if lower.endswith(".csv"):
        return "csv"
    if lower.endswith(".txt") or lower.endswith(".log"):
        return "text_log"
    if lower.endswith((".png", ".jpg", ".jpeg", ".heic", ".webp")):
        return "screenshot_or_image"
    if lower.endswith((".mov", ".mp4", ".m4v")):
        return "video"
    if lower.endswith((".db", ".sqlite", ".sqlite3")):
        return "database"
    return "other"


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & SKIP_DIR_NAMES)


def collect_hashes(input_dir: Path) -> List[HashRow]:
    rows: List[HashRow] = []

    for p in sorted(input_dir.rglob("*")):
        if not p.is_file():
            continue
        if should_skip(p):
            continue

        try:
            rel = str(p.relative_to(input_dir))
            size = p.stat().st_size
            digest = sha256_file(p)
        except Exception as e:
            print(f"[WARN] failed: {p} : {e}", file=sys.stderr)
            continue

        rows.append(
            HashRow(
                relative_path=rel,
                filename=p.name,
                category=classify(p),
                extension="".join(p.suffixes),
                size_bytes=size,
                sha256=digest,
            )
        )

    return rows


def write_csv(path: Path, rows: List[HashRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(HashRow.__dataclass_fields__.keys())

    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(asdict(r))


def write_json(path: Path, rows: List[HashRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([asdict(r) for r in rows], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_markdown(path: Path, rows: List[HashRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# SHA256 Manifest")
    lines.append("")
    lines.append("Raw artifacts are not included in the public repository.")
    lines.append("")
    lines.append("| Category | Size | SHA256 | Relative path |")
    lines.append("|---|---:|---|---|")

    for r in rows:
        lines.append(
            f"| `{r.category}` | {r.size_bytes} | `{r.sha256}` | `{r.relative_path}` |"
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Private artifact directory")
    ap.add_argument("--output", required=True, help="Output directory")
    args = ap.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)

    if not input_dir.exists():
        print(f"[ERROR] input does not exist: {input_dir}", file=sys.stderr)
        return 2

    rows = collect_hashes(input_dir)

    write_csv(output_dir / "sha256_manifest.csv", rows)
    write_json(output_dir / "sha256_manifest.json", rows)
    write_markdown(output_dir / "sha256_manifest.md", rows)

    print(f"[OK] files hashed: {len(rows)}")
    print(f"[OK] output: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
