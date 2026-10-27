from fractions import Fraction as F
import json
from pathlib import Path
out={}
# All integer query budgets, multiple cost levels including the exact threshold.
tested=0
for n in range(2,101):
    threshold=F(2,n+2)
    for k in [F(0),threshold/2,threshold,threshold*2,F(1)]:
        vals=[F(q+1,n)-k*(q-F(q*(q-1),2*n)) for q in range(n)]
        assert max(vals)==max(vals[0],vals[-1])
        assert ((vals[-1]>=vals[0]) == (k<=threshold))
        tested+=1
out['ECON-D91-482']={'exact_budget_comparisons':tested,'n_range':[2,100],'passed':True}
# Check two-point tensor mixture distinction and a three-point full-rank design.
ps=[F(1,4),F(1,2),F(3,4)]
cols=[[(1-p)**2,p*(1-p),p**2] for p in ps]
a,b,c=cols
det=a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])
assert det!=0
moments1=[F(1,4)**r/2+F(3,4)**r/2 for r in range(3)]
moments2=[F(1,2)**r for r in range(3)]
assert moments1[:2]==moments2[:2] and moments1[2]!=moments2[2]
out['ECON-C72-489']={'three_column_tensor_minor':str(det),'one_draw_equal_two_draw_different':True,'second_moments':[str(moments1[2]),str(moments2[2])]}
# Independent entry and transfer-accounting arithmetic.
regimes=[]
for d,f in [(F(4),F(4,5)),(F(5),F(2))]:
    n=max(i for i in range(1,20) if d*d/F((i+1)**2)>=f)
    q=n*d/(n+1)
    cs=q*q/4
    w=d*q-q*q/2-n*f
    regimes.append({'n':n,'Q':str(q),'CS':str(cs),'W':str(w)})
assert regimes==[{'n':3,'Q':'3','CS':'9/4','W':'51/10'},{'n':2,'Q':'10/3','CS':'25/9','W':'64/9'}]
out['ECON-L51-495']=regimes
# Different availability sample from the manuscript: two singleton-1 sets,
# one singleton-2, and three joint sets. Upper feasible marginal is 5/6.
# Smooth upper conditionals by eta=1/3; joint action-1 probability becomes5/6.
marginal=F(2,6)+F(3,6)*F(5,6)
assert marginal==F(3,4)
weights=(F(5),F(1))
assert F(2,6)+F(3,6)*weights[0]/sum(weights)==marginal
out['ECON-C73-532']={'new_sample_sizes':{'singleton1':2,'singleton2':1,'joint':3},'eta':'1/3','smoothed_marginal':['3/4','1/4'],'weights':['5','1'],'passed':True}
path=Path(__file__).with_name('econ_e_exact_checks.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
