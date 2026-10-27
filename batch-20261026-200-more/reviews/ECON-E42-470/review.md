# Exact settlement feasibility requires every holder-subset coverage inequality

The source's “Consolidating protocol exposures” correctly notes that aggregate external assets need not suffice when claim accessibility is restricted. Its allocation system (8) admits an exact characterization that identifies every potential bottleneck and the minimum shortfall funding.

Let holders form a finite set I and external assets a finite set A. Asset a supplies v_a≥0 deadline goods; holder i requires d_i≥0. Draw an edge a∼i precisely when an enforceable claim permits allocation from a to i, with no additional edge-specific limit. For S⊆I let N(S) be the assets connected to at least one holder in S. Then full settlement is feasible if and only if
∑_{i∈S}d_i ≤ ∑_{a∈N(S)}v_a for every S⊆I.
The source's aggregate condition is the special case S=I, possibly including assets inaccessible to everyone on its right side. Testing all subsets retains the legal accessibility information that an aggregate backing ratio discards.

Necessity follows by summing holder demands within S: they must all be financed from N(S), whose total capacity cannot be exceeded. For sufficiency, construct a directed network from source to assets with capacities v_a, assets to their permitted holders with capacity M, and holders to sink with capacities d_i, choosing M greater than total assets plus total demands. Any cut using an asset-holder edge costs more than the trivial cut of all demand edges, so a minimum cut uses none. For a finite cut let S be the holders on the sink side. All their accessible assets must also be on the sink side; making exactly N(S) the sink-side assets minimizes that cut. Its capacity is
∑_{a∈N(S)}v_a + ∑_{i∉S}d_i.
The maximum-flow/minimum-cut theorem therefore gives maximum payable total
D−max_{S⊆I}[d(S)−v(N(S))],
where D=∑d_i and the maximum is nonnegative because S may be empty. The subset inequalities make this maximum zero, yielding a flow that saturates every holder-demand edge. That flow is exactly a feasible allocation in (8).

The same argument gives an exact rescue requirement. If new liquid goods can be supplied directly to any holder without restriction, the smallest additional amount needed is
Δ*=max_{S⊆I}[d(S)−v(N(S))].
Every subset deficit is a lower bound. A maximum flow leaves total unmet demand Δ*; injecting exactly those unmet amounts directly to their holders attains full settlement. This is a statement about physical liquidity availability, not the welfare or fiscal cost of the injection.

For example, two holders each demanding one can have two units of aggregate assets yet fail settlement: let the first asset provide 1/2 and be the only asset accessible to holder one, while the second provides 3/2 and serves only holder two. The subset {one} has deficit 1/2, so exactly that unrestricted injection is necessary. Relabeling a wrapper does not create a new asset capacity or eliminate its subset deficit.

The theorem assumes enforceable simultaneous fractional allocations and no seniority or edge limits beyond accessibility. Sequential priority, collateral reuse, legal netting and stochastic ownership require explicit additional constraints. It completes a finite exposure calculation without solving endogenous redemptions or protocol participation.

Source: [ECON-E42-470-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/e5/prb_e52accb63be94e76882d07c0c63af88f/contributions/con_33c089a95a7443539e5c20abc259e6e0/files/E42-470.tex), canonical revision `rev_5343436056e64bf6b776cff3ede3a93c`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
