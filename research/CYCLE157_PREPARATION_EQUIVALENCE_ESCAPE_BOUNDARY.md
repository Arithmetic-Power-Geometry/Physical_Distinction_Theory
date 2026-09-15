# Cycle 157 — Preparation-equivalence escape boundary

## Target attacked
PDT-II targets (2) and (3): a non-circular n=3 derivation and a same-input quantitative PDT-vs-QM prediction.

## Theorem (operational closure under preparation equivalence)
Let P and P' be preparation procedures that are operationally equivalent in the declared microscopic/resource window R. Suppose a PDT prediction functional is preparation-extensional: its outcome probabilities depend only on the operational equivalence class [P]_R, together with the same subsequent transformation and effect. Then

P_PDT(O|P,R) = P_PDT(O|P',R).

In particular, in ordinary finite-dimensional quantum mechanics, two ensembles with the same density operator rho are operationally equivalent for all quantum effects. Therefore a PDT rule that assigns different outcome probabilities to two decompositions of the same rho is not a same-input deviation on the quantum state rho; it introduces preparation-context information beyond rho (or rejects the quantum operational equivalence).

### Proof
Preparation-extensionality means there exists f_R such that P_PDT(O|P,R)=f_R(O,[P]_R). If P~_R P', then [P]_R=[P']_R, hence equality follows immediately. For QM, any ensemble {p_i,|psi_i>} with sum_i p_i |psi_i><psi_i|=rho gives Tr(E rho) for every effect E, independent of decomposition.

## Smallest decisive witness
For a qubit,

rho = I/2 = 1/2 |0><0| + 1/2 |1><1| = 1/2 |+><+| + 1/2 |-><-|.

Any PDT formula that predicts different statistics solely because the first or second decomposition was used is preparation-context dependent. Calling both inputs simply 'rho=I/2' while retaining the different prediction is therefore inconsistent with preparation-extensionality.

## Consequence for PDT-II
A proposed same-input PDT-vs-QM difference cannot be obtained merely by making a probability/dynamics rule depend on a hidden ensemble decomposition while simultaneously claiming the microscopic input is only the density operator. A defensible deviation must explicitly declare and operationalize the extra preparation variable, or derive a failure of the usual operational equivalence. Once that extra variable is declared, the comparison is no longer identical microscopic input unless the competing QM model is supplied the same physically accessible variable.

This is a falsification boundary, not a breakthrough candidate.

## Prior-art boundary
The operational-equivalence/preparation-contextuality framework is established prior art, notably R. W. Spekkens, Phys. Rev. A 71, 052108 (2005), DOI 10.1103/PhysRevA.71.052108. Modern GPT/contextuality treatments likewise identify quantum preparation equivalences with different decompositions of the same density matrix. No novelty is claimed for this theorem.

## Status
- Operational closure theorem: PROVED (elementary, conditional on preparation-extensionality).
- Quantum same-density ensemble equivalence: IMPORTED/KNOWN.
- 'Hidden ensemble decomposition alone gives a same-input PDT-vs-QM prediction while input remains only rho': FALSIFIED.
- PDT-native derivation of an additional operationally measurable preparation variable: OPEN.
- Parameter-free experimentally distinctive PDT inequality: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Research discipline
Do not promote ensemble-sensitive nonlinear rules as PDT predictions unless the ensemble label is independently operationalized and the identical-input QM comparator is given that same information. Do not infer gravity/capacity consequences from this boundary.
