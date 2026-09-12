# Cycle 088 — Composition-stable dimension-3 no-go

## Status

- **PROVED**: tensor-composition closure excludes any universal singleton finite Hilbert dimension `d>1`.
- **FALSIFIED**: the claim that the PDT-II `n=3` target can mean “every allowed finite system has Hilbert dimension exactly 3” while retaining ordinary independent tensor composition.
- **NUMERICALLY SUPPORTED**: exact integer regression over `d=1..12,16,24,32,48,64,96,128` and power-family stress through 12 copies.
- **IMPORTED/KNOWN boundary**: multiplicative composite capacity is standard in quantum theory and operational reconstruction; no historical novelty is claimed.
- **OPEN**: a PDT-native derivation that selects an elementary/indecomposable local factor of dimension three by an independently motivated physical principle.
- **NOT A BREAKTHROUGH CANDIDATE**.

## Hypotheses

Assume only:

1. finite-dimensional system Hilbert spaces;
2. at least one nontrivial allowed system of dimension `d>1`;
3. two independently preparable allowed systems may be composed;
4. the independent composite uses the ordinary tensor product, so `dim(H_A tensor H_B)=d_A d_B`.

No Born-rule assumption, quadratic distinction formula, continuity assumption, symmetry group, or selected numerical constant is required.

## Theorem

Let `D` be the set of allowed finite Hilbert-space dimensions. If `D` is closed under independent tensor composition, then

`d in D  =>  d^k in D` for every integer `k>=1`.

Hence no singleton set `{d}` with `d>1` is tensor-composition closed.

### Proof

Take an allowed system with dimension `d>1`. By closure under independent composition, two copies form an allowed composite of dimension `d^2`. Repeating gives allowed dimensions `d^3,d^4,...`. Since `d^2 != d` for every integer `d>1`, the allowed dimension class cannot be the singleton `{d}`. In particular, if `d=3`, two copies have dimension `9`, not `3`. QED.

## Smallest decisive counterexample to the universal n=3 reading

One qutrit-like system:

`d=3`.

Two independent copies:

`d_AB = 3*3 = 9`.

Thus the pair is already a valid composite counterexample to “every allowed Hilbert space has dimension exactly three.”

## Stronger underdetermination after reinterpretation

A natural repair is to say that `n=3` refers only to an elementary/indecomposable local system type. That interpretation survives the theorem, but composition closure still does not select three.

For every prime `p`, the family

`{1,p,p^2,p^3,...}`

has the same multiplicative closure pattern. Therefore `p=2,3,5,7,11,...` are all models of the same bare closure principle. Selecting `p=3` still requires an additional, independently justified PDT-native physical premise.

This strengthens Cycle 076: not only do the current quadratic/revelation axioms admit every finite dimension, but ordinary composition itself forces a distinction between **elementary local dimension** and **composite Hilbert-space dimension**.

## Stress audit

The executable audit checks

`d=1..12,16,24,32,48,64,96,128`.

For every tested `d>1`, the singleton `{d}` fails tensor closure because `d^2 != d`. The `d=1` case is the unique degenerate singleton satisfying `d^2=d`.

For the target value `d=3`, repeated composition gives

`3,9,27,81,243,729,2187,6561,19683,59049,177147,531441`

through 12 copies.

Adversarial elementary families were also generated for primes `2,3,5,7,11`; all obey the same power-family closure structure.

The tests are regression guards only; the theorem is exact integer algebra.

## Prior-art boundary

This is not a novel quantum-foundations theorem. Composite-system capacity multiplication is built into ordinary tensor-product quantum mechanics. Hardy's operational reconstructions explicitly use **Information Locality**, under which maximal measurements on composites are implemented by maximal measurements on their components, while system capacity remains a system-dependent parameter. The present result is therefore recorded as a PDT consistency boundary, not a novelty claim.

Relevant background:

- L. Hardy, *Reformulating and Reconstructing Quantum Theory*, arXiv:1104.2066.
- L. Hardy, *Reconstructing Quantum Theory*, arXiv:1303.1538.

## Consequence for PDT-II

Target (2) must no longer be phrased as a universal derivation of the Hilbert dimension of every composite system. A defensible target is narrower:

> derive, without encoding the answer, why an **elementary/indecomposable PDT system** should have local capacity/dimension three, while composites inherit dimensions through a separately justified composition law.

Even this narrower target remains **OPEN**. Tensor closure alone cannot distinguish elementary dimension `3` from `2`, `5`, `7`, or other candidates.
