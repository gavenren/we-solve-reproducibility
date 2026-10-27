# Three withdrawal observations identify decay and permanent capacity formation

The source separates transient assets from permanent institutional formation after complete withdrawal. Its scalar recurrence also permits exact identification of those components from a short trajectory, while two observations give sharp asymptotic bounds under a decay restriction.

Start at complete withdrawal and write \(x_j=\Delta K_{t_0+j}\). Maintain invariant \(0<\rho<1\), known \(D=d+1/\kappa>0\), and nonnegative permanent increment \(h\). Then the source gives
\[
x_{j+1}=\rho x_j+c,\qquad c=h/D\ge0.
\]
For three consecutive exact observations \(x_0,x_1,x_2\), if \(x_1\ne x_0\),
\[
\rho=\frac{x_2-x_1}{x_1-x_0},\qquad
c=x_1-\rho x_0,\qquad h=Dc.
\]
Subtracting consecutive recurrence equations proves necessity; substituting the recovered parameters reproduces both transitions and supplies the unique compatible recurrence. Compatibility requires \(0<\rho<1\) and \(c\ge0\). The limiting capacity difference is then uniquely \(c/(1-\rho)\).

These conditions imply nonzero consecutive changes have the same sign and shrink geometrically. An observed reversal or acceleration rejects this exact scalar invariant model, unless measurement error or additional regime differences are supplied. With more dates, every ratio of consecutive nonzero changes must equal the same \(\rho\), providing additional checks.

If \(x_1=x_0\), compatibility requires \(x_2=x_0\) as well. A flat trajectory at \(x_0\ge0\) is compatible with every \(\rho\in(0,1)\), setting \(c=(1-\rho)x_0\). Decay and the institutional flow remain confounded, but the limiting capacity effect is exactly the observed level \(x_0\). A negative flat level is incompatible with nonnegative \(c\). At level zero the permanent flow is zero for every allowed decay. Thus failure to identify the decay parameter does not always imply failure to identify the limiting effect.

Now suppose only \(x_0,x_H\) are observed, with integer \(H\ge1\), and external evidence gives \(\rho\in[\rho_L,\rho_U]\subset(0,1)\). The compatible set additionally requires
\[
x_H-\rho^H x_0\ge0,
\]
and the limiting effect at each compatible decay is
\[
L(\rho)=\frac{x_H-\rho^Hx_0}{1-\rho^H}.
\]
Indeed the source trajectory gives \(x_H=\rho^Hx_0+c(1-\rho^H)/(1-\rho)\); solving gives the formula and the nonnegative-flow restriction. Conversely it constructs \(c=(1-\rho)L(\rho)\ge0\), reproducing the observations, proving sharpness.

The feasible decay set is a closed interval or empty, because the extra inequality is monotone in \(\rho^H\) (or constant when \(x_0=0\)). On it,
\[
\frac{dL}{d(\rho^H)}=\frac{x_H-x_0}{(1-\rho^H)^2}.
\]
Therefore the sharp limiting-effect interval is obtained by evaluating \(L\) at the two feasible decay endpoints and sorting the values. Continuity fills every intermediate effect. An increasing observed capacity gap makes the asymptote increase with allowed persistence; a declining gap reverses that order.

For example \(x_0=0,x_H=1,H=1\), and \(\rho\in[1/4,3/4]\) imply a sharp limiting-effect interval \([4/3,4]\). A positive finite follow-up alone does not determine its magnitude, even after all support has ended.

Checked locations: crowd-out rule (3), complete-withdrawal trajectory (4), and grant-withdrawal nonidentification proposition. Full manuscript/YAML were read. The identification requires complete withdrawal and exact invariant trajectories; continuing facilitation, unknown conversion costs, endogenous local behavior or noise require further restrictions. Income effects scale by the source's known \(\omega\); household welfare is separate. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-F35-575-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/89/prb_89164c51972d417c94b6f7c6d21608e7/contributions/con_ed350b7171574e38bbe97401588aa643/files/F35-575.tex). Canonical revision: `rev_ee823ff56d7040d297a28df47482bcd8`.

