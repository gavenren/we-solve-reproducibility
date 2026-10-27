"""Independent numerical spot checks; analytic proofs remain decisive.

Run from this batch directory: python3 checks/verify_a_checks.py
"""
import itertools
import json
import random
from math import comb
from pathlib import Path

rng = random.Random(2647)
results = {
    "seed": 2647,
    "H63_binomial": {
        "N": 100,
        "alpha": 0.05,
        "k2_lower_tail": sum(comb(100, j) * 0.05**j * 0.95**(100-j) for j in range(2)),
        "k3_lower_tail": sum(comb(100, j) * 0.05**j * 0.95**(100-j) for j in range(3)),
    },
}

max_error = 0.0
subsets_checked = 0
for _ in range(100):
    n = rng.randint(1, 6)
    capacities = [rng.uniform(0.01, 1.5) for _ in range(n)]
    if sum(capacities) < 1:
        capacities[0] += 1-sum(capacities)
    vertices = []
    for free in range(n):
        fixed = [i for i in range(n) if i != free]
        for bits in itertools.product((0, 1), repeat=n-1):
            q = [0.0] * n
            for i, bit in zip(fixed, bits):
                q[i] = capacities[i] * bit
            q[free] = 1-sum(q)
            if -1e-10 <= q[free] <= capacities[free]+1e-10:
                vertices.append(q)
    for bits in itertools.product((0, 1), repeat=n):
        left = sum(c for c, bit in zip(capacities, bits) if bit)
        right = sum(c for c, bit in zip(capacities, bits) if not bit)
        predicted = min(1.0, left, right, sum(capacities)-1)
        masses = [sum(qi*bit for qi, bit in zip(q, bits)) for q in vertices]
        max_error = max(max_error, abs(max(masses)-min(masses)-predicted))
        subsets_checked += 1
results["C21_vertex_check"] = {
    "polytopes": 100,
    "subsets_checked": subsets_checked,
    "maximum_absolute_error": max_error,
}

max_residual = 0.0
all_implementable = True
max_grid_advantage = 0.0
for _ in range(100):
    d = rng.uniform(0.1, 2)
    c = rng.uniform(0.001, d)
    D = rng.uniform(d, 3*d)
    mu = rng.uniform(0, D)
    eta = rng.uniform(0.001, 2)
    determinant = D*eta+mu*(D-mu)
    threshold = determinant/(D-mu+eta)
    if c <= threshold:
        a = c*(D-mu)/determinant
        b = 1-c*(D-mu+eta)/determinant
    else:
        a = (D-mu)/(D-mu+eta)
        b = 0
    shortfall_cutoff = 1-a-b
    derivative_a = -(D-mu)*shortfall_cutoff+eta*a
    derivative_b = c-D*shortfall_cutoff-mu*a
    max_residual = max(
        max_residual,
        abs(derivative_a),
        abs(derivative_b) if b > 1e-12 else max(0, -derivative_b),
    )
    all_implementable &= b+1e-12 >= max(0, 1-a-c/d)

    def objective(capacity, buffer):
        tail = max(0, 1-buffer-capacity)**2
        return (c*buffer+D*tail/2
                +mu*((1-buffer)**2-tail)/2+eta*capacity*capacity/2)

    proposed_value = objective(a, b)
    for i in range(31):
        for j in range(31):
            max_grid_advantage = max(
                max_grid_advantage, proposed_value-objective(i/30, j/30))
results["E58_supervised_check"] = {
    "parameter_cases": 100,
    "maximum_KKT_residual": max_residual,
    "all_implementable": all_implementable,
    "grid_dimensions": [31, 31],
    "largest_grid_advantage_over_formula": max_grid_advantage,
}

target = Path(__file__).with_name("verify_a_results.json")
target.write_text(json.dumps(results, indent=2)+"\n")
print(json.dumps(results, indent=2))
