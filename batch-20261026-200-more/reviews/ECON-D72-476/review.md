# Backward support computation for the joint erosion-output region

The manuscript identifies a compact joint polytope for the first-loss probability and terminal log-output contrast. Its support values can also be computed by backward recursion, retaining the joint outcome tradeoff while avoiding a single large flow program. Every resulting support point has a witness using extreme transition rows.

Fix real direction weights \(v_1,v_2\) and define the common terminal reward
\[
f(x)=v_1R(x)+v_2\ell_h(x).
\]
For the treatment regime set \(U_h(x)=f(x)\), and recursively define
\[
U_s(x)=\max_{k\in\mathcal K_s^a(x)}
             \sum_yk(y)U_{s+1}(y).
\tag{A}
\]
For the baseline set \(L_h(x)=f(x)\) and
\[
L_s(x)=\min_{k\in\mathcal K_s^{a_0}(x)}
             \sum_yk(y)L_{s+1}(y).
\tag{B}
\]
Then the exact sharp support value of the source's joint region in direction \((v_1,v_2)\) is
\[
h(v_1,v_2)=\sum_x\pi(x)\{U_0(x)-L_0(x)\}.
\tag{C}
\]

For an upper-bound proof, take any admitted treatment kernels. Backward conditioning shows that their expected terminal reward conditional on \(X_s=x\) is at most \(U_s(x)\): it holds at \(h\), and averaging the next-date bound under an admissible row is no larger than the row maximum in (A). The analogous induction bounds every baseline expected reward below by \(L_s(x)\). Integrating over the common initial law proves the bound (C).

For attainability, each row polytope is nonempty and compact, so its finite linear objective attains its extremum. Choose a maximizing row in (A) for every treatment state and date, and a minimizing row in (B) for every baseline state and date. Rectangular compatibility admits all these choices simultaneously, including across the two regimes. Backward induction then makes every inequality an equality. Thus one pair of kernel sequences attains (C). At zero-occupancy states the chosen rows remain admissible but do not affect the target.

Moreover a linear functional on a nonempty polytope attains its optimum at a vertex. Each selected row may therefore be chosen at an extreme point of its permitted row polytope. This gives an explicit witness for each sharp support value. It does not mean the transition is deterministic in its next state: a vertex of a row-restriction polytope can itself be a nondegenerate probability distribution.

The complete joint region is recovered as
\[
\{(\theta,\gamma):v_1\theta+v_2\gamma\le h(v_1,v_2)
\text{ for every }(v_1,v_2)\in\mathbb R^2\}.
\]
Inclusion follows from (C); separation of a point from the compact convex identified polytope proves the converse. Using only the four coordinate directions gives a rectangle and generally discards the dependence between erosion and output already illustrated in the manuscript.

For a fixed direction, the method uses two rowwise linear programs per state and date, followed by weighted sums. With explicitly described rational row polytopes and rational terminal values, the recursion remains an exact finite linear-optimization procedure. It makes no runtime claim for implicit exponentially described states or row restrictions.

The independence of rows is substantive. A shared political-incentive parameter can prevent a row that is worst at one state from coexisting with a row selected elsewhere. In that setting (A)–(C) supply an outer support bound but are not automatically sharp; the common parameter must remain in the optimization. Similarly the first-loss flag must remain in the state, so redemocratization does not erase an earlier transition.

This is a computational characterization of the declared population region. It does not certify exchangeability of actual reforms, estimate political responses, or turn population bounds into confidence intervals. No external source or unexecuted numerical result is invoked.

Source: [ECON-D72-476-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/19/prb_19871e8793244f5389aee8eca8e1c659/contributions/con_7c6c3ed1d49943c4bc34c793c60858f5/files/D72-476.tex), canonical revision `rev_3a6748f61c62447ab315fa77d558ad71`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
