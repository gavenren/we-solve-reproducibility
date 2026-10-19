# SPDX-License-Identifier: Apache-2.0
"""Exact finite diagnostic; infinite claims depend on the companion proof."""
import sys
if not __debug__:
    raise SystemExit("Refusing optimized Python: assertions must remain enabled")

from fractions import Fraction as F
from random import Random
from heapq import heappop,heappush
rng=Random(7113);cases=0;pairs=0
for trial in range(140):
    n=1;blocks=[];adj=[[]]
    for j in range(rng.randrange(1,6)):
        parent=rng.randrange(n);length=rng.choice([2,3,4,5,6])
        verts=[parent]+list(range(n,n+length-1));n+=length-1
        while len(adj)<n:adj.append([])
        es=list(zip(verts,verts[1:])) if length==2 else list(zip(verts,verts[1:]+verts[:1]))
        weights=[F(rng.randrange(1,15),rng.randrange(1,5)) for e in es]
        for (a,b),w in zip(es,weights):adj[a].append((b,w));adj[b].append((a,w))
        blocks.append((verts,weights))
    coords=[[] for _ in range(n)]
    for verts,weights in blocks:
        # Find physical gates independently by deleting every block edge and BFS.
        forbidden={frozenset(e) for e in (list(zip(verts,verts[1:])) if len(verts)==2 else list(zip(verts,verts[1:]+verts[:1])))}
        gates={}
        for v in verts:
            q=[v];seen={v}
            for a in q:
                gates[a]=v
                for b,w in adj[a]:
                    if frozenset([a,b]) not in forbidden and b not in seen:seen.add(b);q.append(b)
        assert len(gates)==n
        if len(verts)==2:
            local={verts[0]:[F(0)],verts[1]:[weights[0]]}
        else:
            L=sum(weights);pos=[F(0)]
            for w in weights[:-1]:pos.append(pos[-1]+w)
            bounds=sorted(set([F(0),L]+[z for p in pos for z in [p,(p+L/2)%L]]))
            local={v:[] for v in verts}
            for a,b in zip(bounds,bounds[1:]):
                mid=(a+b)/2
                for v,p in zip(verts,pos):local[v].append((b-a)/2 if (mid-p)%L<L/2 else F(0))
        for v in range(n):coords[v].extend(local[gates[v]])
    for start in range(n):
        ds={start:F(0)};heap=[(F(0),start)]
        while heap:
            d,a=heappop(heap)
            if ds[a]!=d:continue
            for b,w in adj[a]:
                z=d+w
                if b not in ds or z<ds[b]:ds[b]=z;heappush(heap,(z,b))
        for end in range(n):
            exact=sum(abs(a-b) for a,b in zip(coords[start],coords[end]))
            assert exact==ds[end];pairs+=1
    cases+=1
print('PASS',cases,'rational weighted cacti;',pairs,'pairwise L1 distances equal independent Dijkstra shortest paths')
