#!/usr/bin/env python3
"""Verify recorded artifact digests without changing any historical receipt."""
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / 'world-series'


def digest(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def main():
    checks, failures = {}, []

    def verify(path, expected, origin):
        relative = str(path.relative_to(ROOT))
        actual = digest(path) if path.is_file() else None
        checks[relative] = dict(expected=expected, actual=actual, origin=origin)
        if actual != expected:
            failures.append(dict(path=relative, expected=expected, actual=actual, origin=origin))

    for name in ['qapen-lifecycle-v1', 'wcode-trained-v1', 'wft-constraints-v1']:
        base = REPO / 'campaigns' / name
        source = base / 'summary.json'
        for row in json.loads(source.read_text())['receipts']:
            for file, sha in row['files'].items():
                verify(base / file, sha, str(source.relative_to(ROOT)))
    for name, campaign in [('CWLNN', 'cwlnn-conditional-v1'), ('WPINN', 'wpinn-structured-v1')]:
        source = REPO / f'docs/closure/{name}_RESULTS.json'
        for file, sha in json.loads(source.read_text())['file_hashes'].items():
            verify(REPO / 'campaigns' / campaign / file, sha, str(source.relative_to(ROOT)))
    for name, key in [('WFIM_LEARNING', 'artifacts'), ('QWIPII_LEARNED', 'files')]:
        source = REPO / f'docs/closure/{name}_AUDIT.json'
        for file, sha in json.loads(source.read_text())[key].items():
            verify(REPO / file, sha, str(source.relative_to(ROOT)))
    states = collections.Counter()
    manifests = []
    for source in sorted((REPO / 'runs').glob('*/manifest.json')):
        row = json.loads(source.read_text())
        states[row.get('status', 'MISSING_STATUS')] += 1
        manifests.append(dict(path=str(source.relative_to(ROOT)), project=row.get('project'),
                              status=row.get('status'), error=row.get('error')))
        artifact = row.get('metrics', {}).get('raw_artifact')
        if artifact:
            verify(source.parent / artifact['path'], artifact['sha256'], str(source.relative_to(ROOT)))
    snapshot = json.loads((ROOT / 'FINAL_RESEARCH/SOURCE_MANIFEST.json').read_text())
    preserved = 0
    for row in snapshot['inventory']:
        path = row['path']
        if path.startswith(('world-series/campaigns/', 'world-series/runs/')):
            verify(ROOT / path, row['sha256'], 'initial closure snapshot')
            preserved += 1
    result = dict(passed=not failures, unique_files_verified=len(checks),
                  original_run_and_campaign_files_preserved=preserved,
                  run_manifest_count=len(manifests), run_states=dict(states),
                  run_manifests=manifests, failures=failures, checks=checks,
                  scope='Artifact identity and preservation only; numerical replay is recorded separately.')
    out = ROOT / 'RESEARCH_CLOSURE/receipts/ARTIFACT_AUDIT.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','run_manifests']}))
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
