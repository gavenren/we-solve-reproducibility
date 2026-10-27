# Exact policy inference with unknown propagation and one observed outcome per loopless component

Claim: **Partial result**. For a growing union of fixed-size loopless complete components, with one observed outcome in each of a vanishing fraction of components, the aggregate policy contrast has exact conditional Gaussian-regression inference despite unknown propagation and noise parameters. Its squared-error minimax order is n⁻¹ whenever the policy contrast weight stays nonzero and the parameter class contains the stated interior submodel.

## A genuinely partially observed network family

Fix an integer k≥2. Partition N vertices into disjoint components of size k, with normalized adjacency B=(J_k−I_k)/(k−1) on each component and zero between components. Thus B is symmetric, has zero diagonal, and has operator norm one. Sample n distinct components independently of all assignments and innovations and observe one prespecified vertex i of each selected component. The n observed outcomes constitute S; all N treatments are observed. Require n→∞ and n/N→0. Within every component the unobserved neighbors therefore affect the observed vertex through the structural equations.

Treatments are independent Bernoulli(1/2). Maintain the prompt's Gaussian innovations and homogeneous parameters α,β,γ,δ,σ, with |δ|≤1−η, σ bounded above and away from zero, and all parameters in a fixed compact set. Write D_i=Σ_{j≠i,\,j\sim i}W_j, the observed number of treated neighbors. No propagation parameter or innovation variance is supplied to the estimator.

Define

\[
a=\frac\alpha{1-\delta},\quad
\kappa=\frac{\beta+\gamma}{1-\delta},\quad
\lambda=\frac{\beta-\gamma/(k-1)}{1+\delta/(k-1)},
\quad u=\lambda+\frac{\kappa-\lambda}{k},\quad
v=\frac{\kappa-\lambda}{k}.
\]

Spectral projections onto the constant vector and its orthogonal complement give the exact marginal regression

\[
Y_i=a+uW_i+vD_i+\xi_i,
\qquad \xi_i\stackrel{\rm iid}{\sim}N(0,s^2),
\]

where

\[
s^2=\sigma^2\left\{\frac1{k(1-\delta)^2}
+\frac{1-1/k}{(1+\delta/(k-1))^2}\right\}.
\]

Errors from selected components are independent and are independent of every treatment. This is the correct marginal distribution after integrating the missing outcomes, not an equation obtained by setting them to zero.

To verify the formulas, put P=J_k/k and Q=I_k−P. Then B=P−Q/(k−1), Mδ=P/(1−δ)+Q/(1+δ/(k−1)), and
Mδ(βI+γB)=κP+λQ. Its diagonal entry is u and every off-diagonal entry is v. The variance is the i-th diagonal entry of σ²Mδ², yielding the expression above.

## Target cancellation and exact confidence intervals

For arbitrary supplied policy probability vectors q⁰,q¹, put c_N=N⁻¹Σ(q¹_i−q⁰_i). Because every row and column sum of B is one,

\[
\psi_N=c_N\kappa=c_N\{u+(k-1)v\}.
\]

Let X have rows (1,W_i,D_i), let θ=(a,u,v)', and let l=(0,1,k−1)'. On rank(X)=3 and n>3, use ordinary least squares \hatθ=(X'X)⁻¹X'Y and residual variance \hat s²=||Y−X\hatθ||²/(n−3). Conditional on X,

\[
\frac{l'\hat\theta-l'\theta}
{\hat s\sqrt{l'(X'X)^{-1}l}}\sim t_{n-3}.
\]

For completeness, orthogonal projection splits the standard Gaussian error vector into independent components in range(X) and its orthogonal complement. The numerator divided by s√(l'(X'X)⁻¹l) is standard normal; (n−3)\hat s²/s² is the sum of n−3 independent squared standard normals and is independent of the numerator. Their ratio defines the stated t law. Thus the corresponding two-sided interval for κ, multiplied by c_N with endpoints ordered, has exact 1−ζ coverage conditional on the observed design. Neither δ nor σ is estimated separately. If c_N=0 the policy contrast is exactly zero and the interval is {0}.

