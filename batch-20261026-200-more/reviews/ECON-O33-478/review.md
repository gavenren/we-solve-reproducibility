# A dated resource budget turns feasible acceleration into an exact fractional-knapsack frontier

The source proves sharp adoption reachability with date-specific investment capacity alone and correctly warns that resource scarcity can invalidate sufficiency. Adding an explicit total resource budget preserves tractability and yields a complete minimum-cost acceleration frontier.

Fix a horizon \(H\ge1\), stock recursion \(S_{t+1}=(1-\delta)S_t+J_t\), initial \(S_0>0\), and required complementary stock \(\kappa>0\). Let investment capacities be \(0\le J_t\le u_t<\infty\), \(t=0,\ldots,H-1\). Dedicated outside resources finance investment at positive declared costs \(c_tJ_t\), with total budget \(\sum_tc_tJ_t\le B\). This is the complete additional resource constraint in this extension; it is not inferred from accounting residuals.

Write
\[
w_t=(1-\delta)^{H-1-t},\qquad
K=[\kappa-(1-\delta)^HS_0]_+.
\]
Then full adoption at \(H\) is feasible exactly when there is a capacity-feasible investment plan with \(\sum_tw_tJ_t\ge K\) costing at most \(B\). If \(K=0\), zero investment suffices. Dates with \(w_t=0\) cannot help reach the target and optimally receive no investment in a minimum-cost plan.

For every positive-weight date define delivered stock \(x_t=w_tJ_t\), delivered capacity \(a_t=w_tu_t\), and cost per unit of horizon stock \(\rho_t=c_t/w_t\). Sort dates in nondecreasing \(\rho_t\), omitting zero weights and capacities. If \(\sum_ta_t<K\), capacity alone makes the target impossible. Otherwise let \(j\) be the first sorted index for which cumulative capacity reaches \(K\). The exact minimum cost is
\[
B_{\min}(K)=
\sum_{\ell<j}\rho_\ell a_\ell+
\rho_j\left(K-\sum_{\ell<j}a_\ell\right).
\]
A minimizing plan fills every cheaper date to capacity, uses only the required fraction at date \(j\), and uses no more expensive date. Thus the joint resource-and-capacity criterion is exactly \(B\ge B_{\min}(K)\).

For proof, any plan delivering more than \(K>0\) can have positive investment reduced until it delivers exactly \(K\), strictly lowering cost; all weights and costs on useful dates are positive. If a proposed minimum uses positive stock from an expensive date while a cheaper date is unsaturated, move a sufficiently small amount of delivered stock from the expensive date to the cheaper one. This preserves total delivered stock and capacities and decreases cost by the stock amount times the strict ratio difference. Repeating yields the sorted form; ties permit alternative equally costly assignments. Direct substitution gives the displayed cost, proving sufficiency and global necessity. The minimum exists because the finite capacity rectangle is compact.

For equal costs and \(0<\delta<1\), later dates have larger \(w_t\), so they are filled first. This late-investment conclusion is a depreciation consequence under dedicated resources, with no benefit from early deployment included. At \(\delta=0\), all stock weights equal one and only the cost ranking matters. At \(\delta=1\), only date \(H-1\) has positive weight, so the criterion reduces to its final-date capacity and cost. These cases prevent division by a zero delivery weight.

As an exact example, take \(H=3,\delta=1/2,u_t=c_t=1\), and required stock above inherited stock \(K=5/4\). Delivery weights are \(1/4,1/2,1\). Minimum cost uses \(J_2=1,J_1=1/2,J_0=0\), costing \(3/2\). A budget below \(3/2\) makes adoption infeasible despite adequate total capacity.

Checked locations: stock recursion, sharp capacity-only acceleration theorem, and resource-feasibility counterexample. Full source/YAML were read. This solves dated reachability, not welfare-optimal diffusion: learning benefits, endogenous output financing, firm choice and the productivity-residual comparison still require their own primitives. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-O33-478-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/00/prb_003a552c5dd640578f1a65d9bd25daa3/contributions/con_3786f30a77ea4f73b3ac826e33476e00/files/O33-478.tex). Canonical revision: `rev_95e7bd8a222244a6874f25897e128555`.

