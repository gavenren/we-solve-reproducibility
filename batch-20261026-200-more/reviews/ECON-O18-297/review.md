# An exact Pareto-financing frontier with heterogeneous expenditure shares

The manuscript's common-expenditure-share assumption makes unit-weight equivalent variation depend only on total income and project cost. Allowing heterogeneous expenditure shares preserves its equilibrium logic but changes the financing problem. One can then solve exactly how much real project cost can be financed while making every household weakly better off.

Keep the two competitive technologies X=A_z L_X and Y=B L_Y, perfect labor mobility, fixed labor endowments L_i>0, and Y as numeraire. Replace the common θ by household-specific θ_i∈(0,1). Baseline project cost is zero. Let the policy raise productivity by r=A_z/A_0≥1 and require C≥0 units of Y. The regulator can allocate nonnegative lump-sum tax amounts τ_i summing to C. Require τ_i<BL_i so that private incomes remain positive. These are tax amounts rather than fixed tax shares; for C>0 they correspond to t_i=τ_i/C.

Both goods have positive private demand, so zero profit still gives w=B and p_z=B/A_z. Individual incomes are BL_i−τ_i. Goods demand uses household-specific shares, but labor clearing continues to hold: electrical production employs ∑θ_i(BL_i−τ_i)/B, and other production employs ∑(1−θ_i)(BL_i−τ_i)/B+C/B. These sum to L. Thus changing the tax allocation does not invalidate the proposed price closure.

Household i's indirect utility has its own Cobb–Douglas constant times income times p^−θ_i. At baseline prices its exact equivalent variation is therefore

EV_i=(BL_i−τ_i)r^θ_i−BL_i.

Consequently EV_i≥0 precisely when

τ_i≤g_i:=BL_i(1−r^−θ_i).

For r>1 every g_i lies strictly between zero and BL_i. A nonnegative tax vector making all households weakly better off exists if and only if

C≤G(r):=∑g_i.

Necessity follows by summing the household inequalities. For sufficiency, if G>0 choose τ_i=Cg_i/G. These taxes sum to C, satisfy τ_i≤g_i, and keep every income strictly positive. The case r=1 gives G=0, so only the costless project is Pareto feasible. At C=G and r>1, the only Pareto-feasible taxes are τ_i=g_i and every equivalent variation equals zero; if C<G, the proportional construction gives every household a strict gain.

This is a sharp feasibility frontier, with all boundary cases explicit. It does not rely on a transferable-utility interpretation of aggregate equivalent variation. The available tax instruments are nonnegative lump-sum charges with no extra redistribution payment or administrative cost.

Positive unit-weight aggregate equivalent variation under a particular financing rule does not imply that some rule makes everyone gain. For an exact example, take two households with BL_1=BL_2=1, r=4, θ_1=1/2, and θ_2=log3/log4. Then r^θ_1=2 and r^θ_2=3, so G=1/2+2/3=7/6. Choose C=6/5>7/6, making Pareto financing impossible. Nevertheless taxes τ_1=9/10 and τ_2=3/10 are feasible and give

EV_1=−4/5,   EV_2=11/10,   EV_1+EV_2=3/10>0.

This does not contradict the frontier: the sum uses household-specific conversion factors r^θ_i, while the resource constraint sums unweighted taxes. Moving the financing burden changes that money-metric sum. With a common θ, by contrast, the condition C≤BL(1−r^−θ) coincides with nonnegative unit-weight equivalent variation, recovering the manuscript's formula.

The result supplies an exact incidence and financing comparison under a broader preference subclass. It does not estimate electrification benefits, allow distortionary taxes, or address migration, reliability, network rationing, distributional weights or alternative welfare measures. Those limitations remain substantive, and the review does not certify the source's external reference.

Source: [ECON-O18-297-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b6/prb_b6c985be7e2b45819b3ee97d6ad540aa/contributions/con_92ee28185bbb47549488c46d6d9d869e/files/O18-297.tex), canonical revision rev_835c80d2211f4fda8aa1b6c024f8f397. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
