# Optimal history-dependent completion validation minimizes the fertility-score variance

The source's Representative completion validation proposition correctly gives inverse-collection and augmented unbiased scores. A substantive design question is how to allocate expensive follow-up across observed early histories. In an oracle benchmark the optimal allocation has a closed form.

Fix one randomized arm and write H for its early history, R for remaining births, m(H)=E[R|H], and σ²(H)=Var(R|H). Assume square integrability, 0<σ(H)<∞ almost surely and positive collection cost c(H). Choose follow-up probability π(H)∈(0,1] independently of R conditional on H. The augmented score is
ψ=m(H)+V[R−m(H)]/π(H).
Its mean is E R, and its exact variance is
Var(ψ)=Var(m(H))+E[σ²(H)/π(H)].
Conditional on H the residual term has mean zero and variance σ²(H)/π(H); total variance proves the formula. Thus concentrating validation only on predictable histories can be inefficient even if their early fertility is highly informative.

Impose an expected collection budget E[c(H)π(H)]≤B with 0<B<E c(H), and assume the displayed expectations and multiplier solution below exist. The variance-minimizing allocation is
π*(H)=min{1, σ(H)/√[λc(H)]},
where λ>0 is chosen so E[c(H)π*(H)]=B.
For example, bounded positive costs and bounded positive conditional standard deviations guarantee a solution by continuity: expected cost tends to E c as λ↓0 and to zero as λ↑∞. The budget function is nonincreasing, and any plateau in its capped part does not affect the allocation.

To verify optimality, minimize σ²/π+λcπ pointwise over 0<π≤1. Its derivative is −σ²/π²+λc and its second derivative is 2σ²/π³>0, giving the stated cap. For any other budget-feasible π, pointwise optimality and integration give
E[σ²/π*]+λB≤E[σ²/π]+λE[cπ]≤E[σ²/π]+λB.
Canceling the budget term proves global minimality. Strict convexity gives uniqueness up to null sets when σ>0. The component Var(m(H)) is unaffected by collection allocation.

At equal costs and away from the cap, follow-up probability is proportional to conditional standard deviation, rather than remaining-birth mean or early parity alone. A stratum with four times the conditional variance gets twice the collection probability. At very high budgets, low-cost/high-uncertainty histories saturate at complete follow-up while the other probabilities continue adjusting.

This oracle theorem does not make m and σ known from early histories alone. A practical allocation would estimate them using separate validation data or a justified adaptive design and account for that estimation. Reusing outcome-dependent collection without conditional independence invalidates the original score. Zero-variance histories can be treated separately when their conditional mean is genuinely known; a positive-probability floor may still be required for model robustness.

The result optimizes precision of each arm's completion mean, not the fiscal ratio near a zero completed-fertility effect. The source's ratio nonprecision remains: efficient follow-up cannot create positive separation that the true effect lacks.

Source: [ECON-J13-560-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/9d/prb_9d41e9e50d2d4a9baf7a5a6341a609b1/contributions/con_4da6b2b20a614d7b8fe3ae272baba544/files/J13-560.tex), canonical revision `rev_f016e9fe992e41d8a53b4f3bd9b785ca`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
