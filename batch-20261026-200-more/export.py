#!/usr/bin/env python3
"""Prepare a public evidence tree without copied upstream manuscripts."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'public_export'/'batch-20261026-200-more'

def main():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    records=manifest['records']
    OUT.mkdir(parents=True,exist_ok=True)
    def copy(relative):
        source=ROOT/relative;dest=OUT/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,dest)
    for r in records:
        for key in ['document_path','metadata_path','audit_path']:
            copy(r[key])
        for path in (ROOT/r['document_path']).parent.iterdir():
            if path.is_file() and path.name!='READY.json' and path.suffix in {'.py','.json','.txt','.md'}:
                copy(path.relative_to(ROOT))
    for name in ['assemble.py','export.py','manifest.json','TASK_PROTOCOL.md','CONFIGURATION.json']:
        copy(name)
    if (ROOT/'readback_verification.json').exists():
        copy('readback_verification.json')
    for optional in ['provenance_corrections.json','issue_updates.jsonl']:
        if (ROOT/optional).exists():
            copy(optional)
    # Only original code/check outputs, never copied source manuscripts or issue histories.
    for path in sorted(ROOT.iterdir()):
        if path.is_file() and (path.name.startswith('check') or path.name.startswith('verify')) and path.suffix in {'.py','.json','.txt','.md'}:
            copy(path.name)
    for directory in ['checks','checkers']:
        if (ROOT/directory).exists():
            for path in (ROOT/directory).rglob('*'):
                if path.is_file() and path.suffix in {'.py','.json','.txt','.md'}:
                    copy(path.relative_to(ROOT))
    receipts=[]
    if (ROOT/'submission_receipts.jsonl').exists():
        receipts=[json.loads(l) for l in (ROOT/'submission_receipts.jsonl').read_text().splitlines() if l.strip()]
        copy('submission_receipts.jsonl')
    by_handle={r['handle']:r for r in receipts}
    lines=[
        '# 200 more WeSolve contributions — 26 October 2026', '',
        f'{len(records)} original scoped mathematical reviews independently checked. {len(receipts)} GitHub issue submissions recorded. Editorial acceptance is not claimed.', '',
        'Each review identifies an exact upstream revision, gives a substantive independent derivation, extension, sharpness example or computational check, and states its limits. A supporting review is not a solution of the wider catalogue problem.', '',
        'All authoring and independent final verification agents were explicitly configured as `gpt-6.1-sol` with `ultra` reasoning. The orchestrating root identifies as OpenAI Codex based on GPT-6; its exact serving version and thinking setting were not exposed. Exact serving revisions and durations are unknown. Gaven (@gavenren) requested and authorized publication; no human mathematical verification is claimed.', '',
        'Final reviews were checked by separate configured agents in a six-team review cycle. Audits record final document hashes, actual checks, corrections and scope; they are not formal proof certificates.', '',
        f'Prior-work check: {manifest["prior_issues_checked"]} issues authored by gavenren in We-Solve/research were compared against the assigned contribution handles. No matching prior submission was found for these targets at the time of checking.', '',
        f'Upstream snapshot: [`{manifest["upstream_commit"]}`](https://github.com/We-Solve/research/tree/{manifest["upstream_commit"]}). Source copies are not redistributed here; original reviews link to the pinned files.', '',
        '## Contributions', '',
        '| Problem | Review and independent result | Submission |',
        '|---|---|---|'
    ]
    for r in records:
        receipt=by_handle.get(r['handle'])
        status=f'[#{receipt["number"]}]({receipt["url"]})' if receipt else 'Checked; not yet recorded as submitted'
        title=r['title'].replace('|','\\|')
        lines.append(f'| {r["handle"]} | [{title}]({r["document_path"]}) · [audit]({r["audit_path"]}) | {status} |')
    lines += ['', '## Rights and reproducibility', '',
        'Original prose and audit records: CC BY 4.0. Original verification code: Apache-2.0. Upstream authors and source revisions are credited in each review. All numerical or finite checks are limited to their recorded domain and do not replace mathematical proof.', '',
        'The assembly script depends on local source snapshots and the deduplication snapshot, which are deliberately not redistributed in this evidence export. The original mathematical check scripts and their recorded outputs are included when present. The contribution prose provides the mathematical arguments independently of code execution.', '']
    if (ROOT/'readback_verification.json').exists():
        verified_count=json.loads((ROOT/'readback_verification.json').read_text())['verified_issues']
        lines += ['## Submission verification', '',
            f'{verified_count} recorded issues were read back from GitHub: each title and complete body matched the prepared submission at that verification checkpoint. The requested intake/review labels were absent in those readback records. A prior explicit label attempt returned GitHub 403 (Resource not accessible by integration), so labeling requires repository permissions. No editorial acceptance is claimed. See [readback verification](readback_verification.json).', '']
    (OUT/'README.md').write_text('\n'.join(lines))
    sums=[]
    for path in sorted(OUT.rglob('*')):
        if path.is_file() and path.name!='SHA256SUMS':
            sums.append(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.relative_to(OUT).as_posix())
    (OUT/'SHA256SUMS').write_text('\n'.join(sums)+'\n')
    entries=[{'path':p.relative_to(OUT.parent).as_posix(),'mode':'100644','type':'blob','content':p.read_text()} for p in sorted(OUT.rglob('*')) if p.is_file()]
    (ROOT/'tree_entries.json').write_text(json.dumps(entries,ensure_ascii=False))
    old=json.loads((ROOT/'published_file_hashes.json').read_text()) if (ROOT/'published_file_hashes.json').exists() else {}
    hashes={e['path']:hashlib.sha256(e['content'].encode()).hexdigest() for e in entries}
    changes=[e for e in entries if hashes[e['path']]!=old.get(e['path'])]
    chunks=[];chunk=[];size=0
    for entry in changes:
        amount=len(entry['content'].encode())
        if chunk and (size+amount>160000 or len(chunk)>=30):
            chunks.append(chunk);chunk=[];size=0
        chunk.append(entry);size+=amount
    if chunk:chunks.append(chunk)
    transfer=ROOT/'transfer';transfer.mkdir(exist_ok=True)
    for i,chunk in enumerate(chunks):
        (transfer/f'chunk_{i}.json').write_text(json.dumps(chunk,ensure_ascii=False))
    (ROOT/'pending_file_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    (ROOT/'transfer_manifest.json').write_text(json.dumps({'chunks':len(chunks),'changed_files':len(changes),'reviewed_count':len(records),'submitted_count':len(receipts)},indent=2)+'\n')
    print(json.dumps({'files':len(entries),'reviews':len(records),'receipts':len(receipts),'bytes':sum(len(e['content'].encode()) for e in entries)}))

if __name__=='__main__':main()
