# Uniform discounted response-error certificates for slowly changing states

The source's finite-horizon freezing certificate (4) is valid without commuting matrices. Its dependence on the horizon permits a further theorem for the entire discounted response path, which is often the policy statistic of interest.

Retain ‖A(v)‖≤ρ<1, ‖B(v)‖≤M_B, Lipschitz constant L_A and path increment bound ‖v_{t+j}−v_t‖≤jε for every j≥1. Fix γ∈[0,1], using γ for the discount factor to avoid confusion with the policy action a. The cumulative transmission matrices
S=∑_{h=1}^∞γ^(h−1)Ψ_h(v_t),
S₀=∑_{h=1}^∞γ^(h−1)CA(v_t)^(h−1)B(v_t)
exist absolutely, since each summand's norm is at most ‖C‖M_B(γρ)^(h−1). In particular S₀=C[I−γA(v_t)]⁻¹B(v_t).

The cumulative freezing error satisfies
‖S−S₀‖ ≤ ‖C‖M_B L_A ε γ/(1−γρ)³.
Multiply by |a| to obtain the error for the cumulative intervention outcome. At γ=0 only the impact response remains and the bound correctly vanishes. The undiscounted response sum γ=1 is also legitimate because the uniform stability bound supplies summability.

For proof, apply (4) term by term for h≥2 and use the triangle inequality. The resulting scalar series is
∑_{h=2}^∞γ^(h−1)[h(h−1)/2]ρ^(h−2)=γ/(1−γρ)³.
This identity follows by differentiating the absolutely convergent geometric series twice, or multiplying its standard binomial expansion. Absolute summability justifies both the matrix subtraction and passage to the infinite sum. Thus no cancellation or matrix commutation has been assumed.

The cubic dependence is locally unavoidable for this path class. Take scalar C=B=1, v_t=0, v_{t+j}=jε, and A(v)=max(ρ−L_A v,0) for v≥0, extending it by ρ for v<0. It is L_A-Lipschitz and stays in [0,ρ]. For each fixed horizon h, differentiating the product of h−1 factors at ε=0 from the right gives
dΨ_h/dε = −L_A[h(h−1)/2]ρ^(h−2)
when 0<ρ<1. All deviations have the same sign. The source's bound supplies a summable dominating sequence for the difference quotients, so dominated convergence gives
lim_{ε↓0}|S−S₀|/ε = L_A γ/(1−γρ)³.
This proves first-order sharpness for every γ>0 without requiring an unbounded transition matrix at distant dates; the clipping preserves global stability.

The theorem strengthens approximation control, not identification. It requires the increment bound over the entire path and action-independent slow states. Endogenous investment or migration, an unstable family, an uncontrolled nonlinear remainder or a change in the post-intervention policy invalidates its assumptions. Better baseline forecasts still do not establish correct intervention contrasts.

Source: [ECON-E32-428-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/2b/prb_2bbf7e6456b14eabae6bffc532356acc/contributions/con_dc00f067181c4a92a7fc2e1de615e395/files/E32-428.tex), canonical revision `rev_9c3e1352a2554194a07cc5d5a900f6f3`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
