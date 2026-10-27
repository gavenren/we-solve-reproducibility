# Heterogeneous-bank allocation under a common sovereign feedback loop

The manuscript correctly solves its scalar exposure-cap problem by substituting the entire geometric feedback loop before differentiating welfare. A substantive extension is possible without adding an unmodeled fiscal mechanism: heterogeneous banks sharing that same aggregate loop admit an exact allocation characterized by one scalar fixed point. This shows which part of the scalar frontier survives heterogeneity and why a common exposure cap generally does not implement it.

Consider finitely many banks i=1,…,N, exposures e_i∈[0,b_i], and aggregate E=∑e_i. Give bank i surplus A_i e_i−ν_i e_i²/2, with A_i,ν_i>0. Suppose aggregate contraction satisfies ℓ=χEz/(1−kE), and retain the manuscript's crisis criterion. Write γ=ωχ²E[z²]>0. Assume k∑b_i<1, so all feasible allocations are stable. The social objective is

W(e)=∑(A_i e_i−ν_i e_i²/2)−D(E),
D(E)=γE²/(1−kE)².

The rational term is the same resolved feedback cost, evaluated at aggregate exposure. We do not assign separate independent sovereign shocks to banks or presume the scalar model already contains these heterogeneous primitives.

Since D''(E)=2γ(1+2kE)/(1−kE)^4>0, the Hessian is −diag(ν_i)−D''(E)11ᵀ. For every nonzero vector x its quadratic form is −∑ν_i x_i²−D''(E)(∑x_i)²<0. Compactness gives existence and strict concavity gives uniqueness, even at corners.

For a proposed marginal crisis cost λ≥0, define

q_i(λ)=min{b_i,max{0,(A_i−λ)/ν_i}},
Q(λ)=∑q_i(λ).

The unique social allocation is e_i*=q_i(λ*), where

λ*=D'(Q(λ*))=2γQ(λ*)/(1−kQ(λ*))³.

Indeed, Q is continuous and nonincreasing. Therefore H(λ)=λ−D'(Q(λ)) is strictly increasing: when λ rises, its first term strictly rises and its subtracted term cannot rise. At zero, Q(0)>0 if some b_i>0 and H(0)<0. At λ=max_i A_i, Q=0 and H>0. The intermediate value theorem gives a unique root. If every capacity vanishes, the unique allocation is zero and λ*=0. This proof handles all changes in the active set; differentiability of Q at capacity thresholds is unnecessary.

At this root, each bank maximizes its strictly concave private surplus less λ*e_i. Its box-constrained first-order inequalities are exactly those of the social objective, since D'(E*)=λ*. Those inequalities are sufficient under concavity. Thus a common per-unit exposure charge implements the unique allocation in a price-taking bank benchmark. Revenue is a transfer under household ownership and is not an additional social loss. The implementation requires the announced price to be treated as fixed by individual banks; a finite strategic game in which banks manipulate the price is a different model.

This also gives comparative statics without assuming interiority. Holding all A_i,ν_i,b_i fixed, increasing γ raises D'(E) at every positive E. Equivalently, aggregate supply at a fixed λ is unchanged while the fixed-point externality rises. The new root λ* rises, and every q_i weakly falls. The same argument applies when k rises while stability is preserved. The inequalities are strict for aggregate exposure whenever the allocation has a bank whose exposure responds to λ; if all positive banks remain capacity-bound, aggregate exposure can stay constant over an interval of parameters. That qualification is essential.

Finally, an identical absolute cap on every bank need not attain e*. With two uncapped banks having ν_1=ν_2=1 and A_1≠A_2, interior optimal exposures satisfy e_1*−e_2*=A_1−A_2, while a common binding absolute cap forces equality. Bank-specific caps e_i* or the common marginal charge do implement the allocation.

This extension validates the feedback derivative and converts it into a heterogeneous prudential frontier, while preserving the manuscript's stated limits. It does not compare guarantees and risk weights, price sovereign debt, or address strategic price-setting, default discontinuities, or fiscal feasibility. The proof uses no unverified external facts.

Source: [ECON-G28-235-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/18/prb_18be78e2b43748d29b1044d3a7a5843c/contributions/con_4b4b9d1b255948aa9bede00f23ba8c37/files/G28-235.tex), canonical revision rev_66fc321b894b4ab5a5e53f3e6e715fee. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
