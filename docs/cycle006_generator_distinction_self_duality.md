# Cycle 006 — Generator–Distinction Self-Duality dimension filter

## Status: CONDITIONAL PDT AXIOM / IMPORTED-KNOWN REPRESENTATION MATHEMATICS / NOT A BREAKTHROUGH

This cycle replaces the stronger cross-product assumption of Cycle 005 by a weaker representation-theoretic question.

After the Euclidean reduction, let the elementary distinction space be a real Euclidean vector space `V ≅ R^n`, and let the full connected reversible isotropy group be `SO(n)`. Its infinitesimal reversible generators form

`so(n) ≅ Λ^2 V`,

with

`dim so(n) = n(n-1)/2`.

### Candidate PDT-native axiom: Generator–Distinction Self-Duality (GDSD)

At a fixed elementary resource scale, require that every primitive distinction direction be representable by exactly one primitive infinitesimal reversible generator, and conversely, with no hidden generator coordinates and no redundant distinction coordinates. Mathematically this asks for an equivariant linear isomorphism

`J_R : V -> so(V)`.

This is an operational closure proposal, not a theorem of PDT. Its physical content would be that the same elementary resource coordinates classify both *what can be distinguished* and *how elementary reversible distinction can change*.

## Necessary dimension theorem

If GDSD holds, then dimensions must agree:

`n = n(n-1)/2`.

For positive integer `n`,

`2n = n(n-1)`,

so `n>0` gives `2 = n-1`, hence

`n = 3`.

Conversely, in dimension three the standard Hodge/axial-vector identification gives an `SO(3)`-equivariant isomorphism `R^3 ≅ so(3)`.

Therefore, among positive-dimensional Euclidean balls with full connected isotropy `SO(n)`, GDSD is possible exactly at

`n = 3`.

## Computational audit

`pdt_generator_duality.py` checks `dim so(n)=n(n-1)/2` and scans dimensions 1–12, while the test suite also scans all positive integers through 1000. The only positive integer solution is `n=3`.

Machine-readable output: `results/cycle006_generator_distinction_duality.csv`.

## Kill tests and prior-art discipline

1. **Mathematics is known.** The identity `so(n) ≅ Λ^2 R^n` and the exceptional equality `dim so(3)=3` are standard representation/geometric-algebra facts.
2. **This is not yet a derivation from existing PDT axioms.** The new burden is to justify GDSD operationally rather than assume it because it selects three dimensions.
3. **No quantum structure is imported into the statement.** The axiom mentions only distinction directions, reversible generators, and resource-scale closure. However, this alone does not establish that nature obeys GDSD.
4. **No same-input QM deviation follows.** Even if GDSD were adopted, it would select a three-dimensional Euclidean elementary distinction body but would not yet produce a prediction differing from standard quantum mechanics.
5. **Potential circularity test.** Any physical argument for GDSD must avoid invoking ordinary 3D axes, Pauli matrices, qubits, the vector cross product, or the already-known isomorphism `so(3) ≅ R^3` as motivation.

## Research consequence

Cycle 006 narrows the dimension problem to a cleaner physical question than Cycle 005:

> Why, if at all, should elementary distinguishable directions and elementary reversible-generator directions be operationally self-dual at the same resource scale?

If this self-duality can be independently derived from PDT resource/composition principles or measured as an operational closure law, the current local Euclidean no-go would be bypassed without importing the stronger normed-cross-product axiom. Until then, the result remains CONDITIONAL and must not be promoted as a breakthrough.

## Prior-art note from this cycle

Fresh literature checking confirms that the mathematical specialness is established: in three dimensions only, the defining vector representation of `SO(n)` has the same dimension as—and is isomorphic to—the adjoint representation, equivalently vectors are Hodge-dual to bivectors. This prevents any novelty claim for the representation theorem itself. The potentially new part, if defensible later, would have to be the independently motivated PDT operational axiom and its physical consequences.
