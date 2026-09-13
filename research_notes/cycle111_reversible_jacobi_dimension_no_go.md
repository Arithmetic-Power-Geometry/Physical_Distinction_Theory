# Cycle 111 — Reversible-composition Jacobi is dimension-blind

## Question attacked
Can PDT obtain a non-circular `n=3` selector by deriving Jacobi coherence from reversible operational composition?

## Result
No. In any associative matrix realization, the commutator bracket satisfies Jacobi by direct expansion. The tangent algebra of orthogonal reversible transformations is `so(n)`, the skew-symmetric matrices, and the commutator closes in `so(n)` for every `n`.

Therefore a derivation of Jacobi from smooth reversible composition would be physically natural but dimension-blind. The smallest non-3 witness is already `so(2)`, which satisfies Jacobi exactly.

The familiar equality

`dim so(n) = n(n-1)/2 = n`

has positive solution only `n=3`. But using this to select dimension requires an additional physical premise identifying the complete infinitesimal generator sector with an `n`-dimensional state/vector sector. That premise is not implied by reversibility, smoothness, closure, or Jacobi.

## Classification
- Matrix commutator Jacobi: **PROVED + IMPORTED/KNOWN**.
- `so(n)` commutator closure: **PROVED + IMPORTED/KNOWN**.
- Jacobi as a dimension selector: **FALSIFIED**.
- Generator/state dimension identification: **OPEN**.
- Breakthrough candidate: **NO**.

## Validation
The local regression suite passed 5/5. Exact basis audits through `n=6` and deterministic structured certificates at `n=7..12,16,24,32,48,64,96,128` showed zero Jacobi and skew-closure failures. A seeded 250-case integer-matrix audit over `n=2..12,16,24` also showed zero failures. These computations audit the implementation; the all-dimension claim rests on the elementary algebraic proof.

## Prior-art boundary
Lie algebras and the Jacobi identity are standard; `SO(n)` has Lie algebra `so(n)` and dimension `n(n-1)/2`. No novelty is claimed for those facts. The PDT contribution of this cycle is a no-go boundary: deriving Jacobi from reversible composition, even if successful, does not by itself close the non-circular `n=3` target.

## Strongest surviving obligation
Derive or falsify a PDT-native reason that primitive reversible generators are exhausted by a state-like `n`-dimensional sector, or find a different pre-Hodge dimension-sensitive operational principle. Do not import generator/state identification merely to recover `n=3`.
