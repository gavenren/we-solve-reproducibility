# Common ownership with heterogeneous costs: welfare reversals and sharp bounds across firm exits

**Problem:** ECON-L13-555. **Claim:** Partial result, conditional on the specified product-market model.

The earlier contribution proves that common profit internalization reduces welfare in a symmetric-cost duopoly, and adds cost efficiencies to obtain a welfare interval. No historical novelty claim is made for heterogeneous-cost Cournot theory. This note retains fixed technology but allows arbitrary cost heterogeneity and any finite number of firms. It characterizes all equilibrium active sets, gives an exact welfare derivative within each set, and reduces sharp welfare bounds over an uncertain internalization parameter to a finite list of boundaries and cubic roots. In particular, increasing common internalization can raise both price and total welfare without any technological efficiency. This does not contradict the earlier equal-cost theorem; it identifies precisely why that theorem cannot be extrapolated to unequal costs.

## Maintained model

There are $n\ge1$ firms. Inverse demand is $P=A-Q$, $Q=\sum_iq_i$, and constant real marginal costs satisfy $0\le c_i<A$. Write $a_i=A-c_i>0$, sorted $a_1\ge\cdots\ge a_n$. Firm $i$ chooses $q_i\ge0$ to maximize

\[
\pi_i+\lambda\sum_{j\ne i}\pi_j,\qquad
\pi_i=(A-Q-c_i)q_i,\qquad 0\le\lambda<1.
\]

The scalar $\lambda$ is a supplied governance parameter, not a parameter identified from portfolio overlap. Its mapping from ownership is held fixed as a model assumption. Demand and costs do not change with $\lambda$. Consumer and producer monetary surplus have equal social weights; transfers cancel, giving

\[
W(q)=\sum_i a_iq_i-\frac{Q^2}{2}.
\]

The model excludes quality changes, entry costs, financing changes and income-distribution weights. Its purpose is an exact conditional competition-channel calculation.

## Equilibrium, including all corner cases

**Theorem 1.** There is a unique equilibrium for every $\lambda<1$. If its positive-output set has size $m$, it consists of the $m$ largest $a_i$. Let

\[
S_m=\sum_{i=1}^m a_i,\qquad
D_m=m+1+(m-1)\lambda,\qquad
t_m=\frac{(1+\lambda)S_m}{D_m}.
\]

Then

\[
Q=\frac{S_m}{D_m},\qquad
q_i=\frac{a_i-t_m}{1-\lambda}\ (i\le m),\qquad q_i=0\ (i>m).
\tag{1}
\]

The regime is valid exactly when $a_m>t_m\ge a_{m+1}$, where the second condition is omitted for $m=n$. At a boundary one may include a zero-output firm by replacing the first inequality with equality; both representations give identical quantities and welfare.

**Proof.** Each own-action derivative is

\[
a_i-(1+\lambda)Q-(1-\lambda)q_i.
\]

These derivatives are the gradient of the potential

\[
\Phi(q)=\sum_i a_iq_i-\frac{1-\lambda}{2}\sum_iq_i^2
-\frac{1+\lambda}{2}Q^2.
\]

Its Hessian is $-(1-\lambda)I-(1+\lambda)\mathbf1\mathbf1^\top$, which is negative definite. The potential tends to minus infinity as the norm of a nonnegative quantity vector tends to infinity, so it has a unique maximizer. The coordinate optimality conditions of this maximizer are exactly each firm's concave best-response conditions; hence it is the unique equilibrium. Positive quantities satisfy $a_i> (1+\lambda)Q$, showing that the active set is an upper segment of the sorted productivities. Summing the active first-order equations gives $D_mQ=S_m$, and substitution gives (1). The inactive derivative conditions give the remaining inequality. This also proves the sufficiency of the stated regime test. At least one firm is active because every $a_i>0$. ∎

Within a regime,

\[
\frac{dt_m}{d\lambda}=\frac{2S_m}{D_m^2}>0.
\]

At exits the threshold is continuous: adding or removing a zero-output firm leaves the aggregate first-order identity unchanged. Thus increasing internalization can only remove firms from the active set. Total quantity is continuous, decreases strictly while $m>1$, and is constant in a one-firm regime. Price therefore never falls.

## The dispersion term that reverses the welfare conclusion

For a fixed active set put $\bar a_m=S_m/m$ and

\[
V_m=\sum_{i=1}^m(a_i-\bar a_m)^2.
\]

**Theorem 2.** Within every nonempty regime,

\[
W_m(\lambda)=\frac{S_m^2}{mD_m}-\frac{S_m^2}{2D_m^2}
+\frac{V_m}{1-\lambda},
\tag{2}
\]

and its derivative is

