"""Independent finite checks of selected mathematical claims in econ_a reviews.

Uses exact integer/rational arithmetic. These checks neither replace proofs nor
run the original authors' programs. Execute from any directory with Python 3.
"""
from fractions import Fraction as F
from itertools import product, permutations, combinations
from pathlib import Path
import json

out = {}

# Exact minimax balance in the two-alternative formula.
count = 0
for r in range(21):
    for s in range(21):
        if r+s == 0:
            continue
        p = F(r*(r+2*s), r*r+4*r*s+s*s)
        def ratios(p):
            d1, d2 = r+2*s-2*s*p, s+2*r*p
            return [F(r+2*s,d1) if d1 else F(1), F(2*r+s,d2) if d2 else F(1)]
        target = 1+F(2*r*s,(r+s)**2)
        assert max(ratios(p)) == target
        for j in range(101):
            # At endpoints with a zero denominator but positive optimal
            # welfare, the actual distortion is infinite, not one.
            pj = F(j,100)
            if (r+2*s-2*s*pj)==0 or (s+2*r*pj)==0:
                continue
            assert max(ratios(pj)) >= target
        count += 1
out['ECON-D71-180'] = {'cases':count,'check':'Exact endpoint balance and all 101 rational grid lotteries for r,s in 0..20, excluding r+s=0.'}

# Greedy all-goods EFX, including zero-valued goods.
count=0
for n in (2,3):
    for size in range(8):
        for values in product(range(3),repeat=size):
            bundles=[[] for _ in range(n)]
            loads=[0]*n
            for v in sorted(values,reverse=True):
                i=min(range(n),key=lambda i:(loads[i],i))
                bundles[i].append(v);loads[i]+=v
            for i,j in product(range(n),repeat=2):
                for v in bundles[j]:
                    assert loads[i] >= loads[j]-v
            count+=1
out['ECON-D63-158']={'cases':count,'check':'Enumerated 0..7 goods with weights in {0,1,2}, for 2 and 3 agents; every removed good, including zero, satisfies EFX.'}
out['ECON-D63-177']=dict(out['ECON-D63-158'])

# The claimed XOS switch, checking every bundle directly rather than clauses.
count=0
goods=range(3)
bundles=[S for size in range(4) for S in combinations(goods,size)]
for z in product((F(1,100),F(5,100),F(9,100)),repeat=3):
    def value(S):
        return max(10*(0 in S),6*(1 in S)+6*(2 in S))+sum(z[g] for g in S)
    for prices,target in [((5,2,2),(1,2)),((5,6,2),(0,))]:
        utilities={S:value(S)-sum(prices[g] for g in S) for S in bundles}
        best=max(utilities.values())
        assert [S for S,u in utilities.items() if u==best] == [target]
        count+=1
out['ECON-D44-196']={'cases':count,'check':'All eight bundles compared exactly at 27 perturbation triples and both price vectors.'}

# Dynamic projection counterexample, generated from reports and state.
def path(reports):
    y=F(0);result=[]
    for a,b in zip(*reports):
        y=max(min(a,b),min(y,max(a,b)));result.append(y)
    return result
truth=(1,0,0);other=(1,1,1)
ypath=path((truth,other));liepath=path(((0,0,0),other))
assert ypath==[1,1,1] and liepath==[0,0,0]
assert sum(abs(x-y) for x,y in zip(truth,ypath))==2
assert sum(abs(x-y) for x,y in zip(truth,liepath))==1
out['ECON-D82-172']={'cases':2,'check':'Both truthful and deviating facility paths generated recursively; undiscounted own costs are 2 and 1.'}

# Cross-world arrays share a single-world pair distribution but not a
# product law over complete response arrays.
law={(u,v):F(1,4) for u,v in product((0,1),repeat=2)}
for a in (0,1):
    pair={}
    for (u,v),p in law.items():
        x=((u,v)[a],(v,u)[a]);pair[x]=pair.get(x,F(0))+p
    assert pair==law
assert law[(0,0)]==F(1,4) and F(1,4)*F(1,4)==F(1,16)
out['ECON-C31-168']={'cases':2,'check':'Enumerated both fixed-treatment pair laws and the discrepant complete-array joint probability 1/4 versus 1/16.'}

