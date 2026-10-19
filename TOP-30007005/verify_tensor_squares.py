# SPDX-License-Identifier: Apache-2.0
"""Complete exact character-table search, degrees 1..16, without third-party code."""
import sys
if sys.flags.optimize:
    raise SystemExit('Refusing optimized Python: assertions must remain enabled.')
from functools import lru_cache
from math import factorial, prod
from collections import Counter
from itertools import permutations
from pathlib import Path
import json

@lru_cache(None)
def partitions(n, bound=None):
    if n==0:return ((),)
    if bound is None:bound=n
    ans=[]
    for x in range(min(n,bound),0,-1):
        ans.extend((x,)+rest for rest in partitions(n-x,x))
    return tuple(ans)

def conjugate(lam):
    return tuple(sum(x>=j for x in lam) for j in range(1,lam[0]+1)) if lam else ()

def cells(lam):
    return {(i,j) for i,r in enumerate(lam) for j in range(r)}

@lru_cache(None)
def rim_removals(lam,k):
    big=cells(lam);ans=[]
    for mu in partitions(sum(lam)-k):
        if len(mu)>len(lam) or any(x>lam[i] for i,x in enumerate(mu)):continue
        skew=big-cells(mu)
        if any((i+1,j) in skew and (i,j+1) in skew and (i+1,j+1) in skew for i,j in skew):continue
        start=next(iter(skew)); seen={start}; todo=[start]
        while todo:
            i,j=todo.pop()
            for v in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if v in skew and v not in seen:seen.add(v);todo.append(v)
        if len(seen)==k:
            ans.append((mu,(-1)**(len({i for i,j in skew})-1)))
    return tuple(ans)

@lru_cache(None)
def character(lam,cycle):
    assert sum(lam)==sum(cycle)
    if not cycle:return 1
    return sum(sign*character(mu,cycle[1:]) for mu,sign in rim_removals(lam,cycle[0]))

def centralizer(cycle):
    return prod(k**m*factorial(m) for k,m in Counter(cycle).items())

def hook_degree(lam):
    hooks=prod(lam[i]-j+sum(r>j for r in lam[i+1:]) for i,row in enumerate(lam) for j in range(row))
    return factorial(sum(lam))//hooks

@lru_cache(None)
def determinant_terms(lam):
    # Pad to n variables, exactly as in the primary Frobenius formula.
    n=sum(lam); padded=lam+(0,)*(n-len(lam)); ans=[]
    for perm in permutations(range(n)):
        caps=tuple(padded[i]-i+perm[i] for i in range(n))
        if min(caps)<0:continue
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        ans.append(((-1)**inversions,tuple(sorted(caps,reverse=True))))
    return tuple(ans)

@lru_cache(None)
def power_sum_coefficient(cycle,caps):
    # Repeated equal-length cycles remain separate factors, so assigning their
    # lengths recursively counts the correct multinomial coefficient.
    if not cycle:return int(not any(caps))
    k=cycle[0]; total=0
    for i,cap in enumerate(caps):
        if cap>=k:
            reduced=list(caps);reduced[i]-=k
            total+=power_sum_coefficient(cycle[1:],tuple(sorted(reduced,reverse=True)))
    return total

def frobenius_character(lam,cycle):
    return sum(sign*power_sum_coefficient(cycle,caps) for sign,caps in determinant_terms(lam))

def main():
    output=[];tables=0;orthogonality_pairs=0;frobenius_entries=0
    for n in range(1,17):
        ps=partitions(n);fact=factorial(n)
        sizes=[fact//centralizer(c) for c in ps]
        rows=[[character(lam,c) for c in ps] for lam in ps]
        if n<=7:
            for i,lam in enumerate(ps):
                for j,cycle in enumerate(ps):
                    assert rows[i][j]==frobenius_character(lam,cycle),(n,lam,cycle)
                    frobenius_entries+=1
        for i,lam in enumerate(ps):
            assert rows[i][-1]==hook_degree(lam)
            for j in range(i+1):
                dot=sum(a*b*s for a,b,s in zip(rows[i],rows[j],sizes))
                assert dot==(fact if i==j else 0),(n,lam,ps[j],dot)
                orthogonality_pairs+=1
        assert sum(row[-1]**2 for row in rows)==fact
        tables+=1
        candidates=[]
        for i,lam in enumerate(ps):
            if lam!=conjugate(lam):continue
            square=[a*a*s for a,s in zip(rows[i],sizes)]
            numerators=[sum(a*b for a,b in zip(square,row)) for row in rows]
            assert all(v>=0 and v%fact==0 for v in numerators)
            multiplicities=[v//fact for v in numerators]
            assert sum(m*row[-1] for m,row in zip(multiplicities,rows))==rows[i][-1]**2
            if min(multiplicities)>0:
                candidates.append({'partition':lam,'dimension':rows[i][-1],'minimum_multiplicity':min(multiplicities),'multiplicities_in_partition_order':multiplicities})
        assert bool(candidates)==(n not in (2,4,9)),(n,candidates)
        record={'n':n,'irreducibles':len(ps),'self_conjugate_candidates':sum(lam==conjugate(lam) for lam in ps),'universal_candidates':len(candidates),'witness':candidates[0] if candidates else None}
        output.append(record)
        print(json.dumps({k:v for k,v in record.items() if k!='witness'},sort_keys=True),flush=True)
    out={'all_assertions_passed':True,'range':[1,16],'complete_character_tables':tables,'row_orthogonality_pairs':orthogonality_pairs,'frobenius_oracle_range':[1,7],'frobenius_oracle_entries':frobenius_entries,'results':output,'method':'Murnaghan-Nakayama via all connected no-2x2 skew rim hooks; exact integer class sums; independent Vandermonde/power-sum Frobenius coefficients through n=7, hook-length degrees and full row orthogonality'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: complete exact search for n=1..16; exceptional degrees exactly 2,4,9 within this range.')
if __name__=='__main__':main()
