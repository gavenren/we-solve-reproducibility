# Predictive coefficients for arbitrarily many noisy ancestors

The manuscript shows that measurement error creates a positive grandparent coefficient under a latent Gaussian first-order process. The mechanism extends to arbitrarily many ancestors. Its full regression coefficients have a simple recursion, which distinguishes distant predictive information from a direct multigenerational causal mechanism.

Retain Y_{j+1}=ρY_j+ξ_{j+1}, Var(Y_j)=1, independent Gaussian innovations of variance 1−ρ², and X_j=Y_j+ε_j with independent Gaussian errors of variance v>0. Observe X_0,…,X_m and predict X_{m+1}. Let P_j be the conditional variance of Y_j before observing X_j, and K_j=P_j/(P_j+v). Start P_0=1. Gaussian conditioning gives posterior mean and variance

hat Y_j=ρhat Y_{j−1}+K_j(X_j−ρhat Y_{j−1}),
R_j=P_jv/(P_j+v),

with hat Y_0=K_0X_0, and the next prediction variance is P_{j+1}=ρ²R_j+1−ρ². These follow directly by conditioning a normal variable with variance P_j on an independent noisy observation; they do not assume that annual records are valid independent lifetime-status indicators.

The conditional expectation of the child proxy is ρhat Y_m because its measurement error and new innovation have mean zero and are independent of the history. Expanding the recursion yields the population regression coefficient on X_{m−h}, for h=0,…,m,

b_{m,h}=ρK_{m−h}∏_{k=m−h+1}^{m}[ρ(1−K_k)].

An empty product equals one. Since P_j>0 and v>0, every gain K_j lies strictly between zero and one. Thus if ρ>0 every ancestral coefficient is strictly positive, however many intermediate noisy generations are controlled. If ρ<0 their signs alternate with generational distance. If ρ=0 they all vanish. Gaussianity ensures these conditional expectations are exactly the joint least-squares regression, not merely a chosen linear approximation.

For m=1, K_0=1/(1+v) and P_1=(1+v−ρ²)/(1+v). Substitution into the h=1 coefficient gives ρ²v/[(1+v)²−ρ²], precisely the source's grandparent coefficient. This supplies a consistency check on the full recursion and identifies its finite-history starting condition.

There is also a stationary infinite-history form. The variance update is T(P)=ρ²Pv/(P+v)+1−ρ². Its derivative is ρ²v²/(P+v)²≤ρ²<1 for P≥0, so repeated updates converge to a unique positive fixed point P satisfying

P²+(1−ρ²)(v−1)P−(1−ρ²)v=0.

Let K=P/(P+v). The stationary predictor is

E[X_{m+1}|…,X_{m−1},X_m]
=ρK∑_{h≥0}[ρ(1−K)]^h X_{m−h}.

The series converges in mean square: the coefficients are absolutely summable and the proxy second moments are uniformly bounded. Iterating the stable posterior-mean recursion and sending its initial date to the remote past proves the formula. Its ancestral coefficient ratio is ρ(1−K), whose absolute value is strictly below |ρ|. Latent status itself remains first order throughout.

This gives a concrete null benchmark for a long ancestry regression. Persistent predictive coefficients beyond grandparents need not refute first-order latent transmission when intervening statuses are measured with error. Conversely the formula is restrictive and can be tested only after defending stationarity, Gaussianity, representative linkage and independent measurement errors.

No causal transfer effect is identified by these coefficients. Correlated proxy errors, multiple ancestral lines, selective linkage and nonlinear latent dependence remain outside this calculation, in accord with the source's limitations. No external result or novelty claim is required for the derivation.

Source: [ECON-J62-441-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/09/prb_09249cd3b69f43cabeb61b434e46dec1/contributions/con_075a254c67ee4477a1c13bdc82f23437/files/J62-441.tex), canonical revision rev_cc1c9bcd0a774b8fae0ae216ff728e05. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
