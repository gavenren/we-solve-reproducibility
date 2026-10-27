# SPDX-License-Identifier: Apache-2.0
"""Exact finite reconstruction check; not a proof of the population theorem."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
if not __debug__:
    raise RuntimeError("Run without -O.")
vals=[F(i,8) for i in range(9)]
cases=signs=0
for a,b,p,m0,m1 in product(vals,vals,vals[1:-1],vals,vals):
    if a+b>=1:
        continue
    kap=1-a-b
    q=a+kap*p
    h=(1-p)*m0+p*m1
    z=a*(1-p)*m0+(1-b)*p*m1
    c=z-q*h
    d=q-a
    e=1-b-q
    assert d>0 and e>0
    assert p==d/(d+e)
    assert m1==h+c/d and m0==h-c/e
    assert m1-m0==c*(1/d+1/e)
    if c:
        assert 0<h<1
        dl,el=(c/(1-h),c/h) if c>0 else (-c/h,-c/(1-h))
        assert d>=dl and e>=el
        assert F(1,8)*e<=F(7,8)*d
        assert F(1,8)*d<=F(7,8)*e
        # Recover the observed complete 2x2 binary law from reconstructed latent model.
        pp=d/(d+e); mm1=h+c/d; mm0=h-c/e
        joint=[a*(1-pp)*mm0+(1-b)*pp*mm1,
               (1-a)*(1-pp)*mm0+b*pp*mm1,
               a*(1-pp)*(1-mm0)+(1-b)*pp*(1-mm1),
               (1-a)*(1-pp)*(1-mm0)+b*pp*(1-mm1)]
        assert joint==[z,h-z,q-z,1-h-q+z]
        assert min(joint)>=0 and sum(joint)==1
        signs+=1
    else:
        assert m1==m0
    cases+=1
result={"status":"PASS","exact_reconstructed_models":cases,
        "nonzero_covariance_models":signs,
        "grid":"a,b,m0,m1 in {0,1/8,...,1}; p in {1/8,...,7/8}; a+b<1",
        "arithmetic":"fractions.Fraction",
        "scope":"Finite algebra/latent reconstruction only; no endpoint optimizer tested."}
Path(__file__).with_name("verification.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))

