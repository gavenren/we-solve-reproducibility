"""Independent supplemental finite audits: product-cycle failures and Gini.

The published proofs cover arbitrary sizes; these exact finite checks
exercise the newly added extension conventions and endpoint statistics.
"""
from itertools import combinations, permutations, combinations_with_replacement
from fractions import Fraction
import importlib.util
from pathlib import Path
import json

author_checker=Path(__file__).parent/'reviews_e'/'matching_checks.py'
spec=importlib.util.spec_from_file_location('matching_audit_support',author_checker)
support=importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)

adj=[set() for _ in range(12)]
ranks=[{} for _ in range(12)]
for vertices in (list(range(4)),list(range(4,10))):
    for index,i in enumerate(vertices):
        successor=vertices[(index+1)%len(vertices)]
        predecessor=vertices[(index-1)%len(vertices)]
        adj[i]={successor,predecessor}
        ranks[i]={successor:0,predecessor:1}
adj[10]={11}; adj[11]={10}; ranks[10]={11:0}; ranks[11]={10:0}
stable=[m for m in support.partial_matchings(adj)
        if support.stable_roommates(m,ranks)]
assert len(stable)==4
pairsets=[frozenset((i,j) for i,j in enumerate(m) if i<j) for m in stable]
fixed=set.intersection(*(set(q) for q in pairsets))
assert fixed=={(10,11)}
failure_budgets=0
for original in pairsets:
    nonfixed=original-fixed
    for a in range(1,8):
        costs=[]
        for size in range(min(a,len(nonfixed))+1):
            for failure in combinations(nonfixed,size):
                failure=set(failure)
                costs.append(min(len(original-repair)-len(failure)
                                 for repair in pairsets if not(repair & failure)))
        predicted=sum([2,1][:min(a,2)])
        assert max(costs)==predicted
        failure_budgets+=1

def convex_sum(z,power):
    return sum(q**power for q in z)

def gini(z):
    total=sum(z)
    return (Fraction(sum(abs(x-y) for x in z for y in z),2*len(z)*total)
            if total else None)

income_cases=0
orders=list(permutations(range(3)))
for a in combinations_with_replacement(range(3),3):
    for b in combinations_with_replacement(range(3),3):
        low=[a[i]+b[2-i] for i in range(3)]
        high=[a[i]+b[i] for i in range(3)]
        for order in orders:
            z=[a[i]+b[order[i]] for i in range(3)]
            for power in (2,3,4):
                assert convex_sum(low,power)<=convex_sum(z,power)<=convex_sum(high,power)
            if sum(z):
                assert gini(low)<=gini(z)<=gini(high)
            income_cases+=1
print(json.dumps({'disconnected_cycle_failure_budget_checks':failure_budgets,
                  'stable_matchings_in_failure_test':len(stable),
                  'sorting_income_permutation_checks':income_cases,
                  'all_passed':True},indent=2))
