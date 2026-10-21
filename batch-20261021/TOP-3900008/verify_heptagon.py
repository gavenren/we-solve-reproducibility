#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact reproduction of Kreisel--Kurz Figure1, not their diameter search."""
import sys
if not __debug__:
    raise SystemExit("Refusing -O: exact certificate assertions must remain enabled.")
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt
import json

D = 2002
POINTS = [
    (Q(0), Q(0)), (Q(22270), Q(0)),
    (Q(26127018,2227), Q(932064,2227)),
    (Q(245363,17), Q(3144,17)),
    (Q(17615968,2227), Q(238464,2227)),
    (Q(56068,17), Q(3144,17)),
    (Q(19079044,2227), -Q(54168,2227)),
]
DISTANCES = [
 [0,22270,22098,16637,9248,8908,8636],
 [22270,0,21488,11397,15138,20698,13746],
 [22098,21488,0,10795,14450,13430,20066],
 [16637,11397,10795,0,7395,11135,11049],
 [9248,15138,14450,7395,0,5780,5916],
 [8908,20698,13430,11135,5780,0,10744],
 [8636,13746,20066,11049,5916,10744,0],
]

def det(a):
    a = [list(map(Q,row)) for row in a]
    out = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j,len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j],a[pivot] = a[pivot],a[j]
            out = -out
        z = a[j][j]
        out *= z
        for i in range(j+1,len(a)):
            f = a[i][j]/z
            for k in range(j+1,len(a)):
                a[i][k] -= f*a[j][k]
    return out

def main():
    squared = []
    for i,j in combinations(range(7),2):
        x,y = POINTS[i]
        u,v = POINTS[j]
        z = (x-u)**2+D*(y-v)**2
        assert z.denominator == 1
        r = isqrt(z.numerator)
        assert r*r == z and r == DISTANCES[i][j] > 0
        squared.append(r*r)
    areas = [det([[POINTS[i][0],POINTS[i][1],1] for i in c])
             for c in combinations(range(7),3)]
    circles = [det([[POINTS[i][0]**2+D*POINTS[i][1]**2,
                    POINTS[i][0],POINTS[i][1],1] for i in c])
               for c in combinations(range(7),4)]
    assert all(areas) and all(circles)
    print(json.dumps({
        "status":"PASS", "rational_y_coefficient_of_sqrt":D,
        "distance_equalities":len(squared),
        "noncollinearity_determinants":len(areas),
        "nonconcyclicity_determinants":len(circles),
        "diameter":isqrt(max(squared)),
        "scope":"This exact seven-point certificate only; no minimum-diameter enumeration."
    },indent=2))

if __name__ == "__main__":
    main()
