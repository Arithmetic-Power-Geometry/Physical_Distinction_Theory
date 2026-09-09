# Cycle 027 — Single-Plane Reversibility dimension filter

## Result and status

**Classification: PROVED + CONDITIONAL + IMPORTED/KNOWN. Not a BREAKTHROUGH CANDIDATE.**

Let the elementary distinction space be Euclidean, `V = R^n`, and let its full connected reversible isotropy be `SO(n)`. Introduce the candidate PDT control axiom:

**Single-Plane Reversibility (SPR).** Every allowed infinitesimal reversible generator rotates at most one independent two-plane at first order. Matrix-wise, every `A in so(n)` has `rank(A) <= 2`.

Also retain **Noncommuting Reversibility (NCR):** the connected reversible dynamics is non-abelian.

Then

`SPR + NCR  <=>  n = 3`.

This is an exact conditional dimension filter, not a derivation from existing PDT axioms.

## Proof

The Lie algebra of `SO(n)` is the vector space `so(n)` of real skew-symmetric `n x n` matrices. Every such matrix is orthogonally reducible to independent `2 x 2` rotation blocks plus, in odd dimension, one zero direction. Therefore its rank is even and the maximum possible rank is

`2 floor(n/2)`.

Hence every generator has rank at most two iff `n <= 3`. For each `n >= 4`, the explicit matrix

`A = J_12 + J_34`, where `J = [[0,-1],[1,0]]`,

is skew-symmetric and has rank four, so SPR fails.

For the full connected isotropy, `so(1)` is trivial, `so(2)` is one-dimensional and abelian, while `so(n)` is non-abelian for every `n >= 3`. Thus NCR excludes `n=1,2`. Combining the two statements leaves exactly `n=3`.

## Falsification / adversarial checks

- Exact dimension audit: `n=1..12`.
- Formula-level tests: `n=1..1000`.
- Explicit rank-four counterexample: all `n>=4`; tests include `4..12,16,24,32,64,128`.
- Random skew-generator stress test: 200 fixed-seed draws per dimension for `n=1..12`; no false violation occurred where SPR is mathematically predicted to hold.
- Higher dimensions are not inferred from random search: the embedded `J_12 + J_34` witness is exact for every `n>=4`.

## Interpretation for PDT

SPR is operationally sharper than Generator Economy. Generator Economy only bounds the number of independent controls. SPR instead constrains the *structure of every one-parameter control*: an elementary reversible control may couple only one distinction plane at first order. In three dimensions this is automatic; in four or more dimensions full isotropy contains genuine simultaneous independent-plane generators.

The important remaining question is whether SPR follows from a genuinely PDT-native principle about elementary distinction changes, resource locality, calibration, or composition. Until such a derivation or independent experiment exists, SPR is an additional axiom and the result must remain CONDITIONAL.

## Prior-art boundary

The mathematical inputs are standard: `so(n)` consists of real skew-symmetric matrices; real skew-symmetric matrices have orthogonal `2 x 2` block canonical form; and `so(n)` is non-abelian from `n=3` onward. Therefore no historical novelty is claimed for the mathematics. The only PDT-specific element is proposing SPR as a physically interpretable control axiom and using it as a transparent dimension-selection diagnostic.

## Breakthrough gate

**Not promoted.** To become a breakthrough candidate, a future cycle would need to derive SPR (or a weaker sufficient substitute) from independent PDT primitives without smuggling in three-dimensional rotation structure, and then survive alternative reversible-group and composite-system counterexamples.
