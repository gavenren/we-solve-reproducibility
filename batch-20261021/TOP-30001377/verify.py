# SPDX-License-Identifier: Apache-2.0
"""Direct cube-edge tests for independent balanced block conjunctions."""
import sys
if not __debug__:
    raise SystemExit('Refusing -O: assertions are required')
from itertools import combinations,product
from random import Random
rng=Random(1377)
BAL=[sum(1<<i for i in ones) for ones in combinations(range(4),2)]
configs=[(list(t),[2,2]) for t in product(BAL,repeat=2)]
configs += [(list(t),[2,2,2]) for t in product(BAL,repeat=3)]
# Unequal, larger internal blocks are not just weighted coordinate functions.
for _ in range(90):
 sizes=[rng.randrange(1,4) for _ in range(4)];tables=[]
 for b in sizes:
  ids=list(range(1<<b));rng.shuffle(ids);tables.append(sum(1<<i for i in ids[:1<<(b-1)]))
 configs.append((tables,sizes))
families=0;conditional=0;edge_profiles=0
for tables,sizes in configs:
 n=len(tables);N=sum(sizes);C=1<<N;offsets=[];s=0
 for b in sizes:offsets.append(s);s+=b
 values=[]
 for tab,b,o in zip(tables,sizes,offsets):values.append([(tab>>((x>>o)&((1<<b)-1)))&1 for x in range(C)])
 sensitivities=[[sum(v[x]!=v[x^(1<<j)] for j in range(N)) for x in range(C)] for v in values]
 A=[max(z[x] for z in sensitivities) for x in range(C)];a=sum(A)
 conjunctions=[];gsens=[]
 for J in range(1<<n):
  v=[int(all(values[j][x] for j in range(n) if (J>>j)&1)) for x in range(C)]
  z=[sum(v[x]!=v[x^(1<<j)] for j in range(N)) for x in range(C)]
  conjunctions.append(v);gsens.append(z);edge_profiles+=C
  assert sum(A[x] for x in range(C) if v[x])*2**J.bit_count()<=4*a
  conditional+=1
 if n<=3:choices=product(range(1<<n),repeat=n)
 else:choices=[tuple(rng.randrange(1<<n) for _ in range(n)) for _ in range(100)]
 q=(4*n-1).bit_length()
 for Js in choices:
  lhs=sum(max(gsens[J][x] for J in Js) for x in range(C))
  assert lhs<=(q+2)*a
  families+=1
# Literal shared-dimension cases: four input bits, four functions, with
# two nontrivial two-bit blocks plus constant-one and constant-zero padding.
padded=0
for tab0,tab1 in product(BAL,repeat=2):
 vals=[[(tab0>>(x&3))&1 for x in range(16)],[(tab1>>((x>>2)&3))&1 for x in range(16)],[1]*16,[0]*16]
 sf=[[sum(v[x]!=v[x^(1<<j)] for j in range(4)) for x in range(16)] for v in vals]
 aa=sum(max(z[x] for z in sf) for x in range(16))
 zz=[]
 for J in range(16):
  v=[int(all(vals[j][x] for j in range(4) if (J>>j)&1)) for x in range(16)]
  zz.append([sum(v[x]!=v[x^(1<<j)] for j in range(4)) for x in range(16)])
 for _ in range(25):
  Js=[rng.randrange(16) for j in range(4)]
  assert sum(max(zz[J][x] for J in Js) for x in range(16))<=6*aa
  padded+=1
print('PASS:',len(configs),'balanced block configurations;',families,'conjunction families;',conditional,'weighted conditioning tests;',edge_profiles,'direct cube-edge profiles;',padded,'literal-dimension constant-padding families')
