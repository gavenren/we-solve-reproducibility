# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def meet(a,b):return a if a==b else 0
def join(a,b):return a if a==b else b if a==0 else a if b==0 else 0
def dist(a,b):return 0 if a==b else 1 if a==0 or b==0 else 2
def canon(x):
    used={0:0};ans=[]
    for a in x:
        if a not in used:used[a]=len(used)
        ans.append(used[a])
    return tuple(ans)
patterns=sorted({canon(x) for x in itertools.product(range(5),repeat=4)});cert=[]
for a,b,c,d in patterns:
    s=dist(a,b)+dist(c,d)-dist(meet(a,c),meet(b,d))-dist(join(a,c),join(b,d));assert s>=0;cert.append((''.join(map(str,(a,b,c,d))),s))
assert len(patterns)==52 and Counter(s for _,s in cert)==Counter({0:32,2:16,4:4})
def solve(n,k,E,phi):
    ch=[[] for _ in range(n)]
    for a,b,w in E:ch[a].append((b,w))
    D=[None]*n
    for v in range(n-1,-1,-1):D[v]=[phi[v][a]+sum(min(D[u][b]+w*dist(a,b) for b in range(k+1)) for u,w in ch[v]) for a in range(k+1)]
    return min(D[0])
def value(x,E,phi):return sum(phi[v][a] for v,a in enumerate(x))+sum(w*dist(x[a],x[b]) for a,b,w in E)
cases=0;inequalities=0
for _ in range(180):
    n=rng.randrange(1,8);k=rng.randrange(2,4);E=[(rng.randrange(v),v,F(rng.randrange(5),rng.randrange(1,4))) for v in range(1,n)]
    phi=[]
    for v in range(n):
        z=F(rng.randrange(-5,6),2);phi.append([z]+[z+F(rng.randrange(6),3) for _ in range(k)])
    want=min(value(x,E,phi) for x in itertools.product(range(k+1),repeat=n));assert solve(n,k,E,phi)==want;cases+=1
    if n<=3:
        states=list(itertools.product(range(k+1),repeat=n))
        for x in states:
            for y in states:
                assert value(x,E,phi)+value(y,E,phi)>=value(tuple(map(meet,x,y)),E,phi)+value(tuple(map(join,x,y)),E,phi);inequalities+=1
RESULTS=dict(cases=cases,global_ksubmodular_inequalities=inequalities,all_52_local_cases=cert,oracle='full assignment enumeration on rational weighted trees')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
