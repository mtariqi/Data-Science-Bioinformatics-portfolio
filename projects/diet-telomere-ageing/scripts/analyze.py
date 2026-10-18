"""Scaffold output only: define and validate the analysis before fitting models."""
from pathlib import Path
import pandas as pd

inventory = pd.read_csv(snakemake.input[0], sep="\t")
out = Path(snakemake.output[0])
out.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame([
    {"status": "scaffold_only",
     "input_file_count": len(inventory),
     "note": "No inferential model fitted; preregister variables and survey design first."}
]).to_csv(out, sep="\t", index=False)
