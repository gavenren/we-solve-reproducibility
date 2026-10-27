# Several collateral channels reduce to a smaller nonnegative feedback matrix

The manuscript's rank-one calculation extends to several interacting collateral channels. The relevant stability statistic becomes a small matrix, and separate stable channels can jointly destabilize the economy. This is a conditional local-system result using the same relaxed comparator.

Retain \(A\ge0,\rho(A)<1,z\ge0\) and \(R=(I-A)^{-1}\). Replace \(uv^{\mathsf T}\) by \(UV^{\mathsf T}\), where \(U,V\) are nonnegative \(n\times r\) matrices. The columns represent \(r\) collateral-loss measures and their sectoral contraction loadings. Define \(K=V^{\mathsf T}RU\) and \(c=V^{\mathsf T}Rz\). Then
\[
\rho(A+UV^{\mathsf T})<1\quad\Longleftrightarrow\quad\rho(K)<1.
\]
In the stable case,
\[
x=Rz+RU(I-K)^{-1}c.
\]
Consequently aggregate amplification is
\[
1+\frac{w^{\mathsf T}RU(I-K)^{-1}c}{w^{\mathsf T}Rz}\ge1
\]
whenever the source's positive-denominator assumption holds.

For sufficiency, \(\rho(K)<1\) gives its nonnegative Neumann inverse. Direct multiplication verifies
\[
Q=R+RU(I-K)^{-1}V^{\mathsf T}R
=(I-A-UV^{\mathsf T})^{-1}\ge0.
\]
Put \(y=Q\mathbf1\ge R\mathbf1\ge\mathbf1\). Exactly as in the first source theorem, the perturbed response matrix sends \(y\) to \(y-\mathbf1\), giving a weighted sup-norm bound strictly below one.

For necessity, suppose the perturbed matrix is stable, so \(Q\) is its nonnegative inverse. The identity \(Q=R+RU V^{\mathsf T}Q\) gives \(V^{\mathsf T}QU=K+K V^{\mathsf T}QU\). Therefore
\[
(I-K)\bigl(I+V^{\mathsf T}QU\bigr)=I.
\]
A square matrix possessing a right inverse is invertible, and its inverse here is nonnegative. Let \(t=(I-K)^{-1}\mathbf1=\mathbf1+V^{\mathsf T}QU\mathbf1\ge\mathbf1\). Then \(Kt=t-\mathbf1\), and the same weighted-norm argument proves \(\rho(K)<1\). This establishes the equivalence without imposing irreducibility or strictly positive columns.

The loss equation also gives a precise instability obstruction. If \(q=V^{\mathsf T}x\), then \((I-K)q=c\). Choose a nonzero nonnegative left Perron vector \(\ell\) of \(K\). If \(\rho(K)\ge1\) and \(\ell^{\mathsf T}c>0\), multiplication gives
\[
(1-\rho(K))\ell^{\mathsf T}q=\ell^{\mathsf T}c>0,
\]
impossible for nonnegative \(q\). The excitation condition matters: an unstable component unexposed to the particular shock can coexist with finite nonnegative solutions. At \(K=\operatorname{diag}(1,0)\), \(c=(0,1)^{\mathsf T}\), the equation allows \(q=(s,1)^{\mathsf T}\) for every \(s\ge0\). Such an equilibrium is not a stable response system.

Interaction cannot be diagnosed from separate loop coefficients alone. For \(A=0\), \(U=I_2\), and
\[
V^{\mathsf T}=K=\begin{pmatrix}0&2\\2&0\end{pmatrix},
\]
each diagonal loop is zero, but the two-channel matrix has Perron root two. A positive direct shock excites that root and rules out nonnegative finite losses. Cross-channel feedback, rather than either isolated diagonal channel, causes the failure.

This reduces an \(n\)-sector stability calculation to an \(r\)-channel one when \(r\) is small. It assumes invariant local derivatives; it does not identify them from input shares or observed losses. Checked locations: the relaxed-comparator system, first theorem, edge intervention and nonidentification example. Full source and YAML were read. Nonlinear crises, causal loadings and external bibliography remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-F32-247-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/06/prb_0646dcef6ccc4afc95eeea869f260643/contributions/con_370d49ece30341e187b483f6192bc3c4/files/F32-247.tex). Canonical revision: `rev_054b709311f64606996ca66eff5ff56a`.

