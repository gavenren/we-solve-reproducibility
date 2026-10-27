#!/usr/bin/env python3
"""Compare read-only GitHub issue snapshots with exact submission receipts."""
# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parent
def main():
    p=argparse.ArgumentParser();p.add_argument('--directory',required=True);a=p.parse_args()
    receipts=[json.loads(l) for l in (ROOT/'submission_receipts.jsonl').read_text().splitlines() if l.strip()]
    payload={r['handle']:r for r in json.loads((ROOT/'submission_payload.json').read_text())}
    remote={r['number']:r for f in (ROOT/a.directory).glob('part_*.json') for r in json.loads(f.read_text())}
    assert len({r['problem_id'] for r in receipts})==len(receipts),'Duplicate problem IDs'
    out=[]
    for r in receipts:
        i=remote[r['number']];p=payload[r['handle']]
        digest=hashlib.sha256(i['body'].encode()).hexdigest()
        assert digest==r['body_sha256']==p['body_sha256'],f'Remote body mismatch: {r["number"]}'
        assert i['title']==p['title'] and i['url']==r['url'],f'Remote identity mismatch: {r["number"]}'
        out.append(dict(handle=r['handle'],number=r['number'],url=i['url'],state=i['state'],labels=i['labels'],body_sha256=digest,matches_prepared_body=True))
    result={'verified_issues':len(receipts),'distinct_problems':len(receipts),'all_remote_bodies_match':True,'all_have_intake_and_review_labels':all({'intake','review'}<=set(r['labels']) for r in out),'label_limitation':'Issue labels are requested during creation. This integration previously returned GitHub 403 Resource not accessible by integration for explicit labeling; repository labeling permissions are not assumed.','records':out}
    (ROOT/'readback_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['verified_issues','distinct_problems','all_remote_bodies_match','all_have_intake_and_review_labels']}))
if __name__=='__main__':main()
