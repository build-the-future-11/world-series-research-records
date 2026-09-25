# WORLD SERIES — Complete Research and Cursor Blueprint

Prepared September 22, 2026. Planning package; not a set of trained models.

This consolidated copy contains the research, mathematical derivations, nine project specifications, execution order, integrator prompt and source registry. The ZIP additionally includes per-module prompts, machine-readable tasks, configuration templates, Cursor rules and executable planning/reference checks.


---

<!-- Source document: START_HERE.md -->

# Start here — World Series Cursor research pack

## What this is

A planning and research package for all nine projects, prepared September 22, 2026. It contains no trained model and no claimed benchmark win. Intended source paths and commands describe what Cursor should implement. Existing repositories have not been inspected or changed by this package.

## Files to read first

Open WORLD_SERIES_MASTER_PLAN.md for scope/order; AGENTS.md for immutable guardrails; docs/ARCHITECTURE.md for contracts; docs/EXPERIMENT_PROTOCOL.md for evaluation; then the single assigned docs/projects/ specification. The source registry records paper titles, URLs, reading depth and implementation relevance. Mathematical derivations and their assumptions are in docs/MATH_FOUNDATIONS.md.

## Validate the planning package

From this directory run:

```bash
python3 tools/validate_pack.py
python3 tools/check_math_reference.py
```

These are the only execution checks shipped by the plan. They validate file/task/schema consistency and tiny mathematical reference examples. They do not train or validate any of the nine proposed models and do not establish new theorems by testing examples.

## Start Cursor

Open this folder as a new workbench, or copy it into a separately reviewed new project directory without overwriting existing work. Paste prompts/00_integrator.md first. Bootstrap CORE-01 through CORE-06. Then use one module prompt from prompts/01_qlearn.md through prompts/09_ultron.md and its next unblocked task.

