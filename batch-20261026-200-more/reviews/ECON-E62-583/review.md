# Credibility revisions under stable risk adjustment

The source proves that a single bond price does not identify the physical implementation probability without risk-kernel restrictions. Two prices can nevertheless identify the direction of a credibility revision if the relative state pricing kernel is stable. Their exact joint restriction also bounds how large that revision can be.

For two communication regimes \(j=0,1\), recover risk-adjusted probabilities \(q_j\in(0,1)\) from the source's bond-pricing equation, using the corresponding known loss and risk-free rate. Suppose the positive conditional pricing-kernel ratio
\[
r=\frac{E[m_j\mid S=1]}{E[m_j\mid S=0]}
\]
is common across the two regimes. Its overall level may change consistently with each risk-free price. Define odds \(o_j=q_j/(1-q_j)>0\). The source's odds equation gives
\[
p_j(r)=\frac{o_j}{r+o_j}.
\tag{A}
\]
Thus the joint credibility set is this one-parameter curve. Independent choices from two marginal credibility intervals generally violate the common-\(r\) restriction.

Assume first \(q_1>q_0\), so \(o_1>o_0\). Their probability difference is
\[
\Delta p(r)=
\frac{r(o_1-o_0)}{(r+o_1)(r+o_0)}>0.
\tag{B}
\]
Hence a positive price-implied \(q\) revision identifies a positive physical credibility revision under stable relative risk adjustment, even when neither level is point identified.

Differentiation gives
\[
\Delta p'(r)=
\frac{(o_1-o_0)(o_0o_1-r^2)}
     {(r+o_1)^2(r+o_0)^2}.
\]
It increases up to \(r_*=\sqrt{o_0o_1}\) and decreases thereafter. Therefore, with no magnitude restriction beyond \(r>0\), the exact change set is
\[
\Delta p\in\left(
0,\frac{\sqrt{o_1}-\sqrt{o_0}}
        {\sqrt{o_1}+\sqrt{o_0}}
\right].
\tag{C}
\]
The maximum is attained at \(r_*\). The zero lower endpoint is approached as \(r\downarrow0\) or \(r\uparrow\infty\), but is not attained by a finite positive kernel ratio. Continuity on each side of the maximum proves that every intermediate value is attained.

If external information supplies \(r\in[\ell,u]\subset(0,\infty)\), both endpoints become attained. The minimum change is the smaller of \(\Delta p(\ell),\Delta p(u)\); the maximum is \(\Delta p\) at \(r_*\) clipped to that interval. Evaluating only adverse level endpoints would miss this interior maximum.

Sharpness follows by using the source's positive two-state pricing kernel separately in each regime:
\[
m_j(1)=q_j/(R_{f,j}p_j),\qquad
m_j(0)=(1-q_j)/(R_{f,j}(1-p_j)).
\]
Substitution of (A) gives state ratio exactly \(r\) in both regimes. These kernels reproduce both bond and risk-free prices, so the entire curve consists of admissible economies.

For \(q_0=1/5,q_1=4/5\), odds are \(1/4,4\), so \(r_*=1\) and the sharp maximum change is \(3/5\). The same price revision can correspond to an arbitrarily small positive physical revision if the unrestricted common ratio is extreme. If the two \(q\)'s coincide, the physical probabilities coincide; if their order reverses, interchange the regimes and negate the resulting interval.

Stable relative risk adjustment is a substantive exclusion: communication can itself alter state-contingent marginal valuations. Without it, the source's separate arbitrary-kernel constructions allow either sign. This result does not infer stability from randomized messages, identify actual implementation beliefs, or combine the pricing sector with the household saving model into a general equilibrium.

Source: [ECON-E62-583-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/46/prb_46e4ff9c0827475c94bd52adde684892/contributions/con_49c7e6d5033243ec9af0fa89d0bf0392/files/E62-583.tex), canonical revision `rev_271d8a5b2583492bb83dea9b6a8b6789`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
