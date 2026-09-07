# PDT Breakthrough Lab — Research Cycle 001

## Result: local dimension-selection no-go

**Status: PROVED / NO-GO.**

The current local PDT assumptions CEU, CER and RDE do **not** select the qubit dimension `n=3`.

### Proposition
For every integer `n >= 2`, the Euclidean unit ball `B^n` satisfies the local CEU/CER/RDE structure used in the current PDT elementary-state theorem.

### Proof sketch
Let the centered elementary body be the Euclidean unit ball `B^n`.

1. **CEU.** Every boundary point `a` has antipode `-a`, and `(a + (-a))/2 = 0`.
2. **CER.** Every radial point `x = r a`, `0 <= r <= 1`, can be written as `x = q a + (1-q)(-a)` with `q=(1+r)/2`.
3. **RDE.** The orthogonal group `O(n)` acts transitively on the unit sphere. For any unit vectors `a,b`, a Householder transformation can be constructed that maps `a` to `b` while preserving the Euclidean distinction form.

Therefore all dimensions `n >= 2` satisfy these local assumptions. No theorem using only this local structure can uniquely conclude `n=3`.

### Computational audit
`scripts/dimension_selection_no_go.py` stress-tests the constructive proof for dimensions 2 through 10 with random boundary points. The committed output `results/dimension_selection_no_go.csv` reports residuals at floating-point precision and PASS in every tested dimension.

This numerical audit is not the proof; it is an implementation check of the proof construction.

## Consequence for the research program

A genuine PDT-native derivation of `n=3` must introduce a principle that is **not invariant across the full family of Euclidean balls**. The next search should therefore target composite or interaction structure, operationally measurable orientation/information structure, or another explicitly physical distinction principle that couples local systems.

## Prior-art boundary checked 2026-09-07

This no-go is consistent with established reconstruction literature rather than a replacement for it. Relevant prior results include:

- Müller & Ududec, *Physical Review Letters* 108, 130401 (2012): bit symmetry implies self-duality in GPTs.
- de la Torre, Masanes, Short & Müller, *Physical Review Letters* 109, 090403 (2012): with qubit local structure, continuous reversible interaction can recover quantum global structure.
- Masanes, Müller, Pérez-García & Augusiak, *Journal of Mathematical Physics* 55, 122203 (2014): for locally tomographic composites of Euclidean balls with continuous reversible dynamics, nontrivial interaction/entanglement singles out the three-dimensional Bloch ball.

Accordingly, any new PDT composition principle must be compared directly against these results and must not simply rename local tomography, reversible interaction, or entanglement.

## Breakthrough status

**No breakthrough claim.** The result is a rigorous narrowing theorem: it eliminates the entire class of purely local CEU/CER/RDE dimension-selection attempts and identifies composite/interventional structure as the necessary next frontier.
