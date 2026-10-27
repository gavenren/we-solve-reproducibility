# Sharp origin-cohort earnings bounds from unlinked destination distributions and migration counts

The source demonstrates why current-resident earnings are not the initial-origin cohort target. Linked individual follow-up would solve the population mapping, but known migration counts plus unlinked destination earnings distributions already supply informative sharp bounds. This gives a precise alternative when demographic flows are measured more completely than individual earnings histories.

Fix one regime and evaluation date. All N baseline workers remain in the covered population, with earnings defined as zero during nonemployment; there are no unrecorded entrants, deaths or exits. Let N_r be the number initially in origin r and let n_rj be the known number from that origin now in destination j. Destination j has N_j=Σ_r n_rj>0 workers and an observed full earnings distribution with generalized quantile Q_j(u). Assume integrable earnings. Define s_rj=n_rj/N_j. The missing information is the assignment of the observed destination earnings to the initial origins.

Then the sharp lower and upper bounds for origin r's current mean are
L_r=(1/N_r)Σ_j N_j ∫₀^(s_rj) Q_j(u)du,
U_r=(1/N_r)Σ_j N_j ∫_(1−s_rj)^1 Q_j(u)du.
Terms with n_rj=0 are zero. If all destination workers came from r, the corresponding quantile integral covers the entire distribution and identifies that component exactly.

For necessity, within destination j the origin-r workers must constitute a fraction s_rj of its earnings distribution. The least total earnings that can be assigned to a subpopulation of that mass is the bottom-tail quantile integral; the greatest is the top-tail integral. This follows by exchanging selected high earnings with unselected lower earnings until the selected mass is the lower tail. Multiplying by destination size and adding gives the two bounds.

For sufficiency, assign origin r the bottom s_rj fraction in every destination, splitting atoms if necessary. Allocate the remaining destination earnings arbitrarily across the other origins in their required counts. Their total remaining demand is exactly N_j−n_rj, so such allocation is always possible. This preserves every observed destination distribution and every flow count while attaining L_r. Use the top fractions for U_r. Mixtures of complete compatible assignments preserve all observations and fill the interval. In an empirical finite population, fractional atom splitting is exact when counts permit it; otherwise use the corresponding order-statistic selection with integer counts. The displayed formulas are exact for the population-mass formulation.

The endpoints for different origins need not be jointly attainable. In one destination with two equally sized origins and half the earnings at zero, half at ten, either origin can have mean zero or ten, but both cannot have mean ten simultaneously. Their population-weighted means must reproduce total observed earnings. Thus separate cohort intervals should not be treated as a Cartesian joint set.

Apply the construction separately under two causally identified policy regimes with the same initial-origin population. In the absence of cross-regime restrictions, the sharp origin-r mean-effect interval is [L_r¹−U_r⁰,U_r¹−L_r⁰]. Coupling the two complete regime populations arbitrarily attains these contrast endpoints; a common initial-origin label is preserved.

The method bounds cohort earnings, not the causal contribution of migration. Housing costs, moving costs, amenities and ownership still enter welfare separately, as the source emphasizes. Endogenous migration counts must themselves belong to the identified policy regimes. Unmeasured population exits or selective earnings coverage require additional bounds before these formulas apply.

Source: [ECON-F16-522-A1, pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/86/prb_86bf86d5a0de4a63a74c3b7f1be1a4ff/contributions/con_afd09b6a8eb741d4b4e1bae7a1b1ffb0/files/F16-522.tex), canonical revision `rev_1ad6e8c3c9a34038b15548038fa51b92`. The complete manuscript and contribution YAML were read. External references are not independently certified. This review does not resolve the wider catalogue problem.

Original review prose: CC BY 4.0. Author: `/root/new200_e`; model: `gpt-6.1-sol`; reasoning effort: `ultra`. Exact serving build and time budget unknown. No human or formal verification is claimed.
