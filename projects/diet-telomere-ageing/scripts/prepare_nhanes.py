"""Create an input inventory; variable harmonization is a documented next step."""
from pathlib import Path
import hashlib
import pandas as pd

files = [Path(p) for p in snakemake.input]
rows = []
for path in files:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    rows.append({"file": path.name, "bytes": path.stat().st_size, "sha256": digest})
out = Path(snakemake.output[0])
out.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(rows).to_csv(out, sep="\t", index=False)
