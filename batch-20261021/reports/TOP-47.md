# TOP-47 — A large prime factor theorem, small modular roots, and the remaining cofactor

**Claim type: Literature report.** Infinitely many prime values of $n^2+1$ are not established here. The report records a published large-prime-factor theorem and proves its precise consequences: infinitely many primes with unusually small square roots of $-1$, and an infinite family of quadratic values with one uniquely large prime factor and a controlled residual cofactor. It keeps the remaining cofactor, which is exactly why these statements do not prove Landau's fourth problem.

## 1. A precisely credited unconditional theorem

Let $P^+(m)$ denote the largest prime factor of an integer $m>1$. Pascadi [1] proves
\[
P^+(n^2+1)>n^{13/10}
\quad\text{for infinitely many positive integers }n.
\tag{1}
\]
The checked author version is arXiv:2404.04239v3,15January2026, Theorem1. The primary publisher record identifies the published article in Forum of Mathematics,Pi14(2026),e8, DOI10.1017/fmp.2026.10025. In that published version the theorem is numbered1.1. We identify the version used rather than mixing theorem numbers.

This bound is unconditional. The source distinguishes it from larger exponents available under Selberg's eigenvalue conjecture in earlier work; that conjecture is not assumed in (1). The substantial large-sieve, Kloosterman-sum and sieve argument is credited, not independently reproved here. No claim that13/10 is the largest currently posted exponent is needed or made.

## 2. The exact residual factorization

For each sufficiently large $n$ satisfying (1), put
\[
p=P^+(n^2+1),\qquad m=(n^2+1)/p.
\]
Then $m$ is a positive integer and
\[
m<\frac{n^2+1}{n^{13/10}}
=n^{7/10}+n^{-13/10}\le2n^{7/10}.
\tag{2}
\]
Also $p>n^{13/10}>n$ for $n>1$, so $n$ itself is a residue representative below $p$.

The prime $p$ occurs to exponent exactly one for all sufficiently large $n$. Otherwise $p^2\mid n^2+1$ would give
\[
n^2+1\ge p^2>n^{13/5},
\]
which is impossible for large $n$ because $13/5>2$. Thus $\gcd(p,m)=1$. The same comparison shows that no two prime factors can both exceed $n^{13/10}$. This makes the large factor unique; it does not bound the number of smaller prime factors in $m$.

Both alternatives $m=1$ and $m>1$ are compatible with the theorem. The first would give a prime value and the second a composite one. Inequality (2) controls the size of $m$, not its absence. Even $m=o(n)$ would not force this positive integer to equal one.

## 3. Infinitely many primes with a small root of minus one

Since $p\mid n^2+1$ and $p>n>1$, the nonzero residue $n\bmod p$ has square $-1$. For odd $p$, its multiplicative order is exactly four: its square is $-1\ne1$, and its fourth power is one. Therefore
\[
p\equiv1\pmod4.
\]
The exceptional prime two cannot satisfy the large-factor inequality for large $n$.

Rearranging (1) gives
\[
1\le n<p^{10/13}.
\tag{3}
\]
Thus there are infinitely many distinct primes $p\equiv1\pmod4$ for which $-1$ has a positive square root below $p^{10/13}$.

The word “distinct” needs proof. If only finitely many primes occurred, their maximum would be some fixed $B$, and (3) would bound every corresponding $n$ by $B^{10/13}$. There would then be only finitely many $n$, contradicting (1). This proves infinitude of the prime parameters rather than merely reusing infinitely many integers with a fixed prime divisor.

Let $r(p)$ be the smaller positive square root of $-1$ modulo such a prime. The two roots are $n$ and $p-n$ modulo $p$, so $r(p)\le n$. Consequently the same infinite family satisfies $r(p)<p^{10/13}$. This is an exact modular-root theorem derived from the credited large-factor theorem. It is weaker than demanding $n^2+1=p$.

## 4. Why neither almost primes nor a large factor supplies the missing value

The earlier contribution focuses on Iwaniec's two-almost-prime theorem and a Liouville-sign extraction criterion. That theorem controls a number of prime factors, whereas (1) controls the magnitude of the largest one. There is no right to assume that the infinite sequences supplied by two existence theorems coincide.

Even if one knew both properties for the same $n$, the possibilities would still include a product of two distinct primes with one very large factor. A sign or other argument would still be needed to force the remaining factor to be one. Conversely (1) alone allows a cofactor with many small prime factors.

The elementary example $12^2+1=145=5\cdot29$ illustrates the logical issue: $29>12^{13/10}$ (equivalently $29^{10}>12^{13}$), but the value is composite. This is a counterexample to an attempted implication, not an asymptotic counterexample or the main evidence for (1).

Nor can one reverse the modular-root consequence. A prime dividing $n^2+1$ with $n<p^{10/13}$ may leave a positive cofactor $m$. Primality of the value would require the much sharper identity $p=n^2+1$, not merely one divisibility relation and a nontrivial size comparison.

## Prior/source checks and remaining task

The complete earlier manuscript was read. Its local root counts, level-of-distribution bound, bounded-weight parity identity and almost-prime discussion are not repeated as new progress. The present theorem and its unique-factor, small-root and cofactor consequences add a different rigorously scoped approximation to the literal target.

The primary v3 PDF and HTML introduction were freshly read, including Theorem1 and the source's explicit conditional/unconditional distinction. The publisher record and abstract were independently checked for publication status and13/10. Its large computation in the sieve proof was not executed or independently certified by this report.

The deductions check $n>1$, exclusion of prime two, exact order four, reversal of the exponent inequality, distinctness of primes, the square-divisibility contradiction and the difference between small and trivial cofactors. They make no assertion about prime density, a complete asymptotic, a record exponent or an actual infinite family of prime values. Proof/source-only: no original program or external formal development was executed.

[1] Alexandru Pascadi, Large sieve inequalities for exceptional Maass forms and the greatest prime factor of $n^2+1$, Forum of Mathematics,Pi14(2026),e8, DOI10.1017/fmp.2026.10025; exact checked arXiv:2404.04239v3,15January2026, Theorem1. https://arxiv.org/html/2404.04239v3 and https://doi.org/10.1017/fmp.2026.10025.

Authorship: /root/hundred_numbers. GPT-6.1 Sol / Ultra is user-specified supplemental attribution; actual runtime configuration and time budget remain unknown.
