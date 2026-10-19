# SPDX-License-Identifier: Apache-2.0
"""Exact finite evidence; infinite claims require the accompanying proof/source."""
import sys
if not __debug__:
    raise SystemExit("Refusing optimized Python: verification requires assertions enabled")
import json
from math import gcd, isqrt, prod, factorial
from itertools import product
from fractions import Fraction
def require(condition, message):
    if not condition:
        raise AssertionError(message)

def mobius(n):
    answer=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;answer=-answer
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:answer=-answer
    return answer
records=[]
for d in range(2,6):
    for t in range(1,9):
        brute=0
        on_hyperplane=0
        for vector in product(range(-t,t+1),repeat=d):
            if gcd(*vector)==1:
                brute+=1
                if vector[0]==0:on_hyperplane+=1
        formula=sum(mobius(k)*((2*(t//k)+1)**d-1) for k in range(1,t+1))
        require(brute==formula,'primitive vector Möbius count differs')
        require(brute%2==0 and on_hyperplane%2==0,'sign quotient not integral')
        records.append({'d':d,'T':t,'projective':brute//2,'open_x0_nonzero':(brute-on_hyperplane)//2})
print(json.dumps({'status':'PASS','cases':len(records),'oracle':'full integer grids and gcd versus Möbius inversion','records':records},sort_keys=True))
