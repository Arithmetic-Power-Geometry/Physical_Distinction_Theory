# PDT-II Cycle 365 — Local-tomography composition no-go

## Target attacked
Priority (1) PDT-native composition law, then (2) non-circular n=3 derivation and (3) same-input PDT/QM prediction gap.

## Candidate principle
**LT:** a composite physical state is completely determined by joint statistics of local measurements (local tomography / local discriminability).

### Exact hypotheses
1. Finite-dimensional state spaces.
2. Independent systems A,B admit a composite AB.
3. Product effects span the dual state space of AB (local tomography).
4. For the quantum counterfamily, states are ordinary complex density operators and composition is the standard tensor product.

## Theorem 365A — complex-QM all-dimension counterfamily [PROVED]
For a complex quantum system of Hilbert dimension n, the real vector space of unnormalised Hermitian operators has dimension K(n)=n^2. For systems of dimensions n and m, standard tensor composition gives

K(nm)=(nm)^2=n^2 m^2=K(n)K(m).

A tensor product of Hermitian operator bases {A_i} and {B_j} is a basis {A_i tensor B_j} for Hermitian operators on AB. Hence expectation values of product effects determine every composite density operator. Complex finite-dimensional QM is locally tomographic for every n,m >= 1.

Therefore LT cannot imply n=3. The smallest nontrivial counterexample is n=2; n=4 immediately defeats uniqueness above 3. The exact diagonal audit n=m=1,...,12 has zero parameter-count defect for every n.

## Theorem 365B — local tomography does not by itself fix composition [PROVED as a no-go inference]
LT imposes a spanning/separation condition on composites, but the condition is already satisfied by ordinary complex QM in all finite dimensions. Consequently LT alone cannot be a PDT-native selector of n=3 and cannot, without an additional PDT postulate, entail P_PDT(O|I,R) != P_QM(O|I,R) for identical microscopic input I and resource window R.

This is an inference no-go, not a claim that all locally tomographic GPTs have identical composition.

## Adversarial comparison: real quantum theory
For real n-dimensional quantum theory, the unnormalised state-space dimension is K_R(n)=n(n+1)/2. Under the ordinary real tensor product,

K_R(nm)=nm(nm+1)/2,

which generally differs from K_R(n)K_R(m). At n=m=2, K_R(4)=10 whereas K_R(2)^2=9. Thus local tomography is a substantive composition constraint, not a tautology; nevertheless it selects neither n=3 nor PDT uniquely.

## Edge/degenerate cases
- n=1: K=1 and LT holds trivially.
- n=2: nontrivial complex-QM counterexample to LT => n=3.
- n=3: LT holds, but not uniquely.
- n=4,...,12: exact parameter identity persists.
- arbitrary finite n,m: analytic identity proves the higher-dimensional extension; random stress testing is unnecessary for the parameter identity.

## Prior-art boundary [IMPORTED/KNOWN]
Local tomography/local discriminability is established in GPT and reconstruction literature. Hardy developed operational circuit/locality formalisms; Hardy and Wootters explicitly contrast locally tomographic complex quantum theory with bilocally tomographic real-vector-space quantum theory. Barnum and Wilce obtain much stronger reconstruction results only after combining local tomography with additional Jordan/homogeneity/self-duality and qubit assumptions. Therefore neither LT nor the complex-vs-real tomography distinction is PDT novelty.

Relevant literature checked 2026-09-24:
- L. Hardy, *A formalism-local framework for general probabilistic theories including quantum theory*, Math. Struct. Comput. Sci. 23 (2013), arXiv:1005.5164.
- L. Hardy and W. K. Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, arXiv:1005.4870.
- H. Barnum and A. Wilce, *Local tomography and the Jordan structure of quantum theory*, arXiv:1202.4513 / J. Phys. A.
- G. Chiribella, *Process tomography in general physical theories*, arXiv:2109.12067 (shows process tomography questions can be separated from assuming local tomography).

## Status ledger delta
| Claim | Status |
|---|---|
| Complex finite-dimensional QM is locally tomographic for every n,m | IMPORTED/KNOWN; algebra reproduced exactly |
| K(nm)=K(n)K(m) for complex QM | PROVED |
| LT => n=3 | FALSIFIED |
| LT alone => unique PDT composition | FALSIFIED as an inference |
| LT alone => same-input PDT/QM probability deviation | FALSIFIED as an inference |
| Real QM with ordinary real tensor product is locally tomographic | FALSIFIED (smallest nontrivial equal-local-dimension witness n=m=2: 10 != 9) |
| PDT-native composition selector beyond LT | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Surviving requirement
Any viable PDT composition law must add a genuinely PDT-native constraint that is not merely local tomography, and that constraint must survive the all-dimensional complex-QM counterfamily. If it is intended to yield experimental distinctiveness, it must specify I and R sufficiently to calculate an outcome probability different from QM rather than merely rename an existing tomographic property.
