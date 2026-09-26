"""Read-only claim-index validation; never regenerate or overwrite frozen evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import statistics
import subprocess


def digest(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--repo', type=Path, help='Restored implementation checkout with raw evidence')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    repo = args.repo.resolve() if args.repo else root / 'world-series'
    refs = {}

    def walk(value):
        if isinstance(value, dict):
            if isinstance(value.get('path'), str) and isinstance(value.get('sha256'), str):
                refs.setdefault(value['path'], set()).add(value['sha256'])
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    index = json.loads((repo / 'results/claim_index.json').read_text())
    walk(index)
    failures = []
    resolutions = []
    historical = []
    for name, expected in refs.items():
        candidates = [(root / name).resolve(), (repo / name).resolve(),
                      (repo / name.removeprefix('world-series/')).resolve()]
        matches = [p for p in candidates if (p.is_relative_to(root) or p.is_relative_to(repo)) and p.is_file()
                   and len(expected) == 1 and digest(p) in expected]
        if not matches:
            # A frozen index may identify a historical source revision. Verify
            # the exact Git blob; never substitute a new hash into that index.
            prefix = 'world-series/'
            old = subprocess.run(
                ['git', '-C', str(repo), 'show',
                 index['source_head'] + ':' + name.removeprefix(prefix)],
                capture_output=True,
            ) if name.startswith(prefix) else None
            if old is not None and old.returncode == 0 and len(expected) == 1 and hashlib.sha256(old.stdout).hexdigest() in expected:
                historical.append({'path': name, 'source_head': index['source_head'],
                                   'sha256': next(iter(expected)),
                                   'current_sha256': digest(root / name)})
            else:
                failures.append(name)
        else:
            resolutions.append({'path': name, 'resolved': str(matches[0]),
                                'sha256': next(iter(expected))})
    wft = json.loads((repo / 'docs/closure/WFT_RESULTS.json').read_text())
    rows = wft['raw_rows']
    transfer = [r for r in rows if r['groups'] in [32, 64]]
    means = {}
    for method, seeds in wft['per_seed'].items():
        means[method] = statistics.mean([
            statistics.mean(r['relative_prediction_error'] for r in transfer
                            if r['method'] == method and str(r['seed']) == seed)
            for seed in seeds
        ])
    result = {
        'passed': not failures,
        'unique_references': len(refs), 'failures': failures, 'resolved': resolutions,
        'historical_source_resolutions': historical,
        'wft': {'evaluation_rows': len(rows), 'transfer_rows': len(transfer),
                'transfer_means': means},
        'current_manuscript': {str(p.relative_to(root)): digest(p)
                               for p in (repo / 'paper').glob('preprint.*')
                               if p.suffix in {'.md', '.tex', '.pdf'}},
        'scope': 'Artifact identity and recalculation from preserved WFT rows; not new training or independent replication.',
    }
    with args.output.open('x') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'resolved'}, indent=2))
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
