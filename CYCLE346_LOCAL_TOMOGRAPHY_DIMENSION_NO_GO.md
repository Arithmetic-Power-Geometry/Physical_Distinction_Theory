# Cycle 346 — Local tomography does not select n=3

## Target
Attack the strongest surviving PDT-II composition route after Cycle 345: add an intrinsically composite consistency principle rather than another local distinction scalar. Candidate: **local tomography** — global states are uniquely determined by statistics of product/local measurements.

## Exact hypotheses
For systems A and B with finite-dimensional real ordered state spaces of unnormalised dimensions K_A and K_B, impose local tomography in the standard operational sense: product effects separate bipartite states. In finite-dimensional locally tomographic theories this gives the parameter-count identity K_AB = K_A K_B.

Candidate claims tested:
1. local tomography supplies a PDT-native composition law;
2. local tomography non-circularly selects n=3;
3. local tomography forces a same-input PDT/QM probability deviation.

## Prove-or-falsify
All three claims fail as universal implications.

### Exact counterfamilies
Classical n-level probability theory is locally tomographic for every finite n, with K_cl(n)=n and K_cl(AB)=n_A n_B.

Complex finite-dimensional quantum theory is locally tomographic for every finite Hilbert dimension n, with K_C(n)=n^2 and K_C(AB)=(n_A n_B)^2=K_C(n_A)K_C(n_B).

Therefore local tomography holds simultaneously at n=1,2,...,12 (and all finite n) in at least these two inequivalent theory families. There is no exceptional n=3 step.

Real quantum theory supplies a useful negative control: K_R(n)=n(n+1)/2, while for the ordinary real tensor product K_R(n_A n_B) generally differs from K_R(n_A)K_R(n_B). Thus local tomography genuinely excludes some composite structures, but exclusion is not unique selection.

Smallest decisive n=3 counterexample: n=2 already satisfies local tomography in both a classical bit and a complex qubit. Hence the implication local tomography => n=3 is false before n=3 is reached.

## Composition boundary
Local tomography is a joint/composite constraint, so it survives Cycle 345's criticism that purely local distinction data cannot determine correlations. But it still does not, by itself, specify which locally tomographic state cone, effect cone, reversible group, or probability theory is physically realised. Classical and complex quantum families are already inequivalent witnesses satisfying it. Therefore it constrains composition without deriving a unique PDT composition law.

## Same-input prediction boundary
Ordinary complex quantum theory satisfies local tomography. Consequently local tomography alone cannot imply P_PDT(O|I,R) != P_QM(O|I,R) under identical microscopic inputs and resource window. A quantitative PDT deviation still requires an additional PDT-native state/composite rule and probability map.

## Prior-art audit
This principle is established reconstruction/GPT machinery, not PDT novelty. Hardy and Wootters, *Limited Holism and Real-Vector-Space Quantum Theory* (Foundations of Physics; arXiv:1005.4870), explicitly contrast locally tomographic complex quantum theory with bilocally tomographic real quantum theory. Barnum and Wilce, *Local tomography and the Jordan structure of quantum theory* (arXiv:1202.4513), show that local tomography becomes highly selective only together with substantial extra hypotheses such as homogeneous self-dual/Jordan structure and a qubit. Thus importing local tomography cannot be promoted as a PDT-native breakthrough.

## Exact dimension stress
The accompanying CSV records n=1,...,12 parameter counts for classical, complex-quantum, and real-quantum single systems and identical-system composites. Classical and complex ratios K(n^2)/K(n)^2 equal 1 exactly for every n; the real-quantum ratio departs from 1 for n>=2. This is exact integer arithmetic, not simulation.

## Status ledger
| Claim | Status |
|---|---|
| Local tomography is a genuine composite constraint | PROVED / IMPORTED-KNOWN |
| Local tomography uniquely determines the PDT composition law | FALSIFIED |
| Local tomography => n=3 | FALSIFIED |
| Local tomography => same-input PDT/QM deviation | FALSIFIED as an inference |
| Classical and complex quantum theories satisfy local tomography for every finite n | PROVED / IMPORTED-KNOWN |
| Standard real quantum theory fails local tomography for n>=2 | PROVED / IMPORTED-KNOWN |
| n=1,...,12 exact parameter-count stress | PROVED |
| PDT-native selector beyond local tomography | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Strengthened surviving target
A viable PDT-II composition candidate must be stronger than local tomography yet not simply import a known reconstruction package. It must constrain the admissible **joint distinction geometry** enough to choose among inequivalent locally tomographic theories, while surviving classical simplices, complex quantum composites, GPT min/max adversaries, restricted-resource quotients, and exact dimension stress. The next cycle should attack such a joint-distinction axiom directly rather than stack established reconstruction postulates.