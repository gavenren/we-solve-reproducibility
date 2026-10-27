# Review of ECON-Q54-176-A1

**Finding: Supports the claim.** I independently checked the optimal-loss formula, monotonicity and sharpness of the rectangular hazard bounds, the stable-choice derivative, and the perfect-information equality criterion. The contribution metadata calls this an unresolved exploration; the manuscript explicitly excludes general-equilibrium feedback, migration, endogenous hazards, and nonlinear utility. The restricted finite-menu claims are valid. A further minimax calculation below identifies an additional consequence of their assumptions and gives a concrete boundary example.

The source reviewed is [the pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/23/prb_2305de6c430c4d1ca1b8a67f9e3bf60c/contributions/con_357de524c5f14e0ab9ca393a5efa063f/files/Q54-176.tex), revision `rev_5fc13a69d3714a7ea9f645a9c03cf3f8`. This review concerns the finite protective-investment model and does not certify a real-world welfare estimate.

## A stronger interpretation of the upper endpoint

The manuscript computes
\[
\sup_{q\in\mathcal Q}\min_a J(a,q)
=L(\overline q).
\]
Here protection is reoptimized for every physical model. In general this is distinct from the problem of choosing one plan before learning the physical model:
\[
V_{\rm robust}=\min_a\sup_{q\in\mathcal Q}J(a,q).
\]
For the manuscript's rectangular hazard set, however, the two problems have exactly the same value.

To verify this without an interchange theorem, fix any plan \(a\). Since every residual damage is nonnegative, every cumulative tipping probability \(F_t(q)\) is coordinatewise nondecreasing, and
\[
J(a,q)\le J(a,\overline q)
\quad\text{for every }q\in\mathcal Q.
\]
The vector \(\overline q\) belongs to the box. Therefore
\[
\sup_{q\in\mathcal Q}J(a,q)=J(a,\overline q)
\]
for every plan separately. Taking the minimum gives
\[
\min_a\sup_qJ(a,q)=\min_aJ(a,\overline q)
=L(\overline q)=\sup_q\min_aJ(a,q).
\]
In particular, any optimizer at the upper hazard corner is one plan whose loss never exceeds the reported upper endpoint under any admissible hazard vector. This is a stronger operational interpretation than simply reoptimizing separately at the endpoints. It depends on all plans sharing the same greatest admissible hazard vector, together with nonnegative damages and protection-independent hazards.

The distinction matters outside that assumption. Here is an explicit example within the manuscript's consumption accounting but with a nonrectangular physical set. Use only dates 1 and 2, set every later damage and hazard to zero, and allow two hazard vectors
\[
q^A=(1/2,0),\qquad q^B=(0,1).
\]
Their cumulative tipping probabilities are respectively \((1/2,1/2)\) and \((0,1)\). Choose two zero-cost plans with discounted residual-damage vectors
\[
(\beta D_1(a),\beta^2D_2(a))=(2,0),\qquad
(\beta D_1(b),\beta^2D_2(b))=(0,1).
\]
The resulting loss matrix is
\[
\begin{array}{c|cc}
 &q^A&q^B\\ \hline
a&1&0\\
b&1/2&1
\end{array}.
\]
Each physical model permits an attractive different plan, and
\[
\max_q\min_a J(a,q)=1/2,
\qquad
\min_a\max_q J(a,q)=1.
\]
All costs and damages are nonnegative, a zero-cost baseline plan exists, and sufficiently large endowments ensure positive consumption. Thus the failure comes from removing the common upper physical model, not from utility or feasibility complications. This is not a counterexample to the source theorem: it verifies why the manuscript explicitly warns against Cartesian sharpness claims under joint restrictions.

## Derivatives, kinks, and information

For a separate check on the derivative proposition, hold all hazards except \(q_s\) fixed. Each \(J(a,q)\) is affine in \(q_s\), because each survival product contains that coordinate at most once. Hence \(L\), the pointwise minimum of finitely many such affine functions, is coordinatewise concave and piecewise affine. At a strict optimum, a positive finite-menu value gap ensures the active plan remains unchanged locally, giving equation (5) directly. At a tie, the one-sided slopes can differ, which explains the manuscript's refusal to assert differentiability there.

This coordinatewise statement should not be promoted to joint concavity. Even a single plan with only date-2 damage has loss proportional to
\[
F_2(q_0,q_1)=q_0+q_1-q_0q_1,
\]
whose Hessian has eigenvalues of opposite signs. The manuscript makes no such stronger concavity claim; its corner and continuity arguments remain valid without it.

The perfect-information equality condition also passes a direct regret check. For any ex-ante optimizer \(a^*\), the gap between its expected loss and perfect information is the expectation of the nonnegative realized regret
\[
\ell(a^*,\tau)-\min_a\ell(a,\tau).
\]
Because timing has finite support, the expectation vanishes exactly when every positive-probability realized regret vanishes. This yields a common optimizing plan on the support, including the no-event state when it has positive probability. Requiring a common optimizer only on positive-probability states is essential; zero-probability timing realizations cannot affect equality.

These checks support the manuscript's restricted results and sharpen their interpretation. They do not address the separately acknowledged empirical calibration and equilibrium gaps. No error was found in the checked mathematical claims, and the source does not claim to have solved the unrestricted climate-tipping problem.
