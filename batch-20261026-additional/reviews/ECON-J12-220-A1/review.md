# Convex-order extension of the fixed-cohort sorting bounds

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/e9/prb_e96fb0d8196f473dbfb5b997c030ef01/contributions/con_b29c0bc6a0914670a8f335a3c8b30de5/files/J12-220.tex), revision `rev_2b9513b96eb94bf5b665e9a26ea200b7`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim.** The source's mechanical variance bounds and behavioral nonidentification example are correct under their explicit fixed-cohort conventions. The contribution is recorded as an unresolved exploration; it does not claim to identify equilibrium marriage, fertility, or child outcomes. An independent extension below shows that the mechanical extrema hold in convex order, not just for variance, and consequently also bound the conventional household-income Gini when the common mean is positive.

Retain sorted earnings \(a_1\le\cdots\le a_n\), \(b_1\le\cdots\le b_n\), uniform household weights, and a common equivalence scale \(s>0\). The mean household income is fixed across permutations. For variance, expanding the square gives

\[
I(\pi)-I(\sigma)=\frac{2}{ns^2}
\sum_i a_i\{b_{\pi(i)}-b_{\sigma(i)}\},
\]

since both marginal sums of squares and the mean term cancel. The sign of each inversion-removing exchange then proves the manuscript's sharp extrema. This calculation relies on uniform weights and a common scale; neither can silently become match-dependent.

For a stronger mechanical statement, let \(\varphi\) be any convex real function on the relevant income interval. If \(x\le x'\) and \(y\le y'\), then

\[
\varphi(x+y)+\varphi(x'+y')
\ge\varphi(x+y')+\varphi(x'+y).
\tag{A}
\]

One proof compares \(\varphi(t+h)-\varphi(t)\) at \(t=x+y\) and \(t=x+y'\), with \(h=x'-x\ge0\): convexity makes this increment nondecreasing in \(t\). No differentiability assumption is required. Positive rescaling by \(s\) preserves the inequality.

Removing an inversion from an arbitrary assignment changes two discordantly paired earnings into concordant pairs. By (A), this weakly raises the sum of \(\varphi\) of household incomes. Repeating the exchanges reaches the assortative assignment. Conversely, swapping any concordant assigned pair weakly lowers that sum; repeatedly doing so reaches the reverse assignment. Therefore, simultaneously for every convex \(\varphi\),

\[
\frac1n\sum_i\varphi\left(\frac{a_i+b_{n+1-i}}s\right)
\le\frac1n\sum_i\varphi\left(\frac{a_i+b_{\pi(i)}}s\right)
\le\frac1n\sum_i\varphi\left(\frac{a_i+b_i}s\right).
\tag{B}
\]

All three distributions have the same mean, so (B) is a convex-order comparison. The square function recovers the manuscript's variance result. More generally it compares every convex fixed-mean dispersion functional of this separable form, without claiming the same conclusion for statistics whose mean or weighting changes with the policy.

To connect this order to the Gini used in the behavioral example, suppose incomes are nonnegative with common positive sum. Write their increasing order statistics as \(z_{(1)},\ldots,z_{(n)}\). The conventional equally weighted Gini is

\[
G(z)=\frac{\sum_{i,j}|z_i-z_j|}{2n\sum_i z_i}
=\frac{\sum_{i=1}^n(2i-n-1)z_{(i)}}{n\sum_i z_i}.
\tag{C}
\]

The numerator is symmetric and convex as a function of the income vector, being a sum of absolute differences. Equivalently, a mean-preserving spread increases it: moving income from a smaller component to a larger one weakly raises every relevant pairwise-difference sum. The same pairwise exchanges used for (B) make the concordant sum pair more spread out, and the discordant pair less spread out, with their pair total unchanged. Consequently assortative and reverse assignments also maximize and minimize (C), respectively. This extension concerns fixed earnings and equal weights, not the behavioral policy in the second part of the source.

The nonidentification construction survives a separate utility and income check. A woman maximizing \(wl-l^2/2\) chooses \(l=w\) for the nonnegative wages used in the example and earns \(w^2\). Diagonal wages one and \(\sqrt3\) therefore produce household incomes two and six in both economies, whose Gini from (C) is \(4/(2\cdot8)=1/4\). Under crossing, partner-independent wages yield incomes four and four. In the alternative economy, the crossed wages zero and three yield female earnings zero and nine; paired with the corresponding men, household incomes are three and ten. Their Gini is \(7/(2\cdot13)=7/26\), which exceeds \(1/4\) by \(1/52\). All changed primitives concern unobserved baseline matches, so identical observed baseline earnings do not distinguish the economies.

The matching policy restricts feasible edges to the displayed complete matching in each regime; it is not asserted to be the unregulated stable outcome of unchanged meeting opportunities. Low outside options make its matches acceptable, as specified. Thus the example establishes logical nonidentification under unrestricted off-match productivity rather than an empirical magnitude or a general claim about marriage-market interventions.

The review supports the manuscript and broadens its mechanical benchmark to convex order and the Gini. Random mixtures still describe expected within-cohort statistics, while deterministic permutations generate a finite attainable set. Changing singles, household scales, fertility, or the population of children changes the underlying comparison and is outside both the source theorem and the extension.
