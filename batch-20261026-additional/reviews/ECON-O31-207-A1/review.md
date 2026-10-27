# A sharp mean-variance characterization of the one-experiment learning value

Finding: **Supports the claim**.

Reviewed source: [ECON-O31-207-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/12/prb_128a758b24d147c1ac5e4e8a79751e28/contributions/con_71c3e0a2d1b04faab7033202a501066c/files/O31-207.tex), revision `rev_fb4555c5f1fd49a591a9b67da31ab4a4` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

The two-period information-value formula and the grant calculation are correct for the manuscript's fixed-effort, common-prior experiment. Its metadata calls the full problem unresolved, and the text explicitly excludes private project quality and adaptive multiperiod policy. This review independently characterizes exactly which priors can make the inferior current project socially preferable. The characterization uses only prior mean and variance because the experiment contains a single Bernoulli observation.

Write \(s=\mu_0\) for the safe success probability, \(\mu=E\Theta\), and \(v=\operatorname{Var}(\Theta)\). First take \(0<\mu<1\). Since
\(E\Theta^2=\mu^2+v\), Bayes' rule gives
\[
 \Pr(Y=1)=\mu,\qquad
 E(\Theta\mid Y=1)=\mu+v/\mu,
\]
\[
 \Pr(Y=0)=1-\mu,\qquad
 E(\Theta\mid Y=0)=\mu-v/(1-\mu).
\]
These identities hold for every prior on \([0,1]\), without requiring a two-point or beta prior. They directly reproduce the manuscript's posterior martingale property and quantify the crossing condition in its theorem.

If \(\mu<s\), the failure posterior is below \(s\), so only success can induce a switch to experimentation at the second date. Substitution into the source's information value yields
\[
 I=[v-\mu(s-\mu)]_+.
\]
If \(\mu>s\), only the failure posterior can induce a switch back to the safe project, giving
\[
 I=[v-(1-\mu)(\mu-s)]_+.
\]
At \(\mu=s\), either expression gives \(I=v\). When \(\mu=0\) or \(1\), the prior is degenerate and \(I=0\). This is an exact characterization of the source's \(I\), not an approximation based on small uncertainty. In particular, positive prior variance alone does not ensure positive information value: the posterior must be able to change the second-period decision.

Because \(0\le\Theta\le1\), \(v\le\mu(1-\mu)\). Consequently the sharp upper envelope over priors with a fixed mean is
\[
 I_{\max}(\mu,s)=
 \begin{cases}
 \mu(1-s),&\mu\le s,\\
 (1-\mu)s,&\mu\ge s.
 \end{cases}
\]
It is attained by the endpoint prior
\(\Pr(\Theta=1)=\mu,\Pr(\Theta=0)=1-\mu\), under which one experimental outcome reveals the permanent success probability exactly. The lower bound zero is attained by the degenerate prior \(\Theta=\mu\). All intermediate prior variances are feasible: mix the degenerate prior with the endpoint prior while preserving their common mean. Since the displayed information value is continuous and piecewise linear in \(v\), its entire interval from zero to the upper envelope is attainable.

For the important case \(\mu<s\), the experiment beats the better current project exactly when
\[
 \beta[v-\mu(s-\mu)]_+>s-\mu,
\]
or, equivalently,
\[
 v>(s-\mu)(\mu+1/\beta).
\]
This sharp threshold shows how much uncertainty is needed to compensate for the initial expected-output sacrifice. Moreover, there exists *some* prior on \([0,1]\) with this mean that makes experimentation strictly optimal exactly when
\[
 \beta\mu(1-s)>s-\mu
 \quad\Longleftrightarrow\quad
 \mu>\frac{s}{1+\beta(1-s)}.
\]
Equality permits at most indifference; below this threshold, no amount of admissible uncertainty can overturn the current ranking in this two-period model. Sufficiency is witnessed by the endpoint prior, and necessity follows from the variance bound. This provides a complete feasibility boundary for the manuscript's narrower learning mechanism.

The numerical example checks exactly. Its prior has \(\mu=1/2\) and \(v=(2/5)^2=4/25\). With \(s=3/5\), the formula gives
\(I=4/25-(1/2)(1/10)=11/100\). The social gain is therefore \(-1/10+(11/100)\beta\), positive precisely at \(\beta>10/11\), as stated. This calculation also demonstrates why the current success mean alone is inadequate: a degenerate prior with the same mean has \(I=0\) and reverses the policy conclusion.

The implementation part has a separate, correctly specified wedge. Under accurate verification the contractor's expected payoff difference is \(t-d\); under capture the experiment is not conducted. Hence \(t=d\), with the stated favorable tie-breaking rule, is the least implementing payment. Its real financing cost is \(\lambda d\) in both institutional states because the grant is paid in both. The source's net gain \((1-\rho)G-\rho L_{\mathrm{cap}}-\lambda d\) follows. The sharp information bound above can be inserted into that expression to rule out welfare-improving experimentation for some means even before addressing the budget or capture constraints.

The mean-variance reduction depends on one observed Bernoulli draw followed by one remaining decision. Multiple observations or private information can require higher prior moments and change selection. Accordingly, it does not remove the screening, endogenous effort, or dynamic-policy limitations acknowledged in the manuscript, and it supplies no general optimal innovation-policy claim.
