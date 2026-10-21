#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact finite-component certificate for Gaussian-prime walks from the origin."""
import argparse
from collections import deque
from functools import lru_cache
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

if not __debug__:
    raise SystemExit("Refusing optimized mode: exact certificate checks must remain active.")

STEP_SQUARED = 8
OFFSETS = [(a,b) for a in range(-isqrt(STEP_SQUARED),isqrt(STEP_SQUARED)+1)
           for b in range(-isqrt(STEP_SQUARED),isqrt(STEP_SQUARED)+1)
           if 0<a*a+b*b<=STEP_SQUARED]

@lru_cache(None)
def trial_prime(n):
    if n<2:
        return False
    return all(n%d for d in range(2,isqrt(n)+1))

def gaussian_trial(z):
    a,b=z
    if a and b:
        return trial_prime(a*a+b*b)
    p=abs(a or b)
    return p%4==3 and trial_prime(p)

def generate():
    origin=(0,0)
    parents={origin:None}
    todo=deque([origin])
    while todo:
        a,b=todo.popleft()
        for u,v in OFFSETS:
            z=(a+u,b+v)
            if z not in parents and gaussian_trial(z):
                if max(map(abs,z))>1000 or len(parents)>100000:
                    raise ValueError("Safety bound exceeded; no finiteness result emitted")
                parents[z]=(a,b)
                todo.append(z)
    vertices=sorted(parents)
    return {"step_squared":STEP_SQUARED,"root":[0,0],
            "vertices":[list(z) for z in vertices],
            "parents":[[list(z),list(parents[z])] for z in vertices if z!=origin]}

def validate(cert):
    def require(ok,message):
        if not ok:
            raise ValueError(message)
    require(cert.get("step_squared")==8 and cert.get("root")==[0,0],"Wrong scope")
    raw=cert["vertices"]
    require(all(isinstance(z,list) and len(z)==2 and
                all(type(x) is int for x in z) for z in raw),"Invalid coordinates")
    vertices={tuple(z) for z in raw}
    require(len(vertices)==len(raw) and (0,0) in vertices,"Duplicate/missing vertex")
    bound=max(max(map(abs,z)) for z in vertices)+isqrt(STEP_SQUARED)
    limit=2*bound*bound
    sieve=bytearray(b"\x01")*(limit+1)
    sieve[0:2]=b"\x00\x00"
    for q in range(2,isqrt(limit)+1):
        if sieve[q]:
            for k in range(q*q,limit+1,q):
                sieve[k]=0
    def gp(z):
        a,b=z
        if a and b:
            return bool(sieve[a*a+b*b])
        q=abs(a or b)
        return q%4==3 and bool(sieve[q])
    require(all(z==(0,0) or gp(z) for z in vertices),"Nonprime vertex")
    parent_rows=cert["parents"]
    parents={tuple(z):tuple(p) for z,p in parent_rows}
    require(len(parents)==len(parent_rows)==len(vertices)-1,"Wrong parent count")
    require(set(parents)==vertices-{(0,0)},"Wrong child set")
    for z,p in parents.items():
        require(p in vertices and 0<(z[0]-p[0])**2+(z[1]-p[1])**2<=8,
                "Invalid parent edge")
    reached={(0,0)}
    children={}
    for z,p in parents.items():
        children.setdefault(p,[]).append(z)
    todo=deque([(0,0)])
    while todo:
        for z in children.get(todo.popleft(),[]):
            require(z not in reached,"Parent cycle")
            reached.add(z)
            todo.append(z)
    require(reached==vertices,"Disconnected parent forest")
    checked=set()
    for a,b in vertices:
        for u,v in OFFSETS:
            z=(a+u,b+v)
            checked.add(z)
            require(not gp(z) or z in vertices,"Prime exit from alleged component")
    maxnorm=max(a*a+b*b for a,b in vertices)
    return {"verdict":"PASS","step_squared":8,"gaussian_prime_vertices":len(vertices)-1,
            "origin_included":True,"maximum_norm":maxnorm,
            "maximum_absolute_coordinate":bound-isqrt(STEP_SQUARED),
            "distinct_neighbor_positions_checked":len(checked),
            "independent_verifier":"Eratosthenes sieve, parent-tree reachability and complete neighbor closure",
            "generation":"Unbounded BFS with exact trial division; safety bound aborts without success"}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verify",type=Path,help="Only verify this exact certificate")
    args=ap.parse_args()
    if args.verify:
        cert=json.loads(args.verify.read_text())
    else:
        cert=generate()
    result=validate(cert)
    blob=(json.dumps(cert,sort_keys=True,separators=(",",":"))+"\n").encode()
    result["certificate_sha256"]=hashlib.sha256(blob).hexdigest()
    if not args.verify:
        target=Path(__file__).with_name("certificate.json")
        target.write_bytes(blob)
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=="__main__":
    main()

