# Cycle 266 — Exact-dimension certification boundary

## Target
Non-circular PDT-native `n=3` derivation, after the Cycle 263 hereditary-selector obstruction and Cycle 265 3-vs-7 cross-product falsification.

## Theorem — finite-support lower-bound obstruction
Let `T_n` be an operational theory in ambient dimension `n`. Let a finite protocol `E` use preparations, transformations, effects, records, and a declared resource window `R`. Suppose that for some `k<n` every operational object used by `E` is supported in a `k`-dimensional invariant sector, and that there is a resource-preserving embedding of this sector into `T_n` preserving all probabilities for `E`.

Then the complete probability table of `E` in `T_k` equals that of its embedded realization in `T_n`. Consequently no statistic computed solely from that table can certify that the ambient dimension is *exactly* `k`; it can at most rule out dimensions below the minimum dimension needed to realize the table.

### Proof
For every history/outcome `h` of the finite protocol, probability preservation gives
`P_k(h | E,R) = P_n(h | i(E),i(R))`.
Therefore the full finite probability vectors coincide. Any witness/statistic `W` depending only on that vector has identical value in the two realizations. If `W` certified exact ambient dimension `k`, the embedded `n>k` realization would give the same certificate, a contradiction. QED.

## Corollary for PDT-II n=3
A PDT experiment or inequality whose operational support is contained in a qutrit/3-dimensional sector cannot by itself establish exact ambient `n=3` whenever that sector embeds resource-preservingly into a higher-dimensional admissible model. Exact `n=3` therefore requires at least one independently justified **upper-bound / ambient-sensitive premise**: e.g. a physically derived capacity ceiling, a completeness/maximality condition, or a protocol whose resource accounting necessarily interrogates the entire ambient carrier. Merely producing a witness impossible for `n<=2` is insufficient.

This is stronger than testing another candidate axiom: it separates the PDT-II dimension target into two logically different obligations:
1. **lower bound:** rule out `n<3`;
2. **upper bound:** rule out every `n>3` under the same declared resource semantics.

Any claimed non-circular `n=3` derivation must discharge both.

## Dimension stress
The theorem is analytic for every `n>k`. In particular with `k=3`, the same finite protocol embeds into `n=4,...,12` and arbitrary higher finite `n` whenever the hypotheses hold. Degenerate `n=1,2` are not asserted to realize the protocol; they belong to the lower-bound side of the certification problem.

## Relation to prior cycles
- Cycle 263 proved the general hereditary-selector obstruction.
- Cycle 265 showed that a genuinely ambient-sensitive cross-product axiom still leaves `{3,7}`.
- Cycle 109 showed `cross product + Jacobi` conditionally removes 7, but explicitly recorded that the cross-product and Jacobi premises were not PDT-native.
- Cycle 111 showed Jacobi derived merely from reversible Lie composition is dimension-blind.

Thus importing `cross product + Jacobi` does not solve the present theorem's requirement for a PDT-native upper-bound premise.

## Prior-art boundary
Quantum dimension witnesses are established tools for lower-bounding the Hilbert-space dimension required by observed statistics. Brunner et al., *Phys. Rev. Lett.* 100, 210503 (2008), explicitly introduced dimension witnesses to put lower bounds on dimension. Later prepare-and-measure work likewise derives lower bounds from observed behaviours. Finite-dimensional correlation methods can impose an assumed upper dimension and optimize inside it, but that assumption is not a derivation of the physical ambient dimension.

Accordingly the general lower-bound role of dimension witnesses is **IMPORTED/KNOWN**. The result here is retained as a PDT-II logical no-go/target decomposition, not claimed as a new quantum-information theorem.

## Classification
- Probability invariance under resource-preserving embedding: **PROVED**.
- Finite-support statistic certifies exact ambient dimension without an upper-bound/ambient-sensitive premise: **FALSIFIED**.
- Standard dimension-witness lower-bound interpretation: **IMPORTED/KNOWN**.
- PDT-II exact `n=3` = lower-bound obligation + independently justified upper-bound obligation: **PROVED as a logical requirement under the stated embedding hypotheses**.
- PDT-native upper-bound/capacity premise selecting 3: **OPEN**.
- PDT-native composition law: **OPEN**.
- Same-input `P_PDT != P_QM` after explicitly changing an operational primitive: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
Do not spend further cycles on finite-support lower-bound witnesses as if they could prove exact `n=3`. Attack the missing upper-bound side directly: search for a PDT-native capacity/completeness principle derived from resource refinement that is non-hereditary, survives composition, and does not simply assume the desired carrier dimension.