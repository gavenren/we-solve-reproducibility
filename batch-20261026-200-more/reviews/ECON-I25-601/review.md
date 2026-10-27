# Cubic coverage activation at the supervision-efficiency threshold

The source proves that the optimal program activates when B/κ exceeds λc, with B=r_Hθ². The manner of activation is highly nonlinear. Just above that threshold, optimal coverage is cubic in the excess return while supervisory capacity is quadratic. A linear pilot-to-scale response would miss this feature even within the manuscript's own smooth positive-region model.

Retain all source parameters κ,δ,γ,c,k,λ>0 and positive capacity upper bound. Regard B as the scalar productivity-retention parameter and let B_0=κλc. Assume the attainable parameter range includes values just above B_0. Write

a=B/κ−λc>0,

and let s(a),A(a) denote the unique optimum of N(s,A)=BsA/(κA+δs)−γs²/2−λcs−λkA²/2.

First, s,A tend to zero as a↓0. To see this rigorously, objectives converge uniformly on the fixed compact feasible rectangle as B→B_0. Any subsequential limit of maximizers must maximize the threshold objective. The source proves that its unique maximizer is the origin. Hence every sequence of maximizers converges there. For sufficiently small positive a, both coordinates are positive and below their upper bounds, so the interior first-order conditions apply.

Set x=s/A. The capacity condition rearranges exactly to

A=Bδx²/[λk(κ+δx)²],
s=Bδx³/[λk(κ+δx)²].

The coverage condition is

Bκ/(κ+δx)²=λc+γs.

Since s→0 and B→B_0, this equation forces x→0. The displayed formula then gives s=O(x³). Expanding the coverage condition around x=0 gives

a=(2Bδ/κ²)x+O(x²)+γs.

As B→B_0 and s=O(x³), division by x yields a/x→2B_0δ/κ². Therefore

x/a→κ/(2λcδ).

Substituting this limit into the exact capacity and coverage formulas gives

A(a)/a²→κ/(4λ²kcδ),
s(a)/a³→κ²/(8λ³kc²δ²).

Both limits are finite and strictly positive. In particular A/s=1/x diverges like 2λcδ/(κa). The program begins with high supervisory capacity per covered pupil, even though both total capacity and coverage vanish at activation.

The displacement coefficient γ does not enter these leading constants. Its penalty is proportional to s², which is of order a⁶ along the optimal activation path. The leading supervisory and thin-coverage frictions act at lower orders. This does not make γ irrelevant away from the threshold; it influences the exact optimum and higher-order terms.

The asymptotic proof uses the exact two first-order equations after establishing interiority and convergence, rather than differentiating the objective at its nondifferentiable origin. Holding A/s fixed while approaching zero would give a strictly lower initial instructional return than B/κ, so it would not reveal the true activation path. The divergent ratio is precisely what lets the optimizer approach that maximal return while containing quadratic capacity cost.

The conclusion is local in B and requires a parameter range crossing B_0. If θ≤κ makes B_0 unattainable for the other primitives, this positive-side asymptotic is a mathematical extension outside that calibration's feasible range and should not be used as an empirical prediction. Fixed minimum program size, indivisible supervisors, staffing caps or adjustment costs also alter activation.

This supplements the source's threshold and uniqueness theorem with an exact response-shape result. It does not estimate ordinary-teacher effort, retention, national learning or the returns to a real education program, and no external novelty claim is made.

Source: [ECON-I25-601-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/20/prb_20fc5d761dce420bb32275b2e6044bac/contributions/con_4c47f53a94374b91a3bfa697a7a33c01/files/I25-601.tex), canonical revision rev_e84f60bc4ad04cdebf8cd2b046bf4e11. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
