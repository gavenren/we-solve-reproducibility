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

LIMIT=100000
sieve=bytearray(b'\1')*(LIMIT+1)
sieve[:2]=b'\0\0'
for p in range(2,isqrt(LIMIT)+1):
    if sieve[p]:sieve[p*p::p]=b'\0'*((LIMIT-p*p)//p+1)
def trial_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
require(all(bool(sieve[n])==trial_prime(n) for n in range(LIMIT+1)),
        'independent full trial primality disagrees with sieve')
primes=[p for p in range(2,LIMIT+1) if sieve[p]]
wieferich=[p for p in primes if p>2 and pow(2,p-1,p*p)==1]
require(wieferich==[1093,3511],'unexpected bounded Wieferich list')
orders={}
for p in wieferich:
    require(pow(2,p-1,p**3)!=1,'valuation exceeds two')
    t=1;residue=2%p
    while residue!=1:residue=residue*2%p;t+=1
    require(pow(2,t,p)==1 and all(pow(2,k,p)!=1 for k in range(1,t)),
            'order minimality certificate failed')
    orders[p]=t
n=prod(wieferich)
require(n==3837523 and pow(2,n-1,n*n)!=1,'only supported composite passes')
# A second bounded oracle checks the full local iff on every odd n<=2001.
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
for m in range(3,2002,2):
    local=True
    for p,e in factors(m).items():
        t=next(k for k in range(1,p) if pow(2,k,p)==1)
        if (m-1)%t or pow(2,p-1,p**(2*e))!=1:local=False
    require(local==(pow(2,m-1,m*m)==1),'local iff failed against direct modulus')
print(json.dumps({'status':'PASS','prime_bound':LIMIT,'prime_count':len(primes),'wieferich':wieferich,'valuations':{str(p):2 for p in wieferich},'orders':orders,'only_supported_composite':n,'composite_residue_mod_square':pow(2,n-1,n*n),'order_remainders':{str(p):(n-1)%orders[p] for p in wieferich},'local_iff_odd_n_through':2001},sort_keys=True))
