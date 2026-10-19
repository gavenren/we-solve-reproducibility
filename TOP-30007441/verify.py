# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def matchings(v):
    if not v:yield ();return
    a=v[0]
    for b in v[1:]:
        for r in matchings([x for x in v[1:] if x!=b]):yield tuple(sorted(((min(a,b),max(a,b)),)+r))
def image(M,perm):return tuple(sorted(tuple(sorted((perm.get(a,a),perm.get(b,b)))) for a,b in M))
def row(M,n):
    out=defaultdict(F);out[M]+=F(1,2);C=math.comb(n,4)
    for Q in itertools.combinations(range(n),4):
        pats=list(matchings(list(Q)))
        for old in pats:
            for new in pats:
                if old==new:continue
                target=tuple(sorted((set(M)-set(old))|set(new))) if set(old)<=set(M) else M
                out[target]+=F(1,12*C)
    return out
rows_count=0;couplings=0
for n in [4,6,8]:
    states=list(matchings(list(range(n))));rows={M:row(M,n) for M in states}
    for M,dist in rows.items():
        assert sum(dist.values())==1 and dist.get(M,F(0))>=F(1,2)
        for N,p in dist.items():assert rows[N].get(M,F(0))==p
        rows_count+=1
        for ab,cd in itertools.combinations(M,2):
            a,b=ab;c,d=cd;perm={b:c,c:b};other=image(M,perm)
            transformed=defaultdict(F)
            for Z,p in dist.items():transformed[image(Z,perm)]+=p
            assert dict(transformed)==dict(rows[other])
            coalesce=F(0)
            for Z,p in dist.items():
                Z2=image(Z,perm);assert len(set(Z)-set(Z2)) in [0,2]
                if Z==Z2:coalesce+=p
            assert coalesce==F(1,12*math.comb(n,4));couplings+=1
RESULTS=dict(exhaustive_n=[4,6,8],transition_rows=rows_count,adjacent_couplings=couplings,arithmetic='Fraction',checks='stochastic, lazy, symmetric, conjugate marginal, exact coalescence probability')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
