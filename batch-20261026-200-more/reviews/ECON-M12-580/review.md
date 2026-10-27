# The complete one-worker identified set for average within-firm binary quantiles

The source proves that one sampled worker per firm does not identify average within-firm quantiles, and gives two observationally equivalent examples. In the binary-earnings submodel, its exact identified set can be calculated for every observed mean and quantile level. The boundary is sometimes open, so merely reporting a closed interval would overstate attainment.

Let each firm have Bernoulli worker earnings with latent success probability p∈[0,1], and sample one worker independently within each randomly sampled firm. Infinite firms identify only μ=E[p], because the observed worker is Bernoulli with that mean. Fix q∈(0,1) and put t=1−q∈(0,1). Under the source's inverse-CDF convention, the firm's q-quantile is one exactly when p>t; at p=t it is zero. The target is therefore r=Pr(p>t).

If μ>t, the sharp set is

r∈[(μ−t)/(1−t),1].

Indeed μ=E[p]≤t(1−r)+r implies r≥(μ−t)/(1−t). Equality is attained by probability 1−r at p=t and probability r at p=1. The upper endpoint is attained by every firm having p=μ>t. Mixtures of these two latent mixing laws preserve μ and attain every intermediate target value. This also handles μ=1, where both endpoints equal one.

For 0<μ≤t, the sharp set is instead

r∈[0,μ/t).

The lower endpoint is attained by constant p=μ, which lies at or below the quantile threshold. If r>0 then E[p·1{p>t}]>tr, because the integrand p−t is strictly positive on a set of probability r. The remainder of the mean is nonnegative, so μ>tr and r<μ/t. Thus the upper endpoint is excluded, including r=1 when μ=t.

Every target strictly below that upper bound is attainable. For 0≤r≤μ, put mass r at p=1 and the remaining mass at p=(μ−r)/(1−r), which lies in [0,t]. For μ≤r<μ/t, put mass r at p=μ/r>t and the rest at p=0. The two constructions meet at r=μ and reproduce exactly the observed worker mean. At r=0 use the first construction directly. These formulas show full-interval sharpness without relying only on a limiting argument. When μ=0, nonnegativity forces p=0 almost surely and the target is exactly zero.

The upper supremum μ/t can be approached by placing the positive-probability firms just above t and assigning the rest p=0. Its nonattainment is caused by a discontinuous within-firm quantile functional; it is not sampling uncertainty. Weak compactness of mixing laws alone does not guarantee the target image is closed.

For the source's q=3/4 example, t=1/4 and μ=1/2. The full sharp interval is [1/3,1], not merely the two values one half and one shown by its illustrative models. The lower endpoint uses two thirds of firms at p=1/4 and one third at p=1. Their pooled worker mean is one half, but only the latter firms have the q-quantile equal to one.

In a randomized policy comparison, apply the sets arm by arm. With no cross-arm restrictions, any difference of admissible arm targets can be coupled across firms, preserving random assignment and both observed laws. Endpoint inclusion in the effect set follows the corresponding attainment in the two arms.

These are exact bounds in the one-worker Bernoulli-superpopulation model. They do not solve fixed-m identification for arbitrary earnings distributions, establish a real manager-policy effect, or replace complete baseline-worker follow-up. They sharpen the manuscript's measurement obstruction while preserving its causal and empirical limits.

Source: [ECON-M12-580-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/5a/prb_5a61d70bf1c34eb4a705b5471c5194f6/contributions/con_ede41c233a7e47baa2fca86f608adf6d/files/M12-580.tex), canonical revision rev_d3a935d6013941d0ae46907e9fff4dc4. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
