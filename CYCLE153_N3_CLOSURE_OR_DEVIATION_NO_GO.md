# PDT-II Cycle 153 — n=3 Closure-or-Deviation No-Go

## Target

Attack target (2), the requested non-circular PDT-native `n=3` derivation, while cross-checking target (3), a same-input probability deviation from QM.

## Theorem

Consider a three-dimensional complex Hilbert-space experiment. Suppose a PDT probability assignment `mu(P)` to projectors satisfies:

1. `mu(P) >= 0`;
2. `mu(I)=1`;
3. for every orthogonal resolution `I = sum_i P_i`, `mu(I)=sum_i mu(P_i)`;
4. the value assigned to a projector is noncontextual: it does not depend on which orthogonal resolution contains that projector.

Then there exists a density operator `rho` such that

`mu(P) = Tr(rho P)`

for every projector `P`.

This is exactly the dimension-three case of Gleason's theorem. Consequently, if PDT keeps the same microscopic state `rho`, the same projectors/effects, and these probability hypotheses, then it cannot obtain

`P_PDT(O|I,R) != P_QM(O|I,R)`

merely from a new n=3 bookkeeping or composition derivation.

## Proof status

The implication is **IMPORTED/KNOWN** mathematics (Gleason), not a PDT theorem and not a novelty claim. Cycle 063 already proved the broader operational-closure no-go once the Born/generalized-Born pairing is retained. Cycle 153 sharpens the boundary at the requested `n=3`: under projector noncontextuality and orthogonal additivity, the probability pairing itself is already forced into Born form.

## Decisive falsification

The candidate route

> derive a new PDT-native n=3 probability law while retaining ordinary Hilbert projectors, normalized orthogonal additivity, noncontextuality, and the same microscopic state

is **FALSIFIED** as a route to a same-input quantitative deviation.

At least one ingredient must change physically or operationally: noncontextuality, orthogonal additivity, the state space, effect space, composition rule, dynamics/process, or resource-window coupling. Merely renaming a quadratic quantity as a PDT distinction resource cannot create a new n=3 empirical law.

## Important loophole boundary

This no-go does **not** say every conceivable PDT n=3 theory equals QM. It says a genuinely different n=3 prediction must leave the Gleason/quantum operational closure explicitly. Any such departure must then be checked for positivity, normalization, compositional consistency, causality/no-signalling, and compatibility with existing experiments.

## Dimension stress interpretation

- `n=1`: trivial probability simplex; no Gleason uniqueness content.
- `n=2`: standard projection-only Gleason theorem has a loophole; generalized-effect/POVM assumptions or composite-system assumptions can close related loopholes, but those are additional imported hypotheses.
- `n>=3`: normalized noncontextual orthogonal additivity on Hilbert projectors forces trace/Born form.

Thus `n=3` is not a promising place to claim a new probability law while keeping those assumptions; it is precisely the first dimension where the classical Gleason uniqueness obstruction applies.

## Prior-art boundary

Gleason (1957) is the primary historical result. Busch (2003) gives a generalized-observable/effect version. Recent work also studies recovering the qubit case from composite-system consistency. None of these are PDT novelty.

## Consequence for PDT-II

The next admissible target-(2)/(3) candidate must declare a specific PDT-native primitive outside this closure before numerical fitting. Candidate departures will be rejected if they merely reproduce known contextual hidden-variable, generalized-probabilistic, or modified-Born families without a PDT-native derivation and a new falsifiable consequence.

## Status ledger

- n=3 projector noncontextuality + orthogonal additivity => Born/trace form: **IMPORTED/KNOWN / PROVED by Gleason**
- new same-input PDT probability law under those same hypotheses: **FALSIFIED**
- bookkeeping-only n=3 deviation: **FALSIFIED**
- PDT-native physical reason to relax one closure hypothesis: **OPEN**
- experimentally viable same-input PDT deviation: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
