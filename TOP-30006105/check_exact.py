# SPDX-License-Identifier: Apache-2.0
"""Exact finite diagnostic; infinite claims depend on the companion proof."""
import sys
if not __debug__:
    raise SystemExit("Refusing optimized Python: assertions must remain enabled")

from fractions import Fraction as F
def solve(A,b):
    n=len(A);M=[[F(x) for x in r]+[F(z)] for r,z in zip(A,b)]
    for c in range(n):
        piv=next((r for r in range(c,n) if M[r][c]),None)
        if piv is None:return None
        M[c],M[piv]=M[piv],M[c]
        q=M[c][c];M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r!=c:
                q=M[r][c]
                M[r]=[x-q*y for x,y in zip(M[r],M[c])]
    return [r[-1] for r in M]
def rank(A):
    if not A:return 0
    M=[[F(x) for x in r] for r in A];r=0
    for c in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][c]),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
        for i in range(r+1,len(M)):
            q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r

from itertools import combinations,product
from random import Random
rng=Random(6105)
def facets(G,H):
    d=len(H[0]);m=len(H)
    for ids in combinations(range(m),d-1):
        A=[H[i] for i in ids]
        if rank(A)<d-1:continue
        if d==1:u=[F(1)]
        else:
            free=next(j for j in range(d) if rank([[r[k] for k in range(d) if k!=j] for r in A])==d-1)
            sol=solve([[r[k] for k in range(d) if k!=free] for r in A],[-r[free] for r in A])
            u=[];it=iter(sol)
            for j in range(d):u.append(F(1) if j==free else next(it))
        dot=lambda v:sum(a*b for a,b in zip(u,v))
        if sum(abs(dot(v)) for v in G)>sum(abs(dot(v)) for v in H):return False
    return True
def member(x,H):
    # Independent bounded-coefficient feasibility oracle: enumerate vertices
    # of {t:H t=x, -1<=t<=1}, using d free columns and all other bounds.
    d=len(x);m=len(H)
    for ids in combinations(range(m),d):
        rest=[j for j in range(m) if j not in ids]
        A=[[H[j][i] for j in ids] for i in range(d)]
        for ss in product([-1,1],repeat=len(rest)):
            b=[x[i]-sum(s*H[j][i] for s,j in zip(ss,rest)) for i in range(d)]
            sol=solve(A,b)
            if sol is not None and all(-1<=v<=1 for v in sol):return True
    return False
cases=0
for d in range(1,5):
    for c in range(3):
        for _ in range(10):
            H=[[int(i==j) for i in range(d)] for j in range(d)]+[[rng.randrange(-2,3) for i in range(d)] for j in range(c)]
            G=[[F(rng.randrange(-4,5),rng.choice([1,2,3])) for i in range(d)] for j in range(rng.randrange(1,5))]
            oracle=all(member([sum(s*v[i] for s,v in zip(ss,G)) for i in range(d)],H) for ss in product([-1,1],repeat=len(G)))
            assert facets(G,H)==oracle
            cases+=1
print('PASS',cases,'rational containment cases d1..4, outer co-rank0..2; independent cube-feasibility oracle')
