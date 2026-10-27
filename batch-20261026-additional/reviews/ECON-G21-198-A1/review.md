# Convex-order verification and an exact CARA participation frontier

Finding: **Supports the claim**.

This review concerns the complete [pinned G21-198 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f6/prb_f6a9f49c546b4156841933a5ca6d3899/contributions/con_8838f0c098ea474abe90d6144f51fcc9/files/G21-198.tex), revision `rev_4b1b8adb560e4fa08519f49c2a52165e`. I read its metadata as well. It is an unresolved exploration with enforceable reciprocal insurance, verified project outcomes, homogeneous borrowers, and an explicitly lender-contract-only complexity metric. The manuscript itself proves that terminal selfish borrowers would not implement the sharing rule without commitment. Treating that acknowledged assumption as an unnoticed gap would misstate the claim. I instead independently verify the welfare ordering and derive an exact, usable meeting-cost threshold for a permitted utility family.

Expected lender repayments are indeed I under both initial contracts. Individual liability collects qR_I=I. Under joint liability each borrower pays R_J with probability q² and 2R_J with probability q(1−q), giving q(2−q)R_J=I. The mixed-outcome probability is doubled only when forming a member's post-sharing consumption distribution; it must not be doubled again in her own repayment probability. The manuscript makes this distinction correctly.

An independent convex-order certificate verifies the welfare comparison for every concave utility, including utilities lacking derivatives. Remove the protected endowment and write the four positive-state consumption levels as

\[
a=(H-2R_J)/2,\quad b_1=(H-R_I)/2,
\quad c=H-R_I,\quad d_1=H-R_J.
\]

Payment feasibility gives 0≤a<b_1<c<d_1. Let p=q² and m_1=2q(1−q). Individual-liability residual consumption X_I takes c,b_1,0 with probabilities p,m_1,(1−q)²; joint-liability residual consumption X_J takes d_1,a,0 with the same probabilities. The distributions have equal means, and

\[
p(d_1-c)=m_1(b_1-a).
\]

For any threshold t, direct evaluation of the two stop-loss functions gives

\[
\mathbb E(X_J-t)_+-\mathbb E(X_I-t)_+
=\begin{cases}
0&t\le a,\\
m_1(t-a)&a\le t\le b_1,\\
p(d_1-c)&b_1\le t\le c,\\
p(d_1-t)&c\le t\le d_1,\\
0&t\ge d_1.
\end{cases}
\]

Every expression is nonnegative. Thus X_I is dominated by X_J in convex order, giving the claimed direction for concave borrower utility after restoring the common endowment. The piecewise formula also shows a nonzero dispersion reduction on a whole interval, explaining strictness under strict concavity. This is a distribution-level certificate rather than a test of one chosen utility or a variance comparison alone.

For the meeting-cost extension, take a strictly increasing, strictly concave utility already admitted by the assumptions: u(c)=−exp(−ρc), with ρ>0. Let h_0=H−I/q and h_m=h_0−m/q. Then the simple insured group's expected utility and solo utility are exactly

\[
G_m=-e^{-\rho b}[1-q+q e^{-\rho h_m/2}]^2,
\qquad
S_0=-e^{-\rho b}[1-q+q e^{-\rho h_0}].
\]

The square follows from the two independent project successes. Its sign matters: G_m≥S_0 is equivalent to the squared bracket being no larger than the solo bracket. Taking the positive square root and then logarithms yields the exact threshold

\[
m\le m_*:=qh_0+\frac{2q}{\rho}
\log\left(
\frac{\sqrt{1-q+q e^{-\rho h_0}}-(1-q)}q
\right).
\]

This criterion applies within the manuscript's payment-feasible domain 0≤m≤q(2−q)H/2−I. The logarithm's argument is positive and below one; strict insurance gains at m=0 imply m_*>0. Utility falls strictly as the financed meeting cost rises, so membership strictly beats solo borrowing below m_*, is tied at m_*, and loses above it. Combined with the manuscript's strict-blocking convention, this gives an exact transition between near-complete pairing, arbitrary stable matchings at equality, and universal solo borrowing, subject to payment feasibility.

For example, q=1/2, I=1/5, H=2, b=1 and ρ=1 give m_* approximately 0.202920989. The feasibility ceiling is 0.55, so this participation threshold is interior and economically operative. Direct evaluation confirms equality at m_*, a positive group-utility difference at half that cost, and a negative difference at one-and-a-half times that cost. The threshold is independent of b here because CARA utility factors out the common endowment; this is a feature of the chosen family, not of arbitrary concave utility.

I independently checked the stop-loss identity across several admissible parameters and the exact CARA comparison. I found no mathematical defect in the two-contract welfare ordering or homogeneous formation characterization. These additional certificates support the claimed restricted separation of liability from insurance. They do not supply the enforcement, monitoring, heterogeneous matching, or comprehension mechanisms the manuscript expressly leaves unresolved.
