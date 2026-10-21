# SPDX-License-Identifier: Apache-2.0
"""Check the published odd-Mycielski line-graph orientation, independently."""
import hashlib
import json
import sys
from collections import deque
from pathlib import Path

if not __debug__:
    raise RuntimeError("Run without -O: verification checks must remain enabled")


def construction(m):
    assert m >= 3 and m % 2 == 1
    edges = []
    labels = []
    for j in range(1, m + 1):
        for i in [0] + [t for t in range(1, m + 1)
                         if (t - j) % m in (1, m - 1)]:
            edges.append(frozenset([("w", 0) if i == 0 else ("v", i),
                                    ("u", j)]))
            labels.append(("a", i, j))
    for i in range(1, m):
        edges.append(frozenset([("v", i), ("v", i + 1)]))
        labels.append(("c", i))
    edges.append(frozenset([("v", 1), ("v", m)]))
    labels.append(("c", m))
    assert len(edges) == len(set(edges)) == 4 * m
    undirected = set()
    arcs = set()
    for x in range(len(edges)):
        for y in range(x + 1, len(edges)):
            if not edges[x] & edges[y]:
                continue
            undirected.add((x, y))
            a, b = labels[x], labels[y]
            if a[0] == b[0] == "a":
                if a[1] == b[1]:
                    forward = a[2] < b[2]
                else:
                    assert a[2] == b[2]
                    forward = a[1] > b[1]
            elif a[0] == b[0] == "c":
                ca, cb = a[1], b[1]
                if {ca, cb} == {1, m}:
                    forward = ca == m
                elif {ca, cb} == {m - 1, m}:
                    forward = ca == m - 1
                else:
                    assert abs(ca - cb) == 1
                    forward = ca > cb
            else:
                forward = a[0] == "a"
            arcs.add((x, y) if forward else (y, x))
    assert len(undirected) == 9 * m + m * (m - 1) // 2
    return edges, labels, undirected, arcs


def check(n, undirected, arcs):
    assert len(arcs) == len(undirected)
    assert {tuple(sorted(e)) for e in arcs} == undirected
    out = [0] * n
    indeg = [0] * n
    for x, y in arcs:
        assert x != y
        out[x] |= 1 << y
        indeg[y] += 1
    queue = deque(x for x in range(n) if indeg[x] == 0)
    topo = []
    while queue:
        x = queue.popleft()
        topo.append(x)
        bits = out[x]
        while bits:
            low = bits & -bits
            y = low.bit_length() - 1
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
            bits ^= low
    if len(topo) != n:
        return False, {"reason": "directed_cycle"}
    reach = out.copy()
    for x in reversed(topo):
        bits = out[x]
        while bits:
            low = bits & -bits
            y = low.bit_length() - 1
            reach[x] |= reach[y]
            bits ^= low
    ancestors = [0] * n
    for x in range(n):
        bits = reach[x]
        while bits:
            low = bits & -bits
            y = low.bit_length() - 1
            ancestors[y] |= 1 << x
            bits ^= low
    intervals = 0
    for u, v in sorted(arcs):
        interval = (reach[u] | (1 << u)) & (ancestors[v] | (1 << v))
        bits = interval
        while bits:
            low = bits & -bits
            x = low.bit_length() - 1
            missing = reach[x] & interval & ~out[x]
            if missing:
                y = (missing & -missing).bit_length() - 1
                return False, {"reason": "shortcut", "arc": [u, v],
                               "comparable_nonedge": [x, y]}
            bits ^= low
            intervals += 1
    return True, {"arc_intervals_checked": intervals}


def main():
    rows = []
    total_intervals = 0
    for m in range(5, 102, 2):
        edges, labels, undirected, arcs = construction(m)
        ok, detail = check(len(edges), undirected, arcs)
        assert ok, (m, detail)
        total_intervals += detail["arc_intervals_checked"]
        rows.append({"odd_cycle_order": m, "root_vertices": 2 * m + 1,
                     "root_edges_line_vertices": len(edges),
                     "line_edges": len(undirected), **detail})
    edges, labels, undirected, arcs = construction(3)
    ok, rejection = check(len(edges), undirected, arcs)
    assert not ok, "The excluded triangle base must reject this orientation"
    assert rejection["reason"] == "shortcut"
    output = {"status": "PASS", "method": "exact integer bitset reachability",
              "positive_cases": len(rows), "odd_cycle_orders": [5, 101],
              "arc_intervals_checked": total_intervals,
              "negative_control_cycle_order_3": rejection, "cases": rows}
    here = Path(__file__).resolve().parent
    (here / "verification.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k != "cases"},
                     sort_keys=True))


if __name__ == "__main__":
    main()
