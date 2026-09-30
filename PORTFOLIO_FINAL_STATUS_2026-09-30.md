# Research Portfolio Final Status — 2026-09-30

This file is the finite closure ledger for the active research portfolio. A project is considered closed when its current claim has an explicit endpoint: POSITIVE, NEGATIVE, BOUNDARY, or ARCHIVED_WITH_EVIDENCE. Optional successor protocols do not keep the current project open.

| Project | Final state | Closure basis |
|---|---|---|
| APEN / Burgers | BOUNDARY | Six-seed replay-verified study: APEN improves the frozen base by 0.3127% pooled MSE (6/6 seeds), but has 4.9836% higher MSE than continued-base training under the primary equal-update comparison. Claim-bearing paper revision merged. |
| APEN Navier–Stokes successor | ARCHIVED_WITH_EVIDENCE / BLOCKED SUCCESSOR | Validated-solver branch exists, but hosted CI repeatedly terminates before step 1. It is not part of the closed APEN efficacy claim and must not be presented as verified. |
| FIM | NEGATIVE / BOUNDARY | Canonical mixed/negative study and final closeout are retained on main. |
| LAM-JEPA | NEGATIVE / INCONCLUSIVE | Frozen negative/inconclusive ARC evidence; paper/AISTATS/reproducibility/claim-boundary builds are green. Portal actions are external human submission work, not unfinished research. |
| Kyrlov-JEPA hybrid | BOUNDARY | Physics-first PT1/PT2 adaptive solvers pass the frozen synthetic comparison gates; learned Krylov feature mechanisms do not beat matched scratch controls. Hybrid PR merged. |
| IRIS | BOUNDARY | Evidence-first closeout package merged; retained mixed/negative evidence and unresolved provenance limits are explicit. |
| IRIS-Space / SIDEREA | BOUNDARY | Evidence-reconciliation package and hosted engineering verification are complete and merged. Scientific/eligibility/authorship/submission approval remains intentionally separate. |
| FI-JEPA | NEGATIVE / BOUNDARY | Canonical v1 macrodata evidence is negative/mixed versus raw-context Ridge. v2 is an optional pre-outcome successor, not unfinished v1 work. |
| Eigen-JEPA | BOUNDARY | Existing retained evidence is mixed/negative. Classical-baseline ladder is a pre-outcome optional successor. |
| Adaptive Theory Geometry | BOUNDARY | Complete reproducible synthetic manuscript/benchmark; synthetic gains are retained, while general discovery/external superiority is not established. |
| NGMT | BOUNDARY | Component-positive / full-mechanism-negative closure; adverse and contaminated cells remain preserved rather than rescued. |
| QFIM | BOUNDARY | Root scientific truth records mixed FIM ablation evidence; unsupported blanket superiority claims are withdrawn. |
| World-Series research program | NEGATIVE / BOUNDARY | Bounded multi-module program, replay/audit/reproducibility and OSS closure are complete; stronger architecture/generalization claims remain not established. |
| Math-11 exploratory research | ARCHIVED_WITH_EVIDENCE | No canonical repository/evidence package currently establishes a publication-grade novel theorem. The exploratory work is closed rather than left as an indefinite research obligation. A future theorem/novelty program must start as a new versioned project. |

## Canonical actions completed on 2026-09-30

- Merged IRIS closeout PR #7.
- Merged IRIS-Space evidence-reconciliation PR #30.
- Merged Kyrlov-JEPA hybrid PR #10 after all exact-head workflows were green.
- Merged APEN claim-bearing paper revision PR #17.
- Re-ran APEN-Synthica PR #17/#18 failing workflows without altering science; failures repeated with zero executed steps, confirming the current hosted Actions admission/runner blocker.
- Recorded bounded final-status files for ATG, FI-JEPA, and Eigen-JEPA.
- LAM-JEPA exact-head AISTATS, paper, reproducibility, and claim-boundary workflows are green.
- FIM already contains its 2026-09-30 final research closeout on main.

## What is *not* unfinished research

The following are deliberately excluded from the research backlog:
- portal submissions, receipts, author-profile actions, venue quota/reviewer eligibility;
- independent external replication not already commissioned;
- optional successor studies and broader validation;
- public-release pushes that require human authorship/release approval;
- stronger claims that the retained evidence does not support.

## Portfolio state

**ACTIVE CURRENT RESEARCH BACKLOG: ZERO.**

Any further experiment must begin as a new, versioned successor with its own hypothesis, evidence boundary, and authorization rather than silently reopening a closed project.
