# Sharp product sensitivity and the exact mediation set in the binary example

Finding: **Supports the claim**.

I reviewed the full [pinned D72-197 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/50/prb_501ef2e2a8bd49a8b1382faba5e515d3/contributions/con_d144960ab09a454a8e1f7f8e037d34ad/files/D72-197.tex), revision `rev_536fca4211534d7a901d6ec5fcb57520`, and its metadata. It is explicitly an unresolved exploration. The maintained sequential-exchangeability and controlled-transition assumptions are substantive assumptions, not asserted properties of historical regime changes. I support the finite-state recursion and mediation obstruction and provide two exact strengthenings: a sharper accumulated-sensitivity bound and the sharp mediation interval for the manuscript's example.

The survival recursion uses the appropriate substochastic transition. Its missing mass records a failure of uninterrupted democratic survival, even if democracy later returns. Under the stated consistency, exchangeability, positivity, and common controlled Markov law, multiplying the selected live-state kernels and summing terminal mass identifies exactly that outcome. It does not identify the effect of an intervention that directly assigns democratic status. The manuscript correctly keeps those interventions separate and requires a different full-state recursion to identify terminal outcomes after democratic failure.

The stated total-variation sum bound is valid, but the same assumptions permit a strictly sharper bound. Complete each live transition by the common absorbing failure state and retain the common baseline distribution and reform rule. If the completed-row distance at time t is at most ε_t, then

\[
|s(p)-\widetilde s(p)|
\le 1-\prod_{t=0}^{T-1}(1-\varepsilon_t).
\]

To prove this, couple the baseline states identically. Whenever the coupled trajectories agree at time t, their next-state laws can be maximally coupled to agree with probability at least 1−ε_t. If they agree in failure, they remain equal because failure is absorbing. Induction therefore couples the entire trajectories to agree through the horizon with probability at least the product displayed. Their terminal survival indicators can differ only if the coupling has separated. The desired probability difference is bounded by that event's probability. This argument uses the common rule: equal current states must select equal actions.

The product bound is sharp under the declared rowwise restrictions. Take just one live state. In the first model it survives surely at every date; in the second it survives the next date with probability 1−ε_t and otherwise enters absorbing failure. Each completed-row distance is exactly ε_t, and the two terminal survival probabilities are 1 and the product. No smaller universal bound is possible. For ε=(0.1,0.2,0.3), the exact worst-case difference is 0.496, compared with the manuscript's valid outer bound 0.6. For two reform rules, the contrast bound similarly improves to twice the product bound. It is attainable when two actions exchange the sure-survival and hazard transitions across the two models. This does not turn arbitrary confidence regions with shared parameters into a sharp joint identified set; it characterizes the stated unrestricted row-distance class.

The binary mediation construction also admits an exact identified-set interpretation. Its observed randomized-reform law has S fair Bernoulli in either arm and Z=A surely. Consistency and randomized A imply Z(0,S(0))=0 almost surely. For any compatible model with the declared binary mediator intervention,

\[
N=\mathbb E[Z(0,S(1))]\in[0,1].
\]

The two manuscript models attain the endpoints. Every intermediate value is attainable as well. Introduce a latent Bernoulli variable V of mean θ, independent of randomized A and the fair U. Keep S=A exclusive-or U. If V=1, use the manuscript's support-mediated response Z(a,s)=s exclusive-or U; if V=0, use its direct response Z(a,s)=a. Under the naturally generated mediator, both branches give Z=A exactly, so the complete observed law is unchanged for every θ. Under the cross-world mediator contrast, the first branch contributes one and the second zero. Therefore N=θ. The sharp identified set for this particular observed law is exactly [0,1].

This strengthening explains the obstruction more precisely than point nonidentification alone. Even both reform arms, positivity of each mediator value within each arm, perfect outcome measurement, and a maximal total reform effect leave the entire unit interval possible for the natural indirect effect. Mediator positivity does not supply mediator exchangeability or identify the cross-world response.

The finite products, example arithmetic, and endpoint constructions were independently checked. The manuscript's weaker sensitivity inequality is explicitly an outer bound, so its lack of product sharpness is not an error. The additional sharp results above support the restricted analysis while preserving its distinction between reform effects, assigned-status effects, and support-mediated mechanisms.
