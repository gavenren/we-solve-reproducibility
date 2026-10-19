# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def solve2(A,b,c):
    lines=list(zip(A,b))+[((F(-1),F(0)),F(0)),((F(0),F(-1)),F(0))];vs=[]
    for (a,s),(d,t) in itertools.combinations(lines,2):
        det=a[0]*d[1]-a[1]*d[0]
        if not det:continue
        x=((s*d[1]-a[1]*t)/det,(a[0]*t-s*d[0])/det)
        if all(q[0]*x[0]+q[1]*x[1]<=r for q,r in lines):vs.append(x)
    assert vs
    val=lambda x:c[0]*x[0]+c[1]*x[1]
    return min(map(val,vs)),lines

def dual(lines,c):
    # Independent dual certificates: nonnegative combination of constraint normals=-c.
    best=None
    for (a,s),(d,t) in itertools.combinations(lines,2):
        det=a[0]*d[1]-a[1]*d[0]
        if not det:continue
        y=((-c[0]*d[1]+c[1]*d[0])/det,(-a[0]*c[1]+a[1]*c[0])/det)
        if min(y)>=0:
            bound=-s*y[0]-t*y[1];best=bound if best is None else max(best,bound)
    if c==(F(0),F(0)):best=F(0)
    return best
lp=0
for _ in range(700):
    point=(F(rng.randrange(5)),F(rng.randrange(5)));A=[(F(1),F(0)),(F(0),F(1))];b=[F(5),F(5)]
    for j in range(rng.randrange(1,9)):
        a=(F(rng.randrange(-5,6)),F(rng.randrange(-5,6)));A.append(a);b.append(a[0]*point[0]+a[1]*point[1]+F(rng.randrange(5)))
    c=(F(rng.randrange(-5,6)),F(rng.randrange(-5,6)));answer,lines=solve2(A,b,c);assert answer==dual(lines,c);lp+=1
traces=0
for n in range(2,6):
    for _ in range(80):
        V=[[rng.randrange(-3,4) for j in range(n)] for i in range(n)];X=[[sum(V[i][h]*V[j][h] for h in range(n)) for j in range(n)] for i in range(n)]
        diag=F(sum(X[i][i] for i in range(n)),n);off=F(sum(X[i][j] for i in range(n) for j in range(n) if i!=j),n*(n-1));u=diag-off;v=diag+(n-1)*off
        assert u>=0 and v>=0
        alpha,beta=[F(rng.randrange(-5,6),rng.randrange(1,5)) for i in range(2)]
        direct=sum((alpha*(i==j)+beta)*X[j][i] for i in range(n) for j in range(n))
        assert direct==(n-1)*alpha*u+(alpha+n*beta)*v;traces+=1
RESULTS=dict(primal_dual_LP_cases=lp,exact_Gram_trace_cases=traces,oracle='independent nonnegative dual multipliers certify every bounded LP optimum',arithmetic='Fraction',limits='program tests bounded feasible LPs; full infeasible/unbounded logic is proved in report')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
