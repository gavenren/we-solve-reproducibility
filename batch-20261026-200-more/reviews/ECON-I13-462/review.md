# One initial lottery between two deterministic care policies

The manuscript proves that one occupied state needs randomization at most. A complementary implementation is available under its same response-reduction and expected-financing assumptions: an optimal policy can be selected by a single initial lottery between at most two deterministic stationary policies. The lottery then remains fixed over the entire realized care history.

First omit the financing inequality and let \(\mathcal X\) be the source's nonnegative discounted occupation polytope. Its extreme points correspond to deterministic stationary policies on occupied states. Here is a direct check. At an extreme occupation point, let \(n_+\) be the number of occupied states and \(k\) the number of positive state-action coordinates. As in the source's proof, flow rows outside occupied states vanish on these coordinates. If \(k>n_+\), a nonzero null perturbation preserves all flows and, in both sufficiently small signs, nonnegativity. This contradicts extremality. Since every occupied state requires one action, \(k=n_+\), hence exactly one action per occupied state. Complete the rule arbitrarily at unoccupied states.

A bounded polytope is the convex hull of its finitely many vertices. Denote the corresponding deterministic stationary policies by \(d=1,\ldots,M\), with discounted welfare and outlay
\[
V_d=\frac{\sum r x_d}{1-\beta},\qquad
C_d=\frac{\sum G x_d}{1-\beta}.
\]
Every history-dependent admissible policy therefore has the same welfare-cost pair as an initial lottery with probabilities \(\alpha_d\):
\[
V=\sum_d\alpha_dV_d,\quad C=\sum_d\alpha_dC_d,\quad
\alpha_d\ge0,\quad\sum_d\alpha_d=1.
\tag{A}
\]
Conversely, drawing a policy once and following it forever is itself an admissible history-dependent randomized policy. Its occupation measure is the corresponding convex combination by linearity of expectation. The source's response reduction is essential: future-policy anticipation cannot alter the stipulated response law after the initial draw.

The financed problem is thus a finite linear program in \(\alpha\), with one normalization equality and one expected-cost inequality. An optimal extreme point has at most two positive coordinates when the budget binds, and at most one when it is slack. The proof is the same nullspace argument: more positive weights than active equalities permit opposite feasible perturbations. Consequently at most two deterministic rules suffice.

If the two selected policies have \(C_1<B<C_2\), the exact lottery is
\[
\alpha_1=\frac{C_2-B}{C_2-C_1},\qquad
\alpha_2=\frac{B-C_1}{C_2-C_1}.
\]
Their expected expenditure equals \(B\). At an endpoint or equal costs, a deterministic policy may suffice. Costs may be negative because the source allows net receipts; no nonnegativity assumption is needed for the convex-hull argument.

Randomization can be necessary. Take one absorbing need state with two legal packages. Let \(\beta\in(0,1)\); package zero has per-period welfare and outlay zero, while package one has both equal to \(1-\beta\). The two deterministic stationary policies have welfare-cost pairs \((0,0)\) and \((1,1)\). At budget \(B\in(0,1)\), mixing them with probability \(B\) on package one attains welfare \(B\), whereas the only feasible deterministic rule has welfare zero.

This implementation does not promise that each initially selected policy separately meets the budget: the expensive branch can exceed \(B\). It is valid precisely because finance is an expected present-value constraint backed by the source's outside fiscal account. Requiring solvency separately in every branch would exclude that lottery and change the problem.

The result preserves legal need verification, specified family responses and net fiscal accounting. It does not establish a forward-looking family reduction, identify untried packages, or claim that initial randomization is administratively preferred to the source's one-state lottery.

Source: [ECON-I13-462-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/05/prb_054120a0a16748df8ca752f23a491dbd/contributions/con_395da907653847b9a7a74f9a93bf3c72/files/I13-462.tex), canonical revision `rev_03f9f065bdb24a0fa4f0ebd315c3dc97`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
