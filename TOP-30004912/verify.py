# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def check(n,E,blocks):
    cuts={}
    for mask in range(1,1<<(n-1)):
        S={v+1 for v in range(n-1) if mask>>v&1};cross=frozenset(i for i,(a,b,w) in enumerate(E) if (a in S)!=(b in S));cuts[cross]=sum(E[i][2] for i in cross)
    lam=min(cuts.values())
    units=[]
    for ids in blocks:
        units.extend([frozenset(ids)] if len(ids)==1 else [frozenset(p) for p in itertools.combinations(ids,2)])
    assert min(sum(E[i][2] for i in U) for U in units)==lam
    for U in units:assert U in cuts
    if lam==0:return 0
    actual={C for C,w in cuts.items() if 3*w<=4*lam};encoded={U for U in units if 3*sum(E[i][2] for i in U)<=4*lam}
    assert actual==encoded;return len(cuts)
cases=0;cutcount=0;zeros=0
for _ in range(240):
    n=1;E=[];blocks=[]
    while n<8:
        a=rng.randrange(n)
        if rng.randrange(2) or n>5:
            ids=[len(E)];E.append((a,n,rng.randrange(7)));n+=1
        else:
            size=rng.randrange(3,5);verts=[a]+list(range(n,n+size-1));n+=size-1;ids=[]
            for u,v in zip(verts,verts[1:]+verts[:1]):ids.append(len(E));E.append((u,v,rng.randrange(7)))
        blocks.append(ids)
    count=check(n,E,blocks)
    if count:cases+=1;cutcount+=count
    else:zeros+=1
# Guaranteed positive-mincut weighted examples, including zero individual cycle edges.
for length in range(3,11):
    E=[(i,(i+1)%length,0 if i==0 else 2+(i%3)) for i in range(length)];cutcount+=check(length,E,[list(range(length))]);cases+=1
RESULTS=dict(positive_mincut_cases=cases,zero_mincut_skipped=zeros,unordered_cuts_enumerated=cutcount,oracle='all nontrivial vertex bipartitions with vertex0 fixed to one side')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
