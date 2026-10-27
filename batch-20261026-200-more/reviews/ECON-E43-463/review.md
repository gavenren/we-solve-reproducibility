# World integration yields a debt-weighted harmonic natural rate and exact creditor thresholds

The source's integrated-world equation has an exact aggregation interpretation. The world rate is a debt-weighted harmonic mean of country autarky rates, and a country's creditor status is determined by its autarky rate relative to that world rate. Its own population share affects the magnitude, but not the sign, of the position.

Retain the stationary integrated model's common cohort growth factor \(g>0\), country middle-aged masses \(N_j>0\), and binding borrowing-limit restrictions. Put
\[
\kappa_j=\beta_j/(1+\beta_j),\quad
s_j=\kappa_j(Y_j-D_j),\quad R_j=gD_j/s_j.
\]
Here \(R_j\) is the unique natural rate the same country would have in autarky. Define debt weights \(\omega_j=N_jD_j/\sum_\ell N_\ell D_\ell\). All are positive and sum to one. The source's equation (8) becomes
\[
\frac1{R_W}=\sum_j\frac{\omega_j}{R_j}.
\]
Thus \(\min_jR_j\le R_W\le\max_jR_j\), strictly between the extremes unless all rates coincide. This follows directly from a positive weighted average of their reciprocals, and requires no approximation.

The national new-claim position can be rewritten as
\[
F_j=N_js_j\left(1-\frac{R_j}{R_W}\right).
\]
Accordingly a country lends net in newly issued claims precisely when its autarky natural rate is below the world rate, borrows when above, and has zero position at equality. This is a precise equilibrium connection between the local saving–borrowing balance and international positions. It does not turn those positions into current accounts, whose maturing claims the source correctly requires separately.

There is a sharper threshold when one country's borrowing limit varies. Fix all foreign primitives and write
\[
P_{-i}=\sum_{j\ne i}N_jD_j>0,\qquad
S_{-i}=\sum_{j\ne i}N_js_j>0.
\]
For country \(i\), write \(D=D_i\), \(Y=Y_i\), and \(\kappa=\kappa_i\). Substitution and cancellation give
\[
F_i(D)=
\frac{N_i[\kappa(Y-D)P_{-i}-DS_{-i}]}
{P_{-i}+N_iD}.
\]
Every denominator is positive. Hence the exact zero-position threshold is
\[
D_i^\circ=\frac{\kappa YP_{-i}}{S_{-i}+\kappa P_{-i}}.
\]
It is a creditor for admissible \(D<D_i^\circ\), a debtor for \(D>D_i^\circ\), and balanced at equality. The threshold does not involve \(N_i\). If it lies outside the maintained binding-limit interval, only the corresponding one-sided status is attainable within this model; the formula does not authorize moving beyond that restriction.

Credit relaxation also has an unambiguous spillover direction. The world rate as a function of \(D\) is
\[
R_W(D)=\frac{g(P_{-i}+N_iD)}
{S_{-i}+N_i\kappa(Y-D)}.
\]
Its derivative is
\[
R_W'(D)=
\frac{gN_i[S_{-i}+N_i\kappa Y+\kappa P_{-i}]}
{[S_{-i}+N_i\kappa(Y-D)]^2}>0.
\]
For every foreign country \(j\), fixed saving and borrowing primitives give \(F_j'(D)=gN_jD_jR_W'(D)/R_W(D)^2>0\). World adding-up then forces \(F_i'(D)=-\sum_{j\ne i}F_j'(D)<0\). Relaxing one country's credit limit raises the world rate and reduces that country's net lending while increasing every foreign new-claim position.

Checked locations: stationary natural-rate theorem, equations (2), (3), and world aggregation (8). Full manuscript/YAML were read. These are comparative-equilibrium identities within the endowment specialization; productive capital, safety premia, nominal output shortfalls, and empirical causal interpretation remain outside scope. External references are unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-E43-463-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/47/prb_47c25d3f8cc84204ab846b499259f4eb/contributions/con_07efe4a761e540c390ce0efacc5612ea/files/E43-463.tex). Canonical revision: `rev_8545a01b6153495d8a44d7b40ad0486b`.

