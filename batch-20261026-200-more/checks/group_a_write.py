# SPDX-License-Identifier: Apache-2.0
"""Persist finished group-a mathematical reports with canonical provenance."""
from pathlib import Path
import json, hashlib, sys
b=Path(__file__).resolve().parents[1]
assign={t['alias']:t for t in json.loads((b/'assignments/a.json').read_text())}
for r in json.loads(Path(sys.argv[1]).read_text()):
 h=r['handle'];t=assign[h];s=json.loads((b/'sources'/h/'provenance.json').read_text());d=b/'reviews'/h;d.mkdir(exist_ok=True)
 if (d/'READY.json').exists(): raise RuntimeError('Report already frozen: '+h)
 body=r['body']+'\n\nSource: ['+h+'-A1]('+s['manuscript']['url']+'), canonical revision `'+t['target']['revision_id']+'`, pinned commit `'+s['ref']+'`.\n\nOriginal review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.\n'
 (d/'review.md').write_text(body)
 m={'handle':h,'problem_id':t['problem_id'],'contribution_handle':t['target_handle'],'contribution_id':t['target']['id'],'revision_id':t['target']['revision_id'],'source_path':s['manuscript']['remote_path'],'source_sha256':s['manuscript']['sha256'],'source_url':s['manuscript']['url'],'title':r['title'],'finding':r['finding'],'checked_scope':r['scope'],'significance':r['significance'],'author':'/root/new200_a','model':'gpt-6.1-sol','reasoning_effort':'ultra'}
 (d/'metadata.json').write_text(json.dumps(m,indent=2)+'\n');(d/'READY.json').write_text(json.dumps({'author':'/root/new200_a','ready':True,'document_sha256':hashlib.sha256(body.encode()).hexdigest()},indent=2)+'\n')
 print(h,len(body.split()))
