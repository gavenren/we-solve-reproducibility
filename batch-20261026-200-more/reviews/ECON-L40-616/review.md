# Sharp all-period restoration probabilities from full path marginals

The source proves sharp restoration-probability bounds for binary outcomes and extends the obstruction to constant paths. Full finite path distributions also admit exact sharp bounds. The relevant object is a compatibility graph between remedied and no-merger paths, which preserves the requirement that restoration hold at every evaluation date.

Let the remedy path have finite support X with probabilities μ_x, and the no-merger counterfactual path have finite support Y with probabilities ν_y. Suppose these two path marginals are identified, but their cross-world coupling is unrestricted. Declare a pair (x,y) good when the chosen all-period tolerance criterion holds, for example max_t|x_t−y_t|≤ε. Let E_G be the good-pair graph and E_B its complement. This uses complete path marginals; separate one-date marginals would leave a larger uncertainty problem.

For any bipartite edge set E define its neighborhood N_E(A) for a subset A⊆X, and the deficiency

D_E=max_{A⊆X}{μ(A)−ν(N_E(A))}.

The empty set makes D_E≥0. Then the exact identified interval for restoration probability is

[D_{E_B}, 1−D_{E_G}].

Here is a derivation including attainment. A partial coupling supported on E transports some amount of probability from X to Y, with row masses at most μ and column masses at most ν. Build a flow network with source capacities μ_x, sink capacities ν_y, and capacity M>1 on allowed edges. A cut of capacity at most one exists, so a minimum cut does not cut an allowed M edge. If A is its source-side set of X vertices, all N_E(A) must also be source-side. Taking exactly that neighborhood minimizes the finite cut cost, giving 1−μ(A)+ν(N_E(A)). The max-flow/min-cut identity therefore gives maximal E-supported transported mass 1−D_E.

Any full coupling's mass on E is such a partial flow, so it cannot exceed that amount. Conversely take an optimal partial flow. Its remaining row and column masses have the same total, so extend them to a full coupling, for example by their normalized product when the total is positive. The extension cannot add positive E mass: if it did, the original flow was not maximal. Thus 1−D_E is the attained maximum full-coupling probability of E.

Apply this once to good edges for the upper restoration bound and once to bad edges for the lower bound, using Pr(good)=1−Pr(bad). Both extremal couplings have exactly the given path marginals. Convex mixtures preserve those marginals and attain every probability between their restoration values, proving the entire interval sharp.

For zero tolerance on common discrete path labels, good edges pair only identical paths. The upper bound reduces to ∑_x min{μ_x,ν_x}=1−TV(μ,ν). The lower bound is max{0,max_x(μ_x+ν_x−1)}: in the bad graph, a singleton's neighborhood excludes its identical label, while any set containing two distinct labels reaches all opposite labels. These are precisely the possible positive deficiencies. Zero-probability labels may be added to align the supports.

For binary one-date outcomes with success probabilities p,q, the lower expression is max{0,p+q−1,1−p−q}=|1−p−q| and the upper is 1−|p−q|, recovering the manuscript. With genuine multi-date paths the graph can encode restoration failures occurring at different times; reducing each path to its average can change the event and its bounds.

The formulas are finite exact identification results, not evidence that real case selection or no-merger counterfactuals are known. They add a complete path-coupling solution under identified marginals while leaving demand, buyer viability, monitoring and causal enforcement selection unresolved.

Source: [ECON-L40-616-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/94/prb_94cf4748105a4261a5d907ab3611fbd0/contributions/con_b08fb6ebf7fb4522856f788438b95035/files/L40-616.tex), canonical revision rev_95a55595913d41d493ce909413aa18f1. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
