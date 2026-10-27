# Low-order factorial recovery has an exact off-design noise amplification factor

The source recovers a degree-bounded welfare function from low-order feature cells and bounds each recovered interaction's error. Prediction of a large untested bundle reuses those same cells, so its exact error should be computed from their combined coefficients. The resulting interpolation formula gives a sharp deterministic amplification factor.

Retain the degree restriction \(\beta_U=0\) for \(|U|>d\), and suppose all cells \(W(T)\) with \(|T|\le d\) are observed with simultaneous error at most \(\epsilon\). Fix a bundle \(S\) of size \(k>d\). Then
\[
W(S)=\sum_{\substack{T\subseteq S\\|T|\le d}}
(-1)^{d-|T|}
\binom{k-|T|-1}{d-|T|}W(T).
\]
No cells outside \(S\) are needed.

To derive it, first use \(W(S)=\sum_{U\subseteq S,|U|\le d}\beta_U\), then substitute the source's finite-difference inversion for each \(\beta_U\). The coefficient of a fixed \(W(T)\), with \(t=|T|\), becomes
\[
\sum_{r=0}^{d-t}(-1)^r\binom{k-t}{r}.
\]
For \(d-t<k-t\), Pascal's identity telescopes this alternating partial binomial sum to \((-1)^{d-t}\binom{k-t-1}{d-t}\), proving the formula. This also covers \(d=0\), where the response is constant and the predicted value is simply the baseline.

The exact worst-case prediction-error radius over the stated cell-error box is
\[
\epsilon A_{k,d},\qquad
A_{k,d}=\sum_{t=0}^d
\binom kt\binom{k-t-1}{d-t}.
\]
The triangle inequality proves inclusion. For attainability, choose each tested cell error at \(\epsilon\) times the sign of its prediction coefficient. Those errors are consistent with another degree-at-most-\(d\) function because low-order cell values parameterize that function invertibly. Thus every error inside the radius, including both extrema, is attainable in the unrestricted degree class. Additional welfare-range or structural constraints can shrink this box image; sharpness is not asserted after adding them.

For additive welfare (\(d=1\)),
\[
W(S)=\sum_{j\in S}W(\{j\})-(k-1)W(\varnothing),
\qquad A_{k,1}=2k-1.
\]
For degree two,
\[
W(S)=\sum_{\{i,j\}\subseteq S}W(\{i,j\})
-(k-2)\sum_{i\in S}W(\{i\})
+\binom{k-1}{2}W(\varnothing),
\]
and
\[
A_{k,2}=2k^2-4k+1.
\]
At \(k=3\), this gives the source's seven-cell identity and radius \(7\epsilon\). At \(k=4\), the exact radius is \(17\epsilon\). If the baseline is known exactly, subtract its coefficient magnitude from the radius rather than charging its error again.

This result matters for bundle selection: the low-degree assumption identifies untested configurations, but uncertainty can grow with their coverage even when all tested cell errors are equally small. A sign certificate for \(W(S)\), or for an improvement relative to an exact baseline, must use the corresponding combined-cell radius. Counting separate interaction errors as independent would ignore the shared observations.

Checked locations: multilinear expansion (1), inversion (2), three-feature prediction (3), and noise bound (4). Full source/YAML were read. This is a deterministic prediction certificate under a degree restriction, not an efficient sparse experimental design or evidence that platform welfare actually has low degree. Equilibrium horizon, surplus measurement and external references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-D47-540-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/80/prb_80e1f3dc25d141cbac73e7c690253593/contributions/con_98b4478e1f6a455dbfa45fa2ed85e82a/files/D47-540.tex). Canonical revision: `rev_78061790c3b548fa84d316878d01eee5`.

