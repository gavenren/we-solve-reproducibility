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

records=[]
for p in (3,5,7,11,13):
    require(all(p%d for d in range(2,isqrt(p)+1)),'parameter not prime')
    initial=Fraction(2,2*factorial(p-1)-1)
    value=initial;terms=[];numerators=[]
    while value:
        require(len(terms)<p+1,'unexpected nontermination in finite family instance')
        numerators.append(value.numerator)
        a,b=value.numerator,value.denominator
        d=(b+a-1)//a
        if d%2==0:d+=1
        require(Fraction(1,d)<=value,'chosen reciprocal too large')
        if d>1:require(Fraction(1,d-2)>value,'chosen odd reciprocal is not greedy')
        terms.append(d);value-=Fraction(1,d)
    require(numerators==list(range(2,p))+[1],'reduced numerator theorem differs')
    require(len(terms)==p-1 and all(d%2 for d in terms),'term count or parity failed')
    require(sum((Fraction(1,d) for d in terms),Fraction())==initial,'exact reconstruction failed')
    records.append({'p':p,'initial_denominator':initial.denominator,'steps':len(terms),'numerators':numerators,'largest_denominator_bits':max(d.bit_length() for d in terms)})
print(json.dumps({'status':'PASS','records':records,'oracle':'exact reconstruction and independent predecessor check for each greedy choice','limitation':'five finite instances do not prove the infinite source theorem'},sort_keys=True))
