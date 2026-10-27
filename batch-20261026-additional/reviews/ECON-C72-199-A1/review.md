# Dual centering certificates and sharpness of the structural regret factor

Finding: **Supports the claim**.

I read the complete [pinned C72-199 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/3d/prb_3dfc7665fcac4b5e92c5300ab46a3cd2/contributions/con_a81beacc02274959afbc690780820867/files/C72-199.tex), revision `rev_d02fad8ebac243a19ad66ca0e97eeefa`, and its exploration metadata. The manuscript explicitly does not prove a universal sub-third approximation. It supplies a computable structural condition, an elementary global fallback, and approximate mixing for constant candidate-list sizes. My check supports those statements and adds a dual optimality certificate plus an example showing that the structural regret constant cannot be improved for arbitrary surrogate equilibria.

The strategic shifts have the correct orientations. A column-dependent term can be removed from the row player's payoff because it is common to all her row deviations. A row-dependent term can similarly be removed from the column player's payoff. With M=A+B and residual C=M−c_i−d_j, the transformed game decomposes as (H+C/2,−H+C/2). At a zero-sum equilibrium, each unilateral H-deviation is nonpositive. The remaining C-deviation compares two averages of entries in [−ε_*,ε_*], so its half is at most ε_*. This verifies the factor and the player-specific certificates without assuming payoffs of the shifted game remain in [0,1]. Only the original payoff normalization is needed for the fallback and continuity arguments.

There is a useful independent way to certify the centering LP's optimum. For a real matrix Z, let ||Z||_1 denote the sum of absolute entries. The exact dual is

\[
\varepsilon_*=
\max\left\{\sum_{ij}Z_{ij}M_{ij}:
\sum_jZ_{ij}=0\ \forall i,\quad
\sum_iZ_{ij}=0\ \forall j,\quad
\|Z\|_1\le1\right\}.
\]

To see weak duality directly, the zero row and column sums cancel every additive c_i+d_j term. Therefore |sum Z_ij M_ij|=|sum Z_ij C_ij|≤ε||Z||_1≤ε for every feasible centering. Equality of the optimization values follows from finite LP duality: assigning nonnegative multipliers to the upper and lower residual inequalities produces their signed difference Z; stationarity in c and d gives the zero-sum constraints, and stationarity in nonnegative ε bounds the total multiplier mass by one. Conversely a balanced Z can be represented by its positive and negative parts. This supplies a short verifiable lower-bound witness alongside the primal residual.

For a 2-by-2 game define δ=M_11+M_22−M_12−M_21. The balanced matrix with alternating signs and absolute entries 1/4 gives ε_*≥|δ|/4. This is attained by setting s=δ/4 and choosing a centering with residual

\[
C=\begin{pmatrix}s&-s\\-s&s\end{pmatrix}.
\]

For example take c_1=0, d_1=M_11−s, d_2=M_12+s, and c_2=M_21−M_11+2s. Direct substitution gives the displayed residual. Thus ε_*=|δ|/4 exactly in this dimension. I used this closed-form primal-dual pair to independently check the structural theorem on 200 rational 2-by-2 games, computing a zero-sum equilibrium exactly and verifying the original game's regret inequality with rational arithmetic. These checks support the proof; they do not replace its arbitrary-dimension argument.

The multiplicative regret bound itself is sharp under the theorem's allowance of an arbitrary zero-sum equilibrium. Consider

\[
A=B=\begin{pmatrix}5/8&3/8\\3/8&5/8\end{pmatrix}.
\]

The exact centering optimum is ε_*=1/4. Choose c=(0,0), d=(1,1); then C has diagonal 1/4 and off-diagonal −1/4, and H is the constant matrix −1/2. Every strategy pair is consequently a zero-sum equilibrium. The pure off-diagonal pair consisting of row one and column two gives each player payoff 3/8, while each has a pure deviation earning 5/8. Its original regret is exactly 1/4=ε_*. Thus a smaller universal multiplicative factor cannot follow merely from optimal centering and the surrogate saddle inequalities. A specially chosen surrogate equilibrium or the later mixing step might improve this example; that would require additional selection information.

Finally, the grid argument has the claimed complexity boundary. The number of coefficient-grid pairs is polynomial in 1/τ when s and t are fixed, with exponent depending on their sum; it is not polynomial in the bit length of τ alone or for unrestricted list size. The manuscript states these restrictions and preserves fallback candidates by explicit comparison. I found no internal error in the centering certificate, fallback, or grid proof. The independent dual and sharpness example strengthen the structural result while leaving the acknowledged universal candidate-generation problem open.
