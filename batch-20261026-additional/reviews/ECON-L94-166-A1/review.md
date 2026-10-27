# An exact multi-interval loss characterization strengthens the storage diagnostic

**Finding: Supports the claim.** The zero-loss storage criterion and its explicit periodic construction are correct under the declared ideal-storage assumptions. The lower bounds allowing unserved load are valid but deliberately necessary only. A useful independent check is an exact deterministic minimum-loss characterization that includes multiple separated deficit intervals. It explains how loose the single worst-interval lower bound can be without contradicting the manuscript.

I read the full contribution metadata and manuscript. The record is exploratory and unresolved. The manuscript clearly fixes generation, assumes cyclic initialization, grants no charge/discharge power limit and unit efficiency, and distinguishes physical adequacy from investment equilibrium. These are part of its stated model, not unacknowledged gaps.

First, the sufficiency recurrence is sound. With total deficit \(D\le0\), the additional length-\((n+1)\) suffix introduced by \(m_{t-1}+d_t\) equals \(D+d_t\le d_t\), so it cannot increase the maximum. Hence \(m_t=(m_{t-1}+d_t)_+\), which gives the stated balance and curtailment. The curtailment bound uses nonnegative load, as required. This also covers a zero total deficit, atoms in a random chronological law, and \(n=1\).

For an independent extension, let \(g_t=r_t+f_t\ge0\), keep the cyclic ideal-storage physics, and minimize total unserved energy over deterministic dispatches. For a subset \(S\) of the \(n\) hours, let \(c(S)\) count the directed cyclic edges entering \(S\) from its complement. Thus \(c(S)\) is the number of contiguous components when \(S\) is nonempty and proper, while \(c(\varnothing)=c(\{1,\ldots,n\})=0\). Then the exact optimum is
\[
 L_{\min}(E)=
 \max_{S\subseteq\{1,\ldots,n\}}
 \left\{\sum_{t\in S}d_t-Ec(S)\right\}.
 \tag{A}
\]
The empty subset ensures nonnegativity. In particular the full subset contributes total net deficit without a storage deduction.

To prove (A), construct a time-expanded directed network. A source has an arc of capacity \(g_t\) into hour \(t\); hour \(t\) has an arc of capacity \(\ell_t\) to a sink; and a storage arc of capacity \(E\) goes from hour \(t\) to its cyclic successor. Flow on the load arc is served load, and flow on the storage arc is the inventory \(s_t\). Unused generation is curtailment. Conservation gives exactly the manuscript's cyclic inventory balance with unserved load \(u_t=\ell_t-\text{served}_t\). Conversely every physical dispatch supplies such flows, after ignoring any gratuitous simultaneous curtailment and nonuse. All arc capacities are finite, so maximum flow exists.

For a source–sink cut, let \(S\) be its hour nodes on the sink side. The cut capacity is
\[
 \sum_{t\in S}g_t+
 \sum_{t\notin S}\ell_t+Ec(S).
\]
The maximum-flow/minimum-cut theorem therefore gives maximum served energy as the minimum of this expression. Subtracting from \(\sum_t\ell_t\) yields (A). This is an application of standard network-flow theory, offered as a verification and sharpening rather than a novelty claim.

The manuscript's bounds are recovered by choosing \(S\) to be the full cycle or one proper contiguous interval. Formula (A) permits a union of several intervals. For example, take four hours with load one, generation \((0,2,0,2)\), hence deficits \((1,-1,1,-1)\), and \(E=0\). The manuscript's maximum interval deficit is \(M=1\), so its displayed lower bounds give \(L\ge1\). Actual minimum loss is two: both zero-generation hours are entirely unserved. Choosing \(S=\{1,3\}\) in (A) gives two and proves exactness. More generally, repeating \(m\) separated deficit/surplus pairs at zero storage gives a single-interval bound of one and total loss \(m\). Thus the lower bound's potential looseness grows with repeated episodes.

Setting \(L_{\min}(E)=0\) in (A) also independently recovers the zero-loss criterion. The full-set cut requires total deficit at most zero; each proper interval requires deficit at most \(E\). Every proper subset decomposes into disjoint cyclic intervals, so those interval inequalities imply all the remaining cuts. This independently certifies both necessity and sufficiency of the manuscript's capacity formula.

The extension remains deterministic and cyclic. Applying its optimum scenario by scenario is a necessary lower bound for a nonanticipative operator, not permission to optimize dispatch with unknown future weather. Neither it nor the manuscript establishes an endogenous resource-cost ranking of market designs. The chronology example correctly proves nonidentification from marginal hourly laws and annual energy alone.

**Source reviewed:** [L94-166.tex at the pinned revision](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/0a/prb_0afa49671938424d9c88a5806c8fd231/contributions/con_21cfd9c57032456a8f14a00fb09a6ffd/files/L94-166.tex). Contribution revision: rev_deb9e89320ea44148acc62d9bdec7b08. No empirical adequacy or full-grid equilibrium claim is assessed.

