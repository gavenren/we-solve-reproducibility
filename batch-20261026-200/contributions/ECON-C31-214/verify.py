# SPDX-License-Identifier: Apache-2.0
"""Exact finite likelihood enumeration for the observed/hidden shared gate."""
from fractions import Fraction as F
from itertools import product
import json,sys
if not __debug__: raise RuntimeError('Run with assertions enabled')

def experiment(J,q,b,t,active,visible):
    law={}
    for w,a in [(0,0),(1,0),(1,1)]:
        pa=F(1,2)*(1 if w==0 else (q if a else 1-q))
        for y in product([0,1],repeat=J):
            z=pa
            for j,yy in enumerate(y):
                prob=b+(t if a and j==active else 0)
                z*=prob if yy else 1-prob
            key=(w,a,y) if visible else (w,y)
            law[key]=law.get(key,F(0))+z
    assert sum(law.values())==1
    return law

cases=0
for J,q,b,t in product([2,3],[F(1,5),F(2,3),F(1)],[F(1,4),F(1,2)],[F(1,7),F(1,3)]):
  for visible in [False,True]:
    p0=experiment(J,q,b,t,None,visible)
    ps=[experiment(J,q,b,t,j,visible) for j in range(J)]
    for j in range(J):
      for k in range(J):
        inner=sum((ps[j][z]*ps[k][z]/p for z,p in p0.items() if p),F(0))
        extra=(q if visible else q*q)*t*t/(2*b*(1-b))
        assert inner==(1+extra if j==k else 1)
    for m in [1,2,3,7]:
      chi=(sum((sum((ps[j][z]*ps[k][z]/p for z,p in p0.items() if p),F(0)))**m for j in range(J) for k in range(J))/J**2)-1
      assert chi==((1+extra)**m-1)/J
      cases+=1
print(json.dumps({'status':'PASS','exact_chi_square_cases':cases,'arithmetic':'fractions.Fraction','limits':'finite likelihood identities only; no infinite-theorem certification'}))
