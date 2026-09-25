#!/usr/bin/env python3
"""Planning-pack consistency checks. Does not validate trained models."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_NS = {
    "qlearn", "qapen", "qwipii", "wcode", "wfim", "wft", "wpinn", "cwlnn", "ultron"
}
REQUIRED_DOCS = [
    "START_HERE.md",
    "AGENTS.md",
    "WORLD_SERIES_MASTER_PLAN.md",
    "docs/ARCHITECTURE.md",
    "docs/EXPERIMENT_PROTOCOL.md",
    "docs/MATH_FOUNDATIONS.md",
    "docs/RESOURCE_AND_SECURITY.md",
    "prompts/00_integrator.md",
    "projects.json",
    "tasks/tasks.json",
]
PROJECT_SPECS = [
    "docs/projects/01_qlearn.md",
    "docs/projects/02_qapen.md",
    "docs/projects/03_qwipii.md",
    "docs/projects/04_wcode.md",
    "docs/projects/05_wfim.md",
    "docs/projects/06_wft.md",
    "docs/projects/07_wpinn.md",
    "docs/projects/08_cwlnn.md",
    "docs/projects/09_ultron.md",
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_DOCS + PROJECT_SPECS:
        if not (ROOT / rel).is_file():
            errors.append(f"missing file: {rel}")

    projects_path = ROOT / "projects.json"
    tasks_path = ROOT / "tasks" / "tasks.json"
    namespaces: set[str] = set()
    if projects_path.is_file():
        projects = json.loads(projects_path.read_text(encoding="utf-8"))
        namespaces = {p["namespace"] for p in projects.get("projects", [])}
        if namespaces != EXPECTED_NS:
            errors.append(f"projects.json namespaces mismatch: {sorted(namespaces)}")

    task_ids: set[str] = set()
    if tasks_path.is_file():
        payload = json.loads(tasks_path.read_text(encoding="utf-8"))
        for t in payload.get("tasks", []):
            tid = t["id"]
            if tid in task_ids:
                errors.append(f"duplicate task id: {tid}")
            task_ids.add(tid)
        for t in payload.get("tasks", []):
            for pre in t.get("prerequisites", []):
                if pre not in task_ids:
                    errors.append(f"{t['id']} missing prerequisite {pre}")

    print("world_series_cursor_pack validate_pack")
    print(f"root: {ROOT}")
    print(f"docs_ok: {not any(e.startswith('missing') for e in errors)}")
    print(f"projects: {len(namespaces)} namespaces")
    print(f"tasks: {len(task_ids)}")
    if errors:
        print("STATUS: FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("STATUS: PASS")
    print("NOTE: planning consistency only; no application or model is implied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
