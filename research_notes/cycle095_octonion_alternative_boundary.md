# Cycle 095 — The octonionic alternativity boundary

## Target

PDT-II targets (1) and (2), following Cycle 094: determine whether the 3D selector survives if operational composition is weakened from full associativity to **alternativity**, while retaining a unit and positive Euclidean norm composition.

## Decisive result

**FALSIFIED + PROVED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED + OPEN.**

The candidate statement

> unital bilinear positive-norm-composing alternative composition selects distinction-vector dimension `n=3`

is false.

The classical octonion algebra
\[
\mathbb O \cong \mathbb R\oplus\mathbb R^7
\]
is an explicit `n=7` counterexample. It has a unit, bilinear multiplication and the positive Euclidean composition law
\[
\|xy\|^2=\|x\|^2\|y\|^2.
\]
It is alternative:
\[
[x,x,y]=[y,x,x]=[x,y,x]=0,
\]
but it is not associative.

With the Cayley-Dickson convention implemented in this cycle, the basis elements give the exact integer-coordinate witness
\[
[e_1,e_2,e_4]=2e_7,
\]
so the associator norm is exactly `2`.

The exhaustive basis-pair alternativity audit has zero residual for all 64 ordered basis pairs. Thus the same algebra simultaneously provides exact alternativity and exact failure of associativity.

## Why this matters for the Cycle-094 `n=3` route

Cycle 094 found that, inside the 3D dot/cross scalar-unit ansatz, full associativity locks the coefficients to the quaternion relation. Cycle 095 shows that **associativity is doing indispensable selection work**. If PDT weakens grouping to alternativity and permits the corresponding exceptional reversible structure, the 7D octonionic sector survives.

Therefore PDT may not claim a non-circular derivation of `n=3` from only:

1. a scalar/unit augmentation,
2. bilinearity,
3. positive norm composition, and
4. alternativity.

An independently derived stronger requirement is still needed—for example full operational associativity, a symmetry/calibration condition excluding the `G2` sector, or a different physical composition postulate. Such a premise must itself come from PDT primitives rather than be chosen because it removes `n=7`.

## Dimension boundary

Classical Hurwitz/normed-division-algebra theory permits full real algebra dimensions
\[
1,2,4,8,
\]
corresponding to imaginary/distinction-vector dimensions
\[
0,1,3,7.
\]

The executable ledger records `n=1..12,16,24,32,48,64,96,128`. Under the positive-definite real normed-division-algebra hypotheses, the higher surviving vector dimensions in this range are `n=1,3,7`; `n=7` is the decisive higher-dimensional counterexample to a purported alternativity-based 3D selector. The exclusions are theorem-based prior art, not numerical discoveries.

## Numerical regression

The executable audit uses 3,000 normalized random octonion triples.

- maximum norm-multiplicativity residual: `5.551115123125783e-16`
- maximum left-alternativity residual: `4.712832172234208e-16`
- maximum right-alternativity residual: `4.795373138347379e-16`
- maximum flexible-law residual: `4.1932970789410407e-16`
- maximum generic associator norm: `1.9226734051912622`
- generic nonassociative cases above `1e-10`: `3000/3000`

These floating checks are regression evidence only. The decisive basis counterexample and basis alternativity identities are exact in integer coordinates.

Local tests: **5/5 passed**.

## Prior-art boundary

This is **not** a breakthrough candidate.

The octonions are a classical 8-dimensional normed division algebra; their multiplication is alternative but nonassociative. Classical Hurwitz/division-algebra theory gives the `1,2,4,8` dimension boundary, and the automorphism group of the octonions is the exceptional group `G2`. Useful references include John C. Baez's *The Octonions* materials and standard Hurwitz/Frobenius division-algebra literature.

Prior-art sources checked in this cycle:

- John C. Baez / Conway–Smith octonion notes: https://math.ucr.edu/home/baez/octonions/conway_smith/
- Baez, discussion of octonionic/G2 structure: https://math.ucr.edu/home/baez/rolling/rolling_5.html
- Encyclopedia of Mathematics, Frobenius theorem: https://encyclopediaofmath.org/wiki/Frobenius_theorem

## Status ledger

- **FALSIFIED:** unit + bilinearity + positive norm composition + alternativity uniquely select `n=3`.
- **PROVED:** the implemented `n=7` Cayley-Dickson algebra has exact basis alternativity and an exact nonassociative witness `[e1,e2,e4]=2e7`.
- **NUMERICALLY SUPPORTED:** 3,000 random normalized trials reproduce norm composition and alternativity to floating precision while generic associativity fails.
- **IMPORTED/KNOWN:** octonions, Hurwitz dimension restrictions and the `G2` automorphism boundary.
- **OPEN:** derive from PDT distinction/resource primitives whether physical composition must be fully associative, only alternative, or resource-indexed/nonassociative.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Next prove-or-falsify obligation

The next strongest target is to derive or falsify **operational associativity from resource refinement/composition itself**. A valid derivation must explain why regrouping independent physical subsystems/resources cannot change predictions, while explicitly separating genuine tensor reassociation from nonassociative internal multiplication. If that cannot be derived, the `n=7` boundary remains live and the Cycle-094 `n=3` selector stays conditional.
