# Atom-safe verification and a continuum safety certificate

Finding: **Supports the claim** for the exogenous one-period real-resource model in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/70/prb_70b30886a9084ce18289d79fd8d0f072/contributions/con_b56e764ca74d413bbe188302864e7071/files/H63-150.tex). I checked the strict-loss event, endpoint convention, mean-only obstruction, bounded-support ambiguity frontier, sampling proposition, and separate welfare calculation. The metadata declares an unresolved exploration, and the manuscript explicitly excludes equilibrium refinancing and intermediate price losses. Their absence is not a gap in the restricted theorems.

The strict inequality is essential throughout. For $b>0$, $L(b)>\ell$ is exactly $R<(1-\ell)b$. The function $F_<(x)=P(R<x)$ is continuous from the left, so an increasing sequence of safe thresholds has a safe finite limit. This justifies inclusion of the supremum threshold $q_\alpha$, even at an atom. For example, masses $\alpha$ at zero and $1-\alpha$ at ten make ten safe and every larger threshold unsafe. Substituting a weak inequality in the loss event changes that conclusion incorrectly.

The bounded-support frontier can be checked by a pointwise moment certificate. For $0<x<M$ and $0\leq r\leq M$,

$$
 \mathbf1\{r<x\}\leq\frac{M-r}{M-x}.
$$

Taking expectations gives $P(R<x)\leq(M-\mu)/(M-x)$. The two-point laws at $r<x$ and $M$, with lower mass $(M-\mu)/(M-r)$, approach equality as $r\uparrow x$. For $x\leq\mu$, this proves both sides of the asserted supremum. At $x=0$ the event is empty, so its value is zero, rather than the positive right limit $(M-\mu)/M$. That discontinuity explains why nonpositive algebraic threshold formulas must be truncated at zero. At a positive robust boundary, using a supremum rather than an attained worst-case law is sufficient for safety: every law's probability is bounded by $\alpha$.

There is a useful distribution-free extension of the manuscript's fixed-grid certificate that handles a continuum of sample-selected thresholds without a grid penalty. It follows directly from a binomial count and preserves the strict-event convention. Let $R_{(k)}$ denote the $k$-th smallest of $N$ independent resource observations. Choose an index $k\in\{1,\ldots,N\}$ in advance satisfying

$$
 \sum_{j=0}^{k-1}{N\choose j}\alpha^j(1-\alpha)^{N-j}
 \leq\delta.
$$

Then the debt

$$
 \widehat b=R_{(k)}/(1-\ell)
$$

is safe with probability at least $1-\delta$, uniformly over resource laws, including laws with atoms. Every smaller nonnegative debt is simultaneously safe on that event. If no index satisfies the inequality, the procedure can return zero. This is a sufficient safety certificate, not an estimator with a guaranteed small capacity error.

Here is a proof that does not assume continuity of the resource distribution. Write $q=q_\alpha<\infty$. The manuscript proves $F_<(q)\leq\alpha$. Moreover $P(R\leq q)\geq\alpha$: otherwise continuity from above of the events $\{R<q+1/n\}$ would make some threshold greater than $q$ safe, contradicting its definition. Since the entire safe-threshold set is $[0,q]$, certificate failure can occur only when $R_{(k)}>q$. The number of observations at most $q$ is binomial with parameter $p=P(R\leq q)\geq\alpha$. Therefore

$$
 P(\widehat b\text{ is unsafe})
 =P(R_{(k)}>q)
 =P(\operatorname{Bin}(N,p)\leq k-1)
 \leq P(\operatorname{Bin}(N,\alpha)\leq k-1)
 \leq\delta.
$$

The binomial lower-tail probability decreases in $p$, as is seen by coupling Bernoulli trials using common uniforms. An infinite $q$, if allowed, makes the claim immediate. With a continuous strictly increasing distribution at its quantile, the binomial failure bound is exact, so atoms only make this particular certificate more conservative. For $N=100$, $\alpha=0.05$, and $\delta=0.05$, $k=2$ qualifies: the binomial lower tail is approximately $0.03708$, whereas $k=3$ does not qualify.

This extension also clarifies the original proposition's limitation. Its fixed-grid union bound is correct; a data-selected continuum requires a different proof, which the manuscript expressly says it has not provided. The order-statistic argument supplies one under precisely its independent-sampling and fixed-resource-law assumptions. It does not validate a policy-dependent resource law, estimate an ambiguity class, or identify the separate welfare benefit function.
