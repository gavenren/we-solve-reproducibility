# SPDX-License-Identifier: Apache-2.0
"""Exact tests of a Barrington compiler against independent formula semantics."""
import sys
if not __debug__:
    raise SystemExit('Refusing -O: assertions are required')
from itertools import permutations, product
from random import Random
E=tuple(range(5))
def mul(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a): return tuple(a.index(i) for i in range(5))
def cyc(a):
    p=list(E)
    for x,y in zip(a,a[1:]+a[:1]): p[x-1]=y-1
    return tuple(p)
A=cyc([1,2,3,4,5]);B=cyc([1,3,5,4,2]);C=mul(mul(mul(A,B),inv(A)),inv(B))
def is5(a):
    i=0;seen=set()
    while i not in seen: seen.add(i);i=a[i]
    return i==0 and len(seen)==5
assert is5(C)
PERMS=list(permutations(range(5)))
def conjugator(a,b):
    return next(s for s in PERMS if mul(mul(s,a),inv(s))==b)
def conjugate(p,a,b):
    s=conjugator(a,b);si=inv(s)
    return [(v,mul(mul(s,x),si),mul(mul(s,y),si)) for v,x,y in p]
def inverse(p): return [(v,inv(x),inv(y)) for v,x,y in p[::-1]]
def complement(p,a):
    q=inverse(p);v,x,y=q[0];q[0]=(v,mul(a,x),mul(a,y));return q

def compile_f(f,target=A):
    if isinstance(f,int): return [(f,E,target)]
    op=f[0]
    if op=='not':return complement(compile_f(f[1],target),target)
    p=compile_f(f[1],A);q=compile_f(f[2],B)
    if op=='or':p=complement(p,A);q=complement(q,B)
    out=conjugate(p+q+inverse(p)+inverse(q),C,target)
    return complement(out,target) if op=='or' else out

def semantic(f,bits):
    if isinstance(f,int):return bits[f]
    if f[0]=='not':return 1-semantic(f[1],bits)
    a=semantic(f[1],bits);b=semantic(f[2],bits)
    return a&b if f[0]=='and' else a|b

def evaluate(p,bits):
    a=E
    for v,x,y in p:a=mul(a,y if bits[v] else x)
    return a

def height(f):return 0 if isinstance(f,int) else 1+max(map(height,f[1:]))
# All depth-at-most-two formulas over two inputs (including NOT).
levels=[0,1]
for d in range(2):
    old=list(levels);levels=old+[('not',x) for x in old]+[(op,x,y) for op in ('and','or') for x in old for y in old]
rng=Random(6707)
def random_f(d,n):
    if d==0 or rng.randrange(5)==0:return rng.randrange(n)
    if rng.randrange(4)==0:return ('not',random_f(d-1,n))
    return (rng.choice(('and','or')),random_f(d-1,n),random_f(d-1,n))
forms=[(f,2) for f in levels]+[(random_f(5,5),5) for _ in range(120)]
checks=0
for f,n in forms:
    p=compile_f(f)
    assert len(p)<=4**height(f)
    for bits in product((0,1),repeat=n):
        assert evaluate(p,bits)==(A if semantic(f,bits) else E)
        checks+=1
for target in [p for p in PERMS if is5(p)]:
    p=compile_f(('and',('not',0),1),target)
    for bits in product((0,1),repeat=2):assert evaluate(p,bits)==(target if bits==(0,1) else E)
print('PASS:',len(forms),'compiled formulas;',checks,'truth-table comparisons; all 24 output 5-cycles; explicit commutator verified')
