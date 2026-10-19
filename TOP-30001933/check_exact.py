# SPDX-License-Identifier: Apache-2.0
"""Exact finite diagnostic; infinite claims depend on the companion proof."""
import sys
if not __debug__:
    raise SystemExit("Refusing optimized Python: assertions must remain enabled")

from fractions import Fraction as F
def solve(A,b):
    n=len(A);M=[[F(x) for x in r]+[F(z)] for r,z in zip(A,b)]
    for c in range(n):
        piv=next((r for r in range(c,n) if M[r][c]),None)
        if piv is None:return None
        M[c],M[piv]=M[piv],M[c]
        q=M[c][c];M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r!=c:
                q=M[r][c]
                M[r]=[x-q*y for x,y in zip(M[r],M[c])]
    return [r[-1] for r in M]
def rank(A):
    if not A:return 0
    M=[[F(x) for x in r] for r in A];r=0
    for c in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][c]),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
        for i in range(r+1,len(M)):
            q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r

from random import Random
from collections import deque
rng=Random(1933)
def vec_tree(n,edges,deletions):
    chosen=[e for i,e in enumerate(edges) if i not in deletions]
    adj=[[] for _ in range(n)]
    for a,b in chosen:adj[a].append(b);adj[b].append(a)
    seen={0};todo=[0];arcs=[]
    for a in todo:
        for b in adj[a]:
            if b not in seen:seen.add(b);todo.append(b);arcs.append((a,b))
    assert len(seen)==n and len(arcs)==n-1
    # Full physical arc coordinates, independent of cycle cumulative formulas.
    return [int((a,b) in arcs) for e in edges for a,b in [e,e[::-1]]]
cases=0
for _ in range(400):
    n=1;edges=[];cycles=[]
    for j in range(rng.randrange(1,5)):
        parent=rng.randrange(n)
        if rng.randrange(4)==0:
            edges.append((parent,n));n+=1
        else:
            size=rng.randrange(3,7);verts=[parent]+list(range(n,n+size-1));n+=size-1
            ids=[]
            for a,b in zip(verts,verts[1:]+verts[:1]):ids.append(len(edges));edges.append((a,b))
            cycles.append(ids)
    k=rng.randrange(1,12)
    w=[0]*(2*len(edges))
    for j in range(k):
        v=vec_tree(n,edges,{rng.choice(C) for C in cycles})
        w=[a+b for a,b in zip(w,v)]
    options=[];breaks={0,k}
    for C in cycles:
        cs=[w[2*i] for i in C]
        a=[k-cs[0]]+[cs[j-1]-cs[j] for j in range(1,len(C))]
        assert min(a)>=0 and sum(a)==k
        cum=[];z=0
        for t in a:z+=t;cum.append(z);breaks.add(z)
        options.append(cum)
    vs=[];weights=[];ts=sorted(breaks)
    for lo,hi in zip(ts,ts[1:]):
        dels={C[next(j for j,t in enumerate(cum) if hi<=t)] for C,cum in zip(cycles,options)}
        vs.append(vec_tree(n,edges,dels));weights.append(hi-lo)
    assert sum(weights)==k
    assert all(sum(a*v[j] for a,v in zip(weights,vs))==w[j] for j in range(len(w)))
    assert rank([[1]+v for v in vs])==len(vs)
    cases+=1
print('PASS',cases,'weighted bidirected-cactus dilate decompositions; physical rooted-tree reconstruction and exact affine-rank oracle')
