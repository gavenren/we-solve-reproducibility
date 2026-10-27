"""Independent supplements to /root/reviews_a's mathematical audit of group b.

Finite checks supplement the proofs in the audit records; they are not proofs
for continuous or unbounded model classes.
"""
from collections import deque
from itertools import product, combinations
from pathlib import Path
import cmath
import json
import math


def served_by_flow(generation, capacity):
    n = len(generation)
    source, sink = n, n + 1
    residual = [[0] * (n + 2) for _ in range(n + 2)]
    for t, g in enumerate(generation):
        residual[source][t] += g
        residual[t][sink] += 1
        nxt = (t + 1) % n
        if nxt != t:
            residual[t][nxt] += capacity
    total = 0
    while True:
        previous = [-1] * (n + 2)
        previous[source] = source
        queue = deque([source])
        while queue and previous[sink] < 0:
            u = queue.popleft()
            for v, available in enumerate(residual[u]):
                if available and previous[v] < 0:
                    previous[v] = u
                    queue.append(v)
        if previous[sink] < 0:
            return total
        amount = n + 1
        v = sink
        while v != source:
            u = previous[v]
            amount = min(amount, residual[u][v])
            v = u
        v = sink
        while v != source:
            u = previous[v]
            residual[u][v] -= amount
            residual[v][u] += amount
            v = u
        total += amount


def storage_checks():
    checked = feasible = 0
    for n in range(1, 8):
        subsets = []
        for mask in range(1 << n):
            members = [t for t in range(n) if mask >> t & 1]
            entering = sum(bool(mask >> t & 1) and
                           not bool(mask >> ((t - 1) % n) & 1)
                           for t in range(n))
            subsets.append((members, entering))
        for deficit in product((-1, 0, 1), repeat=n):
            cuts = [(sum(deficit[t] for t in members), entering)
                    for members, entering in subsets]
            backlog = [max([0] + [sum(deficit[(t - j) % n]
                                      for j in range(length))
                                  for length in range(1, n + 1)])
                       for t in range(n)]
            for energy in range(n + 1):
                exact_cut = max(value - energy * edges
                                for value, edges in cuts)
                actual_loss = n - served_by_flow([1 - d for d in deficit], energy)
                assert actual_loss == exact_cut
                criterion = sum(deficit) <= 0 and energy >= max(backlog)
                assert (actual_loss == 0) == criterion
                if criterion:
                    feasible += 1
                    for t in range(n):
                        assert backlog[t] == max(0, backlog[t - 1] + deficit[t])
                checked += 1
    assert checked == 24603
    return {"cases": checked, "zero_loss_cases": feasible,
            "exact_cut_vs_max_flow": "all matched",
            "source_zero_loss_criterion_and_recurrence": "all matched"}


def reservation_graph_checks():
    checked = []
    for cap in range(2, 9):
        count = 2 * cap
        graph = [set() for _ in range(count)]
        graph[0].add(1)
        graph[1].add(0)
        for i in (0, 1):
            path = [i] + list(range(2 + i * (cap - 1), 2 + (i + 1) * (cap - 1)))
            for u, v in zip(path, path[1:] + [i]):
                graph[u].add(v)
        cycles = []
        for start in range(count):
            def visit(path):
                for nxt in graph[path[-1]]:
                    if nxt == start:
                        cycles.append(tuple(path))
                    elif nxt > start and nxt not in path and len(path) < cap:
                        visit(path + [nxt])
            visit([start])
        assert sorted(map(len, cycles)) == sorted([2, cap, cap])
        best = 0
        for selected in product((False, True), repeat=len(cycles)):
            vertices = [v for c, yes in zip(cycles, selected) if yes for v in c]
            if len(set(vertices)) == len(vertices):
                best = max(best, len(vertices))
        assert best == 2 * cap
        assert all(0 in c or 1 in c for c in cycles)
        checked.append({"K": cap, "simple_cycles": len(cycles), "pooled": best,
                        "reserved": 2})
    return checked


def main():
    storage = storage_checks()
    graph = reservation_graph_checks()
    assert (1 - 1) == 0
    assert (3 - 1) + (3 - 5.5) == -0.5
    assert 2 * 0.8 + 3 * 0.8 - 5.5 == -1.5
    assert 2 * 1.2 + 3 * 1.2 - 5.5 == 0.5
    regrets = []
    intervals = [(0.4, 0.5), (0.3, 1)]
    for h in (0, 1):
        regrets.append(max(max(q) - q[h] for q in product(*intervals)))
    assert all(abs(x - y) < 1e-12 for x, y in zip(regrets, (0.6, 0.2)))
    loss_matrix = [[1, 0], [0.5, 1]]
    assert max(min(loss_matrix[a][q] for a in (0, 1)) for q in (0, 1)) == 0.5
    assert min(max(row) for row in loss_matrix) == 1
    rotation = []
    for omega in (1, 10, 100, 1000):
        a = 1
        lipschitz = math.hypot(a, omega)
        delay = math.atan(a / omega) / lipschitz
        residual = abs((a + 1j * omega) * cmath.exp(1j * lipschitz * delay)
                       - 1j * lipschitz)
        assert residual < 1e-9
        rotation.append({"omega": omega, "identity_residual": residual,
                         "threshold_ratio": delay * lipschitz ** 2 / a})
    output = {"storage": storage, "reservation_graph": graph,
              "drug_welfare_values": [0, -0.5], "drug_sharp_range": [-1.5, 0.5],
              "bureaucracy_exact_regrets": regrets,
              "nonrectangular_tipping_maxmin_minmax": [0.5, 1],
              "rotation": rotation}
    destination = Path(__file__).with_name('reviews_a_audit_b_results.json')
    destination.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output))


if __name__ == '__main__':
    main()
