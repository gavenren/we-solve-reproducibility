# Partial personalization can trigger a discontinuous monopoly-price jump

The source explains that an individual randomized experiment inside one market identifies outcomes at mixed-regime prices rather than the two endpoint equilibria. Its explicit search model permits solving those mixed prices exactly. The result is stronger than a smooth interpolation: at a critical rollout share the seller's optimal price jumps.

Retain the source's two sellers, equal type shares, preferred value HZ, other value LZ, uniform Z, zero inspection cost, hard one-inspection attention constraint, and 2L<H<3L. Independently assign fraction α∈[0,1] of users to personalized ranking and the rest to the common randomized top listing. Assignment is independent of type and Z. Sellers choose one uniform price before displays, as in the source.

Each seller is inspected by preferred users of mass (1+α)/4 and nonpreferred users of mass (1−α)/4. Its demand is

D_α(p)=(1+α)(1−p/H)_+/4+(1−α)(1−p/L)_+/4.

On the low-price interval p≤L, revenue is a concave quadratic whose unconstrained maximizer is

p_L(α)=HL/[H+L−α(H−L)].

Its value, when that maximizer lies in the interval, is HL/[4{H+L−α(H−L)}]. On p≥L the nonpreferred group is absent; since H>2L, that branch is uniquely maximized at p_H=H/2, with value H(1+α)/16. Prices above H yield zero.

Define α*=(3L−H)/(H−L), which lies strictly between zero and one. While the low optimum is feasible, subtracting the two maximal-revenue expressions has the sign of

4L−(1+α){H+L−α(H−L)}
=(α−1){(H−L)α+H−3L}.

Thus the low branch wins for α<α*, the high branch wins for α>α*, and both tie at α*. The low unconstrained optimum reaches L only at α=L/(H−L), which is strictly above α* because H>2L. Beyond that feasibility point the best low-price revenue is at L, while the high branch already strictly dominates it. This verifies global optimality over all price ranges rather than extrapolating the low quadratic outside its domain.

The resulting price correspondence is unique at p_L(α) below α*, unique at H/2 above α*, and has exactly these two optimal prices at α*. A seller's demand does not depend on its rival's price, so these choices give the pure-price equilibrium correspondence. If mixed pricing is allowed, at α* each seller may independently mix arbitrarily over the two revenue-maximizing prices. At α* the two-price jump is strict:

p_L(α*)=HL/[2(H−L)]<H/2.

The discontinuity is a change in the seller's preferred customer segment; no new search information or seller quality is introduced.

For any α>α*, common prices equal H/2>L. A personalized user always inspects the preferred seller and has expected surplus (H−H/2)²/(2H)=H/8. A control user inspects the preferred seller only half the time; the inferior listing never sells at that price, so control surplus is H/16. Consequently the within-market treatment-control surplus difference is H/16>0 even though the source proves that the fully personalized equilibrium has lower consumer surplus than the fully common equilibrium.

The total mixed-market surplus on this high-price branch is H(1+α)/16. That quantity and the positive user-level contrast answer distinct questions. At α* selecting between the two revenue-maximizing prices can itself change consumer surplus, so a complete empirical counterfactual must specify equilibrium selection there.

This exact rollout solution illustrates why scaling a user-level treatment effect to market-wide adoption can fail when sellers reoptimize. It remains conditional on the hard attention constraint, uniform values, zero costs and ranking independent of prices. Sequential search with substitution, entry, quality responses and real-platform monetary surplus identification remain unresolved. No external reference is independently certified by this review.

Source: [ECON-D83-459-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ee/prb_ee17d46c37154b64be52af7924f8158d/contributions/con_e6c927818b4f4033bdca0d9553c43841/files/D83-459.tex), canonical revision rev_1d9836a2bd104e99af22efe2c03e4fb4. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
