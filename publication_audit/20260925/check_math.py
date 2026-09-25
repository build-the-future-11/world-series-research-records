import json, torch, numpy as np
from pathlib import Path
from world_series.wfim.algebra import SparseWordSeries, add, word_norm
from world_series.wfim.learning import CompositionModel
from world_series.wft.constraints import teacher, domain, restriction
from world_series.wpinn.structured import compact_tests

r={}
z=SparseWordSeries({});x=SparseWordSeries({(0,):1e-16})
r['legacy_add_zero_counterexample']={'input':x.coeffs[(0,)],'output':add(z,x).coeffs,'scope':'Threshold pruning violates exact additive identity; headline dense coordinate encoder does not use this add function.'}
r['legacy_invalid_radius_norm']=word_norm(SparseWordSeries({(0,):1},r=-1))
torch.manual_seed(20260925)
m=CompositionModel('learned_coordinates');identity=CompositionModel('identity_coordinates')
with torch.no_grad():m.algebra.theta.uniform_(-.5,.5)
tokens=torch.tensor([[0,0,1,-1],[1,0,1,0]],dtype=torch.long)
s=m.algebra.scales()
weights=torch.stack([torch.stack([s[a+1] for a in w]).prod() if w else s.new_tensor(1.) for w in m.algebra.words])/s
r['wfim_feature_reweighting_max_error']=float((m.encode(tokens)-identity.encode(tokens)*weights).abs().max().detach())
m=teacher(2203);checks=[]
for topology in ['cycle','path']:
    for groups in [16,32,64]:
        fine,coarse=domain(groups,topology,0),domain(groups,topology,1)
        a,b=m.action(fine),m.action(coarse);R=restriction(groups);P=2*R.T
        checks.append({'groups':groups,'topology':topology,'intertwining':float((R@a-b@R).abs().max().detach()),'congruence':float((m.laplacian(coarse)-P.T@m.laplacian(fine)@P).abs().max().detach()),'semigroup':float((R@m.transition(fine)-m.transition(coarse)@R).abs().max().detach())})
r['wft_contracts']=checks
psi,_=compact_tests(np.linspace(0,5,81))
r['weak_test_endpoint_max']=float(np.abs(psi[[0,-1]]).max())
r['scope']='Targeted contract challenges, not formal verification of all code or independent reproduction.'
(Path(__file__).parent/'receipts/math_checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
