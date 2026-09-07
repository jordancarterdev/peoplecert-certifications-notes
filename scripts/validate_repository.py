from pathlib import Path
import json
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
records = json.loads((ROOT / "data" / "certifications.json").read_text(encoding="utf-8"))

for item in records:
    for field in ("official_url", "external_url"):
        parsed = urlparse(item[field])
        if parsed.scheme not in {"http", "https"}:
            raise SystemExit(f"Invalid URL: {item['code']} / {field}")

print(f"Validation successful: {len(records)} records.")
