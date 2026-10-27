# Interval verification and a chain obstruction for two adjacent preference changes

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b1/prb_b17f3d0ebfc042b2a33cc78f55c5f1ed/contributions/con_8833c80d5e0c42b49810e06a2d81cc0e/files/C78-217.tex), revision `rev_3ba61b98f8e8433e80cf4d24fe9fc500`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim.** The discarded-set characterization and endpoint closure tests are correct for the manuscript's two noninteracting adjacent swaps. The contribution is explicitly an unresolved exploration; it does not claim that arbitrary abstract pairs satisfying its necessary conditions are realizable by preference changes. This review adds a chain-based obstruction that is stronger than checking whether the retained set is a sublattice, and independently checks the matching-level formulas by direct enumeration.

The partner-constraint lemma uses both closure and convexity, and both are necessary. Under the source's worker-better-is-smaller order, a worker's partner at a meet is its preferred input partner, while a firm's partner is its less preferred input partner. Equality and original-ranking cutoffs are preserved whichever of those two partners is selected. They are also preserved along an order interval, because each agent's partner changes monotonically in its original ranking. A finite nonempty set satisfying these two properties contains its iterated meet and join; convexity then fills the entire interval between them. This verifies the interval conclusion without confusing an arbitrary sublattice with an interval.

For the worker swap \(a\succ_w b\) to \(b\succ_w a\), adjacency is doing substantive work. The only comparison newly favorable to a deviation is \(b\succ_w a\). A matching stable in the original profile therefore gains a blocker from this swap exactly when \(M(w)=a\) and firm \(b\) prefers \(w\) to its current worker. The noninteraction condition ensures that firm \(b\)'s ranking has not itself changed. The symmetric argument for the changed firm's adjacent swap gives the second discarded interval. Removed comparisons cannot create a new blocker, so taking the union is sufficient as well as necessary.

The endpoint test is also valid in a nondistributive lattice; no matching-specific identity is hidden in it. If the lower endpoints of \([a,b]\) and \([c,d]\) satisfy \(a\le c\), then for any cross pair \(x,y\), \(a\le x\wedge y\le x\le b\), placing the meet in the first interval. If the lower endpoints are incomparable, their own meet lies strictly below both lower endpoints and outside the union. The dual argument uses the upper endpoints. Thus the claimed equivalences do not require the two intervals to be disjoint or incomparable as sets.

There is a further intrinsic necessary condition worth extracting. For any chain \(C\subseteq L\), intersection with a lattice interval is a contiguous order-convex block in that chain: if \(x<y<z\) lie on the chain and \(x,z\) belong to the interval, then so does \(y\). Hence the theorem implies

\[
D\cap C\text{ has at most two separated nonempty blocks.}
\tag{A}
\]

Equivalently, scanning any maximal chain can enter the discarded set at most twice. This is an easily stated obstruction for a proposed abstract pair, independent of whether its retained subset passes the sublattice test.

For example, take a five-element chain

\[
x_0<x_1<x_2<x_3<x_4,
\qquad R=\{x_1,x_3\},\quad D=\{x_0,x_2,x_4\}.
\]

The retained set is a sublattice: on a chain the meet and join of two members are those same two members. Nevertheless, \(D\) has three separated blocks. An interval containing any two of its points also contains a retained point, so two intervals cannot cover \(D\) exactly. This abstract pair is therefore excluded by the local two-swap theorem even though sublattice closure of \(R\) alone permits it. No claim is made here that this abstract pair is realizable under a different perturbation model. It is a necessary-condition witness, not a matching-instance construction.

The general endpoint tests are sharp as statements about interval unions. In the four-element Boolean lattice, take the two singleton intervals at the incomparable middle elements. Their union is neither meet-closed nor join-closed, because its meet and join are the bottom and top, respectively. This confirms that neither direction of the abstract closure criterion can be weakened simply because each individual interval is a sublattice. Again, it does not establish matching realizability of those intervals.

The [independent checker](../../checkers/reviews_e/matching_checks.py) sampled 30,000 strict complete profiles with four agents per side using a fixed seed. Among 12,108 profiles having at least two stable matchings, it checked all 435,260 admissible combinations of one adjacent swap per side satisfying the noninteraction condition. It enumerated stable matchings as permutations and evaluated stability after each change directly. Every discarded set equaled the two stated blocker sets; whenever both were nonempty, both endpoint closure equivalences agreed with direct meet/join closure tests. This is exhaustive over the admissible changes for each sampled profile, not exhaustive over all profiles or evidence of a general realization theorem.

The review therefore supports the proved restricted structure and supplies the additional chain obstruction (A). Arbitrary list permutations and interacting changes remain outside the theorem, exactly as the source states.
