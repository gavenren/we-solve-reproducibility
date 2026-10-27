import json
from fractions import Fraction as F
from random import Random
from pathlib import Path

def equilibrium(a, lam):
    a=sorted(a,reverse=True)
    for m in range(1,len(a)+1):
        s=sum(a[:m]); d=m+1+(m-1)*lam; t=(1+lam)*s/d
        if a[m-1] >= t and (m==len(a) or a[m]<=t):
            q=[(x-t)/(1-lam) if i<m else 0*x for i,x in enumerate(a)]
            return q,m
    raise RuntimeError('No active set')

def welfare(a,lam):
    a=sorted(a,reverse=True);q,m=equilibrium(a,lam)
    return sum(x*y for x,y in zip(a,q))-sum(q)**2/2

a=[F(10),F(6)]
q0,m0=equilibrium(a,F(0));q1,m1=equilibrium(a,F(1,5))
if q0 != [F(14,3),F(2,3)] or q1 != [F(5),F(0)]: raise RuntimeError('Example quantities')
if welfare(a,F(0)) != F(328,9) or welfare(a,F(1,5)) != F(75,2): raise RuntimeError('Example welfare')
rng=Random(553); checked=0; derivative_checks=0
for n in range(1,13):
  for k in range(60):
    a=sorted([F(rng.randrange(1,101),10) for _ in range(n)],reverse=True)
    lam=F(rng.randrange(0,950),1000);q,m=equilibrium(a,lam);Q=sum(q)
    for x,qi in zip(a,q):
      if qi<0: raise RuntimeError('Negative quantity')
      g=x-(1+lam)*Q-(1-lam)*qi
      if (qi>0 and g!=0) or (qi==0 and g>0): raise RuntimeError('KKT')
    s=sum(a[:m]);d=m+1+(m-1)*lam;v=sum((x-s/m)**2 for x in a[:m])
    w=s*s/(m*d)-s*s/(2*d*d)+v/(1-lam)
    if w!=welfare(a,lam): raise RuntimeError('Formula mismatch')
    h=F(1,1000000)
    if lam>h and equilibrium(a,lam-h)[1]==m==equilibrium(a,lam+h)[1]:
      derivative=v/(1-lam)**2-s*s*(m-1)*(1+(m-1)*lam)/(m*d**3)
      fd=(welfare(a,lam+h)-welfare(a,lam-h))/(2*h)
      if abs(float(fd-derivative))>1e-5*(1+abs(float(derivative))): raise RuntimeError('Derivative mismatch')
      derivative_checks+=1
    checked+=1
out={'status':'PASS','exact_kkt_and_welfare_instances':checked,'derivative_checks':derivative_checks,'example_welfare_change':'19/18','seed':553,'scope':'Implementation and arithmetic checks; general claims proved in report.'}
Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
