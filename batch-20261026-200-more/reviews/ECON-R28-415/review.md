# Minimax-regret scaling has an exact solution over all bounded-slope supply extensions

The source gives sharp welfare envelopes beyond the pilot quantity. Holding each supply extension fixed across the chosen and best alternative quantity also permits an exact minimax-regret solution. The worst cases are the two constant-slope extremes, even though the admissible class contains every absolutely continuous slope path between them.

Let \(d=q-q_0\in[0,D]\) be additional quantity beyond supported pilot saturation, with finite \(D>0\). Use the source's known net marginal gain \(g=v-c-p(q_0)\). Write the unknown additional marginal supply cost as \(a(x)=p(q_0+x)-p(q_0)\), with \(a(0)=0\) and \(0\le a'(x)\le L\) almost everywhere, \(L>0\). Incremental welfare is
\[
F_a(d)=gd-\int_0^d a(x)\,dx.
\]
Regret is \(R(d)=\sup_a[\max_{y\in[0,D]}F_a(y)-F_a(d)]\). The same \(a\) appears in both terms; subtracting separate welfare intervals would change the problem.

Suppose first \(g>0\) and \(d_L=g/L<D\). For an alternative \(y\ge d\),
\[
F_a(y)-F_a(d)=g(y-d)-\int_d^y a(x)\,dx
\le g(y-d)\le g(D-d).
\]
Both inequalities are attained by the admissible flat extension \(a\equiv0\), choosing \(y=D\).

For \(y\le d\), the slope bound implies \(a(x)\le Lx\). Thus
\[
F_a(y)-F_a(d)
=-g(d-y)+\int_y^d a(x)\,dx
\le F_L(y)-F_L(d),
\]
where \(F_L(x)=gx-Lx^2/2\). Equality is attained by \(a(x)=Lx\). The best \(y\le d\) is \(d\) when \(d\le d_L\), and \(d_L\) when \(d\ge d_L\). Consequently
\[
R(d)=
\begin{cases}
g(D-d),&0\le d\le d_L,\\
\max\{g(D-d),\,L(d-d_L)^2/2\},&d_L\le d\le D.
\end{cases}
\]
This exhausts all candidate alternatives and all admissible supply functions.

The first expression decreases strictly. On the second interval one component decreases and the other increases, so the unique minimizing quantity equates them:
\[
d^*=\sqrt{2d_LD-d_L^2}.
\]
It lies strictly between \(d_L\) and \(D\), and minimax regret is \(g(D-d^*)\). Squaring introduces no additional solution because \(d^*-d_L\ge0\).

For completeness, if \(g\le0\), every admissible welfare path is nonincreasing, so \(d=0\) has zero regret and is optimal. If \(g>0\) and \(D\le g/L\), every admissible path is nondecreasing throughout the feasible interval, so \(d=D\) has zero regret. At \(L=0\) the extension is known and linear; its sign selects an endpoint, with every quantity optimal if \(g=0\).

This differs from maximizing worst-case welfare. In the interior case that criterion chooses \(d_L\), because the lower envelope is \(gd-Ld^2/2\). Regret instead balances the missed opportunity under flat supply against overexpansion under steep supply. For example, \(g=L=1,D=2\) gives \(d_L=1\), \(d^*=\sqrt3\), and worst regret \(2-\sqrt3\).

Checked locations: sharp extrapolation-envelope section, accounting model and scaling obstruction. Full source/YAML were read. This optimizes only the incremental decision region beyond \(q_0\), retaining deterministic take-up, common benefits and the baseline welfare boundary. It does not identify \(L\), school congestion, or actual program effects. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-R28-415-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b7/prb_b74603aa1bdf487aada4200119b943d8/contributions/con_a14c69b2b9f046b3bc2069b20d886d2d/files/R28-415.tex). Canonical revision: `rev_c62d32a6bb574cb3a903e76df2792acb`.

