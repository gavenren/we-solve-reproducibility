# Global transfer reallocation after a mean-preserving spread of income risk

The source compares marginal utilities at zero transfer for two categories with the same mean and different risk. The conclusion can be strengthened to a global comparative static of the optimal targeting rule, including the response of the common budget multiplier and every other bin.

Keep the verified categories, masses p_i>0, welfare weights ω_i>0, positive resource lower bound and transfer caps of the manuscript. Let 0<b<∑p_i bar t_i, so the budget binds. Change only the income law in category j from Y_j to Y'_j, with Y'_j a mean-preserving spread in the convex-order sense: Eφ(Y'_j)≥Eφ(Y_j) for every applicable convex φ, and means coincide. Require the same positive resource lower bound and finite expected logarithms. All other primitives and the budget stay fixed.

For each category define its marginal benefit per budget dollar as m_i(t)=ω_i E[1/(Y_i+t)]. It is continuous and strictly decreasing on its transfer interval; the lower resource bound justifies differentiation or direct dominated convergence. Since y↦1/(y+t) is convex for every t≥0, the risk change gives

m'_j(t)≥m_j(t) for all feasible t.

Here the prime on m denotes the changed environment, not differentiation. This pointwise inequality is stronger than a comparison of variances alone: a larger variance without convex ordering would not suffice.

At a proposed multiplier λ>0, let T_i(λ) be the unique maximizer on [0,bar t_i] of ω_i Elog(Y_i+t)−λt. Strict concavity makes this demand single-valued and continuous. The first-order conditions give the source's clipped marginal-equality rule. T_i is nonincreasing in λ, and the marginal comparison implies T'_j(λ)≥T_j(λ) at every fixed λ, including zero and upper-cap corners.

Let λ clear the original budget. At that same λ the changed aggregate spending is at least b. As the multiplier tends to infinity, all transfers tend to zero, while the demand function is continuous. Therefore a changed clearing multiplier λ'≥λ exists. It follows immediately that T_i(λ')≤T_i(λ) for every unchanged category i≠j. Both budgets bind, so

p_j(t'_j−t_j)=−∑_{i≠j}p_i(t'_i−t_i)≥0.

Thus the riskier category's optimal payment weakly increases, and every other category's payment weakly decreases. The source's uniqueness theorem makes this a statement about the unique optimal vectors even when a clearing multiplier itself is not unique.

Weak inequalities are necessary. The riskier category may already be capped; a one-category system cannot reallocate its fixed budget; or all responsive margins can remain at corners. A sufficient condition for a strict increase is that the marginal inequality be strict at the original category-j transfer, that category be interior there, and at least one other category respond strictly to the resulting rise in λ without leaving its interior immediately. Then spending rises at the old multiplier, λ must rise, some other payment falls, and the budget forces j's payment upward.

This comparative static clarifies what insurance priority means after the entire allocation adjusts. It does not say the riskier category reaches a higher consumption level, or that social welfare rises after its income becomes riskier. Indeed a mean-preserving spread lowers expected log utility at any fixed payment. The theorem concerns the best allocation conditional on the changed risk, not a benefit of exposure to that risk.

Verification, exogenous income distributions, fixed financing, common payment within a bin and full take-up remain essential. Endogenous take-up, labor responses or a risk change that alters the budget would require a different comparison. The result is a self-contained extension of the source's insurance example, without certifying external references.

Source: [ECON-E62-411-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/07/prb_074185f7fbbb4d24a55a42cb95344242/contributions/con_edc50fc23bea477ebf52a226adbeb515/files/E62-411.tex), canonical revision rev_cb25a434c2744dc2b87dd427095d9555. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
