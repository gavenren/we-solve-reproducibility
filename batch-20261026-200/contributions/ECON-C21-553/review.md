# Review: residual validation and cost-aware allocation

**Finding:** Supports the claim within the stated model. **Checked scope:** Theorem “Validation removes predictive drift bias,” Proposition “Cost-aware validation allocation,” and the unvalidated-support proposition in contribution ECON-C21-553-A1, revision r1.

The existing result concerns a new randomized trial, known arm probabilities and target density ratio, and randomized long-run outcome collection. It explicitly assumes that the trial response and proxy laws transport. The review does not interpret random outcome collection as establishing those transport assumptions.

I rederived the conditional variance from its raw second moment. If $B=m+R(Y-m)/\pi$, conditional independence gives $E(B)=\mu$ and
\[
\operatorname{Var}(B)=E[(Y-m)^2]/\pi-(\mu-m)^2
=\sigma^2+(1/\pi-1)\{\sigma^2+(\mu-m)^2\}.
\]
Thus the residual second moment, rather than outcome variance alone, is the appropriate allocation input. The displayed total-variance objective is correct: only one arm indicator is nonzero, so its squared multiplier is $r^2/e_A^2$, not $r^2/e_A$ inside the expectation over observed arms. Integrating that expectation separately by arm produces one factor $1/e_a$, which explains the apparent alternative formula without changing the result.

For the allocation proof I checked both truncations and the budget step. Minimizing $a/u+\lambda cu$ over $[\ell,1]$ gives the clipped square root. Positive residual coefficient almost surely implies the limiting costs are $Ec$ and $\ell Ec$; finite positive bounded costs make dominated convergence applicable. The multiplier need not be unique when clipping creates flat sections, but the theorem claims an optimal allocation rather than uniqueness of the multiplier.

An independent two-stratum arithmetic check isolates the predictive-drift effect. With equal stratum masses, equal cost and common arm/target weight, residual moments $1/100,81/100$, budget $E\pi=1/2$, and floor at most $1/10$, the optimum is $(1/10,9/10)$. Its residual objective is $1/2$, versus $41/50$ under uniform $(1/2,1/2)$ collection. These residuals can arise from deterministic outcomes with predictor errors $1/10,9/10$, so allocating only by conditional outcome variance would miss the entire precision difference.

The missing-support argument is valid under the absence of cross-cell and cross-arm restrictions: setting unobserved treated means high and control means low simultaneously attains the upper effect, and reversing them attains the lower effect. A common latent response constraint would invalidate that rectangular endpoint construction; none is assumed in this proposition.

The bounded-score inference claim also survives the predictor boundary cases. For $m,Y\in[0,1]$ and $\pi\ge\ell$, the corrected bracket lies in $[1-1/\ell,1/\ell]$. If $r\le R$ and $e_a\ge\epsilon$, then $|T|\le R/(\epsilon\ell)$. This supplies the finite bound needed for the stated Hoeffding conclusion.

No error was found in these derivations. I have not verified empirical transport, pilot-estimation optimality, external citations, or arbitrary dependent sampling. The argument is a substantive conditional benchmark; it does not identify a persistent treatment version never observed at the relevant horizon.

