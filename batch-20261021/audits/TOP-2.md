# Qualified independent review: TOP-2

Verdict: **PASS**.

Reviewer: /root/sol_ultra_numbers; author: /root/hundred_numbers. Configured model `gpt-6.1-sol`, reasoning `ultra`, selected by the recorded successful dispatch; serving revision/time budget unknown.

## Scope and significance

Substantive literature reconstruction of a different arithmetic RH route, including the sharp first-order threshold shift and a fixed-tolerance eventual equivalence. Category remains Literature report; neither the universal inequality nor RH is established.

## Actual mathematical checks

- Re-derived H_n=log n+gamma+r_n with 0<r_n<1/n from the exact tail integral. Multiplying the two expansions gives e^gamma gamma n/log n as the first shift; O(log n+loglog n) is absorbed into O(n/log²n).
- Verified n>=3 makes loglog n positive and F(n)>e^gamma n loglog n. RH direction therefore needs no finite-prefix computation for the eventual criterion.
- For false RH, Lagarias Proposition 3.2 gives a fixed C>0 and exponent b<1/2 on an unbounded subsequence. After multiplication by sqrt(log n), the oscillation dominates both O(1/log n) and each fixed K/sqrt(log n). Checked existential K,n0 quantifiers and the weaker-alpha limitation.

## Prior-body comparison

Read all four retained bodies. Two records summarize unverified 11/12 and 7/8 zero-free claims; one copies the statement; the full other manuscript uses logarithmic moments, polynomial isolation, kernel countermodels and finite positivity. The divisor-sum error-scale route is distinct; none of those unverified claims is an input.

## Primary sources and access

- {"url": "https://arxiv.org/pdf/math/0008177", "version": "math/0008177v2, 6 May 2001; internal 5 May", "locators": "Theorem 1.1; Propositions 3.1–3.2; Lemmas 3.1–3.2; proof and small-integer computation attribution", "retrieval": "coordination/qualified_number_first_half_primary_01.json; _02.json"}

## Limits

- Robin's original paper was not directly read; the exact credited assertions were checked in Lagarias's primary reconstruction. Historical finite checks were not rerun.
- No deep imported theorem is claimed independently reproved; no formal proof, human review, novelty, editorial acceptance or public write is claimed.

All eight core scientific inputs and every retained prior body/wrapper actually reviewed are bound in qualified_audit.json. Program hashes are empty; actual scientific program runs: zero.
