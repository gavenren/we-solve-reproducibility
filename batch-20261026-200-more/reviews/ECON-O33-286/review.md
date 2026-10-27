# A strict welfare-optimal adoption cap under unequal factor ownership

The manuscript proves that expanded automation capability weakly raises output while some labor owners can lose. Its household-income formula permits a sharper normative result: with welfare weights equal to labor shares, unequal factor ownership yields a unique preferred adoption cutoff strictly below the output-maximizing cutoff. This is a conditional welfare theorem in the declared economy, not a universal recommendation about AI restrictions.

Retain the source's fixed K,L, positive continuous nonincreasing productivity a, and cutoff output H(s). Let finitely many household groups have labor shares ℓ_i>0 summing to one and capital shares k_i≥0 summing to one. Choose the explicit normative weights ω_i=ℓ_i. Define m_i(s)=(1−s)ℓ_i+sk_i, which is strictly positive for 0≤s<1. The source's log welfare is

W(s)=H(s)+∑ℓ_i log m_i(s).

Add and subtract ∑ℓ_i log ℓ_i to write this as

W(s)=H(s)+∑ℓ_i log ℓ_i−D(s),
D(s)=∑ℓ_i log[ℓ_i/m_i(s)].

The last term measures the discrepancy between labor ownership and the resulting income shares. Its role here follows directly from the algebra, rather than from an assumed welfare interpretation of an external inequality index.

Differentiation is legitimate for s<1 and gives

D'(s)=−∑ℓ_i(k_i−ℓ_i)/m_i(s),
D''(s)=∑ℓ_i(k_i−ℓ_i)²/m_i(s)².

Consequently D(0)=D'(0)=0. If k differs from ℓ in at least one coordinate, D'' is strictly positive throughout [0,1), so D'(s)>0 and D(s)>0 for s>0. This proves a strict ownership penalty even when every group's total income remains positive.

The source establishes H'(s)=log[a(s)K(1−s)/(Ls)], which is continuous and strictly decreasing. It tends to infinity at zero and vanishes at the unique output-maximizing cutoff s°. No derivative of a is needed. Therefore W'(s)=H'(s)−D'(s) is continuous and strictly decreasing on (0,s°]. It tends to infinity as s↓0, since the finite-group D' has limit zero. At s° it is strictly negative whenever ownership differs. There is exactly one root s_W∈(0,s°), and W increases before s_W and decreases afterwards up to s°. This proves existence and uniqueness of the welfare-optimal technologically induced adoption level.

Because equilibrium adoption is s(b)=min{b,s°}, choosing a capability cap b=s_W implements this optimum. Every b>s_W gives lower welfare, including those above s° that induce the same output-maximizing allocation. If policy may only expand capability from an existing b_0, the optimal choice is s_W when b_0≤s_W and no further expansion when b_0>s_W. These conclusions require that withholding capability is feasible without a separate cost or distortion, exactly as the cap variable is treated in the benchmark.

An explicit instance illustrates the result. Set a=1 and L=K=1, so s°=1/2. Take two equal labor shares, capital shares (1,0), and equal welfare weights. Then

W'(s)=log[(1−s)/s]−s/(1−s²).

At s=1/4 this is log3−4/15>0; for example log3>log2≥1/2 by integrating 1/x on [1,2]. At s=1/2 it is −2/3. Thus the unique preferred cutoff lies strictly between 1/4 and 1/2, while output rises throughout that interval. If capital and labor ownership coincide instead, D vanishes identically and s_W=s°.

This extension makes the welfare tradeoff precise and separates a stated weighting rule from an empirically identified causal effect. Endogenous saving, transfers, new tasks, innovation incentives and political feasibility are outside the result. External references in the source are not independently verified here.

Source: [ECON-O33-286-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/83/prb_83b22937127646f9b8fb5200a468d3f8/contributions/con_b3945f25768c4e7d8d19e76e448d1291/files/O33-286.tex), canonical revision rev_60f7146c80084a9ca33527e61474bdc1. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
