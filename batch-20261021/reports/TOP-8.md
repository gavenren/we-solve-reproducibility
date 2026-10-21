# Odd perfect numbers: an exact barrier for formal factorization arguments

Claim type: Literature report.

The target requires a **positive odd integer** $N$ with its genuine divisor sum $\sigma(N)=2N$. Formal multiplication of geometric sums without primality can mimic this equation. The published work of the BYU Computational Number Theory Group makes this obstruction systematic. We verify a complete infinite extension mechanism and the exact arithmetic defect in the positive seed. These are barriers to a restricted proof strategy, not examples of odd perfect numbers.

For a list of integer bases and positive exponents define
\[
 \widetilde I((x_i,a_i)_i)=
 \prod_i\frac{1+x_i+\cdots+x_i^{a_i}}{x_i^{a_i}},
\]
with bases nonzero. This agrees with $\sigma(N)/N$ when the bases are distinct positive primes and $N=\prod x_i^{a_i}$. In general it is a function of the **factorization list**, not of its integer product alone. A spoof perfect factorization means $\widetilde I=2$.

The positive Descartes seed is
\[
 3^2\,7^2\,11^2\,13^2\,22021^1.
\]
The formal geometric sums do give $2$ as the product of their abundancy ratios. Indeed their first four numerator factors are $13,57,133,183$; factoring them as $13,(3\cdot19),(7\cdot19),(3\cdot61)$ and using $22022=2\cdot7\cdot11^2\cdot13$ verifies the cancellation. But $22021=19^2\cdot61$, so its actual divisor sum is
\[
 \sigma(22021)=(1+19+19^2)(1+61)=23622>22022.
\]
The bases are pairwise coprime, hence the true abundancy of the integer product is
\[
 2\,\frac{23622}{22022}>2.
\]
It is abundant, not perfect. Thus this seed cannot be rejected merely by oddness, positivity, pairwise coprimality and the **formal** equation; the omitted primality/geometric-series identification is essential.

Here is the paper's base-expansion mechanism, with a direct proof. For any integer $x$ and $a\ge1$ for which the displayed denominators are nonzero, put $S=1+x+\cdots+x^{a+1}$. Then
\[
 \frac{1+x+\cdots+x^a}{x^a}
 =
 \frac S{x^{a+1}}\frac{1-S}{-S}.
 \tag{1}
\]
To check this, the right side is $(S-1)/x^{a+1}$ and $S-1=x(1+x+\cdots+x^a)$. Consequently replacing a formal factor $x^a$ by
\[
 x^{a+1}\,(-S)^1
\]
preserves $\widetilde I$ exactly. If $x$ is odd and $a$ odd, $S$ is odd, so all new bases remain odd and the unique odd exponent moves to the new base.

Starting from the Descartes seed and its exponent-one base $x_0=22021$, repeat this operation only on the current exponent-one factor. It produces
\[
 x_{j+1}=-(x_j^2+x_j+1),
\]
leaving exponent two on $x_j$. Every $x_j$ is odd, and $|x_{j+1}|>|x_j|$ for $|x_j|\ge3$. Hence the lists are distinct, have increasing numbers of bases, never use $0$ or $-1$, and satisfy $\widetilde I=2$ at every stage by (1). Also $x_0\equiv1\pmod4$ implies $x_j\equiv1\pmod4$ for all $j$, so the formal Euler parity pattern persists. The induction is an infinite proof, not an extrapolation from a few generated lists.

After the first replacement the new exponent-one base is negative, all earlier bases have even exponents, and the represented integer product is negative. Therefore this infinite sequence does **not** give infinitely many positive candidate integers, much less prime factorizations. The paper allows negative bases in its generalized setting; importing such a family into the literal positive-integer question would change the problem. The positive seed already supplies the narrower positivity/coprimality warning, while the extension sequence supplies the all-parameter formal warning.

The same paper's Theorem6.2 states finiteness for each fixed number of bases among nontrivial odd **primitive** spoof perfect factorizations. Here primitive means no proper sublist is itself spoof perfect; nontrivial excludes bases $0,-1$. This is a credited theorem, not a claim that every family above is primitive or that our short identity reproves the source's complete finiteness argument. Fixed-base-count finiteness is compatible with the increasing-base-count construction and does not imply nonexistence.

The previous contribution derives Euler's shape, abundancy pruning and exact-exponent prime chains for actual hypothetical odd perfect numbers. The additional content here isolates which hypotheses those arguments must continue to use: actual primality, correct divisor sums, positivity and any required coprimality or primitiveness. A universal contradiction deduced only from formal multiplicative identities and odd parity cannot work because the relaxed system has these exact solutions. This is a precise restriction on a method; it neither rules out richer prime-sensitive arguments nor settles whether an odd perfect number exists. No published computation has been rerun.
