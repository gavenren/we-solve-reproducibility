# SPDX-License-Identifier: Apache-2.0
"""Independent exact determinant and permanent checks for the subset matrix."""
import itertools,random,json
if not __debug__:raise RuntimeError('Refusing -O: assertions required.')
def matrix(X,symbolic=False):
 n=len(X); masks=[0]+list(range(1,(1<<n)-1)); idx={s:i for i,s in enumerate(masks)};N=len(masks);A=[[None if symbolic else 0 for _ in masks] for _ in masks]
 for s in range((1<<n)-1):
  for j in range(n):
   if s>>j&1:continue
   t=s|(1<<j);i=idx[s];k=0 if t==(1<<n)-1 else idx[t]
   sign=(-1)**(n-1) if s==0 else 1
   A[i][k]=(sign,(s.bit_count(),j)) if symbolic else sign*X[s.bit_count()][j]
 for i in range(1,N):A[i][i]=(1,None) if symbolic else 1
 return A

def det(A):
 A=[r[:] for r in A];n=len(A);previous=1;sign=1
 for k in range(n-1):
  z=next((i for i in range(k,n) if A[i][k]),None)
  if z is None:return 0
  if z!=k:A[z],A[k]=A[k],A[z];sign=-sign
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*pivot-A[i][k]*A[k][j]
    assert num%previous==0;A[i][j]=num//previous
   A[i][k]=0
  previous=pivot
 return sign*A[-1][-1]
def permanent(X):
 return sum(__import__('math').prod(X[i][p[i]] for i in range(len(X))) for p in itertools.permutations(range(len(X))))

symbolic=0
for n in range(1,4):
 A=matrix([[0]*n for _ in range(n)],True);terms={}
 for p in itertools.permutations(range(len(A))):
  if any(A[i][p[i]] is None for i in range(len(A))):continue
  sign=(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)));mon=[]
  for i in range(len(A)):
   s,x=A[i][p[i]];sign*=s
   if x is not None:mon.append(x)
  mon=tuple(sorted(mon));terms[mon]=terms.get(mon,0)+sign
 terms={m:c for m,c in terms.items() if c}
 expected={tuple((i,p[i]) for i in range(n)):1 for p in itertools.permutations(range(n))}
 assert terms==expected;symbolic+=1
cases=0
for n in range(1,4):
 for bits in range(1<<(n*n)):
  X=[[(bits>>(i*n+j))&1 for j in range(n)] for i in range(n)]
  assert det(matrix(X))==permanent(X);cases+=1
rng=random.Random(20261021)
for n,rep in [(2,25),(3,25),(4,25),(5,10),(6,3)]:
 for _ in range(rep):
  X=[[rng.randrange(-5,6) for _ in range(n)] for _ in range(n)]
  assert det(matrix(X))==permanent(X);cases+=1
print(json.dumps({'status':'PASS','formal_symbolic_coefficient_identities':symbolic,'numeric_exact_identities':cases,'max_permanent_order':6,'max_determinant_order':63,'finite_only':True},indent=2))
