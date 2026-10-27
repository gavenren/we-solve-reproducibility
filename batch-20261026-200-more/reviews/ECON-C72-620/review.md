# Fixed-label strategic symmetry can be recognized without a supplied witness

The source assumes a rational symmetrizing witness is supplied. For its displayed decomposition with the same action labels for both players, that witness can in fact be found or ruled out directly. The only unknown incentive scale is one positive scalar ratio. This closes a restricted recognition gap while leaving action relabelings and broader tractable classes outside scope.

Let rational square payoff matrices \(A,B\) be given. The source's witness equations are equivalent to existence of \(\lambda>0\) and a vector \(d\) such that
\[
A-\lambda B^{\mathsf T}=\mathbf1d^{\mathsf T}.
\]
Necessity follows from \(A=aM+\mathbf1r^{\mathsf T}\), \(B^{\mathsf T}=bM+\mathbf1s^{\mathsf T}\), setting \(\lambda=a/b\) and \(d=r-\lambda s\). Conversely, if this equality holds, choose \(a=\lambda,b=1,M=B^{\mathsf T},r=d,s=0\). This is a valid rational strategic-symmetry witness.

Fix the final row \(n\). Define rational differences
\[
u_{ij}=A_{ij}-A_{nj},\qquad
v_{ij}=B_{ji}-B_{jn}.
\]
The required equality is exactly \(u_{ij}=\lambda v_{ij}\) for every \(i,j\).

If some \(v_{ij}\ne0\), it determines the only possible ratio \(\lambda=u_{ij}/v_{ij}\). Reject if that ratio is nonpositive or if any remaining equality fails. Otherwise set \(d_j=A_{nj}-\lambda B_{jn}\), obtaining the witness above. If every \(v_{ij}=0\), require every \(u_{ij}=0\). If that holds, choose \(\lambda=1\); if it fails, reject. Zero denominators are therefore handled explicitly.

This is not yet the stability test. With \(M=B^{\mathsf T}\), form the source's tangent basis \(R=(e_1-e_n,\ldots,e_{n-1}-e_n)\), and test
\[
-\tfrac12R^{\mathsf T}(B+B^{\mathsf T})R\succeq0.
\]
Acceptance gives the full stable-game witness needed by its convex reduction; failure rules out every witness of the stated form, not merely the normalized one.

To prove the last assertion, suppose another witness exists with matrix \(M_0\) and scale \(b_0>0\). Then \(B^{\mathsf T}=b_0M_0+\mathbf1s_0^{\mathsf T}\). For every tangent vector \(z\), the offset contributes \(z^{\mathsf T}\mathbf1s_0^{\mathsf T}z=0\), so \(z^{\mathsf T}B^{\mathsf T}z=b_0z^{\mathsf T}M_0z\). Positive scaling preserves the required sign. Tangent stability is therefore invariant across all possible strategic witnesses and is decided by this normalized matrix.

In the all-zero-difference case, both players are indifferent among their own actions at every opponent action: \(A\) has identical rows and \(B\) identical columns. Every strategy pair is a Nash equilibrium, and the tangent quadratic vanishes. This degenerate case is correctly accepted without extracting a meaningless unique ratio.

The algorithm uses polynomially many rational differences, one ratio, equality checks, and the exact rational semidefinite test already detailed in the source. Input differences and their quotient have polynomial bit length; subsequent matrix products do as well. It is therefore polynomial bit-time recognition and witness construction for fixed labels. Combining it with the source's conditional convex-programming algorithm removes the need for the witness as an additional input within this precise subclass. I do not independently certify the external general quadratic-programming theorem invoked there.

Checked locations: witness equations (1), tangent promise (2), recognition proposition and remaining-recognition discussion. Full source/YAML were read. The result does not search over unknown action permutations, recognize asymmetric stable structures, or claim a newly discovered game class. Original prose: CC BY 4.0.

Pinned source: [ECON-C72-620-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b0/prb_b0d3209b3039477eb869f4e89c425a66/contributions/con_613b01a2d5c0499aa3c9b21cb9bcf488/files/C72-620.tex). Canonical revision: `rev_e5b96ac791134422857c49a911fb381b`.

