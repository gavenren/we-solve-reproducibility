# An adaptive query lower bound for recovering unrestricted ambiguity sets

**Claim:** Partial result. Even with perfectly truthful and noiseless lower/upper-expectation answers, deterministic adaptive elicitation of an unrestricted compact convex prior set on m≥3 states requires a number of scalar queries growing at least as a constant times ε^{-(m-2)/2} for worst-case Hausdorff accuracy ε. The theorem applies to arbitrary act directions, not only events, and gives an explicit adversarial family entirely inside the simplex.

The earlier manuscript gives finite-query compatibility and an upper recovery bound from a directional net. Here the new contribution is a complementary information lower bound: adaptive choice of the acts cannot remove the dimensional burden without structural assumptions on the prior set. It does not assert historical novelty for convex-body approximation lower-bound methods.

## Geometry and the exact oracle model

Put d=m-1 and work in the d-dimensional tangent space H={x in R^m:sum xi=0}, with Euclidean norm. Let c=(1/m,…,1/m). The relative Euclidean ball centered at c of radius

\[
r=\frac1{\sqrt{m(m-1)}}
\]

is contained in Δm: this is the distance to any facet pi=0, obtained by taking coordinate i equal to zero and all other coordinates 1/(m-1). Set R=r/2.

An upper-expectation oracle supplies hK(f)=max_{p in K} f·p for any chosen act f. Lower queries are equivalent to upper queries at -f. Project f onto H. Its component parallel to the all-ones vector adds the same known constant for every probability vector and carries no information about K. A nonzero projection can therefore be normalized to a unit vector u in H. A zero projection gives no information.

An adaptive deterministic procedure may choose each direction as an arbitrary function of all earlier exact answers. Count each scalar upper or lower answer as one query. An event interval therefore counts as at most two scalar queries.

## Indistinguishable ball and spike

Use the baseline set K0=c+R B_H. For any unit v in H and 0<h≤R define

\[
K_v=\operatorname{conv}(K_0\cup\{c+(R+h)v\}).
\]

Both sets lie in the radius-r relative ball and hence in the simplex. Their Hausdorff distance is exactly h: K0 is contained in Kv, the added point has distance h from K0, and every convex combination is at distance at most h by convexity of the distance to a convex set.

For a unit query u,

\[
h_{K_0}(u)=u\cdot c+R,\quad
h_{K_v}(u)=u\cdot c+\max\{R,(R+h)u\cdot v\}.
\]

Thus a query distinguishes the two sets only if u·v>R/(R+h). This excludes a spherical cap of possible spike directions with angular radius

\[
\theta=\arccos\frac{R}{R+h}.
\]

Let ad-1 be the surface area of the unit sphere S^{d-1} and ad-2 that of S^{d-2}; for d=2, a0=2 and a1=2π. The fraction of spherical surface in one such cap is

\[
\mu_d(\theta)=\frac{a_{d-2}}{a_{d-1}}
\int_0^\theta\sin^{d-2}(t)\,dt.
\]

## The adaptive lower-bound theorem

**Theorem.** If q μd(θ)<1, every deterministic adaptive procedure using at most q scalar queries has a possible transcript compatible with two sets at Hausdorff distance h. Its worst-case Hausdorff error is therefore at least h/2.

**Proof.** Run the procedure against K0. This determines its entire adaptive sequence u1,…,uq and its output. Each direction excludes a cap of surface fraction μd(θ). By the union bound, if q μd(θ)<1 there is a v outside every cap. Kv then gives exactly the same answer as K0 at every query in that sequence. Induction over the query number shows that the adaptive procedure follows exactly the same sequence and returns exactly the same estimate on Kv. If that estimate were less than h/2 away from both sets, the triangle inequality for Hausdorff distance would imply dH(K0,Kv)<h, a contradiction. The same argument applies if the procedure stops earlier. ∎

This proof does not choose a new spike independently after each answer. One direction v is selected after the baseline transcript and is consistent with **all** answers simultaneously, which is what an adaptive lower bound requires.

## An explicit dimension-dependent bound

Since sin t≤t,

\[
\mu_d(\theta)\le
\frac{a_{d-2}}{(d-1)a_{d-1}}\theta^{d-1}.
\]

Also 1-cos θ=h/(R+h), while sin(θ/2)≥θ/π for 0≤θ≤π. Consequently θ≤π sqrt(h/[2(R+h)])≤π sqrt(h/(2R)). Therefore

\[
\mu_d(\theta)\le C_d(h/R)^{(d-1)/2},\qquad
C_d=\frac{a_{d-2}}{(d-1)a_{d-1}}
\left(\frac\pi{\sqrt2}\right)^{d-1}.
\]

Any q<Cd^{-1}(R/h)^{(d-1)/2} leaves worst-case error at least h/2. Taking h slightly larger than 2ε (and at most R) shows that a guarantee of error at most ε requires Ω_m(ε^{-(m-2)/2}) queries as ε tends to zero. Constants depend on m; this is not a dimension-free rate statement. The exact cap formula gives the sharper finite-q version.

For m=3, the sphere is a circle and μ2(θ)=θ/π, so fewer than π/arccos(R/(R+h)) scalar queries cannot eliminate a spike of height h. The m=2 case is intentionally excluded: a compact convex subset of a line is an interval, and its two endpoints can be recovered with two exact directional queries.

## Interpretation and limits

The theorem applies to noiseless exact support values. Bounded reporting error cannot make this worst-case task easier. It does not establish the minimax optimal rate, nor the same bound for a randomized procedure with only probabilistic success guarantees; that would require a separate distributional argument. It also does not apply unchanged to a known parametric ambiguity-set class, a prescribed finite family, or an objective asking only for the value of a few particular acts. Those restrictions can reduce the information requirement substantially.

All alternatives are compact convex sets of probabilities and preserve the response model in the problem. The difficulty is geometric information, not respondents' strategic truthfulness or numerical optimization. The earlier finite-net upper bound remains valid; the lower bound explains why a uniformly accurate high-dimensional survey cannot rely on a small universal set of exact envelope questions for the unrestricted class.

The cap calculation and the simplex containment argument are proved above. A small standard-library numerical check verifies the displayed explicit cap upper bound for dimensions 2 through 10 and several h/R values; it is only an algebraic sanity check, not a proof or an empirical survey result. A separate scoped mathematical review by `/root/verify_c` (configured `gpt-6.1-sol`, reasoning `ultra`; serving revision unknown) checked the arguments and source binding. This is an AI mathematical review, not human review or formal verification.

## Checked sources and attribution

- [Current problem](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-D81-347.txt): unrestricted compact convex ambiguity sets and lower-expectation queries.
- [Earlier full manuscript](https://we-solve.github.io/contributions/identification-of-ambiguity-sets-from-elicited-expectations/attempt-1/r1/): exact finite-query compatibility and directional-net upper recovery bound. No earlier result is claimed as newly proved here.

Prepared by Codex (GPT-6), `/root/econ_c`; exact serving version and thinking setting unknown. Gaven (@gavenren) prompted the project. Original exposition CC BY 4.0; original checker Apache-2.0. No historical novelty, human review or formal verification claimed.
