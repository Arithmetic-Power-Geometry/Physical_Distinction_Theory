# Cycle 007 — Generator Economy + Noncommuting Reversibility filter

## Status: CONDITIONAL PDT AXIOMS / IMPORTED-KNOWN LIE MATHEMATICS / NOT A BREAKTHROUGH

This cycle weakens the exact Generator–Distinction Self-Duality (GDSD) requirement from Cycle 006.

After the Euclidean reduction, let an elementary distinction space be `V ≅ R^n` with full connected reversible isotropy `SO(n)`. The infinitesimal reversible generators form `so(n)` with standard dimension

`dim so(n) = n(n-1)/2`.

We test two candidate operational conditions.

### GE — Generator Economy

At an elementary resource scale, the number of independent infinitesimal reversible generator coordinates must not exceed the number of primitive distinction coordinates:

`dim so(n) <= dim V = n`.

Unlike GDSD, GE does **not** demand a one-to-one identification, equivariance, surjectivity from distinctions to generators, or equality of dimensions. It only rules out hidden continuous reversible-control coordinates outnumbering elementary distinction coordinates.

For positive `n`,

`n(n-1)/2 <= n`

implies `n <= 3`.

### NCR — Noncommuting Reversibility

Require the elementary connected reversible dynamics to contain genuinely noncommuting infinitesimal generators. Under full isotropy `SO(n)`, `so(1)` is trivial and `so(2)` is one-dimensional and abelian, while `so(n)` is non-abelian for every `n >= 3`. Hence NCR implies

`n >= 3`.

### Conditional dimension theorem

Combining GE and NCR gives

`n <= 3` and `n >= 3`,

therefore

`n = 3`.

Thus, among positive-dimensional Euclidean elementary distinction spaces with full connected isotropy `SO(n)`, the pair GE+NCR selects three dimensions.

## Why this is weaker than GDSD

GDSD required an equivariant isomorphism `V -> so(V)` and therefore exact dimension equality plus representation matching. GE+NCR requires neither an isomorphism nor any Hodge/axial-vector structure. GE is only an inequality; NCR only demands noncommutativity. Consequently the new filter has a smaller mathematical assumption burden than Cycle 006.

## Computational audit

`pdt_generator_economy.py` scans dimensions 1–12 in the machine-readable table `results/cycle007_generator_economy_dimension_filter.csv`. The test suite scans all positive integers through 1000. The unique selected dimension is `n=3`.

## Kill tests and novelty discipline

1. The Lie-theoretic facts are standard: `dim SO(n)=dim so(n)=n(n-1)/2`; `so(2)` is abelian and `so(n)` is non-abelian for `n>=3`.
2. GE and NCR are proposed operational axioms, not consequences of the current PDT axioms. The central research burden is to derive or experimentally motivate them without using the desired three-dimensional answer.
3. Full connected isotropy `SO(n)` is still part of the conditional setup. Weakening or replacing that assumption is a separate open problem.
4. GE could be false in nature: a system may possess more independently controllable infinitesimal reversible directions than primitive state/distinction coordinates. Such a counterexample would kill this route.
5. NCR excludes dimensions 1 and 2 only under the stated full-isotropy model. If the physically relevant reversible group differs from `SO(n)`, the filter must be recomputed.
6. No same-input deviation from quantum mechanics follows. This is a dimension-filter proposal, not new physics.
7. Historical novelty is not claimed for the mathematics. The potentially PDT-specific contribution is only the operational interpretation of GE+NCR, which still needs independent justification and prior-art review.

## Research consequence

The dimension-selection burden is now reduced from exact self-duality to two simpler questions:

- Why should elementary reversible-control degrees of freedom not outnumber elementary distinction coordinates?
- Why must elementary reversible dynamics be genuinely noncommuting?

If both principles can be derived from independent PDT resource/composition requirements, the existing local Euclidean dimension no-go would be bypassed with a weaker assumption set than GDSD. Until that derivation exists, Cycle 007 remains CONDITIONAL and must not be promoted as a breakthrough.
