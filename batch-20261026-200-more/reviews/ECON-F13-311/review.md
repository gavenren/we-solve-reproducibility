# Global mandate threshold and a unique closed-form optimum

The source proves that \(g>\delta/2\) is sufficient for a locally beneficial mandate when baseline entry is strict. In its declared benchmark, that threshold is also globally necessary. Moreover the conditional-on-entry welfare curve is unimodal whenever a positive mandate can help, so its optimum can be written explicitly and then truncated by the entry constraint.

Let \(m=A-1>0\), \(\delta=c_0-1>0\), and use the source's \(\kappa\ge0\). On the positive-output region \(0\le\ell<m/\delta\),
\[
8W(\ell)=\frac{m^2+b\ell+c\ell^2}{1+\kappa\ell^2},
\quad
b=m(4g-2\delta),\quad c=\delta(\delta-4g).
\tag{A}
\]
This is obtained by combining the two terms of equation (2), rather than changing its ownership boundary. Put \(C=c-\kappa m^2\). Subtracting baseline welfare gives
\[
8\{W(\ell)-W(0)\}
=\frac{\ell(b+C\ell)}{1+\kappa\ell^2}.
\tag{B}
\]

If \(g\le\delta/2\), then \(b\le0\). If \(c\le0\), also \(C\le0\), and (B) is strictly negative for positive feasible output. If \(c>0\), use \(\ell<m/\delta\) to obtain
\[
b+C\ell\le b+c\ell<b+cm/\delta=-m\delta<0.
\]
Thus no positive mandate with entry can improve national welfare. An exit policy has welfare zero and cannot beat the positive-output baseline. This proves global necessity, including \(g=\delta/2\), where the first derivative vanishes but every positive mandate is still worse.

If \(g>\delta/2\), then \(b>0\), \(c<0\) and \(C<0\). Differentiating (A), the sign of \(W'\) is the sign of
\[
N(\ell)=b+2C\ell-\kappa b\ell^2.
\tag{C}
\]
For every \(\ell\ge0\), \(N'(\ell)=2C-2\kappa b\ell<0\), and \(N(0)=b>0\). It has exactly one positive zero. Hence welfare increases strictly until that zero and decreases strictly afterward. The unconstrained optimum is
\[
\ell_0=
\begin{cases}
-b/(2C),&\kappa=0,\\
b/(\sqrt{C^2+\kappa b^2}-C),&\kappa>0.
\end{cases}
\tag{D}
\]
The second expression is the rationalized positive quadratic root, avoiding cancellation. The root lies strictly below \(m/\delta\): welfare is positive at zero and tends to zero at the positive-output boundary, so its strictly unimodal maximum must precede that boundary.

Operating profit in equation (1) decreases strictly on the positive-output region. Its entry-supporting policies therefore form an initial interval. If baseline profit is strictly above \(F\), that interval contains a neighborhood of zero. The unique global policy optimum is the smaller of \(\ell_0\), one, and the positive-output entry boundary, whenever that boundary binds. At a positive-cost entry threshold the source's entry-at-equality convention includes the boundary. If \(F=0\), the output-zero boundary may be excluded from entry, but it cannot obstruct the interior maximizer in (D). Exit policies cannot improve upon the attained positive welfare maximum.

Thus, under strict baseline entry, a positive policy improvement exists if and only if \(g>\delta/2\). If baseline entry is exactly indifferent, every positive mandate can instead cause immediate exit; strict entry is essential to the sufficiency statement. If baseline profit is below \(F\), no mandate induces entry, by profit monotonicity.

This strengthens the source's one-dimensional numerical prescription into a global analytical solution for its specific procurement conduct and national ownership weights. It does not identify the learning parameter from sourcing data, compare subsidies with mandates under another equilibrium, or extend the threshold to competitive final production.

Source: [ECON-F13-311-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/6d/prb_6dbb012628b64d2f97a8d831b85a9b01/contributions/con_09357af5c76b47348b7500453784e6eb/files/F13-311.tex), canonical revision `rev_e6ee0d1c2cd34866b45ad387b4d4aab6`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
