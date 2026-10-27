# Anytime-valid project-value sign certification across sample sizes and follow-up horizons

The source's finite-horizon sign certificate (3) correctly adds a deterministic tail bound to a valid truncated-mean confidence bound. A practical extension is to make that confidence bound valid when an evaluator repeatedly checks the data and chooses both sample size and follow-up horizon after inspection.

Consider independent identically distributed candidate projects with randomized assignment Z, fixed known e∈[e₀,1−e₀], e₀>0. For every horizon T≥0 let B_T(a) be the discounted gross service benefit through T, assume 0≤B_T(a)≤B uniformly, and define the fully observed horizon-consistent cost C_{j,T}=K_j+C_j^F+∑_{t=0}^T δᵗM_{jt}, with 0≤C_{j,T}≤C_max uniformly in projects and horizons. These boundedness assumptions are additional to the manuscript's integrability assumptions. Define
X_{j,T}=Z_j B_{j,T}(1)/e−(1−Z_j)B_{j,T}(0)/(1−e)−C_{j,T}.
Only the assigned potential benefit is used. Randomization gives E X_{j,T}=μ_T, the truncated mean NPV including maintenance only through T. This horizon-consistent subtraction is essential: subtracting all future maintenance while truncating only gross benefits would not admit the net-flow tail bound below. Every summand lies in [−B/e₀−C_max,B/e₀], an interval of width W=2B/e₀+C_max.

For n≥1 and T≥0 put
r_{n,T}=W√{log[2n(n+1)(T+1)(T+2)/α]/(2n)}.
Then, with probability at least 1−α, every pair (n,T) simultaneously satisfies
|n⁻¹∑_{j=1}^n X_{j,T}−μ_T|≤r_{n,T}.

For proof, ordinary bounded-variable Hoeffding at a fixed pair gives failure probability at most α/[n(n+1)(T+1)(T+2)]. Summing over all pairs is legitimate even though the estimates at different horizons are dependent. The two telescoping series ∑_{n≥1}1/[n(n+1)] and ∑_{T≥0}1/[(T+1)(T+2)] both equal one, so a countable union bound yields simultaneous coverage. No independent replication across follow-up horizons is assumed.

Now impose the source's per-date net incremental flow bound |G_t|≤H. Its deterministic omitted tail is b_T=Hδ^(T+1)/(1−δ), and therefore the infinite-horizon mean μ belongs simultaneously to
[ X̄_{n,T}−r_{n,T}−b_T, X̄_{n,T}+r_{n,T}+b_T ].
An evaluator may stop at any data-dependent available pair (n,T) and declare positive mean value only when the lower endpoint is positive, or negative value only when the upper endpoint is negative. The probability of any incorrect sign declaration over the entire repeated evaluation is at most α, since every such error requires failure of the single simultaneous coverage event.

The construction exposes a tradeoff: longer follow-up shrinks the economic tail term, whereas the multiplicity penalty grows only logarithmically in T. Larger samples shrink the sampling radius. It gives no guarantee that a sign will ever be identified when μ is close to zero or tail restrictions are weak.

The target is the same project-population mean, including failures, with costs accounted for once. Project independence, a common population, known assignment propensity, consistent horizon measurement and bounded outcomes must be justified. Selected completed projects, adaptive project recruitment, network interference or selectively missing costs invalidate this particular Hoeffding argument. The certificate neither identifies individual winners nor supplies actual project service valuations.

Source: [ECON-H43-447-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/31/prb_31f2f860f0c64ab69be1c91beaa5a666/contributions/con_8db1065d69fc481d9008edb3cf06fcf3/files/H43-447.tex), canonical revision `rev_bfd4377011f641e185dd8be33179571f`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
