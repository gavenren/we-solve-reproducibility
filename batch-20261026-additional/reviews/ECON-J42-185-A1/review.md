# Independent observational-equivalence check and a known-output refinement

Finding: **Supports the claim**.

I reviewed the full [pinned J42-185 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/35/prb_3590da7499a24bcc9aab47d89c0b05b9/contributions/con_467f4442c296441db8e2628f7499d6f2/files/J42-185.tex), revision `rev_610a7900686f44f9b0735eb5b84efac0`, together with its exploration metadata. The result concerns a declared price-taking intervention in one labor market, with reservation costs and technology fixed within each compatible model. It does not claim that the basic monopsony first-order condition is new or that sorting and amenities have been empirically eliminated. My check supports the stated sharp bounds and gives a quantitative equivalence example plus a refinement when fixed-input output is observed.

The equilibrium expressions survive a direct marginal-expenditure calculation. At employment L the wage bill is w_0 L(L/L_0)^(1/e), whose derivative is (1+1/e)w(L). Calibration p_0=(1+1/e)w_0 makes marginal revenue equal marginal expenditure at L_0. Their ratio is strictly decreasing, so this is the global baseline optimum below the supply cap. At the competitive intersection, the relevant equation is instead p(L)=w(L). Dividing it by the baseline equality gives the manuscript's employment and wage ratios. This verifies why the competitive wage gain is the technological log wedge divided by 1+eh, rather than the wedge itself.

The finite population cap is important and is handled explicitly: it can be chosen above every competitive employment level on the compact parameter rectangle. The h=0 case is a labor-demand correspondence at wage p_0, and the declared market-clearing quantity belongs to that correspondence. Neither issue invalidates existence. Retention of the entire baseline set follows from the strictly higher competitive wage and the same individual reservation costs within each model.

Here is an explicit pair illustrating the wage-response ambiguity without changing any baseline observable in the specified law. Normalize w_0=L_0=1 and R_0=4. Model A has e=1, h=1/2 and K=0; model B has e=2, h=1/4 and K=2. In both cases the revenue formula gives exactly R_0=4, and the calibrated uniform wage-posting optimum is the same observed (w_0,L_0). A common population measure of three is sufficient for both competitive quantities. The local wage passthrough is

\[
\rho=\frac1{1+eh}=\frac23
\]

in both models. Nevertheless the fixed-worker competitive wage gains are respectively

\[
\frac23\log 2\approx0.462098,
\qquad \frac23\log(3/2)\approx0.270310.
\]

The employment elasticities are 2/3 and 4/3, so observing those responses distinguishes the models immediately. This verifies the identification claim with complete compatible technologies, nonnegative fixed output, and retained baseline workers, rather than merely displaying two values of an unobserved formula. It also makes clear which additional revenue responses have not been included in the observation scheme.

There is a useful exact refinement of the manuscript's remark about observing K. Suppose K is separately known and define the observed variable-output ratio

\[
a=\frac{R_0-K}{w_0L_0}.
\]

Any compatible model necessarily has a>1 and

\[
h(e)=1-\frac{1+1/e}{a}.
\]

Thus the compatible rectangle is cut down to an increasing continuous curve, not an arbitrary rectangle in e and h. Its feasible e-values form a closed interval, or the empty set, because h(e) is strictly increasing. On this curve the wage-gain formula simplifies to

\[
m(e,h(e))=
\frac{a\log(1+1/e)}{(a-1)(e+1)}.
\]

This expression is strictly decreasing in positive e: its positive numerator decreases and its positive denominator increases. Accordingly, if the feasible elasticity interval is [e_-,e_+], its sharp gain interval is [m(e_+,h(e_+)),m(e_-,h(e_-))]. Every point is attained by the same primitive construction, now with the observed K held fixed. This additional observation need not point identify the target, but it changes the sharp bounds in an exactly calculable way. In the numerical pair above it excludes treating models A and B as observationally equivalent once their different K-values are revealed.

The original corner bounds are valid because the manuscript expressly leaves K and marginal products unobserved and supplies a sufficiently large common R_0. Enlarging the actual observable law would require recomputing compatibility; it would not expose an error in those bounds. I found no internal gap in the declared equilibrium, rectangle sharpness, or joint wage-and-employment response inversion. The independent refinement identifies a concrete route for tightening the partial-identification result without mistaking a baseline productivity wedge for the specified competition intervention.
