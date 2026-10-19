# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def packed(a,b,p):
    d=len(a);width=(d*(p-1)**2).bit_length();base=1<<width
    A=sum(v<<(i*width) for i,v in enumerate(a));B=sum(v<<(i*width) for i,v in enumerate(b));P=A*B
    raw=[(P>>(j*width))&(base-1) for j in range(2*d-1)]
    assert P>>(width*(2*d-1))==0
    return [v%p for v in raw],raw,width
primes=[p for p in range(2,201) if all(p%d for d in range(2,math.isqrt(p)+1))];cases=inside=0
for d in range(1,41):
    for p in rng.sample(primes,min(10,len(primes))):
        a=[rng.randrange(p) for _ in range(d)];b=[rng.randrange(p) for _ in range(d)];out,raw,width=packed(a,b,p)
        expected=[sum(a[i]*b[j-i] for i in range(d) if 0<=j-i<d) for j in range(2*d-1)]
        assert raw==expected and out==[v%p for v in expected] and max(raw)<1<<width;cases+=1;inside+=int(d>=2 and d<=p<=d**3)
for d in [2,4,8,16,31]:
    p=2;a=b=[1]*d;out,raw,width=packed(a,b,p);assert out==[min(j+1,2*d-1-j,d)%2 for j in range(2*d-1)];cases+=1
RESULTS=dict(cases=cases,inside_d_le_p_le_d_cubed=inside,degree_bound_d=[1,40],primes=[2,199],oracle='direct quadratic integer polynomial convolution',limits='identity also tested outside claimed fast bit-time band; no HH implementation or timing claim')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
