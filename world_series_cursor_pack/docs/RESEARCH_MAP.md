# Related work → implementation decisions

This review separates established ingredients from proposed combinations and the experiments needed to distinguish them. Source keys resolve to sources/REFERENCES.md. It does not certify novelty or promise publication acceptance.

| Project | Closest prior families | Proposed first discriminating question | Important non-claim |
|---|---|---|---|
| Quantum Learning / MALIS | Learned optimizers, MAML, Celo, Celo2, ELO [R01–R05] | Does a bounded task-aware update policy improve loss-versus-compute on held-out task families and longer horizons? | Learning an optimizer, a scheduler or adaptation itself is not new. |
| Q-APEN | VQ representation, probabilistic ensembles, world-model planning [R06–R08] plus immutable PEN lineage | Does expert/memory lifecycle allocation improve recurrent-shift prediction at matched total cost? | Finite spawning heuristics are neither infinite execution nor Bayesian nonparametric inference. |
| QWIPII | Equivariance, symmetry discovery, RG, neural-symbolic geometry [R09–R13] | Does verified transformation discovery reduce search while preserving proofs under held-out transforms? | Invariance itself and discovering it are established; approximate invariance cannot certify pruning. |
| World-CNN Code | Program graphs, DreamCoder, evaluator-based program search [R14–R16] | Does relational program encoding improve the same bounded synthesis search at equal verification budget? | Program graphs and automated program search are not new, and runtime plots do not resolve P versus NP. |
| World-FIM∞ | Hypercomplex layers, HDC, graded/signature representations, algebras [R17–R20] | Can a learned algebra-preserving coordinate system improve compositional tasks at equal stored bytes? | Infinite-dimensional spaces and isomorphic coordinate changes are not newly invented numbers. |
| World-FT | Graph spectra, learned Laplacians, neural operators [R21–R25] | Do verified symmetry/coarse-consistency constraints improve a learned spectral operator on held-out graphs? | Learning the operator or its basis alone is existing work. |
| World-PINN | Forward/inverse PINNs, SINDy, symbolic regression, HNN [R26–R31] | Does verified, task-appropriate structure improve weak-form sparse law recovery under shift and noise? | Original PINNs already address discovery; low residual does not guarantee correct laws. |
| CWLNN | Latent bottlenecks, sparse experts, graph pooling, state spaces [R32–R35] | Does a truly sparse hierarchy achieve better accuracy/cost tradeoffs with size transfer? | Hierarchies, local graph convolution and sparse routing are existing ingredients. |
| Ultron | AI Scientist, ADAS, Darwin Gödel Machine, Co-Scientist [R36–R39] | Does evidence-aware budgeted routing beat static routing with identical capabilities? | Multi-agent orchestration or self-editing does not establish ASI. |

## Reading priorities for implementation

The implementer should read the exact methods of the nearest comparator before writing its baseline, not just its abstract. Priority method reads: Celo/Celo2/ELO; PETS; LieGAN and G-CNN; program graphs and DreamCoder; PHM and the signature primer; learned Laplacians and FNO; inverse PINNs and SINDy; DiffPool; Darwin Gödel Machine. Selected method sections were consulted for this plan, while the registry identifies abstract-screened context entries.

For every reproduced baseline write a `reproduction_note.md`: original task, official implementation revision when used, license, deviations, hyperparameters, omitted components, and one reference behavior check. Label a simplified implementation `inspired_by`, not `faithful_reproduction`. Do not claim to outperform a named paper from a differently scaled toy adaptation.

## Research contribution ladder

First establish a clean negative-or-positive mechanism experiment. Then establish transfer to a second nontrivial family. Then test stronger faithful comparators with matched budgets. Only after those stages assess whether the theoretical or algorithmic distinction warrants a separate paper. Nine namespaces do not force nine publishable contributions. Some may become supporting infrastructure, ablations or one combined paper.

## Novelty audit template

For each proposed claim, list the closest papers; the exact algorithmic difference; whether the difference changes information access or compute; what a fair ablation removes; and what outcome would refute the claim. Search using both your project name and standard technical terms. A project acronym will usually miss its relevant literature. Additional targeted novelty search is required before a submission; this pack does not claim exhaustive coverage of every 2026 release.


---
