# Reproducibility Protocol

The submission should be reviewable from a clean checkout without relying on local state, credentials, or hidden files.

## Environment

- Python: 3.11+
- Default demo mode: local and credential-free
- Runtime state: generated under `data/` and ignored by Git
- Secrets: supplied only through environment variables for integrations; never committed

## Clean-room procedure

```bash
git clone https://github.com/fotografandrzejmikulski-bit/Agents-for-Humans-Hackathon.git
cd Agents-for-Humans-Hackathon
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e '.[dev]'
pytest -q
ruff check .
python scripts/repo_quality_check.py
python -m cognisync --pretty
python -m cognisync --demo-gate --pretty
python -m cognisync --demo-gate --approve --pretty
```

## Reproducibility requirements

A reported result should include:

1. repository commit SHA;
2. Python version;
3. installed package versions or lock/constraints file used for the run;
4. scenario / fixture identifier;
5. command executed;
6. relevant environment configuration without secret values;
7. observed output and failures.

## Integrity boundaries

The deterministic local mode is the canonical reviewer path. Cloud integrations, model-specific behavior and external connectors are additional layers and must be evaluated independently. A cloud adapter passing import or construction checks is not equivalent to proving production connectivity or successful external execution.
