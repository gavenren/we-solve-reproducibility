# An independent one-state reduction and switching certificate for deterministic sensing

Finding: **Supports the claim**.

Reviewed source: [ECON-D82-205-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/23/prb_23331cf511e049ef9d5da0485ad969e1/contributions/con_aba209ddb6ef4b06ba8ebc4cedd14f85/files/D82-205.tex), revision `rev_aa339c65a60a42dfba04a7e776cf6a37` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

I find the deterministic-schedule benchmark supported. In particular, the receiver's completion-of-squares argument uses a control-independent variance only after fixing a deterministic device; the manuscript does not silently extend that argument to observation-dependent commitments. Its metadata and final section explicitly leave that extension unresolved. The independent contribution of this review is an exact reduction of the sender's two-state objective to a scalar variance-control problem, giving a useful optimality certificate and check on the coefficients.

The receiver's displayed identity is consistent with the backward equations. In the drift of \(KX^2+2sX+d\), the \(X^2\), \(X\), and constant terms combine with the running cost into
\[
 r_R\{u+b(KX+s)/r_R\}^2.
\]
Conditioning on the observation filtration adds precisely \(b^2K^2P/r_R^2\) inside this square. Multiplication by \(r_R\) produces the theorem's residual \(b^2K^2P/r_R\), not a term proportional to \(KP\). A deterministic schedule makes the Riccati variance path independent of receiver controls, which is the necessary incentive step. The stated finite-horizon linear feedback attains equality.

For the sender, put
\[
 g=b^2K/r_R,\quad A=a-g,\quad
 \gamma=r_Sb^2/r_R^2,\quad B=q_S+\gamma K^2.
\]
The mean terms in equation (1) are independent of the sensing schedule. Its schedule-dependent part is
\[
 \int_0^T\{q_SP+B S+c_S\alpha\}\,dt.
\]
Introduce \(V=P+S\), the unconditional state variance. Adding the two variance equations eliminates the direct precision term:
\[
 \dot V=2AV+2gP+\sigma^2,\qquad V(0)=P_0.
\]
Consequently the schedule-dependent cost becomes
\(\int(BV-\gamma K^2P+c_S\alpha)\,dt\).

Let the deterministic adjoint \(Z\) solve
\[
 -\dot Z=2AZ+B,\qquad Z(T)=0.
\]
Multiplying the \(V\) equation by \(Z\), integrating by parts, and using the terminal condition yields
\[
 \int_0^T BV\,dt
 =Z(0)P_0+\int_0^T Z(2gP+\sigma^2)\,dt.
\]
Thus the entire deterministic sender problem is exactly, up to a known schedule-independent constant,
\[
 \min_{0\le\alpha\le\bar h^2}
 \int_0^T\{\chi(t)P(t)+c_S\alpha(t)\}\,dt,
 \qquad
 \dot P=2aP+\sigma^2-\alpha P^2,
\]
where \(\chi=2gZ-\gamma K^2\). This eliminates \(S\) without approximation or a stationarity assumption. It also checks the control-cost variance term: replacing \(S\) by \(P+S\) in the source objective would give a different \(\chi\).

An immediate consequence is that more sensing need not always benefit the sender. The coefficient \(\chi\) need not be nonnegative. If the sender penalizes only control effort, \(q_S=0\), with \(b\ne0,r_S>0\), then near \(T\), \(K=q_R(T-t)+O((T-t)^2)\), while \(Z=O((T-t)^3)\). Therefore
\[
 \chi=-\gamma q_R^2(T-t)^2+O((T-t)^3)<0
\]
sufficiently close to \(T\). This is an internal check on any proposed blanket “maximum information is optimal” rule.

There are also exact endpoint cases. If \(r_S=0\), then \(\chi=2gZ\ge0\). With free sensing, \(c_S=0\), scalar comparison of the variance Riccati equation shows that \(\alpha=\bar h^2\) minimizes \(P\) pointwise and hence is optimal. If the sender's state and control weights are proportional to the receiver's, \(q_S=\eta q_R,\ r_S=\eta r_R\), then the Riccati equation implies \(Z=\eta K\), and
\(\chi=\eta b^2K^2/r_R\ge0\). Again free maximum sensing is optimal, irrespective of differences in the deterministic target terms. These statements concern weak optimality and do not assert uniqueness in degenerate cases.

For a candidate general schedule, let \(L(T)=0\) and
\[
 -\dot L=\chi+(2a-2\alpha P)L.
\]
Linearizing the scalar state equation and integrating by parts gives the first variation
\[
 \delta J=\int_0^T(c_S-LP^2)\,\delta\alpha\,dt.
\]
An optimal schedule must therefore choose maximum precision where \(LP^2>c_S\) and zero precision where \(LP^2<c_S\), almost everywhere; equality leaves possible singular intervals. This is a necessary certificate, not a proof that all optima are bang-bang or that singular cases are resolved.

Finally, the manuscript's attainment proof survives this reduction: bounded states are equicontinuous, bounded controls have a weak-star subsequence, and uniform convergence of \(P\) makes the product \(\alpha P^2\) pass to the limit. The square-root implementation is measurable. None of the reduction or first-variation calculations proves control-independent posterior variance for feedback devices. The source's upper-bound direction for the full sender infimum is therefore retained.
