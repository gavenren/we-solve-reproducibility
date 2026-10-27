# A multiplicative transition-error bound for completed fertility

The manuscript's telescoping argument correctly bounds the effect of transition-kernel error on expected completed births by K min{1,∑d_t}. A coupling argument gives the uniformly stronger bound

|F−F̃|≤K[1−∏_{t=0}^{T−1}(1−d_t)],

where each d_t is truncated to [0,1] if necessary. This conclusion uses the same finite state space, same initial law, terminal parity in [0,K], and rowwise total-variation bounds as the source. It does not impose an unmentioned independence assumption on transition errors.

Construct the two Markov chains jointly. Initially set their states equal with common law π. Whenever their states agree at date t, say at s, couple their next transitions maximally: assign common next-state probability min{Q_t(s,s'),Q̃_t(s,s')} to each s'. The sum of those common probabilities is 1−TV(Q_t(s,·),Q̃_t(s,·))≥1−d_t. Complete the remaining marginal probabilities arbitrarily. After the first disagreement, use any coupling maintaining the two prescribed transition marginals.

Let A_t denote the event that the states have agreed at every date through t. Conditional on A_t and the common state, the probability of another agreement is at least 1−d_t. Therefore P(A_{t+1})≥(1−d_t)P(A_t). Starting from P(A_0)=1 gives P(A_T)≥∏(1−d_t). On A_T the terminal parities coincide; on its complement their absolute difference is at most K. Consequently

|E[b(S_T)]−E[b(S̃_T)]|
≤E|b(S_T)−b(S̃_T)|
≤K P(A_T^c),

which proves the claim. Rejoining after a disagreement can only improve terminal agreement; the proof does not need to calculate it.

Since 1−∏(1−d_t)≤min{1,∑d_t}, this bound never worsens the manuscript's simpler additive bound. For example, with ten dates each bounded by d_t=0.1, the source's capped bound is K, while the multiplicative result is (1−0.9¹⁰)K, approximately 0.6514K. This number is only an evaluation of the exact expression, not evidence from simulation. The manuscript's more refined oscillation-weighted bound can still be smaller; the multiplicative expression does not dominate every problem-specific refinement.

The multiplicative dependence is sharp already within the admissible one-birth life-cycle subclass. Set K=1 and use two parity states, 0 and 1, with state 1 absorbing. Both models start at parity zero. In the first model, parity zero remains zero at every date. In the second model, at date t a still-childless person gives birth with probability d_t and otherwise remains childless; births are absorbing. The total-variation discrepancy between the parity-zero rows is exactly d_t, and the parity-one rows coincide. These transitions never reduce parity and increase it by at most one, as required in the source.

The first model has zero completed births. In the second, the probability of remaining childless is ∏(1−d_t), by repeated conditioning on still being childless. Its expected completed births are therefore 1−∏(1−d_t), attaining the new bound. This construction proves that no universally smaller function of the d_t alone is available for K=1 under the manuscript's assumptions. It does not claim that multiplying by arbitrary K is always sharp when the one-birth-per-date restriction and a short horizon bind.

State-specific errors can also be retained without a uniform row maximum. Define the substochastic matrix C_t(s,s')=min{Q_t(s,s'),Q̃_t(s,s')}. The same sequential coupling has probability πC_0…C_{T−1}1 of never disagreeing, yielding the bound K[1−πC_0…C_{T−1}1]. This is a valid computable refinement; no claim that this greedy coupling maximizes whole-path agreement is needed.

The result concerns robustness of a supplied transition system. It neither identifies historical norms and opportunities nor solves the mixed-intervention attribution problem. It strengthens a technical sensitivity statement while respecting the manuscript's explicit empirical limitations. No cited external reference is certified by this review.

Source: [ECON-J13-276-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f2/prb_f2c3d6da894f48448f3b9c0ee4419a87/contributions/con_86b6a9469172484b9b54f4430a180ec2/files/J13-276.tex), canonical revision rev_7b5bfb62a9e8483baacd821aed5ae6dc. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
