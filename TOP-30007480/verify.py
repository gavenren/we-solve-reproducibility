# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def solve(n,E):
    # Supplied ordering is 0..n-1; create an actual nice path decomposition.
    future=[max([v]+[b for a,b in E if a==v]) for v in range(n)]
    bag=[];dp={0:(0,())};p=0;D=0
    def step(kind,v=None,edge=None):
        nonlocal bag,dp,p,D
        D+=1;new={}
        def keep(mask,score,wit):
            if mask not in new or new[mask][0]<score:new[mask]=(score,wit)
        if kind=='intro':
            bag.append(v);new=dp.copy()
        elif kind=='edge':
            u,v=edge;iu=bag.index(u);iv=bag.index(v);bits=(1<<iu)|(1<<iv)
            for mask,(score,wit) in dp.items():
                keep(mask,score,wit)
                if mask&bits==0:keep(mask|bits,score+1,wit+(edge,))
        else:
            i=bag.index(v)
            for mask,(score,wit) in dp.items():keep((mask&((1<<i)-1))|((mask>>(i+1))<<i),score,wit)
            bag.pop(i)
        dp=new;p=max(p,len(bag))
    for v in range(n):
        step('intro',v=v)
        for u,b in E:
            if b==v:step('edge',edge=(u,v))
        for u in list(bag):
            if future[u]<=v:step('forget',v=u)
    assert bag==[];score,wit=dp[0]
    assert len(wit)==score and len({v for e in wit for v in e})==2*score and set(wit)<=set(E)
    return score,p,D

def brute(n,E):
    # Independent recursion on vertices, with an unmatched branch.
    adj=[set() for _ in range(n)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    def go(S):
        if not S:return 0
        a=min(S);T=S-{a};return max([go(T)]+[1+go(T-{b}) for b in adj[a]&T])
    return go(set(range(n)))
cases=0;maxp=0
for n in range(6):
    es=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(es)):
        E=[e for i,e in enumerate(es) if mask>>i&1];ans,p,D=solve(n,E)
        assert ans==brute(n,E);maxp=max(maxp,p);cases+=1
for _ in range(300):
    n=rng.randrange(6,11);E=[e for e in itertools.combinations(range(n),2) if rng.randrange(4)==0];ans,p,D=solve(n,E)
    assert ans==brute(n,E);cases+=1
RESULTS=dict(cases=cases,exhaustive_graph_order=[0,5],random_graph_order=[6,10],max_exhaustive_bag_size=maxp,oracle='recursive matched/unmatched vertex enumeration',checks='actual introduce-edge-forget DP and matching witness')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
