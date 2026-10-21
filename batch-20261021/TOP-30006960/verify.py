# SPDX-License-Identifier: Apache-2.0
"""Column-run algorithm versus direct existential Boolean product."""
import itertools,json,random
if not __debug__:
    raise RuntimeError('Run without -O: assertions are part of this checker')

def run_product(a,b):
    n=len(a);runs=[]
    for j in range(n):
        col=[];k=0
        while k<n:
            if not b[k][j]:k+=1;continue
            left=k
            while k<n and b[k][j]:k+=1
            col.append((left,k))
        runs.append(col)
    c=[]
    for row in a:
        p=[0]
        for x in row:p.append(p[-1]+x)
        c.append([int(any(p[r]>p[l] for l,r in col)) for col in runs])
    return c,sum(map(len,runs))

def naive(a,b):
    n=len(a)
    return [[int(any(a[i][k] and b[k][j] for k in range(n))) for j in range(n)] for i in range(n)]

cases=0
for n in range(4):
    mats=[[[mask>>(i*n+j)&1 for j in range(n)] for i in range(n)] for mask in range(1<<(n*n))]
    for a in mats:
        for b in mats:
            c,kappa=run_product(a,b)
            assert c==naive(a,b)
            assert kappa<=n*((n+1)//2)
            cases+=1
rng=random.Random(20261021)
for n in [4,7,12]:
    for trial in range(30):
        a=[[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        b=[[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        assert run_product(a,b)[0]==naive(a,b);cases+=1
for n in [2,5,20]:
    a=[[int(i!=j) for j in range(n)] for i in range(n)]
    b=[[int(k<=j) for j in range(n)] for k in range(n)]
    c,kappa=run_product(a,b)
    assert kappa==n and c==naive(a,b)
    assert sum(a[i][k]*b[k][j] for i in range(n) for j in range(n) for k in range(n))==(n-1)*n*(n+1)//2
print(json.dumps({'status':'PASS','matrix_pairs_checked':cases,'exhaustive_dimensions':[0,1,2,3],'additional_structured_dimensions':[2,5,20]}))
