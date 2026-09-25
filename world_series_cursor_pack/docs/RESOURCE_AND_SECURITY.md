# Resource, execution and evaluation boundaries

All numerical sizes in this pack are proposed starting configurations, not measured performance estimates. Default to one numerical training worker, tiny CPU smoke tests, no paid APIs and no dependency on a cluster. Confirm actual RAM, disk, device and available libraries in CORE-01. Do not infer installed hardware from project aspirations.

Suggested smoke ceilings: 64–256 samples, 16–32 inner learning steps, graphs with 32–128 nodes, eight active world experts, 128 memory entries, DSL depth six, algebra degree six. Larger configurations require an explicit budget record. Refuse allocations beyond maximum node/term/candidate count before constructing dense tensors. Resource checks must include adapters and evaluation, not just model forward passes.

Record measured elapsed time, peak process memory where supported, backend/dtype, candidate calls and failure reason. Cooperative Python budgets cannot forcibly contain all native-library allocations; use process/container limits for owned jobs where available. Do not kill other applications, lower system safety limits, or set unsafe accelerator memory variables.

Use a typed total DSL interpreter for synthesis. Validate the AST, operator whitelist, types, lengths and fuel before execution. A safe interpreter contains no file/network/subprocess capability. Do not use Python eval/exec as its implementation. General code execution, if added later, needs a hardened disposable container or equivalent, read-only inputs, no secrets, no host mounts, no network, limited process count and memory/time limits. Host subprocess timeouts are not sufficient isolation.

Keep the final evaluator outside the development workspace, with read-only candidate access and separately controlled input visibility. Do not let Ultron edit evaluator code, scoring functions or the claim ledger's approved thresholds. Agent rules improve behavior but do not enforce access control [D01]. Store secrets outside the repository and do not give research agents production credentials.

Ultron v0.1 executes pre-approved registered operations. Self-modification, external deployment, outreach and live trading are out of scope. Proposed edits in a later phase are reviewed as patches; they are never merged because the agent says its own test passed. Repeated validation selection is development, not fresh blind confirmation.

On exhaustion or dependency failure, emit a failure artifact and stop that task. A missing module returns UNSUPPORTED_CAPABILITY, not a mock success. Continue independent tasks only when their own prerequisites and budgets are satisfied.


---
