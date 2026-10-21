# The BSD majority theorem and the thin-family boundary

Claim type: **Literature report**.

The selected assertion is the rank equality for **every** elliptic curve over $\mathbb Q$; it explicitly excludes the leading-coefficient refinement. A major known regime proves this exact equality for a positive proportion of curves in a specified ordering. This report states that regime precisely and proves why it cannot be transferred automatically to the congruent-number families prominent in the earlier attempt.

Bhargava–Skinner–Zhang, arXiv:1407.1826v2, define minimal integral short models and
\[
 H(E_{A,B})=\max(4|A|^3,27B^2),\qquad
 \mathcal E(X)=\{E/\mathbb Q:H(E)<X\}.
\]
Their Theorems1–2 and displayed formula(1) give the **joint** bound
\[
 \liminf_{X\to\infty}
 \frac{\#\{E\in\mathcal E(X):
       r(E)=r_{\rm an}(E),\ \Sha(E/\mathbb Q)\text{ finite}\}}
      {\#\mathcal E(X)}
 >0.6648.
 \tag{1}
\]
The paper is a checked2014 preprint; no journal publication is claimed here. Its deep modularity, Selmer-statistics and Euler-system ingredients are credited. In particular (1) is not a consequence of a finite list of curve computations.

The source separately gives lower proportions16.50% for simultaneous arithmetic and analytic rank0, and20.68% for simultaneous rank1. Those separate lower bounds do not sum to the stronger joint percentage in (1). The paper explains that optimizing the union gives a better bound than summing the separately optimized estimates. Finiteness of $\Sha$ in (1) is extra information, not the leading-coefficient formula omitted by the literal prompt.

Here are quantitative consequences and limitations that require only (1). First, there are infinitely many $\mathbb Q$-isomorphism classes satisfying the selected equality. Indeed $\#\mathcal E(X)\to\infty$, and (1) eventually makes the numerator at least, for example, $0.66\#\mathcal E(X)$. Second, its complement has upper density less than0.3352 in this height ordering. This is not a claim that every curve in that complement violates BSD: the complement includes any curve not established by the property being counted, and a density estimate does not label individual curves.

For clarity, one can prove without a model-counting asymptotic that
\[
 \#\mathcal E(X)\asymp X^{5/6}.
 \tag{2}
\]
The upper bound counts all integral pairs with
$|A|<(X/4)^{1/3}=U$ and $|B|<(X/27)^{1/2}=V$.
For a lower bound, take positive squarefree $A<U$ and arbitrary integral $|B|<V$. These models are minimal in the required sense, since no prime fourth power divides $A$, and nonsingular because $4A^3+27B^2>0$. There are $\gg U$ such $A$: the number excluded by a prime square is at most
\[
 U\sum_{p\le\sqrt U}p^{-2}+\sqrt U
 \le U\sum_{n\ge2}n^{-2}+\sqrt U.
\]
The series on the right is strictly less than1; for example
$\sum_{n\ge2}n^{-2}<1/4+\int_2^\infty t^{-2}dt=3/4$.
Thus a positive fraction remains. Distinct minimal short pairs represent distinct $\mathbb Q$-isomorphism classes, proving (2).

Now all short models with $j=1728$ have $B=0$, hence there are only $O(X^{1/3})$ of them below height$X$. Dividing by (2) gives density
\[
 O(X^{-1/2})\longrightarrow0.
 \tag{3}
\]
The congruent-number family
\[
 E_n:y^2=x^3-n^2x,\quad n\ge1\text{ squarefree},
\]
is thinner still: its displayed models satisfy the minimality condition and have height$4n^6$. Therefore there are $O(X^{1/6})$ such classes of height$<X$, with relative density
\[
 O(X^{-2/3})\longrightarrow0.
 \tag{4}
\]
Possible repetitions only decrease these upper bounds.

Consequently (1) alone does not settle even one prescribed member of this family, nor a positive proportion within it. Abstractly, a set of global density greater than0.6648 may be disjoint from a prescribed zero-density subset. The estimate cannot be conditioned on that subset without a new theorem. Equations(3)–(4) locate this issue quantitatively instead of treating a global majority as a family-wise majority.

The earlier contributions include extensive congruent-number searches, rational-point/descent certificates and analytic enclosures. Their source and proof sections were read; their large computational appendices were not independently rerun here. The present addition is the independently checked statistical theorem and the full thin-family comparison above. Neither a majority theorem nor many verified special curves changes the universal quantifier. Arbitrary-rank individual BSD, and any assertion of a full leading-coefficient formula, remain beyond the result reported.
