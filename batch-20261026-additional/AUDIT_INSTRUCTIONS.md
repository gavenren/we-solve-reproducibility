# Independent final review

Read each assigned final review, its exact pinned manuscript, and contribution metadata. Independently verify every mathematical addition, counterexample, edge case and reported computational check. Reject superficial restatements, unsupported novelty claims, claims exceeding scope, or misrepresentation of an acknowledged limitation as an error. This is a correctness and significance review, not a formatting-only check.

Work only on the assigned group. You may correct its report and metadata when needed, leaving a clear changes_made list. Check a corrected report again before approving its final bytes. Do not alter another group's report. No publication tools.

Write one audits/PROBLEM_HANDLE.json for each approved item (use ECON-X-123 without -A1), with these fields:

- handle: problem handle
- contribution_handle: target with -A1
- reviewer: your exact agent task path
- model: gpt-6.1-sol
- reasoning_effort: ultra
- verdict: approved_scoped, revise, or reject
- document_sha256: SHA256 of the final report bytes
- source_sha256: manuscript hash, confirmed against actual source
- checked_scope: string, covering all new claims and all explicitly checked source claims
- checks_performed: array of meaningful mathematical or computational checks actually done
- changes_made: array, empty when none
- limitations: array, including unchecked external references and no formal/human verification
- significance: concrete independent result/check justifying submission

Do not approve your own authored review. Supporting a source claim is not a vote; retain precise scope. Report all findings to root. Exact versions and time budgets remain unknown; only model ID and Ultra setting were explicitly configured.
