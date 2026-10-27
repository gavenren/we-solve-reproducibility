# A sharp intervention-strength and duration frontier for network exit

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/3c/prb_3c115f95cc604fd893ea850997c27499/contributions/con_cc0b8dadc4624cdfa926cc29d7d7e12c/files/D72-216.tex), revision `rev_7532a849331340768b529b9729cff97b`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim.** The withdrawal threshold, observational nonidentification example, and omitted-channel bounds are valid for the political game specified in the manuscript. The contribution is recorded as an unresolved exploration. Short-lived politicians and the absence of strategic network investment are explicit assumptions, so their omission from a broader political model is not a discovered error. An independent extension below weakens the manuscript's intervention-strength condition to the exact necessary condition for a given initial network and characterizes when any finite duration can work.

Let \(B_*=(b_0-Vm)/\eta\in(0,B_H)\) be the baseline threshold. Selected purchases satisfy \(C=1\{B>B_*\}\), with abstention at equality. When purchases occur, the next network stock is

\[
f(B)=\rho B+\iota=B_H-\rho(B_H-B).
\]

For \(B\in[0,B_H)\), \(f(B)>B\). Thus exchange itself raises the network toward \(B_H\), whereas no exchange multiplies the stock by \(\rho\). These opposing monotone dynamics explain the two absorbing regions. At the baseline threshold, the tie convention matters: \(B=B_*\) takes the depreciating branch and enters the low region, so the manuscript's permanent-exit condition correctly uses a weak inequality.

During an intervention with constant \(m'\), define its threshold

\[
B_*'=(b_0-Vm')/\eta.
\]

Suppose the intervention weakly suppresses the electoral return, \(m'\le m\), starts at \(B_{\rm init}\in(B_*,B_H]\), and lasts \(K\ge1\) periods. For this initial state the exact strength-and-duration criterion is

\[
\boxed{B_*'\ge B_{\rm init}\quad\text{and}\quad
\rho^K B_{\rm init}\le B_*.}
\tag{A}
\]

To prove sufficiency, the first inequality selects no purchase immediately. Depreciation only lowers the stock, so it remains at or below \(B_*'\) throughout the intervention. Its withdrawal level is \(\rho^K B_{\rm init}\). The second inequality places that stock in the permanently depreciating baseline region.

For necessity, suppose instead that \(B_*'<B_{\rm init}\). The first intervention-period purchase occurs, and the map \(f\) weakly increases the stock throughout \([B_{\rm init},B_H]\). Inductively every intervention period purchases and the stock never falls below its initial level. At withdrawal it therefore still exceeds \(B_*\), so baseline purchases continue forever. No increase in duration can remedy an intervention that fails this initial strength test. If the strength test does hold but the second inequality fails, the intervention suppresses all observed exchanges yet ends in the baseline high-exchange region, giving immediate permanent resumption. This proves both necessity statements.

The source assumes the stronger, initial-state-independent condition \(Vm'\le b_0-\eta B_H\), equivalently \(B_*'\ge B_H\). It guarantees suppression for every feasible initial stock. For a known lower initial stock, the sharp condition is only \(Vm'\le b_0-\eta B_{\rm init}\). Thus the manuscript's condition is sufficient as stated and is exactly sharp when the intervention starts at \(B_H\); it is deliberately conservative when the initial network is smaller.

Conditional on adequate strength, solving the second inequality in (A) yields

\[
K_{\min}=\left\lceil\frac{\log(B_*/B_{\rm init})}{\log\rho}\right\rceil.
\]

Both logarithms are negative, so the expression is positive and the inequality direction reverses on division. If network persistence is only known to satisfy \(\rho\le\overline\rho<1\), and the remaining thresholds and initial level are fixed, the worst-case duration uses \(\overline\rho\) in that formula. This follows directly because \(\rho^K B_{\rm init}\) increases with \(\rho\); uncertainty about intervention strength or the baseline threshold would need its own bounds.

The nonidentification example is also exact. With threshold \(1/2\), initial level one, and two fully suppressing periods, depreciation rates \(0.2\) and \(0.9\) produce withdrawal stocks \(0.04\) and \(0.81\). The observed purchase histories before and during treatment coincide, while their post-treatment histories differ forever. This conclusion requires no hidden substitution channel. Separately, if omitted baseline and policy intensities independently range over \([0,\bar u]\), their difference fills \([-\bar u,\bar u]\), including every interior point; adding the measured change gives the manuscript's sharp interval and its upper-endpoint guarantee.

These calculations support the local theorem and add an actionable distinction between insufficient duration and insufficient suppression strength. They do not establish that reducing exchanges improves public-good responsiveness, identify network depreciation from a short treatment panel, or accommodate a machine that invests strategically during suppression. Those are acknowledged boundaries of the source rather than failures of its proved threshold model.
