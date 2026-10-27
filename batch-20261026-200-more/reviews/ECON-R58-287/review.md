# Exact minimax-regret subsidy under the spatial welfare interval

The sharp observational interval in the manuscript identifies an entire family of national welfare curves, not merely a separate interval at one subsidy. This makes it possible to solve a decision problem under the remaining uncertainty. In the strictly concave case, minimax regret has a closed form that handles constrained policy endpoints.

Retain the source's observations and restrictions, and assume
\[
K=(H-g)/H^2+a>0,\qquad S=\bar s.
\]
Let \(\beta=gn_0-\gamma_2\). The sharp interval for \(\gamma_2\) implies the sharp common-parameter family
\[
\beta\in[\beta_L,\beta_U]=[gn_0-U,gn_0-L],\qquad
W_\beta(s)=\beta s/H-Ks^2/2,\quad0\le s\le S.
\tag{A}
\]
The same value of \(\beta\) governs the entire curve. Allowing it to vary independently with each policy would be a different uncertainty model.

If \(\beta\) were known, its unique oracle policy and value would be
\[
s_\beta=\left[\frac{\beta}{HK}\right]_0^S,\qquad
M(\beta)=W_\beta(s_\beta).
\]
For a chosen policy \(s\), define regret \(R_\beta(s)=M(\beta)-W_\beta(s)\). Suppose first that \(\beta_L<\beta_U\). The exact minimax-regret subsidy is
\[
s^{MR}=
\frac{H\{M(\beta_U)-M(\beta_L)\}}{\beta_U-\beta_L}.
\tag{B}
\]
In particular no additional clipping is needed in this formula.

Here is a proof including the boundary cases. The value \(M(\beta)\) is a supremum of affine functions of \(\beta\), hence convex. Therefore, for fixed \(s\), regret is convex in \(\beta\), and its maximum over the interval occurs at one of its endpoints. Write these two regret functions as \(R_L,R_U\). Their difference is
\[
R_U(s)-R_L(s)=M(\beta_U)-M(\beta_L)
-(\beta_U-\beta_L)s/H.
\tag{C}
\]
They cross exactly at the value in (B).

The oracle map \(s_\beta\) is continuous and nondecreasing, and direct differentiation of its three regimes gives \(M'(\beta)=s_\beta/H\), including the joining thresholds. Integrating this derivative shows
\[
s_{\beta_L}\le s^{MR}\le s_{\beta_U}.
\]
Both oracle policies lie in \([0,S]\), proving feasibility of (B). For \(s<s^{MR}\), equation (C) makes \(R_U\) the larger regret. It is decreasing up to its constrained minimizer \(s_{\beta_U}\), which is at least \(s^{MR}\). For \(s>s^{MR}\), the larger regret is \(R_L\), increasing after \(s_{\beta_L}\), which is at most \(s^{MR}\). Their maximum is therefore minimized exactly at the crossing. This reasoning also covers the case where both oracle policies equal zero or both equal \(S\): the crossing is that common endpoint, with zero regret. Strict convexity in \(s\) gives uniqueness.

When both endpoint oracles are interior,
\[
s^{MR}=\frac{\beta_L+\beta_U}{2HK},\qquad
\sup_\beta R_\beta(s^{MR})
=\frac{(\beta_U-\beta_L)^2}{8H^2K}.
\tag{D}
\]
Indeed \(M(\beta)=\beta^2/(2H^2K)\) in that regime; substitution into (B) proves the midpoint rule, and completing the square gives the regret. If the parameter interval collapses to a point, use its known oracle directly rather than the undefined quotient in (B).

This decision criterion differs from maximizing worst-case welfare: (A) implies that maximin welfare uses the lower endpoint \(\beta_L\) and chooses \(s_{\beta_L}\). Minimax regret instead balances losses relative to the policy that each admissible economy would have selected. The report does not choose between those objectives on the policymaker's behalf.

The result relies on the source's sharp common-parameter construction, fixed identities, quasilinearity and constant positive curvature. It does not identify the true agglomeration split, introduce wage-response evidence, or solve unequal-ownership and heterogeneous-welfare extensions. No empirical recommendation or external-literature claim is made.

Source: [ECON-R58-287-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/9e/prb_9e0fa4ceb644498393d5864bb773fe5f/contributions/con_6bb05e0cc1e94bf1ab8590fe6590c261/files/R58-287.tex), canonical revision `rev_1301c9d2f122473d92e6a73eafe8101f`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
