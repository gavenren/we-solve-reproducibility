# A joint durability polytope with one common baseline

The source correctly warns that a shared persistence parameter couples multiple tutor arms. Bounded outcomes impose an additional joint restriction: the two effects must use the same future comparator mean. Combining these restrictions gives an exact finite polytope for the mean-level durability class.

Let the identified early assistant-free effects be \(s_1,s_2\), and suppose the maintained bridge is
\[
\tau_j=\rho s_j+d_j,\qquad
\rho\in[\rho_L,\rho_U],\quad |d_j|\le\epsilon_j,\quad j=1,2.
\tag{A}
\]
The six-month outcomes \(Y(0),Y(1),Y(2)\) all lie in \([0,1]\). Assume no other temporal or outcome-level restrictions. In particular, (A) concerns effects, not a rank-preserving individual law linking early and future scores.

The exact joint set is the projection onto \((\tau_1,\tau_2)\) of
\[
\rho_L\le\rho\le\rho_U,\qquad
-\epsilon_j\le\tau_j-\rho s_j\le\epsilon_j,
\]
\[
-1\le\tau_j\le1,\qquad
|\tau_1-\tau_2|\le1.
\tag{B}
\]
It is a compact convex polytope when nonempty. If it is empty, the supplied bridge and bounded-score model are jointly rejected.

To prove the additional inequalities, write \(\mu_0=E Y(0)\), so the active means are \(\mu_0+\tau_1,\mu_0+\tau_2\). Three numbers in \([0,1]\) can differ by at most one. Thus each effect and their difference satisfy (B).

Conversely, given any effects obeying those range inequalities, a common baseline mean exists precisely when
\[
\max(0,-\tau_1,-\tau_2)
\le
\min(1,1-\tau_1,1-\tau_2).
\tag{C}
\]
The left side is the least baseline consistent with nonnegative arm means, and the right side is the greatest consistent with means at most one. Condition (C) is equivalent to
\[
\max(0,\tau_1,\tau_2)-\min(0,\tau_1,\tau_2)\le1,
\]
which in turn is exactly the three pairwise range restrictions in (B). Choose any such \(\mu_0\), and set future potential scores to the constants \(\mu_0,\mu_0+\tau_1,\mu_0+\tau_2\), respectively. They are bounded and realize the desired effects. Append these future outcomes to the complete observed early-data law without changing it. Since the only bridge is the mean condition (A), the chosen \(\rho,d_1,d_2\) make this a compatible continuation. This proves sharpness of the entire projected set.

A small example shows why coordinate intervals are insufficient even at a fixed persistence value. Let early effects be \(s_1=0.4,s_2=-0.4\), realized by early means \(0.5,0.9,0.1\). Set \(\rho=1\) and \(\epsilon_1=\epsilon_2=0.6\). The separate delayed-effect intervals include \(\tau_1=0.8\) and \(\tau_2=-0.8\). Together those values are impossible: they require active means differing by \(1.6\). Inequality \(|\tau_1-\tau_2|\le1\) correctly removes that pair, even though both individual contrasts lie in \([-1,1]\).

Every linear joint question, such as the worst-case advantage of one tutor over another, is a linear program over (B). This preserves the common persistence and baseline rather than combining extrema from different continuations. Sampling uncertainty in the early effects requires retaining their simultaneous confidence set as well; the population polytope alone is not a confidence statement.

This result does not validate a six-month persistence bridge, estimate delayed learning, or remove classroom interference and attrition concerns. It supplies an exact realizability refinement inside the source's explicitly stated mean-level sensitivity model.

Source: [ECON-I21-591-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/a9/prb_a9c216bfe7654ac49ed3e886ee724786/contributions/con_cc269e6c263c4cf3a66d51c7aa4c27e1/files/I21-591.tex), canonical revision `rev_4db9d4e5c3f24c28b6b890e82f3d1d14`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
