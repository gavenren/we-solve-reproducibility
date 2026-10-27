# Review: confounding equivalence and finite-sample calibration

**Finding:** Supports the checked claims. **Checked scope:** Gaussian unbounded-bias construction and joint-moment confidence propagation in ECON-C21-581-A1, revision r1.

I independently recomputed the covariance construction. Write $W=\sqrt rE+\sqrt{1-r}V$ and $F=(1-r)E-\sqrt{r(1-r)}V$. Then $\operatorname{Cov}(W,F)=\sqrt r(1-r)-\sqrt r(1-r)=0$, $\operatorname{Var}(W)=1$, and $\operatorname{Var}(F)=1-r$. With $U=cD+\sqrt{1-c^2}W$, the stated regression residual is independent of $(D,U)$ by joint Gaussianity. Substitution gives $\beta D+\gamma U+F=bD+E$ exactly. The partial association with treatment is $c^2$; after residualizing on treatment, the squared correlation between $E$ and $\sqrt{1-c^2}W$ is $r$. Thus the divergence of $\beta=b-c\sqrt{r/(1-c^2)}$ is real, while the entire observed law remains fixed.

For the finite-sample theorem, raw products lie within $[-M^2,M^2]$, and first moments within $[-M,M]$. The chosen radius gives per-entry failure $\alpha/(p+p^2)$; summing over the stated number of entries yields $\alpha$. Counting both covariance triangles is conservative and harmless. The nonlinear covariance transformation is applied to the whole feasible moment region, so no unproved linearization or independent-estimation assumption is needed.

I checked monotonicity of the sensitivity map: for $0\le d<1$, both partial derivatives of $yd/(1-d)$ are nonnegative. On the joint moment-coverage event the true covariance is one admissible point, so its own bias interval is contained in the reported outer interval. This proves coverage even if the covariance extremizers are not jointly attainable causal models; the manuscript correctly avoids claiming sharpness.

Boundary qualifications matter. The cap $d_*<1$ prevents one source of divergence but does not by itself control vanishing residual treatment variance. The manuscript separately requires the projection inverses and positive residual variances, and correctly invokes uniform eigenvalue/residual lower bounds for informativeness. At zero benchmark partial association the declared multiplicative bridge forces the corresponding omitted association to zero; this is an assumption, not something validation proves.

No error was found in this scope. I did not verify any empirical comparative-strength multiplier, transported validation law, external citation or numerical implementation of the nonlinear covariance optimization. The theorem gives conditional coverage; it does not justify the calibration bridge.

