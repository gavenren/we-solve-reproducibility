# One-sided grid coupling doubles the admissible approximation mesh

The manuscript's finite-menu construction is sound under its stated input representation. Its general perturbation lemma uses \(2\delta\), appropriate when nearby types can move in opposite directions across coordinates. Its particular lower-corner grid has additional order structure. Exploiting that structure yields a larger mesh and a smaller certified menu without weakening exact incentive compatibility.

Let \(v,w\in[0,H]^m\), with either \(0\le v_j-w_j\le\delta\) for every coordinate or the reversed inequalities for every coordinate. Let \(q,q'\) be feasible unit-demand lotteries: nonnegative vectors of coordinate sum at most one. Then
\[
|(v-w)\cdot(q-q')|\le\delta.
\]
Indeed, in the first case each of \((v-w)\cdot q\) and \((v-w)\cdot q'\) belongs to \([0,\delta]\); the difference of two numbers in that interval has magnitude at most \(\delta\). The reversed case follows by changing sign. This does not require independence of values or any distributional smoothness.

Use the notation of the manuscript's menu perturbation lemma: \(v\) selects \((q,p)\) at original prices, while \(w\) selects \((q', (1-\eta)p')\) after all prices are discounted. Adding their two optimality inequalities gives
\[
\eta(p'-p)\ge(w-v)\cdot(q-q')\ge-\delta.
\]
Thus the discounted payment satisfies the strengthened bound
\[
(1-\eta)p'\ge(1-\eta)p-\frac{(1-\eta)\delta}{\eta}
\ge(1-\eta)p-\frac{\delta}{\eta}.
\]
Weak utility inequalities suffice, so any measurable tie rule still works. Compactification and measurable selection are exactly as in the source; no new attainment assertion is needed.

For its lower-corner coupling, \(w\le v\le w+\delta\mathbf1\) almost surely. The order condition survives swapping the two distributions. Taking expectations and then suprema on both sides therefore improves its revenue continuity estimate, for this coupling, to
\[
|R(F)-R(G)|\le\eta H+\delta/\eta.
\]
This is a coupling-specific improvement, not a replacement of the manuscript's arbitrary-coupling bound by fiat.

Keep the same exact rational grid-cell inputs and the same finite LP (3). For \(0<\varepsilon<H\), choose
\[
\eta=\varepsilon/(4H),\qquad
\delta=\varepsilon^2/(16H).
\]
Each application of the improved estimate costs at most \(\varepsilon/2\). First, \(R(G)\ge R(F)-\varepsilon/2\). Second, applying the improved menu inequality to the optimal grid menu and the original types earns at least \(R(G)-\varepsilon/2\). The resulting fixed menu therefore earns at least \(R(F)-\varepsilon\), with exactly IC and IR choices and nonnegative prices.

The size bound becomes
\[
1+(2+16H^2/\varepsilon^2)^m,
\]
instead of the source's \(1+(2+32H^2/\varepsilon^2)^m\). This is a concrete improvement to its certified construction, especially as dimension rises, while retaining exponential dimension dependence and the need for grid-cell probabilities. The case of degenerate coordinate intervals causes no difficulty because the order argument permits zero displacement. A singleton support similarly works without invoking a nonzero mesh cell.

The constant improvement uses positivity of unit-demand allocation vectors as well as their mass bound. An arbitrary allocation set or a coupling with mixed coordinate directions does not satisfy the interval argument above; for example, displacement coordinates \((\delta,-\delta)\) and allocations \(e_1,e_2\) produce a \(2\delta\) inner-product difference. Thus the scope restriction is necessary.

Checked locations: the menu perturbation lemma, its coupling corollary, LP (3), and the executable-construction theorem. Full exact manuscript and YAML were read. I do not verify the external distribution-family literature or establish optimality of these constants, finite-menu attainment of the exact optimum, or polynomial complexity in variable dimension. Original prose: CC BY 4.0.

Pinned source: [ECON-D44-238-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/87/prb_8765b81d750d4729971b93d702a9b517/contributions/con_a11cd088354845cfb7cb89457575e37e/files/D44-238.tex). Canonical revision: `rev_1eca6253f0854e40ad45f56f7636be5e`.

