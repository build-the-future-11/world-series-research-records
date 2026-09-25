# Implementation task map

All tasks are PLANNED; these are not completion claims.

| Task | Project | Deliverable | Prerequisites |
|---|---|---|---|
| CORE-01 | core | Inventory, identity protection and dependency lock | None |
| CORE-02 | core | Typed contracts, status enums and artifact schemas | CORE-01 |
| CORE-03 | core | Budgets, devices and independent randomness streams | CORE-02 |
| CORE-04 | core | Generators, family splits and protocol registry | CORE-03 |
| CORE-05 | core | Run manifests, metric accounting and report pipeline | CORE-04 |
| CORE-06 | core | Command-line runner and CPU CI smoke path | CORE-05 |
| QL-01 | qlearn | Functional optimizees and exact meta-gradient reference | CORE-06 |
| QL-02 | qlearn | Matched fixed and learned-control optimizer runners | QL-01 |
| QL-03 | qlearn | Bounded learned policy and meta-training | QL-02 |
| QL-04 | qlearn | Ablations and longer-horizon development study | QL-03 |
| QL-05 | qlearn | Evidence audit and bounded claim statement | QL-04 |
| QL-06 | qlearn | Adaptation capability and exhibition demo | QL-05 |
| QA-01 | qapen | Prequential streams and exact finite mixture reference | CORE-06 |
| QA-02 | qapen | Fixed ensembles and memory control suite | QA-01 |
| QA-03 | qapen | Quantizer, expert bank and bounded lifecycle | QA-02 |
| QA-04 | qapen | Returning-regime and noise development study | QA-03 |
| QA-05 | qapen | Calibrated reporting and lineage audit | QA-04 |
| QA-06 | qapen | World-prediction adapter and demo | QA-05 |
| QW-01 | qwipii | Exact finite actions, projective arithmetic and quotient reference | CORE-06 |
| QW-02 | qwipii | Brute, ranking-only and oracle comparison runners | QW-01 |
| QW-03 | qwipii | Bounded discovery grammar and verifier gating | QW-02 |
| QW-04 | qwipii | Orbit-disjoint development and ablation study | QW-03 |
| QW-05 | qwipii | Certificate and claim audit | QW-04 |
| QW-06 | qwipii | Verified reasoning adapter and demo | QW-05 |
| WC-01 | wcode | Typed total DSL and exact bounded interpreter | CORE-06 |
| WC-02 | wcode | Shared enumerator, source-family data and controls | WC-01 |
| WC-03 | wcode | Program graph extractor and hierarchical relational ranker | WC-02 |
| WC-04 | wcode | Search efficiency and encoder ablations | WC-03 |
| WC-05 | wcode | Correctness-scope and complexity report | WC-04 |
| WC-06 | wcode | Bounded synthesis adapter and demo | WC-05 |
| WF-01 | wfim | Exact sparse word algebra and degree truncation | CORE-06 |
| WF-02 | wfim | Weighted norms, tail certificates and fixed controls | WF-01 |
| WF-03 | wfim | Bounded invertible transport and explicit approximation API | WF-02 |
| WF-04 | wfim | Compositional transfer at equal byte budgets | WF-03 |
| WF-05 | wfim | Mathematical assumptions and benefit audit | WF-04 |
| WF-06 | wfim | Algebra capability and demonstration | WF-05 |
| FT-01 | wft | Sparse Laplacian and weighted spectral reference | CORE-06 |
| FT-02 | wft | Fixed and learned operator baselines | FT-01 |
| FT-03 | wft | Predictive operator fitting with scoped constraints | FT-02 |
| FT-04 | wft | Graph-shift, scale-transfer and constraint ablations | FT-03 |
| FT-05 | wft | Operator identifiability and spectral report | FT-04 |
| FT-06 | wft | Spectral capability and demo | FT-05 |
| WP-01 | wpinn | Oscillator trajectories and analytic weak-form reference | CORE-06 |
| WP-02 | wpinn | Sparse, data-only and inverse-PINN controls | WP-01 |
| WP-03 | wpinn | Verified structure and optional alternating fit | WP-02 |
| WP-04 | wpinn | Noise, parameter shift and structural ablations | WP-03 |
| WP-05 | wpinn | Identifiability and law-recovery evidence audit | WP-04 |
| WP-06 | wpinn | Law-identification adapter and demo | WP-05 |
| CW-01 | cwlnn | Sparse graph hierarchy and local dense-equivalence reference | CORE-06 |
| CW-02 | cwlnn | Flat, fixed-hierarchy and feasible attention controls | CW-01 |
| CW-03 | cwlnn | Budgeted routing and multiscale model | CW-02 |
| CW-04 | cwlnn | Size transfer, hierarchy and routing ablations | CW-03 |
| CW-05 | cwlnn | Complexity and efficiency evidence audit | CW-04 |
| CW-06 | cwlnn | Multiscale encoding capability and demo | CW-05 |
| UL-01 | ultron | Typed episode state, capability registry and static router | CORE-06 |
| UL-02 | ultron | Budgeted executor, verifier client and policy controls | UL-01 |
| UL-03 | ultron | Evidence DAG and development-only learned routing | UL-02 |
| UL-04 | ultron | Matched-capability routing development study | UL-03, QW-06, WC-06, WP-06 |
| UL-05 | ultron | Completion/evidence/limitations report | UL-04 |
| UL-06 | ultron | Exhibition replay and unsupported-task handling | UL-05 |
| REL-01 | release | Audit all nine thin slices and claim states | QL-06, QA-06, QW-06, WC-06, WF-06, FT-06, WP-06, CW-06, UL-06 |
| REL-02 | release | Freeze exhibition and bounded release artifacts | REL-01 |
| REL-03 | release | Plan separately authorized confirmation and manuscript scope | REL-02 |


---
