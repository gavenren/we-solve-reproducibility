# SPDX-License-Identifier: Apache-2.0
import pathlib,json,hashlib,sys
r=pathlib.Path(__file__).resolve().parents[1]
a={t['alias']:t for t in json.load(open(r/'assignments/c.json'))}
for v in json.loads(sys.argv[1]):
 h=v['handle'];p=r/'reviews'/h;s=r/'sources'/h;t=a[h];body=(p/'review.md').read_bytes();sha=hashlib.sha256(body).hexdigest();assert sha==json.load(open(p/'READY.json'))['document_sha256'];m=json.load(open(p/'metadata.json'));y=(s/'contribution.yaml').read_text();assert all(x in y for x in [t['problem_id'],t['target']['id'],t['target']['revision_id']]);ss=hashlib.sha256((s/'manuscript.tex').read_bytes()).hexdigest();assert ss==m['source_sha256']; v.update(contribution_handle=t['target_handle'],reviewer='/root/new200_d',model='gpt-6.1-sol',reasoning_effort='ultra',verdict='approved_scoped',document_sha256=sha,source_sha256=ss,changes_made=v.get('changes_made',[]),limitations=['No human or formal verification.','External references and empirical validity not independently verified.']);(r/'audits'/f'{h}.json').write_text(json.dumps(v,indent=2)+'\n');print(h,sha[:12])
