# SPDX-License-Identifier: Apache-2.0
"""Exact forest Schur factors checked by all principal minors and independent rank."""
import sys
if not __debug__:
    raise SystemExit('Refusing -O: assertions are required')
from fractions import Fraction as Q
from itertools import combinations,product
from random import Random

def det(a):
    a=[list(r) for r in a];n=len(a);ans=Q(1)
    for i in range(n):
        j=next((j for j in range(i,n) if a[j][i]),None)
        if j is None:return Q(0)
        if j!=i:a[i],a[j]=a[j],a[i];ans=-ans
        p=a[i][i];ans*=p
        for j in range(i+1,n):
            c=a[j][i]/p
            for k in range(i+1,n):a[j][k]-=c*a[i][k]
    return ans

def rank(a):
    a=[list(r) for r in a];r=0;n=len(a)
    for c in range(n):
        p=next((i for i in range(r,n) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];z=a[r][c]
        a[r]=[x/z for x in a[r]]
        for i in range(n):
            if i!=r:
                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def psd_minors(a):
    n=len(a)
    return all(det([[a[i][j] for j in s] for i in s])>=0 for k in range(1,n+1) for s in combinations(range(n),k))

def forest_factor(a):
    n=len(a);a=[list(r) for r in a];live=set(range(n));out=[]
    while live:
        i=next(i for i in sorted(live) if sum(a[i][j]>0 for j in live if i!=j)<=1)
        nbr=[j for j in live if j!=i and a[i][j]>0];d=a[i][i]
        if d<0 or (nbr and d==0):return None
        if d:
            c=[Q(0)]*n;c[i]=Q(1)
            if nbr:
                j=nbr[0];c[j]=a[i][j]/d;a[j][j]-=a[i][j]**2/d
            out.append((d,c))
        live.remove(i)
    return out

rng=Random(2964);cases=[]
# Exhaustive paths on up to four vertices, diagonals 0..2, edge values 0..1.
for n in range(1,5):
    for diag in product(range(3),repeat=n):
        for edges in product(range(2),repeat=max(0,n-1)):
            a=[[Q(0) for j in range(n)] for i in range(n)]
            for i in range(n):a[i][i]=Q(diag[i])
            for i,v in enumerate(edges):a[i][i+1]=a[i+1][i]=Q(v)
            cases.append(a)
for n in range(2,7):
    for _ in range(50):
        a=[[Q(0) for j in range(n)] for i in range(n)]
        for i in range(n):a[i][i]=Q(rng.randrange(8),rng.randrange(1,5))
        for i in range(1,n):
            j=rng.randrange(i);a[i][j]=a[j][i]=Q(rng.randrange(4),rng.randrange(1,5))
        cases.append(a)
accepted=0
for a in cases:
    out=forest_factor(a);expected=psd_minors(a)
    assert (out is not None)==expected
    if out is None:continue
    accepted+=1;n=len(a)
    assert len(out)==rank(a)
    assert all(d>0 and all(x>=0 for x in c) for d,c in out)
    rebuilt=[[sum((d*c[i]*c[j] for d,c in out),Q(0)) for j in range(n)] for i in range(n)]
    assert rebuilt==a
# A large binary rational case: source size rather than numerical values is relevant.
a=[[Q(2**120+1),Q(1,2**101)],[Q(1,2**101),Q(2**130+7)]]
out=forest_factor(a);assert out is not None and len(out)==2
assert [[sum(d*c[i]*c[j] for d,c in out) for j in range(2)] for i in range(2)]==a
print('PASS:',len(cases),'forest matrices versus all-principal-minor PSD test;',accepted,'optimal-rank exact factors; large binary-rational case')
