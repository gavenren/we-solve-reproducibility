# Exact surplus incidence of safety improvements with general labor supply

The source's uniform-outside-option model shows that employers can absorb part or all of a commuting-safety benefit through wages. The incidence can be characterized for general differentiable labor supply, and the aggregate welfare gain has a simple exact envelope formula. This retains a genuine safety-cost reduction rather than treating a fare transfer as a resource saving.

Let a unit population have outside opportunity costs θ with cumulative distribution F and positive density f over the relevant interior range. Each accepted job carries the same real money-equivalent expected safety burden c. At wage w, labor supply is N=F(w−c). Let labor demand D(w) be differentiable with D'(w)≤0, arising from a concave production-benefit function. Assume finite worker rent and employer surplus throughout the compared path, for example bounded outside costs and finite production surplus. Assume a locally unique interior equilibrium and no rationing, entry, fiscal transfers or household bargaining. Denote z=w−c and f=f(z)>0.

Differentiating F(w−c)=D(w) gives

dw/dc=f/(f−D'),
dN/dc=D'f/(f−D')≤0.

Thus a marginal reduction in safety burden by ε raises employment by [−D'f/(f−D')]ε and lowers wages by [f/(f−D')]ε. The wage reduction captures a fraction between zero and one of the direct per-job benefit. With strictly downward demand the employment response is positive. When demand is locally fixed, D'=0, wages fall one for one and employment is unchanged, recovering the source's limiting example.

To calculate distributional incidence for the whole baseline population, aggregate worker rent is

WS(c)=∫(z−θ)_+dF(θ).

Its derivative with respect to z is F(z)=N; this follows by differentiating the positive-part expression or its integral representation. Employer surplus PS satisfies dPS/dw=−D(w)=−N, since each extra wage dollar is paid on every demanded job. Therefore the marginal surplus gains from a reduction in c are

dWS/dε=N[−D'/(f−D')],
dPS/dε=N[f/(f−D')].

Both are nonnegative and they sum exactly to N. The expressions include workers entering employment as z rises and compare the same full population. They do not condition welfare on remaining employed.

For a finite safety improvement from c_0 to c_1<c_0 along an interior equilibrium path, integration gives the exact combined surplus gain

[WS+PS](c_1)−[WS+PS](c_0)
=∫_{c_1}^{c_0}N(c)dc.

Wages cancel as transfers between workers and employers. The residual is the avoided real expected burden on equilibrium employment, including the employment adjustment. Since N(c) is nonincreasing in c, this gain lies between N(c_0)(c_0−c_1) and N(c_1)(c_0−c_1). It equals the lower expression when employment stays fixed throughout, including the source's fixed-capacity case.

The source's uniform supply has f=1 and D'=-b, yielding worker share b/(1+b), employer share 1/(1+b), and its exact wage and employment derivatives. The general formulas show that those shares are elastic-response objects, not universal fractions of a safety program's value.

The welfare identity requires the reduction in c to be a genuine reduction in expected harm or another real burden. If it is only a lower fare, the operator's lost receipts and resource costs must be added before calling the same expression a social gain. Program expenditure also must be subtracted once on the declared boundary. Distributional welfare weights can change the ranking even when combined surplus rises.

This extension solves incidence within a competitive one-market subclass. It does not identify actual harm valuations, endogenous job locations, firm entry, transport congestion or household constraints, and it does not justify interpreting a small employment effect as a small welfare benefit.

Source: [ECON-J22-544-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/06/prb_06c2e4437abb433e83793b253ca9121f/contributions/con_35242630af5d4cbb81a37f41d1527660/files/J22-544.tex), canonical revision rev_954bdef8beaa42ba8055b23ea8bf9d1f. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
