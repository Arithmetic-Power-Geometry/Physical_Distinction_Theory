# Cycle 011 — Scalar distinction isotropy does not imply TPI

## Status

**PROVED / FALSIFIED ROUTE / IMPORTED-KNOWN group-action mathematics.**

This note does **not** claim new mathematics. It closes a tempting PDT derivation route for Two-Point Isotropy (TPI).

## Candidate route under attack

A natural PDT thought is that if the elementary distinction geometry is Euclidean and all scalar distinguishabilities are isotropic, then the reversible group should have no preferred azimuth and hence satisfy TPI.

That implication is false.

## Counterfamily

Let the elementary real state space be

\[
V=\mathbb C^m\simeq\mathbb R^{2m},\qquad m\ge2,
\]

with the natural action of `SU(m)`. The action preserves the complex Hermitian inner product and therefore preserves the induced real Euclidean inner product, norm, angle, and distance. It is also transitive on the unit sphere, with stabilizer `SU(m-1)`.

Fix

\[
x=e_1,
\]

and for any `0<a<1` define

\[
y=e_2,\qquad z=i a e_1+\sqrt{1-a^2}\,e_2.
\]

Then

\[
\|y\|=\|z\|=1,
\]

and using the real Euclidean inner product `Re <.,.>`,

\[
\operatorname{Re}\langle x,y\rangle
=
\operatorname{Re}\langle x,z\rangle
=0.
\]

Hence `y` and `z` have the same real angle from `x` and the same scalar Euclidean distance from `x`:

\[
\|x-y\|=\|x-z\|=\sqrt2.
\]

However, every `g` in the stabilizer of `x` preserves the full complex inner product with `x`, while

\[
\langle x,y\rangle=0,
\qquad
\langle x,z\rangle=i a.
\]

Therefore no reversible transformation fixing `x` can map `y` to `z`. TPI fails.

## The no-go

Thus

\[
\boxed{
\text{sphere transitivity}
+
\text{isotropic scalar Euclidean distinguishability}
\not\Rightarrow
\text{TPI}
}
\]

for the natural `SU(m)` actions in every real dimension `2m >= 4`.

The branch audit instantiates explicit witnesses in real dimensions 4, 6, 8, 10, and 12, while the unit tests extend the same analytic construction to larger `m`.

## Why this matters for PDT

The surviving `TPI + PCC => n=3` dimension route cannot derive TPI merely from statements such as:

- every pure distinction has the same scalar capacity;
- Euclidean distances/angles have no preferred direction;
- the reversible group is connected and sphere-transitive;
- every scalar distinguishability depends only on Euclidean angle.

All of those can hold while the reversible dynamics preserve an additional invariant invisible to the chosen scalar distinction measure.

A genuine PDT derivation of TPI must therefore rule out **latent stabilizer invariants**. Operationally, PDT needs a completeness principle saying that the declared distinction data are not merely isotropic as numbers but are complete for the orbit structure of reversible controls.

That completeness principle is currently **OPEN** and must not be silently identified with TPI itself.

## Prior-art boundary

The facts used here are standard: `SU(m)` preserves the Hermitian inner product, acts transitively on the unit sphere in `C^m`, and has point stabilizer `SU(m-1)`. The PDT contribution in this cycle is only the use of this standard family as a kill test for a proposed derivation route; no historical novelty claim is made.
