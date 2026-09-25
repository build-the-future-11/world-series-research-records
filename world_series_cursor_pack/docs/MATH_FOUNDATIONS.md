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
