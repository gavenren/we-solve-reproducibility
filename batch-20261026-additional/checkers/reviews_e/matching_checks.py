"""Independent finite checks for the assigned matching manuscripts."""
from itertools import permutations, product
from random import Random
import json

def partial_matchings(adj):
    n = len(adj)
    def rec(left, pairs):
        if not left:
            m = [-1]*n
            for i,j in pairs:
                m[i]=j; m[j]=i
            yield tuple(m)
            return
        i = min(left)
        yield from rec(left-{i}, pairs)
        for j in adj[i] & left:
            yield from rec(left-{i,j}, pairs+[(i,j)])
    return list(rec(set(range(n)), []))

def stable_roommates(m, ranks):
    return all(not (ranks[i][j] < ranks[i].get(m[i], 999)
                    and ranks[j][i] < ranks[j].get(m[j], 999))
               for i in range(len(m)) for j in ranks[i] if i<j and m[i]!=j)

def cycle_formula(adj, ranks):
    alive=set(range(len(adj)))
    while True:
        tops={i:min(adj[i]&alive, key=ranks[i].get) for i in alive if adj[i]&alive}
        mutual=[(i,j) for i,j in tops.items() if i<j and tops.get(j)==i]
        if not mutual:
            break
        for i,j in mutual:
            alive.discard(i); alive.discard(j)
    alive={i for i in alive if adj[i]&alive}
    sizes=[]
    while alive:
        stack=[min(alive)]; comp=set()
        while stack:
            i=stack.pop()
            if i in comp: continue
            comp.add(i); stack.extend((adj[i]&alive)-comp)
        alive-=comp
        sizes.append(len(comp))
    if any(s%2 for s in sizes): return None
    return max([0]+[s//2-1 for s in sizes])

def degree_two_check():
    total=0
    for n in range(1,11):
        for cyc in (False, True):
            if cyc and n<3: continue
            adj=[set() for _ in range(n)]
            for i in range(n-1): adj[i].add(i+1); adj[i+1].add(i)
            if cyc: adj[0].add(n-1); adj[n-1].add(0)
            variable=[i for i in range(n) if len(adj[i])==2]
            matches=partial_matchings(adj)
            for choices in product((0,1),repeat=len(variable)):
                flip=dict(zip(variable,choices))
                ranks=[]
                for i in range(n):
                    order=sorted(adj[i],reverse=bool(flip.get(i,0)))
                    ranks.append({j:k for k,j in enumerate(order)})
                stable=[m for m in matches if stable_roommates(m,ranks)]
                predicted=cycle_formula(adj,ranks)
                if not stable:
                    assert predicted is None
                else:
                    assert predicted is not None
                    sets=[frozenset((i,j) for i,j in enumerate(m) if i<j) for m in stable]
                    fixed=set.intersection(*(set(q) for q in sets))
                    for q in sets:
                        budget=max([0]+[min(len(q-r)-1 for r in sets if e not in r)
                                        for e in q-fixed])
                        assert budget==predicted, (n,cyc,ranks,q,budget,predicted)
                total+=1
    return total

def stable_marriage(m,wr,fr):
    n=len(m); inv=[m.index(f) for f in range(n)]
    return all(not(wr[w][f]<wr[w][m[w]] and fr[f][w]<fr[f][inv[f]])
               for w in range(n) for f in range(n) if f!=m[w])

def lattice_check():
    rng=Random(217); n=4; orders=list(permutations(range(n)))
    profiles=0; changes=0; witness=None
    for _ in range(30000):
        wp=[rng.sample(range(n),n) for _ in range(n)]
        fp=[rng.sample(range(n),n) for _ in range(n)]
        wr=[{x:i for i,x in enumerate(p)} for p in wp]
        fr=[{x:i for i,x in enumerate(p)} for p in fp]
        stable=[m for m in orders if stable_marriage(m,wr,fr)]
        if len(stable)<2: continue
        profiles+=1
        for w,f,iw,iff in product(range(n),range(n),range(n-1),range(n-1)):
            a,b=wp[w][iw:iw+2]; c,d=fp[f][iff:iff+2]
            if f in (a,b) or w in (c,d): continue
            wp2=[p[:] for p in wp]; fp2=[p[:] for p in fp]
            wp2[w][iw],wp2[w][iw+1]=b,a
            fp2[f][iff],fp2[f][iff+1]=d,c
            wr2=[{x:i for i,x in enumerate(p)} for p in wp2]
            fr2=[{x:i for i,x in enumerate(p)} for p in fp2]
            discarded={m for m in stable if not stable_marriage(m,wr2,fr2)}
            I={m for m in stable if m[w]==a and fr[b][w]<fr[b][m.index(b)]}
            J={m for m in stable if m.index(f)==c and wr[d][f]<wr[d][m[d]]}
            assert discarded==I|J
            def meet(x,y): return tuple(min((x[k],y[k]),key=wr[k].get) for k in range(n))
            def join(x,y): return tuple(max((x[k],y[k]),key=wr[k].get) for k in range(n))
            if I and J:
                lowerI=next(m for m in I if all(meet(m,x)==m for x in I))
                lowerJ=next(m for m in J if all(meet(m,x)==m for x in J))
                upperI=next(m for m in I if all(join(m,x)==m for x in I))
                upperJ=next(m for m in J if all(join(m,x)==m for x in J))
                meetclosed=all(meet(x,y) in discarded for x in discarded for y in discarded)
                joinclosed=all(join(x,y) in discarded for x in discarded for y in discarded)
                assert meetclosed == (meet(lowerI,lowerJ) in (lowerI,lowerJ))
                assert joinclosed == (join(upperI,upperJ) in (upperI,upperJ))
                if not meetclosed and not joinclosed:
                    witness={'worker_preferences':wp,'firm_preferences':fp,
                             'changed_worker':w,'worker_swap':[a,b],
                             'changed_firm':f,'firm_swap':[c,d],
                             'stable_matchings':stable,'I':list(I),'J':list(J)}
            changes+=1
        if witness and profiles>=300: break
    return {'profiles':profiles,'changes':changes,'witness':witness}

if __name__=='__main__':
    print(json.dumps({'degree_two_instances':degree_two_check(),
                      'lattice':lattice_check()},indent=2))
