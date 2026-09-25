#!/usr/bin/env python3
"""Finite sequential checks with fresh outputs and retained failure logs."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / 'world-series'
OUT = ROOT / 'RESEARCH_CLOSURE/receipts/current'


def main():
    OUT.mkdir(exist_ok=False)
    scratch = REPO / '.work-tmp/finite-closure'
    env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONNOUSERSITE='1',
               TMPDIR=str(scratch / 'tmp'), MPLCONFIGDIR=str(scratch / 'cache'),
               XDG_CACHE_HOME=str(scratch / 'cache'), PYTHONPATH=str(REPO / 'src'))
    python = str(REPO / '.venv/bin/python')
    commands = [
        ('tests', [python, '-m', 'pytest', 'tests', '-q', '--basetemp', str(scratch / 'pytest')]),
        ('doctor', [python, '-m', 'world_series', 'doctor']),
        ('wfim_predictions', [python, 'scripts/closure/analyze_wfim_learning.py',
                              '--root', 'campaigns/wfim-coordinate-development-v1',
                              '--output', str(OUT / 'wfim_predictions.json')]),
        ('wfim_full_training', [python, 'scripts/closure/replay_wfim_training.py',
                               '--root', 'campaigns/wfim-coordinate-development-v1',
                               '--output', str(OUT / 'wfim_training')]),
    ]
    receipts = []
    for name, argv in commands:
        start = time.monotonic()
        log = OUT / f'{name}.log'
        with log.open('w') as handle:
            try:
                result = subprocess.run(argv, cwd=REPO, env=env, stdout=handle,
                                        stderr=subprocess.STDOUT, timeout=1800)
                code = result.returncode
            except subprocess.TimeoutExpired:
                code = 124
                handle.write('\nTIMEOUT; incomplete outputs preserved.\n')
        receipts.append(dict(step=name, argv=argv, cwd=str(REPO), exit_code=code,
                             seconds=time.monotonic()-start, log=str(log.relative_to(ROOT)),
                             log_sha256=hashlib.sha256(log.read_bytes()).hexdigest()))
        (OUT / 'commands.json').write_text(json.dumps(receipts, indent=2)+'\n')
        print(json.dumps(receipts[-1]), flush=True)
    result = dict(all_passed=all(r['exit_code']==0 for r in receipts), commands=receipts,
                  scope='Same-host implementation tests and exact historical replay; not independent confirmation.')
    (OUT / 'receipt.json').write_text(json.dumps(result, indent=2)+'\n')
    raise SystemExit(0 if result['all_passed'] else 1)


if __name__ == '__main__':
    main()
