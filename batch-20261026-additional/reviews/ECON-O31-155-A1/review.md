# Dual certificates for the finite hidden-quality contract program

Finding: **Supports the claim** within the contract and timing restrictions in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/c3/prb_c386df8783ee4cb196a05427f5b4d302/contributions/con_9737aa3a659f4fda99b2a7d7bbf860a2/files/O31-155.tex). I checked the binary-effort financing threshold, wealth comparative static, strict-implementation qualification, and finite-menu reduction. Its metadata declares an unresolved exploration. Continuous quality, unrestricted contracts, and empirical identification are acknowledged limitations rather than promises of the formal results.

The public-quality threshold follows from two distinct entrepreneurial constraints, which must both be retained. Incentive compatibility requires $z\geq c/(p_1-p_0)$; participation including the wealth contribution requires $z\geq(c+w)/p_1$. Hence the smallest admissible success rent is their maximum, $z_*$. The lender's gap is nondecreasing in this rent, so its least expected public guarantee is exactly

$$
 S_*=[k-w-p_1(X-z_*)]_+.
$$

On the participation-binding branch, substitution cancels wealth and leaves $k-p_1X+c$ before truncation. On the effort-binding branch the gap falls one for one with wealth. This verifies the source's warning against ignoring participation. A guarantee cannot remedy $z_*>X$, because it is paid to the lender on failure and never changes the entrepreneur's effort comparison in this contract family. Weak tie selection is material at $z_*=c/(p_1-p_0)$; the source expressly supplies a slack-based strict implementation argument instead of asserting strictness at every boundary.

An independent, useful addition is an explicit dual upper-bound certificate for the finite-menu program. It allows a proposed numerical menu to be checked without treating a solver's reported optimum as mathematical evidence. Retain all the source's coefficient definitions, in particular $U_{iC}$ after effort has been reoptimized for true type $i$ under item $C$, including after a false report.

Choose nonnegative numbers $\alpha_i,\gamma_i,\lambda$, and $\beta_{ij}$ for distinct types $i,j$, together with unrestricted numbers $\delta_i$. Suppose that for every report $r$ and every library item $C$,

$$
 \delta_r\geq
 \pi_r(W_{rC}-\lambda S_{rC})
 +\left(\alpha_r+\sum_{j\ne r}\beta_{rj}\right)U_{rC}
 -\sum_{i\ne r}\beta_{ir}U_{iC}
 +\gamma_r L_{rC}.
$$

Then every feasible truthful mechanism has welfare at most

$$
 \lambda B+\sum_r\delta_r.
$$

The proof is a finite summation. Multiply the displayed coefficient inequalities by $x_{rC}\geq0$, add them, and use the unit row sums. The right side becomes the original welfare minus $\lambda$ times expected spending, plus nonnegative multiples of entrepreneur participation, reporting-incentive slacks, and lender participation. All these latter terms are nonnegative for a feasible mechanism. Adding $\lambda B$ and using the spending cap proves the bound. Notice the negative cross-report term $ -\sum_{i\ne r}\beta_{ir}U_{iC}$: replacing its utility index by $U_{rC}$ would erase precisely the hidden-quality deviations that the source correctly includes.

Consequently, a feasible matrix and such a certificate with equal objective values prove global optimality directly. Nonzero multipliers also identify which participation, screening, or spending restrictions prevent improvement, while zero slack products provide a convenient consistency check. This is a standard finite linear-program certificate specialized here to the actual timing and pooling conventions, not a claim of a new general duality theorem or a proof that an unrestricted mechanism admits a finite library.

There is also a simple bound on how much lottery support an optimum needs. With $n$ types, an optimal extreme point has at most $n^2+2n+1$ positive report-item probabilities, or the total number of variables if smaller. There are $n$ row equalities and at most $n+n(n-1)+n+1=n^2+n+1$ nontrivial inequality rows: entrepreneur participation, distinct-type reporting, lender participation, and budget. If an extreme point had more positive coordinates than the rank of these active rows, a nonzero perturbation supported on those coordinates could preserve every active constraint. A sufficiently small perturbation of either sign preserves positivity and inactive inequalities, contradicting extremality. A linear objective on the nonempty compact feasible polytope has an optimal extreme point. Redundant rows only improve this support bound.

Both additions depend on the source's commitment before the lottery and pooling within each reported type. Allowing item-by-item opt-out or requiring lenders to break even separately in every realized contract would introduce additional constraints, and these certificates would need the corresponding rows. Under the stated family, however, effort optimization before coefficient construction makes all reporting constraints genuinely linear, and randomized reports add no profitable deviations beyond their deterministic components. Nothing here identifies the coefficients from a single observed funding success rate or resolves the general financing-innovation agenda.
