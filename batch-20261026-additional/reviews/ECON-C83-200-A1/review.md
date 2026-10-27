# Exact Bayesian lower bounds for the clique replication experiment

Finding: **Supports the claim**.

Reviewed source: [ECON-C83-200-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/41/prb_41f1ce07eec24d7686fcfea501a07f34/contributions/con_b4bfc7222aa846ed9cea9094db94e1d2/files/C83-200.tex), revision `rev_58b997f259254b6a88baf888b1ba7148` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

The declared scope matters here. The contribution metadata labels this an exploration and says the full problem is unresolved; the manuscript separately limits its matching rate to equal disjoint cliques and one representative-policy contrast. Within that scope, I find the replication rate supported. This review gives an independent finite-experiment lower bound with a stronger constant and an exact rare-exposure calculation. Neither result solves the arbitrary-overlap problem.

First, the upper-bound covariance calculation is valid even with heterogeneous outcome functions. Writing \(T_i=R_iY_i\), independent Bernoulli sampling gives
\[
 \operatorname{Var}(S_iT_i/\pi)=\pi^{-1}E T_i^2-(E T_i)^2,
 \quad
 \operatorname{Cov}(S_iT_i/\pi,S_jT_j/\pi)=\operatorname{Cov}(T_i,T_j).
\]
The second identity does not introduce a second inverse-sampling factor. Disjoint primitive neighborhoods imply independence of the two \(T\)'s; intersecting neighborhoods permit the stated Cauchy–Schwarz bound. The cancellation in \(v_i=E(L_i^1-L_i^0)^2\) is also essential: identical policies must give exactly zero risk. I found no missing sampling factor in equation (1).

For an independent lower bound, retain the manuscript's submodel \(Y_i=M W_c V_c\), but permit \(\theta=E V_c\) throughout \([-1,1]\), which the original bounded-outcome class allows. Put \(h=1-(1-\pi)^m\). Conditional on all assignments and sampling indicators, a clique contributes one Bernoulli sign observation precisely when its representative is treated and some outcome is sampled. Every other observation is parameter-free. Thus the entire statistical experiment is equivalent, for estimating \(M\theta\), to
\[
 T\sim\operatorname{Binomial}(K,h/2),\qquad
 V_1,\ldots,V_T\ \text{independent with }\Pr(V_j=1)=(1+\theta)/2,
\]
together with ancillary variables. This equivalence justifies a lower bound against estimators that use the full assignment record, rather than only an informal count of sampled nodes.

Give \(p=(1+\theta)/2\) the uniform prior on \([0,1]\). Conditional on \(T=t\) and \(k\) positive signs, the posterior is \(\operatorname{Beta}(k+1,t-k+1)\). Hence
\[
 \operatorname{Var}(\theta\mid t,k)
 =\frac{4(k+1)(t-k+1)}{(t+2)^2(t+3)}.
\]
The prior-predictive distribution of \(k\) is uniform on \(0,\ldots,t\). Summing the numerator gives
\[
 E\{\operatorname{Var}(\theta\mid T,k)\mid T=t\}
 =\frac{2}{3(t+2)}.
\]
Squared-error Bayes risk is expected posterior variance. Since minimax risk dominates every Bayes risk, the manuscript's minimax risk is at least
\[
 \frac{2M^2}{3}E\frac1{T+2}
 \ \ge\ \frac{4M^2}{3(Kh+4)}.
\]
The last inequality is Jensen's inequality, using \(ET=Kh/2\). With \(L=\min(n,K)\ge1\) and \(Kh\le L\), this yields the explicit rate bound \(4M^2/(15L)\). It independently confirms the claimed \(M^2/\min(n,K)\) law, without a testing reduction or a local restriction \(|\theta|\le1/2\). The larger prior is legitimate because it remains a subfamily of the stated model; it is not a claim that the manuscript's smaller two-point construction itself has this Bayes risk.

There is a similar exact strengthening of the rare-assignment obstruction. In its two deterministic sign models, the distinguishing event has probability
\[
 e=2^{-N}\{1-(1-\pi)^N\}.
\]
On this event the sign is observed perfectly. On its complement the complete records coincide under the two models. Under an equal prior on their targets \(-M,M\), the conditional variance is therefore zero on the distinguishing event and \(M^2\) otherwise. The two-point subexperiment has exact minimax risk \(M^2(1-e)\): the estimator reports the revealed target when possible and zero otherwise, attaining equal risk in both models. Consequently the full class has minimax risk at least this quantity. The manuscript's weaker half-sized bound is correct, not an error.

These checks distinguish two obstructions that cannot be summarized by nominal sample size. The clique experiment limits the number of independent sign replications even when within-clique sampling becomes dense. The rare-exposure experiment hides the policy-relevant response even with complete outcome sampling. Neither argument establishes simultaneous attainability of worst covariances on an arbitrary neighborhood-intersection graph. That is explicitly identified as unfinished in the manuscript and is not a defect in its restricted theorem.
