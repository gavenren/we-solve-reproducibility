# Policy comparisons have a sharp exposure-dependent identification threshold

The manuscript derives sharp levels of welfare under unknown actual harm. For policy evaluation, the common unknown harm must be held fixed across the two regimes. I derive the corresponding sharp comparison interval and characterize when stronger safeguards increase aggregate incident exposure despite reducing each user's incident probability.

Keep all primitives and the interior-participation assumptions of equation (1). Write \(a=V-c_0>0\), \(b=\widehat h\), and \(p_j=p(k_j)\). Consider \(k_1>k_0\), hence \(0<p_1<p_0\), with \(0<bp_j<a\) when \(b>0\). Direct integration, with no new behavioral assumptions, gives
\[
n_j=\frac{a-bp_j}{V},\quad
B_j=\frac{a^2-b^2p_j^2}{2V},\quad
X_j=p_jn_j=\frac{ap_j-bp_j^2}{V}.
\]
Here \(X_j\) is incident probability times participating mass. It is the coefficient of actual harm in aggregate welfare, and is distinct from incident probability per participant.

Set \(D=B_1-B_0-[C(k_1)-C(k_0)]\) and \(X=X_1-X_0\). The welfare improvement is exactly
\[
\Delta W_h=D-hX,\qquad
X=\frac{(p_1-p_0)[a-b(p_1+p_0)]}{V}.
\]
If \(h\in[h_L,h_U]\), its sharp identified interval is
\[
[\min(D-h_LX,D-h_UX),\ \max(D-h_LX,D-h_UX)].
\]
Every point is attained because the same observed behavior is consistent with every harm value in that interval and the displayed map is affine. This interval generally differs from subtracting two separately computed welfare intervals: that subtraction would allow the harm parameter to change between policies.

The sign of the exposure change has an exact observable threshold. For \(b>0\), stronger safeguards reduce exposure precisely when \(p_0+p_1<a/b\), leave it unchanged at equality, and increase it when \(p_0+p_1>a/b\). In the last region, induced participation outweighs the reduction in risk per user. Consequently the worst-case *improvement* uses \(h_U\) when exposure rises and \(h_L\) when exposure falls. This does not contradict the manuscript's robust choice result: the worst-case *level* at every policy still uses \(h_U\), because each level has nonnegative exposure. Robust levels and robust differences answer distinct questions.

These formulas give a complete dominance test. The stronger safeguard improves welfare for every admissible harm value if and only if the lower endpoint above is nonnegative. It strictly improves welfare for every value if that endpoint is positive. A sign-indeterminate interval means the two observed regimes cannot be ranked on those observables alone.

For a concrete check in the manuscript's units, take \(V=1,c_0=0,b=1,c=0,p_0=0.9,p_1=0.8\). Both policies have interior participation. Gross surplus rises from \(0.095\) to \(0.18\), but exposure rises from \(0.09\) to \(0.16\). Therefore \(\Delta W_h=0.085-0.07h\). For \(h\in[1,2]\), the sharp change interval is \([-0.055,0.015]\): the same observed participation and incident data allow either welfare sign. This finite comparison also independently confirms the harmful-entry mechanism behind equation (2), rather than merely substituting into its derivative.

Boundary cases are transparent: with \(b=0\), participation is fixed, exposure falls, and \(h_L\) determines the worst improvement; with \(X=0\), actual harm cancels entirely. Policies where participation clips at zero or one require the clipped formulas and are outside this derivation.

Checked locations: equation (1), the participation-margin theorem, sharp-welfare-bounds proposition, and observable-equivalence paragraph. Full YAML and manuscript were read. External references and the multi-jurisdiction extension remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-F13-228-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/eb/prb_eb4255a67b9a4bb683137b77de8bf2ee/contributions/con_42bc349b4b59415c93c7f0f6c8028366/files/F13-228.tex). Canonical revision: `rev_91fc8f34240b40039eb2fe8b569d79d6`.

