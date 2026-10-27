# Boundary point identification and cone-restricted stability without full instrument rank

The source's “A rank theorem and its boundary” correctly warns that full-rank failure need not imply nonidentification under positivity restrictions. The exact missing criterion can be stated using a feasible-direction cone, and it also yields a useful stability constant.

For clarity omit controls first and write Md=v with d≥0, retaining the source's instrument exclusions. Fix one feasible d*. Let Z={i:d*_i=0} and define the closed cone K={a:a_i≥0 for i∈Z}; coordinates positive at d* impose no sign restriction on a. Then d* is the unique nonnegative solution if and only if ker(M)∩K={0}.

If another solution d exists, a=d−d* is nonzero, Ma=0 and a_i=d_i≥0 on Z, proving necessity of the criterion. Conversely, if nonzero a belongs to the intersection, d*+ta remains nonnegative for every sufficiently small t>0: zero coordinates have nonnegative direction, while the finitely many initially positive coordinates can tolerate a sufficiently small negative perturbation. It satisfies the same moments and is distinct. This proves both directions without an assumed open interval of two-sided perturbations.

Rank deficiency can therefore coexist with identified positive beta and weights. Take
M=[[1,0,0],[0,1,1]], v=(1,0).
Nonnegativity forces d₁=1 and d₂=d₃=0. Thus beta=1 and w=(1,0,0) are uniquely identified although M has rank two rather than three. Its null vectors (0,t,−t) cannot lie in K except at zero because both second and third coordinates must be nonnegative. If v instead equals (1,1), nonnegative d₂+d₃=1 leaves an interval, illustrating how the observed boundary matters.

The same cone provides a deterministic robustness theorem. When uniqueness holds, define
κ=inf{‖Ma‖₂:a∈K, ‖a‖₂=1}.
This number is positive: the intersected unit sphere is compact, and a zero minimum would contradict the kernel criterion. For every nonnegative fitted d̂, the difference d̂−d* lies in K, hence
‖d̂−d*‖₂≤‖Md̂−v‖₂/κ.
With estimated moments M̂=M+ΔM, v̂=v+Δv and fit residual r̂=M̂d̂−v̂, this gives
‖d̂−d*‖₂≤[‖r̂‖₂+‖Δv‖₂+‖ΔM‖op‖d̂‖₂]/κ.
Thus the relevant local stability constant can remain positive even when the unrestricted smallest singular value is zero.

If beta=∑d*_i>0 and betâ=∑d̂_i>0, normalization gives
‖ŵ−w‖₁≤2‖d̂−d*‖₁/beta.
To verify it, write the difference as (d̂−d*)/beta+d̂(1/betâ−1/beta), take norms, and use |betâ−beta|≤‖d̂−d*‖₁. Small beta still makes normalized weights fragile.

With unrestricted cost/activity coefficients included, apply the identical argument to the full coefficient vector: impose nonnegative directions only on zero firm loadings and leave control directions unrestricted. The criterion is exact for this moment model, not proof of the economic instrument exclusions or survey validity. It adds no finite-sample confidence claim and does not identify weights at beta=0.

Source: [ECON-E31-439-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/15/prb_15c233de8808409d8ee46ebff6578983/contributions/con_30d3febba2a849f1bc7f180c43f48640/files/E31-439.tex), canonical revision `rev_965b964eeb1e4c08ae6d64269314360b`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
