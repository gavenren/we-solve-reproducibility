"""Finite exact check including neutral sender types and unused messages.

Equal full-support priors, Delta_R in {-2,-1,0,1,2}, sender signs in
{-1,0,1}, up to three states. Enumerate deterministic sender strategies
against three receiver-message responses in {0,1/2,1}. The proof in the
review, rather than this finite enumeration, covers arbitrary mixing.
"""
from itertools import product, combinations_with_replacement
import json

count=0
for n in range(1,4):
    for signs in product((-1,0,1),repeat=n):
        for deltas in product(range(-2,3),repeat=n):
            dp=sum(d for s,d in zip(signs,deltas) if s==1)
            dm=sum(d for s,d in zip(signs,deltas) if s==-1)
            pz=sum(max(d,0) for s,d in zip(signs,deltas) if s==0)
            nz=sum(min(d,0) for s,d in zip(signs,deltas) if s==0)
            a,b=dp+pz,dm+nz
            predicted=2*(a if a>=0 and b<=0 else max(0,sum(deltas)))
            optimum=None
            for responses in combinations_with_replacement(range(3),3):
                if any((x==0 and min(deltas)>0) or
                       (x==2 and max(deltas)<0) or
                       (x==1 and not(min(deltas)<=0<=max(deltas)))
                       for x in responses):
                    continue
                allowed=[]
                for s in signs:
                    target=max(responses) if s==1 else min(responses)
                    allowed.append([i for i,x in enumerate(responses) if s==0 or x==target])
                for messages in product(*allowed):
                    differences=[sum(deltas[i] for i in range(n) if messages[i]==j)
                                 for j in range(3)]
                    used=set(messages)
                    if any((responses[j]==0 and differences[j]>0) or
                           (responses[j]==2 and differences[j]<0) or
                           (responses[j]==1 and differences[j]!=0) for j in used):
                        continue
                    value=sum(deltas[i]*responses[messages[i]] for i in range(n))
                    optimum=value if optimum is None else max(optimum,value)
            assert optimum==predicted,(signs,deltas,predicted,optimum)
            count+=1
print(json.dumps({'profiles_checked':count,'all_exact_checks_passed':True},indent=2))
