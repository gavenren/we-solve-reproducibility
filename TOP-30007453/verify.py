# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def band(x,y,k):
    if abs(len(x)-len(y))>k:return k+1
    prev={j:j for j in range(min(k,len(y))+1)}
    for i,a in enumerate(x,1):
        cur={}
        for j in range(max(0,i-k),min(len(y),i+k)+1):
            cur[j]=i if j==0 else min(k+1,prev.get(j,k+1)+1,cur.get(j-1,k+1)+1,prev.get(j-1,k+1)+(a!=y[j-1]))
        prev=cur
    return prev.get(len(y),k+1)
def oracle(x,y):
    D=[[0]*(len(y)+1) for _ in range(len(x)+1)]
    for i in range(len(x)+1):D[i][0]=i
    for j in range(len(y)+1):D[0][j]=j
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(x[i-1]!=y[j-1]))
    return D[-1][-1]
words=[x for n in range(6) for x in itertools.product(range(2),repeat=n)];cases=0
for x in words:
    for y in words:
        d=oracle(x,y)
        for k in range(7):assert band(x,y,k)==min(d,k+1);cases+=1
for _ in range(400):
    x=[rng.randrange(5) for _ in range(rng.randrange(50))];y=[rng.randrange(5) for _ in range(rng.randrange(50))];d=oracle(x,y)
    for k in [0,1,3,10,50]:assert band(x,y,k)==min(d,k+1);cases+=1
RESULTS=dict(cases=cases,exhaustive_binary_lengths=[0,5],random_pairs=400,oracle='full two-dimensional edit DP')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
