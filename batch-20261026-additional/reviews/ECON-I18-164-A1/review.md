# A fully specified price-cut stress test with more access, more approvals and lower welfare

**Finding: Supports the claim.** The manuscript's welfare accounting and its warning against treating approvals as a welfare statistic are correct. An independent stress test shows that even observing both increased patient access and increased approvals after a price cut does not settle the welfare sign in the stated model. This complements its displayed example, which instead has falling approvals and unchanged access per approved project.

I read the complete pinned manuscript and contribution metadata. The contribution is an unresolved exploration, not a claimed causal evaluation of United States price regulation. The finite candidate universe, independent approval shock and development cost, exogenous policy-specific patient years, disjoint treatment portfolios and domestic transfer convention are explicit restrictions. Its account of failed-project costs is particularly important: investment cost is incurred whether or not approval occurs, whereas patient benefit and production cost are multiplied by approval probability.

The basic formula checks out directly. With \(I_{jp}=\mathbf1\{F_j\le t_{jp}\}\), expected welfare is
\[
 V_p=\sum_j\mathbb E[I_{jp}(v_{jp}-F_j)].
\]
No cross-project independence is needed for this expected sum. The integration interval includes an atom at zero and an atom at the investment threshold, consistently with the specified investment-at-indifference convention. For nested decreasing thresholds, splitting this expectation over retained and abandoned cost realizations gives equation (3), including the development costs saved by abandonment. The approval-count counterexample is therefore correctly calculated.

For a policy that increases some thresholds, a symmetric accounting formula makes the direction explicit. Suppress \(j\) and write \(m=\min(t_0,t_1)\). Then
\[
 \Delta V=(v_1-v_0)G(m)
 +\mathbf1\{t_1>t_0\}\int_{(t_0,t_1]}(v_1-f)\,dG(f)
 -\mathbf1\{t_0>t_1\}\int_{(t_1,t_0]}(v_0-f)\,dG(f).
 \tag{A}
\]
This follows by partitioning the two investment sets into their intersection and their two differences. It preserves threshold atoms and also covers equal thresholds. The manuscript already notes that its decreasing-threshold condition is maintained rather than implied by the word regulation; (A) independently checks that boundary.

There is also an exact distribution-free sign certificate for an expanding threshold. If \(t_1>t_0\), the welfare change is nonnegative for *every* nonnegative finite-mean cost distribution if and only if both \(v_1\ge v_0\) and \(v_1\ge t_1\). Sufficiency follows from (A): every retained cost has gain \(v_1-v_0\), and every entering cost has gain \(v_1-f\ge v_1-t_1\). Necessity follows by concentrating all probability at zero when the first inequality fails, or at a cost in \((\max\{t_0,v_1\},t_1]\) when the second fails. These are admissible deterministic cost distributions. Thus increased gross social value alone is insufficient: the entrant at the private threshold must also have nonnegative social net value for a guarantee uniform over costs.

Here is a concrete two-project example. Let the projects treat disjoint populations. For both projects set approval probability \(q=1\), production cost \(c=0\), clinical value \(\lambda b=1\) per patient year, and financing limit ten. Under policy zero, let reimbursement be three and patient years per approved project be one. Under policy one, reimbursement falls to two while patient years rise to three. Hence expected private operating profit, and therefore the unconstrained investment threshold, increases from three to six despite the reimbursement cut.

Let the retained project have deterministic development cost one, and the second project have deterministic development cost \(11/2\). Initially only the retained project is invested in; after the price cut both are. All costs have finite mean and all financing conditions hold. Approvals increase from one to two. Patient years, and therefore total health value in these units, increase from one to six. Nevertheless,
\[
 V_0=1-1=0,\qquad
 V_1=(3-1)+(3-11/2)=-1/2.
\]
Access on the retained project adds two units of welfare, but the newly induced project costs \(11/2\) to deliver only three units of health value. The development cost is real; drug reimbursements are transfers and are not subtracted again. Both projects have positive gross clinical benefit, so the welfare reversal does not depend on a harmful treatment or a negative per-patient social surplus.

The same example checks the clinical-value identified interval. Permit the two clinical benefits to range independently over \([0.8,1.2]\), while keeping the demand and reimbursement primitives fixed as the manuscript requires. The change becomes
\[
 \Delta V=2b_{\rm retained}+3b_{\rm entrant}-11/2.
\]
Its sharp range is \([-1.5,0.5]\), attained by the two endpoint benefit vectors. Thus perfectly known reimbursement, access and approval responses still leave the policy ranking unidentified. Moving the benefits changes neither firm's threshold in this specified partial-equilibrium model; if it changed demand, the endpoint calculation would no longer be valid, exactly as the manuscript warns.

Finally, the derivative formula differentiates the truncated expected surplus correctly away from the financing kink. With fixed nonnegative \(v\), including costs below \(v\) and excluding those above \(v\) proves the optimal-threshold statement even with atoms. That abstract threshold instrument does not establish implementability through a price cap or account for fiscal distortions of prizes.

**Source reviewed:** [I18-164.tex at the pinned revision](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/7b/prb_7b70e7aa61fd44b890acd225c42aec2c/contributions/con_8fbdbc1326fc4a68b7bc4265be7d17fa/files/I18-164.tex). Contribution revision: rev_fbf80a55eb8347abaa54cc8ce4b887d9. The stress test supports the stated identification warning; it supplies no empirical policy effect and does not resolve the broader innovation problem.

