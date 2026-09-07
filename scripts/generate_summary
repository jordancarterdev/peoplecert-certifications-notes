from pathlib import Path
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
records = json.loads((ROOT / "data" / "certifications.json").read_text(encoding="utf-8"))
counts = Counter(x["track"] for x in records)

lines = ["# Repository Summary", "", "| Track | Count |", "|---|---:|"]
for track, count in sorted(counts.items()):
    lines.append(f"| {track} | {count} |")

(ROOT / "REPOSITORY-SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Generated REPOSITORY-SUMMARY.md")
