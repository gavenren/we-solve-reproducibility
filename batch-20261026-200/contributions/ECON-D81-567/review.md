# Review: what repeated mirror measurements actually identify

**Finding:** Supports the checked claims. **Checked scope:** observational obstruction, sharp population coupling bounds and finite-panel guarantees in ECON-D81-567-A1, revision r1.

The two utility examples were checked directly. For the lottery $(1/2,4,0)$, normalized linear utility has certainty equivalent $2$, while normalized square-root utility has certainty equivalent $1$. Adding systematic errors $C$ and $1+C$, respectively, gives identical reports $2+C$ under every representation sequence. Repetition cannot distinguish these deterministic models. The example changes latent preferences while preserving utility normalization, so it is stronger than an arbitrary change of utility units.

The sharp-set theorem is carefully indexed by the population law of the conditional mean $\mu$, not by a full finite-panel observable distribution. For every admissible coupling, setting $d=\mu-v$ and trial errors to zero preserves that law and meets the declared model. It would not generally preserve a specified nondegenerate finite-panel law; the manuscript expressly excludes that stronger conclusion. This distinction is necessary for the sharpness argument.

I checked the CDF endpoint convention. The smallest feasible value is $\max(y,\mu-\eta)$ and the largest is $\min(x,\mu+\eta)$. For $y\le t<x$, their CDFs equal the displayed $\Pr(\mu-\eta\le t)$ and $\Pr(\mu+\eta\le t)$. At $t=x$ both genuine CDF bounds must be one, which explains the theorem's strict upper restriction on $t$. For example $y=0,x=1,\mu=0.95,\eta=0.1$ gives lower CDF zero at $t=0.99$ but one at $t=1$.

For the simultaneous panel guarantee, centered errors have range length $2B$. Hoeffding gives $2\exp[-Jb^2/(2B^2)]$ for one subject; the stated $b$ makes this $\alpha/N$, and a union bound yields the claimed event. This is a bound on the sampled subjects' latent values, not automatically a confidence band for a population CDF.

Finally, with independently known continuous increasing utility, the certainty-equivalent-to-weight map is continuous and increasing with positive denominator. It maps every point in the feasible certainty-equivalent interval onto the full displayed weight interval. Unknown utility is not recovered by this step.

No gap was found in the stated scope. No empirical mirror calibration, independence across repetitions, joint identification of utility and probability weighting, or finite-panel deconvolution is certified. These assumptions and exclusions are essential to the result.

