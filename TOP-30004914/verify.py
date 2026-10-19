# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def allmatchings(n,E):
    adj=[set() for _ in range(n)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    def go(S):
        if not S:yield ();return
        a=min(S);T=S-{a}
        yield from go(T)
        for b in sorted(adj[a]&T):
            for M in go(T-{b}):yield ((a,b),)+M
    return list(go(set(range(n))))
cases=0;allk=0
for n in [0,2,4,6,8]:
    pairs=list(itertools.combinations(range(n),2))
    patterns=itertools.product([0,1,2],repeat=len(pairs)) if n<=4 else ([rng.randrange(3) for _ in pairs] for z in range(300))
    for pattern in patterns:
        E={e:int(v==2) for e,v in zip(pairs,pattern) if v};ms=allmatchings(n,E);t=n//2
        chosen=max(ms,key=lambda M:sum(t+1+E[e] for e in M));pms=[M for M in ms if len(M)==t]
        assert (len(chosen)==t)==bool(pms)
        if pms:
            a,b=F(-7,3),F(5,2)
            def direct(M,k):return sum(sorted([b if E[e] else a for e in M],reverse=True)[:k])
            h=sum(E[e] for e in chosen)
            for k in range(t+1):
                assert direct(chosen,k)==max(direct(M,k) for M in pms)==k*a+(b-a)*min(k,h);allk+=1
        cases+=1
RESULTS=dict(cases=cases,k_objectives=allk,exhaustive_graph_orders=[0,2,4],random_graph_orders=[6,8],oracle='all graph matchings and direct sorted rational weights',limits='enumeration verifies reduction; it is not the imported polynomial weighted-matching subroutine')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
