# Lonely runners with at most one rational relation: an exact gap formula

Claim type: Partial result. This is a classical torus-method subcase with a complete proof, not a claim of a new general lonely-runner theorem.

Fix a runner in a system of $n$ distinct real speeds, subtract its speed, and write the remaining nonzero signed relative speeds as $u_1,\ldots,u_k$, $k=n-1$. Define
\[
 G(u)=\sup_{t>0}\min_i\|tu_i\|.
\]
The earlier attempt handles commensurable congruence classes and a weaker general measure bound, but explicitly leaves dependent real phases untreated. We give an exact answer when the lattice $\{a\in\mathbb Z^k:a\cdot u=0\}$ has rank zero or one:
\[
 G(u)=
 \begin{cases}
 1/2,&\text{no nonzero integer relation},\\
 1/2,&\text{one primitive relation }a,\ \sum_i a_i\text{ even},\\
 1/2-1/(2\sum_i|a_i|),&
 \text{one primitive relation }a,\ \sum_i a_i\text{ odd}.
 \end{cases} \tag{1}
\]
Changing $a$ to $-a$ does not affect the answer. Zero coefficients in the relation are allowed.

We first justify the orbit closure, including the fact that time is continuous. If $b_1,\ldots,b_d$ have no integer relation, then for every nonzero $h\in\mathbb Z^d$,
\[
 \frac1T\int_0^T e^{2\pi it(h\cdot b)}\,dt\longrightarrow0.
\]
The constant Fourier mode averages to one. Approximating continuous periodic functions uniformly by trigonometric polynomials (for example their Fejér means) proves convergence of these time averages to Haar integration on $\mathbb T^d$. In particular every nonempty open set is visited at arbitrarily large positive times: choose a nonnegative continuous function supported there with positive integral. Thus this is a density statement, not an unjustified independence assumption for a fixed tuple.

With no relation the closure is the full torus. With exactly one relation, divide its coefficients by their gcd to choose $a$ primitive. Integer Euclidean row operations extend $a$ to the first row of a unimodular matrix $M$. The first coordinate of $Mu$ is zero. Its other $k-1$ coordinates have no integer relation, because any such relation would give a relation on $u$ linearly independent of the first row. The preceding Fourier argument therefore shows that the orbit closure is exactly
\[
 H_a=\{x\in\mathbb T^k:a\cdot x=0\pmod1\}.
\]
Unimodularity is essential: it ensures the kernel is the connected torus represented by setting the first transformed coordinate to zero, with no missing finite components.

A continuous function has the same supremum on a dense orbit as its maximum on its compact closure. On $H_a$, represent each coordinate by $x_i\in[0,1]$ and write $x_i=1/2+d_i$, $|d_i|\le1/2$. Then
\[
 \min_i\|x_i\|=1/2-\max_i|d_i|,\qquad
 \frac12\sum_i a_i+\sum_i a_i d_i\in\mathbb Z.
\]
Put $A=\sum_i|a_i|$ and $S=\sum_i a_i$. The triangle inequality forces
\[
 \max_i|d_i|\ge\frac{\operatorname{dist}(S/2,\mathbb Z)}A.
\]
This bound is achieved: choose a nearest integer $m$ to $S/2$, and set
$d_i=(m-S/2)\operatorname{sgn}(a_i)/A$, with $d_i=0$ if $a_i=0$. These values lie in $[-1/2,1/2]$ and satisfy the required congruence exactly. The distance is zero for even $S$ and one half for odd $S$, proving (1). The full-torus case is attained at its center and gives the first line.

Because all $u_i$ are nonzero, a relation with $A=1$ is impossible. If $S$ is odd then $A$ is also odd, so $A\ge3$. Hence every codimension-one case has $G(u)\ge1/3$; the other cases have supremum $1/2$. For $k\ge3$ these values are strictly greater than the required $1/(k+1)$. Density therefore gives an **actual** positive time with separation strictly greater than the target, rather than only a limiting phase configuration.

For $k=2$, rank one means $u$ is a real multiple of an integer vector, so its orbit is periodic and closed. Its maximum is attained, including the possible endpoint $G=1/3$. Rank two has supremum $1/2>1/3$. For $k=1$, $t=1/(2|u_1|)$ gives the exact $1/2$ bound directly. Thus all endpoint cases needed for the deduction have been covered.

Finally let the rational dimension of the span of the differences $v_j-v_1$ be at least $n-2$. This dimension does not depend on the reference runner: each old difference is an integer difference of two new differences and conversely. For every runner its $n-1$ relative speeds therefore have at most one independent rational relation, so (1) proves that runner's required loneliness. The winning time may depend on the runner, exactly as permitted by the prompt.

This proves an infinite real-speed regime for arbitrary numbers of runners, and gives the exact gap within that regime. It leaves systems with two or more independent relative-speed relations untreated; most primitive integer tuples with many runners lie in that remaining regime. The Fourier approximation and finite-dimensional optimization are proved here, while the classical lonely-runner framework is credited to the literature. No finite tuple scan, general reduction algorithm, current computational record or full solution is claimed.
