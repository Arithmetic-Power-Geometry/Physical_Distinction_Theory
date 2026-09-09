# Cycle 024 — External Distinction Budget for Open-System Revival

## Status

**PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN.** This is not a breakthrough candidate and is not claimed as historically new mathematics.

## Theorem

For two possible joint system-environment states `rho_SE^1(s), rho_SE^2(s)`, let the closed `SE` pair subsequently undergo the same unitary evolution. Define local distinction by trace distance

`D_S(s)=D(rho_S^1(s),rho_S^2(s))`.

Then for every later time `t`,

`D_S(t)-D_S(s) <= D_E(s) + C_1(s) + C_2(s)`,

where

`D_E(s)=D(rho_E^1(s),rho_E^2(s))`

and

`C_i(s)=D(rho_SE^i(s), rho_S^i(s) tensor rho_E^i(s))`.

Thus a positive revival of locally accessible distinction requires a pre-existing external budget: distinguishability in the environment, system-environment correlations, or both.

## Proof

Unitary invariance and contractivity of trace distance under partial trace give

`D_S(t) <= D(rho_SE^1(s),rho_SE^2(s))`.

Insert the two product marginals and apply the triangle inequality:

`D(rho_SE^1,rho_SE^2) <= C_1 + D(rho_S^1 tensor rho_E^1, rho_S^2 tensor rho_E^2) + C_2`.

A second triangle inequality plus tensor stability of trace distance gives

`D(rho_S^1 tensor rho_E^1, rho_S^2 tensor rho_E^2) <= D_S + D_E`.

Combining and subtracting `D_S(s)` proves the claim.

## PDT consequence

A resource-change or non-Markovian PDT law may not treat a local distinction revival as free creation. If the microscopic model is standard quantum mechanics with the same joint states and unitary dynamics, the revival must fit inside the external distinction budget above. A claimed same-input excess would require an explicitly different physical ingredient, not merely a new interpretation of memory.

A particularly sharp kill test is the zero-budget case. If both preparations have the same environment marginal and are initially uncorrelated with that environment, then `D_E=C_1=C_2=0`, so `D_S(t)<=D_S(s)` for every common subsequent unitary.

## Stress audit

The implementation tests random mixed joint states and Haar-like QR unitaries with a two-dimensional environment for system dimensions 1 through 12. The committed fixed-seed audit used 100 trials per dimension and found no violation; the largest `gain - budget` was negative in every dimension. Unit tests also include higher system dimensions 16, 24 and 32 and the exact zero-budget product case.

## Prior-art boundary

This bound is established open-quantum-systems information-flow mathematics. The trace-distance information-backflow program was introduced by Breuer, Laine and Piilo (PRL 103, 210401, 2009), and the explicit role of environmental distinguishability and system-environment correlations in bounding local distinguishability increase appears in Laine, Piilo and Breuer and subsequent reviews. Therefore the result is used here only as a PDT consistency/resource-accounting law, not as a novelty claim.

Prior-art anchors checked in this cycle:

- Breuer, Laine & Piilo, Phys. Rev. Lett. 103, 210401 (2009), DOI 10.1103/PhysRevLett.103.210401.
- Laine, Piilo & Breuer, Phys. Rev. A 81, 062115 (2010), DOI 10.1103/PhysRevA.81.062115.
- Breuer et al., Rev. Mod. Phys. 88, 021002 (2016), arXiv:1505.01385.
