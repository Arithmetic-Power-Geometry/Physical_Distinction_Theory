# Transitive-isotropy dimension no-go

## Status: DECISIVE FALSIFICATION / IMPORTED-KNOWN group-action classification

### Question
Could PDT rescue the pairwise-calibration route by deriving only the apparently natural statement that the connected reversible group acts transitively on the unit distinction sphere, rather than assuming the full rotation group `SO(n)`?

### Result
No. Sphere transitivity is far too weak to recover full rotational isotropy, and it does not rescue dimension selection.

The classical Montgomery-Samelson/Borel classification of compact connected effective groups acting transitively on spheres contains, besides the full orthogonal family, proper subgroups including `U(m)`, `SU(m)`, `Sp(m)`, `Sp(m)Sp(1)`, `G2`, `Spin(7)` and `Spin(9)` in their standard transitive sphere actions. In particular,

`SU(m)/SU(m-1) ~= S^(2m-1)`.

Thus the natural real action of `SU(m)` on `C^m ~= R^(2m)` is transitive on the entire unit sphere.

For the same action, fixing `r` complex-linearly independent reference vectors pointwise leaves stabilizer `SU(m-r)`. Therefore the natural base size is `m-1`. Pairwise Calibration Closure (PCC), meaning that two independent references determine the control, is consequently satisfied for `m<=3`.

This gives explicit higher-dimensional counterexamples satisfying all three properties:

1. connected noncommuting reversible dynamics;
2. transitivity on the full unit distinction sphere;
3. PCC with at most two independent reference states.

The examples are

- `SU(2)` on `C^2 ~= R^4`, real state-space dimension `n=4`, sphere `S^3`, base size `1`;
- `SU(3)` on `C^3 ~= R^6`, real state-space dimension `n=6`, sphere `S^5`, base size `2`.

Hence

`connected + noncommuting + sphere-transitive + PCC  !=>  n=3`.

### Consequence for PDT
The phrase "full isotropy" must not be weakened to mere transitivity/homogeneity of pure distinction directions. To obtain the previous `SO(n)` PCC theorem, PDT would need a genuinely stronger primitive that fixes the reversible group itself (or its stabilizer structure), not just orbit transitivity.

Equivalently, a viable native chain must establish something close to

`PDT primitives -> reversible group = SO(n)`

or another independently justified group restriction that excludes the transitive `SU(2)` and `SU(3)` actions without encoding three-dimensionality by hand.

### Prior-art discipline
The transitive-sphere classification is established mathematics, historically associated with Montgomery-Samelson and Borel. This note makes no novelty claim for that classification. Its PDT value is as a kill test: it closes a tempting but invalid derivation route from sphere homogeneity to three-dimensionality.

Recent accessible summaries of the classification include the 2022 paper by Daura Serrano, Kohn and Lawn on compact connected groups acting transitively on spheres, and standard homogeneous-space references.

### Classification
- mathematical ingredients: IMPORTED/KNOWN;
- PDT implication: PROVED no-go;
- dimension-selection breakthrough: NOT ACHIEVED;
- research route eliminated: sphere transitivity + PCC + noncommutativity.
