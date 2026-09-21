# PDT Cycle 304 — Sequential Selector Orientation Boundary

## Target
Attack PDT-II target (1), a PDT-native composition law, immediately after Cycle 303 showed that naive symmetrization of KL loses the ordinary one-sided conditional chain rule.

## Candidate principle tested
A tempting repair is to demand all of the following of a scalar distinction functional `D(P,Q)` on finite probability distributions:

1. identity: `D(P,P)=0`;
2. nonnegativity;
3. exchange symmetry: `D(P,Q)=D(Q,P)`;
4. independent-product additivity;
5. stochastic data processing;
6. an ordinary sequential chain rule with a *single symmetric branch weight* `w(p,q)=w(q,p)` depending only on the two marginal branch probabilities:

   `D(P_XY,Q_XY)=D(P_X,Q_X)+sum_x w(P_X(x),Q_X(x)) D(P_{Y|x},Q_{Y|x})`.

The strongest natural local normalization is `w(p,p)=p`, so that when the two marginals agree the rule reduces to ordinary expectation over that common marginal.

## Result
**FALSIFIED as a route to a unique PDT-native selector.**

The hypotheses do not determine the branch weight away from the diagonal `p=q`, and hence do not determine a unique sequential composition law. More strongly, the already established KL chain rule shows why the missing datum is directional: forward KL uses `P_X(x)` and reverse KL uses `Q_X(x)`. Their symmetric sum (Jeffreys) therefore has the exact two-weight decomposition

`J(P_XY,Q_XY)=J(P_X,Q_X) + sum_x [ P_X(x) KL(P_{Y|x}||Q_{Y|x}) + Q_X(x) KL(Q_{Y|x}||P_{Y|x}) ]`.

There is in general no reduction of this expression to a single symmetric scalar branch weight multiplying only `J(P_{Y|x},Q_{Y|x})`: such a reduction would require, branch by branch,

`w_x (a_x+b_x)=P_X(x)a_x+Q_X(x)b_x`,

where `a_x=KL(P_{Y|x}||Q_{Y|x})` and `b_x=KL(Q_{Y|x}||P_{Y|x})`. Thus

`w_x=(P_X a_x+Q_X b_x)/(a_x+b_x)`

when `a_x+b_x>0`. The required weight depends on the *conditional pair itself*, not only on the marginal resource/branch probabilities. Choosing two conditional pairs with different ratios `a_x/b_x` while keeping the same marginal pair changes the required `w_x`.

## Small decisive construction
Fix one branch with marginal probabilities `p != q`. Choose a binary conditional pair `(A,B)` with `KL(A||B) != KL(B||A)`. Swapping the conditional pair to `(B,A)` leaves the same marginal pair `(p,q)` and the same Jeffreys conditional distinction, but changes the weight required by the exact joint decomposition from

`(p a+q b)/(a+b)` to `(p b+q a)/(a+b)`.

Their difference is

`((p-q)(a-b))/(a+b)`,

which is nonzero whenever `p != q` and `a != b`. Therefore no branch weight depending only symmetrically on `(p,q)` can reproduce both experiments.

A strict-interior rational witness is available with `p=3/4`, `q=1/4`, `A=(3/4,1/4)`, `B=(1/2,1/2)`. Both KL directions are finite and unequal. The swapped conditional pair gives the contradiction without support singularities.

## Dimension stress
The witness is binary and embeds unchanged into every finite alphabet dimension `n>=2` by appending identical positive tail coordinates to both conditionals and renormalizing, or by taking a direct product with a common ancillary distribution. Hence increasing dimension cannot repair the single-weight law. Degenerate `n=1` is vacuous.

## Interpretation for PDT-II
This closes another apparent shortcut. A sequential physical-distinction law cannot simultaneously obtain exchange symmetry and retain KL-style local branch accounting merely by replacing the directional weight with a symmetric function of marginal branch probabilities. Sequential accounting must either:

- retain directional information;
- carry more than one conditional scalar;
- use a richer invariant than a single scalar distinction; or
- derive a genuinely different PDT-native composition operation.

This is a no-go boundary, not a positive PDT law.

## Prior-art boundary
KL's conditional chain rule and its directional expectation weighting are standard information theory. Symmetrized KL/Jeffreys divergence is also standard. Therefore the underlying ingredients are **IMPORTED/KNOWN**. The PDT contribution of this cycle is only the explicit obstruction test in the current theorem-search programme; no novelty claim is made for KL, Jeffreys, or their chain identities.

## Status ledger
- KL one-sided conditional chain rule: **PROVED / IMPORTED-KNOWN**.
- Jeffreys exact two-direction conditional decomposition: **PROVED / IMPORTED-KNOWN**.
- Single symmetric marginal-only branch weight reproduces Jeffreys sequential composition universally: **FALSIFIED**.
- Binary strict-interior swapped-conditional counterexample: **PROVED**.
- Extension to `n=2..12` and arbitrary larger finite dimension by common-ancilla/direct embedding: **PROVED**.
- PDT-native sequential composition selector: **OPEN**.
- PDT-native non-circular `n=3` derivation: **OPEN**.
- Fully specified same-input `P_PDT != P_QM`: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Search for the minimal richer compositional object that survives this no-go: ordered pair `(D(P||Q),D(Q||P))`, likelihood-ratio spectrum, or an operational equivalence class. Reject any candidate that merely renames standard sufficient-statistic/Blackwell information without a PDT-native physical postulate.
