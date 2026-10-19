# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def parity_certificate(n,E):
    rows=[sum(1<<v for v in e) for e in E]+[((1<<n)-1)|(1<<n)];piv=[];r=0
    for col in range(n):
        q=next((i for i in range(r,len(rows)) if rows[i]>>col&1),None)
        if q is None:continue
        rows[r],rows[q]=rows[q],rows[r]
        for i in range(len(rows)):
            if i!=r and rows[i]>>col&1:rows[i]^=rows[r]
        piv.append(col);r+=1
    if any((row&((1<<n)-1))==0 and row>>n&1 for row in rows):return None
    x=sum(((rows[i]>>n)&1)<<col for i,col in enumerate(piv))
    assert x.bit_count()%2 and all(sum(x>>v&1 for v in e)%2==0 for e in E)
    return x

def perfect(n,E):
    masks=[sum(1<<v for v in e) for e in E];by=[[] for _ in range(n)]
    for e in masks:
        for v in range(n):
            if e>>v&1:by[v].append(e)
    memo={0:True}
    def go(S):
        if S in memo:return memo[S]
        v=(S&-S).bit_length()-1;ans=any(e&S==e and go(S^e) for e in by[v]);memo[S]=ans;return ans
    return go((1<<n)-1)
cases=0;certs=0;dense=0
for n,trials in [(3,2),(6,900),(9,500),(12,50)]:
    es=list(itertools.combinations(range(n),3))
    for trial in range(trials):
        p=rng.choice([F(1,3),F(2,3),F(9,10)])
        E=[e for e in es if (bool(trial) if n==3 else rng.randrange(p.denominator)<p.numerator)]
        cert=parity_certificate(n,E);ans=perfect(n,E)
        if cert is not None:assert not ans;certs+=1
        codeg=min(sum(set(S)<=set(e) for e in E) for S in itertools.combinations(range(n),2))
        if 3*codeg>n:
            # A finite regression check, not an assertion of the asymptotic cutoff.
            assert (cert is None)==ans;dense+=1
        cases+=1
# Explicit nontrivial dense NO certificate in the promised strict interval.
n=18;A=set(range(9));E=[e for e in itertools.combinations(range(n),3) if len(A&set(e))%2==0]
codeg=min(sum(set(S)<=set(e) for e in E) for S in itertools.combinations(range(n),2));assert codeg==7 and 3*codeg>n
assert parity_certificate(n,E) is not None
RESULTS=dict(cases=cases,certificates_checked=certs,strictly_above_one_third_small_cases=dense,dense_NO_example=dict(n=18,codegree=7),oracle='exact recursive perfect matching search for n<=12, direct validation of every GF2 NO certificate',limits='finite dense agreement does not determine KKM sufficient-n cutoff')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
