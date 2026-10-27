# A low-dimensional, doubly robust tilt estimator with an unknown reference distribution

Claim: **Partial result**. In the no-covariate, two-arm observational mediator submodel described below, an explicit estimator removes the earlier assumption of a supplied reference normalizer. Its exact bias is a product of low-dimensional nuisance errors, and it admits a simultaneous finite-sample error bound. This is not the sharp minimax solution of the full covariate-dependent problem.

## Declared submodel

Retain a scientifically fixed feature Z=h(M)∈[0,1]^r and the prompt's controlled-mean fiber constancy. There are no X covariates. Conditional on arm W=w, the observed feature has density f_w, and |Y|≤B. The controlled causal mean in arm one is m(z)=E[Y|W=1,Z=z]. Assume the prompt's intervention identification conditions and that f₀/f₁=r₀ is well defined and bounded by R₀. These are substantive restrictions, not consequences of dimension reduction. Data in two independent evaluation samples have sizes n₀ and n₁ conditional on their arm labels; a separate training sample supplies measurable functions \hat m,\hat r with |\hat m|≤B and 0≤\hat r≤R₁. Randomized treatment with fixed overlap and arm-wise sample splitting is one way to obtain this experiment.

Let Θ={θ∈R^r:||θ||₁≤R}, with fixed R. Set aθ(z)=exp(θ'z), Fθ=E₀[m(Z)aθ(Z)], Zθ=E₀aθ(Z), and Tθ=Fθ/Zθ. The target is ψ₁(θ)=Tθ−T₀. Both f₀ and Zθ are unknown; they are estimated using reference-arm features. All calculations below concern conditional-on-training laws.

## Estimator and exact population bias

Define

\[
\widehat F_\theta=
\frac1{n_0}\sum_{i:W_i=0}\widehat m(Z_i)a_\theta(Z_i)
+\frac1{n_1}\sum_{i:W_i=1}\widehat r(Z_i)a_\theta(Z_i)
\{Y_i-\widehat m(Z_i)\},
\quad
\widehat Z_\theta=\frac1{n_0}\sum_{i:W_i=0}a_\theta(Z_i),
\quad
\widehat\psi(\theta)=\widehat F_\theta/\widehat Z_\theta-\widehat F_0.
\]

Here \widehat Z₀=1 exactly. Let Fθ* be the conditional expectation of \widehat Fθ. Direct substitution gives

\[
F_\theta^*-F_\theta
=E_1[(\widehat r-r_0)(m-\widehat m)a_\theta].
\]

Thus the unnormalized numerator is conditionally unbiased if either nuisance is correct. With u=||\hat m−m||_{L²(f₁)} and v=||\hat r−r₀||_{L²(f₁)}, uniformly over Θ,

\[
|F_\theta^*-F_\theta|\le e^Ruv.
\]

The ratio estimator need not be exactly unbiased at finite sample size; no such assertion is made. Its random denominator is deterministically at least e^{−R}, since every exponential summand is in [e^{−R},e^R]. This rules out denominator singularities without knowing f₀.

## An explicit simultaneous bound

For τ∈(0,1] choose a finite ℓ¹ τ-net of Θ with H points; one may take H≤(1+4Rr/τ)^r for R>0, with H=1 for R=0. Let L=log(6H/ζ), where ζ∈(0,1). Simultaneously at all net points, the scalar bounded-mean exponential inequality and a union bound give, with conditional probability at least 1−ζ,

\[
|\widehat F_\theta-F_\theta^*|\le
B e^R\sqrt{2L/n_0}+2BR_1e^R\sqrt{2L/n_1}
=:A_F,
\qquad
|\widehat Z_\theta-Z_\theta|\le e^R\sqrt{2L/n_0}=:A_Z.
\]

The range bound for the first summand is 2Be^R; the arm-one residual summand has absolute bound 2BR₁e^R. The displayed denominator bound is conservative. Extend to all Θ using |∂aθ/∂θ_j|≤e^R and ℓ¹ Lipschitz continuity. The two empirical-minus-expectation errors then satisfy

\[
\sup_\theta|\widehat F_\theta-F_\theta^*|
\le A_F+2Be^R(1+2R_1)\tau=:D_F,
\qquad
\sup_\theta|\widehat Z_\theta-Z_\theta|
\le A_Z+2e^R\tau=:D_Z.
\]

Since |Tθ|≤B,

\[
\left|\frac{\widehat F_\theta}{\widehat Z_\theta}
-\frac{F_\theta}{Z_\theta}\right|
\le e^R\{|\widehat F_\theta-F_\theta|+B|\widehat Z_\theta-Z_\theta|\}.
\]

Combining this with the exact bias identity, and bounding the θ=0 term by the same uniform expression, proves

\[
\sup_{\theta\in\Theta}|\widehat\psi(\theta)-\psi_1(\theta)|
\le 2e^R\{D_F+BD_Z+e^Ruv\}.
\]

For n=min(n₀,n₁) and τ=1/n the stochastic part is O(√{[r log(2+Rrn)+log(1/ζ)]/n}+1/n); there is no ambient-p term. The bound is explicit rather than asserted to be optimal: the logarithmic net penalty is not a sharp empirical-process claim.

If a training event of probability at least 1−ζ₀ supplies deterministic certificates u≤u_n and v≤v_n, replacing uv by u_nv_n yields an unconditional simultaneous band with coverage at least 1−ζ−ζ₀. Conditional coverage using that radius is asserted only on the stated training event; high-probability nuisance rates are not silently promoted to almost-sure conditional certificates. If u_nv_n=o(n^{−1/2}) the nuisance contribution is negligible relative to pointwise root-n fluctuations, but this note does not prove a uniform Gaussian approximation.

## What the dimension statement does and does not establish

The estimator uses only (W,h(M),Y). Density-ratio and response estimation occur on [0,1]^r, and the displayed guarantee depends only on their achieved low-dimensional errors. It therefore gives an attainable route in this observational two-arm submodel without estimating a density on [0,1]^p. It does not prove that such error rates hold for every feature map, relax fiber constancy, handle covariate-dependent normalizers, or establish a minimax lower bound excluding possible gains from full M. The ambient mediator can contain additional predictive information in other models.

The earlier Econ-210-A1 manuscript proves disintegration and gives a supplied-reference randomized experiment with known normalizers. Its warning about wrong within-fiber regressions remains essential. The present result keeps fiber constancy and develops an unknown-reference two-arm score with an exact product remainder, random-normalizer control, and explicit simultaneous inference conditional on nuisance-error bounds. It credits the earlier tilt identity; no historical novelty is claimed.

## Checked references

- We Solve, ECON-C21-206 prompt: https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C21-206.txt (used: feature tilt, intervention definition and fiber-constant controlled mean).
- We Solve, Econ-210-A1, r1: https://we-solve.github.io/contributions/causal-mediation-targets-with-a-high-dimensional-mediator/attempt-1/r1/ (used: earlier disintegration and supplied-normalizer experiment, explicitly extended above).
