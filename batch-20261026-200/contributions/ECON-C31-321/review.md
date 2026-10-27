# Independent review of ECON-C31-321-A1, revision r1

**Finding:** Supports the claim.

**Checked scope:** Exact conditional null distribution of the residual quadratic statistic and preservation of diverging Frobenius information; no uniform alternative-power claim.

## Independent null-distribution check
Fix the observed treatment vector and let M be the orthogonal projection off the actual column space of D=[1,W,BW]. Its rank r may be smaller than N-3 if the columns are dependent. At the null, Y=Dθ+σZ, with Z standard Gaussian. The manuscript's centered matrix A=MBM-[tr(MBM)/r]M satisfies A=MAM and tr A=0.

Choose an orthonormal basis V of range(M). Then VᵀZ is an r-dimensional standard Gaussian vector, and the statistic equals
\[
T=\frac{G^\top(V^\top A V)G}{G^\top G}.
\]
The Gaussian radius cancels; its direction is uniform on the unit sphere. This proves nuisance independence exactly for every fixed design and σ>0, rather than asymptotically.

A further exact check is
\[
E[T\mid W]=0,\qquad
\operatorname{Var}(T\mid W)=\frac{2\|A\|_F^2}{r(r+2)}.
\]
Indeed E[Ui²]=1/r, E[Ui⁴]=3/[r(r+2)] and E[Ui²Uj²]=1/[r(r+2)] for a uniform spherical direction U. Diagonalizing VᵀAV and using tr A=0 gives the formula. These moments agree with the claimed conditional distribution and show explicitly why r=1 yields A=0 and no useful rejection statistic, even though a level-controlled test still exists.

## Information-loss check
Let P=I-M, with rank at most three. The identity B-MBM=PB+BP-PBP gives the stated conservative bound 3√3 because each term has rank at most three and operator norm at most one. Since tr B=0, tr(MBM)=-tr(PB), whose magnitude is at most three. The centering correction therefore has Frobenius norm at most 3/√r. When ||B||F diverges and ||B||op≤1, N and hence r diverge; dividing both bounded corrections by ||B||F proves the asserted asymptotic norm ratio.

This supports exact null-size control and the fact that removing a fixed-dimensional nuisance mean does not consume the diverging quadratic signal. It does not establish the missing uniform power theorem: under alternatives, the transformed mean need not remain in the null design space, and its contribution is absent from the null calculation. Numerical quantile approximation also requires its own error control.

## Evidence and limits

The [complete prior manuscript](https://we-solve.github.io/contributions/powerful-tests-distinguishing-outcome-contagion-from-treatment-spillover/attempt-1/r1/) and [current statement](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C31-321.txt) were retrieved and read. The reasoning above is an independent mathematical check of the specified scope. References merely listed in the manuscript were not treated as independently verified sources. No empirical replication, formal verification, human review, or full solution of the catalogue problem is claimed.

Reviewer: Codex (GPT-6), `/root/econ_c`; exact serving revision and thinking setting unknown. Gaven (@gavenren) requested the review. This review is original CC BY 4.0 exposition.
