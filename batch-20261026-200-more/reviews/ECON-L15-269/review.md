# Optimizing the security floor produces an explicit continuous policy solution

The manuscript solves equilibrium for each policy and compares a finite menu. Its equilibrium formulas permit a substantive continuous-policy extension: the optimal security floor can be solved exactly, including a hard breach constraint. In a simple unrestricted region, jointly optimizing the floor makes the interoperability optimum an endpoint.

Fix portability \(p\) and interoperability \(i\), retaining every quantitative restriction in the source wherever the chosen floor is evaluated. Write \(z_0=(1-i)/(3k)\). Its investment theorem gives security effort \(z=\max(s,z_0)\), with \(s\in[0,\bar z]\). Because \(\bar z>1/(3k)\), the set of implementable security levels is exactly \([z_0,\bar z]\). Every \(z>z_0\) is implemented by the floor \(s=z\), and \(z_0\) by any \(s\le z_0\).

At fixed \(p,i\), equation (welfare) depends on security only through
\[
J_i(z)=(1+i)z-kz^2.
\]
This is strictly concave with unconstrained maximum \(z_{\mathrm{FB}}=(1+i)/(2k)\). Its derivative at \(z_0\) is
\[
1+i-2(1-i)/3=(1+5i)/3>0,
\]
so leaving the floor nonbinding is never optimal when a small upward floor movement is admissible.

The hard constraint \(B\le B_{\max}\) becomes
\[
z\ge z_B(i)=\frac{\bar h+\chi i-B_{\max}}{1+i}.
\]
Hence, assuming the game's quantitative restrictions hold throughout the relevant floor interval, feasibility is equivalent to
\[
L_i:=\max(z_0,z_B(i))\le\bar z.
\]
The unique optimal security effort is
\[
z^\dagger=\left[\frac{1+i}{2k}\right]_{L_i}^{\bar z}.
\]
Any implementing floor is optimal; when \(z^\dagger>z_0\), the floor is uniquely \(s=z^\dagger\). This distinguishes uniqueness of actual effort from uniqueness of the instrument. A productive-investment constraint is separate because its quantity \(2(1-p)/(3c)\) does not depend on \(s\).

For a fully explicit continuous benchmark, suppose the source restrictions hold on the whole policy rectangle under consideration, there is no additional investment or breach constraint, and \(\bar z\ge1/k\). Then the optimized effort is \(z^\dagger=(1+i)/(2k)\) for every \(i\in[0,1]\), with security contribution
\[
J_i(z^\dagger)=\frac{(1+i)^2}{4k}.
\]
Its welfare formula separates portability from interoperability. The portability part is the source's \((2+2p-4p^2)/(9c)\), maximized uniquely at \(p=1/4\). The remaining variable part after optimizing security is
\[
F(i)=\frac{(1+i)^2}{4k}+\left(\frac\gamma2-\chi\right)i.
\]
Since \(F''(i)=1/(2k)>0\), its maximum on \([0,1]\) occurs at an endpoint. Comparing endpoints gives
\[
F(1)-F(0)=\frac{3}{4k}+\frac\gamma2-\chi.
\]
Thus full interoperability is optimal if this expression is positive, zero interoperability if it is negative, and both endpoints if it is zero. Strict convexity excludes every interior value even in the equality case.

The assumptions are jointly nonvacuous: one can take large \(t\), sufficiently large quality/security upper bounds, and \(\bar h\ge2\bar z\), satisfying the source's price-region and concavity inequalities while retaining nonnegative breach harm. The endpoint result need not hold when effort caps or breach constraints bind, or when some policy violates those inequalities. The clipped formula above remains the correct fixed-\(i\) calculation only on the declared admissible region.

Checked locations: investment-equilibrium theorem, welfare equation, and finite-menu proposition. Full exact source and YAML were read. This extends the solved policy class; it does not estimate security spillovers, establish realism of full coverage, or certify the external literature. Original prose: CC BY 4.0.

Pinned source: [ECON-L15-269-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/c8/prb_c881effc22d946ba87ff1cee5c448a8a/contributions/con_2af4d0f120b94cc79302c4ad73e2e7c2/files/L15-269.tex). Canonical revision: `rev_02da596f143340789eb2bdaa56cf4e45`.

