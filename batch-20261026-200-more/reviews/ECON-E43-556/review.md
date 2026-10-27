# Unknown persistence recovery up to component labels

The source identifies component variances when distinct persistence parameters are known. In its independent stationary Gaussian model, four population autocovariances also recover the unknown persistence parameters, but only up to exchanging the economic labels. That distinction matters for identifying a “neutral” component.

Write \(U=V_q>0\), \(V=\sigma^2V_d>0\), and assume unknown distinct \(\alpha,\beta\in(-1,1)\). The observable centered covariance sequence is
\[
\Gamma_j=U\alpha^j+V\beta^j,\qquad j\ge0.
\]
Define
\[
D=\Gamma_0\Gamma_2-\Gamma_1^2.
\]
Direct expansion gives
\[
D=UV(\alpha-\beta)^2>0.
\tag{A}
\]
Thus distinct persistence and two nondegenerate independent components leave a specific observable rank signature.

Let \(S=\alpha+\beta\), \(P=\alpha\beta\). Each exponential obeys the same second-order recurrence, hence
\[
\Gamma_{j+2}=S\Gamma_{j+1}-P\Gamma_j.
\]
Using \(j=0,1\) and solving the two linear equations yields
\[
S=\frac{\Gamma_0\Gamma_3-\Gamma_1\Gamma_2}{D},
\qquad
P=\frac{\Gamma_1\Gamma_3-\Gamma_2^2}{D}.
\tag{B}
\]
The two persistence coefficients are the distinct real roots of
\(z^2-Sz+P=0\). Once an ordering is selected, their associated variances are
\[
U=\frac{\Gamma_1-\beta\Gamma_0}{\alpha-\beta},
\qquad
V=\frac{\alpha\Gamma_0-\Gamma_1}{\alpha-\beta}.
\tag{C}
\]
These formulas recover all four covariance parameters from lags zero through three.

For necessity, (A) and the recurrence establish every equation. For sufficiency within the declared two-component class, any other parameter quadruple reproducing those four autocovariances must have the same \(S,P\), hence the same two roots. Equations (C) then determine the associated weights uniquely. Consequently the only remaining covariance-parameter ambiguity is their simultaneous exchange. All later covariance values are fixed by the recurrence; in the centered Gaussian class this determines the whole observable law.

The economic label ambiguity is real. Exchanging \((\alpha,U)\) and \((\beta,V)\) preserves every observed covariance. With known \(\sigma>0\), assign the new \(q\) stationary variance \(V\) and the new demand component stationary variance \(U/\sigma^2\). Their independent innovations remain admissible. Nothing in the observed residual says which recovered persistence belongs to the neutral rate. An economically defended ordering restriction, external measurement or another exclusion is needed to attach that name to a root.

For illustration, \(\alpha=1/5,\beta=4/5,U=V=1\) produces
\[
(\Gamma_0,\Gamma_1,\Gamma_2,\Gamma_3)
=(2,1,17/25,13/25).
\]
Then \(D=9/25\), (B) gives \(S=1,P=4/25\), and the roots are exactly \(1/5,4/5\). Both economic labelings fit equally well.

If \(D=0\), the distinct-positive-components class is rejected. Equal persistence, a vanishing variance or a misspecified component model must be considered instead. Formula (A) also shows why near-coincident roots or nearly absent components make recovery unstable: the denominators in (B) shrink. Population recovery does not imply informative finite-sample estimates.

This result does not recover unknown component means, reveal realized latent states, or identify the flexible-price long-run rate. Those remain separate obstructions in the source. It adds unknown-transition parameter recovery only under its strong independence, stationarity, Gaussianity and two-component restrictions, without an empirical neutral-rate estimate.

Source: [ECON-E43-556-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b3/prb_b31220dd17134ff58aaac65685fb2c8f/contributions/con_e7c73428661e4007ba89e51c44a0ebe1/files/E43-556.tex), canonical revision `rev_8ac18c72ac7340cdb0c74f55de7b8417`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
