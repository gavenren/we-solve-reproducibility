# A finite certificate for the aggregate-comparator class

Finding: **Supports the claim** for the unconditional dominant-action and aggregate-comparator bounds in Sections 1–4 of the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/bc/prb_bc572aa70a8748a3b489fa9941f9307e/contributions/con_ab3b0c845f87450680ff7d3b4a226643/files/prb_bc572aa70a8748a3b489fa9941f9307e-attempt.tex). I read the full manuscript and metadata, including the quantitative recurrence argument and conditional real-exponential-field search. This review's positive verification is confined to those unconditional finite-class results; it does not certify the external analytic finite-generation theorem underlying Section 6. The metadata explicitly calls the general-game computation conditional and the full dimension-explicit question unresolved.

An independent finite reduction makes the aggregate-comparator hypothesis directly checkable. Let $a=(a_1,\ldots,a_N)$ range over pure profiles, and introduce probability variables $p_{ib}\geq0$, $\sum_b p_{ib}=1$. Consider the finite linear feasibility system

$$
 \sum_i\sum_b p_{ib}u_i(b,a_{-i})
 \geq\sum_i u_i(a)
 \qquad\text{for every pure profile }a.
$$

This system is necessary and sufficient for the manuscript's hypothesis

$$
 \sum_i[u_i(p_i,x_{-i})-u_i(x)]\geq0
 \quad\text{for every mixed profile }x.
$$

Necessity follows by taking $x=a$. Conversely, average each pure-profile inequality under the independent product distribution $\prod_jx_{ja_j}$. Its right side becomes $\sum_i u_i(x)$. For the term involving $i,b$, summing over $a_i$ contributes one, leaving exactly $p_{ib}u_i(b,x_{-i})$. Hence the averaged inequality is the desired condition. Every coefficient is a payoff-table entry; there is no product between comparator probability variables. The test is finite, though its number of rows is the number of pure profiles and no polynomial-size assertion follows.

This condition is substantially stronger than merely asking that $p$ be a Nash equilibrium. Indeed, if the condition holds, set $x=(y_j,p_{-j})$. Every player's comparison except $j$'s is zero, giving $u_j(p)\geq u_j(y_j,p_{-j})$, so $p$ must be Nash. The converse fails even in a two-action coordination game where both players receive one when their actions match and zero otherwise. At pure profile $(1,1)$, the finite condition requires $p_{11}+p_{21}\geq2$. At $(2,2)$, it requires $p_{12}+p_{22}\geq2$. Adding gives $2\geq4$, impossible. The game has Nash equilibria but no aggregate comparator. Thus the class restriction must not silently be extended to all games possessing an equilibrium.

The source's regret proof also admits a slightly stronger parameterized statement without changing its underlying argument. Write $L=\sum_i\log m_i$ and use its stability quantity $E_T$. Before relaxing the quadratic coefficient, the summed inequality is

$$
 0\leq\frac L\eta+\eta N
 -\frac{1-2\eta^2(N-1)^2}{4\eta}E_T.
$$

Whenever $0<\eta<1/[\sqrt2(N-1)]$, it therefore implies

$$
 E_T\leq\frac{4(L+\eta^2N)}{1-2\eta^2(N-1)^2},
$$

and the individual feedback inequality gives

$$
 R_i(T)\leq\frac{\log m_i}\eta+\eta
 +\frac{2\eta(N-1)(L+\eta^2N)}{1-2\eta^2(N-1)^2}.
$$

This broadens the allowed interval for a finite horizon-uniform constant, while displaying its divergence as the absorption denominator vanishes. At the manuscript's choice $\eta=1/[2(N-1)]$, the denominator is $1/2$ and the expression recovers its displayed bound. The source's simpler step restriction is therefore sufficient, not an alleged maximal stability threshold.

I checked two details that matter for this calculation. First, the aggregate hypothesis implies only $\sum_iR_i(T)\geq0$; individual external regrets can be negative, and the proof never needs to assume otherwise. Second, payoff variation under changing opponents is bounded by half the sum of their $\ell_1$ changes because payoffs lie in $[0,1]$. Omitting that half would change the absorption constants. The initialization $v^0=0$ also yields the source's exceptional first-round variation term $N$.

For weak dominance, the telescoped exponent has coefficient two on the previous payoff vector, as required by the exact update. The loss-gap comparison $x_a^t\leq e^\eta y_a^t$, followed by the exponential chord inequality on $[0,1]$, proves its horizon-uniform bound without a positive dominance gap. Its coefficient $e^\eta/(1-e^{-\eta})$ is minimized at $\eta=\log2$, where it equals four. The static-payoff lower-bound integral also uses the same initialization. These checks and the finite class certificate substantiate the stated special cases without promoting them to an unconditional general-game solution or asserting novelty over the literature already acknowledged by the author.
