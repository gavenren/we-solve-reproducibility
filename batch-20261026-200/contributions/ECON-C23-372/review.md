# Independent review of ECON-C23-372-A1, revision r1

**Finding:** Supports the claim.

**Checked scope:** Conditional realized-effect prediction coverage and the indistinguishable-factor lower bound; not general heterogeneous-effect randomization inference.

## Independent target and coverage check
For the realized average treatment-effect target, subtracting the true post-treatment effect from the observed treated-minus-synthetic estimator cancels Y1t(1). The remaining error is exactly the average untreated counterfactual gap. Thus treated-outcome variation is not an additional sampling term in this particular target. This would change for a population expectation target.

From the assumed conditional MGF bound for sum ξt, exponential Markov gives exp(-sHx+s²Hσ²/2). Minimizing over s>0 gives exp(-Hx²/(2σ²)); applying the same argument to the negative sum gives the two-sided bound. Adding the deterministic bound Δ on the average approximation error produces the displayed interval. Donor and intercept selection are covered only because the MGF and approximation restrictions are conditional on all pretreatment information, including that selection. A good prefit score alone cannot establish these assumptions.

## Independent nonidentification construction
Set every observed outcome to zero. Model zero has untreated treated-unit post outcomes zero. Model one gives them a while keeping treated outcomes zero. A one-factor representation uses treated loading one, every donor loading zero, and a factor path that is zero before treatment and a afterwards. Both models produce exactly the same observed law, but the realized treatment effects are 0 and -a.

Under the common observable law, any confidence set covering each target with probability at least 1-α contains both with probability at least 1-2α by the union bound. Hence its diameter is at least a on that event. This conclusion holds even for randomized procedures and is not an artifact of a particular synthetic-control estimator. It applies to the unrestricted factor class used in the counterexample; an additional donor-spanning condition can exclude it.

Finally, the persistent residual example ξt=Z has average Z, whose variance does not decrease with the horizon. It cannot satisfy the stated sum-MGF bound with a fixed variance proxy as H grows. This verifies that the source's shrinking-width theorem does not accidentally cover arbitrary dependence. I have not established finite-sample validity for the broader factor-model or heterogeneous-effect randomization settings.

## Evidence and limits

The [complete prior manuscript](https://we-solve.github.io/contributions/synthetic-control-inference-with-few-treated-units/attempt-1/r1/) and [current statement](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C23-372.txt) were retrieved and read. The reasoning above is an independent mathematical check of the specified scope. References merely listed in the manuscript were not treated as independently verified sources. No empirical replication, formal verification, human review, or full solution of the catalogue problem is claimed.

Reviewer: Codex (GPT-6), `/root/econ_c`; exact serving revision and thinking setting unknown. Gaven (@gavenren) requested the review. This review is original CC BY 4.0 exposition.
