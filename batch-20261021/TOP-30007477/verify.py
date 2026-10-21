# SPDX-License-Identifier: Apache-2.0
"""Exact edge enumeration, symmetric profiles and zero-threshold checks."""
import sys,itertools,math,json
if not __debug__:
    raise RuntimeError('Refusing -O: assertions are required.')

def edge_count(n, profile):
    return sum(profile[x.bit_count()] != profile[(x^(1<<j)).bit_count()]
               for x in range(1<<n) for j in range(n))

profiles=0; cube_profiles=0; zero_polynomials=0
for n in range(1,15):
    weights=sorted((math.comb(n-1,k) for k in range(n)),reverse=True)
    maxima=[0]*(n+1)
    for mask in range(1<<(n+1)):
        f=[(mask>>k)&1 for k in range(n+1)]
        transitions=[k for k in range(n) if f[k]!=f[k+1]]
        num=2*sum((n-k)*math.comb(n,k) for k in transitions)
        for d in range(len(transitions),n+1): maxima[d]=max(maxima[d],num)
        if n<=8:
            assert edge_count(n,f)==num
            cube_profiles+=1
        profiles+=1
    for d in range(n+1):
        expected=2*n*sum(weights[:d])
        assert maxima[d]==expected
        assert expected**2 <= 2*n*d*d*(1<<n)**2
    # Half-integer roots realize each transition set, with no cube zeros.
    for Jmask in range(1<<n):
        J=[k for k in range(n) if Jmask>>k&1]
        f=[math.prod(2*t-2*k-1 for k in J)>=0 for t in range(n+1)]
        assert [k for k in range(n) if f[k]!=f[k+1]]==J
for n in range(1,7):
    for d in range(1,5):
        for roots in itertools.combinations_with_replacement(range(n+1),d):
            f=[math.prod(t-k for k in roots)>=0 for t in range(n+1)]
            assert sum(f[k]!=f[k+1] for k in range(n))<=d
            assert edge_count(n,f)==2*sum((n-k)*math.comb(n,k) for k in range(n) if f[k]!=f[k+1])
            zero_polynomials+=1
print(json.dumps({'status':'PASS','sign_profiles':profiles,'independent_cube_edge_profiles':cube_profiles,'integer_root_zero_convention_cases':zero_polynomials,'n_max_profile':14,'n_max_cube':8,'finite_only':True},indent=2))
