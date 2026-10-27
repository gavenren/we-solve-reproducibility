# New 200-contribution WeSolve batch

The user explicitly requests 200 more submissions, authorizes public WeSolve GitHub issues, and previously requested GPT-6.1 Sol Ultra attribution. Every assigned agent is explicitly configured as gpt-6.1-sol / ultra. Exact serving build and time budget are unknown. Root is Codex based on GPT-6 with unknown exact version/thinking. Do not purchase credits, redeem resets, or use paid external inference services. Do not publish; root handles posting and receipts.

Work root: /Users/Administrator/Documents/ChatGPT/We Solve/batch_200_more_20261026
Upstream repository: We-Solve/research
Pinned upstream commit: bd5218964aa5efa77ac062e3600b8cfe70df528c

## Quality and scope

WeSolve accepts significant mathematical contributions, not routine restatements. Read each full exact source manuscript and contribution.yaml. Prioritize actual errors/gaps with proofs, sharpness examples, nontrivial independent derivations, substantial restricted extensions, or meaningful independent computational reproductions. A review merely repeating the manuscript or checking one trivial substitution is insufficient. Do not invent defects. Do not call explicitly acknowledged limitations errors. No claim of novelty or priority without verified literature support; an independent consequence/check is sufficient when mathematically substantive. Do not claim the wider open problem solved.

Each assigned group has a target equal to its primary count (a,b:34; c,d,e,f:33), plus 5 disjoint reserves. Replace unsuitable primaries from your own reserves and document skipped targets/reasons. Never produce extra public candidates beyond the group target. If meaningful work cannot be justified even with reserves, notify root rather than padding the count. Reuse no prior reviewed targets.

## Source retrieval and persistence

Use purpose-built GitHub tools through functions and ALL_TOOLS discovery. Fetch contribution.yaml at the pinned ref using target.path from assignments/GROUP.json, then fetch the manuscript artifact path declared there. Batch independent reads in parallel and inspect every result. Verify canonical contribution/problem/revision IDs. Save exact source files and source provenance (remote path, SHA256, returned Git blob SHA, immutable URL) under sources/PROBLEM_HANDLE/. Source copies are internal, not for re-upload.

## Authoring files

For each selected problem save reviews/PROBLEM_HANDLE/review.md and metadata.json. Aim for 500–1000 substantive words where warranted; length is not a substitute for significance. Include exact source locations, assumptions, full independent argument, boundary cases, what remains unverified, pinned source URL and canonical revision. No embedded Python/Lean/program code in review text. Put original checkers separately under checks/PROBLEM_HANDLE/, execute meaningful checks, and save outputs. Label finite checks correctly. Original prose is CC BY 4.0; original code Apache-2.0. Use SPDX headers in code.

Metadata schema:
- handle: problem alias WITHOUT -A1
- problem_id
- contribution_handle: target with -A1
- contribution_id
- revision_id
- source_path: repository manuscript path
- source_sha256: exact saved manuscript SHA256
- source_url: immutable GitHub blob URL including pinned commit
- title
- finding: one of Supports the claim, Error found, Gap found, Counterexample, Known result, Reproduced, Not reproduced, Reference suggestion, Comment
- checked_scope: string
- significance: concrete independent result/check
- author: your exact agent path
- model: gpt-6.1-sol
- reasoning_effort: ultra

When a report and metadata are final, create reviews/PROBLEM_HANDLE/READY.json with author, ready:true, and document_sha256. This marker freezes your report for the separate verifier; do not edit it after marking ready unless coordinating with verifier. Write metadata with every completed report, not only at the end of the group. Root needs durable progress if usage stops.

## Interleaved independent verification

Each agent authors its own group and independently audits a different group in a ring: a audits f, b audits a, c audits b, d audits c, e audits d, f audits e. Do not self-review. After completing each small block of about 3 authored reports, check the other group's READY markers and audit any available unaudited reports. If none are ready, continue authoring; never idle waiting while own work remains. Communicate readiness/corrections directly with the other agent. After authoring all own targets, finish all assigned independent audits as they become ready. Each completed report needs exactly one independent final auditor; root will coordinate if a replacement changes the count.

Read the full report and exact source/YAML independently. Check every new result, counterexample, computational claim, and scope attribution. Reject unsupported or insignificant additions. Inspect and rerun relevant computational checkers when their output supports a finding. Correct mathematical or scope issues where possible, then recheck final bytes. Record all corrections. Do not alter another group's source snapshots. Do not certify unchecked external references.

Write audits/PROBLEM_HANDLE.json with:
- handle, contribution_handle
- reviewer: your exact task path
- model: gpt-6.1-sol
- reasoning_effort: ultra
- verdict: approved_scoped, revise, or reject
- document_sha256: SHA256 of final report bytes
- source_sha256: verified actual manuscript hash
- checked_scope: string
- checks_performed: meaningful checks actually performed
- changes_made: array (empty when none)
- limitations: array including no human/formal verification and external references not independently verified unless actually done
- significance: specific justification for submission

Send root progress after each block, and immediately report blocking defects. Root posts only documents with current final-byte approvals and pinned evidence. Root will publish in small checkpoints; never change an already submitted report without telling root.
