# Cycle 096 — Scalar-readout associativity does not exclude the octonionic sector

## Target
PDT-II targets (1)/(2): test whether full operational associativity can be weakened to grouping consistency only after projecting the scalar/unit readout.

## Candidate statement
A unital bilinear positive-norm-composing alternative composition, together with

`pi_0((xy)z) = pi_0(x(yz))`,

is sufficient to exclude the n=7 vector sector and retain n=3.

**Status: FALSIFIED.**

## Exact counterexample
Take the octonions `O = R + R^7`, with `pi_0 = Re`. Their associator

`[x,y,z] = (xy)z - x(yz)`

is purely imaginary. Hence

`Re((xy)z) = Re(x(yz))`

for every octonion triple, despite generic failure of full associativity.

With the repository's Cayley-Dickson convention,

`[e1,e2,e4] = 2 e7`.

The full associator therefore has norm 2 while its scalar part is exactly 0.

## Exact and numerical audit
- All 512 ordered octonion basis triples have scalar associator exactly zero.
- 168/512 basis triples have a nonzero full associator.
- Maximum basis associator norm is exactly 2.
- 5,000 normalized random triples (seed 9607) all had full associator norm > 1e-10.
- Maximum random full associator norm: 1.9360994967487146.
- Maximum absolute scalar associator residual: 3.3306690738754696e-16 (floating roundoff).
- Dimension stress ledger retains the requested n=1..12 and higher set 16,24,32,48,64,96,128; under the classical positive-definite real normed-division hypotheses the relevant vector-sector dimensions are 0,1,3,7, and n=7 is the decisive counterexample to scalar-readout selection.

## Consequence for PDT-II
A composition principle checked only through one scalar probability/capacity/unit projection cannot distinguish quaternionic associative composition from octonionic nonassociativity hidden entirely in the non-scalar sector. To exclude n=7 without assuming the answer, PDT must derive either:

1. full operational grouping coherence, or
2. a separating/tomographically complete family of records/effects whose joint action detects every nonzero associator direction.

The second route is now the sharper PDT-native obligation: derive record/effect separation from distinction/resource primitives rather than postulate a quantum operator structure.

## Prior-art boundary
This is **not PDT novelty**. Octonionic nonassociativity, alternativity, the imaginary/vector sector and the composition-algebra boundary are classical. Relevant background includes John C. Baez, *The Octonions* (Bull. AMS; arXiv:math/0105155) and standard composition-algebra/Hurwitz results. The new value of this cycle is only the falsification of a proposed PDT-II weakening and the resulting research constraint.

## Classification
- PROVED — exact scalar invisibility for the explicit basis witness and exact basis audit.
- FALSIFIED — scalar-readout associativity is insufficient to select n=3.
- IMPORTED/KNOWN — octonionic/composition-algebra facts.
- NUMERICALLY SUPPORTED — 5,000 random-triple regression.
- OPEN — derive a PDT-native separating record/effect principle or full grouping coherence.
- BREAKTHROUGH CANDIDATE — **NO**.
