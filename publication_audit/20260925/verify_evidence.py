"""Read-only audit calculations. Outputs only to this audit directory."""
from pathlib import Path
import hashlib, json, statistics, subprocess, datetime

ROOT=Path(__file__).resolve().parents[2]
REPO=ROOT/'world-series'
OUT=Path(__file__).resolve().parent/'receipts'
def read(p): return json.loads((ROOT/p).read_text())
def digest(p): return hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
def mean(xs): return statistics.mean(xs)
index=read('world-series/results/claim_index.json')
refs={}
def walk(x):
    if isinstance(x,dict):
        if isinstance(x.get('path'),str) and isinstance(x.get('sha256'),str):
            refs.setdefault(x['path'],set()).add(x['sha256'])
        for v in x.values():walk(v)
    elif isinstance(x,list):
        for v in x:walk(v)
walk(index)
bad=[]; alternate_roots=[]
for p,hashes in refs.items():
    f=ROOT/p
    if not f.is_file() and (REPO/p).is_file() and digest(REPO/p) in hashes:
        alternate_roots.append({'path':p,'resolved':str((REPO/p).relative_to(ROOT)),'sha256':digest(REPO/p)})
    elif not f.is_file():bad.append({'path':p,'error':'missing'})
    elif digest(f) not in hashes or len(hashes)!=1:bad.append({'path':p,'error':'hash mismatch','actual':digest(f),'expected':sorted(hashes)})
final=read('FINAL_RESEARCH/FINAL_SOURCE_MANIFEST.json')
manifest_bad=[p for p,h in final['current_files'].items() if not (ROOT/p).is_file() or digest(ROOT/p)!=h]
wft=read('world-series/docs/closure/WFT_RESULTS.json')
rows=wft['raw_rows'];transfer=[r for r in rows if r['groups'] in [32,64]]
calc={}
for method in wft['per_seed']:
    vals=[mean([r['relative_prediction_error'] for r in transfer if r['method']==method and str(r['seed'])==seed]) for seed in wft['per_seed'][method]]
    calc[method]=mean(vals)
keys=['samples','noise','groups','topology','level']
ctrl={tuple(r[k] for k in keys):r['relative_prediction_error'] for r in wft['cells'] if r['method']=='unconstrained'}
cells=[r for r in wft['cells'] if r['method']=='both']
badcells=[r for r in cells if r['relative_prediction_error']>ctrl[tuple(r[k] for k in keys)]]
wfim=read('world-series/campaigns/wfim-coordinate-development-v1/summary.json')
wfim_calc=[]
for task in ['order','count']:
    for split in ['template','length']:
        group={kind:{r['seed']:r for r in wfim if r['task']==task and r['kind']==kind} for kind in ['learned_coordinates','identity_coordinates']}
        a=group['learned_coordinates'];b=group['identity_coordinates']
        diffs=[a[s]['mse'][split]-b[s]['mse'][split] for s in sorted(a)]
        am=mean([r['mse'][split] for r in a.values()]);bm=mean([r['mse'][split] for r in b.values()])
        wfim_calc.append(dict(task=task,split=split,learned=am,identity=bm,paired_differences=diffs,worse_seeds=sum(x>0 for x in diffs),relative_change=am/bm-1))
qrows=[json.loads(x) for x in (REPO/'campaigns/qwipii-learned-development-v1/rows.jsonl').read_text().splitlines()]
qcalc={}
for method in sorted({r['method'] for r in qrows}):
    rr=[r for r in qrows if r['method']==method]
    qcalc[method]=dict(n=len(rr),solved=sum(r['status']=='solved' for r in rr),expansions=mean(r['expansions'] for r in rr),ms=mean(r['elapsed_ns']/1e6 for r in rr))
brute={(r['seed'],r['start']):len(r['path']) for r in qrows if r['method']=='brute'}
qcalc['longer_paths']={method:sum(len(r['path'])>brute[r['seed'],r['start']] for r in qrows if r['method']==method) for method in qcalc}
gate=read('world-series/docs/closure/GATE_RESULTS.json')
source_files=[REPO/'paper/preprint.md',REPO/'paper/preprint.tex',REPO/'paper/preprint.pdf',REPO/'results/claim_index.json']
result=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),head=subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip(),source_hashes={str(p.relative_to(ROOT)):digest(p) for p in source_files},claim_index=dict(unique_paths=len(refs),mismatches=bad),final_source_manifest=dict(paths=len(final['current_files']),mismatches=manifest_bad),wft=dict(total_rows=len(rows),transfer_rows=len(transfer),means=calc,relative_error_reduction=1-calc['both']/calc['unconstrained'],all_condition_losses=len(badcells),all_conditions=len(cells),transfer_condition_losses=sum(r['groups']>16 for r in badcells),transfer_conditions=sum(r['groups']>16 for r in cells),loss_conditions=badcells),wfim=wfim_calc,qwipii=qcalc,scope='Recalculation from preserved rows and full claim-index hash verification; not new training or independent reproduction.')
result['claim_index']['mixed_path_roots']=alternate_roots
(OUT/'evidence_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['wfim','qwipii','wft']},indent=2))
print('WFT',len(rows),len(transfer),calc,'reduction',result['wft']['relative_error_reduction'])
print('WFIM',wfim_calc)
print('QWIPII',qcalc)
