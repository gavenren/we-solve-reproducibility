# Capacity rents attenuate aggregate task-cost elasticities

The manuscript gives exact unconstrained expenditure weights and a capacity-constrained allocation. Those weights require modification once task capacities bind. Within the same model, a shadow-price identity measures exactly how much total output responsiveness to task costs is attenuated.

Write the productive budget as \(E=R-F>0\). Retain positive costs, weights and capacity bounds, and the source's assumption \(E<\sum_jc_j\bar q_j\), with infinite capacities permitted. Let \(V(c,E,\bar q)\) be optimal CES output, and \(q^*\) its unique allocation from the capacity theorem. Every task is produced positively, and at least one is unsaturated. Let \(m_j=\partial Q(q^*)/\partial q_j\).

The first-order conditions supply a positive resource multiplier \(\lambda\) and nonnegative capacity multipliers \(\nu_j\):
\[
m_j=\lambda c_j+\nu_j,\qquad
\nu_j(\bar q_j-q_j^*)=0.
\tag{A}
\]
For an infinite cap set \(\nu_j=0\). An unsaturated positive coordinate gives \(\lambda=m_j/c_j>0\). The budget binds because output is increasing and not every task can be saturated. The source's clipped allocation satisfies these conditions; concavity makes them sufficient.

Euler's identity for the homogeneous CES aggregator gives
\[
V=\sum_jq_j^*m_j
=\lambda E+\sum_{j:\bar q_j<\infty}\nu_j\bar q_j.
\tag{B}
\]
Thus aggregate output decomposes into a resource shadow value and capacity shadow rents. The latter are optimization values, not additional measured output or an assumed household transfer.

The envelope derivatives, at a regular parameter point, are
\[
\frac{\partial V}{\partial c_j}=-\lambda q_j^*,\quad
\frac{\partial V}{\partial E}=\lambda,\quad
\frac{\partial V}{\partial\bar q_j}=\nu_j
\quad(\bar q_j<\infty).
\tag{C}
\]
They follow by differentiating the Lagrangian \(Q+\lambda(E-\sum c_jq_j)+\sum\nu_j(\bar q_j-q_j)\). No derivative of the chosen quantities enters because the first-order and complementarity conditions cancel those terms. The same statements apply within each fixed active-set region; at switching points one can instead use the associated one-sided envelope sensitivities. The primal optimizer and resource multiplier are uniquely determined here.

Define
\[
s_j=\frac{\lambda c_jq_j^*}{V},\qquad
r_j=\frac{\nu_j\bar q_j}{V}
\]
for finite caps, with \(r_j=0\) at infinite caps. Equations (B) and (C) imply
\[
-\frac{\partial\log V}{\partial\log c_j}=s_j,\qquad
\frac{\partial\log V}{\partial\log E}=\sum_js_j,\qquad
\sum_js_j+\sum_jr_j=1.
\tag{D}
\]
Consequently the cost elasticities sum to at most one, and strictly less than one whenever a capacity has positive shadow value. Without active caps, every \(\nu_j=0\), \(V=E/P(c)\), and \(s_j\) reduces exactly to the manuscript's CES expenditure share. A cap that happens to bind with zero multiplier creates no strict attenuation; that distinction matters at thresholds.

For example, reduce every task cost proportionally while holding physical caps and \(E\) fixed. Equation (D) says that its local output elasticity is \(\lambda E/V\), rather than automatically one. Saved resources can expand unsaturated tasks, but cannot expand the physically fixed task quantities. Conversely, relaxing a valuable cap has elasticity \(r_j\), which the unconstrained task-cost index omits. Since \(E=R-F\), the local loss from an additional unit of deployment cost is \(\partial V/\partial F=-\lambda\).

These formulas give an independent aggregation check for experiments reporting task-level cost reductions. They retain the common-resource model and declared physical caps; they do not identify compute capacity, deployment investment or an empirical TFP accounting map. They neither equate shadow rents with national income nor infer that cap constraints disappear in a transition. The manuscript's bottleneck ceiling and measured-TFP identity remain separate statements.

Source: [ECON-O33-298-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f2/prb_f20f430edb9c42c4b47e512cd6c4cff7/contributions/con_faa5510821c2472c9635b76a339e0405/files/O33-298.tex), canonical revision `rev_1bc3e7dab96c417da8627289b8a60655`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
