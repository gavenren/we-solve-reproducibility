# Robust intervention beyond the two-depositor and bounded-coordination cases

The source's “An exactly solvable policy problem” restricts coordination λ to [0,1] and uses two depositors. Its threshold is correct there. The following extension characterizes what changes when coordination is stronger and shows which conclusions survive an arbitrary depositor count.

Take any N≥2 equal depositors with common z uniform on [0,1]. Their withdrawal advantages are z−u+[λ/(N−1)]∑_{j≠i}w_j, with λ≥0 arbitrary and u∈[0,1+λ]. Define a run by any fixed positive threshold number of withdrawals, from one through N. There are no partially withdrawing pure equilibria, except irrelevant zero-probability ties. Indeed, in a profile with k∈{1,…,N−1} withdrawals, a withdrawing depositor requires z−u+λ(k−1)/(N−1)>0, whereas a waiting depositor requires z−u+λk/(N−1)<0. The latter expression is at least the former, a contradiction. This also handles λ=0 away from ties.

Consequently the least and greatest pure-equilibrium run probabilities are 1−F(u) and 1−F(u−λ), exactly as for two depositors, for every such declared run threshold. This statement concerns the pure-selector class; heterogeneous shocks and mixed equilibria are outside it.

With real loss H>0 and policy cost cu²/2, c>0, put x=H/c. For 0≤λ≤1, retain the manuscript's threshold: u=0 when x<2λ; u=min(x,1+λ) when x>2λ; and, if λ>0, precisely u=0 and u=2λ at equality. When λ=0 the unique minimizer is min(x,1).

For λ>1 a different regime appears. Define t=(1+λ)²/2. The exact robust minimizers are u=0 if x<t, u=1+λ if x>t, and precisely these two endpoints when x=t. In particular, an interior intervention is never globally optimal in this strong-coordination regime.

To prove the new case, divide expected loss by c. On [0,λ], the greatest-equilibrium run probability remains one, so the unique best point is zero with loss x. On [λ,1+λ], the normalized loss is u²/2+x(1+λ−u), strictly convex. If x≤λ, its constrained minimizer is λ, which costs λ²/2 more than zero. If λ<x<1+λ, its minimizer is x and its excess over zero is x(λ−x/2)>0 because x<1+λ<2λ. For x≥1+λ its minimizer is 1+λ, with excess (1+λ)²/2−x=t−x. Since λ>1 gives t>1+λ, these alternatives yield exactly the stated threshold and two-point tie. Strict convexity and the first interval's strict cost increase exclude other minimizers.

At λ=1 the formulas meet: t=2=2λ=1+λ. The intervention jump therefore reaches complete worst-selector run prevention once coordination exceeds one. This conclusion is conditional on uniform fundamentals, common symmetric interactions, selector ambiguity and the quadratic real-cost technology. It is not a prescription for actual insurance or facilities; it identifies a structural regime omitted by the source's deliberately bounded λ subclass.

Source: [ECON-G21-262-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/99/prb_999cdf7d31c847df9b301a3374495a76/contributions/con_e4c4e2f69dcf43cb9afda09ddd19f026/files/G21-262.tex), canonical revision `rev_b9d8ada79ed3420c81ebc07b4637c098`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
