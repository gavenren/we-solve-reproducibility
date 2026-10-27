# Scarce-research clearing, welfare accounting, and an elastic-supply boundary

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/c1/prb_c11e4f89671b4e8aaf4662ca3a8c9de4/contributions/con_e5fd013926ea4e3dbb16a7db9fa081cb/files/O34-212.tex), revision `rev_3f97ca425a094dd6956d945914a14d7f`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim.** The two-project equilibrium and welfare formula are internally consistent, including the treatment of wages as transfers. The contribution metadata identifies an unresolved exploration, and its manuscript explicitly assumes fixed research labor, an exogenous entrant prize, and a specified distortion per incumbent success. The following independent calculation checks those claims and derives the local crowding-out formula when research supply is elastic. This makes the source's fixed-supply restriction operational rather than treating its acknowledged dynamic limitations as mistakes.

For an interior allocation, firms' first-order conditions are

\[
e_1=A-w,\qquad e_2=1-w.
\]

Imposing \(e_1+e_2=1\) gives \(w=A/2\), \(e_1=A/2\), and \(e_2=1-A/2\). For \(A\in[0,2]\) these quantities respect the individual bounds. Strict concavity gives unique firm demands. At \(A=0\), demand at wage zero is exactly one and any positive wage creates excess supply; at \(A=2\), wages below one generate excess demand and wages above one create excess supply. Thus the wage uniqueness claim includes the truncation boundaries; it does not merely follow from interior differentiation.

Substitution in social welfare gives

\[
W(A)=V_2-\tfrac12+
\tfrac12(V_1-V_2+1)A-
\tfrac14(1+2d)A^2.
\tag{A}
\]

The second derivative is \(-(1+2d)/2<0\). Its unconstrained vertex is therefore \((V_1-V_2+1)/(1+2d)\), and projection onto \([0,2]\) gives the manuscript's optimum. Completing the square establishes the finite-duration nearest-prize rule even when the feasible patent prizes are unequally spaced. Completing the square also identifies every tie exactly, including menus with unequal gaps between feasible patent prizes.

For an independent boundary extension, let total research employment be \(Q=e_1+e_2\) and replace fixed supply by a differentiable inverse supply schedule \(w=c(Q)\), where \(c'(Q)\ge0\). Real opportunity cost is \(C(Q)\), with \(C'=c\). Keep the same firm technologies and suppose both research choices remain strictly between zero and one. Labor clearing becomes

\[
Q=A+1-2c(Q).
\]

Its left side after rearrangement has derivative \(1+2c'(Q)>0\), so the implicit local response is well-defined. Differentiation yields

\[
Q'\!=\frac1{1+2c'},\quad
w'\!=\frac{c'}{1+2c'},\quad
e_1'\!=\frac{1+c'}{1+2c'},\quad
e_2'\!=-\frac{c'}{1+2c'}.
\tag{B}
\]

Thus the entrant remains crowded out whenever the inverse supply slope is positive, but the fraction of the incumbent's additional research displaced from the entrant is

\[
\frac{-e_2'}{e_1'}=\frac{c'}{1+c'}<1
\]

for a finite slope. With perfectly elastic local supply, the entrant is unaffected and the incumbent's increment is wholly additional. As the local inverse-supply slope tends to infinity, (B) approaches \(e_1'=1/2\), \(e_2'=-1/2\), and \(Q'=0\), recovering the manuscript's fixed-supply comparative statics. This is a statement about local derivatives in an interior regime; it does not identify the level or intercept of a limiting supply curve.

The welfare accounting changes in a precise way under this extension. Include the real supply cost \(C(Q)\), while retaining transfers within household welfare:

\[
\widetilde W=V_1e_1+V_2e_2-\tfrac12(e_1^2+e_2^2)-C(Q)-dAe_1.
\]

Using the firm conditions and \(C'(Q)=w\), differentiation gives

\[
\widetilde W'
=[V_1-(1+d)A]e_1'+[V_2-1]e_2'-de_1.
\tag{C}
\]

This separates project social-private wedges, reallocation, and the direct added distortion. Applying the fixed-supply quantities and derivatives to (C) reproduces the derivative of (A), providing a second check of the original coefficient \(1+2d\). Counting wages again as an additional real cost would fail this reconciliation: households receive the same wage payments firms make. With elastic supply, \(C(Q)\), rather than total wage payments, is the appropriate additional resource cost.

The source's numerical welfare comparison also follows from (A): for \(V_1=V_2=1\), \(d=1/2\), prizes one and two give welfare changes \(1/2\) and \(-1/2\). Negative incremental welfare is compatible with the common endowment normalization. These conclusions support a scoped equilibrium channel, not a general patent-policy optimum. Entry, replacement, acquisition, and a structural relation between patent rents and product-market losses remain outside the specified model. No external literature-priority claim is made by this review.
