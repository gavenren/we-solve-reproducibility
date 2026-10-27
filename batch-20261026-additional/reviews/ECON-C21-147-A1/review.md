# Exact capacity-sensitive refinement of the approximate version bound

Finding: **Supports the claim** within the finite, known-propensity intervention model. I checked the feasibility lemma, greedy extrema, invariance corollary, approximate-invariance proposition, known-kernel risk bound, and positivity example in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/d9/prb_d91ad5d6bd704bfca94b7c4c91253e2f/contributions/con_762f897b1b2b45d49b3f3274daac1ce8/files/C21-147.tex). Its contribution metadata calls this an unresolved exploration; the continuous learned-representation problem is not a theorem asserted here.

An independent calculation gives an exact refinement of the proposition bounding two version means by $2\delta$. It quantifies how that bound approaches zero when capacities nearly force a unique lift. Fix a covariate value, suppress its index, and write

$$
 \mathcal Q(c)=\{q\geq0:\ \sum_wq_w=1,\ q_w\leq c_w\},\qquad
 C=\sum_wc_w\geq1.
$$

For a subset $S\subseteq F$, put $c(S)=\sum_{w\in S}c_w$. The possible masses of $S$ are exactly

$$
 \max\{0,1-c(F\setminus S)\}\leq q(S)
 \leq\min\{1,c(S)\}.
$$

Necessity follows by adding capacities on either side. Sufficiency follows because any desired mass in this interval can be distributed within each side up to its capacities. This is the same elementary capacitated-simplex feasibility argument, applied separately to $S$ and its complement, including empty sides.

For finite probability vectors, total variation equals $\max_S(q(S)-q'(S))$. There are finitely many subsets and the polytope is compact, so the maximizations can be interchanged and attained. Consequently its exact total-variation diameter is

$$
 d(c)=\max_{S\subseteq F}
 \left[\min\{1,c(S)\}-\max\{0,1-c(F\setminus S)\}\right]
 =\max_S\min\{1,c(S),c(F\setminus S),C-1\}.
$$

The last equality follows by checking whether each side's capacity is below or above one. In particular, $d(c)\leq\min\{1,C-1\}$, and it is zero when $C=1$, consistently with the manuscript's saturated-capacity exception. A singleton fiber also has diameter zero regardless of its excess capacity.

Suppose now the manuscript's approximation condition holds: $m_w=r+e_w$, $ |e_w|\leq\delta$. Since $q-q'$ sums to zero,

$$
 |q\cdot m-q'\cdot m|
 =|(q-q')\cdot e|
 \leq\delta\|q-q'\|_1
 \leq2\delta d(c).
$$

This improves $2\delta$ to $2\delta d(c)$ without changing any causal assumptions. It is also the exact worst-case width over mean vectors satisfying that approximation restriction, whenever the outcome bound permits the two levels $r\pm\delta$. Choose a subset attaining the diameter and take $e=\delta$ on it and $-\delta$ off it. The two extremal subset-mass allocations then differ in their means by exactly $2\delta d(c)$. Across covariates, independence of the conditional choices gives the bound $2\delta\sum_x\pi_xd(c_x)$; the same construction at each covariate proves worst-case sharpness under compatible outcome bounds.

For example, with two capacities $0.55,0.55$, the feasible first coordinate is $[0.45,0.55]$, so $d(c)=0.10$. Conditional means $\delta,-\delta$ give a version range of width $0.20\delta$, attained by lifts $(0.55,0.45)$ and $(0.45,0.55)$. Thus approximate invariance and near saturation reinforce one another; applying $2\delta$ alone loses a factor ten in this example. This is a refinement, not a counterexample to the stated valid upper bound.

As another check on the sharp-range formula, its lower endpoint has the scalar dual representation

$$
 L=\max_{\lambda\in\mathbb R}
 \left[\lambda-\sum_wc_w(\lambda-m_w)_+\right].
$$

For every feasible lift, $q_w(m_w-\lambda)\geq-c_w(\lambda-m_w)_+$, giving the dual lower bound. Taking $\lambda$ equal to the manuscript's crossing mean makes the greedy allocation attain equality. This independently certifies optimality, including ties and a capacity crossing exactly at one.

The risk calculation also respects its statistical scope: $E\omega=1$ and $\omega^2\leq R\omega$ give the displayed $M^2R/N$ mean-squared-error bound only for a supplied kernel, or conditionally on independent training. The null-fiber example does not contradict it because its point-mass intervention violates absolute continuity. No validity for learned continuous fibers or additional novelty claim follows from these checks.
