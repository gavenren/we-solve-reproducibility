# SPDX-License-Identifier: Apache-2.0
"""Exact finite verification; infinite scope relies on report.md."""
if not __debug__:
    raise SystemExit("Refusing python -O: assertions are required")
import itertools, random, json, math
from fractions import Fraction as F
from collections import defaultdict, Counter, deque
from bisect import bisect_left
rng = random.Random(20261018)
def gadget(k,clauses):
    E=[];parents=[];names=[]
    def node(name):names.append(name);parents.append([]);return len(names)-1
    def arc(a,b):E.append((a,b));parents[b].append(a)
    r=node('root');truth=[];var=[];occ={}
    for i in range(k):
        t=node('t'+str(i));f=node('f'+str(i));v=node('v'+str(i));truth.append((t,f));var.append(v);arc(t,v);arc(f,v)
    def outtree(root,leaves):
        if not leaves:return
        if len(leaves)==1:arc(root,leaves[0]);return
        mid=len(leaves)//2
        for sub in [leaves[:mid],leaves[mid:]]:
            if len(sub)==1:arc(root,sub[0])
            else:z=node('split');arc(root,z);outtree(z,sub)
    outtree(r,[v for pair in truth for v in pair])
    for j,C in enumerate(clauses):
        for i,sign in C:occ[(j,i)]=node('occ')
    for i in range(k):
        leaves=[v for (j,h),v in occ.items() if h==i]
        if leaves:
            z=node('variable distribution root');arc(var[i],z);outtree(z,leaves)
    def merge(leaves):
        if len(leaves)==1:return leaves[0]
        mid=len(leaves)//2;a=merge(leaves[:mid]);b=merge(leaves[mid:]);z=node('merge');arc(a,z);arc(b,z);return z
    dest=[merge([occ[(j,i)] for i,s in C]) for j,C in enumerate(clauses)]
    # Verify the graph constraints independently of the objective enumeration.
    deg=[0]*len(names);out=[0]*len(names)
    for a,b in E:deg[a]+=1;deg[b]+=1;out[a]+=1
    assert max(deg)<=3 and max(out)<=2 and max(map(len,parents))<=2
    assert parents[r]==[] and all(parents[v] for v in range(len(names)) if v!=r)
    indeg=list(map(len,parents));todo=[r];seen=[]
    for v in todo:
        seen.append(v)
        for a,b in E:
            if a==v:
                indeg[b]-=1
                if indeg[b]==0:todo.append(b)
    assert len(seen)==len(names)
    best=10**9;choices=0
    for selected in itertools.product(*(parents[v] for v in range(1,len(names)))):
        par=[None]+list(selected);total=0
        for j,target in enumerate(dest):
            costs={}
            for i,sign in clauses[j]:
                t,f=truth[i];costs[(t,var[i])]=int(not sign);costs[(f,var[i])]=int(sign)
            v=target;steps=0
            while v!=r:
                a=par[v];total+=costs.get((a,v),0);v=a;steps+=1;assert steps<=len(names)
        best=min(best,total);choices+=1
    want=min(sum(not any(bool(bits>>i&1)==sign for i,sign in C) for C in clauses) for bits in range(1<<k))
    assert best==want;return choices,len(names)
clauses=[]
for vals in itertools.product([0,1,2],repeat=2):
    C=[(i,v==1) for i,v in enumerate(vals) if v]
    if C:clauses.append(C)
cases=choices=0;maxn=0
for length in [1,2]:
    for cs in itertools.product(clauses,repeat=length):
        c,n=gadget(2,cs);choices+=c;maxn=max(maxn,n);cases+=1
for cs in [[[(0,True)],[(0,False)]],[[(0,True),(1,False),(2,True)],[(0,False),(1,True),(2,False)]]]:
    c,n=gadget(max(i for C in cs for i,s in C)+1,cs);choices+=c;cases+=1;maxn=max(maxn,n)
RESULTS=dict(formulas=cases,parent_choices=choices,max_graph_vertices=maxn,oracle='all truth assignments vs every parent choice on actual bounded-degree routing gadget',checks='DAG, all vertices reachable, indegree<=2, outdegree<=2, undirected degree<=3, actual path-specific 0/1 costs')
print(json.dumps(dict(status="PASS", **RESULTS), sort_keys=True))
