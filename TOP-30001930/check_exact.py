# SPDX-License-Identifier: Apache-2.0
"""Exact finite diagnostic; infinite claims depend on the companion proof."""
import sys
if not __debug__:
    raise SystemExit("Refusing optimized Python: assertions must remain enabled")

from itertools import combinations,permutations
from collections import deque
cases=0
for n in range(2,6):
    pairs=list(combinations(range(n),2))
    for mask in range(1,1<<len(pairs)):
        edges=[e for i,e in enumerate(pairs) if mask>>i&1]
        adj=[set() for _ in range(n)]
        for a,b in edges:adj[a].add(b);adj[b].add(a)
        seen={0};todo=[0]
        for u in todo:
            for v in adj[u]-seen:seen.add(v);todo.append(v)
        if len(seen)<n:continue
        # Independently enumerate all acyclic orientations from all vertex orders.
        orient=set()
        for order in permutations(range(n)):
            pos={v:i for i,v in enumerate(order)}
            orient.add(sum((pos[a]<pos[b])<<i for i,(a,b) in enumerate(edges)))
        neigh={z:[z^(1<<i) for i in range(len(edges)) if z^(1<<i) in orient] for z in orient}
        diameter=0
        for start in orient:
            dist={start:0};q=deque([start])
            while q:
                z=q.popleft()
                for v in neigh[z]:
                    if v not in dist:dist[v]=dist[z]+1;q.append(v)
            assert len(dist)==len(orient)
            diameter=max(diameter,max(dist.values()))
        assert diameter<=len(edges)<=n*(n-1)//2
        cases+=1
print('PASS',cases,'connected labelled simple graphs on2..5vertices; exact all-pairs orientation-graph diameters')
