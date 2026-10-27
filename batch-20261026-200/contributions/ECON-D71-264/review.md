# Scoped review of the randomized-dictatorship constant and one-round scope

**Target:** ECON-D71-264-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Randomized dictatorship's 3−2/n bound and sharp example; the favorite-only deterministic obstruction

**Source identity:** `con_32756a4da22f4ed78f24339e56cd3a3b` / `rev_db4e301ee0eb4bacbeb44dcc638efdf7`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/constant-distortion-using-one-round-of-linearly-many-comparisons/attempt-1/r1/index.html).

I independently checked the dependence on the number of voters rather than replacing the proof by the coarser factor three. Let \(t_v\) be voter \(v\)'s reported favorite, and let \(a^*\) minimize social cost. For every \(u\ne v\),
\[
d(u,t_v)\le d(u,a^*)+d(a^*,v)+d(v,t_v)
 \le d(u,a^*)+2d(v,a^*).
\]
For \(u=v\), favorite optimality gives \(d(v,t_v)\le d(v,a^*)\), with no additional term. Consequently
\[
\mathrm{SC}(t_v)\le\mathrm{OPT}+2(n-1)d(v,a^*).
\]
Averaging over the uniform dictator produces precisely \((3-2/n)\mathrm{OPT}\). The argument remains valid when OPT is zero and does not divide by it. For \(n=1\), it correctly gives factor one.

The proposed line example attains the inequality under the declared tie convention. There are \(n-1\) voters at zero, one at one, and candidates at zero and two. The distant voter's tie can favor the candidate at two. The two social costs are \(1\) and \(2n-1\), so the expected cost is \((n-1)/n+(2n-1)/n=3-2/n\). A local comparison tournament needs \(m-1\) comparisons per voter and is compatible with within-voter adaptive queries in one communication round.

I also checked what the deterministic lower example actually establishes. For one voter per candidate and distinct reported favorites, place the selected candidate at two, its voter at one, and all remaining locations at zero. The social costs again are \(2m-1\) versus one, and suitable tie rankings preserve the favorites. This construction preserves only the favorite information. It need not preserve all answers to a richer predetermined or locally adaptive comparison transcript. Therefore it supports the manuscript's favorite-only impossibility, not a lower bound for every \(O(m)\)-query one-round protocol.

The metric calculations and information restriction are supported. I do not validate a general one-round classification, nor an equivalence between arbitrary comparison protocols and favorite reports. The sharp example uses coincident locations and distance ties as explicitly permitted.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

