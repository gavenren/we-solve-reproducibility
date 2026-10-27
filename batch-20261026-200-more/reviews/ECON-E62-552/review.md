# Sharp population-multiplier bounds from a local complier ratio

The source correctly shows that instrument ratios average spending responses among compliers rather than the population. A bounded-response information model yields an exact population-multiplier interval, making the required transport restriction quantitative.

Fix a predetermined state and the source's monotone binary encouragement design. Let the identified complier share be π∈(0,1], the complier mean spending response be g_C>0, and its spending-weighted multiplier be M_C. Thus complier mean output response is g_CM_C. Consider the population ratio EΔY/EΔG under the same treatment intervention, not a change in the instrument itself.

For noncompliers impose 0<g_L≤ΔG≤g_U<∞ and ΔY=ΔG m with m∈[m_L,m_U]. Assume M_C also belongs to that interval. For the following sharpness statement, the information retained is precisely these complier summaries and the stated noncomplier response restrictions; no additional full-outcome-law or level restrictions are imposed. Such additional observations can tighten the resulting set.

Let a=πg_C and b=(1−π)E[ΔG|not C]. The population multiplier has the form

M=(aM_C+bM_N)/(a+b),

where M_N=E[ΔG m|not C]/E[ΔG|not C] lies in [m_L,m_U] by positive spending weights. Also b∈[(1−π)g_L,(1−π)g_U]. Denote the largest admissible missing spending mass by b_U=(1−π)g_U.

For every fixed b, the ratio is increasing in M_N. Since m_L≤M_C≤m_U, its minimum at M_N=m_L decreases as b increases, while its maximum at M_N=m_U increases as b increases. Therefore the exact identified interval is

[(aM_C+b_Um_L)/(a+b_U),
 (aM_C+b_Um_U)/(a+b_U)].

The lower spending bound drops out of these extrema because greater unobserved spending mass can pull the population ratio farther toward either missing-response endpoint. This conclusion would need modification if the complier multiplier were outside the maintained ratio range.

Both endpoints are attained by assigning every noncomplier ΔG=g_U and m respectively m_L or m_U. To attain every intermediate ratio, hold their spending at g_U and choose any common m between those endpoints. Draw the monotone treatment-response types with the identified complier mass, choose the specified complier mean contrasts, and assign encouragement independently. These constructions realize the summarized information model and prove full-interval sharpness. They are not a claim that every construction preserves arbitrary extra observed outcome distributions.

The interval gives an immediate positive-sign certificate: the population multiplier is strictly positive in every admitted model exactly when aM_C+b_Um_L>0. If the lower expression is zero, zero remains feasible. If π=1, b_U=0 and the interval collapses to M_C. As the complier spending mass becomes small relative to b_U, the interval approaches the unobserved ratio range and the local estimate has little power to determine the population response.

For an exact example, set π=1/5, g_C=1, M_C=3, g_U=2 and [m_L,m_U]=[−1,4]. Then a=1/5 and b_U=8/5, giving population interval [−5/9,35/9]. A valid positive instrument-local multiplier of three is compatible with a negative population multiplier even under positive spending effects for everyone. The ambiguity comes from unobserved output responses and spending weights, not weak first-stage ratio inference.

These bounds supplement the source's composition counterexample. They do not solve national-versus-regional monetary and financing differences, identify the missing-response bounds, or replace denominator-aware statistical inference. They quantify exactly what a particular explicit transport assumption adds, with no empirical multiplier or external novelty claim.

Source: [ECON-E62-552-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/2a/prb_2a9e91cf302b41228747c2a0ea05f64a/contributions/con_11efd7aea6ef49c2880c26015e5daa94/files/E62-552.tex), canonical revision rev_61cb87b78a7545838baa7a688095e904. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
