#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact checks for the connected planar digraph obstruction family."""
import json
import sys

if not __debug__:
    raise SystemExit("Refusing -O: exact checks require assertions enabled.")


def example(f):
    assert isinstance(f, int) and f >= 1
    x = lambda i: 2 * i + 1
    y = lambda i: 2 * i + 2
    arcs = {(x(0), y(0)), (y(0), 0), (0, x(0))}
    super_edges = {tuple(sorted((u, v))) for u, v in arcs}
    faces = {frozenset((0, x(0), y(0)))}
    selected = next(iter(faces))

    def insert(vertex, face):
        assert face in faces and len(face) == 3
        faces.remove(face)
        for old in face:
            super_edges.add(tuple(sorted((vertex, old))))
        a, b, c = sorted(face)
        faces.update((frozenset((vertex, a, b)),
                      frozenset((vertex, b, c)),
                      frozenset((vertex, c, a))))

    for i in range(1, f):
        u, v = x(i - 1), y(i - 1)
        assert {u, v} <= selected
        insert(x(i), selected)
        insert(y(i), frozenset((u, v, x(i))))
        selected = frozenset((u, x(i), y(i)))
        assert selected in faces
        arcs.update(((u, x(i)), (v, x(i)), (x(i), y(i)),
                     (y(i), u), (y(i), v)))

    n = 2 * f + 1
    assert len(arcs) == 5 * f - 2
    assert all(u != v and (v, u) not in arcs for u, v in arcs)
    actual_edges = {tuple(sorted((u, v))) for u, v in arcs}
    assert actual_edges <= super_edges
    assert len(super_edges) == 3 * n - 6
    assert len(faces) == 2 * n - 5
    assert n - len(super_edges) + len(faces) + 1 == 2

    incoming, outgoing = [0] * n, [0] * n
    for u, v in arcs:
        incoming[v] |= 1 << u
        outgoing[u] |= 1 << v
    full = (1 << n) - 1
    for start in range(n):
        reached, frontier = 0, 1 << start
        while frontier:
            reached |= frontier
            follow = 0
            todo = frontier
            while todo:
                bit = todo & -todo
                todo ^= bit
                follow |= outgoing[bit.bit_length() - 1]
            frontier = follow & ~reached
        assert reached == full, (f, "not strongly connected")

    # Independent exhaustive DAG test: remove a source if one exists.
    # The property of the remainder has already been computed on a smaller mask.
    acyclic = bytearray(1 << n)
    acyclic[0] = 1
    maximum = 0
    optimum_mask = 0
    for mask in range(1, 1 << n):
        todo = mask
        while todo:
            bit = todo & -todo
            todo ^= bit
            vertex = bit.bit_length() - 1
            if not incoming[vertex] & mask:
                acyclic[mask] = acyclic[mask ^ bit]
                break
        if acyclic[mask] and mask.bit_count() > maximum:
            maximum, optimum_mask = mask.bit_count(), mask
    assert maximum == f + 1, (f, maximum)

    retained = 1
    for i in range(f):
        retained |= 1 << y(i)
    assert acyclic[retained] and retained.bit_count() == f + 1
    induced_arcs = {(u, v) for u, v in arcs
                    if retained & (1 << u) and retained & (1 << v)}
    path_arcs = {(y(0), 0)} | {(y(i), y(i - 1)) for i in range(1, f)}
    assert induced_arcs == path_arcs

    triangles = [frozenset((0, x(0), y(0)))]
    for i in range(1, f):
        triangles.extend((frozenset((x(i - 1), x(i), y(i))),
                          frozenset((y(i - 1), x(i), y(i)))))
    for triple in triangles:
        a, b, c = sorted(triple)
        assert ((a, b) in arcs and (b, c) in arcs and (c, a) in arcs
                or (a, c) in arcs and (c, b) in arcs and (b, a) in arcs)
    masks = [sum(1 << v for v in triple) for triple in triangles]
    minimum_hitting = min(mask.bit_count() for mask in range(1 << n)
                          if all(mask & triple for triple in masks))
    assert minimum_hitting == f
    if f >= 3:
        assert 5 * maximum < 3 * n
    return {"f": f, "vertices": n, "arcs": len(arcs),
            "vertex_subsets_examined": 1 << n,
            "maximum_induced_acyclic_size": maximum,
            "minimum_triangle_hitting_size": minimum_hitting,
            "strong_connectivity": True, "face_insertion_certificate": True,
            "optimal_acyclic_mask": optimum_mask}


def main():
    cases = [example(f) for f in range(1, 9)]
    print(json.dumps({"status": "PASS", "cases": cases,
                      "exhaustive_subsets_total": sum(c["vertex_subsets_examined"]
                                                     for c in cases),
                      "unbounded_family_proved_in_report": True,
                      "finite_checks_do_not_prove_unbounded_statement": True},
                     indent=2))


if __name__ == "__main__":
    main()
