# Endpoint distributions can identify controlled-effect signs

The source carefully distinguishes its sharp mean-data bounds from what richer endpoint distributions imply. Under its individual scale restriction, the distribution-informed bounds can be completed exactly, including the joint set of both controlled ownership effects.

Write \(A_0=A(0,s_0)\) and \(A_1=A(1,s_1)\), with identified marginal distributions on \([0,1]\), means \(a,b\), and \(c=L(s_1-s_0)\ge0\). The missing cells are \(B_0=A(0,s_1)\) and \(B_1=A(1,s_0)\). The source's individual restriction gives
\[
A_0\le B_0\le\min(1,A_0+c),\qquad
\max(0,A_1-c)\le B_1\le A_1.
\tag{A}
\]
Define
\[
u_0=E[\min(1,A_0+c)],\qquad
l_1=E[\max(0,A_1-c)].
\]
Then the exact joint mean set of missing cells is
\[
(E B_1,E B_0)\in[l_1,b]\times[a,u_0].
\tag{B}
\]
Consequently the exact joint set of controlled ownership effects is
\[
(\tau_F(s_0),\tau_F(s_1))
\in[l_1-a,b-a]\times[b-u_0,b-a].
\tag{C}
\]

To prove sharpness, couple the observed endpoint variables \(A_0,A_1\) arbitrarily; their joint cross-regime distribution is not observed or restricted. For any constants \(\lambda_0,\lambda_1\in[0,1]\), set
\[
B_0=A_0+\lambda_0\{\min(1,A_0+c)-A_0\},
\]
\[
B_1=\max(0,A_1-c)
+\lambda_1\{A_1-\max(0,A_1-c)\}.
\]
These missing outcomes obey (A) pointwise and independently span both mean intervals. Linear interpolation over scale between each ownership-specific pair of endpoints has slope between zero and \(L\), stays in \([0,1]\), and supplies a complete admissible response function. Thus every pair in (B), and hence every pair in (C), is attained while preserving both full observed endpoint distributions. Degenerate intervals cause no difficulty. This proof does not impose an unobserved common-rank coupling.

The controlled interaction \(I=\tau_F(s_1)-\tau_F(s_0)\) therefore has the sharp interval
\[
I\in[a-u_0,\ b-l_1].
\]
Subtracting opposite endpoints of (C) proves inclusion, and the construction above attains both extremes simultaneously. These joint statements require the source's absence of cross-ownership shape restrictions; additional restrictions would couple the two missing cells.

The improvement over mean-only bounds can change a substantive sign conclusion. Take endpoint outcomes to be binary, with \(\Pr(A_0=1)=3/10\), \(\Pr(A_1=1)=3/5\), and \(c=2/5\). Then
\[
l_1=(1-c)b=9/25,\qquad
u_0=a+c(1-a)=29/50.
\]
Equation (C) yields
\[
\tau_F(s_0)\in[3/50,3/10],\qquad
\tau_F(s_1)\in[1/50,3/10].
\]
Both controlled effects are strictly positive throughout the identified set. Using only the same means, the source's intervals are \([-1/10,3/10]\) at both scales, leaving either sign possible.

Why does the difference arise? When a unit's high-scale endpoint is one, the scale restriction forces its low-scale outcome to be at least \(1-c\). When a unit's low-scale endpoint is zero, its high-scale outcome cannot exceed \(c\). Averaging these individual restrictions is stronger than clipping only the mean.

This is a sharp conditional identification refinement. It does not identify actual multinational spillovers, justify an infeasible ownership-scale intervention, or recover physical productivity from revenue data. It retains fixed domestic-firm identities, the specified investment version and exposure mapping, and leaves causal assignment and cohort follow-up requirements intact.

Source: [ECON-F23-525-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/7d/prb_7d369a8255fa40f4abc8160b8c002c8a/contributions/con_2e9a96cd3ede42489918bfae52f6703a/files/F23-525.tex), canonical revision `rev_ccacca55e6694198825989f72bb5928b`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
