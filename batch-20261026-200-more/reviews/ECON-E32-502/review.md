# An exact four-class joint set for a rank-two equal-eigenvalue response matrix

The source supplies exact coordinate bounds for arbitrary response matrices and a full joint simplex when A_H has rank one. A second nontrivial joint case can be solved constructively: four single-label classes with two equal nonzero response eigenvalues. The joint set is a capped simplex, and every point has an explicit orthogonal-rotation realization.

Assume m=4, each of the four classes contains one shock label, and A_H is positive semidefinite with eigenvalues (a,a,0,0), a>0. Thus t_H=2a. The exact joint share set is

{θ∈R⁴:0≤θ_i≤1/2 for every i, ∑θ_i=1}.

Necessity follows directly from the source's formula. After diagonalizing A_H, write A_H=aP where P is a rank-two orthogonal projector. Each diagonal entry of QᵀPQ lies between zero and one and their sum is two. Dividing those entries by two gives the stated conditions. The substantive step is showing those conditions are sufficient for one common Q.

Take any proposed θ and put d_i=2θ_i. Then 0≤d_i≤1 and ∑d_i=2. We first find four planar vectors of lengths d_i summing to zero. A completely elementary construction uses pairs. The possible length of the sum of two planar vectors of lengths d_1,d_2 is the interval [|d_1−d_2|,d_1+d_2], including degenerate zero lengths. The analogous interval for d_3,d_4 intersects it.

To verify intersection, each lower endpoint is no larger than its own upper endpoint. It is also no larger than the other pair's upper endpoint: for example |d_1−d_2|≤d_3+d_4 follows from max(d_1,d_2)≤1 and total length two. The same argument applies to the other pair. Choose a common resultant length R in the intersection, orient the first pair to sum to (R,0), and the second pair to sum to (−R,0). Their four vectors then sum to zero. The usual triangle construction realizes any resultant in each closed interval, including collinear and zero cases.

Write these vectors as d_i(cos2φ_i,sin2φ_i), choosing arbitrary φ_i when d_i=0. Define two real four-vectors

x_i=√d_i cosφ_i,  y_i=√d_i sinφ_i.

The zero sum gives ∑d_i cos2φ_i=∑d_i sin2φ_i=0. Together with ∑d_i=2, the double-angle identities imply ∑x_i²=∑y_i²=1 and ∑x_iy_i=0. Thus x and y are orthonormal. The rank-two projector P*=xxᵀ+yyᵀ has diagonal d_i.

Complete x,y to an orthonormal basis of R⁴. Since any two rank-two orthogonal projectors are related by an orthogonal change of basis, there is Q with QᵀPQ=P*. This can be seen directly by mapping an orthonormal basis of the range and kernel of P* to corresponding bases for P. Consequently the source's variance-share formula gives exactly θ_i=d_i/2 for all four labels under that same rotation. Sufficiency is proved, including all boundary points.

For example (1/2,1/2,0,0) and (1/2,1/4,1/4,0) are feasible, while any proposed share above one half is impossible. Combining coordinate intervals independently remains wrong, but in this spectral case adding the sum constraint is sufficient; that sufficiency has now been proved rather than inferred from coordinate bounds.

The result concerns a stated rank-two equal-eigenvalue restriction and unrestricted rotations. It does not assign economic identities to shocks, cover unequal eigenvalues, or establish cross-horizon feasibility when separate response matrices impose linked restrictions. Those limits preserve the source's distinction between algebraic attribution and empirically justified identification.

Source: [ECON-E32-502-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/53/prb_53906ac9093245f883f6e6c43f849038/contributions/con_0bc7f3f21d0c44519dc21b94a0d2197a/files/E32-502.tex), canonical revision rev_cd96b9931e6a416a8cdb36faeaaaff95. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
