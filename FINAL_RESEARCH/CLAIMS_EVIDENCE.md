# Claims and evidence

All quantitative headline tables are transcribed programmatically from the linked JSON, including failed cells and null means.
Machine-readable exact values, raw-file hashes, source identities, configs and checkpoints: `world-series/results/claim_index.json`.

| Project | Bounded finding | Analysis | Raw campaign |
|---|---|---|---|
| qlearn | No general optimizer advantage; failed sensitivity trajectories remain incomplete. | `world-series/docs/closure/GATE_RESULTS.json` | `world-series/campaigns/natural-digits-v1/` |
| qapen | Lifecycle and delayed-utility memory execute; the combined candidate loses to rolling ridge and recent-memory controls. | `world-series/docs/closure/QAPEN_RESULTS.json` | `world-series/campaigns/qapen-lifecycle-v1/` |
| qwipii | Learned discovery reduces expansions but is slower than random ordering; greedy ranking produces longer paths in some cases. | `world-series/docs/closure/QWIPII_LEARNED_AUDIT.json` | `world-series/campaigns/qwipii-learned-development-v1/` |
| wcode | Trained relational scoring has no robust advantage; held-composition cap24 success is zero. Historical overlap is disclosed. | `world-series/docs/closure/WCODE_RESULTS.json` | `world-series/campaigns/wcode-trained-v1/` |
| wfim | Per-letter product transport cancels exactly. Learned per-word coordinates do not beat identity coordinates on ordered-pattern prediction. | `world-series/docs/closure/WFIM_LEARNING_AUDIT.json` | `world-series/campaigns/wfim-coordinate-development-v1/` |
| wft | Both constraints lower mean error within the declared generator; individual negative cells and spectral-boundary discrepancies remain. | `world-series/docs/closure/WFT_RESULTS.json` | `world-series/campaigns/wft-constraints-v1/` |
| wpinn | Neural weak and passive variants retain failed cells; their primary means stay null. Solver diagnostics do not replace original failures. | `world-series/docs/closure/WPINN_RESULTS.json` | `world-series/campaigns/wpinn-structured-v1/` |
| cwlnn | Learned half routing is slower and less accurate than full hierarchy on both declared tasks. | `world-series/docs/closure/CWLNN_RESULTS.json` | `world-series/campaigns/cwlnn-conditional-v1/` |
| ultron | Observed routing gain over best fixed tool has a family-bootstrap interval spanning zero; no general-agent claim. | `world-series/docs/closure/GATE_RESULTS.json` | `world-series/campaigns/development-v2/` |

Scope: same-host development evidence. No independent replication or publication-readiness claim.
The initial snapshot preserves 181 run manifests including failed, interrupted, unsupported and historically RUNNING receipts.
The stale RUNNING artifact is a historical attempt, not an active worker; see `world-series/docs/closure/RECOVERY.json`.
