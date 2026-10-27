# SPDX-License-Identifier: Apache-2.0
from fractions import Fraction as F
import json
if not __debug__:
    raise RuntimeError('Run with assertions enabled')
count=0
for den in range(1,101):
    for i in range(den+1):
        for j in range(den-i+1):
            q=(F(den-i-j,den),F(i,den),F(j,den))
            b=q[1]+2*q[2]
            distance=abs(q[0]-1)+q[1]+q[2]
            assert distance<=2*b
            count+=1
print(json.dumps({'status':'PASS','simplex_points':count,'denominators':'1..100','arithmetic':'exact fractions','scope':'three-state boundary inequality; not the general continuity theorem'}))
