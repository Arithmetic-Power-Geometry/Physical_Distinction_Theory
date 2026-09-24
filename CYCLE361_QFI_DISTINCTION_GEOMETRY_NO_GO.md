# Cycle 361 — Quantum-Fisher distinction geometry does not select n=3

## Status

**DECISIVE FALSIFICATION / PRIOR-ART BOUNDARY.** No breakthrough candidate is promoted.

## Candidate attacked

A natural PDT-II candidate is that physical distinction should be represented infinitesimally by a resource-sensitive statistical metric whose distinguishability is (i) monotone under parameter-independent admissible processing, (ii) additive on independent composites, and (iii) operationally tied to estimation precision. One might hope that this package selects a unique local dimension, composition rule, or same-input departure from quantum mechanics.

## Exact hypotheses

For a differentiable family of finite-dimensional density operators rho_theta, define the symmetric-logarithmic-derivative (SLD) quantum Fisher information F_Q(rho_theta). Test the package:

H1. F_Q is nonnegative.

H2. For every theta-independent CPTP map Lambda,
F_Q(Lambda(rho_theta)) <= F_Q(rho_theta).

H3. For independent parameter encodings,
F_Q(rho_theta tensor sigma_theta) = F_Q(rho_theta) + F_Q(sigma_theta).

H4. F_Q controls the local estimation bound through the quantum Cramer-Rao framework.

Candidate inference under test: H1-H4, interpreted as a physical-distinction geometry, imply n=3, a unique PDT composition, or a same-input PDT/QM probability gap.

## Counterfamily

For every n >= 2, embed the two-level pure-state family

|psi(theta)> = cos(theta)|0> + sin(theta)|1>

in C^n. For a differentiable pure family,

F_Q = 4( <dot psi|dot psi> - |<psi|dot psi>|^2 ).

Here <dot psi|dot psi>=1 and <psi|dot psi>=0, so

F_Q = 4

for every n >= 2. Thus the identical nonzero local distinction geometry occurs at n=2,3,4,... . At n=1 every normalized state family is physically constant up to global phase, so its state QFI is zero.

This gives the smallest nontrivial decisive counterexample at n=2 and an infinite higher-dimensional counterfamily. There is no n=3 singularity.

For k independent copies of the same family, additivity gives F_Q(rho_theta^{tensor k}) = 4k. This scaling likewise contains no selector for n=3.

## Same-input consequence

H1-H4 are all properties available inside ordinary finite-dimensional complex quantum mechanics. Therefore they cannot, without an additional PDT-native postulate, imply

P_PDT(O | I,R) != P_QM(O | I,R)

for identical microscopic input I and declared resource window R. A QFI-derived experimental inequality that is merely the standard quantum Cramer-Rao/metrological bound is consequently not PDT-distinctive.

## Composition consequence

Additivity of a scalar information metric on product encodings does not determine the full composite state/effect cone or tensor rule. Ordinary quantum tensor products already realize H1-H4 in every finite dimension. Hence QFI additivity is not the missing PDT-native composition law.

## Adversarial/edge audit

- n=1: only trivial physical state variation; F_Q=0.
- n=2: explicit embedded family has F_Q=4 — smallest decisive counterexample to n=3 necessity.
- n=3: same value 4; nothing singular occurs.
- n=4,...,12: same embedded construction gives F_Q=4 exactly.
- arbitrary finite n>=2: analytic embedding proof gives F_Q=4.
- pure states: explicit proof above.
- mixed states: standard SLD-QFI remains a finite-dimensional quantum construction; no n=3 selector follows.
- composites: independent-copy QFI is additive.
- processing: theta-independent CPTP maps obey QFI data processing.
- degenerate direction: theta-independent families have F_Q=0 in every dimension.

## Prior-art boundary

Quantum Fisher information, its relation to fidelity/Bures statistical geometry, monotonicity under parameter-independent quantum channels, additivity for product probes, and quantum-metrological precision bounds are established quantum-information/metrology results. They are **IMPORTED/KNOWN**, not PDT novelty. In particular, existing literature treats QFI explicitly as a distinguishability/estimation quantity and as a resource measure in metrological resource theories.

Representative checks used in this cycle:

- Review/article literature states convexity, tensor-product additivity and monotonicity of QFI under parameter-independent CPTP maps in quantum metrology.
- Z. Chen and X. Hu, *Resource theory of dephasing estimation in multiqubit systems*, Phys. Rev. A 108, 032415 (2023), explicitly uses QFI as a resource measure based on its monotonicity.

## Classification

| Claim | Status |
|---|---|
| Embedded pure family has F_Q=4 for every finite n>=2 | **PROVED** |
| n=1 physical state QFI is zero | **PROVED** |
| SLD-QFI CPTP monotonicity | **IMPORTED/KNOWN** |
| QFI tensor-product additivity | **IMPORTED/KNOWN** |
| QFI/quantum-metrology precision relation | **IMPORTED/KNOWN** |
| H1-H4 imply n=3 | **FALSIFIED** |
| QFI additivity determines unique PDT composition | **FALSIFIED as an inference** |
| H1-H4 imply a same-input PDT/QM probability deviation | **FALSIFIED as an inference** |
| Standard QFI metrological bound is experimentally PDT-distinctive | **FALSIFIED as an inference** |
| Additional PDT-native resource-window law beyond standard quantum statistical geometry | **OPEN** |
| BREAKTHROUGH CANDIDATE | **NO** |

## Surviving PDT-II requirement

A viable PDT-II distinction geometry must contain structure not already satisfied by ordinary finite-dimensional quantum statistical geometry. To matter for the requested prediction target, that extra structure must alter an explicitly specified operational probability or bound under identical microscopic inputs and an identical declared resource window. Merely renaming QFI, Bures geometry, Fisher-information monotonicity, or metrological precision as physical distinction is insufficient.
