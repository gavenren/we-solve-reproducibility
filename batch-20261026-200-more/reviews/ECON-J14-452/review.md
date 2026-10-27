# A sharp coupling certificate improves finite-cohort projection error bounds

The source's projection-error proposition bounds each transition perturbation separately. For nonnegative fiscal rewards, a coupling argument yields a sharper cumulative bound that saturates at probability one. Its transition component is attained by a two-state model with absorbing death.

Consider one true and one approximate finite-horizon regime with the same initial law. Let
\[
\sup_s\frac12\sum_{s'}|K_t(s,s')-\widehat K_t(s,s')|\le\delta_t\le1,
\]
and suppose \(0\le\widehat r_t(s)\le R\) for a finite \(R\), with \(\|r_t-\widehat r_t\|_\infty\le\epsilon_t\). Unlike the source's general signed-reward result, nonnegativity is an additional assumption here. Define
\[
q_0=0,\qquad q_t=1-\prod_{j=0}^{t-1}(1-\delta_j).
\]
Then
\[
|B-\widehat B|
\le\sum_{t=0}^H\beta^t\{\epsilon_t+Rq_t\}.
\]

To prove it, couple the initial states identically. Whenever the two chains currently agree at a state, use a maximal coupling of their next-state distributions. On a finite state space, the diagonal probability mass \(\min(K_t(s,j),\widehat K_t(s,j))\) sums to one minus their total-variation distance, so the chance of keeping agreement is at least \(1-\delta_t\). If the chains have already diverged, use any coupling. Induction shows that the chance they have ever diverged by time \(t\) is at most \(q_t\), and therefore their current disagreement probability is at most \(q_t\).

Split the expected reward difference at time \(t\) as
\[
\mathbb E[r_t(X_t)-\widehat r_t(\widehat X_t)]
=\mathbb E[r_t(X_t)-\widehat r_t(X_t)]
+\mathbb E[\widehat r_t(X_t)-\widehat r_t(\widehat X_t)].
\]
The first absolute value is at most \(\epsilon_t\). The second term vanishes when states agree and is at most \(R\) in magnitude when they differ, because both approximate rewards lie in \([0,R]\). Thus its absolute expectation is at most \(Rq_t\). Discount and sum to obtain the bound. No independence across dates or cross-world potential-outcome assumption is needed; coupling is a proof device comparing two specified laws.

The union bound gives \(q_t\le\min(1,\sum_{j<t}\delta_j)\). With the source's row-l1 errors \(\eta_j=2\delta_j\), the new transition bound is no larger than
\[
R\sum_{t=0}^H\beta^t\sum_{j<t}\eta_j/2.
\]
Reordering this finite sum gives exactly one half of its original transition-error expression for the nonnegative-reward subclass. The product formula improves further when perturbations accumulate substantially, because disagreement probability cannot grow without limit.

Sharpness of the product transition bound is explicit. Use states \(L\) (living) and \(\partial\) (dead), start in \(L\), and assign identical rewards \(R\) in \(L\) and zero at death in both models. Let the approximate chain remain living forever; let the true chain survive from \(L\) at date \(j\) with probability \(1-\delta_j\), with death absorbing. Their row total-variation difference is exactly \(\delta_j\), and their living probabilities at date \(t\) differ by exactly \(q_t\). Hence their discounted fiscal burdens differ by \(R\sum_t\beta^tq_t\), attaining the certificate with every \(\epsilon_t=0\).

If rewards can range from \(-R\) to \(R\), the disagreement term becomes \(2Rq_t\); the nonnegative improvement cannot be asserted without that restriction. The result certifies sensitivity to specified transition errors; it does not establish that an estimated kernel has those errors or that increased survival is a welfare loss.

Checked locations: finite-state projection, fiscal performance difference, and approximate-projection proposition. Full exact source/YAML were read. Empirical health kernels, causal survival interventions and external references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-J14-452-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/bc/prb_bc1ed7e9f973455b933361342585d325/contributions/con_388d1ef0177243d7bd3602690cdb7048/files/J14-452.tex). Canonical revision: `rev_a30e86eb8b694815a485994b5e3add69`.

