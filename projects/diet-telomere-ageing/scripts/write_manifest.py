"""Write run provenance for workflow output."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import hashlib

p = argparse.ArgumentParser()
p.add_argument("--input", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()
source = Path(a.input)
digest = hashlib.sha256(source.read_bytes()).hexdigest()
out = Path(a.output)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(
    f"created_utc: {datetime.now(timezone.utc).isoformat()}\n"
    f"input: {source}\nsha256: {digest}\n", encoding="utf-8")
