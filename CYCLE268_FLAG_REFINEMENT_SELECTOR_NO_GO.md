# Cycle 268 — Flag-refinement conservation is not an n=3 selector

## Target attacked
PDT-II targets (2) non-circular n=3 derivation and (4) resource-refinement/revelation/conservation laws, with consequences for (1) composition.

## Candidate principle
Let a resource/distinction functional D be defined on states with perfectly distinguishable classical flags. Consider the strong flag-refinement law

D(sum_i p_i rho_i tensor |i><i|) = sum_i p_i D(rho_i),

with monotonicity under forgetting/coarse-graining the flag. Could this refinement/revelation law force ambient dimension n=3 or uniquely select the PDT composite?

## Exact counterfamily
For every finite n>=1, take n-dimensional complex quantum states and define the relative entropy of coherence in a fixed basis,

C_r(rho)=S(Delta(rho))-S(rho).

For an orthogonal classical flag register F whose basis is incoherent,

rho_XF = direct_sum_i p_i rho_i.

Entropy of block-diagonal states gives

S(rho_XF)=H(p)+sum_i p_i S(rho_i),
S(Delta(rho_XF))=H(p)+sum_i p_i S(Delta(rho_i)),

hence exactly

C_r(rho_XF)=sum_i p_i C_r(rho_i).

This proof is dimension-independent. It holds for n=1 (degenerate zero resource), n=2, n=3, ..., and every finite n. Therefore flag refinement/additivity cannot uniquely select n=3. The smallest nontrivial counterdimension is n=2; n=4 is the smallest counterdimension above the target.

A still simpler classical counterfamily is Shannon information on an n-symbol system with a revealed flag: the chain rule/refinement identity is valid for arbitrary alphabet size. Thus the obstruction is not specifically quantum.

## Composition consequence
The law presupposes a flagged composite/direct-sum construction. Even if imposed exactly, it constrains the value of D on block-diagonal flagged states; it does not determine the full unflagged joint state cone/effect cone or tensor product. Therefore it cannot, by itself, close PDT-II target (1).

## Prior-art boundary
Flag additivity is established quantum-resource-theory structure, not PDT novelty. Liu, Yu and Tong, *Flag Additivity in Quantum Resource Theories* (2019), explicitly introduce flag additivity and relate it to strong monotonicity, convexity and full additivity (arXiv:1904.07627). Resource theories of distinguishability are also established: Wang and Wilde (2019) and Salzmann et al. (2021) formulate asymmetric/symmetric distinguishability as quantum resources with monotonicity under free transformations. These results are prior-art constraints, not claims of PDT derivation.

## Surviving theorem
**Flag-refinement selector no-go.** Any candidate exact-dimension selector whose only dimension-sensitive content is an orthogonal-flag decomposition identity shared by a family of theories in all finite dimensions cannot select a unique finite ambient dimension. In particular, the flag-additivity identity above is satisfied for all finite complex dimensions, so it cannot imply n=3.

The result does **not** prove that every conceivable PDT-native refinement law is dimension-blind. A future candidate must contain an additional ambient-sensitive hypothesis that actually fails in n=2 or n>=4 and is independently derived rather than inserted to obtain three.

## Stress-test ledger
- n=1: identity holds; degenerate C_r=0.
- n=2: identity holds; decisive nontrivial counterexample below 3.
- n=3: identity holds.
- n=4..12: identity holds by the same block-entropy calculation.
- arbitrary finite n: analytic proof above.
- pure/mixed: covered because block entropy identity holds for arbitrary density operators.
- composites: flagged direct-sum composite covered; law does not determine general unflagged composite.
- Markovian/non-Markovian dynamics: irrelevant to the static identity and therefore cannot rescue dimension selection without an additional dynamical premise.
- different norms/reversible groups: the counterexample already defeats the universal selector claim; no norm assumption is needed.

## Status
| Claim | Status |
|---|---|
| Block-entropy flag identity for relative entropy of coherence in every finite n | PROVED |
| Flag additivity/refinement alone implies n=3 | FALSIFIED |
| Flag additivity alone uniquely determines PDT composition | FALSIFIED / UNDERDETERMINED |
| General flag-additivity/resource-theory framework | IMPORTED/KNOWN |
| A genuinely PDT-native ambient-sensitive refinement law | OPEN |
| Same-input P_PDT != P_QM with an explicitly changed operational primitive | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Research discipline
No experimental claim is made. No novelty is claimed for flag additivity, entropy chain rules, or resource-theory monotonicity. The PDT contribution of this cycle is negative: it removes another tempting but dimension-blind route and sharpens the admissibility criterion for future n=3 candidates.