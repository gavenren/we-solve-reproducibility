# Monotone reporting yields sharp joint bounds and a sign certificate

The source's marginal extortion bounds are sharp without cross-regime restrictions. If enforcement can only increase reporting, the two regimes must instead be optimized jointly. This can certify a reduction in actual victimization from falling reports even when the reporting levels remain unknown.

Let observed report incidences be \(r_0,r_1>0\), actual incidences \(E_z=r_z/q_z\), and externally supplied reporting intervals \([\underline q_z,\overline q_z]\subset(0,1]\). Impose the additional restriction \(q_1\ge q_0\). Feasibility of \(E_z\le1\) gives the effective lower bounds
\[
a_z=\max(\underline q_z,r_z),\qquad b_z=\overline q_z.
\]
Assume the joint feasible set is nonempty: \(a_0\le b_0\), \(a_1\le b_1\), and \(a_0\le b_1\). The treatment effect is
\[
\Delta E=r_1/q_1-r_0/q_0.
\]

Its sharp lower endpoint is
\[
L=r_1/b_1-r_0/a_0.
\]
For fixed positive reports, the effect decreases when \(q_1\) rises and increases when \(q_0\) rises. Thus \(q_1=b_1,q_0=a_0\) minimizes it, and the joint feasibility conditions ensure this pair is allowed.

For the upper endpoint, set \(B=\min(b_0,b_1)\). Conditional on \(q_0=x\in[a_0,B]\), the maximizing choice is \(q_1=\max(a_1,x)\). Therefore
\[
U=\max_{x\in[a_0,B]}
\left\{\frac{r_1}{\max(a_1,x)}-\frac{r_0}{x}\right\}.
\]
This is an explicit finite-candidate calculation: evaluate the displayed function at \(a_0\), \(B\), and at \(a_1\) if it belongs to the interval. For \(x\le a_1\), it is \(r_1/a_1-r_0/x\), which increases with \(x\). For \(x\ge a_1\), it is \((r_1-r_0)/x\), which is monotone or constant. No other maximizer can be required.

Every extremizing pair defines admissible incidences \(E_z=r_z/q_z\) and reproduces the report rates exactly. The feasible reporting region is compact and convex, hence connected; the continuous effect map has an interval as its image. Thus \([L,U]\) is the full sharp identified interval, including every intermediate effect, rather than merely attainable endpoints.

A useful sign implication needs no numerical optimization. If \(r_1<r_0\), monotone reporting gives
\[
E_1=\frac{r_1}{q_1}\le\frac{r_1}{q_0}<\frac{r_0}{q_0}=E_0.
\]
Hence falling reports strictly certify falling actual incidence within this restriction. Rising reports do not certify rising incidence: the reporting change can outweigh a true decline, as the source's first example already illustrates.

Under the stronger common-reporting restriction \(q_1=q_0=q\), the feasible interval is \(q\in[\max(a_0,a_1),\min(b_0,b_1)]\), if nonempty, and the exact effect is \((r_1-r_0)/q\). Its sharp endpoints are the two endpoint values sorted into increasing order. In particular the sign is identified for either direction of the report change, although magnitude generally is not.

Strictly positive reports avoid division degeneracies in this derivation. With zero reports and positive reporting lower bounds, actual incidence is zero in that regime and the remaining one-dimensional bounds apply directly. Neither monotone nor constant reporting is supplied by random assignment; each is a substantive validation assumption requiring evidence.

Checked locations: hidden-extortion reporting section and equation (4), with the full source/YAML read. The activity-choice and spatial-assignment results are not extended. Actual reporting restrictions, latent payments, resident welfare and external bibliography remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-K42-426-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/63/prb_63ef76dc456e497980be4e23f50ea328/contributions/con_d661ee40c2014759bec8a9d9fad04dd0/files/K42-426.tex). Canonical revision: `rev_963b12c7ebd44cb1b81c61f86350ef48`.

