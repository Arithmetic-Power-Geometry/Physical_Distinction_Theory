# Cycle 098 — Compatible refinement with defect creation

## Question attacked

Cycle 097 proved a fixed-defect-space revelation law but found that hidden dimension can increase when a refined resource window admits new defect directions. This cycle asks whether a sharper theorem survives when the defect space itself grows.

## Exact hypotheses

Let the coarse admissible defect space be a finite-dimensional vector space `U`, embedded in a refined defect space `V`. Write

`q = dim(V/U)`.

Let coarse operational records be represented by

`A : U -> Y`

and refined records by

`B : V -> Z`.

The required compatibility condition is that old records remain recoverable from refined records on inherited defects:

`A = P o (B|_U)`

for some linear postprocessing `P : Z -> Y`.

This is weaker than literal row retention. It says refinement may add or reorganize records, but it may not erase the operational information already available on `U`.

## Theorem — defect-creation/revelation accounting

Define

- `r = rank(A)`,
- `r_i = rank(B|_U)`,
- `r_f = rank(B)`,
- `h = dim(U)-r`,
- `h_i = dim(U)-r_i`,
- `h_f = dim(V)-r_f`,
- `g = r_i-r`,
- `v = r_f-r_i`.

Compatibility implies `ker(B|_U) subset ker(A)`, hence `g >= 0`.

Adding at most `q` domain directions can increase rank by at most `q`, hence

`0 <= v <= q`.

Rank-nullity gives the exact balances

`r_f-r = g+v`

and

`h_f-h = q-g-v`.

Therefore

`r_f >= r`

and

`h_f <= h+q`.

So Cycle 097's fixed-space hidden monotonicity is the special case `q=0`. When `q>0`, hidden dimension may rise, but by no more than the number of genuinely new defect directions.

## Interpretation

The result separates three effects that Cycle 097 mixed together:

1. **Inherited revelation** `g`: formerly hidden coarse defects become visible.
2. **Defect creation/admission** `q`: refinement enlarges the admissible defect space.
3. **New-sector visibility** `v`: some of those newly admitted directions are already resolved by refined records.

The exact ledger is

`Delta hidden = created - inherited-revealed - new-visible`.

This is an accounting identity under the hypotheses, not yet a physical conservation law.

## Sharpness

The upper bound is sharp. If a coarse two-dimensional space is fully visible and refinement adds two completely unobserved defect directions, hidden dimension increases by exactly two.

Inherited revelation can also dominate creation, so hidden dimension can decrease.

## Decisive boundary counterexample

Drop record compatibility while keeping the same one-dimensional defect space:

- coarse `A=[1]`, rank 1;
- purported refined `B=[0]`, rank 0.

Then revealed rank falls from 1 to 0. Thus the claim

> revealed rank is nondecreasing under every process labelled resource refinement

is **FALSIFIED** without a compatibility/no-erasure premise.

This is the smallest possible nonzero-dimensional counterexample.

## Stress tests

Canonical compatible constructions were tested for defect dimensions

`1,...,12,16,24,32,48,64,96,128`

and quotient growth `q` in representative values up to 4, producing 74 cases. All satisfy both exact balance identities and both monotonic/bound inequalities.

A separate seeded randomized audit tested 400 compatible integer-matrix refinements up to coarse dimension 64 and added-defect dimension 8; no violation was found.

The local Cycle-098 unit suite passes 6/6 tests.

## Prior-art boundary

The mathematical proof is finite-dimensional rank-nullity and exact-sequence/filtration reasoning. Nested vector spaces linked by compatible linear maps are standard in filtered linear algebra and persistence-module constructions. This cycle therefore makes **no mathematical novelty claim** for the abstract theorem.

The potentially PDT-specific task is different: derive from PDT primitives why increasing a physical resource window induces (i) a consistent embedding of inherited defect directions and (ii) a compatible record map. Those conditions must not be inserted solely to obtain monotonicity.

## Classification

- Defect-creation/revelation balance: **PROVED, CONDITIONAL, IMPORTED/KNOWN**
- Revealed-rank monotonicity under compatible refinement: **PROVED, CONDITIONAL, IMPORTED/KNOWN**
- Hidden-growth bound `Delta hid <= dim(V/U)`: **PROVED, CONDITIONAL, IMPORTED/KNOWN**
- Unqualified revealed-rank monotonicity without record compatibility: **FALSIFIED**
- Dimension/random stress: **NUMERICALLY SUPPORTED**
- PDT-native derivation of embedding + compatibility: **OPEN**
- Same-input PDT-vs-QM quantitative departure: **OPEN**
- **BREAKTHROUGH CANDIDATE: NO**

## Next strongest obligation

Test whether PDT's existing resource-quotient construction itself supplies the required compatibility diagram. If it does, the present accounting law becomes a derived theorem inside that model; if not, record the smallest quotient/composition counterexample rather than postulating compatibility.
