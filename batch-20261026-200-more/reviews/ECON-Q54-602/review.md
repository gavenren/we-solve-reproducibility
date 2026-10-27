# Weather-index insurance and overinsurance after adaptation

The manuscript proves monotone welfare gains from higher fair indemnity coverage, where payment and premium track the actual loss after adaptation. It explicitly notes that a fixed weather-index contract has a different incentive formula. That alternative can be solved exactly and shows why the monotonicity should not be transferred across contract types.

Keep true drought probability \(p\in(0,1)\), CARA parameter \(\rho>0\), loss \(L>0\), adaptation loss reduction \(d\in(0,L)\), and cost \(K>0\). Maintain correct beliefs and financial feasibility of both adoption choices. Replace the indemnity by a weather payment \(qLZ\), with actuarially fair premium \(qpL\), independent of whether the farmer adapts. Coverage satisfies \(q\in[0,1]\). Consumption becomes
\[
c(D,Z)=W-KD-qpL-\{L-dD-qL\}Z.
\tag{A}
\]
The source's \(W>K+L\) is sufficient to keep consumption positive throughout.

Extend its risk function to all real \(x\):
\[
\psi_p(x)=\rho^{-1}\log(1-p+pe^{\rho x}).
\]
The exponential moment is finite for every finite \(x\). The actual certainty equivalent is
\[
CE(D,q)=W-KD-qpL-\psi_p((1-q)L-dD).
\]
Thus adaptation is optimal, with the source's adoption-at-tie convention, exactly when
\[
K\le B_I(q):=
\psi_p((1-q)L)-\psi_p((1-q)L-d).
\tag{B}
\]
There is no premium-reduction term \(qpd\): the premium does not fall after adaptation.

Since \(\psi_p'\) is strictly increasing,
\[
B_I'(q)=-L\{\psi_p'((1-q)L)-\psi_p'((1-q)L-d)\}<0.
\]
At no insurance, this agrees with the source's uninsured threshold. At full index coverage,
\[
B_I(1)=-\psi_p(-d)<pd.
\tag{C}
\]
The strict inequality follows from strict Jensen convexity:
\(\psi_p(-d)>E[-dZ]=-pd\). Full index coverage therefore suppresses adaptation more strongly than full loss indemnity, whose threshold in the source is exactly \(pd\). For any \(K\) strictly between \(B_I(1)\) and \(pd\), full indemnity induces adoption while full index coverage does not.

The welfare difference is also exact. For a fixed decision \(D\),
\[
\partial_q CE(D,q)
=L\{\psi_p'(L-dD-qL)-p\}.
\tag{D}
\]
The derivative is positive when \(q<1-dD/L\), zero at equality, and negative above it, because \(\psi_p'(0)=p\). Without adaptation the optimum is full coverage. With adaptation the optimum is \(q_D=1-d/L<1\): higher coverage creates a net positive drought payoff and overinsures the reduced physical loss. Consequently further fair index coverage beyond that point lowers the adapted farmer's welfare. This is a contract-specific reversal of monotonicity, not an error in the source's indemnity theorem.

If coverage and adaptation can be chosen jointly, each decision uses
\[
q_D=(L-dD)/L.
\]
Residual drought risk then vanishes, and the optimized certainty equivalent is
\[
CE_D^*=W-KD-p(L-dD).
\]
The joint optimum adopts exactly when \(K\le pd\), with equal values at equality. Thus freely adjustable fair index coverage implements full hedging of the actual residual loss; forcing the same maximum coverage across farmers need not do so.

This extension assumes perfect alignment of the weather trigger with loss occurrence, known \(p\), no loading and adjustable coverage. Basis risk, liquidity constraints and insurer participation with hidden adaptation can alter the solution. It does not estimate an insurance effect or extrapolate a current trial to a new climate. It identifies a precise contract-design boundary already signaled by the manuscript.

Source: [ECON-Q54-602-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/90/prb_908b897637e24cc09279dc38fddba408/contributions/con_694a5274c4a2468ab1be10b5fde1f384/files/Q54-602.tex), canonical revision `rev_73ffae74c6904cef8283631803ddd3d3`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
