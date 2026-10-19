# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def inspect(f,n):
    inds=[S for S in range(1<<n) if f[S]==S.bit_count()]
    assert 0 in inds
    for I in inds:
        assert all(J in inds for J in range(1<<n) if J&I==J)
        for J in inds:
            if I.bit_count()<J.bit_count():assert any(I|(1<<e) in inds for e in range(n) if J>>e&1 and not I>>e&1)
    for S in range(1<<n):assert f[S]==max(I.bit_count() for I in inds if I&S==I)
valid=0;functions=0
for n in range(1,4):
    masks=[S for S in range(1<<n) if S.bit_count()>=2]
    for vals in itertools.product(*(range(1,S.bit_count()+1) for S in masks)):
        f=[0 if S==0 else 1 for S in range(1<<n)]
        for S,a in zip(masks,vals):f[S]=a
        functions+=1
        if any((A&B==A and f[A]>f[B]) or f[A]+f[B]<f[A&B]+f[A|B] for A in range(1<<n) for B in range(1<<n)):continue
        inspect(f,n);valid+=1
# Larger partition matroids supply separately generated nontrivial valid functions.
for _ in range(100):
    n=8;parts=[rng.randrange(4) for _ in range(n)];f=[len({parts[e] for e in range(n) if S>>e&1}) for S in range(1<<n)];inspect(f,n)
RESULTS=dict(all_small_functions=functions,valid_small_functions=valid,all_small_n=[1,3],larger_partition_functions=100,oracle='enumerate every independent subset and all matroid axioms/rank values')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
