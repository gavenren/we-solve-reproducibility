# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def solve(A,t):
    g=math.gcd(*A)
    if t%g:return False
    A=[a//g for a in A];T=t//g;R=[False]*(T+1);R[0]=True
    for a in A:
        for j in range(T,a-1,-1):R[j]|=R[j-a]
    return R[T]
def oracle(A):return {sum(a for j,a in enumerate(A) if mask>>j&1) for mask in range(1<<len(A))}
cases=0
for n in range(1,6):
    for A in itertools.product(range(1,5),repeat=n):
        sums=oracle(A)
        for t in range(sum(A)+2):assert solve(A,t)==(t in sums);cases+=1
for _ in range(300):
    A=[rng.randrange(1,50)*6 for _ in range(rng.randrange(2,12))];t=rng.randrange(sum(A)+2)
    assert solve(A,t)==(t in oracle(A));cases+=1
RESULTS=dict(cases=cases,exhaustive_items=[1,5],exhaustive_item_values=[1,4],random_gcd_six_cases=300,oracle='all subset masks',note='small exhaustive checks certify correctness examples, not exponential space bound')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
