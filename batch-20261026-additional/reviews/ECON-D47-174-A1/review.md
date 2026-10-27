# An extremal graph attains the reservation bound without an individual-rationality loss

**Finding: Supports the claim.** The reservation theorem is correct in the manuscript's batch model, and its \(1/K\) count guarantee cannot be improved uniformly for that specific reservation procedure. An explicit extremal family also separates two possible sources of inefficiency: irrevocably reserving particular internal cycles can be costly even when full pooled efficiency is individually rational for every center. This is a substantive boundary check on the mechanism, not a counterexample to its stated guarantee.

I read the full manuscript and contribution metadata. Both identify the work as a restricted unresolved exploration. In particular, the manuscript expressly declines to call the reservation rule truthful against withholding, makes cycle success probabilities common, allows no chains, and does not claim polynomial computation. None of those acknowledged omissions is treated here as an error.

For every integer \(K\ge2\), construct a directed compatibility graph as follows. Center \(A\) owns two vertices \(a_1,a_2\), with the internal two-cycle \(a_1\to a_2\to a_1\). For each \(i=1,2\), introduce \(K-1\) additional vertices \(v_{i,1},\ldots,v_{i,K-1}\). Give each additional vertex its own center, so all these centers have zero internal outside options. Add the directed cycle
\[
 C_i=(a_i,v_{i,1},\ldots,v_{i,K-1},a_i).
\]
There are no other edges.

The only simple directed cycles are \(A\)'s internal cycle and the two displayed \(K\)-cycles. To check this rather than assume it, observe that each added vertex has a unique next vertex along its designated path, and that path returns only to its own \(a_i\). A cycle taking the edge \(a_1\to a_2\) can return to \(a_1\) only through the edge \(a_2\to a_1\); taking \(a_2\)'s longer path instead would revisit \(a_2\). The symmetric observation applies starting at \(a_2\). Thus no additional simple mixed cycle appears.

Center \(A\)'s internal optimum covers both its vertices, so the reservation procedure fixes that two-cycle and \(b=2\). Deleting \(a_1,a_2\) breaks both longer cycles, leaving no residual cycle: \(Q\) is empty. The procedure therefore covers exactly two vertices. The pooled optimum uses \(C_1\) and \(C_2\), which are vertex-disjoint and cover every vertex of the graph. Hence
\[
 T^*=2K,\qquad |V(O\cup Q)|=2=T^*/K.
\]
The finer bound in the theorem is attained too:
\[
 \max\{b,T^*-(K-1)b\}
 =\max\{2,2K-2(K-1)\}=2.
\]
No tie-breaking issue or computational approximation is involved.

Importantly, the pooled optimum itself is individually rational. It transplants both of center \(A\)'s patients, matching its outside-option count of two, and gives one transplant to each remaining center, whose outside option is zero. With common success probability \(s\), the same statements hold in expectation: \(A\) receives \(2s\), the reservation plan gives \(2s\) in total, and the pooled plan gives \(2Ks\). Correlation between failures is immaterial to those expected counts. Thus this example does not establish a \(1/K\) limitation on all individually rational allocation rules. It establishes the exact worst-case ratio of committing to the selected internal cycles.

This distinction complements the manuscript's separate weighted obstruction. There the cross-center cycle deprives the binding center of one expected transplant, so lotteries cannot satisfy its count outside option while accessing the high-weight patient's benefit. In the extremal family above, replacing the internal cycle preserves every relevant outside option. The two examples therefore diagnose different constraints: allocation lock-in versus an intrinsically binding center participation inequality.

The proof's deletion argument also checks out independently. Every optimal cycle intersecting the \(b\) reserved vertices can be assigned a distinct such vertex because optimal cycles are disjoint. There are at most \(b\) intersecting cycles, each of length at most \(K\). This yields the \(Kb\) deletion loss even when some optimal cycles intersect several reserved vertices; those intersections only improve the bound. The common success factor then cancels from the approximation ratio exactly as claimed.

Finally, the two-type formula is a count identity under complete cross-type compatibility; its random-pool bounds follow from absolute-value convexity and a variance bound. They do not convert biological composition into a generic empirical decomposition. The manuscript explicitly states that limitation, as well as its strategic and dynamic limitations.

**Source reviewed:** [D47-174.tex at the pinned revision](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/60/prb_60bdfdcbbee84a5692b684546f829142/contributions/con_6480d3adb78a432a812d94f4167098ab/files/D47-174.tex). Contribution revision: rev_650c4fa9c47a43a782c1ca1399ef522c. The extremal family sharpens the interpretation of the stated theorem; it does not solve strategic kidney-exchange design or assert a new result in the general matching literature.

