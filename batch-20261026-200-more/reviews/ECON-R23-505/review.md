# Known mean social ties yield an exact finite linear program with two-point witnesses

The source bounds one incumbent's welfare change over an unknown persistent tie value. If external evidence identifies the population mean tie value but leaves its distribution unknown, the aggregate problem remains exactly solvable. The individual pointwise bounds need not be sharp after imposing that mean.

Use a homogeneous baseline-incumbent subclass with common known \(v_a,b_a\), tie support \(t\in[0,T]\), and \(T>0\). Let the unknown population distribution of ties have known mean \(\bar t\in[0,T]\). Keep the same persistent \(t\) in both regimes and define
\[
\Delta(t)=\max(v_1+t,b_1)-\max(v_0+t,b_0).
\]
Let \(0=x_1<\cdots<x_J=T\) be the distinct sorted points consisting of both support endpoints and any thresholds \(b_a-v_a\) lying strictly inside the support. Set \(d_j=\Delta(x_j)\).

The sharp bounds for mean incumbent welfare are precisely the minimum and maximum of
\[
\sum_{j=1}^J\pi_jd_j
\]
subject to
\[
\pi_j\ge0,\qquad\sum_j\pi_j=1,\qquad\sum_j\pi_jx_j=\bar t.
\]
This finite linear program has at most four points, and every extremal value is attained by a distribution supported on at most two of them.

First, the program is nonempty because mixing the endpoints realizes any permitted mean; its simplex slice is compact. Every feasible solution is an actual tie distribution satisfying all stated information, and its objective equals the target. Conversely, on every interval between adjacent \(x_j\), the source proves that \(\Delta\) is affine. Replace any tie value inside that interval by a lottery over its endpoints with the same conditional mean. This replacement also preserves its conditional mean welfare because of affinity. Applying it to the whole distribution preserves both \(\mathbb E[t]\) and \(\mathbb E[\Delta(t)]\), and leaves a distribution on the finite breakpoint set. Thus the finite program loses no attainable value.

For the support bound, suppose an extreme feasible vector has at least three positive coordinates. The two constraints on their total mass and mean have rank at most two, so there is a nonzero perturbation on those coordinates preserving both constraints. A sufficiently small perturbation of either sign preserves nonnegativity, contradicting extremality. Linear objectives attain optima at extreme points, so two-point witnesses exist. Mixing the endpoint-optimal distributions preserves the mean and fills the entire interval between the two optimal welfare values; hence these are sharp bounds on the complete identified set.

An equivalent geometric characterization is useful for inspection. The lower bound is the lower convex envelope of the graph points \((x_j,d_j)\) evaluated at \(\bar t\); the upper bound is the upper concave envelope there. Operationally, evaluate every pair \(x_i\le\bar t\le x_j\), assigning masses \((x_j-\bar t)/(x_j-x_i)\) and \((\bar t-x_i)/(x_j-x_i)\), plus a singleton when \(\bar t=x_i\), then take the smallest and largest interpolated values.

In the source's example, the points are \((0,2),(2,2),(5,-1),(6,-1)\). At mean tie value three, the sharp mean-welfare interval is \([1/5,5/4]\): the lower witness mixes \(t=0,5\) with masses \(2/5,3/5\); the upper mixes \(t=2,6\) with masses \(3/4,1/4\). Both are tighter than the individual support interval \([-1,2]\). They require no independence assumption between a tie and its optimizing move decision.

Checked locations: common-tie model (1), sharp individual bounds and the worked example. Full source/YAML were read. Heterogeneous shared rents, household-specific known means, equilibrium constraints and validation of a monetary tie mean require a joint extension. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-R23-505-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ff/prb_ff866b1afdb441b5a7835b83658e5330/contributions/con_bbe54f58abcd4ae796c8ca013adf93ea/files/R23-505.tex). Canonical revision: `rev_80604f3392a4408684e29e38cad56e52`.

