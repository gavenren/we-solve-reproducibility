# Qualified independent review: TOP-1

Verdict: **PASS**

Reviewer: /root/sol_ultra_algorithms; author: /root/hundred_algorithms. Selected model: gpt-6.1-sol; selected reasoning: ultra. Exact serving revision and time budget unknown. New dispatch provenance is retained in coordination/qualified_verifier_dispatches.json; historical authors/reviewers are not relabeled.

Report SHA-256: `545b4b6ad06f717cb693acc64007b807a763ab35376b8b0d95839273bc56ba0e`. Complete scientific input and program hashes are in qualified_audit.json.

Read exact official P-vs-NP prompt and all three retained prior bodies(A1,A2 and alias TOP-3395-A1). Verified incidence-decomposition coverage/connectedness validation and the explicit distinction from primal width and clause arity.

Checked the exact state invariant: s(c) counts only satisfied literals of variables forgotten below. Introduced clauses cannot have forgotten neighbors below; forgetting variables ORs contributions, and forgetting clauses checks both saved and still-bag contributions. Every clause neighbor is then accounted for by decomposition connectedness.

At joins, shared variable assignments agree, forgotten sets are disjoint and clause bits OR exactly; child witnesses combine in both directions. Empty root accepts iff all clauses satisfied; backpointers reconstruct a direct-checkable assignment. Empty clauses/tautologies/repeats are handled.

Verified2^(t+1) states, join pairs<=2^|V|4^|C|<=4^(t+1), polynomial encoding/backpointer costs and t=O(log L) supplied-decomposition consequence. No decomposition for arbitrary formulas or global P=NP claim; source/proof-only zero runs.

Distinctness and significance: Adds a complete clause-width-independent incidence-treewidth algorithm and exact joins, distinct from all three prior affine-summary/rank/projection investigations. This is substantive structural tractability, not a finite SAT experiment.

Primary sources/access limits:

- Samer-Szeider,cs/0610174v2,21Feb2007, primary arXiv abstract https://arxiv.org/abs/cs/0610174, incidence #SAT fixed-parameter theorem; scope read and credited. The report supplies its complete decision-state proof, not an unseen theorem number. Retained coordination/qualified_algorithms_primary_retrieval_04.json.

Actual program executions: 0; logs and exact source/output hashes are in qualified_audit.json. This is source/proof-only; no program run is claimed.

Independent mathematical/source review, not human review, formal certification, historical novelty certification or editorial acceptance.
