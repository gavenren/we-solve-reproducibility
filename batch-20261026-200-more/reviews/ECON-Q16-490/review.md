# Exact cessation-time transforms and discounted adoption profits

The source determines eventual cessation probabilities and gives a finite-horizon survival recursion. Its reserve model also admits a closed-form cessation-time transform. This distinguishes the probability of failure from how long it takes, and evaluates discounted profits without iterating a long time grid.

Keep the independent seasonal increments, reserve-based continuation rule and fixed outside option. Write \(q=1-p\), \(X=m+1\ge1\), so the shifted reserve starts at \(X\) and cessation occurs on first hitting zero. Let \(\tau\) be that hitting time, taking value infinity on persistent paths. For \(0<z<1\), define \(z^\infty=0\). Then
\[
\mathbb E_X[z^\tau]=h(z)^X,\qquad
h(z)=\frac{1-\sqrt{1-4pqz^2}}{2pz}.
\]

To prove it, the transform \(f_x=\mathbb E_x[z^\tau]\) is bounded, has \(f_0=1\), and satisfies \(f_x=z(pf_{x+1}+qf_{x-1})\) for \(x\ge1\). The displayed \(h\) is the smaller root of \(h=z(ph^2+q)\), lies strictly between zero and one, and hence \(h^x\) is a bounded solution with the right boundary value. Uniqueness follows directly: on bounded sequences with zero boundary difference, the recurrence operator has sup-norm at most \(z<1\). Two solutions would have difference norm at most \(z\) times itself, forcing equality. Thus this is the actual first-passage transform.

Taking \(z\uparrow1\) recovers the source's ruin probability. If \(p>q\), \(h(1)=q/p\), giving \((q/p)^X\); if \(p\le q\), the limit is one. This independently checks its infinite-horizon probability result.

When \(p>q\), the *conditional* cessation-time law equals the hitting-time law of the walk with the step probabilities exchanged. Indeed a finite path first hitting zero has numbers of up and down steps satisfying \(d-u=X\). Its original probability divided by the exchanged probability is
\[
\frac{p^uq^d}{q^up^d}=(q/p)^X,
\]
independent of path length and shape. Summing over first-passage paths gives the conditional-law identity after dividing by the cessation probability. Therefore persistent positive average returns do not make failure paths short by definition; they select a downward-drifting path law.

The conditional mean is
\[
\mathbb E_X[\tau\mid\tau<\infty]=\frac{X}{p-q}\qquad(p>q).
\]
For a direct transform check, differentiating \(h=z(ph^2+q)\) at \(z=1\), where \(h=q/p\), gives \(h'(1)/h(1)=1/(p-q)\). The logarithmic derivative of \(h(z)^X/h(1)^X\) yields the stated mean. The positive drift permits this finite derivative; at the fair boundary the mean first-passage time is infinite.

Finally let \(\mu=d(2p-1)\) be mean incremental seasonal profit and use discount factor \(0<\zeta<1\). Independence of season-\(t\) profit from the prior survival event, exactly as in the source, gives
\[
\mathbb E\sum_{t\ge0}\zeta^t\Pi_t\mathbf1_{\{\tau>t\}}
=\frac{\mu}{1-\zeta}\{1-h(\zeta)^X\}.
\]
The pathwise identity \(\sum_{t\ge0}\zeta^t\mathbf1_{\{\tau>t\}}=(1-\zeta^\tau)/(1-\zeta)\) proves the last step. Absolute discounted profits are bounded by \(d/(1-\zeta)\), justifying expectation interchange. At \(p=1/2\), this discounted expected profit is zero despite eventual cessation being certain; an undiscounted terminal-loss argument cannot be interchanged with an infinite expected stopping time.

Checked locations: exact persistence theorem and finite-horizon profit recursion. Full source/YAML were read. The insurance and information models remain separate; no risk-averse optimal stopping rule, consumption welfare or empirical persistence estimate is claimed. External references are unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-Q16-490-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/40/prb_4015ed0b2de34537b67f2734d0dcedbf/contributions/con_fc56a725f48c449d882912ebbc766f1a/files/Q16-490.tex). Canonical revision: `rev_6b1fe972e27348a389356fe5e1a3aeff`.

