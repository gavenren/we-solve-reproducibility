# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def partition(n,E,S,q,beta,lam):
    rest=[v for v in range(n) if v not in S];adj={v:[] for v in rest}
    for a,b in E:
        if a in adj and b in adj:adj[a].append(b);adj[b].append(a)
    parent={};order=[];roots=[]
    for r in rest:
        if r in parent:continue
        roots.append(r);parent[r]=-1;stack=[r]
        for v in stack:
            order.append(v)
            for u in adj[v]:
                if u==parent[v]:continue
                assert u not in parent;parent[u]=v;stack.append(u)
    zp=F(0);zh=F(0)
    for colors in itertools.product(range(q),repeat=len(S)):
        a=dict(zip(S,colors));factor=beta**sum(a[u]==a[v] for u,v in E if u in a and v in a);D={}
        for v in reversed(order):
            D[v]=[]
            for c in range(q):
                value=beta**sum(c==a[s] for x,s in E if x==v and s in a)*beta**sum(c==a[s] for s,x in E if x==v and s in a)
                for u in adj[v]:
                    if parent.get(u)==v:value*=sum(D[u][d]*(beta if c==d else 1) for d in range(q))
                D[v].append(value)
        for r in roots:factor*=sum(D[r])
        zp+=factor
    for bits in itertools.product(range(2),repeat=len(S)):
        chosen={v for v,b in zip(S,bits) if b}
        if any(a in chosen and b in chosen for a,b in E):continue
        D={};factor=lam**len(chosen)
        for v in reversed(order):
            children=[u for u in adj[v] if parent.get(u)==v];zero=F(1);one=F(0) if any((a==v and b in chosen) or (b==v and a in chosen) for a,b in E) else lam
            for u in children:zero*=sum(D[u]);one*=D[u][0]
            D[v]=(zero,one)
        for r in roots:factor*=sum(D[r])
        zh+=factor
    return zp,zh
cases=0;assignments=0
for _ in range(140):
    n=rng.randrange(1,9);S=tuple(sorted(rng.sample(range(n),rng.randrange(min(4,n)+1))));rest=[v for v in range(n) if v not in S];E=[]
    for j,v in enumerate(rest):
        if j and rng.randrange(3):E.append(tuple(sorted((v,rng.choice(rest[:j])))))
    for a,b in itertools.combinations(range(n),2):
        if (a in S or b in S) and rng.randrange(2):E.append((a,b))
    E=sorted(set(E));q=rng.choice([2,3]);beta=rng.choice([F(3,2),F(2),F(7,3)]);lam=rng.choice([F(1,2),F(2),F(3,2)])
    wantp=sum(beta**sum(x[a]==x[b] for a,b in E) for x in itertools.product(range(q),repeat=n))
    wanth=sum((lam**mask.bit_count() for mask in range(1<<n) if all(not(mask>>a&1 and mask>>b&1) for a,b in E)),F(0))
    assert partition(n,E,S,q,beta,lam)==(wantp,wanth);cases+=1;assignments+=q**n+(1<<n)
RESULTS=dict(cases=cases,assignments_enumerated=assignments,graph_orders=[1,8],feedback_set_size=[0,4],q_values=[2,3],oracle='all spin assignments and all independent vertex subsets',arithmetic='Fraction')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
