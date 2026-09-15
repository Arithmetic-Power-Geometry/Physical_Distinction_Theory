# Cycle 162 — Local tomography does not rescue PDT-native composition

## Priority
PDT-II target (1): PDT-native composition law; consequence for target (2).

## Status
- **PROVED:** local tomography is an additional composite-system axiom, not a consequence of isolated-system distinction geometry or simple-product consistency.
- **FALSIFIED:** the candidate route "repair Cycle 161 by imposing local distinguishability/tomography and call the resulting composition PDT-native".
- **IMPORTED/KNOWN:** local tomography is a standard reconstruction/GPT postulate; complex quantum theory satisfies it, while real quantum theory supplies a standard countermodel and is instead bilocally tomographic.
- **OPEN:** a PDT-derived composite-only principle with independent physical meaning that selects a composition rule without importing local tomography/Hilbert composition.
- **BREAKTHROUGH CANDIDATE:** NO.

## Exact claim attacked
After Cycle 161 showed that factor norms, reversible factor symmetry, exchange symmetry and simple-product multiplicativity leave injective/projective and other tensor structures underdetermined, consider adding:

> LT: joint states are uniquely determined by the statistics of all product/local measurements.

Could LT be treated as the missing PDT-native composition law?

## Theorem / falsification boundary
No, not without a separate PDT derivation of LT.

LT is logically stronger than the Cycle-161 factor assumptions because those assumptions constrain the behavior of decomposable tensors but do not require product effects to separate all joint states. A theory can agree on isolated systems and product normalization while possessing holistic joint degrees of freedom invisible to local measurements.

A standard decisive countermodel is real-vector-space quantum theory. It has legitimate finite-dimensional state spaces and composites, but local tomography fails; Hardy and Wootters show that real quantum theory is bilocally tomographic rather than locally tomographic. Thus local tomography is not forced merely by having a coherent probabilistic composite theory.

Therefore adding LT can reduce composition ambiguity only by adding genuinely new physical content. Unless PDT derives that content from its own distinction/resource primitives, using LT is IMPORTED/KNOWN rather than a PDT-native derivation.

## Parameter-count witness
For a real Hilbert system of dimension d, the real vector space of unnormalised symmetric states has

    K_R(d) = d(d+1)/2

parameters. For two such systems with dimensions d_A,d_B, the real composite has

    K_R(d_A d_B) = d_A d_B(d_A d_B+1)/2,

whereas local tomography would require

    K_R(d_A) K_R(d_B).

Already for two rebits, d_A=d_B=2:

    K_R(4)=10,   K_R(2)^2=9.

So one global degree of freedom is invisible to purely local tomography. This is the smallest parameter-count witness that the LT identity K_AB=K_A K_B is not automatic.

For equal d>=2 the deficit is

    Delta(d)=K_R(d^2)-K_R(d)^2 = d^2(d-1)^2/4 > 0.

Hence the obstruction persists and grows with dimension; it is not a 2x2 accident.

## Exact dimension stress check
For d=1,...,12, Delta(d)=d^2(d-1)^2/4. It vanishes only at d=1 and is strictly positive for every d=2,...,12. Thus the real-quantum counterfamily defeats any claim that local tomography follows universally from coherent factor/composite structure.

## Prior-art boundary
Hardy & Wootters, *Limited Holism and Real-Vector-Space Quantum Theory* (2010), explicitly contrast locally tomographic complex quantum theory with bilocally tomographic real quantum theory. Barnum & Wilce show that local tomography becomes powerful only together with additional structural assumptions such as homogeneous self-dual/Jordan single-system structure and a qubit. These are reconstruction assumptions/results, not PDT-native consequences.

## Consequence for PDT-II
Cycle 161 cannot be repaired by silently adding local tomography. A defensible PDT-native composition result must instead derive an operational separation/revelation principle from PDT primitives and then prove what composite degrees of freedom it permits or forbids. The derivation must survive at least classical, real-quantum, complex-quantum and GPT countermodels.

This also sharpens target (2): an n=3 derivation that assumes local tomography before deriving composition is conditional/imported, not non-circular PDT-native.

## Next obligation
Attack a genuinely PDT-flavored candidate: **resource-complete revelation** — whether every globally persistent distinction that can influence a later admissible PDT intervention must be revealable by some bounded composite observation. Formalize it without assuming local tomography; test whether it selects a tensor rule or whether real-QM/GPT countermodels falsify it. If false, record the smallest witness and retain only the surviving conditional theorem.
