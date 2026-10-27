# Eventual-selection bounds under heterogeneous commitment speed

The source's two-horizon inversion is exact for one geometric commitment hazard per equilibrium. If hazards vary across groups destined for the same equilibrium, the same observations generally identify only a lower bound on eventual selection. The complete identified interval can still be computed.

Keep the source's empirical-profile neighborhoods and off-diagonal precommitment path. Fix one equilibrium, let \(w\in[0,1]\) be its eventual group mass, and draw its commitment hazard \(\rho\in(0,1]\) from an arbitrary distribution. Conditional on that hazard, waiting time remains geometric as in the source. The remaining groups do not enter this equilibrium's neighborhood. Its probabilities at horizons four and eight are
\[
u=q(4)=wE[\rho],\qquad
v=q(8)=wE[2\rho-\rho^2].
\tag{A}
\]
Every positive hazard eventually commits almost surely, so \(w\) is indeed the eventual mass, even without a uniform positive lower hazard bound.

If \(u>0\) and \(u<v\), the data are compatible exactly when
\[
v\le2u-u^2,
\]
and the sharp identified interval is
\[
w\in\left[\frac{u^2}{2u-v},\,1\right].
\tag{B}
\]
For \(v=u>0\), instead \(w=u\) and the hazard equals one almost surely. If \(u=0\), positive hazards imply \(w=0\) and therefore \(v=0\). Values outside these cases reject the subclass.

For necessity in the nondegenerate case, (A) gives
\[
E[\rho]=u/w,\qquad E[\rho^2]=(2u-v)/w.
\]
Nonnegative variance implies \(u^2\le w(2u-v)\), yielding the lower bound in (B). Since \(w\le1\), it also implies the stated compatibility inequality. The strict inequality \(v<2u\) follows automatically from \(E[\rho^2]>0\). Moreover \(\rho^2\le\rho\) gives \(v\ge u\). Equality requires \(\rho\in\{0,1\}\) almost surely; positivity excludes zero, proving the separate \(v=u\) conclusion.

For sharpness, take any \(w\) in (B) and put \(m=u/w\), \(s=(2u-v)/w\). They satisfy \(0<m<1\), \(m^2\le s<m\). The two-point hazard distribution supported on
\[
\ell=\frac{m-s}{1-m}\in(0,m],\qquad 1
\]
has the required moments when the probability on one is
\[
\pi=\frac{m-\ell}{1-\ell}.
\]
Indeed \(E\rho=m\), and \(E\rho^2=m(1+\ell)-\ell=s\). At \(s=m^2\), \(\ell=m,\pi=0\), giving a constant hazard. All hazards are strictly positive and at most one. Give mass \(w\) this timing law and let the remainder stay off diagonal forever. The construction reproduces both observations and attains every eventual mass in (B).

For \(u=0.2,v=0.3\), the exact interval is \(w\in[0.4,1]\). The source's homogeneous inversion gives hazard \(0.5\) and mass \(0.4\), the lower endpoint. The same finite-horizon data also fit eventual mass one: choose hazard \(1/8\) with probability \(32/35\) and hazard one with probability \(3/35\). These give \(E\rho=1/5\) and \(E\rho^2=1/10\), hence exactly the observed probabilities.

Other equilibria can impose a further common mass constraint; (B) treats this one equilibrium with all remaining groups permitted to remain unclassified. Allowing zero hazards would change the interpretation of a “destined” mass and the equality boundary.

The source makes its homogeneous-hazard restriction explicit, so this is a partial-identification extension, not an error claim. It does not identify unknown learning rules, validate belief-report kernels or establish portability across games.

Source: [ECON-C73-564-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/c7/prb_c7087fcc13aa4d88b2100a4120e73bcb/contributions/con_a9bb069109bd41ddb1250291a5d897ff/files/C73-564.tex), canonical revision `rev_39c55f4841f24b12ba40f3659d3eec8a`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
