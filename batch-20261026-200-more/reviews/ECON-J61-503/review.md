# Exact cumulative wage losses with capital adjustment

The source bounds the cumulative native wage loss between two geometric sums. Its exact wage path permits a sharper representation: cumulative losses are an explicitly convergent positive series, with a controlled second-order approximation. This quantifies transition losses even when wages eventually recover completely.

Use \(x=M/(N+M)\in[0,1)\), \(r=1-\eta\in[0,1)\), baseline wage \(\bar w>0\), and \(0<\alpha<1\). For any \(0<\beta\le1\), define the infinite-horizon loss
\[
\mathcal L=\bar w\sum_{t=0}^\infty\beta^t
              \{1-(1-xr^t)^\alpha\}.
\tag{A}
\]
It is finite by the source's upper bound, since \(\beta r<1\). The case \(x=0\) gives zero.

For \(k\ge1\), let
\[
c_k=(-1)^{k+1}{\alpha\choose k}.
\]
Every \(c_k\) is positive: for \(k\ge2\), the product defining the binomial coefficient has one positive factor and \(k-1\) negative factors. The binomial expansion on \(0\le z<1\) therefore gives
\[
1-(1-z)^\alpha=\sum_{k=1}^\infty c_kz^k.
\]
Substitute \(z=xr^t\) into (A). All terms are nonnegative, so exchanging the sums is justified by monotone convergence, without assuming absolute convergence in advance. Summing each geometric series yields the exact identity
\[
\frac{\mathcal L}{\bar w}
=\sum_{k=1}^\infty\frac{c_kx^k}{1-\beta r^k}.
\tag{B}
\]
Its finiteness follows independently from the upper bound on (A). Thus partial sums of (B) are certified lower bounds on the actual loss.

The first two terms give
\[
\frac{\mathcal L}{\bar w}
=\frac{\alpha x}{1-\beta r}
+\frac{\alpha(1-\alpha)x^2}{2(1-\beta r^2)}
+\mathcal R.
\tag{C}
\]
The remainder has the explicit bound
\[
0\le\mathcal R\le
\frac{\alpha(1-\alpha)(2-\alpha)x^3(1-x)^{\alpha-3}}
     {6(1-\beta r^3)}.
\tag{D}
\]
To verify it, differentiate \(f(z)=1-(1-z)^\alpha\) three times:
\(f'''(z)=\alpha(1-\alpha)(2-\alpha)(1-z)^{\alpha-3}\).
On \([0,x]\) this derivative is positive and bounded above by its value at \(x\). Taylor's integral remainder is therefore between zero and that bound times \(z^3/6\). Apply it at \(z=xr^t\) and sum. This proves (D), rather than treating the second-order expansion as an unqualified numerical approximation.

Every term in (B) increases with \(x\) and with \(r\). For a positive inflow, cumulative losses therefore rise strictly as adjustment slows, apart from a boundary comparison with no change in \(r\). This statement holds at \(\beta=1\); eventual recovery does not imply zero undiscounted transition losses. The first two denominators also distinguish first-order propagation \(r\) from second-order propagation \(r^2\).

Boundary checks are exact. If \(\eta=1\), then \(r=0\), and (B) reduces to \(\sum_kc_kx^k=1-(1-x)^\alpha\), the impact-period loss alone. If \(M=0\), every term vanishes. As \(\eta\downarrow0\) with \(\beta=1\) and \(x>0\), even the first term diverges; the limit approaches a nonadjusting capital stock and is different from every fixed positive adjustment rate.

This is a mathematical refinement of the announced capital-adjustment technology. It does not derive that technology from saving behavior, combine renter losses with native ownership gains, or identify migration selection and innovation responses. No simulated or empirical result is claimed.

Source: [ECON-J61-503-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/3b/prb_3bdedadfe37045f49d313891523164d6/contributions/con_442a61b3b3604756b2f1802b2fca37b9/files/J61-503.tex), canonical revision `rev_1a6597dac456418ba2cf69f42b1131b0`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
