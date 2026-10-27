# An exact cascade criterion for selector-robust investment in many capabilities

The source's subsidy works by making one office invest strictly, after which complementarity forces the other office to invest. The same logic gives a necessary-and-sufficient criterion for a finite network of capabilities, including all mixed Nash equilibria and threshold equalities.

At the initial low state, consider \(n\) offices with binary investments \(i_j\). Specify office \(j\)'s payoff difference as
\[
-t_j+s_j+\sum_{\ell\ne j}a_{j\ell}i_\ell,
\]
where \(t_j>0\), \(s_j\ge0\), and \(a_{j\ell}\ge0\). These are declared political payoff primitives, preserving the source's short-lived-office restriction; no long-lived strategic value is silently introduced. Off-diagonal coefficients may be asymmetric or zero. The source's low-state game is the case \(n=2,t_j=c-b,a_{12}=a_{21}=a\).

Starting from \(C_0=\varnothing\), iterate
\[
C_{m+1}=C_m\cup
\left\{j:s_j+\sum_{\ell\in C_m}a_{j\ell}>t_j\right\}.
\]
The sets increase and stabilize after at most \(n\) strict expansions; call the final set \(C_\infty\). Then every Nash equilibrium invests in every capability with probability one **if and only if** \(C_\infty\) contains all offices.

First prove the forcing direction. At the first step, any newly included office has strictly positive investment gain even if every other office chooses zero. It therefore invests with probability one in every equilibrium. Inductively, offices already in \(C_m\) invest surely. Any newly included office's expected gain is strictly positive given just those forced investments; nonnegative complementarities ensure that additional investments cannot reverse it. Thus every office in \(C_\infty\) invests surely in every pure or mixed equilibrium. If the set is full, this also verifies that the all-investing profile is an equilibrium and the only equilibrium outcome.

For necessity, suppose some offices remain outside \(C_\infty\). Consider the pure profile investing exactly on \(C_\infty\). Every investing office entered at some finite stage, where its investment gain given previously admitted offices was strictly positive. It still strictly prefers investment at the larger final set. Every excluded office has gain
\[
-t_j+s_j+\sum_{\ell\in C_\infty}a_{j\ell}\le0
\]
by termination of the algorithm, so noninvestment is a best response. The proposed profile is consequently a Nash equilibrium omitting every excluded office. This supplies an explicit obstruction whenever the cascade fails.

Strict inequality is indispensable. If a subsidy only makes an office indifferent before others invest, choosing zero remains a best response; such an office cannot be treated as forced. In the source's symmetric two-office model, \(a>c-b\). The cascade is full precisely when at least one subsidy strictly exceeds \(c-b\), reproducing and extending its one-target result. Splitting that same total subsidy across two offices can fail if each receives at most the threshold.

The network version also makes targeting meaningful. For a three-office directed chain with \(t_j=1\), links \(a_{21}=a_{32}=2\), all other links zero, subsidizing office 1 by more than one forces all three investments. Subsidizing only office 3 by the same amount forces office 3 alone; the explicit failed-cascade profile is an equilibrium. These claims follow directly from the iteration, with no equilibrium-selection assumption.

To obtain persistent capacity after the initial intervention, retain complete depreciation and assume that owning a capability adds a persistence payoff \(\eta_j>t_j\). Once all capabilities are built, every office then invests strictly even without subsidies, so the full state sustains itself. This persistence conclusion is separate from the initial cascade criterion and from welfare: investment resource costs and output gains still require the source's accounting.

Checked locations: political game (1), conditions (2), both equilibrium and escape-threshold theorems. Full manuscript/YAML were read. The extension does not identify network coefficients, optimize the subsidy budget, or establish welfare improvement. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-H11-300-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ab/prb_aba956a74d6a40cbb0ef3e619de57e9b/contributions/con_1bec8590801749ba876827f7ca1968b3/files/H11-300.tex). Canonical revision: `rev_e879eeaf6fc74d41a6d6b3aac569120b`.

