# Cycle 344 — Multiplicative-affinity composition boundary

## Target
Attack the strongest unresolved PDT-II target: whether replacing scalar total-variation distinction by a tensorizing scalar can yield a PDT-native composition law, select n=3, or force a same-input deviation from quantum theory.

## Candidate
For finite classical preparations P,Q define the Hellinger/Bhattacharyya affinity

A(P,Q) = sum_x sqrt(P(x) Q(x)),

and squared Hellinger distinction H^2(P,Q)=1-A(P,Q).

Candidate composition principle (independent composition):

A(P1 x P2, Q1 x Q2) = A(P1,Q1) A(P2,Q2),

or equivalently

H^2_12 = H^2_1 + H^2_2 - H^2_1 H^2_2.

## Exact proof
For finite distributions,

A(P1 x P2,Q1 x Q2)
= sum_{x,y} sqrt(P1(x)P2(y)Q1(x)Q2(y))
= [sum_x sqrt(P1(x)Q1(x))][sum_y sqrt(P2(y)Q2(y))].

Hence the rule is exact for every finite alphabet size, including n=1,...,12 and all n>12. Degenerate zero-probability coordinates cause no problem because every summand is nonnegative and sqrt(0)=0.

For k identical copies,

A(P^k,Q^k)=A(P,Q)^k,
H^2(P^k,Q^k)=1-(1-H^2(P,Q))^k.

## Adversarial consequence
This is a genuine scalar tensorization law, unlike total variation. But it does NOT determine the physical composite. The identity follows after the independent product P x Q has already been chosen. It therefore describes how this affinity behaves under a specified tensor/product rule; it does not derive that product rule.

The same identity holds for every finite n. Therefore it cannot select n=3.

Moreover Hellinger tensorization is established probability/statistics machinery, so the identity is not PDT-native novelty. Existing literature explicitly contrasts tensorizing Hellinger/KL/chi-square quantities with non-tensorizing total variation.

## Same-input PDT/QM test
No probability rule distinct from QM follows. A metric identity on already specified preparations/composites supplies neither a new state space, Born-rule replacement, nor resource-window-dependent measurement law. Thus no parameter-free P_PDT(O|I,R) != P_QM(O|I,R) is licensed.

## Stress classification
- n=1: trivial A=1 for the unique normalized one-point distribution.
- n=2,...,12: exact algebra above; no exceptional n=3 term.
- arbitrary finite n: exact proof.
- edge/degenerate supports: exact.
- repeated independent composites: exact k-copy formula.
- correlated composites: hypothesis fails because the factorization premise is absent; affinity alone does not reconstruct correlations.
- alternative tensor/composition rules: OPEN unless independently specified; the scalar law cannot select among them.
- quantum pure/mixed states: importing fidelity/quantum affinity analogues would be known quantum-information structure, not a PDT derivation.

## Prior-art audit
Bhattacharyya et al., IJCAI 2023 / arXiv:2206.07209, and the 2024 complexity paper arXiv:2405.08255 explicitly note that Hellinger, KL and chi-square tensorize over marginals while TV does not. Kontorovich, Electronic Communications in Probability 30 (2025), studies the non-tensorization boundary for variational distance. These sources block novelty claims for scalar Hellinger tensorization itself.

## Status ledger
| Claim | Status |
|---|---|
| Hellinger/Bhattacharyya affinity multiplicativity under an already specified independent product | PROVED / IMPORTED-KNOWN |
| k-copy formula H^2_k = 1-(1-H^2)^k | PROVED / IMPORTED-KNOWN |
| multiplicative scalar affinity derives a unique PDT composition law | FALSIFIED as an inference |
| multiplicative scalar affinity selects n=3 | FALSIFIED |
| multiplicative scalar affinity forces same-input PDT/QM deviation | FALSIFIED as an inference |
| a richer PDT-native object that derives correlated composition rather than merely respecting it | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Surviving strengthened requirement
A viable PDT composition principle must determine admissible correlated composites from PDT-native distinction structure. Merely finding a scalar that tensorizes after a product has been supplied is insufficient and circular for the composition target.
