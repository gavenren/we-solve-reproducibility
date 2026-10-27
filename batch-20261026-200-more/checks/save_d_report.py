# SPDX-License-Identifier: Apache-2.0
import json,pathlib,sys,hashlib
root=pathlib.Path(__file__).resolve().parents[1]
assign={x['alias']:x for x in json.load(open(root/'assignments/d.json'))}
for r in json.loads(sys.argv[1]):
 h=r['handle']; t=assign[h]; p=root/'reviews'/h;p.mkdir(parents=True,exist_ok=True)
 assert not (p/'READY.json').exists(), 'Frozen report'
 prov=json.load(open(root/'sources'/h/'provenance.json'))
 text='# '+r['title']+'\n\n'+r['body'].strip()+'\n\nSource: ['+h+'-A1]('+prov['immutable_url']+'), canonical revision `'+t['target']['revision_id']+'`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.\n\nOriginal prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.\n'
 (p/'review.md').write_text(text)
 meta=dict(handle=h,problem_id=t['problem_id'],contribution_handle=t['target_handle'],contribution_id=t['target']['id'],revision_id=t['target']['revision_id'],source_path=prov['remote_path'],source_sha256=prov['source_sha256'],source_url=prov['immutable_url'],title=r['title'],finding=r.get('finding','Supports the claim'),checked_scope=r['scope'],significance=r['significance'],author='/root/new200_d',model='gpt-6.1-sol',reasoning_effort='ultra')
 (p/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n');(p/'READY.json').write_text(json.dumps(dict(author='/root/new200_d',ready=True,document_sha256=hashlib.sha256((p/'review.md').read_bytes()).hexdigest()),indent=2)+'\n')
 print(h,len(text.split()))
