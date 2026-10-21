# SPDX-License-Identifier: Apache-2.0
"""Rank discovery and exact comparisons against independent small-class oracles."""
import sys
if not __debug__:
    raise SystemExit('Refusing -O: assertions are required')
from math import isqrt
from itertools import product
from random import Random

def rank_discover(xs):
 u=[]
 for a in xs:
  if a==0:continue
  found=False
  for mask in range(1<<len(u)):
   P=1
   for i,b in enumerate(u):
    if (mask>>i)&1:P*=b
   z=isqrt(a*P)
   if z*z==a*P:found=True;break
  if not found:u.append(a)
 return len(u)

def decide(xs,k):
 n=len(xs);r=rank_discover(xs);B=max(1,k+sum(xs));q=B.bit_length()*((1<<r)-1)
 p=q+(n+1-1).bit_length()+2
 A=sum(isqrt(a<<(2*p)) for a in xs);K=k<<p
 return not (A>K)
 # If K lies below the interval lower endpoint, answer no; every other
 # branch is yes, by the proved nonzero separation and chosen width.

def factor_rank(xs):
 # Independent oracle only for tiny verifier inputs, not the algorithm.
 vectors=[];primes=set()
 for a in xs:
  if not a:continue
  ps=set();d=2
  while d*d<=a:
   parity=0
   while a%d==0:a//=d;parity^=1
   if parity:ps.add(d)
   d+=1
  if a>1:ps.symmetric_difference_update({a})
  vectors.append(ps);primes.update(ps)
 basis={}
 for v in vectors:
  while v:
   p=max(v)
   if p in basis:v=v^basis[p]
   else:basis[p]=v;break
 return len(basis)

checks=0
for a,b,k in product(range(21),repeat=3):
 d=k*k-a-b;expected=d>=0 and d*d>=4*a*b
 assert decide([a,b],k)==expected
 checks+=1
rng=Random(3399);rankchecks=0
for _ in range(700):
 xs=[rng.randrange(201) for j in range(rng.randrange(9))]
 assert rank_discover(xs)==factor_rank(xs);rankchecks+=1
# Lists of unbounded count within one square class: S=A+B sqrt(2).
for _ in range(700):
 xs=[];A=B=0
 for i in range(rng.randrange(31)):
  b=rng.randrange(20)
  if rng.randrange(2):xs.append(2*b*b);B+=b
  else:xs.append(b*b);A+=b
 k=rng.randrange(700);d=k-A
 expected=d>=0 and d*d>=2*B*B
 assert decide(xs,k)==expected
 assert rank_discover(xs)<=1
 checks+=1
# Long binary values and exact equality in rank zero.
b=2**300+37
assert decide([b*b,(b+1)**2],2*b+1)
assert not decide([b*b,(b+1)**2],2*b)
assert decide([],0)
print('PASS:',checks,'exact comparisons against two-surd/one-class oracles;',rankchecks,'ranks against prime-parity elimination; large binary equality and empty-list boundaries')
