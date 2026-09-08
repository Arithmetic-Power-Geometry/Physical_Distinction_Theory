# Cycle 011 — Two-Point Isotropy + Pairwise Calibration dimension filter

## Status

**CONDITIONAL / IMPORTED-KNOWN MATHEMATICS / NOT A BREAKTHROUGH CLAIM**

This cycle weakens the earlier assumption of full connected isotropy `SO(n)` to an operationally phrased symmetry requirement while preserving an `n=3` filter inside the audited compact connected linear sphere actions.

## Two-Point Isotropy (TPI)

Let the pure distinction directions form the unit sphere of a Euclidean distinction space. TPI requires that, after fixing one pure distinction `x`, the reversible stabilizer of `x` acts transitively on all pure directions making the same angle with `x`. Operationally: once one distinction is fixed, there is no preferred azimuth around it.

TPI is stronger than ordinary sphere transitivity. The earlier `SU(2)` on `R^4` and `SU(3)` on `R^6` PCC counterexamples are sphere-transitive but do not satisfy this stronger isotropy requirement.

## Pairwise Calibration Closure (PCC)

PCC requires an ordered pair of independent elementary reference states to determine a reversible control uniquely; equivalently, the pointwise stabilizer of a generic independent pair is trivial.

For the orthogonal family, fixing two independent vectors leaves `SO(n-2)`. Hence PCC holds only for `n<=3`. Noncommuting connected reversibility excludes `n=2`, leaving `n=3`.

## Exceptional TPI stress cases

The important exceptional actions do not rescue higher dimensions:

- `G2` acts transitively on `S^6` with stabilizer `SU(3)`. The latter acts transitively on the tangent `S^5`, so this action passes TPI. Fixing a second independent direction leaves `SU(2)`, of dimension 3; therefore PCC fails in real dimension 7.
- `Spin(7)` acts transitively on `S^7` with stabilizer `G2`, and `G2` is transitive on the tangent `S^6`. Thus this action also passes TPI. Fixing a second independent direction leaves `SU(3)`, of dimension 8; therefore PCC fails in real dimension 8.

Accordingly, among the standard compact connected linear sphere actions surviving the TPI filter, the audited conjunction

`TPI + PCC + genuinely noncommuting connected reversibility`

selects real dimension 3.

## Why this is not yet a breakthrough

The stabilizer chains and classification of homogeneous sphere actions are established mathematics. More importantly, PDT has not yet derived TPI or PCC from a more primitive distinction/composition/resource law. Treating either principle as an axiom would therefore make the result conditional.

The genuine target is a non-circular derivation such as

`PDT primitive operational equivalence -> TPI`

and

`primitive distinction pair as a complete calibration resource -> PCC`,

without assuming orthogonal geometry, ordinary spatial rotations, complex quantum structure, or a hidden equivalent of three-dimensionality.

## Kill-test result

This cycle also corrects an over-strong inference: ordinary sphere transitivity is insufficient. Proper transitive subgroups such as `SU(m)` supply higher-dimensional counterexamples. TPI is the minimum stronger symmetry condition currently surviving that kill test; it is not asserted to be uniquely minimal.

## Computational audit

- `pdt_two_point_isotropy.py`
- `tests/test_pdt_two_point_isotropy.py`
- `results/tpi_pcc_ncr_dimension_audit.csv`
- `results/tpi_pcc_ncr_status.json`

The code checks the `SO(n-2)` stabilizer dimension through `n=100`, audits real dimensions 2–12, and includes the `G2` and `Spin(7)` exceptional cases.

## Prior-art anchors checked in this cycle

- J. Daura Serrano, M. Kohn, M.-A. Lawn, *G-invariant spin structures on spheres*, Annals of Global Analysis and Geometry 62 (2022), for compact connected transitive sphere actions.
- Standard homogeneous-space identities `S^6 = G2/SU(3)` and `S^7 = Spin(7)/G2`, together with the stabilizer chain `SU(3)/SU(2)=S^5`.
- Existing classifications of compact connected two-point homogeneous spaces. These prevent presentation of the group-action mathematics as PDT novelty.
