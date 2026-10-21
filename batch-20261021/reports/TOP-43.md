# A binary-alphabet Unique Games gap classifier from hyperplane rounding

Problem: TOP-43  
Claim type: Partial result  
Author: /root/hundred_algorithms

**Exact scope.** For binary-alphabet permutation Unique Games, prove OPT≥1−√κ where κ is the minimum normalized signed-vector SDP violation. Consequently, for fixed rational ε,δ with ε<(1−δ)², the promised values OPT≥1−ε versus OPT≤δ are distinguishable deterministically in polynomial bit time using weak SDP optimization. This alphabet-two result does not refute or prove UGC with its tolerance-dependent larger alphabet.

Encode labels by signs x_v∈{−1,1}. Each binary permutation constraint has a sign σ_e∈{−1,1} and is satisfied iff x_u x_v=σ_e. Parallel constraints and loops are counted with their original multiplicity. For m>0 constraints consider
\[
 \kappa=\min_{X\succeq0,\ X_{vv}=1}\frac1m\sum_{e=uv}\frac{1-\sigma_eX_{uv}}2.
\]
A labeling gives the Gram matrix X=xx^T, so κ≤1−OPT. This is a positive-semidefinite relaxation, not the always-one basic local-marginal LP of the earlier alias attempt.

Every feasible X is a Gram matrix of unit vectors v_v in a finite-dimensional real Euclidean space. Pick a rotationally invariant random hyperplane normal r and round x_v=sign(r·v_v). For constraint e let θ_e be the angle between v_u and σ_e v_v. Rotational symmetry in their two-dimensional span gives violation probability θ_e/π; a zero dot product has probability zero. The same formula holds in the parallel/opposite degenerate cases and for loops. Concavity of sin on [0,π/2] gives
\[
 \theta_e/\pi\le\sin(\theta_e/2)
 =\sqrt{(1-\sigma_eX_{uv})/2}.
\]
Averaging constraints and applying Cauchy–Schwarz therefore bounds expected violated fraction by the square root of the SDP cost. Some actual labeling has violated fraction at most that expectation. Compactness of the elliptope ensures the minimum is attained; hence
\[
 \operatorname{OPT}\ge1-\sqrt\kappa. \tag{1}
\]
The geometric rounding argument is the classical Goemans–Williamson mechanism, here specialized to signed binary constraints. No exact continuous random sampler is required by the deterministic classifier below.

If OPT≥1−ε then κ≤ε. If OPT≤δ then (1) implies κ≥(1−δ)². These closed intervals have fixed positive gap g=(1−δ)²−ε. Approximate κ to additive error below g/4 and compare with their midpoint. This yields a deterministic polynomial-time promise classifier; behavior outside the promised value ranges is unrestricted. Both parameters are fixed rational constants; an equivalent input-parameter version charges polynomial dependence on log(1/g) as well as their rational encoding length.

For precision, the solver invoked is ordinary deterministic weak optimization of a rational SDP, as in Goemans–Williamson §4. The variables are the off-diagonal entries of X. The feasible region is bounded by |X_uv|≤1 and contains a relative full-dimensional ball around I: if a symmetric zero-diagonal perturbation has Frobenius norm less than 1/2, then I+E is positive definite. Thus the inner/outer radius ratio is polynomial in the number of vertices, the constraints/objective have polynomial rational encoding length, and weak ellipsoid SDP optimization to a fixed positive additive tolerance has polynomial **bit** cost. This standard solver theorem is credited; no exact optimizer, algebraic Gram factor or infinite-precision sampling oracle is claimed as a polynomial-time subroutine. Empty-edge instances can be accepted as value one by convention and treated separately.

**Quantifiers.** The result covers all growing binary instances at the stated fixed gap, not only trees or bounded cycle rank. It cannot rule out UGC: that conjecture allows a larger fixed alphabet depending on ε and δ, and binary permutations have the special signed-vector representation used here. Nor does membership of this one promise problem in P unconditionally exclude NP-hardness without a P≠NP assumption. The retained 2026 OpenAI summary asserting full UGC is not independently endorsed or used as an assumption.

**Attribution and limits.** User-requested attribution: GPT-6.1 Sol; thinking level Ultra. This is supplemental user-specified attribution. Actual runtime version, thinking settings and time budget are unknown. Author: /root/hundred_algorithms. No human mathematical review, formal verification, editorial acceptance or unperformed execution is claimed.
