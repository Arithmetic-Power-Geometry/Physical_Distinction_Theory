# Cycle 099 — Complete records diagnose defects; they do not enforce composition

## Question attacked

Cycles 095–098 left a tempting route: perhaps PDT can derive a separating or tomographically complete record family, use that family to expose every associativity defect, and thereby remove the `n=7` octonionic sector. This cycle tests that implication directly rather than treating visibility as if it were a dynamical constraint.

## Exact theorem: observation–enforcement separation

Let `delta:X -> W` be any composition-defect map and let `L:W -> Y` be injective. Then

`L(delta(x)) = 0  <=>  delta(x) = 0`.

Proof: the reverse implication is immediate by linearity. For the forward implication, `L(delta(x))=0` means `delta(x)` lies in `ker L`; injectivity gives `ker L={0}`, hence `delta(x)=0`.

This is a certification theorem only. It says that an injective record detects a defect faithfully. It does **not** impose `L(delta(x))=0`, and therefore cannot force `delta(x)=0`.

## Decisive counterexample to the proposed n=3 route

Take the octonions `O = R + R^7` with the standard Cayley–Dickson product. They are unital, bilinear, positive-norm composing, alternative, and nonassociative. Their basis associators span the full seven-dimensional imaginary sector. Use all seven imaginary coordinates as operational records:

`L(a0,a1,...,a7) = (a1,...,a7)`.

On the associator defect space this map has rank seven and is injective. Exact enumeration of all `8^3 = 512` ordered basis triples gives:

- 168 nonzero basis associators;
- associator-span rank 7;
- full-record rank 7;
- 0 nonzero basis associators missed by the complete record family.

Nevertheless the algebra remains nonassociative. The exact witness used since Cycle 095 remains

`[e1,e2,e4] = 2 e7`,

and its complete record has norm `2`, not zero.

Therefore the candidate implication

`alternative + norm composition + separating/tomographically complete records => associativity (or n=3)`

is **FALSIFIED**. The `n=7` sector survives complete observability of its defects.

## Numerical stress

A seeded 3,000-trial audit of normalized random octonion triples found 3,000 nonzero associators above `1e-10`, all detected by the seven-coordinate record. The maximum scalar associator component was `3.33e-16` and the maximum gap between full associator norm and complete-record norm was `0.0` in the run. Generic rank stress uses identity records on defect spaces of dimensions `1..12,16,24,32,48,64,96,128`; in every case rank equals dimension while nonzero defects still exist. This dimension stress is intentionally logical rather than a claim that octonionic composition exists in every dimension.

## Prior-art boundary

The injectivity argument is elementary linear algebra. Octonion alternativity, norm composition, nonassociativity and the seven-dimensional imaginary sector are classical facts; no historical novelty is claimed for them. Standard references include John C. Baez, *The Octonions* (2001/2002), and the established Cayley–Dickson/octonion literature.

## PDT consequence

Record completeness belongs to **diagnosis/revelation**. Associativity or another composition law belongs to **dynamics/structure**. Conflating them would make the dimension argument invalid.

The surviving prove-or-falsify obligation is therefore stronger: PDT must derive an independent law that constrains the composition defect itself. Candidate directions worth attacking are operational path-independence, coherent composition under all parenthesizations, or a resource-cost/forbidden-defect principle. Such a law must exclude the octonionic sector without simply restating associativity or importing quaternionic structure.

## Status

- Observation–enforcement separation theorem: **PROVED**.
- Complete-records-imply-associativity/n=3 route: **FALSIFIED**.
- Octonion structural facts: **IMPORTED/KNOWN**.
- Random stress audit: **NUMERICALLY SUPPORTED**.
- PDT-native defect-suppression law: **OPEN**.
- `BREAKTHROUGH CANDIDATE`: **NO**.
