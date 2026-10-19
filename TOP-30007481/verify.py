# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def expected(seq,k):
    states={(tuple(range(k)),frozenset()):F(1)};cost=F(0)
    for request in seq:
        nxt=defaultdict(F)
        for (cache,marks),p in states.items():
            if request not in marks and len(marks)==k:marks=frozenset()
            marked=marks|{request}
            if request in cache:nxt[(cache,marked)]+=p;continue
            cost+=p;victims=[v for v in cache if v not in marks]
            assert victims
            for v in victims:nxt[(tuple(sorted((set(cache)-{v})|{request})),marked)]+=p/len(victims)
        states=nxt;assert sum(states.values())==1
    return cost

def offline(seq,k):
    states={tuple(range(k)):0}
    for request in seq:
        nxt={}
        for cache,c in states.items():
            choices=[(cache,c)] if request in cache else [(tuple(sorted((set(cache)-{v})|{request})),c+1) for v in cache]
            for new,val in choices:nxt[new]=min(nxt.get(new,val),val)
        states=nxt
    return min(states.values())
cases=0;ratios={}
for k,length in [(2,6),(3,5)]:
    H=sum((F(1,j) for j in range(1,k+1)),F(0));maxratio=F(0)
    for size in range(length+1):
        for seq in itertools.product(range(k+2),repeat=size):
            alg=expected(seq,k);opt=offline(seq,k);assert alg<=2*H*opt
            if opt:maxratio=max(maxratio,alg/opt)
            else:assert alg==0
            cases+=1
    ratios[k]=str(maxratio)
RESULTS=dict(cases=cases,k2_all_sequences_alphabet4_length_at_most=6,k3_all_sequences_alphabet5_length_at_most=5,max_observed_ratio=ratios,oracle='exact optimal offline cache DP',arithmetic='complete rational distribution over every random eviction')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
