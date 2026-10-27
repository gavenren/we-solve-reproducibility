# Exponential algebraic degree in the manuscript's scalar equilibrium family

Finding: **Supports the claim**.

Reviewed source: [ECON-C63-209-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/54/prb_5407dcc1268b4f939393c72ac8436fc2/contributions/con_6bd33f554e66461e8f1203ea1e9e0a02/files/C63-209.tex), revision `rev_419ef00f956c4101abdda9b5515c9f31` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

The scalar-equilibrium theorem and the irrational example are correct. The contribution metadata describes an unresolved exploration; the manuscript explicitly disclaims a FIXP-hardness reduction and distinguishes radical expressions from efficient sign comparison. This review strengthens its encoding example: the same promised family admits unique normalized equilibrium prices of algebraic degree exponential in the number of consumers. That is a precise representation obstruction, not a complexity-hardness proof.

The demand derivation respects the wealth constraint. With \(p_2=1\), budget exhaustion leaves the strictly concave objective \(a_ix/(1+x)-tx\) on the budget-feasible interval. Any equilibrium has \(0<t<A\); otherwise all first-good demands vanish. Because each first-good allocation is at most aggregate supply \(E\), the hypothesis \(H_i>AE\) makes second-good consumption strictly positive at equilibrium. This justifies the unconstrained first-order solution
\[
 x_{i1}=\max\{\sqrt{a_i/t}-1,0\}.
\]
The aggregate demand function is strictly decreasing where positive, diverges at zero, and vanishes at \(A\), proving existence and uniqueness of its positive clearing root. The converse construction also respects budgets and clears the second good after summing the displayed allocation formula.

Now choose any \(m\) distinct primes \(p_1,\ldots,p_m\), let \(A=\max_i p_i\), and use the rational input
\[
 a_i=p_i,\qquad e_i=A,\qquad H_i=mA^2+1.
\]
Then \(E=mA\) and \(H_i>AE\), exactly as required by the manuscript. Define
\[
 t=\frac{(\sum_i\sqrt{p_i})^2}{(E+m)^2}.
\]
Since \(\sum_i\sqrt{p_i}\le m\sqrt A\),
\[
 0<t\le\frac{A}{(A+1)^2}<1<\min_i p_i.
\]
Therefore every consumer is active, and the clearing equation verifies this expression directly. The endowment sizes and the arithmetic construction are polynomial in the bit length of the prime list; the argument does not rely on expanding the equilibrium into a dense polynomial.

Consider the multiquadratic field
\(K=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_m})\). Distinct primes have independent square classes by unique factorization, so the field has degree \(2^m\), with automorphisms given by independent sign flips of its square roots. The conjugates of the numerator of \(t\) are
\[
 \left(\sum_i\varepsilon_i\sqrt{p_i}\right)^2,
 \qquad \varepsilon_i\in\{-1,1\}.
\]
Two such squared sums are equal only if their unsquared sums are equal or negatives. Indeed their difference factors as a product of the sum and difference, and a field has no zero divisors. The square roots of distinct primes are linearly independent over \(\mathbb Q\), being distinct basis elements of the multiquadratic extension. Thus equality of squared sums requires \(\varepsilon_i=\eta_i\) for every \(i\), or \(\varepsilon_i=-\eta_i\) for every \(i\).

Exactly the global sign flip leaves the square unchanged. There are consequently \(2^{m-1}\) distinct conjugates, and
\[
 [\mathbb Q(t):\mathbb Q]=2^{m-1}.
\]
The rational denominator does not change this count. Normalization does not lower the degree either: if \(p=t/(1+t)\), then \(t=p/(1-p)\), so \(\mathbb Q(p)=\mathbb Q(t)\). Both normalized price coordinates therefore have the same exponential degree.

For \(m=2\), this reproduces the type of quadratic irrationality in the source. Its explicit example gives \(t=(3+2\sqrt2)/16\), whose polynomial is \(256t^2-96t+1\); the discriminant is \(8192\), not a rational square. Its first-good demands are positive and sum to two, and \(H_i=10>4=AE\), so the example satisfies the sufficient wealth condition rather than merely solving an unconstrained formal equation.

The exponential-degree extension sharpens the output-representation distinction. An expanded minimal polynomial requires exponentially many coefficient slots solely because its degree is \(2^{m-1}\). Yet the displayed radical expression remains short. There is no contradiction: a compact arithmetic or radical description can represent algebraic numbers of large degree. Nor does this establish a lower bound for numerical approximation, whose output is a rational approximation with a specified tolerance.

It also does not establish FIXP-hardness. The construction retains a monotone one-dimensional clearing equation; the sign-flip argument concerns representation degree, not a solution-preserving reduction from general algebraic fixed points. The source's caution about sums-of-radicals comparisons remains appropriate, and no polynomial-time active-set selection algorithm is inferred here. Thus the review supports the manuscript's encoding conclusion while giving a strictly stronger algebraic witness within its own stated economy class.
