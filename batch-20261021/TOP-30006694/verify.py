# SPDX-License-Identifier: Apache-2.0
"""Exact finite Markov-chain probabilities; no Monte Carlo asymptotic inference."""
from fractions import Fraction
import itertools,random,json
if not __debug__:raise RuntimeError('Refusing -O: assertions required.')
def checked(n,F):
 def sat(x):return all(any(bool(x>>(abs(z)-1)&1)==(z>0) for z in C) for C in F)
 solutions=[x for x in range(1<<n) if sat(x)]
 transitions=[]
 for x in range(1<<n):
  if sat(x):transitions.append(None);continue
  C=next(C for C in F if not any(bool(x>>(abs(z)-1)&1)==(z>0) for z in C))
  if not C:transitions.append(());continue
  padded=list(C)
  while len(padded)<3:padded.append(C[0])
  transitions.append(tuple(x^(1<<(abs(z)-1)) for z in padded))
 p=[Fraction(int(sat(x))) for x in range(1<<n)]
 for _ in range(6*n):
  p=[Fraction(1) if T is None else (sum((p[y] for y in T),Fraction(0))/3 if T else Fraction(0)) for T in transitions]
 if solutions:
  target=solutions[0]
  for x,q in enumerate(p):assert q>=Fraction(1,2**((x^target).bit_count()+1))
  assert sum(p,Fraction(0))/(1<<n)>=Fraction(3,4)**n/2
 else:assert all(q==0 for q in p)
 return bool(solutions)
rng=random.Random(20261021);cases=0;sat_cases=0
for n in range(1,7):
 dataset=[[],[()],[tuple([i]) for i in range(1,n+1)],[(1,),(-1,)]]
 for _ in range(35):
  F=[]
  for j in range(rng.randrange(1,14)):
   width=rng.randrange(1,min(3,n)+1);vs=rng.sample(range(1,n+1),width)
   F.append(tuple(rng.choice([-1,1])*v for v in vs))
  dataset.append(F)
 for F in dataset:sat_cases+=checked(n,F);cases+=1
print(json.dumps({'status':'PASS','exact_formula_chains':cases,'satisfiable_chains':sat_cases,'max_variables':6,'steps_per_trial':'6n','all_initial_state_bounds_checked':True,'finite_only':True},indent=2))
