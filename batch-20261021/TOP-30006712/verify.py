# SPDX-License-Identifier: Apache-2.0
"""Three-block integer counting/Strassen versus independent clique enumeration."""
import itertools,math,random,json
if not __debug__:raise RuntimeError('Refusing -O: assertions required.')
def add(A,B,sgn=1):return [[a+sgn*b for a,b in zip(r,s)] for r,s in zip(A,B)]
def product(A,B):
 n=len(A)
 if n<=2:return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
 h=n//2
 def split(M):return [ [r[:h] for r in M[:h]],[r[h:] for r in M[:h]],[r[:h] for r in M[h:]],[r[h:] for r in M[h:]] ]
 a,b,c,d=split(A);e,f,g,hb=split(B)
 m1=product(add(a,d),add(e,hb));m2=product(add(c,d),e);m3=product(a,add(f,hb,-1));m4=product(d,add(g,e,-1));m5=product(add(a,b),hb);m6=product(add(c,a,-1),add(e,f));m7=product(add(b,d,-1),add(g,hb))
 C11=add(add(add(m1,m4),m5,-1),m7);C12=add(m3,m5);C21=add(m2,m4);C22=add(add(add(m1,m2,-1),m3),m6)
 return [x+y for x,y in zip(C11,C12)]+[x+y for x,y in zip(C21,C22)]
def count(n,E,k):
 def clique(S):return all(tuple(sorted(e)) in E for e in itertools.combinations(S,2))
 brute=sum(clique(S) for S in itertools.combinations(range(n),k))
 if k<3:return brute
 sizes=[k//3+(i<k%3) for i in range(3)]
 A,B,C=[[S for S in itertools.combinations(range(n),z) if clique(S)] for z in sizes]
 def compatible(S,T):return not set(S)&set(T) and all(tuple(sorted((u,v))) in E for u in S for v in T)
 N=1
 while N<max(len(A),len(B),len(C)):N*=2
 P=[[0]*N for _ in range(N)];Q=[[0]*N for _ in range(N)]
 for i,S in enumerate(A):
  for j,T in enumerate(B):P[i][j]=int(compatible(S,T))
 for i,S in enumerate(B):
  for j,T in enumerate(C):Q[i][j]=int(compatible(S,T))
 H=product(P,Q);total=sum(H[i][j] for i,S in enumerate(A) for j,T in enumerate(C) if compatible(S,T))
 D=math.factorial(k)//math.prod(math.factorial(z) for z in sizes)
 assert total%D==0 and total//D==brute
 return brute
cases=0
for n in range(1,6):
 edges=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(edges)):
  E={e for j,e in enumerate(edges) if mask>>j&1}
  for k in range(1,n+1):count(n,E,k);cases+=1
rng=random.Random(20261021)
for n in (6,7,8):
 graphs=[set(itertools.combinations(range(n),2)),set()]+[{e for e in itertools.combinations(range(n),2) if rng.randrange(2)} for _ in range(8)]
 for E in graphs:
  for k in range(1,n+1):count(n,E,k);cases+=1
print(json.dumps({'status':'PASS','graph_parameter_cases':cases,'all_graphs_through_order':5,'seeded_and_complete_graphs_through_order':8,'integer_strassen_product':True,'partition_multiplicity_checked':True,'finite_only':True},indent=2))
