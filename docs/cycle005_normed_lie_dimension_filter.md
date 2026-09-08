# Cycle 005 — Normed-Lie interaction dimension filter

## Status: CONDITIONAL / IMPORTED-KNOWN MATHEMATICS / PDT PHYSICAL AXIOM OPEN

This cycle asks a narrower question than the failed CEU/CER/RDE route: what additional *interaction* structure would be strong enough to select dimension three once the elementary PDT state body is already Euclidean?

Consider a bilinear antisymmetric product

`x × y : R^n × R^n -> R^n`

with the following properties:

1. `x × y` is orthogonal to both `x` and `y`;
2. `||x × y||^2 = ||x||^2 ||y||^2 - <x,y>^2` (normed cross-product identity);
3. the product is nontrivial;
4. it satisfies the Jacobi identity, so it can serve as a Lie bracket for continuous reversible interaction generators.

Known vector-cross-product classification restricts nontrivial normed binary cross products to dimensions 3 and 7 (apart from trivial dimensions 0 and 1). The standard 3D product satisfies Jacobi. The 7D octonionic cross product obeys the norm and orthogonality identities but fails Jacobi. Therefore these four algebraic requirements leave only

`n = 3`.

This is a genuine *dimension filter*, but it is **not yet a PDT-native derivation of n=3**. The missing step is physical: PDT must independently justify why elementary distinction interactions should be represented by exactly such a normed bilinear antisymmetric Lie product. Without that justification, importing the cross-product classification would merely relocate the reconstruction assumption.

## Computational audit

`pdt_dimension_filter.py` implements the ordinary 3D cross product and an explicit 7D octonionic/Fano-plane product. Deterministic/random audits show:

- dimension 3: norm, orthogonality and Jacobi residuals are numerical zero (random 2000-trial max Jacobi residual about `4e-15`);
- dimension 7: norm and orthogonality remain numerical zero, but the basis-vector maximum Jacobi residual is exactly `3`, with large nonzero random residuals;
- dimensions 1–12 are catalogued in `results/cycle005_dimension_filter.csv` using the known classification, leaving only 3 after the Jacobi filter.

## Prior-art discipline

The mathematical dimension restriction is established and must not be advertised as a new PDT theorem. Classical vector-cross-product/Hurwitz/Brown–Gray theory already gives the 3/7 restriction, and the failure of the Jacobi identity for the seven-dimensional octonionic cross product is standard. The PDT research value of this cycle is diagnostic: it identifies a precise additional physical principle that *would* be sufficient to select n=3, and therefore narrows the search for a PDT-native composition/interaction axiom.

## Kill test for future PDT claims

Any proposed PDT derivation based on this route must answer, without circularly invoking qubits, SO(3), Pauli matrices, or ordinary 3D rotations:

**Why must physically elementary distinction interactions carry a nontrivial norm-preserving bilinear antisymmetric product that closes under Jacobi?**

Until that physical statement is independently derived or experimentally motivated, the route remains CONDITIONAL rather than BREAKTHROUGH.
