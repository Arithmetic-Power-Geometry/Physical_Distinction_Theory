# Cycle 370 — Full-rotation equivariance as a selector after the {3,7} vector-product obstruction

## Status

- **CONDITIONAL:** a binary normed vector product that is equivariant under the *full* orientation-preserving orthogonal group selects dimension 3 among nontrivial Euclidean dimensions.
- **IMPORTED/KNOWN:** ordinary vector cross-product classification; the 7-dimensional product is octonionic and its stabilizer is the exceptional group G2, not all of SO(7).
- **OPEN:** PDT has not yet derived the full-SO(n) equivariance hypothesis from a PDT-native operational principle.
- **NOT A BREAKTHROUGH CANDIDATE:** the selector is mathematically useful but currently rests on an extra symmetry hypothesis rather than a PDT-native derivation.

## Candidate hypotheses

Let V=R^n with Euclidean inner product and let ×:V×V→V be bilinear. Require:

H1. Alternating: x×x=0.

H2. Orthogonality: <x×y,x>=<x×y,y>=0.

H3. Norm identity: ||x×y||^2=||x||^2||y||^2-<x,y>^2.

H4. Full proper-rotation equivariance: for every R in SO(n),

    (Rx)×(Ry)=R(x×y).

The previous cycle established that H1–H3 alone leave n=3 and n=7.

## Exact selector argument

A bilinear alternating product is equivalently a linear map T:Λ^2 V→V. H4 says T is an SO(n)-intertwiner. For n>=4, no nonzero SO(n)-equivariant map Λ^2 V→V exists: Λ^2 V is the adjoint representation (with the familiar n=4 splitting after restriction to self/anti-self-dual pieces), whereas V is the defining representation, and these do not contain isomorphic irreducible constituents. Hence T=0 for n>=4, contradicting H3 on any orthonormal pair. In n=3, Hodge duality *:Λ^2 V→V is SO(3)-equivariant and gives the usual cross product satisfying H1–H4. n=2 cannot satisfy H3 with a V-valued product orthogonal to two independent inputs. n=1 is degenerate.

Therefore, under H1–H4, the unique nontrivial finite Euclidean dimension is n=3.

## Why the n=7 escape is closed

The octonionic 7D cross product satisfies H1–H3 but not H4. Its automorphism/stabilizer group is G2, a proper subgroup of SO(7). Thus generic rotations in SO(7) do not preserve the chosen 7D product. This is the decisive distinction from Cycle 369.

## Adversarial checks n=1..12

| n | H1–H3 possible? | full SO(n) equivariance compatible? | status |
|---:|:---:|:---:|---|
|1|degenerate|degenerate|reject nontriviality|
|2|no|no|reject|
|3|yes|yes|survives|
|4|no|no|reject|
|5|no|no|reject|
|6|no|no|reject|
|7|yes|no|reject by H4|
|8|no|no|reject|
|9|no|no|reject|
|10|no|no|reject|
|11|no|no|reject|
|12|no|no|reject|

Higher n are excluded by the same intertwiner argument, not merely numerical testing.

## Counterexample pressure on H4

H4 must not be smuggled in as “isotropy.” A physical theory can have a smaller reversible group than SO(n); the 7D octonionic example demonstrates exactly that. PDT therefore needs an independent operational theorem showing that every proper rotation of distinction space is physically reversible *and* that the distinction-composition operation is covariant under all such reversibles. Until that is proved, the n=3 result remains CONDITIONAL.

## Consequences for PDT-II targets

1. PDT-native composition law: OPEN. H1–H4 describe a candidate internal product, not yet a composite-system tensor rule.
2. Non-circular n=3 derivation: CONDITIONAL. The mathematical selector is clean, but H4 is not PDT-native yet.
3. Same-input P_PDT != P_QM: OPEN; nothing here changes probabilities.
4. Resource refinement/revelation/conservation: OPEN.
5. Distinctive inequality: OPEN.
6. Gravity/capacity: not invoked.

## Prior-art boundary

The 3/7 vector-product classification is classical prior art (e.g. Brown–Gray/Massey lineage). The 7D octonionic product is preserved by G2 rather than SO(7), and the 3D cross product is SO(3)-equivariant. PDT cannot claim these mathematical facts as novel. Potential novelty would have to lie in deriving H4 (or a weaker genuinely operational equivalent) from PDT’s physical-distinction axioms and connecting it to composition or a falsifiable prediction.

## Next strongest attack

Try to derive or falsify H4 from a PDT-native “reversible indistinguishability of frames” principle. Explicitly compare SO(n), O(n), SU(n), G2 and restricted reversible groups; test whether covariance of the product follows from operational frame equivalence or requires an independent assumption. If H4 cannot be derived, record the smallest countermodel and abandon this selector as foundational.
