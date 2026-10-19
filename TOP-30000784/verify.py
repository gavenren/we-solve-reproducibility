# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def mons(N,d):return [S for S in range(1<<N) if S.bit_count()<=d]
weightcases=0
for N in range(1,5):
    for d in range(min(N,2)+1):
        ms=mons(N,d);cols=[sum((x&S==S)<<x for x in range(1<<N)) for S in ms]
        values=[0]*(1<<len(ms))
        for p in range(1,1<<len(ms)):
            b=(p&-p).bit_length()-1;values[p]=values[p^(1<<b)]^cols[b];assert values[p].bit_count()>=(1<<(N-d));weightcases+=1
def rank(rows):
    basis={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j not in basis:basis[j]=v;break
            v^=basis[j]
    return len(basis)
cert=[]
for n in range(3,7):
    for m in range(1,n+1):
        N=n+m;ms=mons(N,1)
        for attempt in range(500):
            table=[rng.randrange(1<<m) for _ in range(1<<n)];rows=[]
            for x,y in enumerate(table):
                z=x|(y<<n);rows.append(sum((z&S==S)<<j for j,S in enumerate(ms)))
            r=rank(rows)
            if r==len(ms):break
        assert r==len(ms)
        cert.append(dict(n=n,m=m,degree=1,rank=r,table=table))
RESULTS=dict(nonzero_polynomials_weight_checked=weightcases,weight_lemma_variables=[1,4],weight_lemma_degree_at_most=2,full_rank_graph_certificates=cert,note='exact rank certificates concern these finite maps; n>=16 existence relies on report union bound')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
