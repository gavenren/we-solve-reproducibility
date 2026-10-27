# SPDX-License-Identifier: Apache-2.0
"""Persist group-f independent audits after mathematical verification."""
from pathlib import Path
import json, hashlib, sys
b=Path(__file__).resolve().parents[1];a={t['alias']:t for t in json.loads((b/'assignments/f.json').read_text())}
for r in json.loads(Path(sys.argv[1]).read_text()):
 h=r['handle'];d=b/'reviews'/h;s=b/'sources'/h;p=json.loads((s/'provenance.json').read_text());t=a[h];y=(s/'contribution.yaml').read_text()
 assert 'revision_id: '+t['target']['revision_id'] in y and 'contribution_id: '+t['target']['id'] in y and 'home_problem_id: '+t['problem_id'] in y
 for rec in p['records']:
  data=(s/rec['local_file']).read_bytes();assert hashlib.sha256(data).hexdigest()==rec['sha256'];assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==rec['git_blob_sha']
 src=next(x for x in p['records'] if x['local_file'].endswith('.tex'));doc=hashlib.sha256((d/'review.md').read_bytes()).hexdigest();assert doc==json.loads((d/'READY.json').read_text())['document_sha256']
 out={'handle':h,'contribution_handle':t['target_handle'],'reviewer':'/root/new200_a','model':'gpt-6.1-sol','reasoning_effort':'ultra','verdict':'approved_scoped','document_sha256':doc,'source_sha256':src['sha256'],'checked_scope':r['scope'],'checks_performed':r['checks']+['Verified SHA256 and Git blob SHA of exact saved source and YAML; checked canonical IDs and final READY hash.'],'changes_made':r.get('changes',[]),'limitations':['Independent AI mathematical review; no human or formal verification.','External references not independently verified; no external literature claim certified.'],'significance':r['significance']}
 (b/'audits'/(h+'.json')).write_text(json.dumps(out,indent=2)+'\n');print(h,doc)
