# Exact joint identified set after transforming household gains

Finding: **Supports the claim** for the small-open-economy project model in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/9d/prb_9d21d13ae6df4719bbbdad975e08070f/contributions/con_4ec5cb0f01064b77a51ca3fce6332e96/files/F12-161.tex). I checked the optimizer, both profit branches including $B=0$, consumption-equivalent exponent, scalar sharp bounds, and effort-only inversion. The metadata calls the contribution an unresolved exploration, and the manuscript expressly excludes endogenous prices and other general-equilibrium channels. Those restrictions are not hidden gaps in its stated identified-set theorem.

The marginal bounds are correct, but the manuscript's warning about dependence between household gains permits a more explicit exact characterization. For each firm, let $[\pi_i^-,\pi_i^+]$ be its lower and upper profit bounds from the source. Every profit in this interval is attainable. Indeed, interpolate its primitives $(a_i,B_i)$ between their lower and upper corners. The source's continuous profit function maps this path continuously from $\pi_i^-$ to $\pi_i^+$, so the intermediate value theorem applies. Because the primitive restrictions are independent across firms, every vector in

$$
 \Pi=\prod_i[\pi_i^-,\pi_i^+]
$$

is simultaneously attainable, not just each coordinate separately.

Set $\kappa_h=\beta_h(1-\beta_h)>0$ and transform a candidate gain vector by

$$
 y_h=e_h\left[(1+g_h)^{1/\kappa_h}-1\right].
$$

This transformation is increasing and invertible for $g_h>-1$. The exact joint identified set is then characterized by the finite linear feasibility problem

$$
 y_h=\sum_i\alpha_{hi}\pi_i\quad\text{for all }h,
 \qquad \pi_i^-\leq\pi_i\leq\pi_i^+.
$$

Necessity follows by rearranging the manuscript's consumption-equivalent formula. Sufficiency follows from the simultaneous profit attainability just proved, followed by the inverse household transformation. Thus in transformed coordinates the joint set is a linear image of a box, often called a zonotope; the nonlinear household gain set need not itself be convex. This is a computationally explicit refinement of the source's image-set description, not a correction to its valid marginal intervals.

The characterization also supplies exact support certificates. For any vector $v\in\mathbb R^H$, define $t_i=\sum_hv_h\alpha_{hi}$. Then

$$
 \max_{y\in\alpha\Pi}v\cdot y
 =\sum_i
 \begin{cases}t_i\pi_i^+,&t_i\geq0,\\t_i\pi_i^-,&t_i<0.
 \end{cases}
$$

Each firm's endpoint can be selected independently according to the sign of its coefficient. This proves every displayed support bound sharply, and a violation rules out a proposed joint gain vector even if each of its coordinates lies within its marginal interval. With one firm and two households owning positive shares, for example, $y_1/\alpha_{11}=y_2/\alpha_{21}$ must hold. A lower transformed gain for one household cannot coexist with a strict upper transformed gain for the other unless the profit interval degenerates.

There is also a useful distinction between the source's effort-only observation and a richer active-policy observation. Suppose an opened-market intervention reveals both effort $z>0$ and net project profit $\pi$, with known $k$, while prices and primitives are held fixed as assumed. Accounting alone identifies

$$
 a=\frac{\pi+kz^2/2}{z}.
$$

If the spending cap was unknown, optimality further implies $a\geq kz$. If $a>kz$, the objective is still increasing at the observed effort, so the cap must bind and $B=kz^2/2$. If $a=kz$, any $B\geq kz^2/2$ is compatible; a cap exactly at the unconstrained optimum cannot be distinguished from slack finance by this one observation. If $a<kz$, the observation contradicts the declared optimization model. At $z=0$, division is unavailable and the zero-cap observational obstruction persists. This does not refute the source's nonidentification result, which intentionally observes only effort in that proposition; it specifies which additional measurement removes its return ambiguity.

Finally, the exponent in the source's gain formula follows from the actual horizon convention. The innovation increases utility only at date one by $\beta_h\log(1+\sum_i\alpha_{hi}\pi_i/e_h)$. Scaling every baseline consumption date by $1+g_h$ increases utility by $\log(1+g_h)/(1-\beta_h)$. Equating them yields $\kappa_h=\beta_h(1-\beta_h)$, rather than either factor alone. Nonnegative project profits and voluntary participation explain the nonnegative gains within this model, while the source correctly does not transport that sign claim to tariff revenue, unemployment, or endogenous-price economies. No result here identifies primitive interval restrictions from baseline fit alone or solves the full trade-gains problem.
