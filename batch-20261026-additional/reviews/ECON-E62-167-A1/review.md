# A constructive monitoring-budget multiplier and exact sensitivity check

**Finding: Supports the claim.** The enforceability ceiling and clipped escape rule are correct for the stated one-period institutional family. The budget proposition is also correct. Its multiplier condition can be strengthened to a constructive existence result in this particular finite quadratic problem, including the boundary case where the monitoring budget equals the minimum feasible requirement. This supplies an independent computational certificate without assuming a constraint qualification that might fail at that boundary.

I read the whole manuscript and contribution metadata. Both describe unresolved restricted work. Public verification of states, linear concealment cost, terminal debt capacity, and a fixed reference requirement are explicit primitives. Dynamic hidden debt, endogenous spreads, state misreporting and optimizing the reference feedback coefficient are explicitly outside scope. I do not count their absence as defects in the proved benchmark.

The incentive theorem passes a direct global deviation check. The politician's downward-deviation payoff gain is \((B-\min\{qf,k\})x-x^2/2\). If its linear coefficient is positive, arbitrarily small permitted deviations are profitable; if nonpositive, every strictly positive deviation is strictly harmful. The upward gain is \(-Bz-z^2/2\), giving the separate necessity \(B\ge0\). This verifies both the concealment ceiling and uniqueness of actual surplus, including equality in the incentive constraint. It also explains why merely increasing a nominal fine cannot overcome a smaller concealment cost.

For the budget problem, retain the manuscript's nonempty feasible intervals \([L_\theta,U_\theta]\), and set
\[
 \ell_\theta=\frac{L_\theta-s_\theta^*+\gamma_\theta}{f_\theta},
 \qquad
 u_\theta=\frac{U_\theta-s_\theta^*+\gamma_\theta}{f_\theta}.
\]
These are least-monitoring probabilities, so \(0\le\ell_\theta\le u_\theta\le1\). For a proposed multiplier \(\lambda\ge0\), define
\[
 q_\theta(\lambda)=
 \operatorname{clip}_{[\ell_\theta,u_\theta]}
 \left(\frac{\gamma_\theta}{f_\theta}
       -\frac{c_\theta+\lambda}{f_\theta^2}\right),
 \qquad
 B(\lambda)=\sum_\theta\pi_\theta q_\theta(\lambda).
 \tag{A}
\]
Converting back through \(s_\theta=s_\theta^*-\gamma_\theta+f_\theta q_\theta\) gives exactly the manuscript's statewise minimizer with \(c_\theta\) replaced by \(c_\theta+\lambda\). The simplification in (A) is valid because the feasible interval already enforces the politician's unconstrained lower surplus.

The function \(B\) is continuous, nonincreasing and piecewise affine. At zero it is the monitoring demand of the optimum without the administrative budget. For every sufficiently large *finite* \(\lambda\), all coordinates equal \(\ell_\theta\); for example it suffices that
\[
 \lambda\ge
 \max\left\{0,\max_\theta
   \bigl(\gamma_\theta f_\theta-c_\theta-f_\theta^2\ell_\theta\bigr)
 \right\}.
\]
Thus \(B\) reaches \(B_{\min}=\sum_\theta\pi_\theta\ell_\theta\) at a finite multiplier.

If \(Q\ge B(0)\), choose \(\lambda=0\). If \(B_{\min}\le Q<B(0)\), continuity supplies a finite \(\lambda\ge0\) with \(B(\lambda)=Q\), even at \(Q=B_{\min}\). Budget feasibility and complementary slackness follow. The manuscript's Lagrangian proof then certifies optimality. Hence, for every feasible budget in this model, its sufficient multiplier certificate actually exists. The multiplier can be nonunique on a flat segment; the prescribed surplus vector remains unique by strict convexity.

This gives a finite exact solution procedure: sort the finitely many clipping breakpoints of (A), identify an interval on which the active coordinates are fixed, and solve its scalar affine budget equation. Bisection is another option, but no infinite penalty limit is necessary at minimal feasibility.

There is also a useful sensitivity check. On an interval with binding budget and a nonempty set \(I\) of unclipped coordinates, put \(H=\sum_{\theta\in I}\pi_\theta/f_\theta^2\). Then
\[
 \frac{d\lambda}{dQ}=-\frac1H,\qquad
 \frac{ds_\theta}{dQ}=\frac{1}{f_\theta H}
 \quad(\theta\in I),
\]
while clipped coordinates are locally constant. This has the expected interpretation: a larger administrative budget permits more monitoring and moves feasible prescriptions upward toward residents' preferred surplus. Kinks occur exactly when a state hits a bound.

For example, one state with \(s^*=0,\gamma=1,f=2,c=0\), feasible surplus interval \([-1,0]\), and nonbinding concealment ceiling has \(q=(s+1)/2\). For \(0\le Q\le1/2\), the optimum is \(s=2Q-1,q=Q\); for larger budgets it is \(s=0,q=1/2\). This checks the direction and scaling of the formula.

**Source reviewed:** [E62-167.tex at the pinned revision](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/90/prb_902bce6e56404e09871c605ce1734dfb/contributions/con_9c719e656a57457ead5881818fadb225/files/E62-167.tex). Contribution revision: rev_ce735a77a4914167aae40c8096cec113. These are exact results for the one-period benchmark, not a solution of dynamic fiscal-rule design.

