# SPDX-License-Identifier: Apache-2.0
"""Exact packing identity versus independent unordered-triple enumeration."""
import itertools,json
if not __debug__:
    raise RuntimeError('Run without -O: assertions are part of this checker')

def packed(s):
    n=len(s)
    if n<3:return 0
    u=max(map(abs,s),default=0)
    b=(n**3).bit_length()
    f=sum(1 << (b*(a+u)) for a in s)
    c=((f*f*f) >> (3*u*b)) & ((1<<b)-1)
    r=sum(-2*a in s for a in s)
    d=c-3*r+2*(0 in s)
    assert d>=0 and d%6==0
    return d//6

count=0
universe=range(-5,6)
for mask in range(1<<11):
    s={x for i,x in enumerate(universe) if mask>>i&1}
    expected=sum(a+b+c==0 for a,b,c in itertools.combinations(sorted(s),3))
    assert packed(s)==expected,(s,packed(s),expected)
    count+=1
assert packed({-2,1})==0 and packed({-1,0,1})==1
assert packed({-1000,0,1000})==1
print(json.dumps({'status':'PASS','all_subsets_checked':count,'independent_oracle':'enumeration of unordered 3-element subsets','large_gap_case':True}))