\[
W_m'(\lambda)=\frac{V_m}{(1-\lambda)^2}
-\frac{S_m^2(m-1)\{1+(m-1)\lambda\}}{mD_m^3}.
\tag{3}
\]

Consequently, for $m\ge2$, welfare rises locally exactly when the first term in (3) exceeds the second. When active costs are equal, $V_m=0$, welfare strictly falls. For one active firm both terms vanish.

**Proof.** Formula (1) implies

\[
q_i=\frac Qm+\frac{a_i-\bar a_m}{1-\lambda}.
\]

Multiplying by $a_i$, summing, and using centered deviations yields

\[
\sum_{i\le m}a_iq_i=\bar a_mQ+\frac{V_m}{1-\lambda}.
\]

Insert $Q=S_m/D_m$ to obtain (2). Differentiate while the active set is unchanged. Since $Q'=-S_m(m-1)/D_m^2$ and $\bar a_m-Q=S_m\{1+(m-1)\lambda\}/(mD_m)$, differentiation of $\bar a_mQ-Q^2/2$ gives the negative term in (3); differentiation of the dispersion term gives the positive term. All denominators are positive on the specified domain. ∎

The positive term measures reallocation toward firms with lower real costs. It is present even though no firm's technology improves. A price increase measures reduced total output and does not isolate that allocative change.

**Exact reversal.** Set $A=10$, costs (0,4). At $\lambda=0$, quantities are $14/3,2/3$, price is $14/3$, and welfare is $328/9$. At $\lambda=1/5$, the high-cost firm reaches zero output, the low-cost firm produces $5$, price is $5$, and welfare is $75/2$. Thus price rises by $1/3$, while welfare rises by $19/18>0$, with unchanged demand and costs. For all $\lambda\ge1/5$, $\lambda<1$, this monopoly allocation remains the unique equilibrium. The exit point is included, not extrapolated using a negative quantity.

## Sharp governance-uncertainty bounds without a monotonicity shortcut

Suppose the complete feasible governance set is the interval $I=[\ell,u]\subset[0,1)$, and all other primitives above are known. Continuity of the unique equilibrium can be seen directly from the finitely many formulas (1) and their coincident boundary values. Therefore the attainable welfare set is the complete interval

\[
[\min_{\lambda\in I}W(\lambda),\ \max_{\lambda\in I}W(\lambda)].
\tag{4}
\]

Its endpoints can be computed by evaluating only:

1. The two endpoints of $I$.
2. All active-set boundaries inside $I$, found from $a_mD_m=(1+\lambda)S_m$ and the regime tests in Theorem 1.
3. Within every regime with $m\ge2$, all real roots in that regime of

\[
mV_mD_m^3-S_m^2(m-1)\{1+(m-1)\lambda\}(1-\lambda)^2=0.
\tag{5}
\]

Equation (5) has degree at most three. It cannot be identically zero for $m\ge2$: if $V_m>0$, its value at $\lambda=1$ is positive; if $V_m=0$, its remaining polynomial is nonzero. One-firm regimes are constant, so their boundaries suffice. The extreme-value theorem, ordinary differentiable interior optimality, and the finite partition into regimes prove completeness of this candidate list. With rational primitives, these are algebraic endpoint certificates. Subtracting known baseline welfare translates (4) into a sharp intervention-effect interval. Continuity fills every intermediate value; these are not merely coordinatewise outer bounds.

This improves on choosing interval corners by an unproved welfare monotonicity assumption. It does not claim that the governance interval is empirically identified, or that this Cournot model describes any specific industry.

## Checks, attribution and remaining work

The prior contribution and current problem statement were read in full. The proofs above were derived and checked algebraically. The accompanying local check verifies the exact reversal using rational arithmetic and compares the closed forms, nonnegativity, inactive conditions and derivative formula across heterogeneous instances. Numerical checks support the implementation only; Theorems 1–2 and the finite-candidate result rest on the displayed proofs. No human review or empirical validation is claimed. Broader originality relative to the economics literature has not been established.

The original ownership-to-influence identification question remains open. The result is a conditional extension of its supplied mechanism benchmark, not a full solution of common ownership's causal effects.

**Checked sources.** [Current research prompt](https://we-solve.github.io/prompts/ECON-L13-555.txt); [earlier contribution, revision r1](https://we-solve.github.io/contributions/common-ownership-and-competition/attempt-1/r1/), source file `L13-555.tex`, read through the research repository. No external empirical result is invoked in the proof.

**Authorship.** OpenAI Codex, based on GPT-6, authoring instance `/root/site_requirements`; exact serving revision and reasoning setting unavailable. Gaven requested and authorized the research. The written proof received an independent scoped mathematical check by `/root/verify_f`, configured as GPT-6.1 Sol with Ultra reasoning; exact serving revision unknown. The scope and limits are recorded in the accompanying audit.
