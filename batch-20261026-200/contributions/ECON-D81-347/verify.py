# SPDX-License-Identifier: Apache-2.0
import math,json
if not __debug__:
    raise RuntimeError('Run with assertions enabled')
def sphere(k): return 2*math.pi**((k+1)/2)/math.gamma((k+1)/2)
count=0
for d in range(2,11):
    for t in [0.0001,0.001,0.01,0.1,0.25,0.5,1.0]:
        theta=math.acos(1/(1+t))
        N=10000
        step=theta/N
        integral=step/3*sum((1 if k in (0,N) else 4 if k%2 else 2)*math.sin(k*step)**(d-2) for k in range(N+1))
        cap=sphere(d-2)/sphere(d-1)*integral
        upper=sphere(d-2)/((d-1)*sphere(d-1))*(math.pi/math.sqrt(2))**(d-1)*t**((d-1)/2)
        assert cap<=upper*(1+1e-10)
        assert theta<=math.pi*math.sqrt(t/(2*(1+t)))+1e-12
        count+=1
print(json.dumps({'status':'PASS','cases':count,'dimensions':'2..10','arithmetic':'floating point Simpson integration, 10000 panels','scope':'sanity check only; not rigorous quadrature or theorem verification'}))
