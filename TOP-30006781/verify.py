# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def operands(x):
    m=len(x);B=m.bit_length();A=sum(v<<(i*B) for i,v in enumerate(x));C=sum(1<<(j*B) for j in range(m));return A,C,B
cases=0
for m in range(1,13):
    for x in itertools.product([0,1],repeat=m):
        A,C,B=operands(x);product=A*C;mask=(1<<B)-1
        for j in range(2*m-1):
            coeff=sum(x[i] for i in range(m) if 0<=j-i<m);assert coeff<1<<B and ((product>>(j*B))&mask)==coeff
        assert (product>>((m-1)*B))&1==sum(x)%2;cases+=1
for n in range(8,513):
    L=(n+1).bit_length();m=n//(2*L);x=[rng.randrange(2) for _ in range(m)];A,C,B=operands(x)
    assert m*B<=n and A<1<<n and C<1<<n
    assert ((A*C)>>((m-1)*B))&1==sum(x)%2;cases+=1
RESULTS=dict(cases=cases,exhaustive_parity_variables=[1,12],padding_operand_lengths=[8,512],oracle='exact integer multiplication and direct convolution coefficients',limits='no finite test certifies the imported AC0 parity theorem')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
