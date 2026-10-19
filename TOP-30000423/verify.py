# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def forest(g,E):
    seen=set();adj=[[] for _ in range(g)]
    for a,b in E:adj[a].append(b);adj[b].append(a)
    def go(v,p):
        if v in seen:return False
        seen.add(v);return all(go(u,v) for u in adj[v] if u!=p)
    return all(go(v,-1) for v in range(g) if v not in seen)
def root(g,E,sizes,k):
    if g==1 and sizes==[1]:return {0:[]},[0]
    adj={i:[] for i in range(g)};nextid=g
    def path(a,b,length):
        nonlocal nextid
        for z in range(length-1):
            c=nextid;nextid+=1;adj[c]=[];adj[a].append(c);adj[c].append(a);a=c
        adj[a].append(b);adj[b].append(a)
    for a,b in E:path(a,b,k//2)
    leaves=[]
    for a,size in enumerate(sizes):
        for _ in range(size):
            l=nextid;nextid+=1;adj[l]=[];path(a,l,1);leaves.append(l)
    comp=[];seen=set()
    for a in range(g):
        if a in seen:continue
        comp.append(a);q=[a];seen.add(a)
        for v in q:
            for u in adj[v]:
                if u not in seen:seen.add(u);q.append(u)
    for a,b in zip(comp,comp[1:]):path(a,b,k+1)
    return adj,leaves
cases=0
for g in range(1,5):
    pairs=list(itertools.combinations(range(g),2))
    for mask in range(1<<len(pairs)):
        E=[e for i,e in enumerate(pairs) if mask>>i&1]
        if not forest(g,E):continue
        for sizes in itertools.product([1,2],repeat=g):
            sizes=list(sizes);groups=[a for a,s in enumerate(sizes) for _ in range(s)]
            for k in range(5,11):
                adj,leaves=root(g,E,sizes,k)
                assert sum(map(len,adj.values()))==2*(len(adj)-1)
                for v,neigh in adj.items():
                    if len(adj)>1:assert (len(neigh)==1)==(v in leaves)
                for i,l in enumerate(leaves):
                    dist={l:0};q=[l]
                    for v in q:
                        for u in adj[v]:
                            if u not in dist:dist[u]=dist[v]+1;q.append(u)
                    assert len(dist)==len(adj)
                    for j in range(i):
                        expected=groups[i]==groups[j] or tuple(sorted((groups[i],groups[j]))) in E
                        assert (dist[leaves[j]]<=k)==expected
                cases+=1
RESULTS=dict(cases=cases,quotient_vertices=[1,4],class_sizes=[1,2],leaf_thresholds=[5,10],oracle='all-pairs BFS distances in explicit unit-edge tree',checks='tree, no extra leaves, exact induced adjacency')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
