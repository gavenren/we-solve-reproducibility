# Dual certificates and a scalar inner solver for compensation

The manuscript's minimum-budget theorem is correct. Its subgradient multipliers also yield an exact dual representation and a practical reduction of the inner optimization to one scalar. This provides global budget certificates and interprets which workers' losses constrain the policy.

Retain all primitives in “Workers, training and fiscal costs.” For \(\lambda\in[0,1]^N\), put \(D_\lambda=\sum_i\lambda_id_i\), \(X=\sum_ix_i\), and
\[
L(x,\lambda)=
\sum_i\lambda_i\ell_i+
\sum_i\{(k_i-\lambda_ia_i)x_i+\lambda_ib_ix_i^2/2\}
+D_\lambda X^2/2.
\tag{A}
\]
Then the exact minimum compensation budget satisfies
\[
B^*=\max_{\lambda\in[0,1]^N}\min_{x\in[0,1]^N}L(x,\lambda).
\tag{B}
\]
Indeed \([z]_+=\max_{0\le\lambda\le1}\lambda z\), so the source objective is \(\max_\lambda L(x,\lambda)\). The box domains are compact and convex; \(L\) is continuous, convex in \(x\), and affine in \(\lambda\). The finite convex epigraph program described in the source has strict feasibility and its Lagrange multipliers on transfer constraints sum to one. Its strong duality therefore gives (B). Equivalently, the convex-concave minimax theorem applies directly to (A).

This formula is constructive. At any fixed \(\lambda\), every coordinate with \(\lambda_i=0\) is zero at an inner minimum: its derivative is \(k_i+D_\lambda X>0\). For the other coordinates, define
\[
x_i(X)=\left[
\frac{\lambda_i a_i-k_i-D_\lambda X}{\lambda_i b_i}
\right]_0^1.
\]
The aggregate \(X_\lambda\) is the unique solution of
\[
X_\lambda=\sum_{\lambda_i>0}x_i(X_\lambda)
\quad\text{on }[0,N].
\tag{C}
\]
To check existence, subtract the right side from \(X\). The resulting continuous function is nonpositive at zero, nonnegative at \(N\), and strictly increasing: its first term strictly increases while every subtracted term is nonincreasing. Hence it has exactly one zero. At that zero, the displayed clipped coordinates satisfy precisely the box first-order conditions for the convex inner problem. They therefore minimize it. If all \(\lambda_i\) vanish, (C) reads \(X=0\), correctly returning no training. If \(D_\lambda=0\), the formula reduces to independent clipped choices.

Any candidate \(\lambda\) now supplies a rigorous lower bound \(L(x(X_\lambda),\lambda)\) on the required budget. Conversely any training vector supplies the primal upper bound
\[
\sum_i k_ix_i+\sum_i[\ell_i-g_i(x)]_+.
\]
Equality certifies global optimality without inspecting every competing policy. This is useful when an approximate policy is proposed: the difference between the two bounds is a genuine optimality gap.

There is also an exact sensitivity interpretation. With other primitives fixed, (B) expresses \(B^*(\ell)\) as a supremum of affine functions of the loss vector \(\ell\). Hence it is convex and coordinatewise nondecreasing. If \(\lambda^*\) is a dual optimum at \(\ell\), then for any other nonnegative loss vector \(\ell'\),
\[
B^*(\ell')\ge B^*(\ell)+\lambda^{*T}(\ell'-\ell).
\]
The multiplier is a subgradient of the compensation frontier. Since \(0\le\lambda_i\le1\), one also has
\[
|B^*(\ell')-B^*(\ell)|\le\sum_i|\ell_i'-\ell_i|.
\]
Thus the model's optimal budget cannot move by more than the total absolute revision to measured losses. This bound remains valid at kinks where a worker first becomes exactly compensated.

This is a restricted optimization and sensitivity extension. It retains observable losses, enforceable divisible training, nonnegative transfers and the specified quadratic congestion. It does not add private information, identify spillovers from small experiments, or replace the source's distinction between a Pareto compensation floor and weighted welfare.

Source: [ECON-F16-277-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f9/prb_f9bbb55e38af4843ba0f39c8f23b83d0/contributions/con_99b2c25f233e451aa7d25949b4d1edda/files/F16-277.tex), canonical revision `rev_f72c2ca4919346cf88ad9d30ed14dd7c`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
