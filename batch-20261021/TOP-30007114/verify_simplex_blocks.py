#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite part of the optimal-simplex-block rate certificate.

The analytic tail proof is in report.md, not replaced by finite enumeration.
"""
import json
import sys
from fractions import Fraction
from math import comb, factorial

if not __debug__:
    raise SystemExit("Refusing -O: exact assertions must be enabled.")

def c(n):
    return Fraction((n + 1) * n ** n, factorial(n))

winner = 13
peak = c(winner)
strict_comparisons = 0
for n in range(1, 1000):
    if n == winner:
        continue
    assert c(n) ** winner < peak ** n, n
    strict_comparisons += 1

# These exact rational certificates close the infinite tail in the proof.
assert comb(1000, 6) > 1001 * 100 ** 6
tail_rate = Fraction(11, 4) * Fraction(101, 100)
assert tail_rate ** 10 < c(10)
assert c(10) ** 13 < peak ** 10

# Independently optimize all partitions through dimension80 using a recurrence,
# including interval factors, then compare their products to the rate bound.
best = [Fraction(1)]
partitions = [()]
for n in range(1, 81):
    value, parts = max(
        (best[n - j] * c(j), partitions[n - j] + (j,))
        for j in range(1, n + 1)
    )
    best.append(value)
    partitions.append(parts)
    assert value ** winner <= peak ** n
    assert sum(parts) == n
    product = Fraction(1)
    for j in parts:
        product *= c(j)
    assert product == value
for q in range(1, 7):
    assert best[13 * q] == peak ** q
    assert partitions[13 * q] == (13,) * q

print(json.dumps({
    "status": "PASS", "strict_block_rate_comparisons": strict_comparisons,
    "unique_best_block_dimension_below1000": winner,
    "tail_rational_certificates": 3,
    "partition_dynamic_program_dimensions": 80,
    "scope": "Exact finite comparisons and rational tail constants; report supplies the infinite tail argument and geometric product formula."
}, sort_keys=True))
