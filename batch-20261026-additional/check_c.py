"""Independent arithmetic checks for the c-assignment reviews (standard library)."""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose
import random

def require(condition, message):
    if not condition:
        raise AssertionError(message)

# H24: the hidden-transfer mean restriction gives exactly [0, 1].
for j in range(101):
    u1 = F(j, 100)
    u3 = 2-u1
    require(0 <= u1 <= 1 and 0 <= u3 <= 3, 'H24 feasibility')
    require((u1+u3)/2 == 1, 'H24 hidden mean')
    require((u3-u1)/2 == 1-u1, 'H24 covariance')
d, kap, t = F(1,2), F(1), F(1,2)
alpha = (1-d)*(1-t)/kap
r = t*(d+(1-d)*alpha)
alpha2 = (1-d)*(1-r)/kap
r2 = r*(d+(1-d)*alpha2)
require((alpha, r, alpha2, r2)==(F(1,4),F(5,16),F(11,32),F(215,1024)), 'H24 horizon example')

# J42: identical wage passthrough and baseline observables, different gains.
for e,h,K in [(1,.5,0),(2,.25,2)]:
    require(isclose((1+1/e)/(1-h)+K, 4), 'J42 R0')
    require(isclose(1/(1+e*h), 2/3), 'J42 rho')
    require((1+1/e)**(e/(1+e*h)) < 3, 'J42 population cap')
print('J42 gains:', (2/3)*log(2), (2/3)*log(1.5))

# H11: two safe pairs of orders with opposite service rankings.
def qservice(k,a):
    x=min(k,1/a)
    return (k-x)**2/k
require(qservice(2,2)>qservice(1,4), 'H11 capacity-first example')
require(qservice(F(11,10),1)<qservice(1,10), 'H11 accountability-first example')

# G28: exact solvency boundary before the liquidity fold.
v,alpha,k,l = F(1),F(1),F(1,16),F(1,8)
zsolv=F(1,4); xsolv=v*zsolv-alpha*zsolv*zsolv
wsolv=(l+xsolv)/(1-k)
wfold=(l+v*v/(4*alpha))/(1-k)
require((xsolv,wsolv,wfold)==(F(3,16),F(1,3),F(2,5)), 'G28 thresholds')
for j in range(1,100):
    w=float(wsolv)+(float(wfold)-float(wsolv))*j/100
    x=w*(1-float(k))-float(l)
    z=(1-sqrt(1-4*x))/2
    require(z<1-float(l) and float(k)-z*z<0, 'G28 solvent/liquid separation')

# L42: selected tariff determines exclusion, keeping costs fixed.
cI,d,Fcost,s = 10,6,2,1
for p in [6.1,8,9,9.1,10,11]:
    require(p>cI-d+Fcost, 'L42 selected tariff admissible')
    exclusive_profit=p-cI+s
    require((exclusive_profit>0)==(p>cI-s), 'L42 exclusion threshold')

# D72: product sensitivity bound is attained by one live state.
eps=[.1,.2,.3]
survival=1
for e in eps:
    survival*=1-e
require(isclose(1-survival,.496), 'D72 sharp product bound')
require(1-survival < sum(eps), 'D72 improvement')

# G21: CARA cost threshold and stop-loss characterization.
q,I,H,b,rho=.5,.2,2,1,1
h0=H-I/q
D=sqrt(1-q+q*exp(-rho*h0))
mstar=q*h0+(2*q/rho)*log((D-(1-q))/q)
def gap(m):
    hm=h0-m/q
    G=-exp(-rho*b)*(1-q+q*exp(-rho*hm/2))**2
    S=-exp(-rho*b)*(1-q+q*exp(-rho*h0))
    return G-S
require(0 < mstar < q*(2-q)*H/2-I, 'G21 threshold feasible')
require(abs(gap(mstar)) < 1e-12 and gap(mstar/2)>0 and gap(1.5*mstar)<0, 'G21 CARA exact threshold')
print('G21 CARA meeting-cost threshold:',mstar)
for q in [.2,.5,.8]:
    RJ=.3; RI=(2-q)*RJ; H=2
    p=q*q; m=2*q*(1-q)
    a=(H-2*RJ)/2; bb=(H-RI)/2; c=H-RI; dd=H-RJ
    for j in range(101):
        z=H*j/100
        callJ=p*max(dd-z,0)+m*max(a-z,0)
        callI=p*max(c-z,0)+m*max(bb-z,0)
        if z<=a: expected=0
        elif z<=bb: expected=m*(z-a)
        elif z<=c: expected=p*(RI-RJ)
        elif z<=dd: expected=p*(dd-z)
        else: expected=0
        require(abs(callJ-callI-expected)<1e-12, 'G21 stop-loss formula')

# C72: exact optimal 2x2 centering and certificate, 200 rational games.
def zero_sum_2(H):
    for i in range(2):
        for j in range(2):
            if H[i][j]>=H[1-i][j] and H[i][j]<=H[i][1-j]:
                return [F(int(a==i)) for a in range(2)],[F(int(a==j)) for a in range(2)]
    a,bb=H[0]; c,d=H[1]
    den=a-bb-c+d
    px=(d-c)/den; py=(d-bb)/den
    require(0<=px<=1 and 0<=py<=1,'C72 zero-sum mixture')
    return [px,1-px],[py,1-py]
def payoff(A,x,y):
    return sum(x[i]*A[i][j]*y[j] for i in range(2) for j in range(2))
rng=random.Random(20261027)
for _ in range(200):
    A=[[F(rng.randrange(11),10) for _ in range(2)] for _ in range(2)]
    B=[[F(rng.randrange(11),10) for _ in range(2)] for _ in range(2)]
    M=[[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
    delta=M[0][0]+M[1][1]-M[0][1]-M[1][0]
    ss=delta/4
    ds=[M[0][0]-ss,M[0][1]+ss]
    cs=[F(0),M[1][0]-M[0][0]+2*ss]
    C=[[M[i][j]-cs[i]-ds[j] for j in range(2)] for i in range(2)]
    require(C==[[ss,-ss],[-ss,ss]], 'C72 exact residual')
    HH=[[(A[i][j]-ds[j]-B[i][j]+cs[i])/2 for j in range(2)] for i in range(2)]
    x,y=zero_sum_2(HH)
    row=max(sum(A[i][j]*y[j] for j in range(2)) for i in range(2))-payoff(A,x,y)
    col=max(sum(x[i]*B[i][j] for i in range(2)) for j in range(2))-payoff(B,x,y)
    require(max(row,col)<=abs(ss), 'C72 regret certificate')
print('All c-assignment independent arithmetic checks passed.')

# The C72 structural factor is attained by a degenerate surrogate equilibrium.
A=[[F(5,8),F(3,8)],[F(3,8),F(5,8)]]
delta=2*A[0][0]+2*A[1][1]-2*A[0][1]-2*A[1][0]
require(delta/4==F(1,4), 'C72 sharp centering')
HH=[[(A[i][j]-1-A[i][j])/2 for j in range(2)] for i in range(2)]
require(all(v==F(-1,2) for row in HH for v in row), 'C72 degenerate surrogate')
require(A[0][0]-A[0][1]==F(1,4), 'C72 sharp regret')
print('C72 sharp-factor example passed.')
