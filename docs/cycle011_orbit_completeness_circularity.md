# Cycle 011 — Orbit-completeness circularity and scalar-invariant no-go

## Status

**PROVED equivalence / FALSIFIED derivation route / IMPORTED-KNOWN group-action mathematics.**

This note does **not** claim a PDT breakthrough or novel group theory.

## Question

After the scalar-isotropy counterexample, a natural rescue is to postulate that the PDT scalar distinction observable is *operationally complete*: once a reference distinction `x` is fixed, two pure directions `y,z` with the same scalar distinction from `x` should be physically interchangeable under a reversible transformation that fixes `x`.

Could such an operational-completeness principle independently derive Two-Point Isotropy (TPI)?

## Exact equivalence

Let `X` be the pure-state sphere, let a reversible group `G` act transitively on `X`, fix `x in X`, and write `H=G_x` for the stabilizer of `x`. Let `s_x : X -> S` be the declared scalar distinction observable around `x` (for a Euclidean sphere one may take `s_x(y)=<x,y>` or equivalently the distance `||x-y||`).

Define:

- **Scalar orbit-completeness (SOC):** `s_x(y)=s_x(z)` iff `y,z` lie in the same `H`-orbit.
- **TPI relative to `s_x`:** `H` acts transitively on each level set `{y : s_x(y)=c}`.

Because every reversible transformation fixing `x` preserves the declared invariant `s_x`, each `H`-orbit is contained in one scalar level set. Therefore TPI says every scalar level set is a single `H`-orbit. But that is exactly SOC.

Hence

`SOC <=> TPI`.

For Euclidean angle/distance, "the scalar distinction is a complete invariant of the stabilizer orbit" is therefore not an independent derivation of TPI. It is TPI rewritten as an orbit-separation statement.

## Explicit SU(m) kill family

For every `m>=2`, take the natural action `SU(m)` on `C^m ~= R^(2m)` and fix

`x=e1`, `y=e2`,

`z=i a e1 + sqrt(1-a^2) e2`, with `0<a<1`.

Then all three vectors are unit vectors and

`Re <x,y> = Re <x,z> = 0`,

so

`||x-y||^2 = ||x-z||^2 = 2`.

Thus `y` and `z` have exactly the same Euclidean scalar distinction from `x`.

However,

`<x,y>=0`, while `<x,z>=i a`.

Every unitary fixing `x` preserves the full complex inner product `<x, .>`. Consequently no element of the stabilizer of `x` can map `y` to `z`. The scalar distinction is therefore not orbit-complete for this action.

The executable audit covers `SU(m)` for real dimensions 4, 6, 8, 10 and 12, while unit tests stress `m=2..19` and parameters approaching both endpoints of `(0,1)`.

## Consequence for PDT dimension selection

The surviving `TPI + PCC -> n=3` route cannot be made PDT-native merely by declaring that the current scalar distinction observable is "complete." There are only three logically distinct options:

1. **Scalar data are not orbit-complete.** Then higher-dimensional reversible actions such as `SU(m)` retain latent invariants and TPI fails.
2. **Scalar data are declared orbit-complete.** Then TPI has been assumed in equivalent language, not derived.
3. **PDT admits richer operational invariants.** Those invariants may separate the stabilizer orbits, but then equal Euclidean angle/distance is no longer the complete physical relation, so the current TPI-based dimension proof no longer follows without another axiom collapsing the richer invariants.

This is an **independence/circularity boundary**, not a new physical law.

## Prior-art discipline

The group-action ingredients are standard: stabilizers, orbits and homogeneous spaces are established mathematics; transitive compact group actions on spheres and their proper subgroups are classified in the transformation-group literature; and separating invariants are a standard concept in invariant theory. PDT novelty is therefore not claimed for the equivalence itself.

## New target

A non-circular PDT route must derive a statement stronger than scalar isotropy but weaker than simply assuming orbit-completeness/TPI. One possible target is a physically motivated composition or calibration law that forces all stabilizer-invariant information to become operationally reducible to the declared distinction scalar. Such a reduction must be proved from independent PDT primitives and must survive the `SU(m)`, symplectic, and exceptional transitive-action counterfamilies.
