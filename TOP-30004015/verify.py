# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def sparse(x,y):
    where=defaultdict(list)
    for j,a in enumerate(y):where[a].append(j)
    tails=[];ids=[];pairs=[];pred=[]
    for i,a in enumerate(x):
        for j in reversed(where[a]):
            r=bisect_left(tails,j);p=ids[r-1] if r else -1;idx=len(pairs);pairs.append((i,j));pred.append(p)
            if r==len(tails):tails.append(j);ids.append(idx)
            else:tails[r]=j;ids[r]=idx
    chain=[];i=ids[-1] if ids else -1
    while i>=0:chain.append(pairs[i]);i=pred[i]
    chain.reverse()
    assert all(x[i]==y[j] for i,j in chain)
    assert all(a<c and b<d for (a,b),(c,d) in zip(chain,chain[1:]))
    return len(chain)
def dp(x,y):
    row=[0]*(len(y)+1)
    for a in x:
        prev=row;row=[0]
        for j,b in enumerate(y):row.append(prev[j]+1 if a==b else max(prev[j+1],row[-1]))
    return row[-1]
words=[x for n in range(7) for x in itertools.product(range(2),repeat=n)];cases=0
for x in words:
    for y in words:assert sparse(x,y)==dp(x,y);cases+=1
for _ in range(500):
    x=[rng.randrange(30) for _ in range(rng.randrange(80))];y=[rng.randrange(30) for _ in range(rng.randrange(80))];assert sparse(x,y)==dp(x,y);cases+=1
RESULTS=dict(cases=cases,exhaustive_binary_lengths=[0,6],random_pairs=500,oracle='quadratic full LCS dynamic program',checks='strict pair indices and equality witness')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
