# Sharp taste-belief regions under imperfect revelation

The source's information-factorial inversion requires equal beliefs after quality revelation and a stable taste cost. Relaxing both assumptions in bounded form yields an exact joint identified set. The resulting uncertainty cannot be inferred from the raw callback contrast without retaining the common index normalization.

Keep interior callback probabilities and the source's known strictly increasing noise distribution \(F\). Let
\[
d_b=F^{-1}(p_{1b})-F^{-1}(p_{0b}),\qquad
d_b=\delta_b-\tau_b,\quad b=0,1.
\]
Here \(\delta_b\) is the cue difference in believed productive value, and \(\tau_b\) is the taste cost in regime \(b\). Replace perfect revelation and taste stability by supplied bounds
\[
|\delta_1|\le\epsilon,\qquad
|\tau_1-\tau_0|\le s,\qquad \epsilon,s\ge0.
\tag{A}
\]
These are restrictions on economic mechanisms in the index units, not estimated facts.

The sharp joint region for the ordinary-regime mechanisms is
\[
\tau_0\in[-d_1-\epsilon-s,\,-d_1+\epsilon+s],
\qquad
\delta_0=d_0+\tau_0.
\tag{B}
\]
Thus the two components lie on a line segment, not in the Cartesian product of their marginal intervals. If the maintained model also requires \(\tau_0\ge0\), intersect the segment with that halfspace. Additional known belief or taste bounds are intersected in the same way; an empty intersection rejects the combined restrictions.

To prove necessity, write \(e=\tau_1-\tau_0\). The informed-regime equation gives
\[
\tau_0=\delta_1-d_1-e.
\]
The difference of independently bounded scalars \(\delta_1\in[-\epsilon,\epsilon]\) and \(e\in[-s,s]\) fills exactly \([-\epsilon-s,\epsilon+s]\), proving the interval. The ordinary equation gives its joint line restriction.

For sufficiency, take any \(\tau_0\) in that interval. Choose \(\delta_1,e\) within their bounds with \(\delta_1-e=\tau_0+d_1\), and set \(\tau_1=\tau_0+e\). Then \(\delta_1-\tau_1=d_1\). Put \(\delta_0=d_0+\tau_0\). For either regime choose the cue-zero belief level as
\[
\mu_{0b}=k+F^{-1}(p_{0b}),
\]
and cue-one level \(\mu_{1b}=\mu_{0b}+\delta_b\). The cue-one index becomes \(F^{-1}(p_{1b})\), so all four observed binary callback distributions are reproduced exactly. No restrictions on belief levels beyond (A) were imposed. This proves sharpness rather than only a triangle-inequality outer bound.

For an illustrative index configuration \(d_0=-0.4,d_1=-0.1\), take \(\epsilon=0.03\), \(s=0.02\). Equation (B) yields
\[
\tau_0\in[0.05,0.15],\qquad
\delta_0\in[-0.35,-0.25].
\]
Both a positive ordinary taste cost and a negative belief difference are robustly present in this model. With \(\epsilon+s\ge0.1\), a zero taste cost becomes compatible with the same callbacks. The data have not changed; the maintained information and stability restrictions have.

At \(\epsilon=s=0\), (B) recovers exactly the manuscript's inversion \(\tau=-d_1,\delta_0=d_0-d_1\). The two uncertainty sources enter additively, but their interpretations remain distinct: imperfect information leaves a belief gap, while regime drift changes preferences.

This is a structural sensitivity region, not an empirical allocation of discriminatory mechanisms. It retains the common threshold and known noise scale, excludes recruitment networks, and does not convert callback evidence into a career earnings effect. Unknown regime-specific noise scales or selective quality validation require a different model.

Source: [ECON-J71-531-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f4/prb_f4197ad3648d460d87daccd506b5685a/contributions/con_b85d069fb7804ae28725bf86425d3c26/files/J71-531.tex), canonical revision `rev_b24f0722bcc2466d97caef4c764d4ba0`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
