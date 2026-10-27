# Independent check of timing neutrality and hidden-transfer sharpness

Finding: **Supports the claim**.

This review concerns the [pinned H24-183 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/d9/prb_d9ee126843624b42bd48f43646cfd7a9/contributions/con_3f1489411d2a445487d31578b6c6f6f4/files/H24-183.tex), revision `rev_1520032f90904a4e9a27e7cd223b08c3`. I read its complete source and contribution metadata. The metadata calls this an unresolved exploration; the manuscript expressly confines its welfare dominance to a fixed-saving, equal-weight benchmark with all estates maturing. The assessment below supports those restricted results and supplies independent sharp examples and an additional measurement calculation. It does not certify an optimal inheritance-tax system.

The behavioral calculation is internally consistent. Dividing the donor objective by positive wealth P leaves a strictly concave quadratic in the gift fraction. Its linear coefficient is (1−t_g)−d(1−t_e), so the clipped solution follows without any distributional assumption beyond positive P. The donor's separate consumption resources pay the gift-management cost, as explicitly stipulated. Consequently one must not subtract that cost again from the principal reaching the recipient.

There is a particularly useful independent accounting check. Write S=α+d(1−α) for the fraction of parental principal received by the horizon. The recipient coefficient and tax coefficient satisfy T+r=S. When d=1, S=1 identically: endogenous timing changes cannot change the sum of receipts and revenue. Therefore any same-revenue policy has the same population regression coefficient under the stated zero baseline covariance. Harmonizing both statutory rates at r eliminates the quadratic management cost while preserving that accounting identity. This confirms the exact welfare gain, not just its sign. The maximal-rate policy's dominance also follows because r is then a convex combination of the two bounded statutory rates. These arguments depend on the manuscript's resource and welfare conventions.

The all-estates-mature condition is quantitatively essential. Consider d=1/2, κ=1, and initial equal rates t_g=t_e=1/2, with a legal upper bound at least 1/2 and below one. Then α=1/4 and the effective revenue coefficient is r=5/16. Replacing the statutory pair by (5/16,5/16) produces α'=11/32 and effective revenue

\[
r'=\frac{5}{16}\left(\frac12+\frac12\frac{11}{32}\right)
=\frac{215}{1024}<\frac{5}{16}.
\]

Thus the same numerical harmonization operation ceases to be revenue equivalent even without reporting or saving responses. This is a check of the explicitly stated boundary, not a counterexample to the theorem. Receipt before the horizon has its own value when the donor may survive.

The hidden-transfer interval is also sharp for exactly the measurement class declared. A concrete example makes both its breadth and the importance of omitted information transparent. Let P equal 1 or 3 with equal probabilities, let observed terminal resources be zero, and take h(P)=P. Then E P=2 and Var(P)=1. The manuscript's lower endpoint is −1/2, attained by U=1 at P=1 and U=0 at P=3. Its upper endpoint is 3/2, attained by U=0 at P=1 and U=3 at P=3. All intermediate coefficients are feasible. Nonnegative concealed transfers can therefore generate a negative regression slope; nonnegativity alone imposes no positive association with parental resources.

An additional observable mean would materially change that conclusion. Suppose the same example also reveals E U=1. Let u_1 and u_3 denote the conditional means of U. Feasibility requires 0≤u_1≤1, 0≤u_3≤3 and u_1+u_3=2. Consequently

\[
\operatorname{Cov}(P,U)=\frac{u_3-u_1}{2}=1-u_1\in[0,1].
\]

Conversely, every u_1 in [0,1], with deterministic conditional transfers u_3=2−u_1, attains its corresponding coefficient. The sharp set is now [0,1], strictly smaller than [−1/2,3/2]. This is a new restriction on the measurement class, not a correction to equation (8). It explains precisely why that equation must not be combined mechanically with externally known revenue or aggregate-transfer information: the endpoint constructions need not preserve such information.

All arithmetic in these examples was independently checked. I found no mathematical defect in the reported timing-response, all-estates-mature harmonization, or unrestricted hidden-transfer sharpness arguments. The useful next extension is to optimize the hidden-transfer covariance subject to the common aggregate and cross-policy restrictions actually available, rather than regarding separate pointwise envelopes as already jointly sharp.
