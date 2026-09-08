# Cycle 011 — Two-point isotropy closes the SU PCC loophole

## Status

**CONDITIONAL PDT DIMENSION THEOREM / GROUP-ACTION MATHEMATICS IMPORTED-KNOWN / NOT A BREAKTHROUGH CLAIM**

## Motivation

The earlier Pairwise Calibration Closure (PCC) route required full connected isotropy `SO(n)`. That was too strong: `SU(2)` on `R^4` and `SU(3)` on `R^6` are connected, noncommuting, sphere-transitive PCC counterexamples.

This cycle tests a weaker and more operational symmetry requirement.

### Two-point isotropy (TPI)

Fix a pure distinction direction `x`. For any two pure directions `y,z` at the same Euclidean angle from `x`, there is an allowed reversible transformation that fixes `x` and maps `y` to `z`.

Equivalently, the stabilizer of `x` acts transitively on each angular shell; in particular it acts transitively on the unit sphere in `x^perp`.

TPI expresses "no preferred azimuth around a fixed distinction". It is strictly stronger than sphere transitivity and strictly weaker than assuming the full group `SO(n)`.

## Conditional theorem

Assume an elementary distinction body is a Euclidean ball `B^n`, its connected reversible group acts effectively and linearly, and:

1. **TPI** — two-point isotropy as above;
2. **PCC** — one ordered pair of independent elementary reference distinctions determines a reversible control uniquely, i.e. the generic two-reference stabilizer is trivial;
3. **NCR** — the connected reversible dynamics are genuinely noncommuting.

Within the standard classification of compact connected linear sphere actions, these conditions leave only real dimension

`n = 3`.

### Standard orthogonal family

For `SO(n)` the pointwise stabilizer of two orthonormal references is `SO(n-2)`. PCC therefore requires `n <= 3`. NCR excludes `n=1,2`, leaving `n=3`.

### Earlier SU counterexamples

The natural `SU(2)` action on `R^4` and `SU(3)` action on `R^6` can satisfy PCC, but they fail TPI. After one real unit vector is fixed, the remaining stabilizer preserves additional complex structure and is not transitive on the full real orthogonal sphere. Thus the previous higher-dimensional PCC loophole is removed without postulating the full `SO(n)` group.

### Exceptional isotropic actions

The standard exceptional chains are

- `G2 -> SU(3) -> SU(2)` on `R^7`; after fixing two orthonormal references a nontrivial `SU(2)` stabilizer remains.
- `Spin(7) -> G2 -> SU(3)` on `R^8`; after fixing two orthonormal references a nontrivial `SU(3)` stabilizer remains.

Hence both fail PCC even though they satisfy the relevant isotropy condition.

The executable audit encodes these stabilizer dimensions and scans the `SO(n)` family through arbitrary chosen dimension limits.

## What this does and does not establish

This is a real strengthening of the dimension-selection program because the assumption "full `SO(n)` isotropy" can be replaced by the weaker TPI condition while still eliminating the already-found `SU(2)`/`SU(3)` counterexamples and the exceptional `G2`/`Spin(7)` cases.

It is **not** yet a PDT breakthrough because:

- the classification and stabilizer chains are established Lie/group-action mathematics;
- TPI and PCC are not yet derived from primitive PDT composition/resource principles;
- no same-input prediction differing from standard quantum mechanics follows from this theorem alone.

## Kill criterion for the next cycle

Search for any compact connected effective linear action on a Euclidean sphere that satisfies TPI + PCC + NCR in real dimension `n != 3`. Any such action falsifies the conditional theorem as currently formulated. If none exists under the complete classification, the remaining task is physical: derive TPI and PCC non-circularly from PDT primitives.
