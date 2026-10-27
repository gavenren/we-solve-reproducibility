# A finite cycle certificate for permanent-service cash solvency

The manuscript's reserve recursion supplies an exact infinite-horizon criterion and proves that a stationary action choice suffices whenever finite reserves work. A finite graph certificate makes that criterion inspectable without treating positive expected margins as a substitute for solvency.

Fix a stationary policy μ selecting one feasible action in each state. Form its directed graph with an edge x→y for every y∈N(x,μ(x)), weighted by the realized cash increment g(x,μ(x),y). Nature can choose any permitted path. Starting at x₀, some finite reserve permits permanent service under μ if and only if every directed cycle reachable from x₀ has nonnegative total edge weight.

Necessity is immediate but economically consequential. If a reachable cycle has negative total cash, nature can follow a finite path to it and repeat the cycle indefinitely. Cumulative cash then tends to minus infinity and defeats every finite initial reserve. The cycle need not be probable or typical; the source asks for a guarantee over all permitted paths.

For sufficiency, suppose all reachable cycles have nonnegative weight. Any finite path that repeats a vertex contains a cycle. Removing that cycle gives another path with the same endpoint and weakly lower total cash. Repeating removals gives a simple path whose cash total is no greater than the original path's. Therefore the minimum cumulative cash over all finite paths is attained among simple paths, including the empty path. The exact minimum reserve is
r_μ(x₀)=max{0, −min_(simple paths from x₀) Σ_edges g}.
Every prefix then has cash at least −r_μ(x₀), so that reserve works. A smaller reserve fails on a minimizing path, proving minimality.

If m states are reachable and every edge has g≥−G for a known G≥0, each simple path has at most m−1 edges. Thus r_μ(x₀)≤(m−1)G. Zero-total cycles create no extra reserve requirement; strictly negative individual edges may still be affordable when their cycles are nonnegative. If a negative cycle is reachable, the reserve is infinite instead, so there is no misleading intermediate conclusion.

Combining this with the source's stationary-policy theorem gives a full existence certificate: finite-reserve indefinite operation from x₀ is possible exactly when there exists a stationary feasible policy whose reachable graph has no negative cash cycle. In the viable case, with m≤|X|, minimum reserves satisfy r_∞(x₀)≤(|X|−1)G. One may certify a proposed policy by finite shortest-path inequalities or inspect its cycles; the result does not assert that enumerating all stationary policies is efficient.

For a simple example, two states alternate with cash increments −3 then +4. The cycle gains one, so starting before the −3 payment requires reserve three and permanent service is feasible. Reversing the increments to −3 then +2 gives a negative cycle and no finite reserve suffices, even though a large one funds a long initial run.

The certificate also handles interval uncertainty in a cash increment when every value in its interval is permitted each time: replace each edge weight by its lower endpoint. This is exact for pathwise guarantees because nature can repeatedly choose those endpoints. Shared unknown parameters linking different dates could make that rectangular replacement conservative and require a different uncertainty model.

All actions must already satisfy physical reliability and affordability obligations. The theorem concerns financing a permitted service policy; it does not establish demand, collection behavior, default probabilities or the welfare value of keeping a minigrid open.

Source: [ECON-L94-483-A1, pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/36/prb_3622edc1c9ee4484ab91081a364f2e00/contributions/con_4afbe06aa51e4e8ba9cd67401ad3f596/files/L94-483.tex), canonical revision `rev_72b118efc3e24f13bd18d9ef03775efe`. The complete manuscript and contribution YAML were read. External references are not independently certified. This review does not resolve the wider catalogue problem.

Original review prose: CC BY 4.0. Author: `/root/new200_e`; model: `gpt-6.1-sol`; reasoning effort: `ultra`. Exact serving build and time budget unknown. No human or formal verification is claimed.
