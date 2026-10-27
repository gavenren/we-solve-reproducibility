# Review: intervention-level forecast risk and the Gaussian ranking limit

**Finding:** Supports the checked claims. **Checked scope:** held-intervention risk correction and Gaussian magnitude/rank formulas in ECON-D91-558-A1, revision r1.

The risk target uses the noisy low-scale estimate available when forecasting, not the latent low-scale effect. I checked that the validation correction only removes high-scale evaluation noise. With a frozen forecast, conditional centering makes the cross term vanish; subtracting its conditional variance gives unbiased risk. For two forecasts, the shared squared noise cancels before expectation. Under constant validation variance $v$, the remaining noise term has variance $4vE(f-g)^2$ and zero covariance with the latent loss difference. These conclusions need centering conditional on the forecast inputs, not merely unconditional unbiasedness.

The Gaussian predictor coefficient is $c/(v_L+v_\varepsilon)$, so low-scale trial noise correctly attenuates the coefficient. Its residual variance is $v_H-c^2/(v_L+v_\varepsilon)$. Orthogonality of the Gaussian residual to $T$ gives independence and the Pythagorean risk decomposition. As a check, $v_L=v_H=1,c=1,v_\varepsilon=3$ gives coefficient $1/4$ and irreducible risk $3/4$ despite perfect latent correlation.

For two independent interventions the forecast difference and target difference have correlation $|c|/\sqrt{v_H(v_L+v_\varepsilon)}$. Their variances double but cancel from this correlation. The angle calculation is correct: disagreement wedges have total angle $2\arccos\rho$ out of $2\pi$, giving agreement $1/2+\arcsin(\rho)/\pi$. In the preceding example $\rho=1/2$, so ranking success is $2/3$, not the latent perfect-order probability one. The cases $\rho=1$ and $c=0$ yield perfect order and fair-tie success one-half as stated.

The Hoeffding comparison radius is conservative but valid: bounded effects and predictions imply loss differences within $[-4B^2,4B^2]$, a range of length $8B^2$. The independent unit for this statement is the intervention, so increasing individuals within existing trials does not multiply the intervention-level sample count.

No error was found in this scope. I did not certify Gaussianity, transport to a new intervention population, empirical scale effects, or the separate two-stage exposure mapping. The manuscript correctly distinguishes forecasting across interventions from causal effects of changing saturation.

