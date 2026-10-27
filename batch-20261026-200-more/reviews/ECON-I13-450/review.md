# Robust network benefits can lose submodularity, while policy randomization helps

The source carefully separates its submodular access-benefit theorem from its finite-model robust policy table. Combining the two without care would lose the greedy guarantee: the pointwise minimum of admissible submodular benefits need not itself be submodular. A small exact example also shows how randomizing policy can improve the robust criterion when nature chooses a model before the random draw.

Take providers a,b,d and two compatible access models. In model 1 a single patient receives benefit one only from a; in model 2 a single patient receives benefit one only from b. Provider d gives zero in both. All opening costs are zero. These are exactly the source's one-provider-per-patient maximum-benefit functions, hence normalized, monotone and submodular.

The robust benefit is F(N)=min{B_1(N),B_2(N)}. It satisfies F({a})=F({b})=0 and F({a,b})=1. Thus adding b to {a} has marginal benefit one, while adding b to the empty network has benefit zero, contradicting diminishing returns. This is not caused by provider complementarity within either model; it arises solely from taking their minimum.

With provider-count budget k=2, a greedy algorithm based on F can choose d first because every singleton has marginal value zero. Its second choice still leaves robust benefit zero. The optimal pair {a,b} has value one. Thus no positive multiplicative guarantee follows for this greedy rule under unspecified tie selection, despite each individual model satisfying the source's theorem. The example does not invalidate greedy applied to the original fixed known B.

Now consider a finite regulation menu P and model set M, with welfare table W_m(p) as in the source. Let a policy lottery π be chosen before the model is selected, and let nature choose one model before the policy is randomly realized. The robust expected-welfare problem is the linear program

maximize t,
subject to ∑_pπ_p W_m(p)≥t for every m,
∑_pπ_p=1, π_p≥0.

Its feasible policy simplex is compact and the minimum of finitely many affine expected-welfare functions is continuous, so an optimum exists. Nature must not observe the realized policy before selecting a model; that different timing would give Eπ[min_m W_m(p)] and eliminate this diversification benefit.

The dual minimizes s over model probabilities λ_m≥0 summing to one, with s≥∑_mλ_m W_m(p) for every p. To see the weak bound directly, every policy lottery's minimum-model payoff is at most its payoff under any fixed mixture λ, which is at most max_p∑λ_mW_m(p). Finite linear-program duality supplies equality and attained optimal strategies. Thus an optimal model mixture is an exact upper certificate for the randomized robust value, not a claim that the model probabilities are statistically identified.

For k=1 in the two-model example without d, deterministic networks {a} and {b} both have robust benefit zero. A half-half lottery has expected benefit one half in each model. No lottery can exceed one half because equal model weights give every singleton expected benefit one half. The randomized robust value is therefore exactly one half.

There is a finite support bound as well. An optimal extreme solution can use at most |M| policies: with r positive policy probabilities and the free value variable t, the mass equation and at most |M| active welfare inequalities must have rank at least r+1, forcing r≤|M|. This is an existence bound, not a claim of cheap enumeration when the policy menu is huge.

These results concern expected welfare under an explicitly chosen timing and uncertainty set. Insurance regulation may require a fixed network, and patients may value continuity in ways not present in the table. The construction neither recommends random network reassignment nor identifies market equilibria; it clarifies which mathematical guarantees survive robustification of the source's benchmark.

Source: [ECON-I13-450-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/8a/prb_8a769965ad5e4127bff6f8a7732a8d18/contributions/con_ef81cb3191ef42c496464b79ac99b9cb/files/I13-450.tex), canonical revision rev_5dda3fbd36ec4a1f89b854e3f0c13ebb. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
