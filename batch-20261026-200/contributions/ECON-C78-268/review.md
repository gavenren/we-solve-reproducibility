# Independent verification of the reachable terminal trap and certificate bounds

**Target:** ECON-C78-268-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Four-agent terminal trap; potential witness bound; complete-network reachability reduction

**Source identity:** `con_7cdc88aaf540461a9bf2c4ce76ee2262` / `rev_ebf7f8d8e1d14ae7b4d6f2d6f9a9bd39`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/house-exchanges-along-longer-social-network-cycles/attempt-1/r1/index.html).

I checked the terminal-trap example against the full preference table. The first branch is
\[
(1,2,3,4)\to(1,2,4,3)\to T=(1,3,4,2).
\]
The swaps use edges \(34\) and \(24\). Agent 3 improves \(3\to4\); agent 4 improves \(4\to3\to2\); agent 2 improves \(2\to3\). At \(T\), agent 4 holds its top house and cannot join any strictly improving cycle. The remaining induced graph has edges \(12,13\) only. A swap on \(12\) would give agent 2 its worst house 1; a swap on \(13\) would give agent 1 its worst house 4. There is no remaining length-three cycle. This checks terminality even when cycles of arbitrary permitted length are considered.

The second branch uses \(13\), then \(24\), reaching \(D=(3,4,1,2)\). Relative to \(T\), the preference rows give strict improvements for agents 1, 2 and 3 and equality for agent 4. All four swaps are independently legal. Thus terminality does not imply Pareto optimality within the entire set reachable from the initial allocation. The missing edge \(23\) prevents the direct three-person rotation between the two outcomes.

For the certificate claim, assigning distinct ordinal scores in \(\{0,\ldots,n-1\}\) increases the score sum by at least two in every legal cycle. Its total range is at most \(n(n-1)\), yielding the displayed path bound and a polynomial-length certificate even when the cycle limit is part of the input. Prefix self-reduction of this certificate supplies the stated NP-oracle search upper bound; it does not give an ordinary polynomial algorithm.

In the complete graph with unrestricted cycles, I also checked the converse reduction: the permutation taking initial holdings to an individually rational target decomposes into disjoint cycles. Every nontrivial cycle strictly improves all its members, whose initial holdings remain untouched until that cycle executes. Thus the matching reduction is valid. Decomposing a long cycle into shorter swaps would not preserve this argument, which explains why the unrestricted-cycle assumption matters.

These checks support the three specified restricted results. They do not establish hardness or a general-graph complexity classification.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

