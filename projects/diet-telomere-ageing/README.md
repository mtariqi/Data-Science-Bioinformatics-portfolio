# Diet, Telomeres, and Biological Ageing

Reproducible project scaffold for evaluating dietary patterns and telomere-related ageing biomarkers. The initial computational analysis is designed around public NHANES 1999–2002 data. This repository does not provide medical advice and does not claim that any individual food prevents ageing.

## Repository status

The workflow and container scaffolding are in place. The analysis scripts currently validate inputs and produce a reproducible pipeline skeleton; the final exposure definitions and inferential models must be preregistered and reviewed before scientific interpretation. NHANES is cross-sectional for this analysis, so results can show associations, not causation.

## Structure

- `workflow/Snakefile`: Snakemake DAG for downloading, preparing, and analyzing public NHANES data.
- `workflow/envs/`: pinned workflow dependencies.
- `scripts/`: data download, preparation, and analysis entry points.
- `config/config.yaml`: cycles and workflow settings.
- `tests/`: smoke test using synthetic data; no participant data committed.
- `data/` and `results/`: runtime outputs, excluded from Git.
- `Dockerfile`: reproducible runtime.
- root `.github/workflows/diet-telomere-ageing.yml`: Docker build and workflow smoke test.

## Run with Docker

```bash
docker build -t diet-telomere-ageing .
docker run --rm -v "$PWD":/project -w /project diet-telomere-ageing \
  snakemake --snakefile workflow/Snakefile --cores 2
```

For a lightweight DAG check: `snakemake -n --snakefile workflow/Snakefile`.

## Data and privacy

The workflow downloads public NHANES XPT files at runtime. Raw data and derived outputs are not committed. Do not add restricted, identifiable, or clinical participant data to this repository. Record source URLs, retrieval dates, checksums, and any transformations in the project provenance log.

## Scientific safeguards

- Separate observational associations from causal claims.
- Predefine exposures, outcomes, covariates, and multiplicity handling before model fitting.
- Use NHANES survey weights, strata, and clusters for population inference.
- Treat individual foods and AI-derived predictions as exploratory unless independently validated.
- A future intervention requires ethics approval, consent, clinical oversight, and a justified sample-size calculation.
