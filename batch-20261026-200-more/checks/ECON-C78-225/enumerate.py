# SPDX-License-Identifier: Apache-2.0
"""Exact serial-DA state enumeration; only n=3 is certified here."""
import itertools, json, collections

def states(plists, rlists):
    n=len(plists)
    ranks=[{p:i for i,p in enumerate(r)} for r in rlists]
    seen={(0,)*n}; todo=list(seen)
    while todo:
        q=todo.pop(); held=[None]*n
        for p in range(n):
            for r in plists[p][:q[p]]:
                if held[r] is None or ranks[r][p]<ranks[r][held[r]]:
                    held[r]=p
        for p in range(n):
            if p not in held and q[p]<n:
                nq=list(q); nq[p]+=1; nq=tuple(nq)
                if nq not in seen:seen.add(nq);todo.append(nq)
    return seen

ps=list(itertools.permutations(range(3)))
hist=collections.Counter(); maximum=0; witness=None; witness_states=None
for rest in itertools.product(ps,repeat=2):
    plists=(ps[0],)+rest
    for rlists in itertools.product(ps,repeat=3):
        ss=states(plists,rlists);hist[len(ss)]+=1
        if len(ss)>maximum:
            maximum=len(ss);witness=(plists,rlists);witness_states=ss
assert sum(hist.values())==7776
assert maximum==15
out={'n':3,'canonical_profiles':sum(hist.values()),'maximum':maximum,'histogram':dict(sorted(hist.items())),
     'witness_proposer_lists':witness[0],'witness_receiver_lists':witness[1],
     'witness_states':sorted(witness_states),'witness_support_counts':dict(sorted(collections.Counter(sum(v>0 for v in q) for q in witness_states).items()))}
print(json.dumps(out,indent=2))
