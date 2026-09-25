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
