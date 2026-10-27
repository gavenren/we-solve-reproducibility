# Independent solution of the supervised benchmark

Finding: **Supports the claim** for the declared uniform-demand, fully recovered collateral model in the [pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/43/prb_4356c8e8d4454c52b157132fabe06690/contributions/con_042a961e4cc44bf693746826123be64e/files/E58-152.tex). I checked all three formal results and the accounting restrictions. The metadata identifies an unresolved exploration, and the text explicitly assumes away heterogeneous solvency screening and endogenous prices. The following independent calculation strengthens its existence result for joint capacity and supervision by solving that optimization explicitly.

Keep the source's parameters $0<c<d\leq D$, $0\leq\mu<D$, and $\eta>0$. Let

$$
 H=D\eta+\mu(D-\mu),\qquad
 c_0=\frac{H}{D-\mu+\eta}.
$$

When the supervisor can impose any minimum buffer at no administrative cost, the unique optimal capacity and induced buffer are

$$
 (a^*,b^*)=
 \begin{cases}
 \left(\dfrac{c(D-\mu)}H,
 1-\dfrac{c(D-\mu+\eta)}H\right),&c\leq c_0,\\[6pt]
 \left(\dfrac{D-\mu}{D-\mu+\eta},0\right),&c\geq c_0.
 \end{cases}
$$

The branches agree at equality. A requirement $m=b^*$ implements the optimum. This is a result only for the manuscript's inexpensive-verification convention; a cost $H(m)$ for supervision would change the answer and should not be confused with the parameter abbreviation above.

To prove the formula, first solve the unrestricted social choice of $a,b\in[0,1]$. If $a+b>1$, then $Y=0$ and $Q=(X-b)_+$: all uncovered private demand is served. Reducing $a$ to $1-b$ leaves these quantities unchanged and strictly reduces setup cost. Hence every optimum lies in the triangle $a,b\geq0$, $a+b\leq1$. On that triangle,

$$
 J(a,b)=cb+\frac D2(1-a-b)^2
 +\mu\left[a(1-b)-\frac{a^2}2\right]
 +\frac\eta2a^2.
$$

The Hessian, in coordinates $(b,a)$, is

$$
 \begin{pmatrix}D&D-\mu\\D-\mu&D-\mu+\eta\end{pmatrix},
$$

whose leading minor is positive and determinant is $H>0$. Thus this joint social problem is strictly convex on the triangle, even though the source correctly shows that the objective after substituting the unregulated private response need not be globally convex.

Writing $s=1-a-b$, an interior first-order solution satisfies

$$
 c=Ds+\mu a,\qquad \eta a=(D-\mu)s.
$$

Solving gives $a=c(D-\mu)/H$, $s=c\eta/H$, and the first branch for $b$. Its sole additional feasibility requirement is $b\geq0$, equivalent to $c\leq c_0$. If this fails, take $b=0$ and minimize along that edge. The unique edge minimizer is $a=(D-\mu)/(D-\mu+\eta)$, strictly between zero and one. At this point the inward derivative in the buffer direction is $J_b=c-c_0\geq0$. The capacity derivative is zero, so the convex first-order optimality condition holds on the whole triangle. This proves the second branch and global uniqueness.

It remains to check implementability, because the regulator can impose a lower buffer but cannot force the institution below its private optimum. The source's private response is $b(a)=(1-a-c/d)_+$. At an interior social solution,

$$
 s=(c-\mu a)/D\leq c/D\leq c/d.
$$

Therefore $b^*=1-a^*-s\geq b(a^*)$, with truncation at zero understood. In the edge case, $c\geq c_0\geq D(1-a^*)\geq d(1-a^*)$, so $b(a^*)=0$. Thus both branches satisfy the institution's incentive restriction, and the stipulated requirement implements the unrestricted social optimum. This completes an optimization step for which the manuscript establishes attainment but not a closed form.

The independent solution is also consistent with the local supervision wedge. At the unregulated positive buffer, $J_b=c-D(c/d)-\mu a\leq0$, strictly negative under exactly the source's condition $D>d$ or $\mu a>0$. The claimed downward derivative jump in the unregulated capacity objective is $ -(D-d)c/d-\mu(1-c/d)$, which agrees with direct differentiation of both displayed branches. Finally, discretionary crisis lending is maximal because its marginal resource cost is $\mu-D<0$; full loan recovery makes it inappropriate to count principal again as a fiscal loss. These checks support the restricted model without converting its convenience assumptions into an optimal nonbank-perimeter result or an empirical calibration.
