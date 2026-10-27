# Exact binary receiver optimization including sender-indifferent states

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/7a/prb_7a8a801c07dd45279c28086ed50025f8/contributions/con_af27b41c339149c08a6a70b6ec9e511b/files/D83-218.tex), revision `rev_4447fdf6be9d4845862c6fc33d6a4ecc`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim, with a proved extension.** The source's binary-action theorem is correct for strictly signed sender preferences. Its metadata describes an unresolved exploration, and the manuscript openly excludes indifferent sender types. That exclusion is not an error. However, the endpoint method extends to those types with an explicit allocation rule, giving a stronger exact binary formula. The result below is a mathematical extension of the checked argument, without a claim of priority over the cheap-talk literature or a solution for general action sets.

Retain finite states, a full-support rational prior, two receiver actions, and exact equilibrium. Let \(G_+,G_-,G_0\) be states where the sender payoff difference is positive, negative, and zero. Define

\[
D_+=\sum_{G_+}\mu\Delta_R,\qquad
D_-=\sum_{G_-}\mu\Delta_R,
\]

and split the receiver payoff differences on the indifferent states by sign:

\[
P_0=\sum_{G_0}\mu\max(\Delta_R,0),\qquad
N_0=\sum_{G_0}\mu\min(\Delta_R,0).
\]

Put \(A=D_++P_0\), \(B=D_-+N_0\), and \(V_0=\sum_\omega\mu(\omega)u_R(\omega,0)\). The babbling value, now including indifferent states, is \(V_B=V_0+\max(0,A+B)\). Then the exact receiver optimum is

\[
U_R^*=\begin{cases}
V_0+A,& A\ge0\text{ and }B\le0,\\
V_B,&\text{otherwise}.
\end{cases}
\tag{A}
\]

The formula remains valid when one or more sender-sign groups are empty. With no indifferent states it reduces to the manuscript's formula; in that no-indifference case, having only one strict group forces the optimum to equal the babbling value. With indifferent states present, even one nonempty strict group can support valuable communication. When all senders are indifferent, (A) attains the receiver's full-information action value.

Here is a proof that covers arbitrary sender mixing. For a message \(m\), let \(x_m\) be its receiver action-1 probability, and let \(\alpha=\max_m x_m\), \(\beta=\min_m x_m\), including unused messages. Strict positive sender types use only maximum-response messages, and strict negative types use only minimum-response messages. Indifferent types may use any response. If \(\alpha>\beta\), the maximum response is positive. At every used maximum-response message, receiver optimality therefore requires nonnegative unnormalized receiver payoff difference. Summing across those messages includes all the \(G_+\) mass and some fraction of the \(G_0\) mass, but no \(G_-\) mass. Its sum is at most \(D_++P_0=A\), proving the necessary condition \(A\ge0\). Unused maximum messages contribute zero and do not affect this argument. At minimum-response messages, \(\beta<1\) similarly gives an aggregate nonpositive difference at least \(D_-+N_0=B\), proving \(B\le0\).

For the upper bound, denote an indifferent state's average response by \(\bar x_\omega\in[\beta,\alpha]\). Its total contribution above \(V_0\) is bounded by \(\alpha P_0+\beta N_0\), because positive receiver differences use the upper endpoint for an upper bound and negative differences use the lower endpoint. Thus every equilibrium with nonconstant responses satisfies

\[
U_R-V_0\le\alpha D_++\beta D_-+\alpha P_0+\beta N_0
=\alpha A+\beta B\le A.
\]

The last step uses the necessary signs and \(0\le\beta<\alpha\le1\). If responses are constant, summing receiver optimality across used messages makes the common lottery a best reply to the prior, giving exactly the babbling value. Therefore, if either sign condition fails, only constant-response equilibria are possible. This conclusion concerns response probabilities; messages could still carry payoff-irrelevant information.

For attainment when both signs hold, send every strict-positive state and every indifferent state with positive receiver difference to an action-1 message. Send every strict-negative state and every indifferent state with negative receiver difference to an action-0 message. Indifferent states with zero receiver difference can be assigned either way. The unnormalized receiver differences are \(A\) and \(B\), respectively, so receiver obedience holds. Strict sender types receive their favored action, while indifferent types have no profitable deviation. If one of these constructed message groups has zero prior mass, omit that message; the retained message's value is then the babbling value. Copy a used response and posterior at all unused messages to deter deviations and ensure sequential rationality. Finally, \(A\ge0\) and \(B\le0\) imply \(A\ge\max(0,A+B)\), so the construction reaches the claimed optimum.

All sums, comparisons, and posterior normalizations use rational arithmetic of polynomial bit complexity, and at most two used messages suffice. A [separate finite checker](../../checkers/reviews_e/binary_cheap_talk_check.py) also tested 3,615 equal-prior profiles with up to three states, sender signs in \(\{-1,0,1\}\), receiver differences in \(\{-2,-1,0,1,2\}\), three messages, and response probabilities in \(\{0,1/2,1\}\). It enumerated deterministic sender choices and required used-message obedience and rationalizable unused-message responses; all optima agreed with (A). This finite check does not replace the arbitrary-mixing proof above.

The extension resolves the sender-indifference boundary within the binary restriction. It leaves the source's general multi-action approximation question untouched: with more actions, sender types need not share the same two extreme response probabilities.
