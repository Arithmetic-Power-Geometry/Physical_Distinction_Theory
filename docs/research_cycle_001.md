# PDT Breakthrough Lab — Research Cycle 001

## Candidate investigated

Can the PDT distinction-capacity primitive make elementary Euclidean dimension operationally identifiable, and can that fact select `n=3`?

## Result

**Status: CONDITIONAL / KNOWN-MATH OPERATIONALIZATION — NOT A BREAKTHROUGH.**

Let `M_n(epsilon)` be the maximum size of an `epsilon`-separated codebook in the Euclidean unit ball `B_2^n`. Standard packing/covering volume arguments give, for `0 < epsilon < 1`,

`epsilon^{-n} <= M_n(epsilon) <= (1 + 2/epsilon)^n`.

Writing `K_n(epsilon)=log_2 M_n(epsilon)` therefore yields

`n log_2(1/epsilon) <= K_n(epsilon) <= n log_2(1 + 2/epsilon)`.

Dividing by `log_2(1/epsilon)` and taking `epsilon -> 0` gives

`lim K_n(epsilon)/log_2(1/epsilon) = n`.

### PDT interpretation

If a declared resource window induces an effective Euclidean discrimination resolution `epsilon`, and admissible codebooks are exactly `epsilon`-separated alternatives, the fine-resolution scaling of distinction capacity identifies the elementary dimension operationally.

This is useful because PDT previously separated scalar capacity from geometry. Once Euclidean geometry is independently justified, the *scaling family* of capacities across resolution contains dimension information even though a single scalar capacity value does not.

### What it does **not** prove

- It does not derive Euclidean geometry from distinction capacity.
- It does not select `n=3`.
- It does not establish new mathematics; the asymptotic is standard metric entropy / packing-covering theory.
- It does not replace the need for a PDT-native composite/interventional principle if the goal is to explain why the physical elementary dimension is three.

## Counterexample / no-go consequence

For every integer `n >= 2`, the Euclidean ball `B_2^n` has the same qualitative CEU/CER/RDE local structure while its capacity-scaling exponent equals `n`. Therefore a principle that merely *reads off* the scaling exponent cannot explain why Nature chooses 3; it only measures whichever dimension the theory already has.

## Numerical audit

`results/dimension_identifiability_audit.csv` records lower/upper capacity bounds and normalized slopes for dimensions 2–5 at decreasing resolutions. The lower normalized slope is exactly `n`; the upper bound converges downward toward `n` as resolution becomes finer.

## Prior-art boundary

This result rests on classical epsilon-entropy / metric-entropy mathematics, including Kolmogorov–Tikhomirov packing/covering ideas. It is therefore tracked as a PDT operationalization rather than a novelty claim.

Useful references checked in this cycle:

- Encyclopedia of Mathematics, epsilon-entropy: https://encyclopediaofmath.org/wiki/Epsilon-entropy
- Kolmogorov & Tikhomirov (1961), epsilon-entropy and epsilon-capacity (cited there).
- Standard Euclidean packing/covering volume bounds, e.g. high-dimensional probability lecture treatments.
- Masanes, Müller, Pérez-García & Augusiak (2014), *Entanglement and the three-dimensionality of the Bloch ball*, DOI 10.1063/1.4903510. This remains important prior art for dimension-three reconstruction via composite assumptions.

## Next research target

Search for a **dimension-sensitive PDT-native composite/interventional invariant** that is not equivalent to local tomography + continuous reversible interaction and is false for generic `B_2^n` but true for `n=3`. Every candidate must be subjected to explicit `n=2,4,5,...` countermodels before promotion.
