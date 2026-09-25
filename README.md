# World Series research records

Collection-level planning, audit, publication and provenance records for the
nine-module [World Series workbench](https://github.com/Build-the-future12/world-series).
This is a private archival review export. It is not nine separate implemented
repositories or a publication acceptance claim.

## What this collection contains

- `world_series_cursor_pack/`: reconstructed planning specifications and validators.
- `RESEARCH_CLOSURE/`: bounded study registry, decisions and verification receipts.
- `FINAL_RESEARCH/`: historical source manifests and changes; preserve their snapshots.
- `publication_audit/`: dated scientific and manuscript audits.
- `publication/`: preserved publication closure freeze; unfinished authoring remains explicit.
- `release_export/20260925/`: initial inventory, preserved working diff and current checks.
- `FINAL_RELEASE_REPORT.md`: private export recommendation and remaining limitations.

The nine empty top-level aliases contain no independent source and are not new
projects. The Celo2 checkout is a third-party dependency inside the implementation
workspace; its remote and local generated weights are not changed by this export.

## Installation and usage

Clone the collection, then its implementation into the expected child path:

```sh
gh repo clone Build-the-future12/world-series-research-records
gh repo clone Build-the-future12/world-series world-series-research-records/world-series
cd world-series-research-records
python3 world_series_cursor_pack/tools/validate_pack.py
python3 world_series_cursor_pack/tools/check_math_reference.py
```

For numerical environment installation, raw archive download, tests and replay,
see the implementation's `docs/RELEASE_REPRODUCIBILITY.md`. Restoring its raw
archive is required before collection-wide claim/evidence validation. After
restoration, use `python3 release_export/verify_claims.py --output FRESH.json`.
These are same-host engineering and artifact checks, not independent replication.

## Results and limitations

Bounded negative/inconclusive outcomes remain valid results. New generalization,
independent confirmation and original full-architecture claims are NOT YET
ESTABLISHED. Historical reports may describe older snapshots; current export
receipts identify their actual inputs. Do not interpret stale COMPLETE labels
as public release approval. No production deployment applies.

## Citation and license

For private review use repository URLs and exact Git revisions. Human author
names, affiliations and a publication citation are not supplied by this export.
Distribution terms remain unresolved; see `LICENSE.md`. Preserve third-party
attributions and do not infer a blanket open-source license.
