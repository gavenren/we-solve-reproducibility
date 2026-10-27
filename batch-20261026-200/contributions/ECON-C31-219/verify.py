# SPDX-License-Identifier: Apache-2.0
"""Check resolvent and target identities against independent exact elimination."""
from fractions import Fraction as F
from itertools import product
import json
if not __debug__: raise RuntimeError('Run with assertions enabled')
def inv(a):
 n=len(a);x=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 for j in range(n):
  z=next(i for i in range(j,n) if x[i][j]);x[j],x[z]=x[z],x[j]
  d=x[j][j];x[j]=[v/d for v in x[j]]
  for i in range(n):
   if i!=j:
    d=x[i][j];x[i]=[v-d*w for v,w in zip(x[i],x[j])]
 return [r[n:] for r in x]
def mul(a,b):return [[sum((x*y for x,y in zip(r,c)),F(0)) for c in zip(*b)] for r in a]
cases=0
for k,delta,beta,gamma in product(range(2,8),[F(-3,4),F(0),F(2,3)],[F(-2,3),F(1,4)],[F(-1,3),F(3,4)]):
 B=[[F(i!=j,k-1) for j in range(k)] for i in range(k)]
 M=inv([[F(i==j)-delta*B[i][j] for j in range(k)] for i in range(k)])
 T=mul(M,[[beta*F(i==j)+gamma*B[i][j] for j in range(k)] for i in range(k)])
 kap=(beta+gamma)/(1-delta);lam=(beta-gamma/(k-1))/(1+delta/(k-1))
 u=lam+(kap-lam)/k;v=(kap-lam)/k
 assert all(T[i][j]==(u if i==j else v) for i in range(k) for j in range(k))
 assert all(sum(r)==kap for r in T)
 assert sum(x*x for x in M[0])==F(1,k)/(1-delta)**2+(1-F(1,k))/(1+delta/(k-1))**2
 cases+=1
print(json.dumps({'status':'PASS','exact_resolvent_cases':cases,'arithmetic':'fractions.Fraction','limits':'finite matrix identities only; inference theorem uses written Gaussian proof'}))
