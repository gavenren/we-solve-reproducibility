# We-Solve reproducibility programs

This payload contains the unchanged Python verification programs for 32 pending contributions from the reviewed 200-contribution batch. The selected source bytes match both the frozen input hashes and the successful recorded main-instance runs. Separate LLM audits bind those same program hashes. The programs were not rerun during this payload assembly.

The scope listed for each handle belongs to its associated report. A program checks the finite cases, identities or witnesses described in its recorded verification summary; passing a bounded check does not prove an unrestricted or infinite claim. The original reports supply their proofs and credit imported results. These records do not claim human peer review, formal proof verification or editorial acceptance.

## Run and identify a program

Use Python 3.13 or a compatible Python 3 installation. All imports in these files are from the Python standard library. Run the command listed for a handle from the repository root, with normal assertion checking enabled. The programs reject optimization mode, so do not pass `-O`. Each command below refers to the exact source bytes identified by its SHA256.

Two programs also write their own output beside their source: `TOP-9400104/verify.py` writes `tunnell_counts.json`, and `TOP-30007005/verify_tensor_squares.py` writes `verification.json`. Those generated outputs are not included in this prepared source payload.

`manifest.json` records each original source path, SHA256, author, separate reviewer, associated scope, and historical run record. `SHA256SUMS` covers every payload file except itself. For durable public references, use the actual uploaded commit identifier together with the source hash; no commit identifier is assigned or assumed in this preparation.

## Credits, model disclosure and license

Gaven (`@gavenren`) prompted the batch and its publication. The frozen contribution records identify the authoring LLM instances and the separate reviewing instances. Author identifiers in this selected code set are:

- `/root/hundred_algebra`: 1 program(s).
- `/root/hundred_algorithms`: 23 program(s).
- `/root/hundred_geometry`: 4 program(s).
- `/root/hundred_numbers`: 4 program(s).

Historical author/reviewer roles and original model disclosures remain as recorded. The submitting user additionally requested the following model attribution; it supplements the prior disclosure and does not independently establish runtime configuration:

User-specified model attribution (19 October 2026):
Model: GPT-6.1 Sol
Reasoning level: Ultra
Source: the submitting user's explicit instruction on 2026-10-19. Runtime model and reasoning settings were not independently verified.
This supplements the original disclosure. The recorded author/reviewer roles and historical provenance above remain unchanged; this label does not retrospectively verify the configurations used for the earlier work.

The original software is licensed under Apache License 2.0; `LICENSE` is an exact copy of the original software license accompanying all 32 source files. Each source preserves its Apache-2.0 SPDX header. The original report scopes and other original contribution prose retain their CC BY 4.0 attribution and credited scientific sources; consult the per-handle author and checked-reference records in `manifest.json`. No third-party research paper is redistributed.

## Programs, commands and source hashes

