# SPDX-License-Identifier: Apache-2.0
from fractions import Fraction as F
import json

if not __debug__:
    raise RuntimeError('Run with assertions enabled')
checks=0
for den in range(1,13):
    grid=[F(k,den) for k in range(den+1)]
    for p0 in grid:
        for p1 in grid:
            all_values=[]
            for r in grid:
                x0=[x for x in grid if max(0,r+p0-1)<=x<=min(r,p0)]
                x1=[x for x in grid if max(0,r+p1-1)<=x<=min(r,p1)]
                values=[p1-p0-2*(b-a) for a in x0 for b in x1]
                lo=p1-p0-2*(min(r,p1)-max(0,r+p0-1))
                hi=p1-p0-2*(max(0,r+p1-1)-min(r,p0))
                assert min(values)==lo and max(values)==hi
                all_values+=values
                checks+=1
            radius=min(p0+p1,2-p0-p1)
            assert min(all_values)==-radius and max(all_values)==radius
print(json.dumps({'status':'PASS','known_prevalence_cases':checks,'denominators':'1..12','arithmetic':'exact fractions','scope':'binary-code formulas only'}))
