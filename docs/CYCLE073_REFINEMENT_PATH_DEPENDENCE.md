# Cycle 073 — Refinement revelation is path dependent

## Status

**PROVED** (exact qubit witness); **FALSIFIED** (universal path-independent local revelation increment); **IMPORTED/KNOWN boundary** (restricted-measurement distinguishability); **OPEN** (a genuinely PDT-native conservation law).

## Hypotheses

Let a resource window be a nested real operator space of accessible Hermitian observables. For a state pair `(rho,sigma)`, let `D_R` denote optimal binary discrimination advantage restricted to that space. Refinement monotonicity `R subset R' => D_R <= D_R'` is standard and was already audited in Cycle 048.

The candidate killed here is stronger: that each one-step enlargement carries a scalar revelation increment determined only by the size/rank of the enlargement (or otherwise independent of the refinement path), so that equal-size refinement steps reveal equal amounts of distinction.

## Exact smallest witness

Take the qubit states `rho=|0><0|` and `sigma=|1><1|`. Start with constants only, `R0=span{I}`. Compare two chains ending at the same resource space:

* A: `span{I} -> span{I,Z} -> span{I,X,Z}`.
* B: `span{I} -> span{I,X} -> span{I,X,Z}`.

For this pair the distinction is entirely in the Z direction. Therefore the restricted distinguishabilities are exactly

* Chain A: `(0,1,1)`, increments `(1,0)`.
* Chain B: `(0,0,1)`, increments `(0,1)`.

The chains have the same start, same end, and the same dimension pattern `1 -> 2 -> 3`, but their stepwise revelation differs maximally. Hence no universal increment depending only on refinement dimension/rank can be a conservation law.

The only automatic scalar conservation remaining at this level is telescoping:

`sum_k [D(R_{k+1})-D(R_k)] = D(R_final)-D(R_initial)`.

That identity is bookkeeping, not a new physical conservation principle.

## Dimension stress

The qubit witness embeds as a two-dimensional block in every finite dimension `n>=2`, preserving the exact separator. Dimension 1 is degenerate. The executable audit records n=1 through 12 exactly; the proof itself covers every n>=2.

## Consequence for PDT-II

A PDT-native revelation/conservation theorem cannot assign resource-independent scalar 'distinction quanta' to generic refinement steps. Any nontrivial surviving law must depend on state-resource geometry, conditional/orthogonal innovation relative to what is already accessible, or an additional physical structure derived by PDT. Such a law must then be compared against standard conditional expectation, martingale, information-geometric, and resource-theoretic decompositions before novelty is claimed.

No BREAKTHROUGH CANDIDATE is claimed.
