# Observing a shared transmission bottleneck changes the sparse cascade detection boundary

Claim: **Partial result**. The result treats a specified fork network with one observed shared bottleneck, known background infection probability, and at most one active terminal transmission. It establishes matching separation orders in a nonempty rare-cascade regime. It does not characterize arbitrary networks.

## Experiment and exact scope

Let a source-to-hub path of length L−1 contain one edge of transmission probability q∈(0,1]; all other path edges transmit surely. For L=2 this is a single source-to-hub edge. Attach J≥2 terminal leaves to the hub, so their distance from the source is L. Take K≥L, no background seeds on the path, and independent background seeds at each leaf with known probability b∈(0,1), bounded away from zero and one. The source assignment W is a fair independent coin. Write A for the observed infection indicator of the hub. Then A=W B with B∼Bernoulli(q). All of W, A and the J leaf outcomes are observed in m independent outbreaks.

Under the null all terminal edges have probability zero. Under alternative j, only terminal edge j transmits, with probability p. Put t=(1−b)p and δ=qt. The treatment effect at leaf j is δ and all other effects vanish. Conditional on A=1, its infection probability is b+t; conditional on A=0 it is b. The probability that treatment changes any distant outcome is exactly δ, so this alternative lies in the prompt's rare class if δ≤ρ. These statements use the shared counterfactual seeds and edge draws stipulated in the prompt.

For fixed error probabilities α,β with α+β<1, and q allowed to depend on m, the separation order is

\[
\delta_{\mathrm{obs}}\asymp \sqrt{q\log J/m},
\]

provided mq is at least a sufficiently large constant times log J and the proposed separation is at most both ρ and q(1−b). Constants can depend on b, α and β. The phrase “separation order” concerns this specified one-active-leaf class; it is not an assertion about the unrestricted cascade class.

## An adaptive-to-q finite-sample test

Let M=ΣA_i. When M=0 do not reject. Otherwise let \bar Y_{j,A} be the mean of leaf j over outbreaks with A=1 and reject if

\[
\max_j(\bar Y_{j,A}-b)>
\sqrt{\log(J/\alpha)/(2M)}.
\]

The test does not use q. Conditional on the complete A sequence, under the null each included leaf observation is Bernoulli(b). The exponential bound for a mean of independent [0,1] variables and a union bound give conditional, hence unconditional, size at most α.

Since M∼Binomial(m,q/2), the elementary multiplicative binomial bound gives

\[
\Pr\{M<mq/4\}\le e^{-mq/16}.
\]

One can derive this bound directly from E exp(−sM)=(1−q/2+(q/2)e^{−s})^m and optimize in s; the weaker displayed constant suffices. On M≥mq/4, the active leaf's missed-detection probability is at most β/2 if

\[
\delta\ge
\sqrt{2q/m}\{
\sqrt{\log(J/\alpha)}+\sqrt{\log(2/\beta)}\}.
\]

Indeed divide by q to obtain a lower bound for t, use M≥mq/4 in the threshold, and apply the lower-tail exponential bound to the active leaf. If mq≥16 log(2/β), the bad-count event has probability at most β/2. This proves total type-II error at most β. Correlation among the leaves caused by the bottleneck has disappeared after conditioning on the observed gate.

## Matching lower bound retaining every observed vertex

Let P0 be the null with the same q and b. Let Lj be the likelihood ratio of alternative j with respect to P0 over all m outbreaks, including the upstream observations. For a single outbreak the likelihood ratio is one when A=0. When A=1 it is the Bernoulli(b+t)-to-Bernoulli(b) ratio of leaf j. Consequently

\[
E_0 L_j^2=\left(1+\frac{q t^2}{2b(1-b)}\right)^m
=\left(1+\frac{\delta^2}{2q b(1-b)}\right)^m,
\qquad E_0L_jL_k=1\quad(j\ne k).
\]

The cross identity follows by conditional independence of distinct leaf outcomes given (W,A), with conditional likelihood-ratio means one. Thus the uniform mixture over J alternatives has

\[
\chi^2(\bar P,P_0)=
\frac{(1+\delta^2/[2q b(1-b)])^m-1}{J}.
\]

For δ²=cq log J/m, this is at most (J^{c/[2b(1−b)]}−1)/J. A sufficiently small positive c makes one half of its square root less than 1−α−β, uniformly for J≥2. The total variation inequality follows from Cauchy–Schwarz applied to the likelihood ratio. A level-α test with power at least 1−β at every alternative would have the same power against the mixture and would contradict that total variation bound. This proves the lower separation order. All preceding path infections are functions of (W,A) together with parameter-free observations and do not invalidate the likelihood calculation.

The required alternatives exist only when the chosen δ satisfies δ≤q(1−b) and δ≤ρ. In particular mq≳log J is a substantive feasibility condition, not a disposable technicality. If the rare class is smaller, the claim is not that an empty alternative can be detected.

## Why observing the gate matters

For comparison, change the observation scheme by hiding A and all upstream outcomes other than W. In this reduced experiment, conditional on W=1 the single affected leaf has probability b+δ, and all other leaves are independent Bernoulli(b); under W=0 all are Bernoulli(b). Since only one terminal edge can be active, the latent shared gate creates no dependence with the other leaves. The same mixture calculation now gives

\[
\chi^2(\bar P_{\rm hidden},P_{0,\rm hidden})=
\frac{(1+\delta^2/[2b(1-b)])^m-1}{J}.
\]

The usual arm-contrast test provides the matching upper order √(log J/m). Thus visible upstream activation improves the sparse-effect separation by √q in the overlap of the two nonempty parameter regimes. This comparison is explicitly a change in observed data, not a contradiction of the prompt's full observation experiment.

## Relation to the earlier attempt and limitations

The earlier Econ-218-A1 manuscript establishes noiseless and noisy path boundaries and a deterministic-hub fork lower bound. The present argument credits that likelihood-mixture method and extends it to an observed random common gate, deriving the q-dependent boundary, a test not requiring q, and a visible-versus-hidden information comparison. Unknown b, several simultaneously active leaves, multiple bottlenecks, and arbitrary geometry remain untreated. No historical novelty, human peer review or formal proof certification is asserted.

The supplementary exact checker enumerates the small finite experiments and checks both chi-square identities. Its finite checks support the calculation; the universal statement rests on the proof above.

## Checked references

- We Solve, ECON-C31-214 current research prompt, read 26 October 2026: https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C31-214.txt (used: exact cascade model and target).
- We Solve, Econ-218-A1, revision r1: https://we-solve.github.io/contributions/detection-limits-for-rare-long-range-causal-cascades/attempt-1/r1/ (used: existing path/fork results and the likelihood-mixture method; extension distinguished above).
