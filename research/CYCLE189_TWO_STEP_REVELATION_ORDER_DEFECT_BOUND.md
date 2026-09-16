# Cycle 189 — Sharp two-step revelation order-defect bound

## Status

- **PROVED (conditional):** for one nonzero scalar effect and two invertible reversible interventions, the two-order revelation-rank defect has absolute value at most 1.
- **IMPORTED/KNOWN boundary:** the proof is finite-dimensional linear algebra / switched-observability rank structure; no PDT novelty is claimed for the abstract rank fact.
- **FALSIFIED:** any conjecture that the two-order defect can grow with dimension for a single scalar effect and exactly two reversible interventions.
- **OPEN:** whether a PDT-native physical restriction yields a stronger multi-step/resource-cost inequality not reducible to observability rank theory.
- **BREAKTHROUGH CANDIDATE:** NO.

## Setup

Let V be a finite-dimensional real or complex vector space, let e in V* be nonzero, and let A,B in GL(V). For chronological order A then B define

D(A,B) = rank{e, eA, eBA},

and for B then A define

D(B,A) = rank{e, eB, eAB}.

Define the order defect

Delta_e(A,B) = D(B,A)-D(A,B).

This is a resource-relative observable/revelation dimension. No probability law is assumed.

## Theorem (sharp two-step scalar-effect bound)

For every finite-dimensional V, nonzero e, and invertible A,B,

|Delta_e(A,B)| <= 1.

The bound is sharp from dimension 3 onward.

### Proof

Each rank lies in {1,2,3}. It is enough to exclude the only possible rank gap of 2.

Suppose D(A,B)=1. Then eA=a e and eBA=b e for nonzero a,b (nonzero because A,B are invertible and e is nonzero). From eA=a e we have eA^{-1}=a^{-1}e. From eBA=b e, right-multiplying by A^{-1} gives

eB = b eA^{-1} = (b/a)e.

Then eAB=(eA)B=a eB=b e. Hence D(B,A)=1. By symmetry, D(B,A)=1 implies D(A,B)=1. Therefore the pair of ranks can never be (1,3) or (3,1). Since both ranks are integers in {1,2,3}, their difference has absolute value at most 1. QED.

### Sharp witness

In dimension 3, the Cycle-188 reversible permutation witness realizes ranks 2 and 3 under opposite orders, hence |Delta|=1. The witness embeds by identity on unused coordinates into every n>=3.

## Dimension stress implications

- n=1: Delta=0 identically.
- n=2: |Delta|<=1 analytically.
- n=3..12: |Delta|<=1 analytically, with the Cycle-188 n=3 sharp witness embedded into all n>=3.
- arbitrary finite n: same proof; no asymptotic growth with n is possible for this exact two-intervention/single-effect protocol.

Because the theorem is analytic and dimension-independent, numerical tests are not used as evidence for the bound in this cycle.

## Degenerate and edge cases

1. e=0: all ranks are 0, so Delta=0; excluded from the theorem only to avoid vacuous proportionality coefficients.
2. A or B noninvertible: the proof step using A^{-1} (or B^{-1}) fails. Larger behavior must be tested separately; the reversible hypothesis is substantive.
3. Multiple independent effects: the rank ceiling becomes larger and this scalar-effect bound does not automatically persist.
4. Longer words: the three-row ceiling disappears; order defects may accumulate and require separate bounds.
5. Choice of norm: irrelevant because the theorem is rank-only.
6. Real/complex field: proof is unchanged.

## PDT-II consequence

Cycle 188 established that sequential noncommuting revelation can be order dependent. This cycle sharply limits that effect in the smallest reversible scalar-observation protocol:

    order dependence exists, but a two-intervention scalar-effect defect cannot exceed one revealed dimension.

Thus a dimension-growing two-step order-defect inequality is **FALSIFIED**. Any experimentally distinctive PDT inequality must use additional PDT-native structure (longer resource histories, multiple effects, constrained costs, environment records, thermodynamic restrictions, or a non-rank observable) and must be compared against switched-system observability before novelty claims.

## Prior-art boundary

Observability matrices and Gramians are standard in linear systems, and switched-system observability explicitly studies information accumulated under switching sequences. Rank-based sensor/observability objectives and their submodular structure are also established. Accordingly this theorem is retained as a useful PDT-II boundary/lemma, not promoted as a breakthrough.
