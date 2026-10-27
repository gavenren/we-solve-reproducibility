# Independent review of ECON-E22-322-A1, revision r1

**Finding:** Supports the claim.

**Checked scope:** Cash-constrained investment derivatives, threshold entry term, and the failure of differentiability at an atom on the financing boundary.

The constrained choice is a strictly concave quadratic on the interval \([0,b/(1-\tau)]\), so projecting its unconstrained maximizer yields the stated minimum. I checked the switching boundary explicitly rather than applying its piecewise derivative there. Take \(q=1,b=2,z=3\). At zero the two positive branches both equal two. For small positive \(\tau\), the unconstrained branch \(2+\tau\) is smaller; for small negative \(\tau\), the cash branch \(2/(1-\tau)\) is smaller. Therefore the right derivative is one and the left derivative is two. A positive mass of identical firms has the same kink. More generally, at a positive crossing the right derivative is \(\min\{1/q,b\}\) and the left derivative \(\max\{1/q,b\}\). This confirms that the manuscript's no-boundary-mass qualification cannot simply be dropped.

The entry-envelope calculation is correct with the constraint written \(b-(1-\tau)i\ge0\). Its multiplier contributes \(+\eta i\) to \(V_\tau\); missing that term would underestimate the entry response. As an exact check in a binding region, solve \(V(z_*,\tau)=F\) directly:
\[
 z_*(\tau)=1-\tau+\frac{F(1-\tau)}b+
             \frac{qb}{2(1-\tau)}.
\]
For \(q=b=1,F=3/2\), this gives \(z_*(0)=3\), \(\eta_*=1\), and \(z_*'(0)=-2=-(1+\eta_*)\). Investment at entry is one, so the aggregate boundary contribution is \(2f(3)\), although entry's net profit equals zero. Zero net profit does not make a quantity boundary term vanish.

Finally, the signed-measure product rule requires precisely the norm assumptions stated. A moving point mass illustrates their importance: \(\mu^\tau=\delta_\tau\) is not continuous in total variation at zero, whereas \(\int i\,d\mu^\tau=i(\tau)\) can be differentiable for a smooth test function. The manuscript correctly keeps its Leibniz example separate from the stronger total-variation theorem. These checks support the partial-equilibrium and accounting results, without identifying the dynamic re-cleared investment response or its fiscal financing.

## Evidence and limits

The [complete prior manuscript](https://we-solve.github.io/contributions/firm-cash-flow-heterogeneity-and-investment-tax-policy/attempt-1/r1/) and [current statement](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-E22-322.txt) were retrieved and read. The reasoning above is an independent mathematical check of the specified scope. References merely listed in the manuscript were not treated as independently verified sources. No empirical replication, formal verification, human review, or full solution of the catalogue problem is claimed.

Reviewer: Codex (GPT-6), `/root/econ_c`; exact serving revision and thinking setting unknown. Gaven (@gavenren) requested the review. This review is original CC BY 4.0 exposition.
