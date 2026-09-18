# Cycle 234 — Refinement-Lattice Valuation Nonuniqueness No-Go

## Target
PDT-II target (4), with direct consequences for targets (1), (3), and (5): attack the Cycle-233 survivor that a PDT-native refinement lattice might uniquely separate unique distinction, redundant revelation, and synergistic joint revelation.

## Candidate attacked
Suppose two accessible records X,Y concern the same target H. A tempting PDT move is to require a nonnegative four-atom refinement accounting

- R: distinction redundantly available from either X or Y,
- U_X: distinction unique to X,
- U_Y: distinction unique to Y,
- S: distinction available only jointly (synergy),

with observable cumulative values

    D_X  = R + U_X,
    D_Y  = R + U_Y,
    D_XY = R + U_X + U_Y + S.

Question: do refinement order, nonnegativity, and the three cumulative distinction values determine the atoms uniquely?

## Exact theorem: one free degree of freedom remains
Solving the three equations gives

    U_X = D_X - R,
    U_Y = D_Y - R,
    S   = D_XY - D_X - D_Y + R.

Nonnegativity is equivalent to

    max(0, D_X + D_Y - D_XY) <= R <= min(D_X, D_Y).

Therefore whenever this interval has positive width, there is a continuum of distinct nonnegative atomizations with exactly the same cumulative refinement data. The refinement lattice and cumulative values alone do not select a unique redundancy/synergy decomposition.

## Smallest decisive witness
Take

    D_X = 1/2,
    D_Y = 1/2,
    D_XY = 1.

Then every R in [0,1/2] is admissible and yields

    (R,U_X,U_Y,S) = (R, 1/2-R, 1/2-R, R).

Two exact completions are

    R=0:   (0, 1/2, 1/2, 0),
    R=1/2: (1/2, 0, 0, 1/2).

Both reproduce the identical observable cumulative triple (1/2,1/2,1), satisfy nonnegativity, and respect the same bivariate refinement lattice, yet assign radically different unique/redundant/synergistic content.

Hence

    refinement lattice + cumulative distinction + nonnegativity
        does NOT imply
    unique unique/redundant/synergy valuation.

This is an algebraic identifiability failure, not a numerical artifact.

## Dimension and embedding audit
The witness needs only a binary target/record subexperiment, so it embeds into every finite physical alphabet/capacity n>=2 by restricting to two labels. Thus the obstruction applies exactly for n=2,...,12 and all higher finite n. n=1 is degenerate. Enlarging dimension cannot restore uniqueness without an additional selector axiom.

The proof is independent of Euclidean/trace/TV norm choice because it begins after the three operational cumulative values have been fixed. It is likewise independent of reversible-group choice, tensor convention, Markovianity, or pure/mixed representation: any realization producing the same cumulative triple inherits the underdetermination at the accounting layer.

## Prior-art boundary
This nonuniqueness is not a PDT discovery. Partial-information-decomposition (PID) literature already organizes redundancy, unique information, and synergy on redundancy/partial-information lattices, and different redundancy definitions induce different atomizations. Williams and Beer (2010) introduced a nonnegative redundancy-lattice decomposition; later work explicitly studies alternative redundancy/synergy measures and gain/loss lattices. Möbius inversion uniquely recovers atoms only *after* a cumulative redundancy function on the lattice has been specified; it does not choose that function.

Accordingly, importing a PID redundancy functional, Shannon/von-Neumann entropy, co-information, or a Möbius transform and renaming it PDT distinction would be IMPORTED/KNOWN.

## Consequences for PDT-II
1. A refinement lattice can organize admissible comparisons but cannot by itself supply the missing physical selector.
2. A putative PDT conservation/revelation law cannot claim unique redundant/synergistic terms unless PDT independently derives an additional operational axiom fixing R.
3. No PDT-vs-QM same-input probability difference can be inferred from choosing one atomization over another: the observable cumulative data are identical by construction.
4. No experimentally distinctive inequality follows from the lattice alone if its value changes with the unconstrained redundancy selector.
5. This route provides no n=3 selection: the binary witness embeds in n=3 and every n>=2.

## Status
- Unique atomization from bivariate refinement lattice + cumulative values + nonnegativity: **FALSIFIED**.
- General feasible interval for the redundancy atom: **PROVED**.
- Smallest decisive binary witness: **PROVED**.
- Exact embedding through n=2,...,12 and all finite n>=2: **PROVED**.
- PID/Möbius/redundancy-lattice machinery: **IMPORTED/KNOWN** as prior-art boundary.
- PDT-native operational selector fixing R without importing an information measure: **OPEN**.
- Same-input PDT != QM prediction from this accounting alone: **FALSIFIED**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Stronger surviving obligation
The next candidate must not merely postulate a lattice valuation. PDT must derive an independently testable operational condition that fixes the free redundancy parameter (and its multivariate analogues) from PDT primitives. That selector must then be adversarially compared with existing PID redundancy axioms/measures, Blackwell sufficiency, common information, decision-theoretic information, and Möbius/inclusion-exclusion constructions. If no PDT-native selector survives, the refinement/revelation programme remains an organizational language rather than a predictive physical law.
