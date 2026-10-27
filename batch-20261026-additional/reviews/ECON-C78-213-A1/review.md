# Independent decomposition checks and a simultaneous-failure extension

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b5/prb_b56f436088e54110a1e57b27120a461a/contributions/con_c88bb7e104604a4f97d85172d994b07a/files/C78-213.tex), revision `rev_4a3b1dabd2e640be8372f8112fc2641c`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim.** The exact degree-two repair-budget formula follows from the forced-pair reduction and alternating-cycle decomposition. The manuscript counts removed original pairs, subtracts the failed pair, and excludes fixed pairs from the failure set; these conventions are essential to the numerical formula. The contribution metadata and manuscript both leave the unrestricted approximation problem unresolved. This review independently checks the decomposition and extends its conclusion to several simultaneous non-fixed failures, without claiming an approximation result for general graphs.

Consider first a path component. Every vertex with a remaining neighbor points to its first choice. A directed cycle in a finite functional digraph is unavoidable, but the underlying path has no undirected cycle, so that directed cycle must be a mutual pair. Thus every nonempty path permits the forced-pair reduction. In a cycle component, absence of mutual pairs forces every vertex to point in one consistent cyclic direction: once one arrow proceeds clockwise, its next vertex cannot point back and therefore also points clockwise, continuing around the component. Removing a mutual pair breaks a cycle into paths, so no other terminal component type is possible.

There is a small but important issue in iterating the reduction. A removed endpoint's first choice is its first choice among the vertices still present at its removal, not necessarily its original first choice. Reconstruction remains valid: when adding a pair to a stable matching of that reduced instance, edges to earlier-deleted vertices are not present; when those earlier pairs are subsequently added, their own endpoints reject all such possible blocks. Repeated application of the stated bijection therefore proves the global result without incorrectly assuming every removed pair was mutually top-ranked in the original instance.

On a consistently directed cycle, an unmatched vertex would block with its predecessor, who ranks it first and cannot already be matched to it. Thus every stable matching is perfect. Odd cycles are infeasible, and an even cycle of length \(2\ell\) has only the two alternating perfect matchings. For an unused cyclic edge, exactly the endpoint matched to its successor rejects the edge, proving stability. Both existence and uniqueness-of-the-two-alternatives are needed for the repair argument.

Consequently the stable matching space is a product of \(r\) binary choices, one for each terminal even cycle, together with the fixed deleted pairs. Switching a chosen cycle removes exactly its \(\ell_j\) original pairs. A repair avoiding one failed pair on that cycle must perform this switch, and changes to other components cannot help. Its additional-pair cost is therefore exactly \(\ell_j-1\). This independently recovers the manuscript's maximum-over-cycles formula, including its zero value when there is no terminal cycle.

The same reasoning gives a useful simultaneous-failure extension. For an integer \(a\ge1\), define

\[
b_{\le a}(M)=\max_{F\subseteq M\setminus\mathrm{Fix}(I),\ |F|\le a}
\min_{N\in\mathcal S(I),\ N\cap F=\varnothing}
\bigl(|M\setminus N|-|F|\bigr).
\tag{A}
\]

Here only non-fixed original pairs may fail, and the objective counts additional removed pairs after all failed originals are excluded. Order the terminal half-lengths so \(\ell_{(1)}\ge\cdots\ge\ell_{(r)}\). Then every stable initial matching satisfies

\[
b_{\le a}(M)=\sum_{j=1}^{\min(a,r)}(\ell_{(j)}-1).
\tag{B}
\]

Indeed, let \(T\) be the set of cycles touched by a failure set. Every touched cycle must flip, and no untouched cycle need flip. The inner minimum in (A) is exactly \(\sum_{j\in T}\ell_j-|F|\). Since \(|T|\le|F|\le a\), this is at most the sum of the \(\min(a,r)\) largest values \(\ell_j-1\). Conversely, failing one pair in each of those cycles attains that sum. Multiple failed pairs on one cycle add no forced switch and reduce, rather than increase, the count of additional removals. Formula (B) concerns an **at most a** failure budget; an exactly-a convention would require separate feasibility and counting qualifications. With \(a=1\), it reduces to the source theorem.

An independent finite check enumerated all strict ranking choices on every connected path with 1 through 10 vertices and every connected cycle with 3 through 10 vertices: 2,552 preference instances. For each it enumerated all partial matchings, tested blocking pairs directly, identified fixed pairs by intersection of the complete stable set, and computed the repair minimum from its definition. Infeasibility and every stable matching's budget agreed with the reduction formula. Disconnected graphs are covered structurally by the proved product decomposition, rather than asserted to have been enumerated. The [separate checker](../../checkers/reviews_e/matching_checks.py) contains no manuscript-specific stability shortcuts.

The finite enumeration supports the implementation and edge cases; the mathematical proof handles arbitrary size. Fixed failures, higher-degree interactions, ties, or repairs defined by a new post-failure preference instance are outside (A) and the manuscript's model. Neither the source formula nor its simultaneous-failure extension resolves the general approximation question.
