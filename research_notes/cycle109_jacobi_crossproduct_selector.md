# Cycle 109 — Jacobi-coherent vector composition selector

## Question
Can the surviving PDT-II composition/n=3 target be sharpened by requiring a primitive, vector-valued, norm-preserving composition law to be coherent under the Jacobi identity?

## Result
**Conditional selector only; not a PDT-native derivation.**

Established vector-cross-product theory restricts nontrivial Euclidean binary vector cross products with the standard norm/orthogonality property to dimensions 3 and 7. The 3D cross product satisfies Jacobi. The standard 7D octonionic cross product does not.

Exact repository audit:
- n=3: 27 ordered basis triples, 0 Jacobi failures.
- n=7: 343 ordered basis triples, 168 Jacobi failures.
- first exact witness: J(e1,e2,e4) = -3 e7.
- norm cross-product identity failures on basis pairs: 0 in n=3 and 0 in n=7.
- seeded random audit, 4000 triples per dimension: n=3 had 0 residuals above 1e-9; n=7 had 3056 nonzero residuals above 1e-9.

Therefore, within the imported cross-product classification,
`normed vector cross product + Jacobi` leaves n=3 as the only nontrivial candidate.

## Classification
- Cross-product dimension restriction: **IMPORTED/KNOWN**
- Exact 3D/7D audit in this repository: **PROVED / NUMERICALLY SUPPORTED**
- PDT-native derivation of cross-product axioms: **OPEN**
- PDT-native derivation of Jacobi from distinction/resource primitives: **OPEN**
- Breakthrough candidate: **NO**

## Circularity guard
This result must not be advertised as PDT deriving n=3. PDT has not yet shown that primitive composition is:
1. vector-valued on the primitive distinction space,
2. Euclidean norm preserving in the cross-product sense, or
3. Jacobi coherent.

Those are precisely the next prove-or-falsify obligations. Importing them would merely import a known 3-vs-7 classification and then remove 7 with a known Jacobi obstruction.

## Next attack
Try to derive or falsify Jacobi from an independently stated PDT operational law on infinitesimal reversible distinction transformations. If that derivation only reconstructs standard Lie-group kinematics, classify it as IMPORTED/KNOWN rather than PDT novelty.