| Handle | Command from repository root | SHA256 |
|---|---|---|
| TOP-9400095 | `python3 TOP-9400095/verify.py` | `bebba35b9623167d99b164b445288b080db888e32e63d0fa09f5164cccaf9bc7` |
| TOP-9400104 | `python3 TOP-9400104/verify.py` | `45538a9c55e6e0ec7b4cc22f5af9bb49a013cef1bb9591a1d6a581152a1e3429` |
| TOP-9400141 | `python3 TOP-9400141/verify.py` | `ccf21c58b3e87537ea8959c58066204db4bd3345b8af5d9b56cd40268a49d69a` |
| TOP-30000423 | `python3 TOP-30000423/verify.py` | `dbe0a87b793be9edb08ac19ce4cf263d7f568b88908bb618b6527c89921ba662` |
| TOP-30000608 | `python3 TOP-30000608/verify.py` | `5cc06dbff01d98cd58d6fe40aa4bb8c25312ffb9c40cb381f4e8877e30ffe96e` |
| TOP-30000784 | `python3 TOP-30000784/verify.py` | `5d2fc84ed14b4c2dd9e278a6845ee4485c3523d2613080415d70ab93bb081138` |
| TOP-30001930 | `python3 TOP-30001930/check_exact.py` | `a528ff954c25539c79d066bbc82b408369ce5b5b6c0ecbe1622400b4a341f168` |
| TOP-30001933 | `python3 TOP-30001933/check_exact.py` | `330f996d5dd4ed1c6a35d3d112c180222762c0755613e2386920b04399f44511` |
| TOP-30001934 | `python3 TOP-30001934/verify.py` | `2e4caa5028b86edc662b3ee195cf62f6c97ffbcae81aa07e5a159205cd7ea9dd` |
| TOP-30002722 | `python3 TOP-30002722/verify.py` | `8e3320ffb15f690b699c3f2e78659a8692fbfa6569ff2f341a84e1aaa31e2af0` |
| TOP-30003997 | `python3 TOP-30003997/verify.py` | `f7e86ad34b08d0530eabf8d58724e467f1f52a6ca4684b929a62aeb3c68ac0b1` |
| TOP-30004015 | `python3 TOP-30004015/verify.py` | `7f96ac040a065c7e3f979f520d8bf935b5b2032491e8a5457bc1044abfba1f0b` |
| TOP-30004130 | `python3 TOP-30004130/verify.py` | `c262611a26cb9350a6e39868448871915f0e6aa4553823a2b7935bc8008c8a17` |
| TOP-30004864 | `python3 TOP-30004864/verify.py` | `3e48f57a1c63c64a65113ed6922fb27f6f289ceb98543c034d6832f2623a6d17` |
| TOP-30004909 | `python3 TOP-30004909/verify.py` | `b4cacf04560e53faebe7b44917ef8519dc98f4ab9f4e9c1539deb37e7603b080` |
| TOP-30004912 | `python3 TOP-30004912/verify.py` | `6d904b162c84344fc71b978773b8a0894d87bc650e94b8b071b87f82aff72747` |
| TOP-30004914 | `python3 TOP-30004914/verify.py` | `fe5eec414ccfe5708d6acd070b69fbb05915b394088dc2fdec9d76ac7df587c3` |
| TOP-30005977 | `python3 TOP-30005977/verify.py` | `185d95e1073451d2d4130ceb48c5e5f3a67fccd56586565098d030aed8dbed75` |
| TOP-30006105 | `python3 TOP-30006105/check_exact.py` | `fb890b68ca4b1f96b346b93d16e732f8311930b82caea57ced72b76cf5a3e6d1` |
| TOP-30006109 | `python3 TOP-30006109/verify.py` | `1b5a0074a98797897da53d5c88fd0fec91c9ded2eae77656f3703321d011e41f` |
| TOP-30006760 | `python3 TOP-30006760/verify.py` | `a841b23da04aae90b3193a5e53113cdb995258763f891a3309f70fc88ab74c2d` |
| TOP-30006781 | `python3 TOP-30006781/verify.py` | `168423b71de96f429818e65d13ef579f7d6d7ac1e1b7575819685e73f778d61d` |
| TOP-30006800 | `python3 TOP-30006800/verify.py` | `7c18b3a39790b69c4e80d75ad9efc26deae95b96b997c986c5338cc43f8f7f7d` |
| TOP-30007005 | `python3 TOP-30007005/verify_tensor_squares.py` | `bb0fa76674cbb7fa0c4d9a272155702368f44f0bc6c38bc0021ca3e2850c43d4` |
| TOP-30007113 | `python3 TOP-30007113/check_exact.py` | `707b19215cb07d2234ade410d1b52134d1e5a922a09c35a20e331b070fc84470` |
| TOP-30007441 | `python3 TOP-30007441/verify.py` | `2661640a10ed741227ac0f83fbd1ba93887d3bfd6674b602ac3138b759bc25fd` |
| TOP-30007453 | `python3 TOP-30007453/verify.py` | `36a4e3e8cac424205f6c99ee5ab5720f9445feb455296a8049380f5037654518` |
| TOP-30007460 | `python3 TOP-30007460/verify.py` | `a2dd14117bdbbf07c7d600ef8536d54ab2b6cbef8cd83111fcd3b57f1b38c08d` |
| TOP-30007461 | `python3 TOP-30007461/verify.py` | `0ddce175ccdc83937a0c74c728a38764ba2ed6701b10e9441b551c0a8220d410` |
| TOP-30007480 | `python3 TOP-30007480/verify.py` | `de887f0bb8a64c850f9c3ec55c1d71b08f385356c6bf48e11fb997db4bdca6f9` |
| TOP-30007481 | `python3 TOP-30007481/verify.py` | `e683a7ca0203a350595dacb22aa13aa8812fd9e33414e62c2c04bb58190cdd86` |
| TOP-30007486 | `python3 TOP-30007486/verify.py` | `a7811c52998b0e1af4777ac40cdfaaf8479a28e32f6e14fce72e54fe49c9c8c6` |

