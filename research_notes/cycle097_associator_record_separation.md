# Cycle 097 — Separating operational records and the revelation-rank law

## Question attacked

Cycle 096 showed that the scalar/unit readout cannot see octonionic nonassociativity. This cycle asks the stronger PDT-II question: exactly how much operational record structure is required to certify grouping consistency, and what survives as an exact resource-refinement law?

## Theorem 1 — finite record separation

Let `W` be a fixed finite-dimensional vector space of admissible composition defects (for example, the span of all associators) and let a resource window `R` expose scalar linear records `l_1,...,l_m`. Assemble them into

`L_R : W -> R^m`.

Every nonzero defect is detected by at least one record **iff** `L_R|_W` is injective. Equivalently,

`rank(L_R|_W) = dim(W)`.

Therefore `m >= dim(W)` is necessary for universal linear separation. This is rank-nullity, not a PDT novelty claim.

## Exact octonion stress test

Using the repository's existing Cayley-Dickson convention, all 512 ordered basis associators were enumerated exactly in integer coordinates.

- 168/512 basis triples have nonzero associator.
- Every associator has zero scalar component.
- The associators span rank 7.
- Explicit ±2 e_r witnesses exist for every imaginary basis direction `r=1,...,7`.

Hence the scalar record has rank 0 on the associator sector. Six or fewer independent scalar linear records necessarily leave a hidden direction; seven independent records spanning the imaginary dual are sufficient.

This sharpens Cycle 096: the failure is not merely that one scalar happens to miss one counterexample. The scalar/unit projection misses an entire seven-dimensional associator sector.

## Theorem 2 — resource revelation law

For fixed `W`, define

`rev_R = rank(L_R|_W)`

and

`hid_R = dim(W ∩ ker L_R)`.

Then exactly

`rev_R + hid_R = dim(W)`.

If `R'` refines `R` only by adding records (the old record span is retained), then

`rev_R' >= rev_R`,
`hid_R' <= hid_R`,
and
`Delta rev = - Delta hid`.

This is an exact conservation/accounting identity for revealed versus hidden defect dimension. It is **CONDITIONAL** on a fixed defect space and nested record refinement.

## Boundary / decisive counterexample

The naive statement "hidden defect dimension must decrease under every resource refinement" is false if refinement can also enlarge the admissible defect space. Example:

- coarse `W = span(e1)` with record `e1*`: hidden dimension 0;
- refined `W' = span(e1,e2)` with the same record available: hidden dimension 1.

Thus PDT needs a compatibility axiom relating `W_R` across resource windows before promoting hidden-dimension monotonicity to a physical law.

## Dimension stress

The rank/nullity theorem is dimension-independent. Canonical exact tests cover defect dimensions 1–12 and 16, 24, 32, 48, 64, 96, 128. With `n-1` independent coordinate records in an `n`-dimensional defect space, exactly one hidden dimension survives in every tested dimension.

## Prior-art boundary

The mathematical core is standard finite-dimensional linear algebra and the operational interpretation parallels informationally complete measurements/tomography: complete observations must separate the relevant operational states or directions. Octonion nonassociativity/alternativity is also classical. Therefore this cycle is **not** promoted as a breakthrough.

## Classification

- Finite record-separation theorem: **PROVED, IMPORTED/KNOWN**
- Universal certification by fewer than `dim(W)` scalar records: **FALSIFIED**
- Seven-dimensional octonion associator span: **PROVED, NUMERICALLY_SUPPORTED, IMPORTED/KNOWN**
- Fixed-space revelation law: **PROVED, CONDITIONAL, IMPORTED/KNOWN**
- Unqualified refinement monotonicity when the defect space changes: **FALSIFIED**
- PDT-native derivation of the physically available record family: **OPEN**
- Same-input PDT-vs-QM quantitative departure: **OPEN**
- **BREAKTHROUGH CANDIDATE: NO**

## Next strongest obligation

Do not postulate tomography merely to eliminate the octonionic sector. Derive from PDT primitives what records a finite resource window physically exposes, including how the record span and admissible defect space transform under composition/refinement. Only then test whether the derived structure excludes `n=7` and whether it yields a same-input quantitative prediction unavailable to ordinary quantum theory.
