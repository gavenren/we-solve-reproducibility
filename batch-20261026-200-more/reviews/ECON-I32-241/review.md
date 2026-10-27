# Sharp finite-horizon robustness and the escape condition needed for mean-time stability

The source's Identified finite-horizon recovery theorem gives the valid bound min(1,Tη). Its infinite-horizon example also correctly shows why mean escape time lacks uniform stability without separation. Both statements can be sharpened within the same homogeneous finite-state experiment.

For kernels K and K̃ whose corresponding rows have total-variation distance at most η∈[0,1], the exact universal finite-horizon bound is

supᵢ |Pᵢᴷ(τ_H≤T)−Pᵢᴷ̃(τ_H≤T)| ≤ 1−(1−η)ᵀ.

Construct a coupling of the chains started at the same state. Whenever their current states agree, couple their next-state rows maximally; their next states then agree with probability at least 1−η. Once they disagree, choose any coupling. The probability of remaining identical through T transitions is at least (1−η)^T by conditioning successively. If paths remain identical, their hitting indicators through T agree. The difference of their event probabilities is therefore at most the probability of a coupling disagreement, proving the bound. Initial states in H cause no difficulty because both probabilities are already one.

Sharpness follows with states L,H and H absorbing. Let K(L,L)=1, while K̃(L,H)=η and K̃(L,L)=1−η. Starting from L, the two recovery probabilities are 0 and 1−(1−η)^T; the only nonzero row distance is exactly η. This is a proof for every integer T≥0, not a numerical check. The source's linear bound follows from 1−(1−η)^T≤Tη.

There is also a useful positive result for mean escape times. Impose the additional, empirically substantive restriction that every state outside H has one-step probability at least δ>0 of entering H, under both kernels. Let m_K(i)=E_i^K[τ_H], with m_K=0 on H. Then

‖m_K−m_K̃‖∞ ≤ η/δ².

Indeed, survival past t is at most (1−δ)^t, so each mean is finite and bounded by 1/δ. On H's complement, let Q and Q̃ be the substochastic transition blocks. Their sup-norm operator bounds are at most 1−δ, and m=(I−Q)^{-1}1, with resolvent norm at most 1/δ. Subtracting Bellman equations gives

m−m̃ = (I−Q)⁻¹(Q−Q̃)m̃.

Extend m̃ by zero on H. Its range is contained in [0,1/δ], so the total-variation row bound makes the rightmost vector at most η/δ in sup norm. Multiplication by the resolvent gives the claim.

The δ dependence is meaningful. In the two-state model, take escape probabilities δ and δ+η≤1. Mean-time difference is η/[δ(δ+η)], approaching η/δ² when η/δ tends to zero. Hence an order δ⁻² sensitivity cannot be uniformly eliminated. As δ decreases toward zero, the guarantee deteriorates exactly where the source's absorbing-versus-slow-escape testing obstruction operates.

These extensions retain observed states, time homogeneity, independent experimental subjects and the exclusion restriction. A positive δ is an extra structural restriction, not something guaranteed by finite data or by the original Hoeffding bound. The results therefore improve conditional robustness without asserting identification for noisy heterogeneous panels.

Source: [ECON-I32-241-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/25/prb_25d6e4d59d5b49efb127e4b75960f4fe/contributions/con_c7c3fd401873457d91b86f06f56b2bc5/files/I32-241.tex), canonical revision `rev_810874aff8b54c988e67407856d7fc0f`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