## Associated report scopes and recorded checks

### TOP-9400095 — Odd greedy expansions can terminate after arbitrarily many steps

Associated report scope: For every odd prime p, the odd greedy algorithm applied to 2/(2(p-1)!-1) terminates with reduced positive numerators 2,3,...,p-1,1 and therefore exactly p-1 unit fractions, by Pihko Theorem3.5. This gives an explicit unbounded-length terminating family, not universal termination.

Recorded verification: Executed verify.py for source-family primes3,5,7,11,13 using exact Fraction arithmetic. Reduced numerators and term counts2,4,6,10,12 match; exact reconstruction and the preceding-odd-denominator test verify every greedy choice. The largest tested denominator has58103 bits. The infinite family remains the credited source theorem. Standard-library exact Python, Apache-2.0 SPDX; normal run PASS and python -O rejection were executed and retained in verification.json/verification_output.txt.

### TOP-9400104 — Exact Tunnell obstructions with the conditional direction kept separate

Associated report scope: For positive squarefree n, unequal signed ternary-form counts in Tunnell’s criterion prove n is not congruent, unconditionally. Equality is only reported as a BSD-conditional converse. The attached exact counting certificate classifies these necessary conditions through5000; it does not unconditionally classify all congruent numbers.

Recorded verification: Executed verify.py for all3042 positive squarefree n<=5000, with all four signed-form counts independently checked by full signed enumeration for every0<=n<=120. Exactly1275 fail Tunnell’s necessary test;1767 merely pass it. Exact per-n evidence is tunnell_counts.json; passing is not an unconditional congruence certificate. Standard-library exact Python, Apache-2.0 SPDX; normal run PASS and python -O rejection were executed and retained in verification.json/verification_output.txt.

### TOP-9400141 — Every composite super-Wieferich candidate needs a prime factor exceeding100000

Associated report scope: For odd n>1 with p^e exactly dividing n, n^2 divides2^(n-1)-1 iff every p satisfies ord_p(2)|(n-1) and v_p(2^(p-1)-1)>=2e. Exact enumeration of all primes<=100000 then proves that any composite candidate must have a prime factor>100000. Existence of composite candidates is not settled.

Recorded verification: Executed verify.py: sieve independently matches trial primality for all integers<=100000 (9592 primes); only1093,3511 pass the Wieferich test, each valuation is2, their exact orders are364,1755, and their sole composite product fails. The local iff also agrees with direct modular exponentiation for every odd3<=n<=2001. Infinite prime-support exclusion rests on the proof. Standard-library exact Python, Apache-2.0 SPDX; normal run PASS and python -O rejection were executed and retained in verification.json/verification_output.txt.

### TOP-30000423 — Recognition and Characterization of Leaf Powers

Associated report scope: For every fixed k≥5, graphs whose quotient by equal closed neighborhoods is a forest have explicit k-leaf roots, constructible in polynomial time; the test is sufficient, not a recognition test for all leaf powers.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30000608 — Complexity of Dense Perfect Hypergraph Matching

Associated report scope: For fixed c>1/3, sufficiently large 3-uniform hypergraphs with n divisible by three and minimum codegree≥cn have a polynomial-time perfect-matching decision algorithm consisting of one explicit GF(2) linear-system test.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30000784 — Optimal Algebraic Immunity of Boolean Functions

Associated report scope: For every n≥16 and 1≤m≤n, some Boolean map f:F₂ⁿ→F₂ᵐ has graph algebraic immunity at least floor(n/16)+1; this is nonconstructive and does not prove the optimum dimension bound.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30001930 — Quadratic graph diameter for every simple graphical zonotope

Associated report scope: Every graphical zonotope of a connected simple graph on d+1 vertices, and every invertible affine image, has vertex-edge diameter at most |E| <= d(d+1)/2.

Recorded verification: Executed check_exact.py with assertions enabled: PASS 771 connected labelled simple graphs on2..5vertices; exact all-pairs orientation-graph diameters. python -O was separately executed and refused. These are finite exact checks only.

### TOP-30001933 — ICP for rooted arborescences on bidirected cactus graphs

