# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def tree_vectors(t):
    for j in range(t):
        for choices in itertools.product([0,1],repeat=t-1):
            x=[0]*(2*t);x[2*j]=x[2*j+1]=1
            for i,c in zip([i for i in range(t) if i!=j],choices):x[2*i+c]=1
            yield tuple(x)
def greedy(w,k,t):
    z=[w[2*i]+w[2*i+1]-k for i in range(t)];j=next(i for i in range(t) if z[i]>0);x=[0]*(2*t);x[2*j]=x[2*j+1]=1
    for i in range(t):
        if i==j:continue
        a,b=w[2*i:2*i+2];c=0 if a==k else 1 if b==k else 0 if a>0 else 1;x[2*i+c]=1
    lam=min([k,z[j]]+[w[e] if x[e] else k-w[e] for e in range(2*t)])
    return tuple(x),lam
def independent_max(w,k,x,t):
    # All spanning-tree subset-rank inequalities, rather than pair constraints.
    edges=[(a,i+2) for i in range(t) for a in [0,1]];bounds=[F(k)]+[F(w[e]) for e in range(2*t) if x[e]]
    for mask in range(1,1<<(t+2)):
        size=mask.bit_count()
        if size==t+2:continue
        ids=[j for j,(a,b) in enumerate(edges) if mask>>a&1 and mask>>b&1]
        den=size-1-sum(x[j] for j in ids);num=k*(size-1)-sum(w[j] for j in ids)
        assert num>=0
        if den:bounds.append(F(num,den))
    return min(bounds)
cases=0;steps=0
for t in [2,3,4]:
    ts=list(tree_vectors(t))
    inputs=[]
    if t<=3:
        for k in range(1,4):
            for w in itertools.product(range(k+1),repeat=2*t):
                if sum(w)==k*(t+1) and all(w[2*i]+w[2*i+1]>=k for i in range(t)):inputs.append((list(w),k))
    for _ in range(500):
        k=rng.randrange(1,12);chosen=[rng.choice(ts) for _ in range(k)];inputs.append(([sum(v[j] for v in chosen) for j in range(2*t)],k))
    for w,k in inputs:
        original=w[:];oldk=k;history=[]
        while k:
            x,lam=greedy(w,k,t);assert x in ts and lam>=1 and int(lam)==lam
            assert F(lam)==independent_max(w,k,x,t)
            history.append((x,lam));w=[a-lam*b for a,b in zip(w,x)];k-=lam;steps+=1
        assert w==[0]*(2*t) and sum(l for _,l in history)==oldk
        assert all(sum(x[j]*l for x,l in history)==original[j] for j in range(2*t))
        assert len(history)<=5*t+1;cases+=1
RESULTS=dict(cases=cases,subtractions=steps,t_values=[2,3,4],oracle='all graph vertex-subset rank inequalities give an independent exact rational maximum lambda',arithmetic='integer and Fraction')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
