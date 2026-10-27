# Scoped review of the binary-marginal EFX transfer potential

**Target:** ECON-D63-294-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Two-agent construction, zero-marginal removals and matroid-rank representation

**Source identity:** `con_0d55e04158c94971a31cbbfebe38db8f` / `rev_8c1032fde7b54e20a67505527bb06443`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/efx-existence-for-chores-with-binary-submodular-costs/attempt-1/r1/index.html).

I checked all transfer cases in the potential argument, including the one in which removing a chore does not lower the owner's cost. Write \(r>s\) for the two current bundle costs, and let \(g\) violate EFX, so the higher bundle's cost after removal still exceeds \(s\). Binary increments constrain the new costs to \(\{r-1,r\}\) and \(\{s,s+1\}\).

If removal lowers the high cost to \(r-1\), integrality of the violation implies \(s\le r-2\). Both new costs are therefore at most \(r-1\), and the first potential coordinate falls. If the high cost remains \(r\) and the low cost rises, the lower cost rises even if the bundles tie at \(r\), so the second coordinate \(-s\) falls. If neither cost changes, the same unique higher bundle contains one fewer chore, and the third coordinate falls. This verifies strict lexicographic decrease in every case without invoking submodularity.

All costs and bundle sizes lie between zero and the number of chores \(m\), giving at most \((m+1)^3\) potential states. Scanning all possible own-bundle removals costs \(O(m)\) oracle queries per step. Termination therefore supplies the claimed polynomial oracle bound. Testing only positive removal marginals would be incorrect: the third-coordinate case is exactly what handles a redundant, zero-removal-marginal chore.

After agent 1 cuts an EFX partition by its own costs, either bundle assignment satisfies its removal inequalities. Agent 2's cheaper-bundle choice is envy-free and hence EFX by monotonicity. This verifies the two-agent conclusion even for binary-marginal costs that are not submodular. It supplies no analogous simultaneous cutting property for three unrelated evaluations.

I also checked the rank representation. Heredity follows because deleting \(k\) elements can lower the cost by at most \(k\). If independent sets \(I,J\) with \(|I|<|J|\) had no augmenting element from \(J\setminus I\), submodularity would keep every such marginal zero while adding them, contradicting \(c(I\cup J)\ge c(J)=|J|\). The greedy retained set is independent; every rejected element remains zero marginal at the final retained set, so its size equals \(c(S)\). This establishes rank, while also showing why dependent-bundle redundancy cannot be modeled as additive zero-cost items.

The specified proofs are supported. Arbitrary-agent EFX for unrelated matroid ranks and the manuscript's external literature status are outside this review.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