Associated report scope: For every connected undirected cactus, replace every edge by both directed arcs. Its outward arborescence polytope at any root has ICP for every integer dilation.

Recorded verification: Executed check_exact.py with assertions enabled: PASS 400 weighted bidirected-cactus dilate decompositions; physical rooted-tree reconstruction and exact affine-rank oracle. python -O was separately executed and refused. These are finite exact checks only.

### TOP-30001934 — Greedy Decomposition of the Spanning-Tree Polytope

Associated report scope: Under the usual greedy range 0≤λ≤k, every scaled integral point of the spanning-tree polytope of K_{2,t}, t≥2, admits positive integral greedy subtraction; a polynomial-time decomposition uses at most 5t+1 steps.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30002722 — Polynomial-Time Minimization of K-Submodular Functions

Associated report scope: Explicit k-submodular functions given by admissible unary terms and nonnegative star-metric pair interactions on a tree can be minimized exactly in O(n(k+1)²) rational operations, with polynomial bit complexity.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30003997 — Hardness of Path-Cost Arborescence Optimization

Associated report scope: Distinguishing optimum zero is NP-hard for destination-specific path-cost spanning arborescences even on DAGs with indegree≤2, outdegree≤2, underlying undirected degree≤3 and only 0/1 costs.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30004015 — Subquadratic Approximation for Longest Common Subsequences

Associated report scope: For matching-position count r, an exact longest common subsequence is computable in O((n+r) log(n+2)) word operations after alphabet compression; r=n^{2−Ω(1)} gives a truly subquadratic exact regime.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30004130 — Complexity of Approximate Counting in Spin Systems

Associated report scope: For fixed q≥2 and a supplied feedback vertex set S of size k, exact rational Potts and hard-core partition functions are computable in q^k·poly(L) and 2^k·poly(L) bit time, respectively, where G−S is a forest and L is full encoded input length.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30004864 — Algorithms for Symmetry-Reduced Semidefinite Programs

Associated report scope: A rational SDP whose coefficient matrices are invariant under all simultaneous row/column permutations reduces exactly to a two-variable rational LP, allowing exact feasibility/optimality/unboundedness decisions in polynomial bit time.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30004909 — Approximating Submodular Functions by Matroid Rank Functions

Associated report scope: Every integer-valued normalized monotone submodular function with f({i})=1 is exactly a matroid rank function, so the prompt’s comparison holds with α=1 in this integral regime.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30004912 — Compact Representations of Four-Thirds Near-Mincuts

Associated report scope: Every cut of a connected nonnegatively weighted cactus with 0<λ and weight≤4λ/3 is one bridge or one pair of edges in one cycle; all such cuts have an O(n+m)-word implicit representation.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30004914 — Deterministic Optimization of Top-$k$ Perfect-Matching Edges

Associated report scope: On arbitrary graphs with two rational weight levels a<b, one polynomial-time perfect matching maximizes the sum of its k largest edge weights simultaneously for every k, including k supplied as input.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30005977 — Finite-field polynomial multiplication and integer-multiplication lower bounds

Associated report scope: For every fixed C≥1 and primes d≤p≤d^C, d≥2, degree<d polynomial multiplication over F_p takes O(d log p·log(d log p)) bit time using credited O(N log N) integer multiplication and explicit carry-free packing.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30006105 — Exact containment when the outer zonotope has fixed generator co-rank

Associated report scope: For rational full-row-rank H in Q^(d x m), centered zonotope containment is decidable in binom(m,d-1) poly(L) bit operations. With m=d+c and fixed c this is polynomial in total encoded input length L.

Recorded verification: Executed check_exact.py with assertions enabled: PASS 120 rational containment cases d1..4, outer co-rank0..2; independent cube-feasibility oracle. python -O was separately executed and refused. These are finite exact checks only.

### TOP-30006109 — Approximating Fare-Zone Assignment on Trees

Associated report scope: Exact hard-budget fare-zone optimization is NP-hard even on stars with edge congestion exactly three, all commodity weights and budgets one, and paths of length one or two.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30006760 — An explicit anticanonical count on every open subset of projective space

Associated report scope: For every n>=1 and every fixed nonempty Zariski open U in P^n/Q, with H([x])=max|x_i|^(n+1) on primitive integer coordinates, N(U,B)~2^n B/zeta(n+1), with error O_U(B^(n/(n+1))) for n>=2 and O_U(B^(1/2) log B) for n=1.

