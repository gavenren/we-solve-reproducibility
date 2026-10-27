# Global response bounds and an explicit certificate for projection-set width

Finding: **Supports the claim**.

Reviewed source: [ECON-Q54-208-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f9/prb_f9287cde8abb4535b7c7be909ee94b6c/contributions/con_9813457870d24df38deb33a7bdb8f71c/files/Q54-208.tex), revision `rev_c90617e03b8945d2ae06cdc39d3dc267` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

The restricted identification theorem is correct. In particular, it conditions on a specific observation scheme—baseline wages, rents, and location shares—and explicitly excludes observed output and profits. The metadata labels the full climate-migration problem unresolved. I find no contradiction between baseline observational equivalence and the endogenous wage equations. This review gives independent global bounds on counterfactual migration and on the size of the projection interval, rather than only checking the local derivative at zero.

Put \(d_b=n_b(\delta)-1/2\) for \(\delta>0\). The equilibrium equation becomes
\[
 \delta=\tau\log\frac{1+2d_b}{1-2d_b}+2bd_b,
 \qquad 0<d_b<1/2.
\]
The right side is continuous, strictly increasing from zero to infinity, so existence, uniqueness and the positive sign of the response follow directly. For \(b=0\),
\[
 d_0=\tfrac12\tanh\{\delta/(2\tau)\}.
\]
Adding \(2bd\) to the inverse response function reduces its positive solution, giving \(d_b\le d_0\). This independently verifies attenuation and supplies a finite-shock benchmark rather than a derivative-only comparison.

Let \(C=4\tau\cosh^2\{\delta/(2\tau)\}\). The derivative of the inverse response function, as a function of \(d\), is
\[
 \frac{4\tau}{1-4d^2}+2b.
\]
For \(0\le d\le d_b\le d_0\), this lies between \(4\tau+2b\) and \(C+2b\). Integrating that derivative from zero to \(d_b\) yields the global bounds
\[
 \frac{\delta}{C+2b}\le d_b
 \le\frac{\delta}{4\tau+2b},
 \qquad d_b\le d_0.
\]
These inequalities hold for every finite positive shock. The upper linear bound need not itself be below one half, so the logistic bound should also be retained. Both rational bounds converge to the manuscript's local response \(\delta/(4\tau+2b)\) as \(\delta\downarrow0\).

The same calculation gives a certified width for the sharp set. Write
\(W(\delta)=d_{b_L}-d_{b_U}\). Implicit differentiation with respect to \(b\) gives
\[
 -\frac{\partial d_b}{\partial b}
 =\frac{2d_b}{4\tau/(1-4d_b^2)+2b}.
\]
Using both bounds above on its numerator and denominator, and integrating from \(b_L\) to \(b_U\), gives
\[
 \delta\!\left(\frac1{C+2b_L}-\frac1{C+2b_U}\right)
 \le W(\delta)\le
 \delta\!\left(\frac1{4\tau+2b_L}-\frac1{4\tau+2b_U}\right).
\]
The lower bound is positive whenever \(b_L<b_U\), and both bounds have the same first-order expansion as \(\delta\) tends to zero. This proves quantitatively that the uncertainty in equilibrium feedback produces a nontrivial projection interval even though every admissible economy has a unique equilibrium. It also gives analytic checks for any numerical endpoint solver without treating simulation as proof.

For the identification claim itself, baseline equilibrium has \(n=1/2\), so the stipulated choice \(A=w_*+b/2\) gives both wages \(w_*\). The restriction \(b_U<2w_*\) ensures \(A>b\) for every admissible slope, and zero rents follow from the explicitly elastic housing technology. Since the response is continuous and strictly decreasing in \(b\), its image on the closed interval is exactly the source's endpoint interval, including every interior value. There is no hidden equilibrium-selection issue in this argument.

The observation scheme is consequential and can be tested algebraically. At baseline, aggregate physical output is
\[
 Q=2F(1/2)=A-b/4=w_*+b/4,
\]
and aggregate profits are \(b/4\). Thus either measured aggregate output together with \(w_*\), or measured aggregate profits, point-identifies \(b\). This verifies the manuscript's warning that the same nonidentification claim does not apply to every richer dataset.

Likewise, observing a response \(n>1/2\) to one known positive shock, with known \(\tau\), identifies the slope by
\[
 b=\frac{\delta-\tau\log(n/(1-n))}{2n-1}.
\]
The formula is well-defined away from the zero-shock baseline. Compatibility with \(b\ge0\) requires \(n\) not exceed the no-feedback logistic response. It shows precisely why baseline fit alone leaves the slope free while a suitable counterfactual experiment does not.

These checks support a sharp set only within the announced static model. They establish neither a distributional welfare ordering nor a benefit from improved anticipation; the model has no forward investment or information decision. Those missing ingredients are already expressly separated in the manuscript, so I do not classify them as errors in the stated theorem.
