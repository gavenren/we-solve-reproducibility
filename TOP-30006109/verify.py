# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def inspect(n,E):
    deg=[0]*n
    for a,b in E:deg[a]+=1;deg[b]+=1
    if max(deg,default=0)>3:return None
    paths=[(a,b) for a,b in E]+[(v,) for v in range(n) for _ in range(3-deg[v])]
    assert all(sum(v in P for P in paths)==3 for v in range(n))
    profit=[sum(v in P for P in paths) for v in range(n)]
    best=0
    for mask in range(1<<n):
        if all(sum(mask>>v&1 for v in P)<=1 for P in paths):best=max(best,sum(profit[v] for v in range(n) if mask>>v&1))
    # Separate oracle: minimum vertex cover, rather than maximizing independent sets.
    cover=min(mask.bit_count() for mask in range(1<<n) if all(mask>>a&1 or mask>>b&1 for a,b in E))
    assert best==3*(n-cover);return best
cases=0
for n in range(1,6):
    pairs=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        if inspect(n,[e for i,e in enumerate(pairs) if mask>>i&1]) is not None:cases+=1
for _ in range(300):
    n=8;E=[];deg=[0]*n
    for a,b in rng.sample(list(itertools.combinations(range(n),2)),28):
        if deg[a]<3 and deg[b]<3 and rng.randrange(2):E.append((a,b));deg[a]+=1;deg[b]+=1
    inspect(n,E);cases+=1
RESULTS=dict(cases=cases,exhaustive_subcubic_orders=[1,5],random_order=8,oracle='all minimum vertex covers vs all star path-budget feasible selections',checks='actual path lists, congestion exactly3, profit coefficient3, objective equality')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
