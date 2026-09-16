# Cycle 176 — Maximum-entropy probability selection is not PDT-native

## Target
PDT-II targets (2) and (3): test whether the missing preparation-dependent probability measure can be selected non-circularly from distinction data by a maximum-entropy / least-commitment principle.

## Candidate principle
Given a finite PDT operational quotient Q with declared constraints C, select

p* = argmax_{p in Delta(Q), p satisfies C} H(p),

where H(p) = -sum_x p_x log p_x.

## Exact result 176.1 — unconstrained case
For |Q|=n and no constraint beyond normalization, strict concavity of Shannon entropy gives the unique maximizer

p_i = 1/n.

This holds for every finite n, hence exactly for n=1,...,12 and all higher finite dimensions.

Classification: PROVED, but IMPORTED/KNOWN (standard maximum-entropy result), not PDT-native.

## Exact result 176.2 — the rule imports a reference structure
The optimization is not determined by the bare distinction partition. It requires at least:
1. a choice of entropy/divergence functional;
2. a choice of atomic outcome representation/reference measure (especially outside finite uniform counting cases);
3. the physical constraints to impose.

Therefore distinction equivalence alone does not derive MaxEnt. Adopting MaxEnt is an additional inference axiom.

Classification: FALSIFIED as a claim of derivation from bare PDT distinction structure.

## Exact result 176.3 — MaxEnt cannot by itself yield a same-input PDT-vs-QM prediction
Suppose the identical microscopic input I and resource window R already specify a quantum state rho and measurement {Pi_i}. QM predicts q_i=Tr(rho Pi_i). Replacing q by a MaxEnt distribution while ignoring rho is not a same-input physical derivation: it discards microscopic preparation information. If instead the MaxEnt constraints are chosen to encode enough expectation information to recover rho, the resulting distribution reproduces rather than independently contradicts the encoded statistics.

Thus a claimed P_PDT != P_QM generated solely by choosing MaxEnt would be inserted by a new inference postulate or by dropping input information, not forced by PDT distinctions.

Classification: FALSIFIED for target (3) as currently posed.

## n=3 boundary
With three fully symmetric outcomes and only normalization, MaxEnt gives (1/3,1/3,1/3). This is a valid conditional rule but is not a PDT-native derivation of the general n=3 quantum probability law. A generic qutrit preparation has nonuniform Born probabilities in a fixed basis. Obtaining those probabilities requires preparation-dependent structure beyond a three-element distinction quotient.

Classification: CONDITIONAL + IMPORTED/KNOWN; PDT-native n=3 derivation remains OPEN.

## Dynamics / path variant
Replacing state entropy by path entropy (maximum caliber) does not remove the underdetermination: one must specify a path reference measure and dynamical constraints. Hence Markovian/non-Markovian path selection is not obtained from distinction equivalence alone.

Classification: IMPORTED/KNOWN + OPEN as a PDT bridge.

## Prior-art boundary
Maximum entropy is a long-established inference principle associated with Jaynes and subsequent consistency work. Gleason-type uniqueness is also established once Hilbert/projector structure and noncontextual orthogonal additivity are supplied in dimension >=3. Neither can be relabeled as PDT novelty.

## Surviving theorem / obligation
PDT must derive a preparation-dependent measure or scoring functional from independently motivated physical distinction primitives. Candidate axioms must be tested for whether they merely re-express a prior, amplitude, density operator, Gibbs weight, reference measure, or MaxEnt constraint.

A useful next attack is representation invariance: ask whether any probability selector depending only on the unlabeled finite distinction quotient and commuting with all quotient automorphisms can encode nonuniform preparation probabilities. The expected boundary is that full permutation naturality forces uniformity unless extra preparation structure breaks the symmetry; this should be formulated categorically and checked for whether it is merely a standard naturality result.

## Status
- Maximum-entropy finite uniform selector: PROVED / IMPORTED-KNOWN.
- Derivation of MaxEnt from bare PDT distinctions: FALSIFIED.
- MaxEnt-only same-input PDT != QM prediction: FALSIFIED.
- General PDT-native n=3 probability derivation: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

No gravity/capacity claim is promoted.
