# World Series research records

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/build-the-future-11/world-series-research-records?include_prereleases)](https://github.com/build-the-future-11/world-series-research-records/releases/tag/v0.1.0-oss)

Collection-level planning, audit, publication and provenance records for the
nine-module [World Series workbench](https://github.com/build-the-future-11/world-series).

**License:** Apache-2.0 — see [`LICENSE`](LICENSE), [`NOTICE`](NOTICE),
[`THIRD_PARTY.md`](THIRD_PARTY.md).
**Go-live results:** [`release_export/20260925/GO_LIVE_RESULTS.json`](release_export/20260925/GO_LIVE_RESULTS.json).

## What this collection contains

- `world_series_cursor_pack/`: reconstructed planning specifications and validators.
- `RESEARCH_CLOSURE/`: bounded study registry, decisions and verification receipts.
- `FINAL_RESEARCH/`: historical source manifests and changes; preserve their snapshots.
- `publication_audit/`: dated scientific and manuscript audits.
- `publication/`: preserved publication closure freeze; unfinished authoring remains explicit.
- `release_export/20260925/`: initial inventory, preserved working diff and current checks.
- Implementation clone expected at `world-series/` (separate repository).

The nine empty top-level aliases contain no independent source and are not new
projects. Celo2 is a third-party dependency inside the implementation workspace
and is not redistributed by this collection.

## Installation and usage

```sh
gh repo clone build-the-future-11/world-series-research-records
gh repo clone build-the-future-11/world-series world-series-research-records/world-series
cd world-series-research-records
python3 world_series_cursor_pack/tools/validate_pack.py
python3 world_series_cursor_pack/tools/check_math_reference.py
```

For numerical environment installation, raw archive download, tests and replay,
see the implementation's `docs/RELEASE_REPRODUCIBILITY.md` and
`docs/OPEN_SOURCE_GO_LIVE.md`. Restoring the raw archive is required before
collection-wide claim/evidence validation against campaigns. After restoration:

```sh
python3 release_export/verify_claims.py --repo world-series/.work-tmp/restored --output FRESH.json
```

These are same-host engineering and artifact checks, not independent replication.

## Results and limitations

Bounded negative/inconclusive outcomes remain valid results. New generalization,
independent confirmation and original full-architecture claims are NOT YET
ESTABLISHED. Do not interpret stale COMPLETE labels as acceptance of the nine
original proposals. No production deployment applies.

## Citation

Repository URLs and exact Git revisions. Author / copyright: Ryan (see
implementation `docs/AUTHORSHIP.md`).
