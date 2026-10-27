# Optimal randomized follow-up of leavers under a fieldwork budget

The source proves that randomized collection of leavers' outcomes identifies the full-cohort mean. Its collection probabilities can also be chosen optimally under a fieldwork budget. The relevant allocation depends on residual outcome variation, not merely on how many workers leave.

Work within one randomized location arm. Let X take finitely many strata with probabilities p_x, and let ℓ_x=Pr(L=0|X=x)>0 be the leaver share. Among leavers in stratum x, define μ_x=E[Y|X=x,L=0] and σ_x²=Var(Y|X=x,L=0). Assume bounded Y, σ_x>0 and known positive fieldwork costs c_x per collected outcome. Retained workers' outcomes are already observed. Randomized collection V is independent of Y given X and L=0, with probability π_x.

For any supplied numbers m_x, the score

Z=LY+(1−L){m_X+V(Y−m_X)/π_X}

has mean E[Y]. Conditional on the full record X,L,Y, collection expectation equals Y; integrate to obtain unbiasedness. The score is computable even when V=0 because its unobserved-outcome term is multiplied by zero. If m is independently trained, the same result holds conditionally on training.

Its collection-induced variance, by the law of total variance, is

Var(Z)=Var(Y)+∑_x p_xℓ_x E[(Y−m_x)²|X=x,L=0](1−π_x)/π_x.

The conditional variance is zero for retained workers and is (Y−m_x)²(1−π_x)/π_x for leavers. Choosing the oracle m_x=μ_x minimizes this expression stratum by stratum, replacing the second moment by σ_x². This is a variance design calculation; learning μ_x and σ_x is a separate pilot-estimation task.

Impose a positivity floor ε∈(0,1), and an expected fieldwork budget ∑p_xℓ_x c_xπ_x≤b, where ε∑p_xℓ_xc_x<b<∑p_xℓ_xc_x. Since every σ_x>0, the budget binds at the variance optimum. Ignoring additive constants, minimize ∑p_xℓ_xσ_x²/π_x over ε≤π_x≤1. Strict convexity gives a unique solution.

There is λ>0 such that

π_x*=min{1,max{ε,σ_x/sqrt(λc_x)}},

with λ chosen to exhaust the budget. To prove sufficiency directly, each π_x* minimizes σ_x²/π+λc_xπ on its interval. Multiply those pointwise inequalities by p_xℓ_x, sum, and cancel equal budget totals. Necessity follows from the interior derivative −σ_x²/π²+λc_x and the corresponding one-sided endpoint conditions. Continuity and the endpoint limits of total spending supply a clearing multiplier, though that multiplier need not be unique across corner plateaus.

Population and leaver shares determine the spending equation, while the within-stratum collection probability depends on standard deviation divided by the square root of cost. A rare stratum does not automatically deserve a smaller collection probability. Larger residual variation merits more follow-up, and expensive collection merits less, subject to guaranteed positivity.

If one instead uses the source's unaugmented inverse-probability score, the same optimization uses sqrt(E[Y²|leavers,x]) rather than σ_x. Residualization can therefore change both precision and where follow-up should be allocated. A constant nonzero outcome creates collection noise under raw weighting but none under the oracle residual score.

The result is conditional on independent randomized collection, defended stratum information and an expected fieldwork budget. It does not make employer exit ignorable, identify long-term careers without follow-up, or satisfy a hard realized survey budget automatically. Applying it across treatment arms requires the corresponding assignment and budget accounting. It supplies a practical design implication of the source's identification theorem without claiming actual remote-work effects.

Source: [ECON-J24-590-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/51/prb_51bf6f467c774a11b12ac68db5ad8c19/contributions/con_06075a1ca7ac4aabb795cc6406a96d39/files/J24-590.tex), canonical revision rev_4f1f0889c42a400f981a7d63c9dd8405. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
