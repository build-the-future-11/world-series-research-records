#!/usr/bin/env python3
"""Fail closed on missing identities, broken evidence references or source drift."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]


def sha(p):
    with p.open('rb') as handle:
        return hashlib.file_digest(handle,'sha256').hexdigest()


def main():
    registry=json.loads((ROOT/'RESEARCH_CLOSURE/REGISTRY.json').read_text())
    original=json.loads((ROOT/'publication_audit/20260924/PROJECT_REGISTRY.json').read_text())
    snapshot=json.loads((ROOT/'FINAL_RESEARCH/SOURCE_MANIFEST.json').read_text())
    assert {p['id'] for p in registry['projects']}=={p['id'] for p in original['projects']}
    assert len(registry['projects'])==len({p['id'] for p in registry['projects']})==9
    allowed={'VERIFIED_COMPLETE','SCIENTIFICALLY_COMPLETE_NEGATIVE_OR_INCONCLUSIVE',
             'BLOCKED_EXTERNAL','BLOCKED_DATA','BLOCKED_PROTOCOL','DEFERRED_COMPUTE',
             'FAILED_VERIFICATION','INCOMPLETE_TIMEBOX'}
    checked=set()
    for project in registry['projects']:
        assert project['completion_state'] in allowed
        assert project['blockers'] and project['stages']['K_publication_ready']=='NO'
        for field in ['result_artifact','frozen_protected_protocol']:
            r=project[field]
            assert sha(ROOT/r['path'])==r['sha256'],r['path']
            checked.add(r['path'])
    for file,digest in snapshot['tracked_source_hashes'].items():
        if file.startswith('src/'):
            assert sha(ROOT/'world-series'/file)==digest,file
    index=json.loads((ROOT/'world-series/results/claim_index.json').read_text())
    assert len(index['claims'])==9
    for claim in index['claims']:
        assert claim['independent_replication'] is False
        for field in ['analysis','config']:
            r=claim[field];assert sha(ROOT/r['path'])==r['sha256']
        assert claim['raw_files']
    verification=json.loads((ROOT/'RESEARCH_CLOSURE/receipts/current/receipt.json').read_text())
    assert verification['all_passed']
    wfim=json.loads((ROOT/'RESEARCH_CLOSURE/receipts/current/wfim_training/summary.json').read_text())
    assert wfim==dict(models=80,training_updates=12000,selection_scores=240,all_exact=True,
                      scope='same-host replay; not independent confirmation')
    cwlnn=json.loads((ROOT/'RESEARCH_CLOSURE/receipts/cwlnn/receipt.json').read_text())
    assert cwlnn['exit_code']==0 and cwlnn['full_result_matches_original']
    artifacts=json.loads((ROOT/'RESEARCH_CLOSURE/receipts/ARTIFACT_AUDIT.json').read_text())
    assert artifacts['passed']
    result=dict(passed=True,projects=9,numerical_source_unchanged=True,
                evidence_references_checked=len(checked),scientific_completion_claimed=False,
                scope='Closure consistency and local verification; scientific blockers retained.')
    (ROOT/'RESEARCH_CLOSURE/receipts/CLOSURE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
