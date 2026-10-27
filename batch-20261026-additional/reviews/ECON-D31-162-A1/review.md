# A sharp factor-one Wasserstein certificate for top wealth shares

Finding: **Supports the claim**, with an independently proved improvement of its error constants, for the nonnegative-wealth framework in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/32/prb_32858f003027452fb9e61b6bea35b03a/contributions/con_6e1ca7ed185f426792e5c13972a0319d/files/D31-162.tex). I checked the observational-equivalence example, top-share bound, transition coupling, and permutation-average accounting. The metadata calls this an unresolved exploration; identification of structural interventions and general equilibrium is not asserted by its conditional propagation theorem.

The manuscript proves $ |S_p(F)-S_p(G)|\leq2W_1(F,G)/m$ for nonnegative laws whose means are at least $m>0$. Its bound is valid but the coefficient two can be replaced by one under exactly those assumptions. This halves the downstream constants and is sharp uniformly over the stated class.

Write the upper- and lower-population wealth amounts as

$$
 a=A_p(F),\quad c=\mu_F-a,\qquad
 b=A_p(G),\quad d=\mu_G-b.
$$

All four numbers are nonnegative. Splitting the quantile integral into the two disjoint intervals gives

$$
 |a-b|+|c-d|\leq W_1(F,G).
$$

Let $s=S_p(G)=b/\mu_G\in[0,1]$. An exact algebraic rearrangement, rather than separately bounding numerator and denominator errors, is

$$
 S_p(F)-S_p(G)
 =\frac{(1-s)(a-b)-s(c-d)}{\mu_F}.
$$

Therefore

$$
 |S_p(F)-S_p(G)|
 \leq\frac{(1-s)|a-b|+s|c-d|}{\mu_F}
 \leq\frac{W_1(F,G)}{\mu_F}
 \leq\frac{W_1(F,G)}m.
$$

No continuity of the distributions or fixed identity of rich households is required. The same fractional treatment of cutoff atoms as in the manuscript is built into the quantile integrals. Interchanging the roles of the laws also gives denominator $\max\{\mu_F,\mu_G\}$ if their actual means are available.

To verify sharpness of the uniform coefficient one, fix any $p\in(0,1)$. Let $F$ put mass $1-p$ at zero and mass $p$ at $m/p$. Let $G_\varepsilon$ move only the lower atom to $\varepsilon\in(0,m/p)$. Then

$$
 \mu_F=m,\quad \mu_{G_\varepsilon}=m+(1-p)\varepsilon,
 \quad W_1(F,G_\varepsilon)=(1-p)\varepsilon,
$$

and the top shares are $1$ and $m/[m+(1-p)\varepsilon]$. Hence

$$
 \frac{|S_p(F)-S_p(G_\varepsilon)|}{W_1(F,G_\varepsilon)/m}
 =\frac{m}{m+(1-p)\varepsilon}\longrightarrow1.
$$

Thus no smaller constant works uniformly when the only denominator information is the common lower bound $m$. This example also shows why fractionally allocating atoms is convenient: the statement remains exact with only two wealth levels.

The manuscript's transition coupling recursion itself is sound. Coupling the current wealth laws by a common quantile and using the same independent shock gives

$$
 W_1(F_{t+1},\widetilde F_{t+1})
 \leq(L_t+K_t)W_1(F_t,\widetilde F_t)+\epsilon_t.
$$

The approximation bound is evaluated at the approximate input, while the exact-transition Lipschitz condition compares the exact and approximate inputs; no Lipschitz assumption on the approximate map is needed. Thus its $D_t$ recursion remains unchanged, but the strengthened share estimate gives $ |S_p(F_t)-S_p(\widetilde F_t)|\leq D_t/m$. Each permutation-average marginal contribution is a difference of two subset values, so its approximation error is at most $2D_H/m$, improving the source's $4D_H/m$. These are uniform sufficient bounds; correlated subset errors can cancel further, and a contribution need not have the sign of any one removal effect.

The baseline counterexample is also internally consistent. Both models save zero at the observed return. After its removal, the high type in the capped-terminal-wealth model saves one, while the current-consumption model still saves zero. The resulting wealth pairs $(1,4)$ versus $(1,3)$ produce exactly the two claimed counterfactual shares. Zero postintervention current consumption is allowed by that example's linear utility and stated feasible set, so importing a log-utility positivity restriction would incorrectly invalidate it.

Finally, the nonnegative-wealth and positive-mean restrictions are essential to the sharpened proof, just as to the original one: the coefficients $s,1-s$ lie in $[0,1]$ because top and bottom wealth amounts are nonnegative. The refinement supplies no certificate for signed net wealth without additional controls. It also does not recover missing saving preferences or identify the counterfactual transition from the wealth identity. The improvement is a mathematical stability result within the source's declared model, without a novelty or complete open-problem-resolution claim.
