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
