# SPDX-License-Identifier: Apache-2.0
"""Exact finite-space numerator bias and double-robustness checks."""
from fractions import Fraction as F
from itertools import product
import json
if not __debug__: raise RuntimeError('Run with assertions enabled')
cases=0
for a,b,c,d in product([F(1,4),F(1,2),F(3,4)],repeat=4):
 f0=[a,1-a];f1=[b,1-b];m=[c,d];mh=[d,c];r=[f0[i]/f1[i] for i in range(2)]
 for rh in [r,[F(1),F(1)],[F(1,2),F(3,2)]]:
  for fitted in [m,mh]:
   for wt in [[F(1),F(1)],[F(1,3),F(4)],[F(2),F(3,4)]]:
    target=sum(f0[i]*m[i]*wt[i] for i in range(2))
    expected=sum(f0[i]*fitted[i]*wt[i]+f1[i]*rh[i]*wt[i]*(m[i]-fitted[i]) for i in range(2))
    bias=sum(f1[i]*(rh[i]-r[i])*(m[i]-fitted[i])*wt[i] for i in range(2))
    assert expected-target==bias
    if rh==r or fitted==m:assert expected==target
    cases+=1
print(json.dumps({'status':'PASS','exact_bias_cases':cases,'arithmetic':'fractions.Fraction','limits':'arbitrary positive discrete weights test the algebra; uniform continuous tilt bound uses written proof'}))
