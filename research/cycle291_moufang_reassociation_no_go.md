# PDT-II Cycle 291 — Moufang reassociation no-go

## Target
Test whether a physically weaker reassociation principle than Jacobi can eliminate the n=7 survivor of the normed distinction cross-product programme without simply importing Lie/Jacobi structure.

## Candidate principle
A natural attempted repair is to require sequential distinction composition to obey alternative/Moufang reassociation laws. These laws are attractive operationally because they constrain repeated/overlapping updates while being weaker than full associativity.

## Result
**FALSIFIED:** alternative or Moufang reassociation is insufficient to select n=3.

The unit octonions form a Moufang loop, and imaginary octonions induce the standard 7-dimensional normed cross product. Therefore the same n=7 survivor that violates Jacobi nevertheless satisfies the stronger-than-generic nonassociative Moufang identities at the underlying composition level.

An exact integer regression in `experiments/cycle291_octonion_moufang.py` constructs octonion multiplication from the same Fano orientation used in Cycle 290 and exhaustively checks the Moufang identity

`(x*y)*(z*x) = x*((y*z)*x)`

on all signed basis triples. It also rechecks a nonzero associator/Jacobi witness. Thus Moufang consistency and Jacobi are genuinely separated by the n=7 model.

## Consequence
The implication

`normed distinction composition + alternative/Moufang reassociation => n=3`

is false. Any PDT-native operational axiom intended to derive n=3 must be stronger than alternativity/Moufang consistency and must exclude the octonionic model for an independently physical reason. Merely calling reassociation 'consistent' is ambiguous and insufficient.

A particularly important boundary is that deriving Jacobi from commutators of associative operator composition would recover n=3 only by importing an associative/Lie substrate. That route is mathematically valid but is not yet a PDT-native derivation.

## Prior-art boundary
This is not claimed as new mathematics. The facts that unit octonions form a Moufang loop, imaginary octonions form the simple 7D non-Lie Malcev algebra, and the 7D cross product violates Jacobi are established. The PDT contribution of this cycle is a no-go classification for the proposed dimension-selection route.

## Status
- Alternative/Moufang reassociation as an n=3 selector: **FALSIFIED**.
- Exact n=7 Moufang countermodel: **PROVED / IMPORTED-KNOWN mechanism**.
- Separation `Moufang does not imply Jacobi`: **PROVED / IMPORTED-KNOWN**.
- PDT-native operational derivation of Jacobi: **OPEN**.
- PDT-native n=3 derivation: **OPEN**.
- Same-input PDT-vs-QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Adversarial conclusion
Do not promote any 'path consistency', 'reassociation consistency', or 'repeated distinction consistency' axiom unless its exact operational content is formalized. If it reduces only to alternativity, flexibility, or a Moufang law, n=7 survives.