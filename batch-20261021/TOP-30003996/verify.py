# SPDX-License-Identifier: Apache-2.0
"""Cactus block factorization against exhaustive global spanning trees."""
import itertools,random,json
from fractions import Fraction
from collections import deque
if not __debug__:
    raise RuntimeError('Refusing -O: assertions are required.')
def orient(n,edges,r):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    parent={r:None};q=deque([r]);arcs=[]
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in parent:parent[v]=u;q.append(v);arcs.append((u,v))
    return arcs if len(parent)==n else None

def all_trees(n,edges):
    return [T for T in itertools.combinations(edges,n-1) if orient(n,T,0) is not None]
def objective(n,T,c,inward=False):
    return sum((c[r,v,u] if inward else c[r,u,v]) for r in range(n) for u,v in orient(n,T,r))
def factor(n,blocks,c):
    edges=[e for B in blocks for e in B];adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    distances=[]
    for r in range(n):
        ds={r:0};q=deque([r])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in ds:ds[v]=ds[u]+1;q.append(v)
        distances.append(ds)
    result=[];bound=Fraction(0)
    for B in blocks:
        vs={v for e in B for v in e};projections=[]
        for r in range(n):
            a=min(vs,key=lambda v:distances[r][v]);assert sum(distances[r][v]==distances[r][a] for v in vs)==1
            projections.append(a)
        candidates=[B] if len(B)==1 else [B[:j]+B[j+1:] for j in range(len(B))]
        scores=[]
        for T in candidates:
            subtotal=Fraction(0)
            local=[[] for _ in range(n)]
            for u,v in T:local[u].append(v);local[v].append(u)
            for r,a in enumerate(projections):
                seen={a};q=[a]
                for u in q:
                    for v in local[u]:
                        if v not in seen:seen.add(v);q.append(v);subtotal+=c[r,u,v]
                assert seen==vs
            scores.append(subtotal)
        j=min(range(len(scores)),key=scores.__getitem__);bound+=scores[j];result+=candidates[j]
    return tuple(result),bound

# Generate block-certified cacti by attaching each fresh cycle/bridge at one old vertex.
rng=random.Random(20261021);graphs=[(1,[])]
for shape in [(1,),(3,),(4,),(1,1,1),(3,3),(3,1,3),(4,3),(1,4,1),(3,1,1)]:
    for trial in range(4):
        n=1;blocks=[]
        for size in shape:
            a=rng.randrange(n)
            if size==1:blocks.append([(a,n)]);n+=1
            else:
                cycle=[a]+list(range(n,n+size-1));n+=size-1
                blocks.append([tuple(sorted((cycle[j],cycle[(j+1)%size]))) for j in range(size)])
        graphs.append((n,blocks))
cases=0;trees_checked=0
for n,blocks in graphs:
    E=[e for B in blocks for e in B];trees=all_trees(n,E);assert trees
    for trial in range(5):
        c={(r,u,v):Fraction(rng.randrange(-15,16),rng.randrange(1,8)) for r in range(n) for e in E for u,v in [e,e[::-1]]}
        T,score=factor(n,blocks,c)
        assert objective(n,T,c)==score==min(objective(n,S,c) for S in trees)
        rev={(r,u,v):c[r,v,u] for r,u,v in c}
        U,in_score=factor(n,blocks,rev)
        assert objective(n,U,c,True)==in_score==min(objective(n,S,c,True) for S in trees)
        trees_checked+=2*len(trees);cases+=2
print(json.dumps({'status':'PASS','certified_cactus_graphs':len(graphs),'rational_cost_convention_cases':cases,'global_spanning_trees_scored':trees_checked,'negative_and_fractional_costs':True,'finite_only':True},indent=2))
