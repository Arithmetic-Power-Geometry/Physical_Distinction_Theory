# Cycle 110 — Jacobi/associator boundary and non-circularity guard

## Question
Can PDT turn Cycle 109's Jacobi obstruction into a non-circular composition law or an n=3 derivation?

## Exact algebraic boundary
Let

`A(x,y,z) = (xy)z - x(yz)`

and let the commutator be `[x,y]=xy-yx`. For the left-nested Jacobiator

`J_L(x,y,z)=[x,[y,z]]+[y,[z,x]]+[z,[x,y]]`,

exact expansion gives

`J_L = -Alt(A)`,

where `Alt(A)` is the signed sum of the six permutations of the associator.

If the product is alternative, the associator is alternating, so `Alt(A)=6A` and therefore

`J_L = -6 A`.

Hence, **inside an alternative algebra, Jacobi of the commutator is equivalent to associativity**. It cannot be introduced as an independently weaker coherence principle without simply re-encoding the desired associativity condition.

For the half-commutator cross product `x × y=(xy-yx)/2`, the corresponding nested Jacobiator is one quarter as large, so `J_x=-3A/2`. For the repository octonion convention, `A(e1,e2,e4)=2e7`, hence `J_x(e1,e2,e4)=-3e7`, exactly reproducing Cycle 109.

## Smallest decisive counterexample outside alternativity
Dimension 2 already defeats Jacobi as a dimension selector. On basis `e1,e2`, define only

`e1 e2 = e2`

and set every other basis product to zero. Then

`A(e1,e1,e2)=-e2 != 0`,

so the product is nonassociative. But its commutator obeys

`[e1,e2]=e2`,

which is the 2D affine Lie algebra and satisfies Jacobi exactly. Adding zero-product central coordinates extends the same nonassociative Lie-admissible countermodel to every dimension `n>=2`.

Therefore:

- **Jacobi alone does not select n=3.**
- **With alternativity, Jacobi is associativity in disguise.**
- The Cycle 109 `cross-product + Jacobi -> n=3` selector remains conditional on imported cross-product structure and is not yet PDT-native.

## Repository audits
- General Akivis-sign identity: 720 exact seeded integer checks over dimensions 1..6; 0 failures.
- Dimension ledger: n=1..12,16,24,32,48,64,96,128. Every n>=2 carries the explicit nonassociative Jacobi-coherent countermodel above.
- Octonion audit: all 343 ordered imaginary basis triples checked; 168 have nonzero associator; `J_comm + 6 A` failures: 0.
- Local regression: 6/6 tests passed.

## Classification
- `J_L=-Alt(A)`: **PROVED / IMPORTED/KNOWN** (Akivis identity convention).
- Alternative `=> J_L=-6A`: **PROVED / IMPORTED/KNOWN**.
- “Jacobi alone selects n=3”: **FALSIFIED**.
- “Jacobi is a weaker independent coherence axiom in the alternative branch”: **FALSIFIED**.
- PDT-native operational composition law: **OPEN**.
- Breakthrough candidate: **NO**.

## Prior-art boundary
Lie-admissible algebras, Akivis' commutator/associator identity, alternative algebras, and Malcev-admissibility of commutators of alternative algebras are established mathematics. No novelty is claimed for these algebraic facts.

## Next attack
A viable PDT composition principle must be stated directly in distinction/resource operations before choosing a Lie, cross-product, or alternative-algebra representation. It must exclude both the 2D Lie-admissible countermodel and the 7D octonionic branch without being equivalent to associativity by definition.
