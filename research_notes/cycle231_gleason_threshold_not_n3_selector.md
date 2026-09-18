# Cycle 231 — Gleason/contextual-consistency route does not derive n=3

## Target
PDT-II target (2): seek a non-circular PDT-native derivation selecting n=3.

## Candidate attacked
Use noncontextual probability assignment / frame-function consistency on rank-1 tests as the physical selector, motivated by the special appearance of dimension 3 in Gleason-type results.

## Exact hypotheses
Let H_n be a real or complex Hilbert space of finite dimension n. Let f assign probabilities to rank-1 projectors such that for every orthonormal basis {P_i}_{i=1}^n, sum_i f(P_i)=1, with the assignment noncontextual (the value assigned to P is independent of which orthonormal resolution contains P).

## Result
**FALSIFIED as a selector of exactly n=3; IMPORTED/KNOWN as mathematical machinery.**

The standard Gleason conclusion (under its standard hypotheses) applies for every Hilbert-space dimension n >= 3: admissible frame functions/probability measures are represented by density operators / Born-rule form. Therefore the property is a threshold property, not an exact selector:

    G(n) = false/not-covered at n=1,2 by the original theorem's hypotheses/conclusion regime;
    G(n) = true for every n=3,4,...

Consequently G(n) cannot imply n=3. In particular, n=4 is an immediate decisive countermodel to the implication G(n) => n=3.

This remains true over the requested exact stress range n=1,...,12: every n in {3,...,12} lies in the same Gleason-valid regime. No random higher-dimensional test is needed because the obstruction is algebraic and extends to all finite n>=3.

## Why this matters for PDT
The mere fact that 3 is the *minimum* dimension in the original Gleason theorem does not physically derive that nature must choose dimension 3. Turning “the theorem begins at 3” into “physical dimension equals 3” is an invalid minimality inference unless PDT independently derives a principle requiring the *smallest* dimension satisfying the consistency property. Such a minimality principle would itself be a new physical hypothesis and must be justified without encoding the desired answer.

Moreover, importing Hilbert-space projectors, orthogonality, orthonormal resolutions, and noncontextual frame functions already imports substantial quantum structure. It is therefore circular for the requested PDT-native derivation unless those objects are first obtained from PDT primitives.

## Contextual entropy variant
Known contextual-entropy reconstruction results likewise reconstruct finite-dimensional quantum states for dimension >=3. They therefore inherit the same threshold-versus-selector problem and cannot uniquely select n=3.

## Exact n=1..12 ledger
| n | original Gleason regime sufficient for Born-form conclusion? | selects exactly 3? |
|---:|:---:|:---:|
|1|no|no|
|2|no (standard original theorem)|no|
|3|yes|no|
|4|yes|no|
|5|yes|no|
|6|yes|no|
|7|yes|no|
|8|yes|no|
|9|yes|no|
|10|yes|no|
|11|yes|no|
|12|yes|no|

## Smallest decisive counterexample
n=4. It satisfies the same standard Gleason consistency conclusion as n=3, so any selector based only on that conclusion fails to distinguish 3 from 4.

## Prior-art boundary
- Gleason's theorem is established prior art.
- Contextual-entropy state reconstruction in finite dimension >=3 is established prior art.
- Reconstructions in which a 3-dimensional Bloch ball is derived from composite/generalized-bit axioms are also established prior art and cannot simply be relabeled PDT-native.

## Surviving theorem / obligation
**PROVED logical filter:** If a proposed PDT dimension principle F(n) holds for n=3 and any n != 3, then F alone cannot derive n=3. Threshold-at-3 principles require an independently derived minimality law before they can select 3.

The strongest surviving target is therefore stricter:

    PDT primitives + independently justified physical constraints => F(n),
    with F(3)=true and F(n)=false for every n != 3,

or a separately PDT-derived minimality/optimization theorem whose objective has a unique optimum at n=3. Neither has been established here.

## Status
- Gleason threshold as exact n=3 selector: FALSIFIED
- Gleason machinery: IMPORTED/KNOWN
- Threshold-versus-selector logical filter: PROVED
- PDT-native exact n=3 derivation: OPEN
- BREAKTHROUGH CANDIDATE: NO

No claim of new experimental prediction, gravity law, or PDT-vs-QM probability difference is made in this cycle.
