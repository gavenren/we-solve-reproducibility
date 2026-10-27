# Review: context rank, misspecification amplification and endpoint design

**Finding:** Supports the checked claims. **Checked scope:** affine identification, exact worst-case linear risk, and one-dimensional extrapolation design in ECON-C90-604-A1, revision r1.

The null-space argument gives both directions of identification. If $Z^\top\lambda=z_*$, the target equals $\lambda^\top Z\theta$. Otherwise a null vector $v$ with $z_*^\top v\ne0$ permits $\theta+tv$ without changing any laboratory mean, while the target ranges unboundedly. This conclusion depends on unrestricted affine coefficients and outcomes; it must not be imported into the separate bounded-outcome section.

For the optimal linear estimator, I checked the orthogonality calculation rather than relying only on first-order equations. The proposed $\lambda_0$ satisfies the affine constraints, and $\Omega\lambda_0$ lies in the column space of $Z$. Every other feasible weight is $\lambda_0+h$ with $Z^\top h=0$, so variance increases by $h^\top\Omega h>0$ unless $h=0$. Full column rank makes the inverse valid; positive variances make uniqueness valid.

The departure risk formula is sharp in its declared rectangular error class. The bias $\lambda^\top e-e_*$ attains magnitude $\gamma_*+\sum|\lambda_j|\gamma_j$ by simultaneous coordinate signs, independently of the centered normal sampling error. Thus variance plus squared worst bias is exact. It is not a minimax result over all nonlinear estimators, and the manuscript does not claim that.

An independent extrapolation check uses lab contexts $0,1$ and field context $2$. Affine-exact endpoint weights are $(-1,2)$, whose absolute sum is $3$. Every admissible design has absolute sum at least $3$, because $h(c)=2c-1$ is bounded by one on the laboratory range and $h(2)=3$. Allocating information $N/3,2N/3$ gives variance $9\sigma^2/N$ and worst bias $4\gamma$, yielding risk $9\sigma^2/N+16\gamma^2$. This verifies both terms of the theorem and shows why increasing participant count cannot remove the departure penalty.

At the boundary $x=b$, the absolute-sum bound becomes one and the design collapses to the endpoint context; the formula has the correct continuous limit. Zero prediction weights receive zero information, while nonzero weights necessarily receive positive information.

No error was found in these claims. The review does not establish empirical affine invariance, calibrated departure bounds, normal finite-sample contrast noise, or optimality outside the linear class. The final covariate-support argument is a separate model, as the manuscript explicitly states.

