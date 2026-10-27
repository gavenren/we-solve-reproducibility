# SPDX-License-Identifier: Apache-2.0
"""Exact checks for the interpolation reduction; no floating-point arithmetic."""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial, prod
import json, sys
from pathlib import Path

if not __debug__:
    raise RuntimeError('Run without -O: assertions are part of verification.')

def permanent(n, edges):
    E=set(edges)
    return sum(all((i,n+p[i]) in E for i in range(n)) for p in permutations(range(n)))

def parameters(n, edges):
    d=[0]*(2*n)
    for u,v in edges: d[u]+=1; d[v]+=1
    k=[1]*n+[x-1 for x in d[n:]]
    B=max(k)
    return d,k,[B-x for x in k],B

def degree_terms(n, edges):
    # Original x-variable edge-subset expansion, distinct from coefficient proof.
    terms={}
    for mask in range(1<<len(edges)):
        d=[0]*(2*n); sign=1
        for i,(u,v) in enumerate(edges):
            if mask>>i&1: d[u]+=1;d[v]+=1;sign=-sign
        key=tuple(d);terms[key]=terms.get(key,0)+sign
    return {k:v for k,v in terms.items() if v}

def probability(terms, c, t):
    ans=F(0)
    for ds,sgn in terms.items():
        q=F(sgn)
        for a,b in zip(ds,c):
            # integral x^a (1-x)^(t+b) dx
            q*=F(factorial(a)*factorial(t+b),factorial(a+t+b+1))
        ans+=q
    return ans

def recover(n, edges):
    d,k,c,B=parameters(n,edges);r=2*len(edges);s=B+1
    terms=degree_terms(n,edges)
    Q=[]
    for t in range(r+1):
        den=prod(t+cv+a+1 for cv,dv in zip(c,d) for a in range(dv+1))
        q=probability(terms,c,t)*den
        assert q.denominator==1
        Q.append(q)
    val=F(0)
    for t,q in enumerate(Q):
        lag=F(1)
        for j in range(r+1):
            if j!=t:lag*=F(-s-j,t-j)
        val+=lag*q
    C=prod((-1)**kv*factorial(kv)*factorial(dv-kv) for kv,dv in zip(k,d))
    result=val/C
    assert result.denominator==1
    return int(result)

def constructed_preferences(n, edges, t):
    d,k,c,B=parameters(n,edges)
    sides=[[],[]];partner={};special={};ties={}
    def pair(a,side,b):
        sides[side].append(a);sides[1-side].append(b);partner[a]=b;partner[b]=a
    for v in range(2*n):pair(('v',v),0 if v<n else 1,('p',v))
    adj={v:[] for v in range(2*n)}
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    for v in range(2*n):
        side=0 if v<n else 1;vs=('v',v)
        ties[vs]=[partner[vs]]+[('v',w) for w in adj[v]]
        for j in range(t+c[v]):
            q=('q',v,j);z=('z',v,j);pair(q,1-side,z)
            special[q]=[vs,z];ties[vs].append(q)
    options={}
    for side in [0,1]:
        for a in sides[side]:
            if a in ties:
                top=ties[a];tail=[b for b in sides[1-side] if b not in top]
                options[a]=[p+tuple(tail) for p in permutations(top)]
            else:
                top=special.get(a,[partner[a]])
                options[a]=[tuple(top+[b for b in sides[1-side] if b not in top])]
    return sides,partner,options

def brute_refinements(n,edges,t):
    sides,partner,options=constructed_preferences(n,edges,t)
    agents=sides[0]+sides[1];stable=0;total=0
    for orders in product(*(options[a] for a in agents)):
        ranks={a:{b:i for i,b in enumerate(o)} for a,o in zip(agents,orders)}
        total+=1
        blocked=any(partner[a]!=b and ranks[a][b]<ranks[a][partner[a]] and
                    ranks[b][a]<ranks[b][partner[b]] for a in sides[0] for b in sides[1])
        stable+=not blocked
    return F(stable,total),total

def main():
    count=0
    for n in range(1,4):
        all_edges=[(u,n+v) for u in range(n) for v in range(n)]
        for mask in range(1<<len(all_edges)):
            E=[e for i,e in enumerate(all_edges) if mask>>i&1]
            d=[0]*(2*n)
            for u,v in E:d[u]+=1;d[v]+=1
            if min(d)==0:continue
            assert recover(n,E)==permanent(n,E),(n,E)
            count+=1
    profiles=0;cases=0
    for n in [1,2]:
        all_edges=[(u,n+v) for u in range(n) for v in range(n)]
        for mask in range(1<<len(all_edges)):
            E=[e for i,e in enumerate(all_edges) if mask>>i&1]
            d=[0]*(2*n)
            for u,v in E:d[u]+=1;d[v]+=1
            if min(d)==0:continue
            _,_,c,_=parameters(n,E)
            for t in (range(4) if n==1 else [0]):
                got,num=brute_refinements(n,E,t)
                assert got==probability(degree_terms(n,E),c,t)
                cases+=1;profiles+=num
    out={'status':'PASS','interpolation_graphs':count,'all_bipartite_graphs_sides_at_most':3,
         'graph_filter':'no isolated vertices; isolated cases have zero permanent',
         'direct_refinement_cases':cases,'direct_refinements_enumerated':profiles,
         'arithmetic':'exact Python Fraction','scope':'finite checks; not a proof of hardness'}
    print(json.dumps(out,indent=2))
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
