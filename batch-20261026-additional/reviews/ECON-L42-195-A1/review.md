# Exact dependence of exclusion on the continuation-price selector

Finding: **Supports the claim**.

This assessment concerns the complete [pinned L42-195 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/32/prb_325b4dd4f43f4274b03c10cf4dffc511/contributions/con_3afcfdf94fa24022b4d2fa7db979c631/files/L42-195.tex), revision `rev_068c6401c64e453b96fb008143d91095`. I read both the manuscript and its exploration metadata. Its theorem explicitly fixes the incumbent's nonexclusive continuation selector at c_I and does not claim an equilibrium-robust result over all selectors. I support that theorem and sharpen the selection qualification into an exact threshold and a robustness classification.

The nonexclusive continuation is sequentially coherent. Once the incumbent has posted t, an entrant that profitably serves the retailer can match that price, win the specified tie, and earn t−c_E−F. It therefore enters exactly when t>c_E+F. If the incumbent instead deters entry, its sale profit is at most F−d<0. Allowing entry yields incumbent profit zero, so every tariff

\[
p\in(c_E+F,v]
\]

is a profit-maximizing nonexclusive choice. In particular c_I belongs to this interval because F<d. The announced selection rule is therefore an admissible choice from genuine continuation multiplicity, not an additional profit-maximization condition falsely imposed on a unique equilibrium.

With the manuscript's selection p=c_I, retailer rejection gives v−c_I. The highest acceptable exclusive tariff is consequently c_I. Its profit s>0 strictly exceeds the nonexclusive zero payoff. Exclusive production uses the coordination technology, prevents the entrant from finding a customer, and preserves the final unit. Adding consumer, retailer, and producer payoffs cancels tariffs, leaving the welfare difference s−d+F. This verifies that the sign comparison counts entry cost once and distinguishes the incumbent's own coordination saving from an economy-wide resource saving.

To quantify the role of selection, retain all primitives, timing, and tie rules but fix an alternative nonexclusive continuation tariff p in the interval above. Require the same fixed continuation selection whenever that continuation is reached, including after an exclusive offer is rejected. This is a controlled change of selector, not an assertion about every possible history-dependent subgame-perfect equilibrium.

Rejection now gives the retailer v−p. Thus an exclusive tariff is accepted precisely when t_X≤p, and the best accepted exclusive offer is t_X=p. Its profit is p−c_I+s. Rejected offers and immediate nonexclusive play yield zero. Hence

\[
\begin{cases}
p>c_I-s &: \text{exclusivity is strictly preferred},\\
p<c_I-s &: \text{nonexclusive continuation is strictly preferred},\\
p=c_I-s &: \text{the incumbent is indifferent}.
\end{cases}
\]

Conditional on exclusivity being chosen, the allocation and welfare change remain exactly those in the manuscript: ΔW=s−(d−F). The alternative tariff changes who receives rents, while the technological and entry-cost comparison is unchanged.

This yields a sharper robustness statement. Let a=d−F>0, so the admissible continuation prices satisfy p>c_I−a. If s≥a, then c_I−s≤c_I−a<p, and exclusivity is strictly preferred for every fixed admissible continuation selector. Its welfare effect is nonnegative, and is positive if s>a. If instead 0<s<a, the cutoff c_I−s lies strictly inside the admissible price interval, because c_I−a<c_I−s<c_I<v. Low selectors generate nonexclusive continuation; high selectors generate exclusion with the negative welfare effect s−a. The manuscript's original p=c_I is always on the exclusion side because s>0.

For a concrete example, use c_I=10, d=6, F=2, s=1 and any v>10. Continuation tariffs exceed 6. At p=8, the best exclusive offer earns −1, so the incumbent chooses nonexclusive continuation and the entrant serves the retailer. At p=10, exclusivity earns 1 and is chosen, producing the welfare change −3. Both continuation prices maximize the incumbent's nonexclusive profit. The different regime-1 outcomes are therefore caused by the declared selector, with costs and the entrant's efficiency advantage held fixed.

This extension confirms the manuscript's warning and identifies its exact content. Welfare-improving exclusion is robust within the fixed-selector family just analyzed, whereas welfare-reducing exclusion is possible but selector-dependent. It does not remove the consequential restriction prohibiting entrant-retailer contracting before entry, and it does not cover renegotiation or history-dependent continuation selections. Those are acknowledged boundaries of the benchmark.

I independently checked the tariff inequalities and profit comparisons. I found no error in the selected equilibrium, welfare threshold, or sharp audit-rectangle bounds. The additional selector classification is a substantive qualification of how the selected result should be used, rather than a claim that the manuscript solved the broader exclusionary-contracting agenda.