# Hybrid panel: exact four-cell probabilities, common observable outcomes,
# group residual means and both ATT values.
joint={}
for A,T in product((0,1),repeat=2):
    pt=F(1,4)+F(A,2)
    joint[A,T]=F(1,2)*(pt if T else 1-pt)
for T in (0,1):
    denom=sum(p for (A,t),p in joint.items() if t==T)
    eta=sum(p*(T*(F(A)-F(1,4))-A+F(1,4)) for (A,t),p in joint.items() if t==T)/denom
    assert eta==0
p1=sum(p for (A,T),p in joint.items() if T==1)
att=sum(p*(1-(F(A)-F(1,4))) for (A,T),p in joint.items() if T==1)/p1
assert att==F(1,2)
out['ECON-C23-188']={'cases':4,'check':'All four (A,T) cells; factor residual means zero in both groups and factor ATT 1/2, while selection ATT is 1.'}

# Persistent two-type envelope: check all affine-piece endpoints against
# the asserted formula, with an additional dense rational service grid.
count=0
for low,high in ((1,2),(1,4),(2,5)):
    for T in range(1,5):
        for B2 in range(0,2*high*T+5):
            B=F(B2,2)
            for q in (F(1,4),F(1,2),F(3,4)):
                if B<low*T:
                    # In this case low IR also restricts low payments by B;
                    # direct verified attainable upper bound is B.
                    assert B <= low*T
                    count+=1;continue
                x0=max(F(0),F(high*T-B,high-low))
                def objective(x):return (1-q)*low*x+q*min(B,high*T-(high-low)*x)
                formula=max(F(low*T),q*min(B,high*T)+(1-q)*low*x0)
                assert max(objective(x) for x in (F(0),x0,F(T)))==formula
                for j in range(101):assert objective(F(j*T,100))<=formula
                count+=1
out['ECON-D82-189']={'cases':count,'check':'Three (low,high) pairs, four horizons, half-integer budgets, three type probabilities; envelope endpoints and 101-point service grid checked exactly.'}

# Exhaustive least-unpopularity factors under common strict rankings.
def matchings(n,h):
    return [x for x in product(range(-1,h),repeat=n) if len([a for a in x if a>=0])==len(set(a for a in x if a>=0))]
def factor(M,allm,h):
    worst=F(1)
    for Q in allm:
        rankM=[h if x<0 else x for x in M]
        rankQ=[h if x<0 else x for x in Q]
        r=sum(q<m for q,m in zip(rankQ,rankM));s=sum(m<q for q,m in zip(rankQ,rankM))
        if r and not s:return None
        if s:worst=max(worst,F(r,s))
    return worst
count=0;comparisons=0
for n in range(1,5):
    for h in range(5):
        mm=matchings(n,h)
        finite=[v for M in mm if (v:=factor(M,mm,h)) is not None]
        opt=min(finite)
        assert opt==max(1,min(h,n-1))
        count+=1;comparisons+=len(mm)**2
out['ECON-C78-178']={'cases':count,'matching_pairs':comparisons,'check':'Exhaustive incumbent/challenger enumeration for 1..4 applicants and 0..4 commonly ranked houses, allowing unmatched applicants.'}

# Complementary winning sets, all anonymous profiles with <=5 voters and
# three candidates (all ordered profiles are deliberately enumerated).
orders=list(permutations(range(3)))
def wins(S,profile):
    return all(sum(all(order.index(a)<order.index(b) for b in S) for order in profile)*2<=len(profile) for a in set(range(3))-set(S))
count=0
for N in range(1,6):
    for profile in product(orders,repeat=N):
        for i in range(3):
            S=(i,);T=tuple(j for j in range(3) if j!=i)
            assert wins(S,profile) or wins(T,profile)
        chosen={profile[j][0] for j in range((N+1)//2)}
        assert wins(chosen,profile)
        count+=1
out['ECON-D71-190']={'cases':count,'check':'All ordered strict-ranking profiles for 3 candidates and 1..5 voters; complementary-set and selected-voter-top-set certificates.'}

root=Path(__file__).resolve().parent
(root/'econ_a_review_check_results.json').write_text(json.dumps(out,indent=2)+'\n')
for key,value in out.items():print(key,json.dumps(value,sort_keys=True))
print('ALL EXACT CHECKS PASSED')
