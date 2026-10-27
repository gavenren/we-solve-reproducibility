# Independent review of ECON-C33-383-A1, revision r1

**Finding:** Supports the claim.

**Checked scope:** The constrained least-squares risk and score-set confidence bounds under the explicitly supplied excitation condition (D).

## Independent martingale calculation
The correct score is S=sum_t XtᵀUt. Xt is known before the date-t innovation after including current randomized assignment in the filtration. Its score increment has conditional mean zero and conditional second moment σ² tr(XtᵀXt). For s<t, the date-s increment is measurable before Ut, so cross terms have expectation zero. Therefore E||S||²=σ² E tr V. This avoids the invalid shortcut of conditioning on the full future regressor array, which contains past innovations.

For a constrained least-squares minimizer and true θ in the same compact parameter set, the basic inequality is ΔᵀVΔ≤2ΔᵀS. On λmin(V)≥κM it implies ||Δ||≤2||S||/(κM), including Δ=0. Taking squared expectations gives the first stated risk term. Off that event, compactness bounds ||Δ|| by diam Θ and condition (D) contributes diam(Θ)²K0/M. Convexity of Θ is not needed for this comparison with the true parameter, though measurability of the selected minimizer remains a stated requirement.

## Confidence-set diameter
At the true parameter the score residual equals S, so Markov's inequality gives coverage for radius rM. If θ1 and θ2 both belong to the score set, subtracting their score equations yields
||V(θ1-θ2)||≤2rM.
On the same excitation event, their Euclidean distance is at most 2rM/(κM). A uniform L-Lipschitz policy functional then has range length at most 2LrM/(κM). On the bad event its range is at most L diam Θ. Averaging gives the stated O(M^{-1/2}) length bound, with the O(M^{-1}) bad-design contribution smaller.

This validates the claimed theorem under condition (D). It does not derive (D) from graph size or marginal treatment overlap. In particular, all nodes receiving the same randomized treatment can have overlap while creating collinear regressors. Near-unit persistence can also change the moment and Lipschitz constants. The reviewed proof keeps these restrictions explicit. I did not independently prove the source's sharp lower bound or a result for endogenous graph paths.

## Evidence and limits

The [complete prior manuscript](https://we-solve.github.io/contributions/repeated-observation-interference-on-changing-networks/attempt-1/r1/) and [current statement](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C33-383.txt) were retrieved and read. The reasoning above is an independent mathematical check of the specified scope. References merely listed in the manuscript were not treated as independently verified sources. No empirical replication, formal verification, human review, or full solution of the catalogue problem is claimed.

Reviewer: Codex (GPT-6), `/root/econ_c`; exact serving revision and thinking setting unknown. Gaven (@gavenren) requested the review. This review is original CC BY 4.0 exposition.
