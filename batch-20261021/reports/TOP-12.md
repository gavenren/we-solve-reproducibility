# TOP-12 — A quantitative exceptional-set theorem and a structured additive completion

**Claim type: Literature report.** The literal conjecture requires every even integer greater than two to be a sum of two primes. This report records the precise exponent and ineffectivity of a credited exceptional-set theorem, then proves an all-large-integers consequence with an additional sparse structured summand. It does not discard the third summand or promote an almost-all theorem to binary Goldbach.

Let $E(X)$ count even integers $4\le N\le X$ having no two-prime representation, with equal primes allowed.

## 1. The theorem actually checked

Pintz [1, Theorem1] states
\[
E(X)<X^{0.72}=X^{18/25}
\qquad(X>X_0),
\tag{1}
\]
where the threshold $X_0$ is ineffective. The exact checked PDF is arXiv:1804.09084v2,30April2018. Its theorem has no GRH assumption. Its proof uses the preceding papers in the author's series; this report imports the theorem and does not claim to independently reproduce that analytic argument.

Bhowmik and Grimmelt's freshly read account [2, Section6] explicitly records this bound and its ineffective sufficiently-large qualification. The checked arXiv version is v2,13August2026. Their newly published journal record was also found, but theorem numbering here refers to the exact posted version. We make no broader claim about the latest possible numerical exponent beyond the versions actually checked.

In particular (1) does not assert $E(X)=0$. Its positive upper bound grows without limit. Nor does it supply an effective $X_0$ which can be compared to an existing finite verification range.

## 2. A general translate lemma, proved with all parity conditions

Let $\mathcal A\subseteq\mathbb Z_{\ge0}$ consist of even integers. Suppose that for all sufficiently large $N$,
\[
\#(\mathcal A\cap[0,N/2])>N^{18/25}.
\tag{2}
\]
Then every sufficiently large even integer $N$ has a representation
\[
N=p+q+a,\qquad p,q\text{ prime},\quad a\in\mathcal A.
\tag{3}
\]

To prove this, take the distinct integers $N-a$ for $a\in\mathcal A\cap[0,N/2]$. They are even, lie in $[N/2,N]$, and are greater than two once $N$ is large. If none were a two-prime sum, they would give more than $N^{18/25}$ distinct exceptions at most $N$, contradicting (1). Thus one is a Goldbach number and yields (3).

This is an injective counting argument; no distribution theorem for $\mathcal A$, independence from primes, or equidistribution of the exceptional set is assumed. The strict inequality in (2) ensures the pigeonhole step even when the upper bound is not an integer.

More generally any lower bound $\#(\mathcal A\cap[0,X])\gg X^\theta$ with fixed $\theta>18/25$ implies (2), after setting $X=N/2$ and letting the positive power $N^{\theta-18/25}$ absorb the constant. At the endpoint $\theta=18/25$, the constants matter and this inference alone is unavailable.

## 3. An explicit sparse family giving an all-large-even theorem

Take
\[
\mathcal A=\{2\lfloor k^{4/3}\rfloor:k\in\mathbb Z_{\ge1}\}.
\]
The terms are even and strictly increasing. Indeed the derivative of $t^{4/3}$ is at least $4/3$ for $t\ge1$, so successive real powers differ by more than one and their floors cannot coincide.

Every integer $1\le k\le(N/4)^{3/4}$ gives
\[
2\lfloor k^{4/3}\rfloor\le N/2.
\]
Consequently
\[
\#(\mathcal A\cap[0,N/2])
\ge\left\lfloor(N/4)^{3/4}\right\rfloor.
\]
Since $3/4-18/25=3/100>0$, this count exceeds $N^{18/25}$ for all sufficiently large $N$. The translate lemma therefore proves, with the exact credited dependence on (1):
\[
\boxed{\text{Every sufficiently large even }N
=p+q+2\lfloor k^{4/3}\rfloor
\text{ for primes }p,q\text{ and }k\ge1.}
\tag{4}
\]

This is a rigorous structured additive consequence, not a probabilistic heuristic. The threshold remains ineffective because (1) is ineffective, even though the elementary comparison of the powers in the displayed count can be made explicit. The family $\mathcal A$ has sublinear counting growth of order $X^{3/4}$; the extra summand is restricted rather than arbitrary.

Statement (4) is not binary Goldbach. In particular $k\ge1$ makes the extra term at least two. One cannot choose it to be zero without changing the argument. A proof that each $N$ has a representation with some $a\in\mathcal A$ says nothing about whether zero is one of the successful shifts.

## 4. A different consequence: Goldbach numbers cannot have very long gaps

For every sufficiently large even $N$, consider the candidates
\[
N,\ N+2,\ldots,N+2K,\qquad
K=\left\lceil(2N)^{18/25}\right\rceil.
\]
For large $N$, $2K\le N$, so they all lie below $2N$. There are $K+1>(2N)^{18/25}$ candidates. By (1), at least one is a sum of two primes. Thus some Goldbach number lies at even distance at most
\[
2\left\lceil(2N)^{18/25}\right\rceil=O(N^{18/25})
\]
above every large even $N$.

Again this bounds the length of an exceptional run, not the absence of isolated exceptions. Infinite sparse exceptions could satisfy both this conclusion and (1). It also does not supply a short-interval asymptotic for the representation count.

## Prior comparison and limitations

Both complete earlier contributions were read. They derive pointwise Fourier criteria, distinguish prime powers and ordered pairs, and expose why mean-square estimates cannot prove universal positivity. They mention exceptional-set theory as context but do not record the precise Pintz theorem with the translate lemma and explicit sparse completion (4). These are the additions here.

No portion of the earlier finite verifications was rerun or claimed as new evidence. The report does not assume an exceptional set is randomly located, use GRH, replace an ineffective threshold by a numerical one, or infer a complete binary theorem from density zero. The given deductions are classical-style consequences without a historical priority claim. Proof/source-only: no program, numerical experiment or formal development was executed.

[1] János Pintz, A new explicit formula in the additive theory of primes with applicationsII. The exceptional set in Goldbach's problem, arXiv:1804.09084v2,30April2018, Theorem1. https://arxiv.org/pdf/1804.09084v2.

[2] Gautami Bhowmik and Lasse Grimmelt, The exceptional set of the Goldbach problem, checked arXiv:2607.27282v2,13August2026, Section6, especially Proposition6.4 and following conclusion; exact posted theorem account. https://arxiv.org/html/2607.27282v2.

Authorship: /root/hundred_numbers. GPT-6.1 Sol / Ultra is user-specified supplemental attribution; exact runtime configuration and time budget remain unknown.
