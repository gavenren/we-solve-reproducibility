# Review: merger forecast comparisons with a common noisy benchmark

**Finding:** Supports the checked claims. **Checked scope:** unbiased scoring, simultaneous selected-model regret, and interval-identified risk comparisons in ECON-L41-549-A1, revision r1.

I expanded the paired score directly:
\[
(f_k-\widehat\tau)^2-(f_\ell-\widehat\tau)^2
=(f_k-f_\ell)(f_k+f_\ell-2\tau)-2(f_k-f_\ell)\epsilon.
\]
The quadratic benchmark error cancels exactly. Accordingly, model comparisons need no variance correction, although absolute risks do. An unbiased variance estimate may be dependent on the benchmark; expectation linearity alone suffices for the correction. The manuscript also correctly warns that truncating negative corrected risks destroys unbiasedness.

The comparison's sub-Gaussian proxy is $4\sum\nu_m^2(f_{km}-f_{\ell m})^2\sigma_m^2$, with squared cohort weights. Independent errors justify multiplying moment-generating bounds; arbitrary common macro shocks do not. A union bound over the finite pair set makes the result simultaneous. Consequently, selection of the empirical winner is covered: its observed difference from the true best is nonpositive, and its true regret is at most one comparison radius, not two. The proof correctly conditions on frozen forecasts and cohort composition.

For interval identification I checked the distinction between marginal and paired risk bounds. With one effect $\tau\in[0,1]$ and forecasts $0,1/2$, the paired difference is $\tau-1/4$, hence its sharp range is $[-1/4,3/4]$. Combining separate risk ranges would instead permit $[-1/4,1]$, overstating the upper endpoint. Linear optimization of the paired difference preserves their shared unknown effect and gives the correct range. Across mergers, endpoint choices are jointly attainable only under the stated product-box identified set.

The variance-zero boundary is handled correctly: a centered variable with zero sub-Gaussian proxy is almost surely zero, so no division by its proxy is required. Zero cohort weights likewise contribute neither risk nor uncertainty.

No mathematical error was found in this scope. This review does not check causal validity of retrospective merger estimates, cross-merger independence, price-basket definitions, cohort representativeness or any empirical ranking. The result is a conditional evaluation certificate, not an observed before/after price comparison.

