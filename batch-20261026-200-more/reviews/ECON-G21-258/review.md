# Sparse implementation under funding and uptake constraints

The manuscript permits budget-induced randomization but does not bound how much randomization is needed. Its finite-group oracle has a particularly simple implementation: there always exists an optimum assigning deterministic offers in every group except possibly one. This remains true with multiple offers per group. In the quadratic scale model, at most two groups need randomize.

Include no offer explicitly as action zero, with \(\tau_{j0}=c_{j0}=0\), and write \(x_{ja}\) for action probabilities, so
\[
x_{ja}\ge0,\qquad \sum_{a=0}^Ax_{ja}=1,\qquad
\sum_{j,a}p_jc_{ja}x_{ja}\le B.
\tag{A}
\]
The objective is \(\sum p_j\tau_{ja}x_{ja}\). The source's assumptions ensure that this is a nonempty compact polytope; a linear objective attains its maximum at an extreme point.

At an extreme point with a binding budget, there are at most \(J+1\) positive coordinates. To see this directly, suppose more coordinates are positive. Restrict the \(J\) group-sum equations and the budget equality to these coordinates. Their matrix has rank at most \(J+1\), so a nonzero vector \(z\) is in its nullspace. For sufficiently small \(\epsilon>0\), both \(x+\epsilon z\) and \(x-\epsilon z\) remain nonnegative, preserve all group sums and preserve the budget. They are distinct feasible points with midpoint \(x\), a contradiction.

Every group requires at least one positive coordinate. Therefore at most one group can have two positive coordinates, and no group can have three. All other groups receive a single action with probability one. If the budget is slack, the same perturbation argument uses only the \(J\) group equations: sufficiently small perturbations preserve the strict budget inequality, giving at most \(J\) positive coordinates. Thus a slack-budget extreme optimum is entirely deterministic.

This is an existence statement, not a claim that every optimal policy is sparse. Ties can make convex combinations of sparse optima optimal and produce randomization in many groups. A degenerate budget row may also lower the available rank; it cannot invalidate the upper bound.

The one-group exception is necessary. Take one group and one nonzero action with cost one and welfare gain one, with \(0<B<1\). The policy's offer probability must satisfy \(x\le B\), and its value is \(x\), so the unique optimum is \(x=B\). It randomizes between the offer and no offer, while every deterministic feasible policy has value zero. This example satisfies the source's cost and welfare bounds.

Now consider the source's scaled welfare
\[
\mathcal V(x)=V(x)-\eta Q(x)^2/2,\qquad
Q(x)=\sum_{j,a}p_jd_{ja}x_{ja},
\]
with \(d_{j0}=0\). Choose any optimum and denote its aggregate uptake by \(q^*\). On the slice \(Q=q^*\), maximizing \(\mathcal V\) is exactly maximizing the linear objective \(V\), because the quadratic term is constant. Choose an extreme-point maximizer of this sliced polytope. It remains globally optimal: a higher value on the slice would contradict the original optimum.

The positive-coordinate argument now has the group equations, one uptake equality and, if binding, one budget equality. Hence there exists an optimum with at most \(J+2\) positive coordinates. At most two groups randomize; if both do, each uses two actions. Alternatively one group may use three. If the budget is slack, the upper bound improves to \(J+1\), so at most one group randomizes. Redundant uptake or budget rows can further reduce these bounds.

The argument applies to the declared population-probability optimization, not a guarantee about realized finite-portfolio spending. It does not identify the uptake externality parameter or transport trial effects across markets. It supports the source's oracle characterization and gives an implementable structural refinement without claiming a solution to private-type contract design.

Source: [ECON-G21-258-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/8e/prb_8e26044927224700a15f3f72dd88c0df/contributions/con_3126ce2f86674907960728444b388d12/files/G21-258.tex), canonical revision `rev_7559353db10b4044ae284302558720ba`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
