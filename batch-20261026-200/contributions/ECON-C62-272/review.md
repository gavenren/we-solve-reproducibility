# Scoped review of hedonic-market existence and the exact-clearing repair

**Target:** ECON-C62-272-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Finite-type existence proof's boundary and supply-pruning steps; two counterexamples

**Source identity:** `con_16a52be68b3b4ceb8c831e7ee3b5925c` / `rev_d4d6b78b7c1c4900a0c13e7b8241741b`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/existence-in-nonseparable-competitive-hedonic-markets/attempt-1/r1/index.html).

The delicate point in the existence argument is the transition from the price fixed point to exact clearing. I checked it separately. With excess demand \(E=D-S\), maximizing \(q\cdot E\) over the price box forces \(p_z=P\) when \(E_z>0\). Because \(P\) exceeds every consumer endowment, the boundary assumption excludes consumption of \(z\) there, making \(D_z=0\) and contradicting \(E_z>0\). Thus the fixed point has \(D_z\le S_z\).

If \(D_z<S_z\), the same maximization forces \(p_z=0\). Every producer assigning positive probability to \(z\) must then have cost zero: a positive cost would yield negative profit whereas the outside option yields zero. For these producers, the outside option and \(z\) are both optimal. Multiplying their probabilities of producing \(z\) by \(D_z/S_z\) and transferring the removed probability to the outside option therefore preserves optimality and clears that market exactly. Applying this operation quality by quality leaves other supplies unchanged. If demand is zero, the multiplier is zero; a zero-supply market cannot be oversupplied. This is an exact-clearing repair, not an implicit appeal to free disposal.

The consumer utility extension at exhausted budgets is legitimate only because \(u_i(z,0)<u_i(0,e_i)\). At and beyond exhaustion, the artificial value cannot be optimal. Continuity then gives the closed optimal-choice correspondence needed for the finite-dimensional fixed-point argument.

I checked the failure example without this boundary condition. With consumer utility \(u_1(t)=2+2t\), \(u_0(t)=t\), endowment one, and producer mass \(1/2\) at zero cost, demand is one at every feasible positive price at most one; supply is \(1/2\). Above one demand is zero and supply remains \(1/2\). At zero, supply cannot exceed \(1/2\); at a negative price it is zero. No price clears. Strict consumer preference prevents resolving the mismatch by consumer mixing.

In the second example, \(u_1(t)=t+1/2\) makes the consumer indifferent at price \(1/2\). Splitting its unit type mass equally clears with all producer mass supplying; requiring each type to choose a single pure action removes that equilibrium. The distinction between individual randomization or type splitting and an all-pure type kernel is material.

These checks support finite-type existence with the stated assumptions and the two boundaries. They do not establish a continuum-quality extension.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

