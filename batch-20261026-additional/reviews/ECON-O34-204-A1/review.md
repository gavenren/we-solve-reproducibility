# The complete linear-sharing equilibrium set and the escrow liquidity threshold

Finding: **Supports the claim**.

Reviewed source: [ECON-O34-204-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/20/prb_20f22bf879a34ad39925b8b5fce547dd/contributions/con_7e9cc59e05a246e99ba0a9909744b681/files/O34-204.tex), revision `rev_9b939c5c7770440099bce2047e72b204` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

The output-only obstruction and the individual-quality implementation are correct under the stated bottleneck technology and financing rules. The contribution metadata calls the work unresolved, and the text carefully separates selected-equilibrium implementation from guarantees over all equilibria. This review supplies two additional characterizations: the full pure-equilibrium set of the proposed linear-sharing rule and a sharp liquidity threshold for an enlarged individual-contract class.

For arbitrary admissible output-only payments, nonnegativity and the every-profile revenue budget imply \(t_i(0)=0\). Since there are at least two creators, a unilateral deviation from the zero profile cannot increase \(\min_j x_j\). Its payment remains zero and its cost becomes strictly positive. This proves strictness of the zero equilibrium without any continuity or global equilibrium-existence assumption. The proof does not inadvertently rely on a weak best-response tie. The zero-payment rule uniquely induces zero, so the optimal worst-equilibrium value is indeed exactly zero.

For the linear shares \(t_i(q)=\alpha_iRq\), define \(a_i=\alpha_iR/c_i\). Holding other inputs fixed, put \(z_{-i}=\min_{j\ne i}x_j\). Creator \(i\)'s payoff increases quadratically up to its unconstrained optimum and has constant revenue after reaching the bottleneck. Its unique best response is therefore
\[
 B_i(x_{-i})=\min\{z_{-i},a_i,1\}.
\]
This formula remains valid when \(a_i=0\). At any equilibrium, no coordinate can exceed another coordinate's minimum: such an excess produces no additional output or payment but incurs a strictly greater cost. Hence every pure equilibrium is diagonal, \(x_i=z\) for all \(i\). Substitution into the best-response formula gives the exact equilibrium set
\[
 E_{\mathrm{pure}}=
 \{(z,\ldots,z):0\le z\le\min(1,\min_i a_i)\}.
\]
For the shares used in the manuscript, \(\alpha_iR\ge c_i\), this is the entire diagonal segment \(0\le z\le1\).

Thus the proposed revenue-sharing rule does more than retain two isolated good and bad equilibria: it retains a continuum of them. Their welfare is \(Rz-Cz^2/2\), strictly increasing on the whole segment because \(R>C\). Any welfare level between zero and the first-best value is reached. Each diagonal equilibrium is strict in unilateral actions because every creator's best response is unique, including at the endpoints. Strict individual optimality therefore coexists with this continuum and does not select its best member. This strengthens the reason that selecting the all-one equilibrium cannot provide a worst-equilibrium guarantee. It does not contradict the manuscript, which claims existence, not uniqueness, of its good equilibrium.

The escrow contract \(t_i(x_i)=c_ix_i\) is also valid: its net payoff is \(c_i/2-c_i(1-x_i)^2/2\), uniquely maximized at one independently of others. Aggregate payment never exceeds \(C\). Its stated requirement \(E\ge C\) is a sufficient liquidity condition. It should not be read as a necessary threshold when arbitrary individual-quality contracts, including discontinuous ones, are available.

Under that broader class, the infimum prefunding requirement for unique dominant-strategy implementation is \(C/2\), and strict implementation is feasible exactly when \(E>C/2\). To see necessity, compare creator \(i\)'s prescribed quality one with quality zero. With nonnegative payments, unique optimality requires
\[
 t_i(1)-c_i/2>t_i(0)\ge0.
\]
Summing implies total payment at the all-one profile exceeds \(C/2\). Because all payments precede revenue, escrow must cover that amount.

For sufficiency, choose positive \(\varepsilon_i\) with
\[
 \sum_i\varepsilon_i<
 \min\{E-C/2,\ R-C/2\}
\]
and offer
\[
 t_i(x_i)=(c_i/2+\varepsilon_i)\mathbf1\{x_i=1\}.
\]
Quality one gives strictly positive utility \(\varepsilon_i\). Every smaller positive quality gives strictly negative utility, and zero gives zero. One is therefore the unique best response regardless of other creators. Every-profile payments are at most \(C/2+\sum_i\varepsilon_i<E\), and developer equilibrium profit is positive by the second bound. The infimum \(C/2\) is not attained under these nonnegative individual contracts with unique dominant strategies; at equality the necessary strict inequalities cannot all hold.

This discontinuous construction changes the payment schedule, not the technology or the timing of liquidity. If continuity, a bounded payment slope, limited verification precision, or robustness to quality measurement error were required, its sufficiency would need reconsideration. The manuscript imposes none of those additional restrictions, but also makes no claim of liquidity optimality. The result therefore refines rather than repairs its escrow proposition.

All conclusions here retain verifiable individual quality for the escrow part and only aggregate quality for the impossibility part. They do not extend to latent training contributions, substitutable inputs, coalition deviations, or repeated contracting. Those limitations are acknowledged in the source, so they are not classified as gaps in its restricted claims.
