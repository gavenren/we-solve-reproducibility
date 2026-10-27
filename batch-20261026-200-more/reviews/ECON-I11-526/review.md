# A coalition merger prices every insurer-value interaction by its internal multiplicity

The source's two-hospital payment comparison extends to any merging coalition under the same stipulated bilateral disagreement protocol. Its sign depends on interactions in insurer network value, with an exact multiplicity weight. A graph-based substitute-value class then gives a particularly transparent aggregation rule.

Let \(N\) be a finite set of hospitals, \(V(\varnothing)=0\), and maintain strictly positive incremental surpluses for the agreements considered. Before merger, each hospital \(i\) bargains separately, taking all other agreements as fixed, so the source's Nash-product calculation gives
\[
p_i=\alpha[V(N)-V(N\setminus\{i\})].
\]
For a coalition \(C\subseteq N\) that merges into a single all-or-nothing negotiator, while outside agreements remain fixed, the postmerger coalition payment is
\[
p_C=\alpha[V(N)-V(N\setminus C)].
\]
The same \(\alpha\in(0,1)\) is used throughout. Assume total payments preserve insurer participation in both structures, just as the source explicitly does for two hospitals. This is a specified continuation protocol, not a theorem that other negotiations are invariant under every bargaining game.

Represent network value by its finite interaction coefficients
\[
\delta_T=\sum_{S\subseteq T}(-1)^{|T|-|S|}V(S),\qquad
V(S)=\sum_{T\subseteq S}\delta_T.
\]
The source's two-hospital formula is then a special case of
\[
p_C-\sum_{i\in C}p_i
=-\alpha\sum_{T\subseteq N}
\bigl(|T\cap C|-1\bigr)_+\delta_T.
\]
Here \(x_+=\max(x,0)\).

For proof, interaction \(T\) contributes \(\delta_T\) to the incremental value of hospital \(i\) precisely when \(i\in T\). Thus it enters the sum of separate coalition payments \(|T\cap C|\) times. It enters the coalition's joint incremental value once if \(T\cap C\ne\varnothing\), and zero otherwise. Subtracting gives coefficient \(1-|T\cap C|\) when the intersection is nonempty, exactly the negative positive-part expression above. Finite summation proves the identity for arbitrary interaction signs and orders.

Consequently singleton interactions never affect the merger contrast. A positive complementary interaction involving two coalition hospitals lowers their joint payment relative to separate bargaining; a negative substitute interaction raises it. An interaction involving only one coalition member has no direct coalition-payment effect under this protocol, even if other hospitals outside the coalition participate in it. Higher-order interactions are weighted by the number of their coalition participants beyond the first, rather than allocated uniformly by geography.

For a concrete class, suppose
\[
V(S)=\sum_{i\in S}v_i-\sum_{\{i,j\}\subseteq S}b_{ij},
\qquad b_{ij}\ge0,\quad v_i>\sum_{j\ne i}b_{ij}.
\]
These conditions guarantee every hospital's incremental network value is positive. Separate payments sum to \(\alpha[\sum_iv_i-2\sum_{i<j}b_{ij}]\), which is below \(V(N)\); merging coalitions also preserve participation for \(\alpha<1\), since each internal pair ceases to be counted twice and every cross-coalition pair is still counted twice. The exact coalition-merger increase is
\[
\alpha\sum_{\{i,j\}\subseteq C}b_{ij}.
\]
Thus internal insurer-overlap links add directly, while links crossing the merger boundary do not enter this particular payment contrast. For three merging hospitals with equal pair coefficients \(b\), the increase is \(3\alpha b\).

Checked locations: bargaining-payment proposition (1), insurer participation restriction and network-overlap section. Full source/YAML were read. This is a transfer-price result; quality, resources, premiums and household ownership are needed for welfare. It does not identify actual insurer values or a universal distance cutoff. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-I11-526-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/3b/prb_3bf2ef9846b94ec1aa5d6407578dc6b8/contributions/con_5e3bd239c7294c67843415d3d71ec707/files/I11-526.tex). Canonical revision: `rev_00d0893518a049c2a19db25762d15cde`.

