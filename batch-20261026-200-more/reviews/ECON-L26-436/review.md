# Sharp joint error bounds for four-block Shapley attribution with known endpoints

The source proves a valid \(2\epsilon\) error bound for each four-block Shapley contribution when every hybrid value has error at most \(\epsilon\). If observed initial and final indices are exact, the hybrid errors have more structure. Individual uncertainty shrinks, and the full attribution vector satisfies a sharp joint bound substantially tighter than summing individual bounds.

Assume \(e(S)=\widehat v(S)-v(S)\) satisfies \(|e(S)|\le\epsilon\) for the fourteen nontrivial hybrids, with \(e(\varnothing)=e(K)=0\). Let \(\Delta_j=\widehat\phi_j-\phi_j\). Linearity of the source's Shapley formula gives \(\Delta_j=\phi_j(e)\). Efficiency implies
\[
\sum_{j=1}^4\Delta_j=e(K)-e(\varnothing)=0.
\]
Thus separate coordinate error intervals cannot be interpreted as independent.

For a fixed block \(j\), every positive coalition coefficient has the same total weight one, as do the negative coefficients. The positive endpoint \(e(K)\) and negative endpoint \(e(\varnothing)\) each have coefficient \(1/4\). Removing their now-zero contributions leaves total absolute coefficient mass \(2-1/4-1/4=3/2\). Consequently
\[
|\Delta_j|\le3\epsilon/2.
\]
This is sharp: choose each nontrivial hybrid error at \(\epsilon\) times the sign of that coordinate's coefficient. Such errors meet the assumed hybrid box restrictions and attain equality. This is a worst-case numerical certificate, not a claim that every structural equilibrium family realizes every such error pattern.

The exact joint bound is
\[
\sum_{j=1}^4|\Delta_j|\le\frac{10}{3}\epsilon.
\]
To prove it, use \(\|\Delta\|_1=\max_{\sigma_j\in\{-1,1\}}\sum_j\sigma_j\Delta_j\). Fix a sign pattern with \(m\) positive signs. For a coalition \(S\) of size \(k\), let \(r\) be its number of positive-sign members. Its coefficient in this signed attribution sum is
\[
\frac{2(4r-km)}{k(4-k)\binom4k},\qquad k=1,2,3.
\]
This follows because a block inside \(S\) has coefficient \(1/[k\binom4k]\), while a block outside has coefficient \(-1/[(4-k)\binom4k]\). Multiplying each error by its coefficient and summing absolute values therefore gives its exact support-function bound.

The coalition counts yield the following absolute coefficient totals, with the first and third rows symmetric:

| Coalition size | One positive sign | Two positive signs |
|---|---:|---:|
| 1 | \(1\) | \(4/3\) |
| 2 | \(1\) | \(2/3\) |
| 3 | \(1\) | \(4/3\) |
| Total | \(3\) | \(10/3\) |

Three positive signs give the same total as one by sign reversal; zero or four give zero. Hence the maximum is \(10/3\). Sharpness follows by selecting a two-positive sign pattern and setting each hybrid error to \(\epsilon\) times its displayed coefficient sign. Its signed error sum is \(10\epsilon/3\), so its l1 norm attains the upper bound as well. Zero coefficients can receive zero error.

For comparison, independently summing the four sharp individual bounds would give \(6\epsilon\), which overlooks their exact dependence. The joint bound can therefore certify the total possible reallocation of the fixed observed dynamism change more tightly.

Checked locations: Shapley definition (1), interaction formula (2), and counterfactual-evaluation error section. Full manuscript/YAML were read. If endpoints are estimated, their errors must be restored; these constants then need not apply. The calculation propagates evaluation uncertainty, without identifying structural histories or empirical drivers. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-L26-436-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/cd/prb_cd3398326e204488b90973a96fc38c74/contributions/con_0b6dc7fb7eb34d91984c95c332a52b65/files/L26-436.tex). Canonical revision: `rev_5315a70ab64d4779b481c99d683dc4cc`.

