from functools import lru_cache
from itertools import product
import json
from pathlib import Path

def followers(x):
    ans=set()
    for i in range(6):
        j=(i+1)%6
        for a in range(x[i]+1):
            for b in range(x[j]+1):
                if (a,b)==(x[i],x[j]): continue
                y=list(x);y[i]=a;y[j]=b;ans.add(tuple(y))
    return ans

@lru_cache(None)
def grundy(x):
    vals={grundy(y) for y in followers(x)}
    g=0
    while g in vals:g+=1
    return g

states=list(product(range(4),repeat=6))
zero=sum(grundy(x)==0 for x in states)
assert zero==214
face=0
for a,b,c,d in product(range(4),repeat=4):
    x=(0,a,b,0,c,d)
    assert grundy(x)==((a+b)^(c+d));face+=1
mirror=0
for a,b,c in product(range(4),repeat=3):
    assert grundy((a,b,c,a,b,c))==0;mirror+=1
path=0
for a,b,c in product(range(4),repeat=3):
    assert (grundy((a,b,c,0,0,0))==0)==(b==0 and a==c);path+=1
# Exact numeric data from the eighteen-row "positive nonmirror certificate"
# table in ECON-C79-271-A1, revision r1 (rights holder: mehmetmars7;
# archive licence: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/).
# Canonical revision:
# https://we-solve.github.io/contributions/winning-positions-and-nim-values-in-circular-nim/attempt-1/r1/
# Revision ID: rev_95da5b7312f3429fb7687e199327e585.
# Only the numeric follower/response pairs are embedded, without alteration.
# This keeps the checker independent of source-paper files and its working directory.
pairs = [
    ((0,0,1,2,1,2), (0,0,1,1,0,2)),
    ((0,1,1,2,1,0), (0,1,0,0,1,0)),
    ((0,1,1,2,1,1), (0,1,1,0,1,1)),
    ((0,1,1,2,1,2), (0,1,1,0,0,2)),
    ((1,0,0,2,1,2), (1,0,0,2,0,1)),
    ((1,0,1,2,1,2), (1,0,1,2,0,2)),
    ((1,1,0,0,1,2), (0,1,0,0,1,0)),
    ((1,1,0,1,1,2), (1,1,0,1,1,0)),
    ((1,1,0,2,1,2), (1,1,0,2,0,0)),
    ((1,1,1,0,0,2), (0,1,1,0,0,2)),
    ((1,1,1,0,1,2), (0,1,1,0,1,1)),
    ((1,1,1,1,0,2), (0,0,1,1,0,2)),
    ((1,1,1,1,1,2), (1,1,1,1,1,1)),
    ((1,1,1,2,0,0), (1,1,0,2,0,0)),
    ((1,1,1,2,0,1), (1,0,0,2,0,1)),
    ((1,1,1,2,0,2), (1,0,1,2,0,2)),
    ((1,1,1,2,1,0), (1,1,0,1,1,0)),
    ((1,1,1,2,1,1), (1,1,1,1,1,1)),
]
x=(1,1,1,2,1,2)
assert len(pairs)==18 and {a for a,b in pairs}==followers(x)
for y,z in pairs:
    assert z in followers(y)
    assert grundy(z)==0
assert grundy(x)==0
out=dict(states=len(states),zero_grundy=zero,opposite_zero_face=face,mirror_family=mirror,three_heap_path=path,certificate_rows=len(pairs),all_checks_passed=True,limits='Bounded enumeration only; infinite claims require the separate mathematical proofs.')
Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
