# A robust arithmetic criterion for RH and its error scale

Claim type: **Literature report**.

The selected problem asks for the location of every nontrivial zeta zero, with no simplicity condition. A classical equivalent formulation uses divisor sums and harmonic numbers. We give its quantitative scale and prove a robust eventual version:
\[
 \boxed{\quad \mathrm{RH}\ \Longleftrightarrow\
 \exists K\ge0\ \exists n_0\
 \forall n\ge n_0:\quad
 \sigma(n)\le H_n+e^{H_n}\log H_n+
                       K\frac n{\sqrt{\log n}}.\quad}
 \tag{1}
\]
Here $H_n=\sum_{j=1}^n1/j$ and $\sigma(n)=\sum_{d\mid n}d$. The right side is not established here. Formula(1) is a consequence of credited classical results, not a claimed new solution.

The precise deep inputs, checked in Lagarias's original paper, are Robin's two assertions as stated there. If RH holds, then
\[
 \sigma(n)\le e^\gamma n\log\log n\quad(n\ge5041).
 \tag{2}
\]
If RH fails, there exist $C>0$ and $0<b<1/2$ such that, for infinitely many$n$,
\[
 \sigma(n)\ge e^\gamma n\log\log n+
                 C\frac{n\log\log n}{(\log n)^b}.
 \tag{3}
\]
Lagarias Propositions3.1–3.2 attribute these to Robin. The original Robin paper was not independently reread; this report relies on their exact formulation in the checked primary Lagarias argument. In particular the positive oscillation in(3), not just a failure at one unknown integer, is the key input.

We first control the difference between the harmonic threshold and the Robin threshold. Put
$F(n)=H_n+e^{H_n}\log H_n$ and$L=\log n$. Elementary integral comparison gives
\[
 H_n=L+\gamma+r_n,\qquad0<r_n<1/n.
 \tag{4}
\]
For example the exact tail expression
$r_n=\int_n^\infty\{t\}t^{-2}\,dt$ in Lagarias's proof gives these strict bounds. Therefore
\[
 e^{H_n}=e^\gamma n(1+O(1/n)),\qquad
 \log H_n=\log L+\frac{\gamma}{L}
                         +O(L^{-2})+O((nL)^{-1}).
\]
Multiplying and adding$H_n$ proves
\[
 F(n)=e^\gamma n\log\log n+
           e^\gamma\gamma\,\frac n{\log n}
           +O\!\left(\frac n{(\log n)^2}\right).
 \tag{5}
\]
The terms$O(\log n+\log\log n)$ can be absorbed into the final error for sufficiently large$n$. This expansion exhibits the first extra allowance, rather than treating the two thresholds as identical.

For$n\ge3$, (4) also gives$e^{H_n}>e^\gamma n$ and
$\log H_n\ge\log\log n>0$. Thus
\[
 F(n)>e^\gamma n\log\log n.
 \tag{6}
\]
If RH holds, (2) and(6) establish the right side of(1) with$K=0$ and$n_0=5041$. No small-integer computation is required for this **eventual** criterion.

Conversely suppose the right side of(1) holds but RH fails. At the infinitely many unbounded integers in(3), combine(3) with(5) and the assumed inequality. After dividing by$n$ this requires
\[
 C\frac{\log\log n}{(\log n)^b}
 \le O((\log n)^{-1})+
                         K(\log n)^{-1/2}.
\]
Multiply by$(\log n)^{1/2}$. The left side is
$C(\log n)^{1/2-b}\log\log n\to\infty$, while the right side is bounded. This contradiction proves(1). The fixedness of$K$ is essential; permitting an arbitrary growing$K(n)$ changes the statement.

The same calculation gives an informative limitation for weaker tolerances. An error$n/(\log n)^\alpha$ with$\alpha<1/2$ does not yield this contradiction for every$b<1/2$: one would need$b<\alpha$. Hence the displayed proof cannot replace the exponent$1/2$ by an arbitrary positive exponent and still claim an RH equivalence. This is a limitation of the deduction, not a theorem that weaker arithmetic criteria are impossible.

Lagarias's full Theorem1.1 states the sharper all-integer criterion
$\sigma(n)\le F(n)$ for every$n\ge1$, with equality only at1. Its paper also credits a computer check up to5040 in proving that exact formulation. That historical finite check was not rerun here. Our eventual formulation avoids relying on any fresh finite computation, while the stated original criterion remains fully attributed.

The earlier main contribution uses inverse-zero logarithmic moments, polynomial isolation and finite-test obstructions. Other records describe unaudited full or partial zero-free claims. The present arithmetic route is separate: it gives a checked published-era criterion, derives its exact first-order tolerance, and shows how the oscillation theorem survives a substantially larger square-root-logarithmic allowance. Establishing(1)'s inequality uniformly for all sufficiently large integers is still the missing work. A finite test, or the asymptotic expansion(5) alone, does not prove it.
