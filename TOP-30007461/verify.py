# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def multiply(a,b):
    n=len(a);out=[0]*(2*n)
    for j,bit in enumerate(b):
        if not bit:continue
        carry=0
        for i in range(2*n):
            term=a[i-j] if j<=i<j+n else 0
            value=out[i]+term+carry;out[i]=value&1;carry=value>>1
        assert carry==0
    return out
def bits(a,n):return [(a>>j)&1 for j in range(n)]
def integer(v):return sum(b<<i for i,b in enumerate(v))
cases=0
for n in range(1,8):
    for a in range(1<<n):
        for b in range(1<<n):assert integer(multiply(bits(a,n),bits(b,n)))==a*b;cases+=1
for n in [128,511,2048]:
    for _ in range(50):
        a=rng.getrandbits(n);b=sum(1<<j for j in rng.sample(range(n),min(n,4)))
        assert integer(multiply(bits(a,n),bits(b,n)))==a*b;cases+=1
    a=(1<<n)-1
    for b in [0,1,(1<<(n-1))+1,(1<<n)-1]:assert integer(multiply(bits(a,n),bits(b,n)))==a*b;cases+=1
RESULTS=dict(cases=cases,exhaustive_operand_bits=[1,7],large_operand_bits=[128,511,2048],oracle='Python integer multiplication',algorithm='explicit low-to-high Boolean carry array; tape time proved in report')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
