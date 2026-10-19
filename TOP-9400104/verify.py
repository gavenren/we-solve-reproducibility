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

BOUND=5000
FORMS={'A':(2,1,32),'B':(2,1,8),'C':(8,2,64),'D':(8,2,16)}
def arrays(a,b,c):
    result=[0]*(BOUND+1)
    for x in range(isqrt(BOUND//a)+1):
        for y in range(isqrt((BOUND-a*x*x)//b)+1):
            rem=BOUND-a*x*x-b*y*y
            for z in range(isqrt(rem//c)+1):
                n=a*x*x+b*y*y+c*z*z
                result[n]+=(2 if x else 1)*(2 if y else 1)*(2 if z else 1)
    return result
counts={name:arrays(*abc) for name,abc in FORMS.items()}
def signed_oracle(n,a,b,c):
    return sum(a*x*x+b*y*y+c*z*z==n
        for x in range(-isqrt(n//a),isqrt(n//a)+1)
        for y in range(-isqrt(n//b),isqrt(n//b)+1)
        for z in range(-isqrt(n//c),isqrt(n//c)+1))
for name,abc in FORMS.items():
    for n in range(121):
        require(counts[name][n]==signed_oracle(n,*abc),'signed oracle disagrees')
squarefree=[True]*(BOUND+1);squarefree[0]=False
for k in range(2,isqrt(BOUND)+1):
    for n in range(k*k,BOUND+1,k*k):squarefree[n]=False
require(all(squarefree[n]==all(n%(k*k) for k in range(2,isqrt(n)+1))
            for n in range(1,BOUND+1)),'squarefree oracle differs')
rows=[]
for n in range(1,BOUND+1):
    if squarefree[n]:
        left,right=(2*counts['A'][n],counts['B'][n]) if n%2 else (2*counts['C'][n],counts['D'][n])
        rows.append({'n':n,'left':left,'right':right,'passes_necessary_test':left==right})
require(all(next(r for r in rows if r['n']==n)['passes_necessary_test'] for n in (5,6,7)),
        'known rational triangle squareclasses fail')
from pathlib import Path
Path(__file__).with_name('tunnell_counts.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'status':'PASS','squarefree_through':BOUND,'squarefree_count':len(rows),'unconditionally_excluded':sum(not r['passes_necessary_test'] for r in rows),'passes_necessary_test_only':sum(r['passes_necessary_test'] for r in rows),'signed_oracle_all_n_through':120,'forms':FORMS,'limitation':'passes are not unconditional congruence certificates'},sort_keys=True))
