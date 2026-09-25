#!/usr/bin/env python3
"""Replay the recorded CWLNN source in an isolated copy; retain old attempts."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT/'world-series'
OUT = ROOT/'RESEARCH_CLOSURE/receipts/cwlnn'
COPY = REPO/'.work-tmp/finite-closure/cwlnn-source'


def main():
    OUT.mkdir(exist_ok=False)
    COPY.mkdir(exist_ok=False)
    for name in ['src', 'scripts', 'docs']:
        shutil.copytree(REPO/name, COPY/name, ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copytree(REPO/'campaigns/cwlnn-conditional-v1', COPY/'campaigns/cwlnn-conditional-v1')
    identity = json.loads((COPY/'campaigns/cwlnn-conditional-v1/identity.json').read_text())
    restored = []
    for name, expected in identity['files'].items():
        path = Path(name)
        if path.is_absolute():
            if path.parts[-3:-1] != ('scripts','closure'):
                raise ValueError(name)
            path = Path('scripts/closure')/path.name
        target = COPY/path
        if hashlib.sha256(target.read_bytes()).hexdigest() != expected:
            data = subprocess.check_output(['git','show',f'{identity["head"]}:{path}'],cwd=REPO)
            if hashlib.sha256(data).hexdigest() != expected:
                raise ValueError(f'Historical identity mismatch: {path}')
            target.write_bytes(data)
            restored.append(str(path))
    env = dict(os.environ, PYTHONPATH=str(COPY/'src'), PYTHONNOUSERSITE='1',
               OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1',
               TMPDIR=str(REPO/'.work-tmp/finite-closure/tmp'))
    argv = [str(REPO/'.work-tmp/review-v2-env/bin/python'), 'scripts/closure/analyze_cwlnn.py',
            '--replay-output', str(COPY/'campaigns/fresh-training-replay')]
    start = time.monotonic()
    with (OUT/'replay.log').open('w') as log:
        try:
            run = subprocess.run(argv,cwd=COPY,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=1800)
            code=run.returncode
        except subprocess.TimeoutExpired:
            code=124
    report=COPY/'docs/closure/CWLNN_RESULTS.json'
    old=json.loads((REPO/'docs/closure/CWLNN_RESULTS.json').read_text())
    new=json.loads(report.read_text()) if code==0 else None
    if code==0:
        shutil.copy2(report,OUT/'CWLNN_RESULTS.json')
    result=dict(exit_code=code,seconds=time.monotonic()-start,argv=argv,cwd=str(COPY),
                source_head=identity['head'],restored_historical_paths=restored,
                full_result_matches_original=new==old if new is not None else False,
                audit=None if new is None else new['audit'],
                environment='Existing separate review-v2 dependency environment, isolated source copy.',
                scope='Same-host numerical/checkpoint/permutation replay; not independent replication.')
    (OUT/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
    raise SystemExit(0 if code==0 and new==old else 1)


if __name__=='__main__':
    main()