The included .cursor/rules/*.mdc files and AGENTS.md provide persistent project instructions, following Cursor's documented formats [D01]. They are not security isolation or a substitute for testing. Keep the final evaluator/answers outside the development-agent workspace.

Do not paste the entire source registry and all nine specifications into every session. Each task records minimal relevant files and papers. Preserve context between sessions using templates/HANDOFF.md. One integrator owns shared contracts; module workers should not independently redesign them.

## Important statuses

All implementation tasks start PLANNED. Every claim starts NOT_RUN. Development configuration JSON files are templates, not authorized confirmation protocols. Missing practical thresholds/sample sizes are intentional unresolved experimental-design choices to settle using development evidence before freezing a confirmation protocol—not permission to choose them after looking at final results.

Proposed application commands such as `python -m world_series run ...` become available only after Cursor implements the corresponding package tasks. The pack validator passing does not imply that command already exists.

## Deadline

Sunday, September 27 is the demonstration target. October 4 is the follow-on v0.1 target. Prioritize real thin slices and clear limitations rather than nine untested large architectures. Successful verification with a negative empirical result is still a useful completed research artifact.


---

<!-- Source document: WORLD_SERIES_MASTER_PLAN.md -->

# WORLD SERIES — research and Cursor implementation plan

**Prepared September 22, 2026. Exposition target: Sunday, September 27. Follow-on release target: October 4.**

This pack contains a reviewed research foundation, proposed mathematics, nine engineering specifications, a dependency-ordered execution queue and Cursor instruction files. It does not contain nine implemented/trained models, benchmark results or a verified novelty guarantee. No existing repositories were modified or audited as part of constructing this pack. Dates are scope targets, not promises that all hypotheses will succeed.

## The program in one sentence

Investigate whether explicit adaptation of learning rules, simulation capacity, symmetry reasoning, program representations, algebraic representations, spectral operators, physical constraints, multiscale computation and tool selection can improve separately measurable tasks under explicit budgets.

The project tuple is an organizing language, not a theorem of universal intelligence. One workbench makes experiments consistent; it does not justify training all nine mechanisms jointly before their individual effects are understood.

## Frozen project identities and first vertical slices

| Project / namespace | First executable scientific slice | Later ambition |
|---|---|---|
| Quantum Learning / qlearn | Bounded learned update policy on held-out small optimizees | Joint curriculum, memory and compute adaptation |
| Q-APEN / qapen | Finite adaptive experts and engrams on returning regimes | Larger simulation graphs and more principled capacity inference |
| QWIPII / qwipii | Verified symmetry quotient search plus exact projective identity | Broader learned mathematical reasoning |
| World-CNN Code / wcode | Typed-DSL graph-guided synthesis with a real verifier | Safe repository-level algorithm improvement |
| World-FIM∞ / wfim | Exact sparse algebra, degree truncation and learned coordinate test | Better extensible operator/representation families |
| World Fourier / wft | Learned sparse graph operator and weighted transform | Domain/discretization transfer with justified spectral assumptions |
| World-PINN / wpinn | Weak-form oscillator law identification with valid structure | More difficult PDE and symmetry-discovery tasks |
| CWLNN / cwlnn | Sparse hierarchical graph model with measured routing cost | Reusable multimodal/world-model backbone |
| Ultron / ultron | Evidence-aware routing over several real capabilities | Carefully evaluated sequential research orchestration |

## Research corrections that shape the build

Learning an optimizer, discovering symmetry, representing programs as graphs, learning Laplacians, identifying unknown equations with PINNs, sparse routing and research-agent orchestration all have substantial prior art. The source registry maps that work to exact comparison obligations. The initial goal is not to announce nine revolutions; it is to isolate nine mechanisms well enough that positive or negative findings mean something.

Infinite-dimensional algebra needs a finite approximation contract. Approximate invariance does not permit exact search pruning. Eigenspaces can be nonunique. Known physics constraints can be wrong for another system. A large collection of tools does not establish general intelligence. These are implementation requirements, not cosmetic wording caveats.

## Repository and workflow decision

Use one new monorepo with independent module namespaces. Existing APEN/PEN and FIM work remains protected; use reviewed, provenance-pinned adapters rather than changing archived experiments. Keep all modules independently runnable. Do not make one universal tensor forward method or require every experiment to depend on Ultron.

One integrator builds core contracts and locks the environment. Then assign isolated modules to coding agents. Start with at most two or three simultaneous editing workers if the environment supports them, and one numerical experiment worker. The nine briefs are logical ownership units, not an instruction to launch nine memory-intensive agents or training jobs. This is a suggested concurrency policy, not a measured device limit.

A task is small enough when it implements one verifiable unit with its tests and a handoff. Use six stages per module: reference, controls, candidate, development comparisons, evidence audit, adapter/demo. Do not substitute a 5,000-line one-shot generation for this progression.

## Proposed calendar and exit criteria

**September 22:** finalize identities, source inventory, comparison questions and exact reference assumptions. Establish core schemas and dependency policy. Exit: nine unambiguous specifications, protected legacy boundaries and no unknown claimed results.

**September 23:** finish core runner/receipts and reference implementations. Prioritize algebra arithmetic, quotient search, typed DSL, oscillator weak residual, graph Laplacian and simple optimizees. Exit: executable references with actual tests; no learned-model claim required.

**September 24:** implement nearest simple baselines and small candidates. Keep the same data/contracts across controls. Exit: at least one end-to-end development run per unblocked module or a precise blocker receipt.

**September 25:** test mechanism ablations and adversarial cases. Fit small policies only after data and evaluation are trustworthy. Integrate a few real adapters into Ultron; do not wait for every optional feature. Exit: truthful preliminary comparisons, including failed mechanisms.

**September 26:** freeze the demonstration code/configuration. Rerun selected demos, verify artifact hashes and prepare offline recorded outputs as labeled fallbacks. Exit: reproducible evidence-backed demonstrations, not a promise of statistical significance.

**Sunday, September 27:** show the research program, several live or clearly labeled replay demos, all nine status cards, the closest prior work and the actual limitations. A module with only reference arithmetic is shown as such; missing learned components are not hidden.

**September 28–October 4:** strengthen comparators and task families; use development variance to design feasible confirmation runs; freeze protocols before approved final evaluation; analyze results and decide manuscript scope. Nine technical notes may be useful, but nine separate publishable discoveries must not be assumed.

If the schedule slips, reduce experiment breadth—not verification or scientific honesty. Keep one strong family and one failure control per module before adding a new domain. The exposition can present negative and incomplete findings accurately without representing them as completed successes.

## Exposition structure

Show one overview, then a few high-information demonstrations: MALIS adaptation, verified invariant search, algebra/spectral structure, and Ultron executing a real checked task. Display a compact nine-project status table. Each card contains the hypothesis, closest baseline, implemented scope, actual metric with evidence reference or NOT_RUN, and limitation. Avoid a live giant training session as the critical demonstration path.

Every plot comes from raw run artifacts. Label mock fixtures, replays and synthetic data. A paper citation establishes prior art, not evidence that this implementation works. A proof-backed reference operator establishes its stated mathematics, not learned downstream benefit.

## Final definition of done

Software: reference and behavioral tests; reproducible command; bounded resources; typed failures; provenance; no hidden placeholder. Research: comparable baselines; leakage checks; actual raw results; uncertainty where appropriate; ablations; defensible scope and negative outcomes preserved. Integration: only real registered capabilities, immutable evidence and a verifier outside the agent's control. Publication: further novelty/reproduction review, clear assumptions, permissions/licenses and appropriate claim wording.

Read START_HERE.md to run the package validator and hand the first task to Cursor.


---

<!-- Source document: docs/RESEARCH_MAP.md -->

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

<!-- Source document: docs/MATH_FOUNDATIONS.md -->

# Mathematical foundations and checkable derivations

These are derivations for this design. They are not claims of new mathematics. The modeling combinations are research proposals; their empirical benefit and novelty remain to be established against the cited literature.

## 1. A budgeted, typed world description—not a universal theorem

Use a typed tuple `W=(X, μ, A, G, L, D, J)` to record state space, measure, representation algebra, admissible transformations, dynamics/operator, evidence and objective. Different tasks instantiate different subsets. It is bookkeeping that aligns modules, not proof that a single universal representation exists. In particular a stochastic transition kernel, an elliptic differential operator and a program semantics function are distinct types.

MALIS adapts an update policy; Q-APEN allocates model/memory capacity; QWIPII proposes and verifies transformations; WCode searches bounded programs; WFIM defines a structured algebra; WFT estimates a spectral operator; WPINN identifies laws; CWLNN computes sparse multiscale features; Ultron selects valid operations under budgets. Missing components are permitted.

## 2. Conditional descent for bounded learned preconditioning

Let `f:R^d→R` be L-smooth, `g=∇f(θ)` and `D` symmetric positive definite with `aI ≼ D ≼ bI`, where `0<a≤b`. For `θ'=θ−ηDg`, smoothness gives

`f(θ') ≤ f(θ) − η gᵀDg + (Lη²/2)||Dg||²`

`≤ f(θ) − (ηa − Lη²b²/2)||g||²`.

Thus a descent step is guaranteed for a nonzero gradient if `0<η<2a/(Lb²)`. This is a local update guarantee under the stated global smoothness bound, not a convergence guarantee for arbitrary meta-learned networks, stochastic gradients or unknown L. On tiny quadratics L is known; on general neural tasks the controller is bounded for stability but this numerical threshold must not be advertised as certified. Gradient clipping, momentum and stochasticity require separate reasoning.

## 3. Predictive variance in a finite world mixture

For normalized `π_k≥0`, component means `μ_k` and covariance `Σ_k`,

`μ̄=Σ_k π_k μ_k`,

`Cov(Y)=Σ_k π_k Σ_k + Σ_k π_k(μ_k−μ̄)(μ_k−μ̄)ᵀ`.

This is the law of total covariance. Calling the terms aleatoric and epistemic is a modeling interpretation: an ensemble does not automatically supply a calibrated Bayesian posterior. Test the decomposition with exact two-component examples and separately evaluate calibration. A dynamic finite ensemble is not equivalent to posterior inference in an infinite mixture model.

## 4. When quotient search preserves correctness

Let a finite group G act by automorphisms on a directed transition graph, preserving transition costs and the goal set. Orbits define quotient states. Every original path projects to an orbit path with the same edge costs. Conversely, after selecting a representative of the initial orbit, an edge from one orbit to another can be lifted from the current representative using the automorphism that relates it to an edge witness. Induction lifts a complete quotient path. Goal invariance ensures its endpoint remains a goal.

Therefore shortest-path search on the correctly constructed quotient preserves reachable goals and optimal costs under these assumptions. Store witness transforms to reconstruct a concrete path. If only state features—not transitions, constraints and goal predicates—are invariant, the result does not follow. An approximate learned embedding is insufficient for exact orbit merging. Use it for ranking only.

## 5. A rigorous expandable algebra for World-FIM∞

Let `Σ={1,…,d}`, `Σ*` the finite words including the empty word ε, and `r>0`. Define

`A_r = { x=Σ_w x_w e_w : ||x||_r=Σ_w |x_w| r^{|w|}<∞ }`.

Define concatenation product `e_u ⋆ e_v=e_{uv}` and extend bilinearly. Each coefficient has finitely many prefix/suffix decompositions. Absolute convergence and the triangle inequality give

`||x⋆y||_r ≤ Σ_{u,v}|x_u||y_v|r^{|u|+|v|} = ||x||_r ||y||_r`.

Associativity follows from word concatenation and absolute convergence. The unit is `e_ε`; for `d≥2` the algebra is generally noncommutative. This is a standard completed free/tensor-algebra-type construction, not a new family of numbers merely because the coordinates are infinite.

Let P_N keep degrees at most N. Since degrees cannot decrease under concatenation,

`P_N((P_Nx)⋆(P_Ny)) = P_N(x⋆y)`.

The truncated product `x⋆_Ny=P_N(x⋆y)` is associative on degree≤N elements: omitted high-degree terms can never contribute back to lower degrees. This property does not extend to arbitrary top-k pruning.

For `r'>r` and `x,y∈A_{r'}`,

`||x⋆y−P_N(x⋆y)||_r`
`≤ (r/r')^{N+1} ||x⋆y||_{r'}`
`≤ (r/r')^{N+1} ||x||_{r'} ||y||_{r'}`.

This is an explicit approximation bound, provided the stronger weighted norms are finite and known/bounded. Never report it as a numerical certificate for an input whose tail is unknown.

A bounded invertible degree-preserving map S with S(e_ε)=e_ε yields the transported product

`x⋆_S y=S^{-1}((Sx)⋆(Sy))`.

It remains associative and unital. A bounded positive diagonal scaling per word is a simple implementation. Because this is an algebra isomorphism, it does not establish a fundamentally new algebra; its research value would be measured representational efficiency, optimization or conditioning. Arbitrary learned structure constants would need separate constraints and proofs.

## 6. Weighted graph spectral transform

Take an incidence matrix B, nonnegative edge weights w, graph Laplacian `L=Bᵀdiag(w)B`, and positive diagonal mass M. Define the real symmetric matrix `S=M^{-1/2}LM^{-1/2}`. Its eigenvectors Q can be chosen orthonormal; with `Φ=M^{-1/2}Q`,

`ΦᵀMΦ=I`, `c=ΦᵀMf`, and `f=Φc` when all modes are retained.

Hence `fᵀMf=cᵀc`. With the first k modes, the reconstruction is the M-orthogonal projection. The transform depends on a self-adjoint finite operator; do not extend this result to arbitrary non-normal Koopman operators without additional hypotheses. In infinite dimensions a countable complete eigenbasis requires stronger spectral assumptions.

Eigenvectors are nonunique inside repeated eigenspaces. Compare invariant spectral projectors or subspaces, not arbitrary eigenvector columns; train polynomial filters where possible to avoid eigenvector-gradient singularities [D03]. An eigen-residual from an exact eigensolver is a diagnostic, not evidence that the learned operator captures the true physics.

## 7. Weak-form identification and appropriate physics

For `ẋ=Θ(x)ξ` and a smooth test function ψ vanishing at interval endpoints, integration by parts yields

`∫ ψ'(t)x(t)dt + ∫ ψ(t)Θ(x(t))ξ dt = 0`.

This motivates a weak residual that does not require directly differentiating noisy observed samples. Quadrature and smoothing still introduce errors and must be tested. Sparsity recovery depends on excitation, library specification and noise; low residual alone does not prove uniqueness.

For `q̇=v`, `v̇=−kq−cv`, define `E=(v²+kq²)/2`. Then `Ė=−cv²`. Conservation is appropriate when `c=0`; monotone dissipation is the correct structure for `c>0`. This simple counterexample should be a mandatory test against blindly imposing conservation.

## 8. Sparse multiscale cost accounting

Suppose each hierarchy level has `N_l≤N/2^l` nodes, degree at most k, fixed width h, and a constant number of local updates. The aggregation/dense-feature work is bounded by

`O(Σ_l (N_l k h + N_l h²)) = O(Nkh + Nh²)`.

This excludes hierarchy construction, sorting, routing and task-dependent depth; report them separately. Dense pooling matrices or all-pairs attention violate the assumed bound. Complexity in N does not imply actual lower wall-clock at small N or memory advantage at arbitrary h.

## 9. Verified orchestration is not self-scored intelligence

A finite-horizon policy π selects admissible operations from state `(goal,evidence,budget,capabilities)`. Optimize a development estimate of

`E[verified task score − λ measured cost − κ invalid-action penalties]`.

The verifier is external to the modifying agent. Learning a contextual bandit for one-step module selection is not equivalent to solving the sequential MDP. Repeatedly tuning on final held-out outcomes destroys their role as independent confirmation. Keep a development evaluator for selection and a separately controlled final evaluation for claims.


---

<!-- Source document: docs/ARCHITECTURE.md -->

# Architecture: one workbench, nine independently testable projects

## Status and repository decision

This is a proposed layout, not an inspection of the user's current Git repositories. Bootstrap must inventory existing work before creating or copying files. Use one new monorepo `world-series` with one installable Python package `world_series`; retain pre-existing repositories as read-only provenance sources until reviewed. Do not merge their outcome records or automatically relocate files. Nine isolated namespaces share contracts, generators and reporting, not mutable global state.

```text
world-series/
  AGENTS.md
  .cursor/rules/
  pyproject.toml
  dependency-lock-file
  src/world_series/
    __init__.py
    __main__.py
    cli.py
    core/
      contracts.py
      budgets.py
      devices.py
      seeds.py
      artifacts.py
      registry.py
      protocols.py
    data/
      families.py
      generators.py
      splits.py
      provenance.py
    evaluation/
      runner.py
      metrics.py
      uncertainty.py
      cost.py
      reports.py
    qlearn/ qapen/ qwipii/ wcode/ wfim/ wft/ wpinn/ cwlnn/ ultron/
  configs/{project}/{smoke,dev,ablation}.yaml
  tests/{core,qlearn,qapen,qwipii,wcode,wfim,wft,wpinn,cwlnn,ultron}/
  docs/projects/
  tasks/tasks.json
  sources/references.json
  experiments/registry.json
  runs/{run_id}/{manifest.json,events.jsonl,metrics.json,artifacts/}
  demos/
  tools/
```

The final holdout and its evaluation runner live outside the development-agent workspace. The repository may contain a public evaluation API and toy fixtures, not sealed answers. A path exclusion alone does not seal data.

## Minimal dependency policy

Use Python 3.11 or 3.12 after checking the available environment; select one and lock it. Use NumPy, SciPy and PyTorch for numerical work, pytest and Hypothesis for tests, Ruff and a type checker for development, and a YAML parser for static configuration. SymPy is optional for exact symbolic checks, not a prerequisite for every module. Start with explicit dataclasses and argparse; do not spend the sprint building a generic workflow framework. Use standard-library graph adjacency structures first; large graph frameworks, Ray, Kubernetes and cloud schedulers are unnecessary for the reference workbench.

Resolve actual compatible dependency versions in CORE-01 and save the lock. The documentation links to a current PyTorch documentation version; this is not a claim that that version is installed or supports every target device. Keep a pure CPU mathematical reference. Document any MPS/CUDA fallbacks rather than silently changing the evaluated system. See [D02–D05].

## Typed boundaries

`TaskSpec`: project ID, task family, public inputs, resource contract, development split ID and objective. It must not contain inaccessible evaluation answers.

`ObservationBatch`: named arrays/tensors, masks, shape metadata and source IDs. No positional tensor guessing between modules.

`ModuleRequest`: request ID, operation, input artifact references, immutable config hash, budget allocation and allowed output types.

`ModuleResult`: status, typed output artifacts, measured cost, diagnostics and verification status. Failure is a first-class value with an error code.

`ArtifactRef`: local relative path, SHA-256, producer run ID, schema version and media/type label. Resolve paths beneath the designated artifact root and reject traversal.

`EvidenceRecord`: claim ID, protocol ID, input/run hashes, metric name, raw trial references, verifier result and limitations. Agent prose is not evidence.

`Budget`: maximum training steps, wall-clock allowance, simulator calls, candidate evaluations, artifact bytes and planned memory. Hard safety requires OS/container enforcement; Python estimates are advisory. Never assert a universal laptop-memory guarantee from a polling monitor.

## Interfaces: do not force a universal forward method

Use specialized protocols: `Learner.fit_task`, `WorldModel.predict`, `InvariantEngine.propose/verify`, `ProgramSearch.solve`, `Algebra.multiply`, `SpectralTransform.encode/decode`, `LawIdentifier.fit`, `Backbone.forward`, `Orchestrator.run`. Each adapter converts a shared ModuleRequest into a project-specific request. Require round-trip serialization and explicit version checks. A PINN and a program synthesizer should not pretend to accept the same tensor just to make an architecture diagram uniform.

## Dependency graph

All nine depend on core contracts and generators. No standalone training experiment depends on the other eight implementations. Optional integration dependencies are:

```text
wfim -> wft: structured coefficient experiment, later and optional
qwipii -> wpinn: verified applicable invariance constraints
wft -> wpinn: optional spectral features/operator estimates
cwlnn -> wcode or qapen: optional encoder swap, after standalone controls
qlearn -> selected model trainers: optional controller swap
all implemented adapters -> ultron: routing, not joint end-to-end training
```

The v0.1 Ultron demo may use three real capabilities. It must report which capabilities are not implemented; it must not call dummy versions of all eight and count them as integrated research.

## Experiment API

Target commands to implement, not commands that exist in this planning package:

```bash
python -m world_series doctor
python -m world_series validate-config configs/qlearn/smoke.yaml
python -m world_series run --config configs/qlearn/smoke.yaml
python -m world_series compare --protocol experiments/registry.json --split dev
python -m world_series report --run-id REAL_RUN_ID
python -m pytest tests/core tests/qlearn -q
```

`run` creates an immutable run directory after validation, stores environment/config/input hashes, and writes crash or interruption receipts. `compare` never selects the best test seed. `report` reads artifacts, never asks a language model to invent missing numbers. A manifest's `git_head` is nullable; a content hash is not a Git commit.

## Ownership and integration

One integrator owns `core`, schemas, config conventions, dependency locks and shared CI. Module implementers own only their namespace, tests and configs. A module interface change needs a small contract change request with migration tests, not simultaneous edits by every agent. Worktrees may separate concurrent editing, but all numerical runs share one resource queue by default. Shared file ownership is more important than maximizing agent count.

CI stages: syntax/lint/type checks; core property tests; nine tiny CPU smoke suites; schema/evidence integrity; selected integration smoke. Longer training runs are explicit development jobs, never an accidental pull-request default. A study can be software-correct and scientifically negative.


---

<!-- Source document: docs/EXPERIMENT_PROTOCOL.md -->

# Experimental protocol and claim policy

## Three separate questions

1. Does the implementation match the proposed mechanism?
2. Does that mechanism improve the preregistered task under matched resources?
3. How broadly does the result generalize?

A passing test addresses the first question. A benchmark addresses a specified part of the second. Neither automatically answers the third. No statement of universal learning, quantum advantage, infinite execution, P=NP or ASI is an admissible v0.1 result.

## Preserve study identities

The archived `PEN_SOURCE_IDENTITY_RECONCILIATION_2026-09-18.md` defines APEN as the family and PEN as a fixed precursor. It preserves mixed/negative memory evidence and prohibits rescue tuning under the historical identity. Keep that identity immutable. World Series uses `WS-{PROJECT}-20260922-v0.1-dev` for development proposals and a separately frozen confirmation protocol. Do not reuse visible historical outcome packets as blind confirmation. The new World-FIM algebra study is distinct from Fabric-Induced Memory.

## Split unit and leakage control

Split by generative task family or source object, not by adjacent rows. MALIS: separate whole optimizee/task distributions. Q-APEN: separate complete streams, regime schedules and parameter draws. QWIPII: split canonical problem orbits so equivalent transforms cannot straddle train and test. WCode: split source program families after normalization, not examples from one program. WFIM: split compositional templates and lengths. WFT/CWLNN: split graph instances, generator parameters and selected graph sizes. WPINN: split initial conditions, trajectories and physical parameters. Ultron: split full research tasks and templates.

Training data fits parameters. Development data chooses architecture and hyperparameters. A protected confirmation set is generated/committed by an evaluator outside the development agent after the protocol is frozen; its seed/answers are not in agent prompts. Record its manifest hash. Evaluate a frozen candidate and baselines once per declared protocol. Any post-confirmation revision is a new study version, not a silent retry. Do not promise secrecy if the same agent can read the evaluator's filesystem.

## What is frozen before confirmation

Record the exact code/config/environment hashes, task generator, inclusion/exclusion criteria, primary metric, effect direction, practical effect threshold, seeds, sample size, failure handling, compute accounting, baseline tuning budget, stopping rule, uncertainty procedure and claim wording. Do not select a practical threshold after viewing confirmation effects. Until these are specified the registry status is `DRAFT_NOT_AUTHORIZED`, not preregistered.

Initial development plan: three paired seeds for debugging, then five or more paired runs over multiple independent task instances if resources permit. These are planning defaults, not a promise that five seeds yields adequate power. Use development variance to design a feasible confirmation sample size. Report noisy or underpowered outcomes as inconclusive. Family diversity often matters more than many seeds of one task.

## Comparators and resources

Use one matched simple baseline, one nearest mechanism baseline and one ablation as the minimum. Share input information, data splits, stopping budgets and tuning opportunities. Include all candidate overhead: graph construction, search, gating, simulator birth/warmup, verification and preprocessing. Separate one-time meta-training/pretraining from per-task inference or adaptation. Report amortization assumptions and break-even task count rather than pretending pretraining was free.

Resource equality can mean different things. Predefine the primary comparison: wall-clock on identical hardware, simulator calls, candidate evaluations, or training FLOPs estimated by a stated method. Report secondary comparisons rather than choosing whichever budget makes the candidate look best. Equal parameters alone is not equal compute. Timeout/divergence counts must remain in the denominator.

## Statistics

Use paired differences on the same tasks/seeds. For heterogeneous families report family-level effects and an aggregate with a documented weighting. Bootstrap at the independent task/trajectory level, nesting seed resampling only where justified; do not treat 1,000 correlated timesteps as 1,000 independent trials. Report intervals, all raw trial summaries, medians and failures. For suites, robust aggregate summaries can supplement—not replace—per-family outcomes [R40]. Avoid a single best-seed chart.

A proposed development promotion rule is: no correctness regression; practical improvement over the strongest eligible matched baseline; and an uncertainty interval consistent with the declared effect. This is a policy to freeze before confirmation, not a universal significance recipe. Nine projects and many endpoints create multiplicity: identify nine primaries in advance, distinguish exploratory results, and use an explicitly chosen correction or avoid joint significance claims.

## Mechanism ablations

Remove only the claimed mechanism while keeping information access and reasonable model capacity comparable. Replace learned memory writes with random/recent writes; replace adaptive worlds with fixed ensembles; replace verified quotienting with ranking-only; compare learned algebra transport to the identical fixed algebra; remove spectral constraints individually; compare learned routing with fixed routing. Do not compare the full model against an intentionally crippled straw man.

## Evidence states

`SPECIFIED`: design and tests written, no implementation implied.
`IMPLEMENTED`: code path exists and has been reviewed.
`SMOKE_PASSED`: tiny correctness/plumbing checks actually executed.
`BENCHMARKED`: matched declared comparisons actually executed.
`SUPPORTED`, `NOT_SUPPORTED`, `INCONCLUSIVE`: bounded interpretation of a frozen primary result.
`BLOCKED`, `NOT_RUN`, `INVALIDATED`: explicit absence/failure/protocol violation.

Each claim links to immutable raw evidence and a specific scope. A software build may pass with `NOT_SUPPORTED`. Never make CI demand a positive research finding. Publication readiness also needs independent review, literature coverage, reproducibility, licenses and truthful reporting; a Sunday demo does not establish all of these.


---

<!-- Source document: docs/RESOURCE_AND_SECURITY.md -->

# Resource, execution and evaluation boundaries

All numerical sizes in this pack are proposed starting configurations, not measured performance estimates. Default to one numerical training worker, tiny CPU smoke tests, no paid APIs and no dependency on a cluster. Confirm actual RAM, disk, device and available libraries in CORE-01. Do not infer installed hardware from project aspirations.

Suggested smoke ceilings: 64–256 samples, 16–32 inner learning steps, graphs with 32–128 nodes, eight active world experts, 128 memory entries, DSL depth six, algebra degree six. Larger configurations require an explicit budget record. Refuse allocations beyond maximum node/term/candidate count before constructing dense tensors. Resource checks must include adapters and evaluation, not just model forward passes.

Record measured elapsed time, peak process memory where supported, backend/dtype, candidate calls and failure reason. Cooperative Python budgets cannot forcibly contain all native-library allocations; use process/container limits for owned jobs where available. Do not kill other applications, lower system safety limits, or set unsafe accelerator memory variables.

Use a typed total DSL interpreter for synthesis. Validate the AST, operator whitelist, types, lengths and fuel before execution. A safe interpreter contains no file/network/subprocess capability. Do not use Python eval/exec as its implementation. General code execution, if added later, needs a hardened disposable container or equivalent, read-only inputs, no secrets, no host mounts, no network, limited process count and memory/time limits. Host subprocess timeouts are not sufficient isolation.

Keep the final evaluator outside the development workspace, with read-only candidate access and separately controlled input visibility. Do not let Ultron edit evaluator code, scoring functions or the claim ledger's approved thresholds. Agent rules improve behavior but do not enforce access control [D01]. Store secrets outside the repository and do not give research agents production credentials.

Ultron v0.1 executes pre-approved registered operations. Self-modification, external deployment, outreach and live trading are out of scope. Proposed edits in a later phase are reviewed as patches; they are never merged because the agent says its own test passed. Repeated validation selection is development, not fresh blind confirmation.

On exhaustion or dependency failure, emit a failure artifact and stop that task. A missing module returns UNSUPPORTED_CAPABILITY, not a mock success. Continue independent tasks only when their own prerequisites and budgets are satisfied.


---

<!-- Source document: docs/projects/01_qlearn.md -->

# 01 — Quantum Learning / MALIS
## Working research title
Bounded Meta-Learned Update Policies for Resource-Aware Adaptation.

The project studies classical learning algorithms. “Quantum Learning” is a brand, not a claim about qubits, quantum speedup, subjective awareness or metacognition. The eventual ambition is a controller that adapts optimization, curriculum, memory and computation. The first experiment isolates optimization; adding all those mechanisms at once would obscure attribution.

## Related work and the exact gap to test

Learned optimizers [R01], meta-learned initializations [R02], Celo [R03], Celo2 [R04] and ELO [R05] cover substantial parts of the original idea. In particular transfer and long-horizon stability are already active research targets. Our candidate question is narrower: can a bounded controller conditioned on task progress and remaining budget improve a predeclared compute-normalized objective across held-out optimizee families? This is a hypothesis, not an established novel result. Celo2 and ELO deserve stronger-comparator evaluation beyond the demonstration phase.

## Mathematical definition

For task τ, support data Sτ fits the optimizee and query data Qτ scores adaptation. Let θ_t be functional optimizee parameters, g_t a support gradient and m_t a momentum feature. A shared controller maps per-parameter and per-layer normalized features into positive diagonal gates and a bounded step size:

`(η_t,D_t,h_{t+1}) = π_φ(features(g_t,m_t,loss_progress,budget),h_t)`

`θ_{t+1}=θ_t−η_t D_t g_t`.

Enforce `η_min≤η_t≤η_max` and `a≤diag(D_t)≤b` with smooth parameterizations. Initialize near a stable fixed rule. Controller features never contain query labels or future losses. The outer loss may use query losses because it is the meta-training objective, but that is not information available to the controller at inference.

Proposed outer objective:

`J(φ)=E_τ[Σ_t ω_t normalized_query_loss(θ_t) + λ_cost C(τ) + λ_fail 1[diverged]]`.

Normalize by a fixed task scale or initial loss plus ε, not by the candidate's best outcome. Discrete failure penalties are diagnostics/selection signals unless an explicitly documented gradient estimator handles them. Do not pretend a Boolean divergence penalty supplies useful differentiable gradients.

The conditional descent inequality in MATH_FOUNDATIONS.md applies to known L-smooth objectives with a bounded positive preconditioner. Use it as a theorem-backed quadratic sanity check. It is not a safety proof for arbitrary neural training, momentum, stochastic gradients or unknown curvature.

## Data and first experiment

Generate positive-definite quadratics with controlled condition numbers and task-specific minimizers. Then add small linear regression and two-layer MLP regression tasks. Split entire distributions: hold out condition-number ranges, function families and model widths. Begin with batch four tasks, controller hidden width 32, 16 unrolled steps and optimizee width 64. These are resource caps, not tuned results. Evaluate horizon 32 or 64 only after the 16-step loop is sound.

A task object returns support/query batches independently and a task_id. It exposes analytic curvature only to the oracle baseline and reference tests, never covertly to the learned controller. Use separate result labels for oracle-information controls.

## Contracts and tensors

`OptimizeeSpec.build(seed) -> parameter_dict, buffer_dict`.
`FunctionalOptimizee.loss(params, buffers, batch) -> scalar`.
`FeatureBuilder.build(params, grads, state, budget) -> features[P,F]`.
`UpdatePolicy.forward(features[P,F], state[P,H]) -> gates[P], step_sizes[layer], new_state`.
`InnerLoop.unroll(task, policy, steps) -> Trajectory`.
`MetaTrainer.step(tasks) -> MetaMetrics`.

P is flattened parameter count. A metadata table maps slices back to named shapes; assert exact round trips. No shared controller state across independent tasks. All learned-policy parameters must receive finite gradients in a tiny diagnostic problem. Use `torch.func.functional_call` to evaluate parameter dictionaries [D02].

## Files and implementation units

| File under src/world_series/qlearn | Responsibility |
|---|---|
| tasks.py | Quadratic/regression task generation, family splits and oracle flags |
| functional.py | Parameter flatten/unflatten and functional loss evaluation |
| features.py | Stable gradient/momentum/budget features with explicit detach policy |
| policy.py | Bounded positive gates, controller state and reset |
| unroll.py | Exact short differentiable inner loop; separate named truncated mode |
| meta_train.py | Outer objective, finite-gradient checks and checkpointing |
| baselines.py | Tuned SGD, momentum, AdamW, fixed schedule and small learned control |
| evaluate.py | Loss-versus-compute, divergence and longer-horizon evaluation |
| adapter.py | Capability `adapt_learner` returning checkpoint and evidence |

Implement the exact tiny loop first. Use `autograd.grad(create_graph=True)` for the reference meta-gradient. Do not mutate `.data`, call an ordinary in-place optimizer inside the differentiable loop, or detach the update graph accidentally. Full-gradient finite-difference checks require matching analytic dependencies; a deliberately first-order/stop-gradient mode must have its own name and tests. Truncated backpropagation introduces bias and must not be represented as an exact full-horizon meta-gradient.

## Reference algorithm

```text
for task in independent_meta_batch:
    params, buffers = initialize_optimizee(task.seed)
    policy_state = zeros_for_this_task()
    for step in range(unroll_steps):
        support_loss = functional_loss(params, buffers, task.support(step))
        grads = differentiable_gradient(support_loss, params)
        features = build_features(grads, history, remaining_budget)
        params, policy_state = bounded_update(params, grads, features, policy_state)
        outer_terms.append(query_loss(params, task.query(step)))
    record instability without discarding the task
backpropagate declared outer objective into controller parameters
```

## Baselines and ablations

Minimum controls: tuned fixed-step SGD, momentum SGD, AdamW with a matched tuning budget, and a small learned update policy without task/budget features. An initialization-only meta-learning control is meaningful on the same adaptation task, but do not force it into incomparable optimizer-only settings. Ablate budget features, gate learning, recurrence and task augmentation separately. Later evaluate a faithful Celo2/ELO implementation through a separate runner with its dependency/license records; a simplified substitute must not inherit their names.

Primary development endpoint: area under normalized validation-loss-versus-measured-compute curve, lower is better. Also report final loss, divergence fraction, adaptation time, peak memory and amortized meta-training cost. Select an interpretable practical effect threshold before final confirmation; it is intentionally not fabricated here.

## Required tests and completion gates

Reference tests: analytic quadratic gradient; flatten/unflatten identity; conditional descent when assumptions hold; finite-difference check of one outer parameter in CPU float64. Candidate tests: bounds always respected; task states reset; query labels inaccessible to policy; nonzero finite outer gradients; checkpoint reload matches the same next update; budget exhaustion stops deterministically. Include a deliberately unstable large-step control so the divergence detector is genuinely exercised.

The smoke suite may use two tasks and four steps. Passing means the implementation works, not that MALIS beats AdamW. Mechanism benchmarking requires the same tasks, tuning policy and compute counters for all comparators. An unsuccessful controller remains a valid `NOT_SUPPORTED` result.

## Sunday slice and deferred work

Demonstrate learning-policy adaptation on tiny tasks with a baseline trace and actual run manifest. Present a held-out example only from the authorized demonstration split. Defer curriculum selection, dynamic architecture surgery, optimizer mutation, memory policies, arbitrary LLM training and meta-meta control. These become separately versioned hypotheses after the bounded update-policy study is interpretable.


---

<!-- Source document: docs/projects/02_qapen.md -->

# 02 — Q-APEN
## Working research title
Adaptive Quantized World Ensembles with Delayed-Utility Engram Memory.

Use Q-APEN as the World Series successor label, with WAPEN as an optional alias only if the project owner confirms they are the same study. Do not invent a new expansion for APEN that overrides its existing family specification. Preserve PEN as a fixed historical precursor. This project has finite execution and resource caps even when its conceptual model family is extensible.

## Prior work and lineage

VQ representations [R06], probabilistic ensembles/planning [R07] and world-model imagination [R08] are established. The private PEN reconciliation requires preserving mixed/negative memory outcomes and testing adaptive mechanisms against appropriate fixed controls. The research proposal is a jointly measured lifecycle for model capacity and explicit memories under returning regimes, not merely a larger ensemble or a new codebook.

New protocol IDs and fresh synthetic streams are mandatory. Do not tune the historical PEN experiment, change its frozen seeds, or import its outcome numbers into these results. A legacy adapter is optional and blocked until its source identity and read-only use are verified.

## Model definition

Encode observations `h_t=E(o_≤t)` and quantize through a learned codebook `z_t=argmin_j ||h_t−c_j||²`. Keep a continuous residual feature to avoid forcing all dynamics through a lossy discrete index. Pretrain/freeze the codebook for the first lifecycle experiment; joint online codebook drift can otherwise make memory keys incomparable across time.

For active expert set A_t, predict a finite mixture:

`p(y_{t+1}|h_t,a_t)=Σ_{k∈A_t} π_{k,t} N(μ_k(h_t,a_t),Σ_k(h_t,a_t))`.

Use normalized routing weights and positive variance floors. Decompose predictive variance with the total-covariance formula from MATH_FOUNDATIONS.md. Disagreement is a useful feature, not automatically calibrated epistemic uncertainty.

Engrams store a key, compressed value, originating regime/expert ID, write time, access statistics and a delayed-utility estimate. Utility is estimated from subsequent development-stream prediction changes, not only immediate salience or training reconstruction. Each intervention uses a defined ablation/replay protocol so “memory helps” is supported by outcomes, not activation counts.

## Lifecycle and causal order

Use a finite state machine: NEW → WARMUP → ACTIVE → SLEEPING → REVIVED, with separate PRUNED archives. Stable UUIDs identify experts. Spawning requires sustained pre-update surprise and a cooldown, not one noisy point. Warm a candidate using a bounded replay window and assess it on subsequent stream blocks. A newly fitted expert cannot claim success on the same label that triggered its creation.

Crucial evaluation order: predict, log predictive distribution and memory state, observe target, score, then update gates/experts/memory. Future observations and true regime labels are unavailable to the learner. Truth labels may be used only in the evaluator to diagnose shift lag and regime recurrence.

Proposed caps: at most eight active experts, 32 archived identities, 128 engrams, codebook 64, latent width 16, rollout horizon 16 and 64 rollout calls. These are starting limits. Every warmup, routing decision, retrieval, merge check and simulation counts toward cost.

## Contracts

`WorldExpert.predict(features[B,D], action[B,A]) -> mean[B,O], logvar[B,O]`.
`WorldBank.route(features) -> expert_ids[K], weights[B,K]`.
`LifecyclePolicy.observe(scored_event) -> LifecycleDecision`.
`EngramStore.write/retrieve/consolidate -> typed records`.
`StreamEvaluator.step(observation, optional_action) -> prequential receipt`.

Use `nn.ModuleDict` keyed by stable IDs; maintain optimizer groups/state when experts appear or sleep. Do not index mutable experts only by list position. Serialize dormant weights and memory references together. A bounded graph of expert similarities may support transfer later, but is disabled in the first lifecycle comparison to avoid collapsing ensemble diversity.

## Code units

| File | Main responsibility |
|---|---|
| streams.py | Switching linear systems, delayed cues and recurrent regime schedules |
| quantizer.py | Codebook fitting, commitment loss, distortion and code usage |
| expert.py | Small probabilistic predictors with variance floors |
| mixture.py | Routing, predictive moments and scoring |
| engrams.py | Fixed-capacity trace storage, retrieval, forgetting and utility receipts |
| lifecycle.py | Birth/sleep/revive policy with cooldowns and explicit cost |
| bank.py | UUID registry, optimizers and checkpoint round trips |
| baselines.py | Fixed ensembles and memory-write controls |
| evaluate.py | Prequential metrics, calibration and regime diagnostics |
| adapter.py | `predict_worlds` capability, not arbitrary external actions |

## First benchmark

Generate streams from several stable linear state-space systems with noisy observations. Insert delayed cues that help identify a later regime and repeat earlier regimes after long gaps. Vary observation noise independently of regime shifts so spawning on noise is penalized. Keep an easier no-shift negative control: adaptive growth should not be necessary there.

Compare against one probabilistic model, a fixed ensemble, a rolling/replay-only ensemble, dynamic experts without memory, fixed experts with memory, random-write engrams and an attention/recent-history replacement. Match either total measured time or total training/prediction calls as the declared primary resource. Report parameter-matched and active-compute-matched comparisons separately; they answer different questions.

Primary proposal: prequential negative log likelihood at fixed total cost. Secondary: rollout error, calibration, shift recovery delay, expert count, false spawns, memory retrieval precision and measured delayed utility. Finance is not needed for this mechanism test. Any later financial benchmark needs a separate chronological/leakage/cost protocol, not a profitable-trading claim from these synthetic streams.

## Tests

Exact mixture moments for two known Gaussians; weights sum to one; variances positive; no target accessed before prediction; no missing/duplicated optimizer state after spawn; revive preserves archived identity; codebook freeze preserves old keys; memory cap enforced before writes; cooldown prevents repeated spawning; deterministic stream replay; ablations truly disable the named feature.

Behavioral test: a controlled returning regime should produce an observable lifecycle event, even if it does not improve the primary metric. Separate this mechanism activation check from the benchmark claim. Mock lifecycle scripts belong only in unit tests, never in claimed learned results.

## Infinite-model interpretation and scope boundary

A countably infinite mixture or stick-breaking prior may be a later mathematical model, but threshold spawning is not posterior inference under that prior. Do not include an infinite sum in the paper and label a capped heuristic implementation as an exact realization. Sunday needs a truthful finite demonstration: the active expert population changes under a measured budget and its effect is compared to fixed controls. Merge policies, graph knowledge transfer and nonparametric inference are later hypotheses.


---

<!-- Source document: docs/projects/03_qwipii.md -->

# 03 — QWIPII
## Canonical project name
Quantized World Renormalized Invariant Projective Inductive Intelligence.

The first implementation is a verified invariant-guided reasoner. The name is an ambition map, not evidence that quantization, renormalization, projective geometry and Olympiad-level induction have all been solved. Keep exact symbolic objects separate from optional learned representations.

## Related work

G-CNNs formalize equivariance [R09]; LieGAN and later symmetry-discovery methods already learn transformations [R10–R11]; information-based RG work studies coarse-graining [R12]; AlphaGeometry demonstrates neural-symbolic geometry reasoning [R13]. The proposed distinction is a verification gate between discovered transformations and correctness-critical search reductions. Whether the particular implementation is novel requires further comparison, not an acronym.

## Two lanes: proposing versus certifying

A discovery model proposes candidate invariants or transformations from a bounded grammar. A verifier determines the permitted use. Labels are `PROPOSED`, `EMPIRICALLY_SUPPORTED`, `EXACTLY_VERIFIED_WITHIN_DOMAIN`, or `REJECTED`. Only exact verified automorphisms may merge search states. Approximate invariants may rank candidates or suggest lemmas; they cannot erase possibilities.

For a group action `g·x`, invariance means `I(g·x)=I(x)`; equivariance means `E(g·x)=ρ(g)E(x)`. Encode both domain and codomain actions. A constant embedding is invariant but useless, so training also needs non-collapse and task-usefulness checks. Invariant loss alone is not a sufficient objective.

## Exact quotient search

Begin with a finite puzzle domain such as token transformations on a ring. Define full problem states including constraints and goal predicates. Use a finite candidate group (e.g. dihedral permutations) only when it preserves legal transitions, costs and the goal set. If a specific target breaks symmetry, use its stabilizer or transform the entire problem consistently; do not quotient only the board while keeping an incompatible goal fixed.

Canonicalization:

`can(s)=min_{g∈G} serialize(g·s)`.

Store the minimizing witness g. A quotient edge stores a concrete legal transition and witness transformations so the returned solution can be lifted back to the original state. MATH_FOUNDATIONS.md states the assumptions needed to preserve reachability and shortest-path costs. Exhaustively test them on all small instances before introducing a learned ranker.

## Projective slice

Implement one-dimensional projective transformations with exact rational arithmetic:

`T(x)=(a x+b)/(c x+d)`, with `ad−bc≠0` and defined denominators.

For four distinct admissible points, test the cross-ratio

`CR(a,b;c,d)=((a−c)(b−d))/((a−d)(b−c))`.

The same argument names should not be confused with the matrix entries in code; use distinct identifiers. Verify invariance using symbolic/rational arithmetic and explicit pole checks. Either implement the projective point at infinity correctly or reject it; never divide through a zero denominator and report a generic numerical failure. This is a compact proof-backed demo, not a general projective geometry theorem prover.

## Coarse-graining slice

Optional `R_l` maps fine symbolic features to a coarser representation. Test consistency `R_lρ_l(g)≈ρ_{l+1}(g)R_l`. This is an equivariant coarse-graining constraint. Call it that, not a fully established renormalization flow with fixed points/exponents unless those objects are defined and analyzed. Quantization may be added to learned representations but must not alter exact proof certificates silently.

## Code units

| File | Responsibility |
|---|---|
| domains.py | Finite transition systems, legal moves, goals and costs |
| group_actions.py | Exact finite actions, composition, inverses and domain checks |
| invariant_grammar.py | Parity, modular residues, bounded polynomial/permutation candidates |
| discovery.py | Candidate scoring/training on development problems |
| verifier.py | Exhaustive finite-domain checks and rational projective identities |
| canonicalize.py | Orbit representative and witness transforms |
| search.py | Brute BFS, quotient BFS and ranking-only variants |
| certificates.py | Replayable proof/path certificates |
| projective.py | Rational Möbius transforms and cross-ratios |
| adapter.py | `solve_invariant_problem` and `verify_certificate` capabilities |

`Transformation.apply(problem_state) -> state`; `verify_automorphism(domain, transformation) -> certificate`; `Search.solve(problem,budget) -> path_certificate`. A certificate includes domain version, assumptions, checked property, witness and verification method. “Verified” must name the finite domain or theorem actually covered.

## First learning experiment

Generate training problems from several known families and ask a small ranker to choose candidate invariants or group generators. Discovery is selection within a declared grammar, not arbitrary invention of all mathematical concepts. Split by canonical problem orbit and generator family to avoid transformed duplicates crossing the boundary. Compare brute search; exact hand-specified quotient search; learned ranking with no pruning; learned proposal plus verification; and oracle symmetry selection. The oracle is an upper-bound diagnostic with additional information, not a standard fair baseline.

Primary: verified solved fraction under a fixed expansion/time budget. Secondary: expansions including discovery/verification overhead, certificate length, rejected invariant count and performance under held-out admissible transformations. Also run fixed-success comparisons of cost conditional on a common solved subset, clearly labeled to avoid selection bias.

## Tests and adversarial cases

Test group identity/composition/inverses; canonicalization idempotence; exact orbit equivalence; all legal transitions remain legal; goal/cost preservation; path lifting and replay; agreement with exhaustive BFS on every small state; invalid proposed symmetry rejected; constant invariant cannot trigger pruning; rational cross-ratio preservation; singular transform and pole errors; budget abort preserves partial evidence.

A deliberate false transformation that matches a few samples but fails one state is mandatory. The test should show it may remain a heuristic suggestion but cannot enter the quotient verifier's trusted registry. Avoid assigning a theorem-proved label to a neural score.

## Sunday slice and future scope

Show one proof-preserving search reduction and one projective-invariance identity with actual certificates. Neural discovery can be a development add-on after exact infrastructure passes. Broad Olympiad benchmarks, theorem-library mining, Lie-group discovery outside the grammar and formal Lean integration are later versions. A synthetic puzzle result must not be advertised as general Olympiad ability.


---

<!-- Source document: docs/projects/04_wcode.md -->

# 04 — World-CNN Code
## Working research title
Relational Hierarchical Program Encoding for Verifier-Guided Bounded Synthesis.

The first deliverable is a coding research experiment, not a production coding agent and not a P-versus-NP result. A complete bounded language lets us measure correctness and search cost before trusting generated host code.

## Prior art and hypothesis

Program graphs already encode structural and semantic relations [R14]. DreamCoder learns programs and reusable abstractions [R15]. FunSearch's laboratory explanation illustrates evaluator-driven program search [R16]. Our candidate hypothesis is that a particular hierarchical relational encoder ranks localized candidates more efficiently than nonrelational encoders under the same enumerator and verifier. A speedup could be distribution-specific and does not imply a worst-case polynomial-time algorithm.

## Typed language and safety boundary

Start with scalar integers, booleans and bounded lists of integers. Whitelist arithmetic, comparisons, conditionals and a few total list operators such as sum, reverse, take, map with a bounded body and filter with a bounded predicate. Define overflow or arbitrary-precision behavior explicitly. No file operations, imports, network, shell, recursion or unbounded loops. Every interpretation receives fuel, maximum list length and a typed AST depth/node cap.

The interpreter must dispatch on typed AST constructors. Do not implement it using Python eval/exec. A timeout around arbitrary Python is not equivalent to a safe interpreter. Invalid types, division by zero, excessive integer size, exhausted fuel and malformed trees produce typed failures. General Python patching requires a later sandboxed runner and is not necessary for this study.

## Representation and candidate search

For program P, build a directed relational graph with AST child/parent, sibling order and permitted scope/use relations. Only claim data/control-flow edges actually defined by the DSL; do not label a simple AST as a full compiler representation. Node features include operator type, value category, scope/depth and type information. Relations have separate learned weights:

`h_v^{l+1}=σ(W_0h_v^l+Σ_r Σ_{u∈N_r(v)} W_rh_u^l/c_{v,r})`.

Pool expressions to blocks/root using sparse parent mappings. A scorer conditions on the task's public examples and returns candidate priority. It may guide beam order but cannot declare correctness. For an exhaustive bounded reference mode, ranking must not remove candidates needed for completeness. For beam search, explicitly acknowledge search incompleteness.

Use a common candidate generator across all encoder comparisons. Otherwise gains may come from proposing better programs, not from the claimed graph representation. Cache immutable AST/graph features by a canonical hash; invalidate any cache when a subtree changes.

## Correctness before efficiency

Use lexicographic selection: first satisfy the declared verification contract, then optimize cost/length. Public examples guide search. A separate verifier evaluates withheld inputs, or exhaustive finite inputs when the domain is small enough. Passing examples does not prove universal correctness. Record the exact scope: `EXHAUSTIVE_FINITE_DOMAIN`, `HELDOUT_TESTS`, or a later formal equivalence certificate.

Runtime objectives should use deterministic interpreter operations/fuel initially; very short wall-clock timing is noisy. Count parsing, graph construction, ranking, interpretation and verification. Do not reward a candidate for skipping cases or changing its own test harness. A cost penalty must never outweigh a correctness failure and make an incorrect program look better.

## Code units and shapes

| File | Responsibility |
|---|---|
| dsl.py | Frozen typed AST grammar and total semantics |
| interpreter.py | Whitelist evaluation with fuel/size limits |
| dataset.py | Target programs, public examples and source-family splits |
| graph.py | Node/edge extraction and canonical AST hashing |
| encoder.py | Relational convolution and sparse hierarchical pooling |
| search.py | Enumerative, beam and evolutionary-style bounded search |
| verifier.py | Separate finite-domain/test evaluator |
| baselines.py | Uniform/heuristic priority, token encoder and MLP encoders |
| evaluate.py | Correctness, searched candidates and total measured cost |
| adapter.py | `synthesize_dsl_program` capability |

`ProgramGraph` has node features `[V,F]`, edge index `[2,E]`, relation IDs `[E]`, parent indices `[V]` and masks. `SynthesisTask` includes input/output types and public examples, never verifier answers. `SearchResult` stores the AST, evidence ID, completeness mode and resource receipt.

## Data and leakage controls

Generate target programs with depth at most six and initially at most 64 AST nodes. Normalize commutative forms, variable names and exact syntactic identities before source-family splitting. Train and test cannot share the same target program merely with different input/output examples. Hold out operator compositions or depth ranges for transfer tests, but distinguish an unsupported grammar from failure inside the supported grammar.

Train the scorer on bounded search traces collected on development tasks. Label candidates by actual verifier progress/correctness within the development partition; do not train on final evaluation answers. Preserve unsuccessful traces so the learner sees realistic negative candidates instead of an artificially easy success-only distribution.

## Baselines and ablations

Use uniform enumeration, hand-coded length/type ordering, token-sequence encoding, graph encoding without semantic relations, and the proposed multiscale graph encoding. Keep candidate generation, examples, verifier and budget fixed. A later library-learning baseline inspired by DreamCoder may change the language/search space and must be evaluated as a distinct experiment. An external LLM baseline is optional and requires a fixed model/version, token budget, prompt and cost accounting; do not make it necessary for the core study.

Primary: verified solve rate at a fixed candidate-evaluation budget. Secondary: correct-program search cost, interpreter cost, generalization to held-out compositions, memory and failure categories. Report all tasks, including exhausted searches. Empirical `C(n)` plots describe tested distributions, not P=NP.

## Tests and Sunday slice

Test every DSL operator and type error, fuel accounting, AST hash stability, graph edge semantics, batching consistency, exhaustive search completeness on tiny grammar, verifier isolation, adversarial attempts to exceed list/integer bounds and a candidate that memorizes public examples but fails withheld cases. Compare learned and nonlearned searches on identical generated candidate pools.

Sunday demonstration: one small synthesis problem with a replayable search trace, verified output and matched baseline. Defer unrestricted repository editing, full Python semantics, compiler optimization, general NP-hard claims and self-modifying verifier code. The architecture can later become a coding-agent component once the bounded experiment establishes a useful mechanism.


---

<!-- Source document: docs/projects/05_wfim.md -->

# 05 — World-FIM∞
## Working research title
Learnable Coordinates in Sparse Completed Word Algebras with Certified Degree Truncation.

This study is separate from the existing Fabric-Induced Memory project. The infinity symbol denotes an underlying extensible mathematical space, not infinitely many stored values. The first useful deliverable is an exact algebra library, an error-aware finite representation and a controlled learning experiment. Do not call a high-dimensional tensor a newly discovered number system without defining operations and proving the claimed properties.

## Related work and positioning

Hypercomplex parameterizations [R17], hyperdimensional computing [R18], graded/signature representations [R19] and noncommutative algebra [R20] make high-dimensional representation a crowded and mathematically mature area. The proposed numerical construction deliberately uses existing algebraic foundations. Its possible contribution is a useful learning/approximation method with explicit guarantees, not the invention of infinite dimension or an isomorphic algebra.

## Chosen algebra, not arbitrary structure constants

Let words over an alphabet Σ index basis vectors. The empty word ε is the multiplicative identity. Define weighted absolutely summable series

`x=Σ_w x_w e_w`, `||x||_r=Σ_w |x_w|r^{|w|}<∞`, `r>0`.

Set `e_u⋆e_v=e_{uv}`. This is associative concatenation and, for at least two alphabet symbols, generally noncommutative. The product obeys `||x⋆y||_r≤||x||_r||y||_r`. MATH_FOUNDATIONS.md provides a short proof and assumptions.

Do not begin with a dense learned `C_ij^k` tensor. It has problematic storage growth and provides no automatic associativity, identity or norm control. A user-defined alternative product can be a later research branch, but must state exactly which axioms it satisfies.

## Finite representation and error guarantees

Use a sparse mapping from tuples of symbol IDs to coefficients. `P_N` removes degrees above N. For concatenation,

`P_N((P_Nx)⋆(P_Ny))=P_N(x⋆y)`.

Consequently the degree-truncated algebra retains associativity. With stronger norm bounds at `r'>r`,

`||x⋆y−P_N(x⋆y)||_r ≤ (r/r')^(N+1)||x||_{r'}||y||_{r'}`.

Return a tail certificate only when the caller supplies an actually justified stronger-norm bound. A finite observed prefix does not identify the unknown infinite tail. Distinguish exact finite polynomial inputs, certified series inputs and uncertified sampled representations.

Top-k coefficient pruning is different from degree truncation and may break associativity. Keep it in a separate approximate API that reports discarded mass and propagates an error bound when enough information exists. Never silently apply it in the exact reference product. Set a maximum output-term budget and estimate it before multiplication; on exhaustion return a typed error rather than silently dropping terms.

## Learned component that preserves the algebra

Use an invertible, degree-preserving coordinate map Sθ, initially a bounded positive diagonal scaling with `Sθ(e_ε)=e_ε`. Define

`x⋆θy=Sθ^{-1}((Sθx)⋆(Sθy))`.

Associativity and the unit are preserved by transport. Enforce nonzero scale bounds to control conditioning. The resulting algebra is isomorphic to the original; this is not a claim of a mathematically new algebra. The empirical question is whether the learned coordinates help a downstream compositional task under finite budgets. Compare to the same algebra with S=I; otherwise any benefit might come entirely from the fixed concatenation representation.

A more expressive block-per-degree Sθ is deferred because inverse conditioning and dense block storage can erase the efficiency objective. Avoid pretending an arbitrary neural encoder is an invertible linear algebra isomorphism.

## Data structures and APIs

`SparseElement`: sorted tuple keys, coefficients, alphabet ID, maximum degree, coefficient type, norm metadata and optional tail certificate.

`AlgebraSpec`: alphabet size, weighting r, product kind, identity, exact/approximate mode and budget.

`multiply_exact(x,y,max_degree,max_terms) -> SparseElement`.
`truncate_degree(x,N) -> SparseElement`.
`multiply_approx(x,y,policy) -> ApproximationResult`.
`transport_product(x,y,scales) -> SparseElement`.
`certify_tail(x,y,r_prime,N) -> TailBound | Unavailable`.

Exact reference coefficients use rational arithmetic on tiny examples. Differentiable finite experiments use tensors aligned with a frozen vocabulary/index map. Never mutate sparse index order between forward and backward. An input's alphabet and algebra version must match before multiplication.

## Code units

| File | Responsibility |
|---|---|
| words.py | Canonical word keys, degree and alphabet checks |
| elements.py | Typed sparse elements and sorted serialization |
| reference.py | Rational associative multiplication and degree truncation |
| norms.py | Weighted norms and justified error certificates |
| transport.py | Bounded invertible coordinate maps and differentiable product |
| approximate.py | Explicit optional pruning with measured discarded mass |
| tasks.py | Order-sensitive compositional sequence/operator benchmarks |
| baselines.py | Fixed same-algebra, vector binding and bilinear controls |
| evaluate.py | Accuracy, stored bytes, error bounds and algebraic diagnostics |
| adapter.py | `compose_algebraic_objects` capability |

## Experiment design

First exhaustively verify algebraic operations for tiny alphabets and degrees. Then train a small classifier/regressor on ordered compositions where order matters. Hold out composition templates and lengths. Keep an identity-insensitive task as a control: a complicated noncommutative representation should not be presumed useful everywhere.

Suggested starting caps: alphabet two to four, degree at most six, at most 4,096 stored terms, reference rational degree at most three. Dense dimension grows exponentially with degree; sparse representation postpones rather than eliminates worst-case growth. Record actual occupied terms and serialized bytes, including indices and metadata—not only coefficient count.

Minimum baselines: the identical fixed concatenation algebra; an ordinary fixed-size vector encoder; a simple bilinear composition model; and an appropriate binding/HDC-inspired control. A PHM-inspired layer can be an additional comparator after a reproduction note. Match downstream decoder capacity and available sequence information. Do not compare a memory-rich representation with a tiny vector and attribute all gains to algebra.

Primary development endpoint: task accuracy/error at a fixed representation-byte cap. Secondary: multiplication time, approximation error, norm growth, generalization to longer compositions and exact algebraic property violations. Mathematical correctness does not require beating a neural baseline.

## Required tests

Unit and associativity tests on exact polynomials; degree-truncation compatibility; zero and identity; alphabet mismatch; noncommutativity witness; coefficient serialization; norm submultiplicativity; valid tail bound on a known finite series; unavailable certificate for an unknown tail; transport/inverse round trip; transported associativity; gradients for finite transport parameters; deliberate top-k associativity counterexample; preallocation budget rejection.

The approximate product must never return `EXACT` merely because its numerical error is small on one sample. Test error propagation across repeated products and record when a bound becomes too loose to be useful.

## Sunday slice and future theory

Demonstrate exact composition, degree expansion and a certificate on a known example, then a measured small task comparison if available. The strongest honest mathematics result is the implemented classical guarantee plus a new computational study. Later work may investigate different completions, task-dependent bases, stable operators or genuinely new products—but each needs its own axioms, proofs and independent usefulness test.


---

<!-- Source document: docs/projects/06_wft.md -->

# 06 — World Fourier Transform
## Working research title
Constraint-Guided Learned Graph Spectra for Transferable Signal Representation.

A Fourier-like transform requires an operator, inner product, basis and inverse. “Decompose anything” is not a complete mathematical specification. The first domain is finite weighted graphs with a self-adjoint operator; arbitrary manifolds, non-normal dynamics and universal transforms are deferred.

## Related work and corrected novelty

Graph Fourier analysis [R21] and learning Laplacians from signal data [R22] already cover learning an operator and its spectrum. FNO [R23], neural operators [R24] and DeepONet [R25] address mappings between function spaces, which is related but not identical to learning a transform. The candidate question is whether specific verified symmetry and cross-resolution constraints help an operator learned from limited/noisy signals. The constraints must demonstrate an advantage over an otherwise identical learned-Laplacian baseline.

## Operator construction

Given sparse candidate edges, orient each edge arbitrarily to form incidence matrix B. Use nonnegative trainable weights `w=softplus(a)+ε` and

`Lθ=Bᵀdiag(w)B`.

For positive diagonal mass M, define `Sθ=M^(-1/2)LθM^(-1/2)`. This is symmetric positive semidefinite. Normalize or constrain a scale statistic such as trace/total edge weight according to the declared generative model; without a scale convention, a trivial near-zero operator can minimize some smoothness losses. Do not introduce a normalization that rules out the physical operator you are trying to estimate.

Let `SθQ=QΛ`, `Φ=M^(-1/2)Q`. Encode `c=ΦᵀMf`; decode `f_hat=Φ_k c_k`. With all modes, Parseval holds in the M inner product. With k modes, reconstruction is a projection. In the full-rank case, perfect reconstruction is automatic for any valid basis and therefore cannot establish that the learned operator is meaningful.

## Training objectives that identify something

Use observed development signal transitions or missing/noisy signal reconstruction. For diffusion-like data, a model may predict `f(t+Δt)≈exp(−Δt Sθ)f(t)` in appropriately mass-normalized coordinates. Use a small matrix exponential reference or a polynomial filter `Σ_j α_j Sθ^j` for training. Evaluate which approximation is used and its error.

A proposed loss combines held-in prediction error, operator regularization, verified symmetry commutation and optional cross-resolution consistency:

`L=L_pred+λ_reg R(Lθ)+λ_sym Σ_g||T_gLθ−LθT_g||²+λ_scale||R L_f−L_c R||²`.

Transform maps T_g and coarsening R must be applicable to the problem and available under the same information contract as controls. They are not arbitrary augmentation operators. In weighted spaces, define compatible mass-weighted actions rather than assuming Euclidean commutation covers every discretization. Add each constraint as a separate ablation before combining them.

An eigensolver's residual is a numerical diagnostic, not a learning signal for physical correctness. Likewise a reconstruction loss with all N modes cannot choose among complete orthogonal bases. Use a real prediction/compression/missing-data task with held-out signals and graphs.

## Numerical stability

Eigenvectors have sign ambiguity and repeated-eigenspace nonuniqueness; derivatives through them become problematic near repeated eigenvalues [D03]. Train polynomial/operator actions first and compute eigenspectra after freezing the candidate. For tests compare projectors or principal angles, not arbitrary eigenvector columns. If a truncation boundary cuts a repeated cluster, report the ambiguity or retain the complete cluster.

Dense `eigh` is acceptable for small reference graphs, not a scalable FFT replacement. Cap dense diagnostics at a declared small N. The implementation must not market an O(N³) eigendecomposition as an O(N log N) transform without counting setup and repeated-use assumptions.

## Contracts and code units

`GraphDomain`: node count, edge index, mass vector, coordinates if public, admissible transformations and provenance.
`OperatorModel.apply(f[N,C]) -> [N,C]`.
`SpectralBasis`: eigenvalues[k], basis[N,k], mass[N], operator hash and degeneracy metadata.
`Transform.encode/decode`: shape-checked weighted coefficients and reconstruction.

| File | Responsibility |
|---|---|
| domains.py | Graph instances, public edge candidates and signal splits |
| laplacian.py | Sparse PSD construction and scale constraints |
| mass.py | Weighted inner products and coordinate conversion |
| filters.py | Polynomial action and small exponential reference |
| train.py | Prediction loss and individually toggled constraints |
| spectra.py | Frozen eigendecomposition and subspace diagnostics |
| transform.py | Encode/decode with mode-selection policy |
| baselines.py | Fixed geometry Laplacian, learned Laplacian, PCA and valid grid DFT |
| evaluate.py | Predictive/compression error, cost and discretization transfer |
| adapter.py | `fit_spectral_operator` and `transform_signal` |

## First benchmark

Generate signals on small graphs with hidden edge weights and public candidate connectivity. Do not pass the exact true operator into the candidate as “geometry.” Create train/dev graph instances with different weight distributions and hold out additional graph sizes or discretizations. Start at 32–128 nodes, two to eight signal channels and a small polynomial degree. Reserve a regular grid as a sanity case where a conventional basis should be strong, not an artificially weak baseline.

Minimum comparisons: fixed geometry-based Laplacian; learned-Laplacian model with identical parameterization but no new constraints; PCA fit only on training signals; random orthogonal basis; DFT only on a domain where ordering/periodicity makes it legitimate. Include the true generator operator only as an explicitly privileged oracle. Compare FNO/DeepONet only for a common prediction task, not as nonsensical transforms of one graph snapshot.

Primary proposal: held-out transition prediction or missing-signal reconstruction at a fixed total computational budget—choose one before confirmation. Secondary: k-mode compression, weighted reconstruction error, operator recovery when identifiable, cost including setup, and transfer across declared graph sizes. Reusing a frozen learned operator over many signals may amortize cost; state the reuse count.

## Tests and failure controls

PSD and symmetry; row sums zero in the unweighted Laplacian; constant null mode; positive masses; mass-weighted Parseval; encode/decode on a complete basis; permutation covariance including mass and edges; repeated-eigenspace projector consistency; degree-zero filter; analytic gradients for a small simple-spectrum case; polynomial gradients independent of eigenvector choice; no dense allocation beyond the cap; wrong supplied symmetry rejected or shown harmful in a labeled ablation.

Sunday demonstration: a learned sparse operator, its spectrum and a genuine held-out reconstruction/prediction comparison. Defer universal spectral theory, arbitrary Koopman diagonalization, learned graph topology plus learned masses plus learned basis simultaneously, and coupling to every other module before this single-domain study is interpretable.


---

<!-- Source document: docs/projects/07_wpinn.md -->

# 07 — World-PINN
## Working research title
Weak-Form Law Identification with Verified Symmetry and Dissipation Constraints.

The project combines observation fitting, sparse law identification and validated structure. Inverse PINNs already address discovery [R27], so “the equations are unknown” is not its novelty claim. The proposal must show exactly which verified structural information improves identification and when it fails.

## Prior work and scientific distinctions

Forward PINNs [R26], inverse discovery [R27], SINDy [R28], structured symbolic regression [R29] and Hamiltonian networks [R30] are necessary context. Known PINN failure modes motivate tests beyond training residuals [R31]. Distinguish three tasks: unknown coefficients in known equations; unknown sparse support within a fixed library; and unknown functional forms outside the library. The first version tackles the first two only. It cannot claim arbitrary physical-law discovery.

## Primary system and identifiability

Start with a damped oscillator:

`q̇=v`, `v̇=−kq−cv`.

Generate multiple initial conditions, k and c values, sampling rates and noise realizations. Use c=0 as a conservative subset and c>0 as a dissipative subset. The observation interface exposes noisy trajectories; generator truth is available only to evaluation/oracle controls. If the signal does not excite relevant modes, coefficients may not be identifiable—record this, rather than assuming every trajectory uniquely determines the equation.

A small neural field `xθ(t,context)` fits observations, or use a simpler smoother as a baseline. Construct a declared candidate library Θ from normalized polynomial terms in q,v and any authorized derivatives. Normalize columns during sparse regression and restore original units afterward. A poorly scaled library can change apparent sparsity without changing the physics.

## Weak residual

For a test function ψ that vanishes at endpoints, use

`r(ξ)=∫ψ'(t)x(t)dt + ∫ψ(t)Θ(x(t))ξ dt`.

Minimize weak residuals plus data fitting and declared structure. This avoids direct finite-difference differentiation of noisy measurements, but smoothing and quadrature errors remain. Test quadrature on known analytic trajectories and vary sampling resolution. Do not secretly calculate derivatives from clean generator trajectories while claiming robustness to noisy-only observations.

A proposed objective is

`L=λ_data L_data+λ_weak ||r(ξ)||²+λ_sparse Penalty(ξ)+λ_structure L_verified`.

For a PINN variant include initial/boundary conditions explicitly. Use sequential thresholded least squares or another documented sparse method to select support, then refit coefficients without a shrinkage bias where appropriate. L1 shrinkage alone does not necessarily produce the exact symbolic support you want to report.

## Physics must be appropriate

For `E=(v²+kq²)/2`, `dE/dt=−cv²`. Conserve E only for c=0; use dissipation when c>0. A candidate symmetry or invariant supplied by QWIPII must be accompanied by a domain/assumption certificate. Its verification cannot use the same held-out outcome you later cite as evidence of successful generalization. Wrong constraints should be rejected when analytically decidable or retained as labeled failure-control experiments.

The first study does not need an autonomous symbolic theorem generator. It can compare verified known-applicable constraints with no constraints, then add learned candidate selection as a separately measured extension. Otherwise success may depend on hidden privileged knowledge of the true law.

## Staged fitting algorithm

```text
split full trajectories and physical parameter draws
fit observation smoother on training trajectories only
build a normalized declared candidate library
assemble weak-form integrals with endpoint-zero test functions
fit sparse support using development-selected hyperparameters
refit coefficients on the selected support
optionally alternate field fitting and law fitting with logged objectives
validate rollouts and structure on development trajectories
freeze code, library, selection thresholds and budget before confirmation
```

Alternation is optional; prove it adds value over the simpler sequential pipeline before making it mandatory. Different stopping points must be selected on development data only.

## Code units

| File | Responsibility |
|---|---|
| systems.py | Oscillator generators, truth separation and complete-trajectory splits |
| field.py | Small neural field and simpler smoothing interface |
| library.py | Typed candidate terms, units and normalization |
| weak_form.py | Test functions, quadrature and residual assembly |
| sparse_fit.py | Support selection, refitting and coefficient serialization |
| constraints.py | Conservation/dissipation and verified symmetry contracts |
| train.py | Sequential and optional alternating fitting |
| baselines.py | Least squares, SINDy-style, inverse PINN and data-only models |
| evaluate.py | Law recovery, rollout and uncertainty summaries |
| adapter.py | `identify_dynamical_law` |

`Trajectory` has times[T], observations[T,D], masks[T,D], trajectory_id and public context. `LibraryMatrix` carries named terms and scaling. `LawResult` contains symbolic terms, coefficients with units/scales, validity domain, support-selection settings, uncertainty method and measured evidence. A printed equation without those fields is not a reproducible result.

## Baselines, endpoints and ablations

Minimum: ordinary linear/sparse regression with the same library; a SINDy-style derivative baseline with its noise assumptions documented; a known-support inverse PINN; a data-only predictor; and the proposed weak/structure method. Known-support methods have extra information and should be labeled accordingly. Match observation access and tuning budget, not just epochs.

Choose one primary: support recovery on identifiable synthetic tasks, or held-out rollout error. The other remains important but cannot rescue a failed preregistered primary. Report coefficient error only after aligning term scaling and support. Include noise, missing samples, sampling rate and out-of-training parameter regimes. A correct fit on a single trajectory is not a general law-identification claim.

Ablate weak form, structural constraints, sparse selection, smoothing and alternating training separately. Include deliberately wrong conservation on damped trajectories as a failure demonstration, not as part of a production method that falsely assumes it is valid.

## Tests and Sunday slice

Analytic residual for a known oscillator; integration-by-parts identity under exact/accurate quadrature; polynomial autodiff including second derivatives where needed; library units/scales; support threshold behavior; coefficient round trip; no clean-target derivative leakage; trajectory-level split integrity; conservative and damped energy tests; held-out rollout integrator accuracy; finite loss and explicit convergence failure.

Sunday should demonstrate oscillator-law identification with transparent assumptions and real residual/rollout evidence. Burgers, KdV, reaction-diffusion, general Lie symmetry discovery and simultaneous unknown boundaries are later modules. Expanding from one ODE to several PDEs before validating identifiability would produce impressive names but uninterpretable evidence.


---

<!-- Source document: docs/projects/08_cwlnn.md -->

# 08 — CWLNN
## Working research title
Sparse Multiscale World Representations with Budgeted Local-to-Global Computation.

Retain the user's CWLNN brand (“Convoluted World Large Neural Network”) without treating “large” as proof of capability. The first model is deliberately small. Its research purpose is a measurable hierarchy and routing mechanism, not another giant language-model pretraining project.

## Prior work and narrow claim

Perceiver IO [R32], Switch Transformers [R33], DiffPool [R34], Mamba [R35] and equivariant graph processing [R09] cover bottlenecks, sparse routing, hierarchy and efficient computation. The proposed experiment asks whether a genuinely sparse multiscale relational architecture yields better accuracy-versus-cost and size transfer on a chosen task than matched flat/local controls. Adding all known efficient mechanisms is not by itself a novel contribution.

## Graph hierarchy

Represent a sample with sparse levels `G_0,…,G_L` and parent maps `p_l:[N_l]→[N_{l+1}]`. Begin with a supplied/public deterministic structural hierarchy; do not use target labels to build it. Each level performs local relation-aware aggregation:

`h_i'=σ(W_self h_i+Σ_{j∈N(i)}K(e_ij)h_j)`.

Pool children by normalized sums/means using parent indices, then broadcast coarse updates back through the same mapping with a residual connection. Keep level widths and aggregation normalization explicit. A parent with many children should not gain an unintended magnitude advantage unless the task intentionally encodes count.

Use sparse index/scatter operations; no dense N×N soft assignment or adjacency in the claimed sparse path. A dense DiffPool-like baseline may be useful for accuracy, but its cost must be measured rather than hidden inside a “linear” complexity label.

## Routing scope

The reference always processes a fixed hierarchy. The next candidate may learn which nodes require expensive fine-scale updates, using local uncertainty/disagreement/budget features. Define a budget ledger and count routing itself. Begin with a fixed threshold control and a learned score with an explicit top-k budget. Training through hard selection may use a surrogate/straight-through estimator, but document that it is not an exact gradient of the discrete routing objective.

Expert mixtures and variable-depth computation are deferred until the hierarchy-alone ablation is interpretable. Avoid simultaneously changing hierarchy, width, routing and loss and then attributing gains to one named mechanism.

## Complexity statement and assumptions

If `N_l≤N/2^l`, bounded degree k, fixed width h and constant updates per level, aggregation/feature work is `O(Σ_l(N_lkh+N_lh²))=O(Nkh+Nh²)`. Building the hierarchy, sorting, dynamic routing and output decoding add work. Include those costs. An all-pairs attention step anywhere in the path can reintroduce quadratic interactions. Linear asymptotic scaling does not guarantee a faster small-N implementation.

Permutation behavior requires care. A hierarchy built by arbitrary input node order may break equivariance. Test a node permutation with edges, parent maps and public structural labels transformed consistently. Do not claim equivariance when only features are permuted and the hierarchy remains attached to old indices. Learned hierarchy construction later needs its own equivariance analysis.

## Code units and shapes

| File | Responsibility |
|---|---|
| graphs.py | Sparse graph batches and public hierarchy metadata |
| hierarchy.py | Deterministic coarsening, parent maps and sparse edges |
| local.py | Bounded-degree relational updates |
| pool.py | Count-aware pooling and consistent broadcast |
| routing.py | Fixed and learned budgeted selection with cost counters |
| model.py | Local/coarse/residual composition and readout |
| tasks.py | Multiscale graph signals and held-out graph sizes |
| baselines.py | Flat GNN/local CNN, small dense attention and relevant bottlenecks |
| evaluate.py | Accuracy, latency, memory and size-transfer curves |
| adapter.py | `encode_multiscale_world` |

`GraphLevel` contains features[N_l,H_l], edge_index[2,E_l], edge features[E_l,R], batch indices and parent_index[N_l]. A hierarchy validates every parent bound and batch boundary. `RoutingReceipt` stores selected nodes, requested/actual budget and dropped operations. Budget exhaustion cannot silently truncate a graph while reporting a normal result.

## Initial tasks and fair controls

Start with graph-signal prediction requiring both local and global information, such as multiscale diffusion or a compositional aggregation target on a public hierarchy. Train on small graphs and hold out larger graph instances and generator parameters. A task generated from exactly the candidate's architecture can favor it artificially, so include at least one task without an aligned hierarchy and report this limitation.

Compare a flat message-passing model, an equally wide local model, fixed hierarchical processing, the proposed routed hierarchy and a small dense-attention baseline at feasible sizes. Perceiver/Mamba-inspired alternatives are optional on genuinely common inputs/tasks; do not reshape graphs arbitrarily merely to claim a named-model comparison. Match parameter ranges and separately report total measured compute. Give controls access to the same public coordinates/hierarchy information where relevant.

Primary: error/accuracy at a declared measured inference-time budget on held-out graph sizes. Secondary: training cost, memory, preprocessing cost, robustness to node relabeling, performance on nonhierarchical controls and routing utilization. Save raw timings with warmup policy and synchronization; do not compare unsynchronized accelerator timing against synchronous CPU wall-clock.

## Tests

Sparse aggregation equals a tiny dense reference; pooling and broadcast shape/value checks; no cross-graph edges in batches; parent bounds; count normalization; node-permutation consistency with transformed hierarchy; deterministic routing under tied priorities; hard selected-node cap; empty/single-node graph behavior; disabled routing recovers reference hierarchy; no hidden dense adjacency at large-N test; gradient flow through supported surrogate; explicit reporting of unsupported device operations.

Use complexity counters and allocation checks as structural tests, plus measured timing as an empirical result. A test asserting that “our model is always faster” would be brittle and scientifically unjustified.

## Sunday slice and extension

Demonstrate a small multiscale forward/training pass, its routing receipt and a matched baseline comparison if completed. Defer billion-parameter scale, multimodal pretraining, arbitrary conceptual neighborhoods, universal language-model claims and making every World Series module depend on this backbone. Only after the standalone result passes should WCode or Q-APEN receive a controlled encoder-swap experiment.


---

<!-- Source document: docs/projects/09_ultron.md -->

# 09 — Ultron
## Working research title
Verified Budgeted Orchestration of Heterogeneous Research Capabilities.

ASI is a long-term motivation, not a v0.1 capability claim. Ultron initially coordinates a few real, tested modules under transparent budgets. It need not invoke all eight for every task, and an absent module must not be replaced with a fake successful adapter.

## Related work

The AI Scientist [R36], ADAS [R37], Darwin Gödel Machine [R38] and Co-Scientist [R39] already study research automation, agent design, agent modification and scientific hypothesis generation. The proposed question is whether a particular evidence-aware routing policy improves verified task completion over simpler policies with identical capabilities and resource budgets. “Multiple agents” or “self-improvement” alone is insufficient novelty.

## Typed state and actions

Represent a state as `(goal, task_type, evidence_DAG, capabilities, remaining_budget, failure_history)`. An action is a registered operation with typed inputs, expected artifact types, maximum cost and a verifier. The registry enumerates allowed actions; the model cannot invent a tool name and pretend it executed.

Examples: identify an oscillator law; solve a verified invariant puzzle; synthesize a bounded DSL program; fit a graph operator. Different tasks select different modules. A capability can be `AVAILABLE`, `UNAVAILABLE`, or `BLOCKED_BY_CONTRACT`; only available operations may run.

A full sequential research controller can be modeled as a finite-horizon constrained decision process. Start with a static router and a transparent state machine. The first learned extension is a contextual bandit or supervised ranker for choosing an applicable operation from development task features. Do not call this one-step selection a solved general meta-MDP. A sequential policy can follow after there is enough trustworthy trajectory data.

## Grounded objective

Use an externally computed objective such as

`R=verified_completion−λ measured_cost−κ invalid_actions`.

The completion score is computed by the task's verifier, not by the agent's prose, confidence or a self-written report. Separate partial engineering progress from final scientific correctness. A plot, paper draft or confident explanation does not count as successful law recovery unless the declared verifier checks it.

Evidence artifacts form a DAG: each result refers to input artifact hashes, producer version, config, cost receipt and verifier decision. Paths must resolve within the artifact root and hashes must match. Missing evidence is a hard failure for the corresponding claim, not an invitation to infer what probably happened.

## Execution state machine

```text
VALIDATE_TASK -> SELECT_AVAILABLE_ACTION -> RESERVE_BUDGET
  -> EXECUTE_REGISTERED_CAPABILITY -> VALIDATE_OUTPUT_SCHEMA
  -> VERIFY_RESULT -> APPEND_EVIDENCE -> STOP_OR_SELECT_NEXT
```

Errors release only the unused reserved budget, record the actual spent portion, and create an immutable failure receipt. Retries are bounded and counted. A module cannot change the task specification, success threshold or verifier while working on the task. Token/LLM costs are included if an optional language-model planner is added.

## Code units

| File | Responsibility |
|---|---|
| tasks.py | Research mini-task contracts and development task features |
| capabilities.py | Explicit operation registry and adapter availability |
| state.py | Immutable episode state and evidence references |
| router.py | Static, cheapest-valid, random-valid and learned policies |
| executor.py | Budget reservations and bounded capability execution |
| evidence.py | Hash-checked artifact DAG and claim provenance |
| verifier_client.py | Restricted interface to an independently controlled verifier |
| train_router.py | Development-only routing traces and policy fitting |
| evaluate.py | Matched-capability completion/cost comparisons |
| report.py | Structured evidence summary, never invented metrics |

The actual final verifier runs outside the development workspace. A client interface does not make a mutable in-process function independent. For tests, a toy verifier may live in fixtures, but fixture success is tagged `PLUMBING_ONLY` and cannot populate a research result table.

## Module adapters and integration boundaries

Start with QWIPII, WCode and World-PINN because they have clear verifiable outputs. Each adapter must pass standalone contract tests before registration. Remaining modules can register later when their real capability is useful: MALIS for adaptation, Q-APEN for prediction, WFIM for composition, WFT for transforms, CWLNN for encoding. No dependency requires all eight to be implemented before Ultron's state machine can be tested.

Avoid a forced linear pipeline through every module; it creates artificial dependencies and obscures attribution. If an exhibition includes a scripted all-module walkthrough, label it an architectural demonstration rather than evidence that the combined system outperforms simpler alternatives.

## Learning and baseline protocol

Collect development task outcomes for valid candidate modules under common budgets. Features must be available before the routing decision. Train a contextual bandit/ranker or imitate a development oracle that enumerates bounded choices. Counterfactual labels derived from running all modules cost real compute and belong in the training-cost ledger. Do not infer an untried route's outcome from the selected route's result.

Compare fixed task-type routing, cheapest valid routing, random valid routing, the learned policy and optionally a small monolithic planner with the same underlying tools/model access. Hold all capabilities and their checkpoints fixed during the routing comparison. Otherwise improvement could come from a stronger tool rather than better orchestration.

Primary: verified completion rate at a fixed per-task cost budget. Secondary: mean total cost, invalid action fraction, evidence completeness, latency, repeated-work overhead and ability to reject unsupported tasks. Report outcomes by task family and not only a pooled average dominated by the easiest task.

## Self-modification boundary

No automatic self-modification in v0.1. A later proposal system may generate patches in isolated worktrees, but changes to evaluators, protected tests, resource policy or approved claim thresholds are forbidden. Candidate changes are selected on development validation, reviewed and frozen before a separate confirmation evaluation. Reusing final holdout scores repeatedly to choose modifications would invalidate the “held-out” claim. An agent's own success declaration cannot approve its patch.

Darwin Gödel Machine uses an archive that can preserve useful stepping stones [R38]; do not mischaracterize that prior work as only monotonic hill climbing. Our safer scoped first experiment is routing, not an attempted replication of the entire self-improving-agent literature.

## Tests and Sunday slice

Unavailable capability rejection; typed input/output validation; path traversal rejection; artifact hash tampering; cycle detection in evidence DAG; verifier refusal; budget reservation/release; bounded retries; deterministic static routing; checkpoints fixed during evaluation; mock receipts excluded from scientific summaries; unsupported tasks reported truthfully; attempted evaluator modification blocked by actual environment controls.

Sunday demonstration: one task routed through one or more real modules with visible evidence and cost, plus a simpler-routing comparison where run. This can be useful research without pretending to be autonomous general science or ASI. Defer open-ended internet actions, external deployment, unrestricted code execution and recursive model rewrites.


---

<!-- Source document: tasks/TASK_MAP.md -->

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

<!-- Source document: prompts/00_integrator.md -->

# Cursor integrator: bootstrap the World Series workbench

Read START_HERE.md, AGENTS.md, WORLD_SERIES_MASTER_PLAN.md, docs/ARCHITECTURE.md, docs/EXPERIMENT_PROTOCOL.md and tasks/tasks.json. This is a research-and-code planning pack, not an already implemented model repository.

First inspect the current workspace, Git state, existing tests, project identities, available hardware and Python environment. Preserve all user work and frozen study outcomes. Do not delete, reset, clean, overwrite or migrate existing repositories. Record useful reusable code with its true revision/hash and license. If this is an empty new workbench, create the proposed package structure; if not, make an explicit compatibility plan before edits.

Execute CORE-01 through CORE-06 in dependency order with atomic verifiable changes. Choose a compatible locked environment and implement shared contracts, bounded resource accounting, split controls, immutable run manifests, a small CLI and CPU tests. Do not scaffold fake models to make an all-project command pass. Unimplemented capabilities must remain unavailable.

After core is sound, allocate per-module tasks using prompts/01_qlearn.md through prompts/09_ultron.md. One integrator owns shared contracts and lockfiles. Parallelize isolated editing only; allow one numerical worker by default. Never start nine heavy training jobs because nine prompts exist.

Finish each task with actual test results and a handoff. Build the smallest complete reference → baseline → candidate → evidence path. Protect final evaluation outside the development workspace. Do not create positive metrics, launch paid services, deploy anything, access sealed data or execute unrestricted generated code. A correct negative result is a successful research artifact.


---

<!-- Source document: sources/REFERENCES.md -->

# Verified source registry

Checked September 22, 2026. Years use the displayed first preprint year where applicable, not necessarily the journal publication year. Reading depth is explicit: an abstract-screened entry is not a claim of a cover-to-cover review. Laboratory explanations and documentation are not counted as research papers. This is a targeted related-work review, not proof that no similar method exists.

## [R01] Learning to learn by gradient descent by gradient descent

Andrychowicz et al. (2016). **paper**.

Source: https://arxiv.org/abs/1606.04474

Review depth: abstract / paper landing.

Implementation relevance: Establishes learned update rules as prior work. Reproduce a small learned-optimizer control rather than claiming that learning an optimizer is new.

## [R02] Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks

Finn, Abbeel and Levine (2017). **paper**.

Source: https://proceedings.mlr.press/v70/finn17a.html

Review depth: paper landing.

Implementation relevance: Meta-learning an initialization differs from learning an update policy. Use a MAML-like control only on a common task-adaptation protocol.

## [R03] Learning Versatile Optimizers on a Compute Diet

Moudgil, Knyazev, Lajoie and Belilovsky (2025). **paper**.

Source: https://arxiv.org/html/2501.12670v1

Review depth: selected full-text methods.

Implementation relevance: Celo already combines optimizer design and scheduling ideas. The proposed contribution must test transfer and budget allocation, not merely combine a scheduler with a learned update.

## [R04] Celo2: Towards Learned Optimization Free Lunch

Moudgil, Knyazev and Belilovsky (2026). **paper**.

Source: https://arxiv.org/html/2602.19142v1

Review depth: selected full-text methods.

Implementation relevance: Normalized update rules and augmentation are relevant strong comparators. Preserve its distinction between a learned update rule and tunable step size; a tiny custom port is not a faithful reproduction.

## [R05] Efficient Long-Horizon Learning for Learned Optimization

Huang, Thérien, Harrison and Belilovsky (2026). **paper**.

Source: https://arxiv.org/abs/2607.06772

Review depth: selected full-text methods plus latest abstract.

Implementation relevance: ELO studies long-horizon failures and expert supervision. Test longer unrolls than meta-training, log divergence, and do not assess generalization on short training horizons only.

## [R06] Neural Discrete Representation Learning

van den Oord, Vinyals and Kavukcuoglu (2017). **paper**.

Source: https://arxiv.org/html/1711.00937v2

Review depth: selected full-text methods.

Implementation relevance: VQ codebooks are established. Measure quantization distortion and code usage; separate quantization from the adaptive-memory mechanism.

## [R07] Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models

Chua, Calandra, McAllister and Levine (2018). **paper**.

Source: https://arxiv.org/html/1805.12114

Review depth: selected full-text methods.

Implementation relevance: PETS supplies a probabilistic-ensemble and trajectory-sampling comparator. Distinguish within-model noise from disagreement between model predictions.

## [R08] Mastering Diverse Domains through World Models

Hafner et al. (2023). **paper**.

Source: https://arxiv.org/abs/2301.04104

Review depth: abstract / paper landing.

Implementation relevance: DreamerV3 is relevant world-model context. A toy ensemble is not a replication of the full Dreamer system and should not be benchmarked as if the settings match.

## [R09] Group Equivariant Convolutional Networks

Cohen and Welling (2016). **paper**.

Source: https://proceedings.mlr.press/v48/cohenc16.html

Review depth: paper landing.

Implementation relevance: Equivariance is established. State exactly which group acts, on which objects, and what the output action is.

## [R10] Generative Adversarial Symmetry Discovery

Yang, Walters, Dehmamy and Yu (2023). **paper**.

Source: https://arxiv.org/html/2302.00236v2

Review depth: selected full-text methods.

Implementation relevance: LieGAN already learns symmetries. Discovery proposals need anti-collapse controls and verification before being used to remove search states.

## [R11] Symmetry Discovery Beyond Affine Transformations

Shaw, Magner and Moon (2024). **paper**.

Source: https://arxiv.org/abs/2406.03619

Review depth: abstract / paper landing.

Implementation relevance: Nonlinear symmetry discovery is also prior work. The first World Series implementation deliberately uses a restricted discovery grammar.

## [R12] Optimal Renormalization Group Transformation from Information Theory

Lenggenhager, Gökmen, Ringel, Huber and Koch-Janusz (2018). **paper**.

Source: https://arxiv.org/abs/1809.09632

Review depth: abstract / paper landing.

Implementation relevance: Coarse-graining and information preservation have a substantial literature. A commutation penalty alone does not establish a physical renormalization-group theory.

## [R13] Solving olympiad geometry without human demonstrations

Trinh et al. (2024). **paper**.

Source: https://www.nature.com/articles/s41586-023-06747-5

Review depth: selected full-text methods.

Implementation relevance: AlphaGeometry motivates neural guidance plus symbolic checking. A finite puzzle solver must not claim equivalent coverage or Olympiad performance.

## [R14] Learning to Represent Programs with Graphs

Allamanis, Brockschmidt and Khademi (2017). **paper**.

Source: https://arxiv.org/html/1711.00740

Review depth: selected full-text methods.

Implementation relevance: Program graphs and their semantic relations already exist. Isolate the benefit of the proposed graph ranker using the same enumerator and verifier as controls.

## [R15] DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning

Ellis et al. (2020). **paper**.

Source: https://arxiv.org/html/2006.08381

Review depth: selected full-text methods.

Implementation relevance: Program-library learning and guided synthesis are close prior art. Library induction is a later extension, not an unimplemented claim in the first search experiment.

## [R16] FunSearch: Making new discoveries in mathematical sciences using Large Language Models

Google DeepMind (2023). **primary laboratory explainer**.

Source: https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/

Review depth: primary laboratory explainer.

Implementation relevance: Evaluator-driven program search is an important design precedent. This entry is a laboratory explanation, not a claim to have read the full Nature paper.

## [R17] Beyond Fully-Connected Layers with Quaternions: Parameterization of Hypercomplex Multiplications with 1/n Parameters

Zhang et al. (2021). **paper**.

Source: https://arxiv.org/abs/2102.08597

Review depth: abstract / paper landing.

Implementation relevance: PHM already learns hypercomplex-inspired multiplication parameterizations. Arbitrary bilinear weights do not automatically satisfy associativity or division properties.

## [R18] Hyperdimensional Computing: An Introduction to Computing in Distributed Representation with High-Dimensional Random Vectors

Kanerva (2009). **paper**.

Source: https://link.springer.com/article/10.1007/s12559-009-9009-8

Review depth: paper landing.

Implementation relevance: High-dimensional distributed representation is not a new number system by itself. Include ordinary vector and binding-based controls.

## [R19] A Primer on the Signature Method in Machine Learning

Chevyrev and Kormilitzin (2016). **paper**.

Source: https://arxiv.org/html/1603.03788

Review depth: selected full-text background.

Implementation relevance: Iterated integrals and graded representations provide nearby context. The proposed completed word algebra is a deliberately classical mathematical foundation, not a claim of inventing infinite dimensions.

## [R20] The Octonions

Baez (2001). **paper**.

Source: https://arxiv.org/abs/math/0105155

Review depth: abstract / paper landing.

Implementation relevance: Choose algebraic axioms explicitly. Do not assume that adding dimensions preserves familiar division, commutativity or associativity properties.

## [R21] The Emerging Field of Signal Processing on Graphs: Extending High-Dimensional Data Analysis to Networks and Other Irregular Domains

Shuman et al. (2012). **paper**.

Source: https://arxiv.org/abs/1211.0053

Review depth: abstract / paper landing.

Implementation relevance: Graph spectral transforms are established. The transform must specify its operator, inner product and inverse; the listed year is the preprint year.

## [R22] Learning Laplacian Matrix in Smooth Graph Signal Representations

Dong, Thanou, Frossard and Vandergheynst (2014). **paper**.

Source: https://arxiv.org/html/1406.7842

Review depth: selected full-text methods.

Implementation relevance: Learning a graph Laplacian and its spectral representation already exists. Compare to this family before claiming learned-world spectra as novel; year refers to first preprint.

## [R23] Fourier Neural Operator for Parametric Partial Differential Equations

Li et al. (2020). **paper**.

Source: https://arxiv.org/html/2010.08895

Review depth: selected full-text methods.

Implementation relevance: FNO learns operator mappings using Fourier-domain layers. A learned spectral transform is a different object; compare prediction only when the task and data match.

## [R24] Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs

Kovachki et al. (2023). **paper**.

Source: https://jmlr.org/papers/v24/21-1524.html

Review depth: paper landing.

Implementation relevance: Function-space operator learning and discretization transfer are existing research areas. Test discretization claims explicitly instead of inferring them from notation.

## [R25] DeepONet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators

Lu et al. (2019). **paper**.

Source: https://arxiv.org/abs/1910.03193

Review depth: abstract / paper landing.

Implementation relevance: Branch-trunk operator approximation is a useful alternative when testing learned mappings, but is not a mandatory comparator for a pure transform reconstruction study.

## [R26] Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations

Raissi, Perdikaris and Karniadakis (2017). **paper**.

Source: https://arxiv.org/abs/1711.10561

Review depth: abstract / paper landing.

Implementation relevance: Residual-constrained neural fitting is established. Compare against an ordinary data-only network and an appropriate known-equation PINN.

## [R27] Physics Informed Deep Learning (Part II): Data-driven Discovery of Nonlinear Partial Differential Equations

Raissi, Perdikaris and Karniadakis (2017). **paper**.

Source: https://arxiv.org/html/1711.10566v1

Review depth: selected full-text methods.

Implementation relevance: Original physics-informed work already addresses inverse discovery. Unknown coefficients or equations alone are not sufficient novelty.

## [R28] Discovering governing equations from data: Sparse identification of nonlinear dynamical systems

Brunton, Proctor and Kutz (2015). **paper**.

Source: https://arxiv.org/html/1509.03580

Review depth: selected full-text methods.

Implementation relevance: SINDy provides sparse-library law identification. Normalize library columns, distinguish support recovery from forecasting, and avoid differentiation of inaccessible clean targets.

## [R29] AI Feynman 2.0: Pareto-optimal symbolic regression exploiting graph modularity

Udrescu et al. (2020). **paper**.

Source: https://arxiv.org/abs/2006.10782

Review depth: abstract / paper landing.

Implementation relevance: Symbolic regression exploiting structure is existing work. A fixed polynomial-library method should not be presented as unrestricted symbolic discovery.

## [R30] Hamiltonian Neural Networks

Greydanus, Dzamba and Yosinski (2019). **paper**.

Source: https://arxiv.org/abs/1906.01563

Review depth: abstract / paper landing.

Implementation relevance: Energy-structured modeling is relevant for conservative systems. Do not impose conservation on genuinely damped dynamics.

## [R31] Characterizing possible failure modes in physics-informed neural networks

Krishnapriyan et al. (2021). **paper**.

Source: https://arxiv.org/html/2109.01050

Review depth: selected full-text methods.

Implementation relevance: A small physics residual is not by itself a reliable success criterion. Check held-out trajectories, boundary conditions and known failure cases.

## [R32] Perceiver IO: A General Architecture for Structured Inputs & Outputs

Jaegle et al. (2021). **paper**.

Source: https://arxiv.org/abs/2107.14795

Review depth: abstract / paper landing.

Implementation relevance: Latent bottlenecks are a relevant efficiency baseline. Count encoding and decoding costs, not just the latent processing block.

## [R33] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

Fedus, Zoph and Shazeer (2021). **paper**.

Source: https://arxiv.org/abs/2101.03961

Review depth: abstract / paper landing.

Implementation relevance: Sparse routing is established. Routing overhead and imbalance must be included in efficiency comparisons.

## [R34] Hierarchical Graph Representation Learning with Differentiable Pooling

Ying et al. (2018). **paper**.

Source: https://arxiv.org/html/1806.08804v4

Review depth: selected full-text methods.

Implementation relevance: Learned graph hierarchies are prior art. A dense assignment/coarsened adjacency can destroy the desired sparse complexity bound.

## [R35] Mamba: Linear-Time Sequence Modeling with Selective State Spaces

Gu and Dao (2023). **paper**.

Source: https://arxiv.org/abs/2312.00752

Review depth: abstract / paper landing.

Implementation relevance: Selective state spaces provide a sequence-model alternative. Only include on common sequence tasks with matched resource reporting.

## [R36] The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

Lu et al. (2024). **paper**.

Source: https://arxiv.org/abs/2408.06292

Review depth: abstract / paper landing.

Implementation relevance: Research automation already spans ideas, experiments and reports. The proposed test isolates evidence-aware routing, rather than claiming the first automated scientist.

## [R37] Automated Design of Agentic Systems

Hu et al. (2024). **paper**.

Source: https://arxiv.org/abs/2408.08435

Review depth: abstract / paper landing.

Implementation relevance: Searching agent architectures is existing work. Retain an immutable external evaluation protocol.

## [R38] Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents

Zhang et al. (2025). **paper**.

Source: https://arxiv.org/html/2505.22954v1

Review depth: selected full-text methods and limitations.

Implementation relevance: Empirically evaluated agent modification is existing work. The paper uses an archive of stepping stones; do not misdescribe it as only accepting immediate improvements.

## [R39] Accelerating scientific discovery with Co-Scientist

Gottweis et al. (2025). **paper**.

Source: https://arxiv.org/abs/2502.18864

Review depth: abstract / paper landing.

Implementation relevance: Multi-agent scientific hypothesis generation is close context. Ultron must demonstrate measured benefit rather than merely draw a multi-agent architecture.

## [R40] Deep Reinforcement Learning at the Edge of the Statistical Precipice

Agarwal et al. (2021). **paper**.

Source: https://arxiv.org/abs/2108.13264

Review depth: abstract / paper landing.

Implementation relevance: Aggregate uncertainty and task variation matter. Use paired task-level comparisons and report distributions rather than only the best seed.

## [D01] Rules

Cursor documentation (2026). **official documentation**.

Source: https://cursor.com/docs/rules

Review depth: official documentation.

Implementation relevance: Use .cursor/rules/*.mdc with frontmatter or root AGENTS.md. These are agent instructions, not a security boundary.

## [D02] torch.func

PyTorch documentation (2026). **official documentation**.

Source: https://docs.pytorch.org/docs/2.14/func.html

Review depth: official documentation.

Implementation relevance: Use functional parameter evaluation for differentiable inner loops. Resolve and lock a compatible installed stack before implementation.

## [D03] torch.linalg.eigh

PyTorch documentation (2026). **official documentation**.

Source: https://docs.pytorch.org/docs/2.14/generated/torch.linalg.eigh.html

Review depth: official documentation.

Implementation relevance: Eigenvector sign/phase and degenerate eigenspaces are nonunique; near-repeated eigenvalues can cause unstable eigenvector gradients.

## [D04] Reproducibility

PyTorch documentation (2026). **official documentation**.

Source: https://docs.pytorch.org/docs/2.14/notes/randomness.html

Review depth: official documentation.

Implementation relevance: Seed control does not guarantee identical results across releases and devices. Record exact versions, backend, dtype and deterministic settings.

## [D05] MPS backend

PyTorch documentation (2026). **official documentation**.

Source: https://docs.pytorch.org/docs/2.14/notes/mps.html

Review depth: official documentation.

Implementation relevance: Probe MPS support for the actual operations. Keep CPU float64 mathematical references and avoid assuming every higher-order gradient path works identically.
