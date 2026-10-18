"""Download one public-use NHANES XPT file with basic integrity checks."""
import argparse
from pathlib import Path
import requests

p = argparse.ArgumentParser()
p.add_argument("--url", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()
out = Path(a.output)
out.parent.mkdir(parents=True, exist_ok=True)
r = requests.get(a.url, timeout=120)
r.raise_for_status()
if len(r.content) < 100:
    raise SystemExit(f"Downloaded file is unexpectedly small: {a.url}")
out.write_bytes(r.content)
print(f"Downloaded {a.url} ({len(r.content)} bytes)")
