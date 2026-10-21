# Qualified independent review: TOP-47

Verdict: **PASS**.

Reviewer: /root/sol_ultra_numbers; author: /root/hundred_numbers. Configured model `gpt-6.1-sol`, reasoning `ultra`, selected by the recorded successful dispatch; serving revision/time budget unknown.

## Scope and significance

Credited substantial large-prime-factor approximation with a complete small-root/cofactor interpretation, distinct from prior two-almost-prime extraction. Literature report never drops the residual cofactor or asserts prime-value infinitude.

## Actual mathematical checks

- Checked Pascadi v3 Theorem 1: P+(n²+1)>n^1.3 infinitely often, explicitly unconditional. Conditional larger exponents in neighboring discussion are not used.
- For each large n in that sequence, m=(n²+1)/p<2n^0.7. Two factors >n^1.3, or a square of such a prime, would force n²+1>n^2.6, impossible eventually. Thus the large factor is unique, exponent one and coprime to m.
- p>n>1 and p|(n²+1) imply a nonzero root of −1 of exact order four; hence p=1 mod4. Rearrangement gives n<p^(10/13), and a finite set of p would bound n, contradicting infinitude.
- Verified smaller root r(p)<=n and the concrete composite 145=5·29 illustrates that the cofactor need not be one. No intersection of the Iwaniec and Pascadi infinite sequences is assumed.

## Prior-body comparison

Complete earlier body read. It gives local square-root counts, sieve-level bounds, bounded-weight Liouville extraction and an almost-prime parity gap. Large-factor magnitude and root-size consequences are additional.

## Primary sources and access

- {"url": "https://arxiv.org/html/2404.04239v3", "version": "2404.04239v3, 15 January 2026", "locators": "Theorem 1 and following unconditional-versus-Selberg discussion", "retrieval": "coordination/qualified_number_first_half_primary_03.json; _04.json"}

## Limits

- The source's deep sieve/numerical integrations were not reproduced. No current-optimal exponent certification is made.
- No deep imported theorem is claimed independently reproved; no formal proof, human review, novelty, editorial acceptance or public write is claimed.

All eight core scientific inputs and every retained prior body/wrapper actually reviewed are bound in qualified_audit.json. Program hashes are empty; actual scientific program runs: zero.
