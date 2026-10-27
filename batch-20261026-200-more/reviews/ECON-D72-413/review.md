# Sharp population polarization bounds for binary scores

The manuscript correctly warns that pairwise opposite-quantile extrema cannot generally be combined into a joint population distribution. For binary scores with a common known marginal, that joint problem can be solved exactly for every population size. The answer includes a finite-population lattice correction.

Let \(n\ge2\), \(X_i\in\{-1,1\}\), and suppose every individual has known mean \(\mu\in[-1,1]\). No restriction is placed on dependence within the fixed population. Define \(S=\sum_iX_i\). The source's index simplifies to
\[
\Pi=\frac{2(n^2-S^2)}{n(n-1)},\qquad E[S]=n\mu.
\tag{A}
\]
Indeed \(\sum_iX_i^2=n\), and expanding all ordered squared differences gives \(2n\sum_iX_i^2-2S^2\).

For \(-1<\mu<1\), let \(s_-\) be the largest point of the grid
\(\{-n,-n+2,\ldots,n\}\) not exceeding \(n\mu\), put \(s_+=s_-+2\), and write
\[
\theta=(n\mu-s_-)/2\in[0,1).
\]
Then the exact interval of expected polarization is
\[
0\le E[\Pi]\le
\frac{2\{n^2-(1-\theta)s_-^2-\theta s_+^2\}}{n(n-1)}.
\tag{B}
\]
The endpoints \(\mu=\pm1\) force every score to that constant and give the singleton zero.

To prove the upper bound, let \(L(s)\) be the affine function interpolating \(s^2\) at \(s_-\) and \(s_+\). For any permitted grid point,
\[
s^2-L(s)=(s-s_-)(s-s_+)\ge0,
\]
because there is no grid point strictly between the adjacent endpoints. Taking expectations and using \(E[S]=n\mu\) yields
\[
E[S^2]\ge(1-\theta)s_-^2+\theta s_+^2.
\]
Equation (A) proves the proposed upper bound without making inconsistent assumptions about separate pairs.

It is attained by a single joint coupling. Draw \(S=s_-\) with probability \(1-\theta\) and \(S=s_+\) with probability \(\theta\). Conditional on \(S=s\), choose uniformly a subset of \((n+s)/2\) people to receive score \(+1\), assigning \(-1\) to everyone else. Symmetry gives
\[
E[X_i\mid S=s]=s/n,\qquad E[X_i]=\mu
\]
for every individual. Thus every required marginal is exactly respected, and the lower second-moment bound is achieved.

For the lower polarization endpoint, let all scores equal a common binary variable with mean \(\mu\). Then \(S=\pm n\) and \(\Pi=0\). Mixtures of this comonotone coupling and the maximizing coupling preserve every marginal and attain all values between the endpoints. This establishes the whole interval's sharpness, not merely valid outer bounds.

The upper endpoint can also be written
\[
\frac{2n}{n-1}(1-\mu^2)
-\frac{8\theta(1-\theta)}{n(n-1)},
\tag{C}
\]
because the optimal second moment is \(n^2\mu^2+4\theta(1-\theta)\). The correction disappears only when the required mean total lies on the score grid.

For symmetric marginals \(\mu=0\), the maximum equals \(2n/(n-1)\) for even \(n\), attained by exactly balanced scores in every realization. For odd \(n\), it equals \(2(n+1)/n\), attained by alternating the two closest-to-balanced totals \(-1\) and \(+1\). With three people the maximum is \(8/3\), strictly below the infeasible pairwise maximum four. With two people the formula recovers the manuscript's sharp opposite-score construction.

If treated and baseline regimes each satisfy this subclass and their cross-regime dependence is unrestricted, their expected-polarization contrast has the interval obtained by subtracting the two sharp intervals. Independent coupling across the two policy worlds attains the endpoint combinations.

This result addresses joint outcome coupling, not assignment identification. It does not identify a population-wide platform intervention from individual exposure experiments, validate ideological scores, or solve arbitrary nonbinary heterogeneous marginals. It adds a fully solved population subclass to the source's stated joint-feasibility gap.

Source: [ECON-D72-413-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/d0/prb_d0c62970727042b093fc1702d0b9af3b/contributions/con_9eed3d9a64bb439b97cc11144499bc0f/files/D72-413.tex), canonical revision `rev_4e3510c43b9345a8864b2259176ee4fb`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
