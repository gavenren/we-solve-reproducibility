#!/usr/bin/env python3
"""Assemble reviewed contributions; no network calls or issue creation."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
PUBLIC = 'batch-20261026-additional'
REPO = 'https://github.com/gavenren/we-solve-reproducibility'
UPSTREAM = 'bd5218964aa5efa77ac062e3600b8cfe70df528c'
FINDINGS = {'Supports the claim','Error found','Gap found','Counterexample','Known result','Reproduced','Not reproduced','Reference suggestion','Comment'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def read(path):
    return json.loads(path.read_text())

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--commit')
    parser.add_argument('--ready-only',action='store_true',help='Checkpoint only independently approved final documents.')
    args = parser.parse_args()
    if args.commit:
        assert re.fullmatch('[0-9a-f]{40}',args.commit)
    candidates = {r['alias']:r for group in 'abcde' for r in read(ROOT/'assignments'/f'{group}.json')}
    prior = read(ROOT/'prior_issues_snapshot.json')
    records=[]
    for path in sorted((ROOT/'reviews').glob('*/metadata.json')):
        m=read(path)
        h=m['handle']
        if h.endswith('-A1') and h not in candidates:
            h=h[:-3]
        if args.ready_only:
            candidate_audit=ROOT/'audits'/f'{h}.json'
            if not candidate_audit.exists() or read(candidate_audit).get('verdict')!='approved_scoped':
                continue
        c=candidates[h]
        target=c['target']
        assert m['problem_id']==c['problem_id'],h
        assert m['contribution_handle']==c['target_handle'],h
        assert m['contribution_id']==target['id'],h
        assert m['revision_id']==target['revision_id'],h
        assert m['finding'] in FINDINGS,h
        assert m['model']=='gpt-6.1-sol' and m['reasoning_effort']=='ultra',h
        assert m['author'].startswith('/root/reviews_'),h
        assert UPSTREAM in m['source_url'],h
        assert not any(m['contribution_handle'] in (i['body'] or '') or i['title']=='Attempt: '+h for i in prior),h
        doc=path.with_name('review.md')
        data=doc.read_bytes()
        assert len(data)>1500,h
        assert not re.search(r'```(?:python|lean|javascript|js|bash|sh)\b',data.decode(),re.I),h
        source_matches=[p for p in (ROOT/'sources').glob('**/*') if p.is_file() and sha(p.read_bytes())==m['source_sha256']]
        assert source_matches, f'Missing exact source: {h}'
        audit_path=ROOT/'audits'/f'{h}.json'
        assert audit_path.exists(), f'Missing audit: {h}'
        audit=read(audit_path)
        assert audit['verdict']=='approved_scoped',f'Unapproved: {h}'
        assert audit['document_sha256']==sha(data),f'Stale audit: {h}'
        assert audit['model']=='gpt-6.1-sol' and audit['reasoning_effort']=='ultra',h
        assert audit['reviewer']!=m['author'],f'Self review: {h}'
        if isinstance(m['checked_scope'],list):
            m['checked_scope']='; '.join(m['checked_scope'])
        records.append(dict(m,handle=h,document_path=str(doc.relative_to(ROOT)),document_sha256=sha(data),metadata_path=str(path.relative_to(ROOT)),audit_path=str(audit_path.relative_to(ROOT)),reviewer=audit['reviewer']))
    assert len({r['problem_id'] for r in records})==len(records)
    manifest={'batch':PUBLIC,'upstream_commit':UPSTREAM,'candidate_count':len(candidates),'reviewed_count':len(records),'submitted_count':0,'editorially_accepted_count':0,'prior_issues_checked':len(prior),'records':records}
    receipt_path=ROOT/'submission_receipts.jsonl'
    receipts=[]
    if receipt_path.exists():
        receipts=[json.loads(l) for l in receipt_path.read_text().splitlines() if l.strip()]
        assert len({r['handle'] for r in receipts})==len(receipts)
        manifest['submitted_count']=len(receipts)
    write(ROOT/'manifest.json',manifest)
    if args.commit:
        base=f'{REPO}/blob/{args.commit}/{PUBLIC}'
        payload=[]
        old_payload={r['handle']:r for r in read(ROOT/'submission_payload.json')} if (ROOT/'submission_payload.json').exists() else {}
        submitted={r['handle']:r for r in receipts}
        for r in records:
            h=r['handle']; audit=read(ROOT/r['audit_path'])
            if h in submitted:
                old=old_payload[h]
                assert old['document_sha256']==r['document_sha256'],f'Submitted document changed: {h}'
                assert old['body_sha256']==submitted[h]['body_sha256'],f'Submitted body changed: {h}'
                payload.append(old)
                continue
            body=(ROOT/r['document_path']).read_text().strip()
            body += f'\n\n**Frozen review and reproducibility files:** [review source]({base}/{r["document_path"]}) · [evidence directory]({REPO}/tree/{args.commit}/{PUBLIC}). Original check programs, where used, are hosted separately there.'
            body += f'\n\n**Independent final check:** [{r["reviewer"]}, explicitly configured GPT-6.1 Sol / Ultra]({base}/{r["audit_path"]}). Reviewed document SHA-256: `{r["document_sha256"]}`. The finding is limited to the scope below; this is not editorial acceptance or human peer review.'
            models=f'OpenAI GPT 6.1 Sol | version: unknown (requested model ID gpt-6.1-sol) | thinking: Ultra (explicitly configured) | time: unknown | roles: {r.get("authoring_agents",r["author"])} authored the mathematical review; {r["reviewer"]} independently checked the final document and cited source scope.\n\nOpenAI Codex (based on GPT-6) | version: unknown | thinking: unknown | time: unknown | role: /root selected targets, supplied supplementary derivation suggestions for the L42-195 and D83-218 reviews, checked provenance and submission fields, and assembled and submitted the batch.\n\nGaven (@gavenren): requested and authorized the submissions; no human mathematical verification is claimed.'
            fields=[('Contribution handle',r['contribution_handle']),('Finding',r['finding']),('What you checked',r['checked_scope']+f'\n\nContribution `{r["contribution_id"]}`; revision `{r["revision_id"]}`; source commit `{UPSTREAM}`.'),('Evidence',body),('Models used','OpenAI GPT 6.1 Sol, Other (named below)'),('Thinking level / time','Mixed (specified per model below)'),('Other LLMs','OpenAI, Codex (based on GPT-6)'),('Per-model versions, thinking and roles',models),('Model eligibility and verification evidence',f'The author and independent final reviewer were explicitly configured as GPT-6.1 Sol with Ultra reasoning. [Final-byte audit, checks, and limitations]({base}/{r["audit_path"]}). The root orchestration instance has undisclosed serving version and thinking settings. The review does not certify unchecked external references or resolve the wider open problem.'),('Conflicts of interest','Gaven (@gavenren) requested this contribution. The review author and final verifier are separate AI agents. The upstream manuscript author is credited in the pinned source; no affiliation with its author or human peer-review status is claimed.'),('Declarations','- [X] I have the right to publish this material under CC BY 4.0, and third-party material is credited.\n- [X] I understand that this issue and its contents are public immediately.\n- [X] Every LLM and person involved is listed, with versions or "unknown".')]
            text='\n\n'.join('### '+k+'\n\n'+str(v).strip() for k,v in fields)+'\n'
            assert len(text)<60000
            out=ROOT/'forms'/f'{h}.md';out.parent.mkdir(exist_ok=True);out.write_text(text)
            payload.append({'handle':h,'problem_id':r['problem_id'],'title':'Review: '+r['contribution_handle'],'body':text,'labels':['intake','review'],'body_sha256':sha(text.encode()),'document_sha256':r['document_sha256'],'evidence_commit':args.commit,'file':str(out.relative_to(ROOT))})
        write(ROOT/'submission_payload.json',payload)
    print(json.dumps({k:manifest[k] for k in ['reviewed_count','submitted_count','editorially_accepted_count','prior_issues_checked']}))

if __name__=='__main__':
    main()
