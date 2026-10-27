# Independent sharpness check for the global small-delay coefficient

**Finding: Supports the claim.** I checked the complete pinned manuscript and its contribution metadata. The record describes an unresolved exploration, and the manuscript conditions convergence on a particular trajectory remaining in the compact domain. The invariant-domain theorem does not contradict that conditional result. The strongest additional check is that the numerical coefficient in the sufficient bound \(a/L^2\) is asymptotically optimal over the stated class of dissipative Lipschitz fields. This supports the estimate while making its possible conservatism more precise.

The estimate in Theorem 1 survives a direct accounting check. On \([\tau,R]\), the delayed difference uses only the solution on \([-\tau,R-\tau]\); no differentiability of the arbitrary initial history is required. The double integral contributes at most \(\tau\int_{-\tau}^{R}\|x(v)\|^2\,dv\). After moving its part over \([\tau,R]\) to the left, the coefficient is exactly \(a-L^2\tau\), with the remaining history integral and \(V(\tau)\) forming the displayed constant. Compactness bounds the derivative, and uniform continuity plus square integrability proves convergence. Thus no hidden exponential-stability theorem is needed.

Here is an independent extremal family. Work in a two-dimensional tangent subspace, so at least three prices suffice. In an orthonormal basis define
\[
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 A=aI+\omega J,\qquad F(p^*+x)=-Ax,
\]
where \(a>0,\omega>0\). Then
\[
 \langle x,F(p^*+x)\rangle=-a\|x\|^2,\qquad
 \|A\|_2=L=\sqrt{a^2+\omega^2}.
\]
These are precisely the constants used by the nonlinear theorem: the rotation contributes no radial dissipation but increases the Lipschitz constant.

Set
\[
 \tau_c=\frac{\arctan(a/\omega)}{L}.
\]
Identifying the tangent coordinates with a complex variable \(z\), the delayed equation becomes \(z'=-(a+i\omega)z(t-\tau)\). At \(\tau=\tau_c\), the function
\[
 z(t)=\varepsilon e^{-iLt}
\]
is an exact solution, because
\[
 (a+i\omega)e^{iL\tau_c}=iL.
\]
Its norm is constantly \(\varepsilon\), so it does not converge. Choose \(p^*\) in the interior of the price simplex and \(\varepsilon\) small enough that the closed tangent disk of radius \(\varepsilon\) remains strictly positive. The complete initial history and this entire solution then lie in that compact disk. This meets the admissibility assumption for this trajectory; it does not assert invariance for every disk-valued history.

The ratio of this failure delay to the theorem's sufficient threshold is
\[
 \frac{\tau_c}{a/L^2}
 =\frac{L}{a}\arctan(a/\omega)
 =\frac{\arcsin(a/L)}{a/L}\longrightarrow1
 \quad\text{as }\omega/a\longrightarrow\infty.
\]
Consequently, no fixed constant \(C>1\) can replace 1 in a convergence guarantee of the form \(\tau<C a/L^2\) over all fields satisfying the manuscript's two inequalities. For any such \(C\), this family has a nonconvergent admissible solution at a delay strictly below \(C a/L^2\), once the rotational component is sufficiently large. This is an asymptotic statement across fields, not a claim that \(a/L^2\) is the exact threshold for each particular field.

The construction can also be made compatible with the manuscript's Walras-law algebra without claiming a pure-exchange implementation. Take \(D=I\), normalize \(\mathbf1^\top p=1\), and define locally
\[
 z(p)=F(p)-(p^\top F(p))\mathbf1.
\]
Then \(p^\top z(p)=0\), while \(\Pi z(p)=F(p)\), since \(F\) is tangent and \(\Pi\mathbf1=0\). This supplies a continuous Walras-compatible field on the positive neighborhood. It does not supply consumers, endowments, or a proof that these aggregate demands arise from the desired primitive preference class; that remains a separate limitation exactly as the manuscript states.

The invariant-domain proof is also sound: a history can place its endpoint at a support maximizer while its delayed endpoint generates an outward velocity. Convexity is what permits that connecting history. Finally, the scalar imaginary-root example correctly distinguishes a characteristic-root statement from a nonlinear stability conclusion. The rotating family above adds a sharper assessment of the global estimate without resolving the catalogue's unrestricted economic adjustment problem.

**Source reviewed:** [C62-182.tex at the pinned revision](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/5a/prb_5a86eaea5acb4b7c80a5f661a27e2070/contributions/con_bf6cb18f052c4244ba41010bd931c45d/files/C62-182.tex). Contribution revision: rev_205aa818f47940faaf2796eaeda97b51. The check concerns the manuscript's mathematical claims, not empirical relevance or novelty of standard delay-equation methods.

