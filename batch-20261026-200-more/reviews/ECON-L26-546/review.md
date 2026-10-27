# The supervision model has an exact global coverage and setup-cost solution

The manuscript solves supervision conditional on coverage and gives one numerical intermediate-scale optimum. Its entire continuous coverage problem also has a closed-form solution, with a separate setup-cost participation decision.

Write \(B=LN>0\), \(G=Ng>0\), and \(A=\sqrt{B/k}\), retaining \(k>0\), capacity \(H\ge0\), setup cost \(F\ge0\), and coverage \(s\in[0,1]\). Let \(V(s)=NB^*(s)+F\) for \(s>0\): this is optimized value before setup cost. No service remains available at zero with value zero.

If \(A\le1\), supervision is zero and \(V(s)=(G-B)s\). The best positive-coverage candidate is full coverage when \(G>B\), and it is adopted exactly when \(G-B>F\); equality gives a tie with no service. If \(G\le B\), no service is optimal, with the evident zero-value ties when setup and slope both vanish. The same linear case applies for \(H=0\), regardless of \(A\).

Now suppose \(A>1,H>0\), and define
\[
m=G-2\sqrt{Bk}+k,\qquad s_0=H/(A-1).
\]
Below the capacity threshold, \(V(s)=ms\). Above it,
\[
V(s)=Gs-\frac{Bs^2}{s+H}-kH,
\quad
V'(s)=G-B+\frac{BH^2}{(s+H)^2}.
\]
The two branches and their first derivatives agree at \(s_0\), where the common derivative is \(m\). The capped derivative decreases strictly, since \(V''(s)=-2BH^2/(s+H)^3<0\).

If \(m\le0\), the uncapped branch is nonincreasing and every later derivative is no larger. Hence no service is optimal after subtracting nonnegative setup cost. At \(m=F=0\), any uncapped feasible coverage is also optimal with zero value; this tie does not create a strictly beneficial program.

If \(m>0\), the unique positive-scale maximizer before setup is as follows. When \(s_0\ge1\), it is \(s_c=1\). When \(s_0<1\) and \(G\ge B\), the derivative remains positive, so again \(s_c=1\). Otherwise \(s_0<1,G<B\), and
\[
s_c=\min\left\{1,\ H\left(\frac1{\sqrt{1-G/B}}-1\right)\right\}.
\]
The stationary point lies strictly above \(s_0\): positivity of \(m\) says \(G/B>2/A-1/A^2\), so \(\sqrt{1-G/B}<1-1/A\), which gives exactly that inequality. Thus the formula never selects a point on the wrong supervision branch.

The final policy compares \(V(s_c)\) with \(F\). Adopt coverage \(s_c\) if \(V(s_c)>F\), choose no service if it is smaller, and retain both at equality. Fixed setup does not change the preferred positive coverage, because it is the same cost at every positive scale.

For an interior capped optimum, put \(r=\sqrt{1-G/B}\). Substituting \(s_c=H(1/r-1)\) simplifies the peak value to
\[
V(s_c)=H\{B(1-r)^2-k\}.
\]
This gives an exact maximum affordable setup cost. In the manuscript's example \(B=4,k=1,G=3.5,H=1/4\), it reproduces its interior scale \(H(\sqrt8-1)\) and pre-setup value about \(0.1679\), leaving about \(0.1179\) after \(F=0.05\).

Checked locations: supervision theorem (2), uncapped value (3), capped derivative (4), and scale reversal. Full source/YAML were read. The solved coverage policy is conditional on the stated error technology, complete aggregate business accounting and fixed capacities. It does not rank real advisory modes or identify long-run effects. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-L26-546-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b2/prb_b2f223324a3f40f1a2928c42c5858ea9/contributions/con_54b48cd174e24c9583e91d50fa0ab038/files/L26-546.tex). Canonical revision: `rev_bcbfc7e8b08847648080bcb230bfcc8b`.

