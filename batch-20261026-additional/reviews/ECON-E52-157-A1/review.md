# Sharp reward loss and necessary horizon dependence in the welfare certificate

Finding: **Supports the claim** for the finite equilibrium reduction actually assumed in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ee/prb_ee4b2b69c3bf40bd8e5c086cdfe59a6a/contributions/con_817bbea43010400b86bc598bebf6d1df/files/E52-157.tex). I checked the accounting derivative, two-action information bound, and backward-induction certificate. The contribution metadata and manuscript both describe an unresolved exploration. In particular, a nonanticipative equilibrium selector and common feasible action library are assumptions, not outcomes of this dynamic-programming proof.

The certificate's two comparisons are necessary: the full-state optimum must be compared with the representative optimum, and the implemented representative policy must separately be evaluated in the original state process. Each comparison incurs the same error recursion. For a bounded continuation value, the estimate is $2M\operatorname{TV}(p,q)$, using the manuscript's convention $\operatorname{TV}=\frac12\|p-q\|_1$. This verifies both the factor two in its transition term and the final triangle inequality. The nominal revaluation derivative likewise has the correct factor $-N_iP'/P^2=-N_i\pi'/P$; the zero sum of nominal positions does not remove their marginal-utility-weighted sum.

Two explicit finite models independently test the strength of the certificate. They show that the reward-error coefficient is sharp and quadratic undiscounted horizon dependence cannot generally be replaced by a linear one. These are models of the finite control theorem, not heterogeneous-agent monetary equilibria, and make no economic implementability claim beyond that theorem's stipulated data.

For reward error alone, take two persistent hidden states $x_0,x_1$ in one measured-state cell, with representative $x_0$, and two actions $A,B$. Both actions leave the actual state unchanged. Choose $0<\gamma<\epsilon_r$, and rewards

$$
 r(x_0,A)=\gamma,\quad r(x_0,B)=0,\qquad
 r(x_1,A)=\gamma-\epsilon_r,\quad r(x_1,B)=\epsilon_r.
$$

These satisfy the uniform within-cell reward restriction exactly and have zero transition error. All absolute rewards are at most $R=\epsilon_r$. The representative strictly prefers $A$, whereas at $x_1$ full information strictly prefers $B$. Starting from $x_1$, welfare regret over dates $0,\ldots,T$ is

$$
 (2\epsilon_r-\gamma)\sum_{t=0}^T\beta^t.
$$

Letting $\gamma\downarrow0$ shows that the coefficient $2$ multiplying accumulated reward error is unavoidable, even with deterministic transitions and strict representative action selection. This also rules out attributing the coefficient solely to a loose tie-breaking argument.

For transition error alone, take states $x_0,x_1,b$, with $x_0,x_1$ sharing a safe observation and $b$ having a distinct bad observation. Again $x_0$ is the safe-cell representative. At either safe state both actions have reward $R$; at $b$, reward is $-R$. The bad state is absorbing. At $x_0$, both actions remain at $x_0$. At $x_1$, action $B$ remains at $x_1$, while action $A$ moves to $b$ with probability $e\in(0,1)$ and otherwise remains at $x_1$. All within-cell rewards coincide, so $\epsilon_r=0$. The pushforward transition error is $e$ for action $A$ and zero for action $B$, exactly meeting $\epsilon_P=e$.

The representative is indifferent and may select $A$, which is an allowed optimal representative rule. Starting from $x_1$, the informed rule always choosing $B$ obtains $R(T+1)$ when $\beta=1$. The representative rule survives safely to date $t$ with probability $(1-e)^t$, so its exact regret is

$$
 2R\sum_{t=0}^T[1-(1-e)^t]
 =ReT(T+1)+O(Re^2T^3).
$$

The expansion applies, for example, as $e\to0$ with fixed $T$, or in the regime $eT\to0$ with the usual corresponding remainder control. Thus an $O(R\epsilon_PT^2)$ term is necessary in general. The source gives $2R\epsilon_PT(T+1)$, so this construction verifies the horizon order, not optimality of that particular numerical coefficient. It also demonstrates why comparisons of baseline transitions alone would be inadequate: the hidden state's action-$A$ hazard is precisely the missing policy-dependent information.

Neither construction disproves the source's theorem; both satisfy it and delimit possible uniform improvements. The log-utility exposure example is separately valid as a local allocation experiment: its common observations hide which household receives the redistribution, and the minimax randomization loss is exactly half the two-action welfare gap. The source carefully declines to call that experiment a complete sticky-price equilibrium. These distinctions support the restricted mathematical results while leaving equilibrium construction, discretization error, and empirical state sufficiency unresolved as stated.
