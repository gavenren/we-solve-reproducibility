"""Exhaustively compare stability, serial outcomes and frontier optimization.

All 26 possible acceptable weak-order rows on three named partners are
combined for three agents. Partner priorities are the common strict order.
This is a finite independent check, not an asymptotic proof.
"""
from itertools import product
import json

N = 3

def rows():
    answer = []
    for mask in range(1 << N):
        neighbors = [w for w in range(N) if mask >> w & 1]
        if not neighbors:
            answer.append({})
            continue
        for ranks in product(range(len(neighbors)), repeat=len(neighbors)):
            if set(ranks) == set(range(max(ranks) + 1)):
                answer.append(dict(zip(neighbors, ranks)))
    return answer

def matchings(preferences, i=0, used=frozenset(), prefix=()):
    if i == N:
        yield prefix
        return
    yield from matchings(preferences, i+1, used, prefix+(-1,))
    for w in preferences[i]:
        if w not in used:
            yield from matchings(preferences, i+1, used | {w}, prefix+(w,))

def stable(preferences, matching):
    owner = {w:i for i,w in enumerate(matching) if w >= 0}
    for i, row in enumerate(preferences):
        current = row[matching[i]] if matching[i] >= 0 else N+1
        if any(rank < current and i < owner.get(w, N)
               for w,rank in row.items()):
            return False
    return True

def serial(preferences, i=0, used=frozenset(), prefix=()):
    if i == N:
        yield prefix
        return
    available = {w:r for w,r in preferences[i].items() if w not in used}
    if not available:
        yield from serial(preferences, i+1, used, prefix+(-1,))
    else:
        rank = min(available.values())
        for w,r in available.items():
            if r == rank:
                yield from serial(preferences, i+1, used | {w}, prefix+(w,))

def reward(i,w):
    return (i+2)*(w+1)-5

def objective(matching):
    return (sum(w >= 0 for w in matching),
            sum(reward(i,w) for i,w in enumerate(matching) if w >= 0))

def frontier(preferences):
    first = {w:min(i for i in range(N) if w in preferences[i])
             for w in range(N) if any(w in row for row in preferences)}
    last = {w:max(i for i in range(N) if w in preferences[i]) for w in first}
    labels = {frozenset():(0,0)}
    for i in range(N):
        after = {w for w in first if first[w] <= i < last[w]}
        next_labels = {}
        for used,label in labels.items():
            available = {w:r for w,r in preferences[i].items() if w not in used}
            if not available:
                options = [-1]
            else:
                best = min(available.values())
                options = [w for w,r in available.items() if r == best]
            for w in options:
                state = frozenset((used | ({w} if w >= 0 else set())) & after)
                increment = (1,reward(i,w)) if w >= 0 else (0,0)
                value = tuple(a+b for a,b in zip(label,increment))
                next_labels[state] = max(next_labels.get(state,(-1,-10**9)),value)
        labels = next_labels
    return labels[frozenset()]

def main():
    choices = rows()
    assert len(choices) == 26
    tested = 0
    unstable_greedy_gap = 0
    for preferences in product(choices, repeat=N):
        actual = {m for m in matchings(preferences) if stable(preferences,m)}
        generated = set(serial(preferences))
        assert actual == generated, (preferences,actual,generated)
        assert frontier(preferences) == max(map(objective,actual))
        unstable_greedy_gap = max(unstable_greedy_gap,
            max(sum(w>=0 for w in m) for m in actual)
            - min(sum(w>=0 for w in m) for m in actual))
        tested += 1
    print(json.dumps({'instances':tested,'row_types':len(choices),
        'serial_set_mismatches':0,'frontier_objective_mismatches':0,
        'largest_stable_cardinality_gap':unstable_greedy_gap},indent=2))

if __name__ == '__main__':
    main()
