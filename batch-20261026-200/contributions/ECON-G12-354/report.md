# Entropy selection remains continuous at fixed-polytope calibration boundaries

**Claim:** Partial result and correction of a boundary-continuity assertion. Fix finitely many payoff columns a1,…,an in a Euclidean space, and let C=conv{a1,…,an}. For every strictly positive physical probability vector p and every b in C, minimize

\[
F_p(q)=\sum_{i=1}^n q_i\log(q_i/p_i),\qquad q\in\Delta_n,\quad \sum_i q_i a_i=b,
\]

using 0 log 0=0. Denote its unique minimizer by q*(p,b). The selector extends continuously over **all** of C, including its boundary. At a boundary it may cease to be equivalent to p; that loss of equivalence is not discontinuity of the selected probability vector or of bounded-payoff prices.

The second prior attempt's abstract conflates these two issues. Its detailed proof establishes loss of full support at boundary calibration, not discontinuity of the extended selector. This report supplies the missing boundary theorem. It does not extend the economically admissible equivalent-measure domain to boundary points by definition: the limit may lie outside that domain.

## 1. Existence and uniqueness on the closed domain

For every b in C the feasible fibre is nonempty, compact and convex. Fp is continuous on the closed simplex and strictly convex, so there is exactly one minimizer. These facts apply whether or not a strictly positive feasible q exists.

Let F be the minimal face of C containing b; b belongs to the relative interior of F. Every feasible q at b has zero mass on columns outside F. Indeed, a face of a polytope is exposed: choose a linear functional l maximized exactly on F. The equality l(b)=max_C l and nonnegative weights force each positively weighted column to lie in F. Let I={i:ai belongs to F}.

## 2. A constructive approximation lemma for boundary fibres

**Lemma.** If bn belongs to C and bn→b, every q in the fibre over b admits qn in the fibre over bn with qn→q.

**Proof.** Choose any probability representation rn of bn. Let tn be its total mass outside I. With the exposing functional from above, the finite positive gap

\[
\gamma=\min_{i\notin I}\{l(b)-l(a_i)\}>0
\]

gives tn≤[l(b)-l(bn)]/γ→0. If there are no outside columns, set tn=0. For sufficiently large n, tn<1. The normalized inside part of rn has barycentre cn in F, and cn→b because the columns are bounded and tn→0.

If F has positive dimension, choose ρ>0 so the relative ball of radius ρ around b lies in F. For cn≠b and sufficiently large n, put εn=||cn-b||/ρ and vn=b+(cn-b)/εn. Then vn belongs to F and cn=(1-εn)b+εn vn. Choose any probability representation sn of vn using columns in I. The vector un=(1-εn)q+εn sn is supported in I, has barycentre cn, and converges to q. If cn=b, use un=q. If F is a singleton, cn=b automatically, so the same choice works without a radius.

Now put qn=(1-tn)un plus the unchanged outside coordinates of rn. This is a probability vector with barycentre (1-tn)cn+sum_{i outside I}rn,i ai=bn. Also ||qn-q||1≤2tn+2εn→0. ∎

The proof uses finite-polytope geometry, not an interior-point assumption at the limiting calibration. It applies even when every limiting feasible measure has zeros.

## 3. Joint continuity with a changing physical law

**Theorem.** Suppose pn→p with every pi>0, and bn→b inside C. Then q*(pn,bn)→q*(p,b) in every finite-dimensional norm.

**Proof.** Take any convergent subsequence of the minimizers; compactness supplies one, with limit qbar in the fibre over b. Apply the lemma to q*=q*(p,b) to obtain feasible qtilde_n→q*. Entropy is jointly continuous on Δn times the strictly positive simplex: x log x extends continuously to zero, and log pn,i→log pi. Therefore optimality gives

\[
F_p(\bar q)=\lim F_{p_n}(q^*(p_n,b_n))
\le\lim F_{p_n}(\widetilde q_n)=F_p(q^*).
\]

Uniqueness gives qbar=q*. All convergent subsequences have this same limit, proving convergence of the whole sequence. ∎

For any bounded finite-state discounted payoff h, h·q*(pn,bn) consequently converges to h·q*(p,b). On any compact physical-law set with pi≥δ>0, the selector is uniformly continuous over the entire calibration polytope by continuity and compactness. No global Lipschitz modulus is asserted here.

## 4. An explicit boundary example and the correct multiplier space

Take columns a=(0,1,2), physical p=(1/3,1/3,1/3), and b decreasing to zero. Every feasible q satisfies q2+2q3=b, hence q2+q3≤b and ||q-(1,0,0)||1≤2b. In particular the entropy selector converges to (1,0,0). It loses equivalence at the limit while every bounded-payoff price converges. The inequality holds for every calibrated selector, not just entropy selection, so this cannot be explained by a special numerical optimizer.

For the normalized exponential expression qi proportional to pi exp(λ·ai), the precise multiplier invariance space is

\[
L=\{v:v\cdot a_i\text{ is the same constant for every }i\}.
\]

It is generally larger than ker Aᵀ, where A has the columns ai. Adding v in L multiplies all unnormalized weights by one common factor, which cancels. Conversely, equal positive normalized weights force (λ-λ')·ai to be constant. The covariance Hessian has kernel exactly L because Var_q(v·a)=0 iff those finitely many values are identical. Thus interior analyticity arguments should work on the quotient by L (equivalently, after deleting affine redundancy), rather than automatically on the orthogonal complement of ker Aᵀ. A normalization row is an immediate example of the extra constant direction.

## Limits and relation to earlier work

The first prior attempt correctly warns about changing constraint rank. The theorem here fixes the columns A: it does not contradict that example, and does not claim continuity under arbitrary payoff-matrix perturbations. It also requires the limiting physical law to remain strictly positive. General infinite-state markets, uniform integrability, global terminal constraints and economic justification of entropy selection remain outside the result. A continuous extension to non-equivalent measures does not establish existence in the original equivalence-constrained problem at a boundary.

The proof was checked for vertex faces, positive-dimensional faces, redundant columns and zero limiting probabilities. A separate exact checker validates the displayed three-state boundary inequality on a finite rational grid. That check is not a proof of the general theorem. Independent review is pending.

## Checked sources and attribution

- [Current problem](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-G12-354.txt).
- [Attempt 1, full manuscript](https://we-solve.github.io/contributions/selection-of-a-pricing-measure-in-incomplete-markets/attempt-1/r1/): interior continuity under constant rank and its rank-loss example.
- [Attempt 2, full manuscript](https://we-solve.github.io/contributions/selection-of-a-pricing-measure-in-incomplete-markets/attempt-2/r1/): the boundary assertion and normalized multiplier argument corrected here.

Prepared by Codex (GPT-6), `/root/econ_c`; exact serving revision and thinking setting unknown. Gaven (@gavenren) prompted the project. Original exposition CC BY 4.0; original verification code Apache-2.0. No historical novelty, human peer review or formal verification is claimed.
