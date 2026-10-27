# SPDX-License-Identifier: Apache-2.0
from fractions import Fraction as F
from itertools import product,permutations
from random import Random
import json

if not __debug__:
    raise RuntimeError('Run with assertions enabled')
rng=Random(386373)
def matchings(lists):
    return [a for a in product(*[[-1]+x for x in lists]) if len([h for h in a if h>=0])==len(set(h for h in a if h>=0))]
def score(a,orders,R,indices=None):
    v=[0]*R
    for i in range(len(a)) if indices is None else indices:
        if a[i]>=0:v[orders[i].index(a[i])]+=1
    return tuple(v)
cases=0
for n in range(1,5):
 for m in range(1,5):
  for repeat in range(20):
    lists=[[h for h in range(m) if rng.random()<0.75] for _ in range(n)]
    baseline=[]
    for li in lists:
        li=li[:];rng.shuffle(li);baseline.append(li)
    k=min(n,1+repeat%2);U=list(range(k));D=list(range(k,n))
    supports=[]
    for i in U:
        perms=list(permutations(lists[i]));rng.shuffle(perms)
        supports.append(perms[:min(3,len(perms))])
    profiles=[]
    for orders in product(*supports):
        p=baseline[:]
        for i,order in zip(U,orders):p[i]=list(order)
        profiles.append(p)
    R=max(map(len,lists),default=0)
    matches=matchings(lists)
    # Brute-force oracle over every matching and every realized profile.
    optimum=[max(score(a,p,R) for a in matches) for p in profiles]
    probability={a:F(sum(score(a,p,R)==v for p,v in zip(profiles,optimum)),len(profiles)) for a in matches}
    # Reduction: enumerate only uncertain assignments, select one residual
    # matching by deterministic original ranks before looking at profiles.
    candidates=[]
    for ua in product(*[[-1]+lists[i] for i in U]):
        real=[h for h in ua if h>=0]
        if len(real)!=len(set(real)):continue
        extending=[a for a in matches if tuple(a[i] for i in U)==ua]
        candidate=max(extending,key=lambda a:score(a,baseline,R,D))
        candidates.append(candidate)
        for a in extending:
            for p,v in zip(profiles,optimum):
                assert score(candidate,p,R)>=score(a,p,R)
                if score(a,p,R)==v:assert score(candidate,p,R)==v
    assert max(probability[a] for a in candidates)==max(probability.values())
    cases+=1
print(json.dumps({'status':'PASS','instances':cases,'applicants':'1..4','houses':'1..4','uncertain_applicants':'1 or 2','seed':386373,'arithmetic':'exact rank vectors and fractions','scope':'candidate dominance and exact optimum against exhaustive oracle'}))
