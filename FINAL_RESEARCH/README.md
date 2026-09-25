# World Series final research package

The nine original research projects remain distinct. This is a verified local
development package with explicit original-scope blockers, not nine completed
papers or independently confirmed results.

- Collection registry and decisions: `../RESEARCH_CLOSURE/REGISTRY.json` and `FINAL_REPORT.md` there.
- Source at entry, including dirty state, branches, every recovered file and hashes: `SOURCE_MANIFEST.json`.
- Historical protocols, seeds, splits, model/baseline settings, metrics and failure rules: `PROTOCOL.yaml`.
- Exact headline tables and source/raw/checkpoint links: `../world-series/results/claim_index.json`.
- Claims in readable form: `CLAIMS_EVIDENCE.md`.
- Manuscript, LaTeX, PDF and generated figures: `../world-series/paper/`.
- Implementation, configs and tests: `../world-series/src/`, `configs/` and `tests/`.
- Raw outcomes and checkpoints: `../world-series/campaigns/` and `runs/`.
- Failed, interrupted, unsupported and stale RUNNING receipts are preserved.

Use Python 3.12 and the repository's pinned requirements. Installation from a
fresh environment requires the listed dependencies to be available:

```sh
cd world-series
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.lock.txt
.venv/bin/python -m pip install --no-deps --no-build-isolation -e .
TMPDIR="$PWD/.work-tmp" ./reproduce.sh --output .work-tmp/FRESH_REVIEW --full-wfim
```

The output must be fresh. This command builds and checks the archive, runs tests,
recomputes the original development analysis, verifies contracts, reloads every
WFIM checkpoint and optionally reruns its complete training/selection process.
It uses an isolated source extraction and the caller's dependency environment;
it does not claim a new independent environment or retrain every historical study.
Set `PYTHON` to another compatible interpreter when needed.

The CWLNN closure replay uses its recorded numerical revision and a separately
installed dependency environment. Its command, restored historical paths,
elapsed time and exact comparisons are in `../RESEARCH_CLOSURE/receipts/cwlnn/`.
Original studies must be replayed against their own source identities, not
silently against later module changes. The source bundle retains Git history.

Official Celo2 weights are not redistributed. Fetch instructions, revision and
weight hashes remain in `../world-series/docs/execution/development-v2/CELO2_PROVENANCE.json`.
UCI digit acquisition/attribution is preserved in `../world-series/data/optdigits/`.
PySINDy has a separate qualified environment and lock under `docs/closure/`.

The WFIM figure is regenerated with `scripts/closure/plot_wfim.py` from the
preserved campaign summary, using matplotlib and the recorded analysis
dependencies. Figure provenance lists the exact data hash. No new experimental
observations are produced by plotting or report regeneration.

Confirmation, original-scope missing controls, authorship, permissions, novelty
review and publication approval remain unresolved. No public deployment,
submission, data replacement or protocol-threshold relaxation occurred.
