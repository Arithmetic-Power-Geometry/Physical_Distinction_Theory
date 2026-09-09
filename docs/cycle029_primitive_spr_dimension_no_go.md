# Cycle 029 — Primitive-generator SPR dimension-selection no-go

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN**. Not a breakthrough candidate.

## Question attacked

Cycle 027 obtained a conditional three-dimensional filter by combining:

1. **Single-Plane Reversibility (SPR):** every infinitesimal reversible generator has rank at most 2; and
2. **Noncommuting Reversibility (NCR):** at least two allowed infinitesimal reversible generators do not commute.

Cycle 028 then showed that universal SPR is not stable under ordinary tensor-product spectator extension, because `rank(A ⊗ I_B)=rank(A)d_B`.

This cycle asks whether the physically more natural interpretation — *primitive controls are single-plane* — can rescue the n=3 derivation.

## Theorem (primitive-generator no-go)

Let

\[
J_{ij}=E_{ij}-E_{ji},\qquad 1\le i<j\le n.
\]

Then `{J_ij}` is the standard coordinate-plane basis of `so(n)`. Every nonzero `J_ij` has rank exactly 2. Hence `so(n)` admits a complete primitive generating basis satisfying single-plane rank for **every n>=2**.

For every `n>=3`, choose `J_12` and `J_23`. Their commutator is nonzero (indeed proportional, up to convention/sign, to `J_13`). Thus NCR also holds for every `n>=3`.

Therefore

\[
\boxed{\text{primitive SPR}+\text{NCR holds for every }n\ge3.}
\]

It follows that

\[
\boxed{\text{primitive SPR}+\text{NCR does not select }n=3.}
\]

This is an infinite counterexample family, not merely a numerical exception.

## Consequence for the Cycle-027 claim

The apparent uniqueness of `n=3` came from the **universal** quantifier over all elements of `so(n)`. For `n>=4`, linear combinations such as `J_12+J_34` have rank 4, so universal SPR fails. But if "elementary" means primitive available controls — the interpretation suggested by the physical wording — then every dimension has a rank-2 plane-rotation basis.

Thus the three-dimensional selection cannot currently be regarded as a PDT-native derivation unless PDT independently justifies why *every linear combination in the Lie algebra*, rather than only primitive controls, must itself count as elementary.

## Factor-local repair also fails as a standalone selector

For a spectator of dimension `m`,

\[
\frac{\operatorname{rank}(A\otimes I_m)}{m}
=\operatorname{rank}(A).
\]

This normalization is useful because it removes spectator multiplicity, but it simply returns the local rank. Applied to the primitive basis, it therefore remains 2 in every `n>=2`; with NCR it again accepts every `n>=3`.

So factor-local SPR is composition-compatible for local spectator lifts but has **no unique n=3 selecting power by itself**.

## Audit

The committed table covers `n=1..12` exactly. Unit tests verify the rank-2 basis and NCR threshold through `n=100`, plus explicit high-dimensional witnesses at 24 and 64 dimensions and spectator-normalized rank checks.

No random simulation is needed for the central claim because the counterexample family is analytic and exhaustive in dimension.

## Prior-art / novelty review

The ingredients are standard: `so(n)` is the Lie algebra of real skew-symmetric matrices with commutator bracket, and coordinate-plane/Givens rotations act in a single two-dimensional coordinate plane. Consequently this cycle makes **no novelty claim** for the mathematics.

The defensible PDT advance is the no-go conclusion: the natural primitive-control interpretation of SPR cannot produce a unique three-dimensionality result.

## Research direction after the no-go

A viable n=3 principle must constrain something not shared by the standard plane-rotation generating structure of all `SO(n)`. Candidates worth attacking next include genuinely compositional constraints on interaction generators, closure costs under restricted resources, distinction-flow invariants that depend on subsystem structure, or experimentally meaningful constraints that cannot be satisfied by the coordinate-plane basis in every dimension.
