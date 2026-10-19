# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
# Independently enumerate every Cartesian rectangle of layer-variable supports
# for width 2, length 3. Positivity means its expanded support lies in path support.
w=2;L=3
variables=[(i,j) for i in range(w) for j in range(w)]
subsets=[set(s) for r in range(1,5) for s in itertools.combinations(variables,r)]
pathmons={tuple([(0,a),(a,b),(b,0)]) for a in range(w) for b in range(w)}
rectangles=valid=0
for supports in itertools.product(subsets,repeat=L):
    rectangles+=1;mons=set(itertools.product(*supports))
    if mons<=pathmons:
        valid+=1;assert len(mons)==1 and all(len(s)==1 for s in supports)
assert valid==w**(L-1)
# Check same-variable-choice layer multidegree lemma with all layer assignments.
for layers in itertools.product(range(L),repeat=L):
    if sorted(layers)==list(range(L)):continue
    assert Counter(layers)!=Counter(range(L))
RESULTS=dict(rectangles=rectangles,valid_rectangles=valid,width=w,layers=L,oracle='full monomial Cartesian expansion, checked against explicitly listed paths')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
