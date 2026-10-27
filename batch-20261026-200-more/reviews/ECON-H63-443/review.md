# Joint reserves and maturity: the cheapest-insurance frontier

The manuscript explicitly notes that joint reserve optimization requires a carrying cost. Adding a linear real carrying cost yields a complete two-instrument solution. It exposes a sharp substitution frontier: with identical liquidity effects, the cheaper instrument supplies all insurance unless their marginal costs coincide.

Keep the source's proceeds requirement \(B>0\), event probability \(p>0\), disruption coefficient \(c>0\), and long-maturity premium \(\tau>0\). Let \(u=mB\in[0,B]\) be long-maturity proceeds. Choose reserves \(R\ge0\) at positive carrying cost \(\zeta R\), \(\zeta>0\), measured in the same numeraire as the source objective. The joint cost is
\[
J(u,R)=\tau u+\zeta R+\frac{pc}{2}[B-u-R]_+^2.
\tag{A}
\]
The carrying cost is stipulated as a real net financing cost, not the reserve principal counted as a loss. If reserve financing has another liquidity effect, equation (A) must be changed.

No optimum has \(u+R>B\): reduce a positive instrument until total coverage equals \(B\), preserving zero disruption while strictly lowering cost. Thus put \(y=u+R\in[0,B]\). At a fixed \(y\), the least linear cost is \(hy\), where \(h=\min(\tau,\zeta)\). If \(\tau<\zeta\), the unique minimizing split is \((u,R)=(y,0)\); if \(\zeta<\tau\), it is \((0,y)\); if they are equal, every nonnegative split with sum \(y\) minimizes cost. The bound \(u\le B\) never obstructs these splits.

The remaining scalar objective is
\[
hy+\frac{pc}{2}(B-y)^2,\qquad 0\le y\le B.
\]
It is strictly convex and has unique total coverage
\[
y^*=\left[B-\frac{h}{pc}\right]_+.
\tag{B}
\]
Since \(h>0\), coverage is strictly below \(B\). All joint optima are exactly the cheapest splits of (B). In particular all-short borrowing with zero reserves is uniquely optimal when \(h\ge pcB\). When costs tie below that threshold, there is a whole line segment of equally good maturity-reserve combinations, even though total uncovered exposure is unique.

The minimum cost is
\[
J^*=
\begin{cases}
pcB^2/2,&h\ge pcB,\\
hB-h^2/(2pc),&0<h<pcB.
\end{cases}
\tag{C}
\]
The formulas agree at the threshold, and their first derivatives in \(h\) agree there as well. Below the threshold the derivative is \(B-h/(pc)=y^*\), as the envelope theorem predicts.

For a concrete comparison using the source's illustrative \(B=100\), \(p=0.1\), \(c=0.01\), \(\tau=0.02\), take reserve carrying cost \(\zeta=0.01\). Then \(h=0.01\), total coverage is ninety, and the unique optimum is all-short funding with reserves \(R=90\). Carrying cost is \(0.9\), expected disruption loss is \(0.05\), and total cost is \(0.95\). If instead \(\zeta=0.03\), long maturity is cheaper: \(u=80\), reserves zero, and total cost is \(1.8\). These are deductions from supplied hypothetical costs, not estimates of reserve policy.

The source's fixed-reserve rule shows reserves displacing long funding unit for unit locally. Joint choice adds a selection margin: changes in relative marginal costs can replace one instrument entirely by the other. Smooth coexistence would require additional curvature or distinct insurance effects.

This extension retains exogenous liquidity risk and premium, and rules out default exactly as the initial benchmark does. It does not solve the endogenous bond-pricing multiplicity shown later in the manuscript. Reserve safety, sterilization, fiscal feasibility and confidence effects must be modeled before using the frontier empirically.

Source: [ECON-H63-443-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/18/prb_18ae4f6977e44f4a841c4e9ab56ea58d/contributions/con_46e077ae8dd14ed6b938b5fbabf71ae0/files/H63-443.tex), canonical revision `rev_755f2f721b1e402c8cc3a040dd78bfdd`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
