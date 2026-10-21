# SPDX-License-Identifier: Apache-2.0
"""Actual bottom-up splaying with exact rational changing potentials."""
from fractions import Fraction
from functools import lru_cache
import itertools,json,math
if not __debug__:
    raise RuntimeError('Run without -O: assertions are part of this checker')

@lru_cache(None)
def shapes(lo,hi):
    if lo==hi:return (None,)
    return tuple((k,l,r) for k in range(lo,hi) for l in shapes(lo,k) for r in shapes(k+1,hi))

class Node:
    def __init__(self,k,parent):self.k=k;self.p=parent;self.l=None;self.r=None

def build(shape,parent=None,nodes=None):
    if nodes is None:nodes={}
    if shape is None:return None,nodes
    k,l,r=shape;x=Node(k,parent);nodes[k]=x
    x.l,_=build(l,x,nodes);x.r,_=build(r,x,nodes)
    return x,nodes

def rotate(x):
    p=x.p;g=p.p
    if x is p.l:
        p.l=x.r
        if x.r:x.r.p=p
        x.r=p
    else:
        assert x is p.r
        p.r=x.l
        if x.l:x.l.p=p
        x.l=p
    p.p=x;x.p=g
    if g:
        if g.l is p:g.l=x
        else:assert g.r is p;g.r=x

def splay(x):
    rotations=0
    while x.p:
        p=x.p;g=p.p
        if g is None:rotate(x);rotations+=1
        elif (g.l is p)==(p.l is x):rotate(p);rotate(x);rotations+=2
        else:rotate(x);rotate(x);rotations+=2
    return x,rotations

def potential(root,w):
    if root is None:return Fraction(0),Fraction(1)
    sl,pl=potential(root.l,w);sr,pr=potential(root.r,w)
    total=sl+sr+w[root.k]
    return total,total*pl*pr

sequences=steps=0
for n in range(1,5):
    assert len(shapes(0,n))==math.comb(2*n,n)//(n+1)
    for shape in shapes(0,n):
        for length in range(5):
            for seq in itertools.product(range(n),repeat=length):
                root,nodes=build(shape);recent=list(range(n));sequences+=1
                for key in seq:
                    w={k:Fraction(1,(i+1)**2) for i,k in enumerate(recent)}
                    W,Pold=potential(root,w);depth=0;q=nodes[key]
                    while q.p:depth+=1;q=q.p
                    root,rot=splay(nodes[key]);_,Psplay=potential(root,w)
                    assert rot==depth
                    assert 2**rot*Psplay/Pold<=2*(W/w[key])**3
                    t=recent.index(key)+1
                    recent.remove(key);recent.insert(0,key)
                    wnew={k:Fraction(1,(i+1)**2) for i,k in enumerate(recent)}
                    Wnew,Pnew=potential(root,wnew)
                    assert Wnew==W and Pnew<=Psplay
                    assert 2**(rot+1)*Pnew/Pold<=32*t**6
                    assert Fraction(1,math.factorial(n)**2)<=Pnew<=2**n
                    assert root.k==key and root.p is None
                    steps+=1
print(json.dumps({'status':'PASS','all_BST_shapes_through_n':4,'sequence_lengths_through':4,'sequences':sequences,'accesses_checked':steps,'arithmetic':'exact Fraction; no floating logs'}))
