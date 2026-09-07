import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "technical" / "service-inventory.json").read_text(encoding="utf-8"))

for service in data["services"]:
    print(
        f"{service['name']:24} "
        f"owner={service['owner']:18} "
        f"criticality={service['criticality']}"
    )
