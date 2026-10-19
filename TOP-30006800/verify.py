# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def reach(n,E):
    rows=[1<<v for v in range(n)]
    for a,b in E:rows[a]|=1<<b;rows[b]|=1<<a
    length=1
    while length<max(n-1,1):
        old=rows;rows=[0]*n
        for v in range(n):
            for u in range(n):
                if old[v]>>u&1:rows[v]|=old[u]
        length*=2
    return rows

def candidate(n,E):
    full=reach(n,E)
    if any(row.bit_count()%2 for row in full):return None
    M=[]
    for e in E:
        a,b=e
        if reach(n,[f for f in E if f!=e])[a].bit_count()%2:M.append(e)
    if all(sum(v in e for e in M)==1 for v in range(n)):return M
    return None

def perfect(n,E):
    def go(S):
        if not S:return True
        a=min(S)
        return any(a in e and set(e)<=S and go(S-set(e)) for e in E)
    return go(set(range(n)))
cases=0;no=0
for n in range(7):
    pairs=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        E=[e for i,e in enumerate(pairs) if mask>>i&1];parents=list(range(n))
        def find(v):
            while parents[v]!=v:v=parents[v]
            return v
        acyclic=True
        for a,b in E:
            a,b=find(a),find(b)
            if a==b:acyclic=False;break
            parents[a]=b
        if not acyclic:continue
        M=candidate(n,E);want=perfect(n,E);assert (M is not None)==want
        if M is not None:assert len({v for e in M for v in e})==n
        no+=not want;cases+=1
RESULTS=dict(cases=cases,no_instances=no,exhaustive_forest_order=[0,6],oracle='full recursive perfect matching search',checks='actual Boolean reachability squarings, component parity, edge deletion parities, matching matrix predicate')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
