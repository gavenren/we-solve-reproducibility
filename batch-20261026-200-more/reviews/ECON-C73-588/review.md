# Exact run-window revision distributions require temporal dependence information

The source's Sharp correction for the forward-looking window correctly distinguishes a successful window's starting date from its later confirmation. A further exact benchmark clarifies how much temporal structure is needed to predict that target beyond observed follow-up.

Set τ=0 and assume the binary criterion indicators c₀,c₁,… are independent with a common success probability p∈(0,1). This is an additional stochastic assumption about observed belief agreement, not a consequence of latent absorption. Fix a required run length w≥1, and let N be the number of observations, counted from c₀, needed to see the first run of w ones. The source's starting-date target is R=N−w.

Construct a transient matrix Q on streak states k=0,…,w−1. From each k, a zero sends the streak to zero with probability 1−p; a one sends it to k+1 with probability p when k<w−1, and from w−1 a one exits to the absorbing confirmed-run state. Then
P(N>n)=e₀ᵀQⁿ1 for n≥0,
and P(R≤H)=1−e₀ᵀQ^(H+w)1 for integer H≥0.
To prove it, the state records the trailing number of consecutive ones before the next observation. A path remains transient through n draws exactly when no qualifying run has been confirmed. The second identity uses N=R+w, so its exponent includes the w−1 future observations needed to confirm a window starting at H. This agrees with the source's censoring diagnosis.

The exact expected starting date is
E R=(1−p^w)/[(1−p)p^w]−w.
For derivation let E_k be the expected additional draws to confirmation from current streak k, with E_w=0. Conditioning on the next draw gives E_k=1+pE_{k+1}+(1−p)E₀. Iterating backward yields
E₀=(1+(1−p)E₀)∑_{j=0}^{w−1}p^j.
Since 1−(1−p)∑p^j=p^w, this solves to E₀=(∑p^j)/p^w. A block of w independent observations is all ones with probability p^w>0; disjoint blocks bound the waiting tail geometrically, ensuring finiteness and justifying the expectation calculation. Subtract w to obtain E R.

At w=1 this reduces to E R=(1−p)/p, the mean first-success index when dates start at zero. As p→1 it tends to zero; at p=0 no successful run exists and R is infinite. These checks prevent confusing starting dates with confirmation counts.

Marginal criterion probabilities alone cannot identify this law. Compare the iid benchmark with c_t=U at every date for a single Bernoulli(p) variable U. Both have P(c_t=1)=p at every date. In the latter model R=0 with probability p and R=∞ otherwise, so mean R is infinite when p<1. Under iid rounds it is finite. Thus even perfectly estimated cross-sectional belief-agreement rates do not establish a revision-window distribution without temporal dependence restrictions.

This is an observable-window calculation, not evidence that minds switch discrete models. It retains the prespecified criterion and makes independence transparent; correlated strategic histories or probe effects require a larger state process.

Source: [ECON-C73-588-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b5/prb_b5d1a6810d3a42f2934b8dc94eab5e88/contributions/con_43026d08fa86427697697b71a74514d2/files/C73-588.tex), canonical revision `rev_de10302139e6430697be843278d0a525`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`. The full manuscript and contribution.yaml were read. This is an independent mathematical extension within the stated benchmark; external references and empirical validity have not been independently verified. No human or formal verification is claimed.

Original prose: CC BY 4.0. Author: /root/new200_d. Model: gpt-6.1-sol; reasoning effort: ultra; exact serving build unknown.