On rank failure or n≤3, report the full prespecified feasible target range. Intersect every reported interval with this range; because the true parameter lies in it, intersection preserves coverage. A conservative fixed range is [−K,K] for κ with K=sup(|β|+|γ|)/η. This makes expected length well defined on every design event.

## Uniform risk and expected-length rates

The design rows are independent, bounded and have a positive-definite population second-moment matrix H depending only on k. Positive definiteness follows because all of (W,D)=(0,0),(1,0),(0,1) have positive probabilities and their augmented vectors are linearly independent. More explicitly, let p_* be the smallest probability of these three row types. A binomial exponential bound and a union bound imply that, except with probability at most 3e^{−c_kn}, each type occurs at least np_*/2 times. On that event X'X≽nH_* for a fixed positive-definite matrix H_*. Consequently l'(X'X)⁻¹l≤C_k/n.

On the good event, the conditional mean squared error of l'\hatθ is at most C_k s²/n and the expected t-interval length is at most C_{k,ζ}s/√n: E\hat s≤s by Jensen's inequality, and the fixed-confidence t quantiles are bounded for all sufficiently large n. Stability and compactness bound s uniformly. Clip the point estimator to [−K,K] and use any point in that interval on the bad event. Clipping cannot increase squared error. The bounded error and interval length on the bad event yield

\[
\sup_P E(\hat\psi_N-\psi_N)^2\le C c_N^2/n+Ce^{-c_kn},\qquad
\sup_P E|C_N|\le C|c_N|/\sqrt n+Ce^{-c_kn}.
\]

The upper bounds use a concrete bounded-row design argument, avoiding an unsupported assertion that a small sampling fraction by itself is harmless.

For a matching n⁻¹ lower bound assume |c_N|≥c₀>0 and that the compact class contains α=γ=δ=0, σ=σ₀>0, and β in an open interval around β₀. Compare β₀ with β₀+h/√n. Given the full treatment vector, only the n sampled outcomes depend observably on β. Their expected relative entropy is h²/(4σ₀²), since EΣ_{i∈S}W_i²=n/2. Marginalizing the random design cannot increase this value. Cauchy–Schwarz/Pinsker followed by midpoint testing gives a constant multiple of c_N²/n as a squared-risk lower bound for sufficiently small fixed h. Any interval honest at both laws similarly has expected length at least a constant times |c_N|/√n when ζ<1/2. The latter follows by transferring the second law's coverage event to the first and intersecting the two coverage events. Hence both displayed orders are sharp on this subclass.

## Identification without identification of every structural parameter

The reduced coefficients (a,u,v,s²) are identified from the marginal experiment. The original parameters need not be: for any nearby admissible δ, the equations κ=u+(k−1)v and λ=u−v determine β,γ linearly, α=a(1−δ), and σ² is adjusted to preserve s². At an interior parameter point this gives an interval of observationally equivalent structural parameter vectors. Their policy contrasts coincide. Thus estimating all original parameters is unnecessary here.

The earlier Econ-223-A1 report assumes supplied δ and σ for its general Gaussian criterion and gives a B=I example, explicitly noting its self-loops. The present family has zero diagonal, unobserved interacting neighbors at each sampled component, and unknown δ and σ, with an exact interval and matching rates. General connected graphs, heterogeneous coefficients, growing k, or correlated innovations require further work. No historical novelty or resolution of the entire graph-design classification is claimed.

## Checked references

- We Solve, ECON-C31-219 current prompt: https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C31-219.txt (used: structural model, target, sampling regime).
- We Solve, Econ-223-A1, r1: https://we-solve.github.io/contributions/generalization-when-observed-outcomes-depend-on-unobserved-outcomes/attempt-1/r1/ (used: comparison with its supplied-propagation information criterion and self-loop example).
