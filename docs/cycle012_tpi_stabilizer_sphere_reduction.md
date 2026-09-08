# Cycle 012 — Stabilizer-sphere reduction for TPI + PCC

## Status

**PROVED CONDITIONAL STRUCTURAL REDUCTION / IMPORTED-KNOWN LIE-GROUP TOPOLOGY / NOT A BREAKTHROUGH CLAIM**

This cycle sharpens the previous TPI+PCC dimension filter and removes the need to inspect the full list of transitive sphere-action families one by one.

## Setup

Let a compact connected effective reversible Lie group `G` act transitively on the pure distinction sphere `S^(n-1)`. Fix a pure distinction `x` and let `H=G_x` be its stabilizer.

- **TPI:** for any nontrivial angle from `x`, `H` is transitive on the equal-angle sphere `S^(n-2)`.
- **PCC:** fixing an ordered generic pair `(x,y)` leaves trivial pointwise stabilizer.

Under TPI+PCC, the `H` action on the equal-angle sphere is both transitive and free. Therefore the orbit map identifies `H` diffeomorphically with `S^(n-2)`.

## First reduction

A connected sphere that is a Lie group can only be `S^1` or `S^3`. Hence

`n-2 in {1,3}`,

so the only local candidates are

`n in {3,5}`.

This also clarifies the `n=2` edge case: with connected `H`, a free/transitive action on the two-point set `S^0` is impossible. Thus TPI itself already removes the connected `n=2` case; an extra noncommutativity assumption is not needed for that exclusion.

## Excluding n=5 without the full sphere-action table

If `n=5`, then `H ~= S^3` and `G/H ~= S^4`. Therefore

`dim(G)=dim(H)+dim(S^4)=3+4=7`.

From the homotopy exact sequence of `H -> G -> S^4`, both `H=S^3` and `S^4` are simply connected, so `G` must be simply connected. A compact connected simply connected Lie group is a product of compact simply connected simple Lie groups. In dimensions below 8 the only nontrivial compact simple factor is `SU(2)` of dimension 3; products therefore contribute dimensions 3, 6, 9, ... and cannot have total dimension 7. Hence the `n=5` branch is impossible.

Therefore

`compact connected effective sphere transitivity + TPI + PCC => n=3`.

The conclusion is stronger than the previous audited statement in two ways: it does not assume full `SO(n)` and it does not require a separate NCR axiom once connected TPI is taken literally.

## Novelty discipline

This is not a PDT breakthrough. The key ingredients—free/transitive group actions, the fact that only `S^1` and `S^3` among connected spheres are Lie groups, the homotopy sequence for homogeneous fibrations, and low-dimensional compact Lie-group classification—are established mathematics. The PDT-specific unresolved step remains deriving TPI and PCC non-circularly from primitive distinction/resource/composition principles.

## Computational audit

- `pdt_tpi_stabilizer_reduction.py`
- `tests/test_pdt_tpi_stabilizer_reduction.py`
- `results/tpi_stabilizer_reduction.csv`
- `results/tpi_stabilizer_reduction_status.json`

The audit scans dimensions 2–12 in the result table and tests the reduction through dimension 100.
