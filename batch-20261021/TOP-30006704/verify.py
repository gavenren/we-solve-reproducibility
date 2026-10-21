# SPDX-License-Identifier: Apache-2.0
"""Independent all-assignment SAT counts versus retained OV-list multiplicities."""
import itertools,random,json
if not __debug__:raise RuntimeError('Refusing -O: assertions required.')
def counts(n,F):
 truth=sum(all(any(bool(mask>>(abs(x)-1)&1)==(x>0) for x in C) for C in F) for mask in range(1<<n))
 left=n//2;A=[];B=[]
 for start,width,out in [(0,left,A),(left,n-left,B)]:
  for a in range(1<<width):
   out.append(tuple(int(not any(bool(a>>(abs(x)-1-start)&1)==(x>0) for x in C if start<=abs(x)-1<start+width)) for C in F))
 orth=sum(not any(x and y for x,y in zip(a,b)) for a in A for b in B)
 assert truth==orth
 return truth
cases=0
for n in range(3):
 lit=[z for i in range(1,n+1) for z in (i,-i)]
 clauses=[()]+[(x,) for x in lit]+[c for c in itertools.combinations(lit,2) if c[0]!=-c[1]]
 for mask in range(1<<len(clauses)):
  counts(n,[c for j,c in enumerate(clauses) if mask>>j&1]);cases+=1
rng=random.Random(20261021)
for _ in range(2000):
 n=rng.randrange(1,9);F=[tuple(rng.choice([-1,1])*rng.randrange(1,n+1) for _ in range(rng.randrange(0,5))) for _ in range(rng.randrange(0,20))]
 counts(n,F);cases+=1
print(json.dumps({'status':'PASS','formula_count':cases,'exhaustive_variables':2,'seeded_max_variables':8,'exact_sat_count_equals_orthogonal_pair_count':True,'odd_splits_empty_clauses_tautologies_duplicates':True,'finite_only':True},indent=2))
