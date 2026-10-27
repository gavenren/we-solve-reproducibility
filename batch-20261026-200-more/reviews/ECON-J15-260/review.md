# One wealth instrument identifies the two-state transition at three horizons

The source supplies sufficient identification using two excluded instruments observed at horizon two. Under its strictly positive feedback coefficient \(b\), one wealth instrument is enough when both state coordinates are observed through horizon three. Wealth-only observations identify a smaller collection of primitives, even with arbitrarily many exact horizons.

Maintain every exclusion and invariance condition preceding equation (7): a scalar randomized \(Z\) is independent of initial states and future innovations, acts only through date-zero wealth input, has nonzero first-stage covariance, and has zero covariance with later inputs and intercepts. Normalize the vector response by that first stage and write
\[
m_k=\frac{\operatorname{Cov}(x_k,Z)}{\operatorname{Cov}(u_0,Z)}
=M^{k-1}e_1.
\]
The date indexing is essential: \(m_1=e_1\), \(m_2=Me_1\), and \(m_3=M^2e_1\).

For \(M=\begin{pmatrix}r&a\\b&c\end{pmatrix}\), direct multiplication gives
\[
m_2=(r,b)^{\mathsf T},\qquad
m_3=(r^2+ab,\ b(r+c))^{\mathsf T}.
\]
Since the model assumes \(b>0\), these observations identify all four coefficients:
\[
r=m_{2,1},\quad b=m_{2,2},\quad
a=\frac{m_{3,1}-r^2}{b},\quad
c=\frac{m_{3,2}}b-r.
\]
Substitution verifies that these are sufficient as well as necessary. The resulting matrix must still satisfy the source's positivity and stability inequalities. Failure of those restrictions rejects this particular benchmark rather than identifying a permissible alternative automatically.

The argument has a useful rank interpretation. The matrix with columns \(e_1,Me_1\) has determinant \(b>0\), so the first wealth intervention and its propagated response span the state space. Knowing how \(M\) sends those two columns to \(Me_1,M^2e_1\) determines its action on a basis. No second intervention is needed for that purpose. By contrast, at only horizon two, the first column \((r,b)^{\mathsf T}\) leaves \(a,c\) unrestricted within the admissible region. The extra horizon supplies the missing information.

If opportunity is unobserved, let \(h_j=e_1^{\mathsf T}M^je_1\). Exact wealth responses through \(j=3\) identify
\[
r=h_1,\quad d=ab=h_2-r^2>0,\quad
c=\frac{h_3-r^3-2rd}{d}.
\]
The last identity follows from \(h_3=r^3+2rab+abc\). Individual cross-effects \(a\) and \(b\) remain unidentified, even from the entire sequence. Indeed, for any \(\tau>0\), take \(S=\operatorname{diag}(1,\tau)\). Then
\[
M_\tau=SMS^{-1}
=\begin{pmatrix}r&a/\tau\\\tau b&c\end{pmatrix}
\]
has the same eigenvalues, positivity and stability condition as \(M\), and \(e_1^{\mathsf T}M_\tau^je_1=h_j\) for every horizon. These are distinct opportunity-response mappings consistent with identical wealth responses.

This distinction has a practical mathematical implication inside the model. The permanent wealth-transfer multiplier \((1-c)/[(1-r)(1-c)-d]\) is identified by wealth impulses alone, while the wealth effect of a unit opportunity intervention depends separately on \(a\), so is not identified without fixing the opportunity scale and observing its response or another excluded input.

The \(b=0\) boundary illustrates why the positivity assumption matters: wealth interventions never reveal opportunity's feedback into wealth when that coordinate is never excited. It is excluded by the manuscript but clarifies the rank requirement. Small positive \(b\) also makes the inverse formulas sensitive to measurement error; exact identification is not a finite-sample accuracy guarantee.

Checked locations: equations (1), (2), (7), the multiplier theorem and “What identifies the mechanism?” Full manuscript and YAML were read. This sharpens its sufficient design, without calling the two-instrument statement erroneous. Exclusions, institutional invariance, empirical measurement and the external reference are not independently established. Original prose: CC BY 4.0.

Pinned source: [ECON-J15-260-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/aa/prb_aa95031fbdb247f48e2f2838d4251a0e/contributions/con_0ab8869c11824e5086e3b117576749bc/files/J15-260.tex). Canonical revision: `rev_d94a736c0a7846ab82d9e5c5627fb0fd`.

