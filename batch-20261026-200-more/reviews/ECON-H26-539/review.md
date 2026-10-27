# Closed-form mediation bounds using all binary cells

The source's response-type linear program is valid and sharp. Under its two optional monotonicities, the full observed binary experiment admits a simple closed-form solution. It is generally tighter than the marginal-response bound when no separate controlled-belief experiment is available.

Assume
\[
B(1)\ge B(0),\qquad C(0,1)\ge C(0,0),
\]
with randomized message assignment and otherwise unrestricted binary response types. Let the observed cells be \(q_z(b,c)\), and set
\[
u=\Pr(B=1\mid Z=1)-\Pr(B=1\mid Z=0),\qquad
r=q_0(0,0).
\]
Provided the data satisfy \(u\ge0\), the exact sharp interval for the source's natural mediated effect is
\[
0\le\tau_B\le\min(u,r).
\tag{A}
\]
No exclusion \(C(z,b)=C(b)\) is imposed. If \(u<0\), monotone beliefs are incompatible with the data.

For necessity, monotonicity partitions the population into always-high, belief-complier and never-high types, with masses
\[
a=\Pr(B=1\mid Z=0),\quad
u,\quad n=\Pr(B=0\mid Z=1).
\]
They sum to one. Natural mediation is positive only for belief compliers whose baseline compliance response changes from zero to one. This event is contained both in the complier group of mass \(u\) and in the observed baseline event \(B(0)=0,C(0,B(0))=0\) of mass \(r\). It has no negative contributions under the two monotonicities. This proves (A).

Here is a construction establishing that every value \(x\in[0,\min(u,r)]\) is attainable while preserving all observed cells. Let \(s=q_0(0,1)\), so \(r+s=n+u\). Choose a mass \(z\) of compliers with baseline compliance zero satisfying
\[
\max(x,u-s,0)\le z\le\min(u,r).
\]
Such a choice exists: \(u-s\le r\) follows from \(r+s=n+u\), and \(u-s\le u\). Allocate \(z\) compliers to baseline zero and \(u-z\) to baseline one. The remaining baseline cells are filled by never-high types, giving their required total mass \(n\).

Among the \(z\) baseline-zero compliers, assign exactly mass \(x\) the response \(C(0,1)=1\), and the remainder zero. For baseline-one compliers, monotone compliance forces \(C(0,1)=1\). Thus the mediated effect is exactly \(x\). For never-high types, set the unobserved \(C(0,1)\) no lower than their baseline response. For always-high types, reproduce the observed baseline \(C(0,1)\) cells and choose unobserved \(C(0,0)=0\). All baseline response restrictions now hold.

Treatment compliance \(C(1,b)\) is unrestricted by these monotonicities. Within the never-high group choose it to reproduce \(q_1(0,c)\). Across the combined always-high and complier group choose it to reproduce \(q_1(1,c)\). Their masses match exactly, and arbitrary correlation with the baseline assignments is permitted. This preserves the complete observed experimental distribution. Fractional masses are valid response-type population probabilities, so the construction also attains both endpoints.

For example, if the message raises high-fairness belief prevalence by \(u=0.4\), but only \(r=0.1\) of the baseline arm jointly have low belief and noncompliance, natural mediation cannot exceed \(0.1\). The remaining belief response cannot generate positive baseline compliance changes for people already compliant. A zero mediated effect still fits, because all message compliance effects may operate through other paths.

The interval is sharp for this complete-cell information class. A separate belief experiment, message exclusion, measurement restrictions or monotonicity of message effects can tighten it further and should be retained jointly. The report does not validate the two monotonicities, treat reported beliefs as error-free in practice, or identify the empirical fairness mechanism.

Source: [ECON-H26-539-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f0/prb_f07bd31f221c45ffbb1d32af9ccdb929/contributions/con_434f8d007d3b41c69138a40e17452ad5/files/H26-539.tex), canonical revision `rev_6a9f8c49f2034662a18c7914247e8060`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
