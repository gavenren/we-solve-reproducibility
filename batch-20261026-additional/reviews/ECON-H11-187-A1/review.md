# Exact oversight requirements and the boundary of sequencing dominance

Finding: **Supports the claim**.

This review targets the complete [pinned H11-187 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/bc/prb_bcd9ea7b9cb248f597b56fba82aca2f5/contributions/con_35ce12d49f954d2dae1fbe4662cabc33/files/H11-187.tex), revision `rev_89e8220458f64a759094bc02b2dfafee`. I also checked the contribution metadata, which describes an unresolved exploration. The manuscript deliberately studies a game with zero repression, externally chosen oversight, fixed bonus scale, and a stronger interim appropriation safeguard than a terminal expected constraint. None of those acknowledged restrictions is an error. My assessment supports the game and safety theorem and derives an exact service-and-safety feasibility condition that clarifies what the theorem does and does not rank.

Backward induction gives unique actions because both relevant objectives are strictly concave. The politician chooses x=min{k,1/a}; the official then chooses e=w(1−x/k). The politician's objective contains no service term or dependence on the official's subsequent action, so no strategic feedback term is missing from that solution. Substitution gives Q=w(k−x)^2/k. In the saturated region k≤1/a, an increase in stock is appropriated completely and leaves service zero. Outside that region, differentiating Q yields w[1−1/(a²k²)]>0. The transition is continuous. These checks confirm the comparative statics across the threshold as well as within each smooth region.

An exact reform threshold is available directly from these expressions. For a positive appropriation cap r,

\[
x(k,a)\le r
\quad\Longleftrightarrow\quad
k\le r\ \text{or}\ a\ge 1/r.
\]

This separates safety achieved by a small stock from safety achieved by effective oversight. If a_0≥1/r, raising k cannot violate the cap at any intermediate stock. The interesting sequencing case therefore requires a_0<1/r. Baseline safety then forces k_0≤r; a capacity-first step is unsafe precisely when k_1>r. Endpoint safety forces the later accountability reform to reach a_1≥1/r. Equivalently, conditional on safe baseline and endpoint, the only unsafe capacity-first configuration is

\[
k_0\le r<k_1,\qquad a_0<1/r\le a_1.
\]

This is an independent necessary-and-sufficient characterization of the manuscript's minimum-expression test. It explains why observing baseline safety alone is insufficient: a low baseline stock can conceal oversight that would not constrain appropriation after expansion.

The same model also yields a quantitative service requirement. Fix a target q_*>0 and positive stock k. No finite a can deliver q_*≥wk, since x remains positive. If k>q_*/w, then service at least q_* is equivalent to

\[
a\ge
\frac{1}{k-\sqrt{kq_*/w}}.
\]

To prove this, positive service requires x=1/a<k. Taking the nonnegative square root of w(k−1/a)^2/k≥q_* gives k−1/a≥sqrt(kq_*/w), which is exactly the displayed condition. It also implies the required interior regime. Combining it with the safety criterion gives a complete feasibility certificate: use this service lower bound on a, and additionally impose a≥1/r if k>r. This calculation is within the manuscript's game and supplies a more informative oversight requirement than an ordinal statement that accountability increases service.

Safety dominance must nevertheless be kept separate from interim-service dominance. Both signs of the service comparison occur even when both reform orders are safe. With w=1, k_0=1, k_1=2, a_0=2, a_1=4 and r=1/2, every relevant state satisfies the cap. Capacity first gives interim service (2−1/2)^2/2=9/8, whereas accountability first gives (1−1/4)^2=9/16. Conversely, take k_0=1, k_1=11/10, a_0=1, a_1=10 and r=1. Both orders are again safe, but their interim services are 1/110 and 81/100, respectively. The common endpoint is identical in each comparison. Thus adding an interim-service objective can rank either order; the safeguard theorem alone cannot supply that ranking.

The numerical and rational calculations above were independently checked. The findings support the precise conditional safety result, rather than a universal prescription to implement accountability first. An empirical application would still need the independently measured accountability, repression, and implementation mechanisms the manuscript itself identifies as unresolved. Within the specified deterministic game, however, the extra feasibility conditions above make those boundaries mathematically explicit and reveal no defect in the stated equilibrium or sequencing proof.