Recorded verification: Executed verify.py on32 complete integer grids: coordinate count d=2,3,4,5 and T=1,...,8. Direct gcd enumeration agrees with Möbius inversion; the sign quotient and open x0!=0 counts are integral. The asymptotic and arbitrary-open claim rest on the proof. Standard-library exact Python, Apache-2.0 SPDX; normal run PASS and python -O rejection were executed and retained in verification.json/verification_output.txt.

### TOP-30006781 — Omega(n log n) Boolean Circuit Lower Bound for Integer Multiplication

Associated report scope: For every fixed depth D≥2, unbounded-fan-in AND/OR/NOT circuits outputting exact n-bit integer products need exp(Ω_D((n/log(n+2))^{1/(D−1)})) gates; no unrestricted-depth lower bound is claimed.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30006800 — Perfect-Matching Search in Deterministic NC (General Graphs)

Associated report scope: Perfect-matching search, including the NO output, is in logspace-uniform NC² on forests, by computing edge-cut parities in parallel and verifying the resulting candidate matching.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007005 — A complete exact universal-tensor-square search through degree sixteen

Associated report scope: For every 1≤n≤16 outside {2,4,9}, an explicit irreducible S_n representation has a tensor square containing every irreducible; no such representation exists at the three excluded degrees in this finite range.

Recorded verification: Complete exact symmetric-group character tables and universal-square candidate searches passed for n=1..16; every character entry for n=1..7 also matched a separate Frobenius coefficient oracle. Hook-length degrees, full row orthogonality, integral nonnegative multiplicities and dimension sums passed. -O was run and rejected; full witness spectra and execution logs retained.

### TOP-30007113 — Isometric L1 embeddings of all positively weighted cactus metrics

Associated report scope: Every finite connected cactus with arbitrary positive edge lengths embeds isometrically in real L1; it has a tree decomposition with bag cardinality at most3, giving distortion1 on this explicit bag-size3 subclass.

Recorded verification: Executed check_exact.py with assertions enabled: PASS 140 rational weighted cacti; 15202 pairwise L1 distances equal independent Dijkstra shortest paths. python -O was separately executed and refused. These are finite exact checks only.

### TOP-30007441 — Polynomial switch-chain mixing for all degree sequences

Associated report scope: For the all-one degree sequence on even n≥4, the literal lazy four-vertex switch chain has gap at least 1/(12 binom(n,4)) and mixes by ceil(12 binom(n,4) ln(4n/2)), hence by 2n⁸.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007453 — Almost-linear edit-distance approximation scheme

Associated report scope: Exact unit-cost edit distance on the promise ED(x,y)≤k is computable in O(N(k+1)) word operations and O(k+1) working words; k=N^{o(1)} gives deterministic almost-linear exact estimation.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007460 — Depth-five homogeneous lower bounds for iterated matrix multiplication

Associated report scope: A monotone homogeneous depth-three ΣΠΣ circuit for IMM_{n,n}, whose product gates multiply n homogeneous linear forms with nonnegative real coefficients, requires at least n^{n−1} product gates for n≥2.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007461 — Integer multiplication below n log n

Associated report scope: A uniform deterministic fixed-multitape algorithm multiplies n-bit operands in O(n(h+1)) bit time and O(n) work bits when one operand has Hamming weight h; h≤√log₂(n+2) meets the prompt’s time scale.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007480 — Almost-linear maximum-cardinality matching

Associated report scope: Maximum-cardinality matching is deterministic exact in O(D·2^p·poly(p,log(n+D+2))) word operations from a supplied nice path decomposition of length D and bag size at most p; D=N^{1+o(1)}, p=o(log N) give almost-linear time.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007481 — Randomized k-server with squared-logarithmic ratio

Associated report scope: On a unit uniform metric with k initially distinct server sites, randomized marking has E[cost]≤2H_k·OPT with additive constant zero for every fixed finite request sequence.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.

### TOP-30007486 — Low-space worst-case Subset Sum at half-exponential time

Associated report scope: Subset Sum is deterministic exact within the requested time/space envelopes whenever the target after gcd normalization satisfies t/g+1≤2^{0.199n}; no bound of this strength is asserted for arbitrary targets.

Recorded verification: An exact standard-library checker accompanies this report; its actual tested ranges and stdout are recorded in verification.json and verification_stdout.txt.
