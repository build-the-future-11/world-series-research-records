#!/usr/bin/env python3
"""Reconcile nine original identities against current, bounded evidence."""
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / 'world-series'
OUT = ROOT / 'RESEARCH_CLOSURE'

DETAILS = {
 'qlearn': ('natural-digits-v1', 'docs/closure/GATE_RESULTS.json', 'configs/natural-digits-v1.json',
   'UCI optical digits; whole digit-pair roles, plus separately declared constructed optimizees.',
   'No general optimizer advantage; failed sensitivity trajectories remain incomplete.',
   'BLOCKED_PROTOCOL', 'Original full-cost, held-optimizee-family estimand, practical margin and external confirmation split are not frozen. Broader MALIS architecture and compatible learned-optimizer qualification remain open.'),
 'qapen': ('qapen-lifecycle-v1', 'docs/closure/QAPEN_RESULTS.json', 'docs/closure/QAPEN_PROTOCOL.md',
   'Seeded linear-Gaussian streams; independent codebook training, four schedules and two noise levels.',
   'Lifecycle and delayed-utility memory execute; the combined candidate loses to rolling ridge and recent-memory controls.',
   'BLOCKED_PROTOCOL', 'No full latent-world-model/generalization and total-cost confirmation contract. The finite linear-Gaussian result does not finish the full proposal.'),
 'qwipii': ('qwipii-learned-development-v1', 'docs/closure/QWIPII_LEARNED_AUDIT.json', 'campaigns/qwipii-learned-development-v1/protocol.json',
   'Finite ring permutations; trained and selection goals separate from four held size-six patterns.',
   'Learned discovery reduces expansions but is slower than random ordering; greedy ranking produces longer paths in some cases.',
   'BLOCKED_PROTOCOL', 'No fresh puzzle-family population or powered full-cost confirmation contract. Exact certificate coverage is restricted to the declared finite domain.'),
 'wcode': ('wcode-trained-v1', 'docs/closure/WCODE_RESULTS.json', 'docs/closure/WCODE_PROTOCOL.md',
   '331 finite integer-function semantics, 171 train / 49 selection / 51 held family / 60 held composition.',
   'Trained relational scoring has no robust advantage; held-composition cap24 success is zero. Historical overlap is disclosed.',
   'BLOCKED_PROTOCOL', 'Fresh uncontaminated semantic-family evaluation and complete cost/DSL coverage are not frozen. Lists, multivariable programs and the original data/control-flow representation remain partial.'),
 'wfim': ('wfim-coordinate-development-v1', 'docs/closure/WFIM_LEARNING_AUDIT.json', 'campaigns/wfim-coordinate-development-v1/protocol.json',
   'Exhaustive binary words length 2–8; template and length holds; two fixed targets.',
   'Per-letter product transport cancels exactly. Learned per-word coordinates do not beat identity coordinates on ordered-pattern prediction.',
   'BLOCKED_PROTOCOL', 'Original exactly byte-matched comparison and independently sampled task-family contract are absent. A common payload ceiling is not equal used capacity.'),
 'wft': ('wft-constraints-v1', 'docs/closure/WFT_RESULTS.json', 'docs/closure/WFT_PROTOCOL.md',
   'Seeded equitable weighted path/cycle graphs; frozen model transfer across size/topology.',
   'Both constraints lower mean error within the declared generator; individual negative cells and spectral-boundary discrepancies remain.',
   'BLOCKED_PROTOCOL', 'Broader physical-field/operator distribution, complete cost-matched controls, novelty distinction and external confirmation contract remain unresolved.'),
 'wpinn': ('wpinn-structured-v1', 'docs/closure/WPINN_RESULTS.json', 'docs/closure/WPINN_PROTOCOL.md',
   'Three oscillator laws, five observation conditions, whole-trajectory role separation and eight seeds.',
   'Neural weak and passive variants retain failed cells; their primary means stay null. Solver diagnostics do not replace original failures.',
   'BLOCKED_PROTOCOL', 'Required held physical-parameter regimes, inverse-PINN and data-only controls need a frozen extension. Joint fitting/PDEs were optional or deferred in the original first-stage scope.'),
 'cwlnn': ('cwlnn-conditional-v1', 'docs/closure/CWLNN_RESULTS.json', 'docs/closure/CWLNN_PROTOCOL.md',
   'Generated path/cycle/tree graphs, held sizes/times, aligned and nonhierarchical targets.',
   'Learned half routing is slower and less accurate than full hierarchy on both declared tasks.',
   'BLOCKED_PROTOCOL', 'Arbitrary-tree receptive-field matching and original full-cost/scaling confirmation contract remain unresolved. Allocation shape probes are not large-scale model evidence.'),
 'ultron': ('development-v2', 'docs/closure/GATE_RESULTS.json', 'docs/execution/development-v2/PROTOCOL.md',
   'Finite DSL task families with repeated seeds; nine held families in the gate reanalysis.',
   'Observed routing gain over best fixed tool has a family-bootstrap interval spanning zero; no general-agent claim.',
   'BLOCKED_EXTERNAL', 'Independent evaluator and privately held verification tasks are absent. Heterogeneous capability, evidence-attribution and full-cost studies also remain open.'),
}


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')


def sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def ref(path):
    return dict(path=str(path.relative_to(ROOT)), sha256=sha(path))


def main():
    snapshot = json.loads((ROOT/'FINAL_RESEARCH/SOURCE_MANIFEST.json').read_text())
    original = json.loads((ROOT/'publication_audit/20260924/PROJECT_REGISTRY.json').read_text())
    inventory = snapshot['inventory']
    projects, contracts, claims = [], [], []
    for old in original['projects']:
        pid = old['id']
        campaign, analysis, protocol, dataset, result, state, blocker = DETAILS[pid]
        code = REPO/'src/world_series'/pid
        analysis_path, protocol_path = REPO/analysis, REPO/protocol
        raw = [r for r in inventory if r['path'].startswith(f'world-series/campaigns/{campaign}/')]
        if pid in {'qlearn','ultron'}:
            for manifest in (REPO/'runs').glob('*/manifest.json'):
                saved=json.loads(manifest.read_text())
                if saved.get('project')==pid:
                    prefix=str(manifest.parent.relative_to(ROOT))+'/'
                    raw.extend(r for r in inventory if r['path'].startswith(prefix))
        relevant = [r for r in inventory if r['path'].startswith(f'world-series/src/world_series/{pid}/')]
        history = json.loads(analysis_path.read_text())
        historical_identity = history.get('identity', history.get('source_identity', {}))
        analysis_identity = historical_identity
        proto = json.loads(protocol_path.read_text()) if protocol_path.suffix=='.json' else protocol_path.read_text()
        if not historical_identity:
            identity_file=REPO/'campaigns'/campaign/'identity.json'
            if identity_file.exists():
                historical_identity=json.loads(identity_file.read_text())
            elif isinstance(proto,dict) and 'source' in proto:
                historical_identity={'source_file_hashes':proto['source'],
                                     'commit_recorded':False,'note':'Do not infer a run commit from a later documentation commit.'}
        stage = {
            'A_idea': 'RECOVERED', 'B_paper': 'SHARED_MANUSCRIPT',
            'C_method': 'SPECIFIED_FOR_BOUNDED_SCOPE',
            'D_partial_implementation': 'PRESENT', 'E_full_implementation': 'PARTIAL_ORIGINAL_SCOPE',
            'F_smoke_test': 'PRESENT_ENGINEERING_ONLY', 'G_benchmark': 'EXECUTED_BOUNDED',
            'H_ablations': 'EXECUTED_BOUNDED_WITH_ORIGINAL_GAPS',
            'I_real_completed_experiment': 'EXECUTED_WITH_ALL_FAILURES_RETAINED',
            'J_analyzed_results': 'PRESENT', 'K_publication_ready': 'NO',
        }
        item = dict(id=pid, canonical_name=old['project'], aliases=old['aliases'],
                    source_path=str(code), repository=str(REPO), branch=snapshot['branch'],
                    head_commit=snapshot['head'], working_tree_state_at_start='CLEAN',
                    current_changes='Packaging and source-resolution verification repairs; numerical experiment code unchanged.',
                    hypothesis=old['hypothesis'], research_question=old['research_question'],
                    contribution=old['central_claim'], original_spec=old['planning_spec'],
                    manuscript_path=str(REPO/'paper/preprint.md'), manuscript_relation='One shared paper, not nine papers',
                    code_path=str(code), dataset=dataset, benchmark=campaign,
                    existing_results=result, result_artifact=ref(analysis_path),
                    frozen_protected_protocol=ref(protocol_path), historical_source_identity=historical_identity,
                    dependencies=['CPU float64 reference runtime', 'Recorded per-study data and source hashes',
                                  'External evaluator for confirmation'],
                    blockers=[blocker, 'Authorship, licensing, novelty review and publication approval unresolved.'],
                    completion_state=state, completion_scope='Original research project; bounded negative findings do not close omitted obligations.',
                    stages=stage, code_files=relevant, primary_campaign_files=raw,
                    original_record_preserved_at='publication_audit/20260924/PROJECT_REGISTRY.json')
        projects.append(item)
        contracts.append(dict(project=pid, artifact=ref(protocol_path), original_contract=proto,
                              interpretation='Historical development contract; not retrospectively preregistered confirmation.'))
        # A full artifact-backed index of headline tables, including every seed and failed cell.
        fields = {'qlearn':['factorial','paired_contrasts','per_seed'], 'qapen':['table','per_seed','comparisons'],
                  'qwipii':['rows_replayed','ranking_only_nonshortest','training_models_exactly_refit'],
                  'wcode':['audit','cells','contrasts'], 'wfim':['summary','models_reloaded','predictions_replayed'],
                  'wft':['table','cells','contrasts'], 'wpinn':['audit','summary'],
                  'cwlnn':['audit','summary','paired_comparisons'], 'ultron':['gates']}[pid]
        values = {k:history[k] for k in fields}
        if pid=='ultron': values={'gates': {'ultron': history['gates']['ultron']}}
        secondary=[]
        if pid=='qlearn':
            path=REPO/'docs/execution/development-v2/analysis.json'
            development=json.loads(path.read_text())
            values['original_digit_cells']=development['digit_cells']
            values['original_digit_comparisons']=development['digit_comparisons']
            values['natural_tuning_failures']=development['natural_tuning_failures']
            secondary.append(ref(path))
        claims.append(dict(id=pid+'-bounded-results', project=pid, claim=result,
                           epistemic_status='DEVELOPMENT_EVIDENCE', analysis=ref(analysis_path),
                           values=values, config=ref(protocol_path), raw_files=raw,
                           secondary_analyses=secondary,
                           code_files=relevant, historical_source_identity=analysis_identity,
                           failures='All original campaign/run files retained; null primary means are not replaced by survivor means.',
                           independent_replication=False))
        dossier = [f'# {old["project"]} — closure dossier', '', f'Final state: **{state}** (original project scope).', '',
                   '## Recovered science', '', old['research_question'], '', old['hypothesis'], '',
                   'Original intended contribution: '+old['central_claim'], '',
                   f'Original mathematical/algorithmic specification: `{old["planning_spec"]}`.',
                   f'Implemented method: `world-series/src/world_series/{pid}/`.', '',
                   '## Experimental contract', '', dataset, '', f'Exact historical settings: `world-series/{protocol}`.',
                   'The linked contract defines the implemented development slice. Unspecified original-scope decisions remain blockers.', '',
                   '## Results, ablations and limitations', '', result, '', f'Analysis: `world-series/{analysis}`.',
                   f'Raw data, checkpoints and failures: `world-series/campaigns/{campaign}/`.', '',
                   blocker, '', '## Manuscript and reproduction', '',
                   'The shared manuscript is `world-series/paper/preprint.md`; this dossier is not a separate paper.',
                   'Use the collection claim index and verification receipts. Same-host replay is not independent confirmation.', '',
                   'Authorship, licensing, novelty review and publication approval remain unresolved.']
        (OUT/'projects').mkdir(exist_ok=True)
        (OUT/'projects'/f'{pid}.md').write_text('\n'.join(dossier)+'\n')
    counts = dict(collections.Counter(p['completion_state'] for p in projects))
    registry = dict(schema_version=1, source_manifest='../FINAL_RESEARCH/SOURCE_MANIFEST.json',
                    scope=str(ROOT), recovered_projects=len(projects), genuinely_distinct_projects=len(projects),
                    source_head=snapshot['head'], projects=projects, final_state_counts=counts,
                    relationships=[dict(type='shared_implementation', projects=list(DETAILS), repository='world-series'),
                                   dict(type='overlapping_data', projects=['wcode','ultron'], evidence='world-series/docs/closure/WCODE_ULTRON_OVERLAP.json'),
                                   dict(type='planning_aliases', detail='Nine empty sibling directories and planning-pack copies are preserved, not counted as new research.')],
                    excluded_prompt_sections=['Bu1LD', 'VertexED', 'FinanceMeta', 'Olympus'],
                    exclusion_reason='No corresponding product or Olympus implementation in the authorized current collection.')
    dump(OUT/'REGISTRY.json', registry)
    dump(REPO/'results/claim_index.json', dict(schema_version=1, source_head=snapshot['head'], claims=claims))
    # JSON is valid YAML 1.2 and avoids introducing another runtime dependency.
    dump(ROOT/'FINAL_RESEARCH/PROTOCOL.yaml', dict(
        schema_version=1, scope='Finite verification and closure of existing World Series evidence',
        historical_results_already_observed=True, new_confirmatory_experiments=False,
        confirmation='DRAFT_NOT_AUTHORIZED', supersedes_existing_protocols=False,
        seeds_splits_metrics_models_baselines_ablations_ood='Verbatim per-study contracts below; no outcome-dependent modifications.',
        temporal_cutoff='Initial source manifest snapshot; historical acquisition/protocol dates retained in original files.',
        stopping_rule='Verify existing outputs, complete interrupted exact replay in fresh outputs, reconcile all nine identities; do not retune negative results.',
        compute=dict(machine_memory_gib=16, numerical_workers=1, device='CPU', threads=1,
                     timeout_per_verification_seconds=1800, scratch='world-series/.work-tmp/finite-closure'),
        success_criteria=dict(engineering='Declared checks pass and original raw artifacts stay unchanged.',
                              science='Original per-study outcomes retained; no claim beyond executed design.',
                              confirmation='Requires independently frozen evaluator/protocol; absent.'),
        study_contracts=contracts))
    lines = ['# Claims and evidence', '',
             'All quantitative headline tables are transcribed programmatically from the linked JSON, including failed cells and null means.',
             'Machine-readable exact values, raw-file hashes, source identities, configs and checkpoints: `world-series/results/claim_index.json`.', '',
             '| Project | Bounded finding | Analysis | Raw campaign |', '|---|---|---|---|']
    for p in projects:
        lines.append(f'| {p["id"]} | {p["existing_results"]} | `{p["result_artifact"]["path"]}` | `world-series/campaigns/{p["benchmark"]}/` |')
    lines += ['', 'Scope: same-host development evidence. No independent replication or publication-readiness claim.',
              'The initial snapshot preserves 181 run manifests including failed, interrupted, unsupported and historically RUNNING receipts.',
              'The stale RUNNING artifact is a historical attempt, not an active worker; see `world-series/docs/closure/RECOVERY.json`.']
    (ROOT/'FINAL_RESEARCH/CLAIMS_EVIDENCE.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'projects':len(projects), 'states':counts, 'claims':len(claims)}))


if __name__ == '__main__':
    main()
