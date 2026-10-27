# Endogenous home and haven rates have a unique interior tax-game equilibrium

The source holds the haven rate fixed while deriving incidence. If both jurisdictions instead maximize their own corporate receipts, its same shifting technology yields a fully solved tax game. This is a restricted strategic extension; no real production or household-demand response is added.

Retain fixed operating rent \(\Pi>0\), quadratic real shifting cost \(ks^2/2\), and the convention that shifting cost is not tax-deductible. Governments simultaneously choose rates \(t,h\in[0,T]\), where \(T>2k\Pi/3\). The firm then chooses
\[
s(t,h)=[(t-h)/k]_0^\Pi.
\]
The home government maximizes \(t(\Pi-s)\), and the haven maximizes \(hs\). No exit option, administrative cost or government utility from household income is added. Under these explicit objectives, the unique Nash equilibrium is
\[
t^*=\frac{2k\Pi}{3},\qquad h^*=\frac{k\Pi}{3},\qquad s^*=\frac\Pi3.
\]

First verify global best responses at this candidate. Holding \(h^*=k\Pi/3\), home receipts equal \(t\Pi\) for \(t\le h^*\), then the strictly concave quadratic \(t[\Pi-(t-h^*)/k]\) while shifting is interior, and zero after full shifting. The quadratic's maximum is \(t=(k\Pi+h^*)/2=2k\Pi/3\), strictly above the first branch's boundary value. It belongs to the allowed rate interval and has interior shifting. Holding \(t^*=2k\Pi/3\), the haven's positive-receipt region is \(0<h<t^*\), where receipts are \(h(t^*-h)/k\); its unique maximizer is \(h=t^*/2=k\Pi/3\). Rates at or above \(t^*\) yield zero. Thus both best responses are global.

For uniqueness, any equilibrium must have \(t>0\). At \(t=h=0\), home can earn positive receipts by a small positive tax; if \(t=0<h\), it can choose any rate in \((0,h]\) and collect positive receipts without shifting. Nor can \(h=0<t\) be an equilibrium: the haven can choose a sufficiently small positive rate below \(t\), receiving positive receipts on a positive shifted base. If \(h\ge t>0\), the haven likewise earns zero and can deviate below \(t\) for positive receipts. Thus \(0<h<t\). Full shifting cannot occur in equilibrium: home receipts would be zero, while setting \(t=h\) yields \(h\Pi>0\). Therefore shifting is interior.

The haven is not at its rate cap, since \(h<t\le T\), and its interior first-order condition gives \(h=t/2\). If home were capped at \(t=T\), its one-sided derivative would be \(\Pi-(2T-h)/k=\Pi-3T/(2k)<0\), contradicting optimality because reducing the rate would increase receipts. Hence home is also interior, and its first-order condition is \(t=(k\Pi+h)/2\). Solving the two equations gives the unique candidate above. Possible clipping thresholds have already been excluded, so the first-order argument omits no equilibrium.

The accounting remains consistent. Equilibrium home and haven receipts are respectively \(4k\Pi^2/9\) and \(k\Pi^2/9\). Real shifting cost is \(k\Pi^2/18\). Adding owner income and both receipts gives
\[
U+R_H+R_F=\Pi-\frac{k\Pi^2}{18}.
\]
Transfers cancel, leaving the real avoidance loss. If rates are coordinated to equality, shifting disappears and this global resource total becomes \(\Pi\), regardless of the common rate under the no-exit convention. This does not say the governments' separate receipt objectives coincide with equal-weight welfare.

When \(T\le2k\Pi/3\), the cap changes the game and the interior result above is not claimed. Likewise a minimum tax, deductibility, mobile investment or household recycling alters best responses.

Checked locations: pure shifting model (1), equations (2)–(4), and boundary discussion. Full source/YAML were read. This is an exact finite tax-game extension, not a description of current legislation or empirical tax competition. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-H22-444-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/d2/prb_d2f00ce493b24be3b78e71ce878435b4/contributions/con_ac485ef1b3ac4c1384f472e12eba63a6/files/H22-444.tex). Canonical revision: `rev_4310edbe925e4a8ca4820b2f7f2cdbb8`.

