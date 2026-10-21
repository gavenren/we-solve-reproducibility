# SPDX-License-Identifier: Apache-2.0
"""Independent brute game evaluation versus width-two quantifier elimination."""
import sys,itertools,random,json
if not __debug__:
    raise RuntimeError('Refusing -O: assertions are required.')

def normalize(F):
    return frozenset(frozenset(c) for c in F if not any(-x in c for x in c))
def truth(F,a):
    return all(any(a[abs(x)] == (x>0) for x in c) for c in F)
def game(F,prefix,a=None):
    a={} if a is None else a
    if not prefix:return truth(F,a)
    x,Q=prefix[0]
    vals=[]
    for v in (False,True):
        b=dict(a);b[x]=v;vals.append(game(F,prefix[1:],b))
    return all(vals) if Q=='A' else any(vals)
def eliminate(F,prefix):
    F=normalize(F);saved={}
    for x,Q in reversed(prefix):
        saved[x]=F
        P=[c-{x} for c in F if x in c];N=[c-{-x} for c in F if -x in c]
        G=[c for c in F if x not in c and -x not in c]
        F=normalize(G+([a|b for a in P for b in N] if Q=='E' else P+N))
        assert all(len(c)<=2 for c in F)
    return frozenset() not in F,saved

def strategy_wins(F,prefix,saved,a=None):
    a={} if a is None else a
    if not prefix:return truth(F,a)
    x,Q=prefix[0]
    if Q=='A': vals=(False,True)
    else:
        # Positive x clause forces1 exactly when its other literal is false.
        forced=any(not any(a[abs(z)]==(z>0) for z in c-{x}) for c in saved[x] if x in c)
        vals=(forced,)
    for v in vals:
        b=dict(a);b[x]=v
        if not strategy_wins(F,prefix[1:],saved,b):return False
    return True
cases=0;strategies=0
for n in range(3):
    literals=[z for x in range(1,n+1) for z in (x,-x)]
    clauses=[frozenset()]+[frozenset([x]) for x in literals]+[frozenset(c) for c in itertools.combinations(literals,2) if c[0]!=-c[1]]
    for mask in range(1<<len(clauses)):
        F=[c for i,c in enumerate(clauses) if mask>>i&1]
        for qs in itertools.product('AE',repeat=n):
            prefix=list(zip(range(1,n+1),qs));v,saved=eliminate(F,prefix)
            assert v==game(F,prefix)
            if v: assert strategy_wins(F,prefix,saved);strategies+=v
            cases+=1
rng=random.Random(20261021)
for _ in range(3000):
    n=rng.randrange(1,9);order=list(range(1,n+1));rng.shuffle(order)
    prefix=[(x,rng.choice('AE')) for x in order]
    F=[]
    for j in range(rng.randrange(0,25)):
        F.append(frozenset(rng.choice([-1,1])*rng.randrange(1,n+1) for _ in range(rng.randrange(0,3))))
    v,saved=eliminate(F,prefix)
    assert v==game(F,prefix)
    if v: assert strategy_wins(F,prefix,saved);strategies+=v
    cases+=1
print(json.dumps({'status':'PASS','formulas_and_prefixes':cases,'winning_strategies_exhaustively_played':strategies,'exhaustive_variables':2,'seeded_max_variables':8,'finite_only':True},indent=2))
