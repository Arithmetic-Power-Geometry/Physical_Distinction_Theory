# Cycle 265 — Binary cross-product selector no-go

## Target attacked
PDT-II target (2): a non-circular PDT-native derivation of n=3, with implications for (1) composition.

## Candidate principle
Let V=R^n with its Euclidean inner product. Postulate a nontrivial bilinear alternating map ×:V×V→V satisfying, for all x,y,

1. <x×y,x>=<x×y,y>=0;
2. ||x×y||^2=||x||^2||y||^2-<x,y>^2.

This is deliberately ambient-sensitive: unlike the embedding-hereditary principles eliminated in Cycle 263, the existence of such a product is a property of the full ambient space.

## Prove-or-falsify result
The candidate does **not** uniquely select n=3. A nontrivial binary vector cross product satisfying the hypotheses exists in dimensions 3 and 7. Dimension 7 is therefore a decisive counterexample to the implication `cross-product principle => n=3`.

The n=7 witness is the standard imaginary-octonion construction: identify V with Im(O) and define x×y = Im(xy). For imaginary octonions this is bilinear and alternating, is orthogonal to x and y, and obeys the norm/Gram identity above. Hence the smallest higher-dimensional survivor is n=7.

The classical classification is stronger: under these hypotheses binary vector cross products occur only in dimensions 0,1,3,7, with the 0- and 1-dimensional cases trivial. Thus among n=1,...,12 the nontrivial existence mask is exactly {3,7}.

## Exact dimension stress table

| n | nontrivial binary VCP exists? | consequence |
|---:|:---:|---|
|1|NO|degenerate/trivial only|
|2|NO|excluded|
|3|YES|candidate accepts target|
|4|NO|excluded|
|5|NO|excluded|
|6|NO|excluded|
|7|YES|decisive counterexample|
|8|NO|excluded|
|9|NO|excluded|
|10|NO|excluded|
|11|NO|excluded|
|12|NO|excluded|

This is theorem-backed classification, not a numerical inference.

## Strengthened survivor
A binary normed cross-product axiom narrows finite Euclidean dimension to {3,7}, but cannot choose 3. Any PDT derivation that uses it must supply an additional independently motivated axiom that rejects the octonionic n=7 survivor. Adding such an axiom merely because it rejects n=7 would be circular and is not accepted.

A tempting extra condition is the Jacobi identity. The ordinary R^3 cross product satisfies Jacobi whereas the standard R^7 octonionic cross product does not. However, using `cross product + Jacobi` as a PDT n=3 derivation is not promoted here: it is established algebraic structure (R^3 cross product is so(3); octonionic nonassociativity obstructs the analogous Lie bracket) and no PDT-native physical reason for imposing Jacobi has yet been derived.

## Prior-art boundary
The dimension restriction is classical mathematics, associated with the vector-cross-product classification (Eckmann; Brown–Gray) and normed division algebras/Hurwitz. Modern expositions explicitly state that nonzero binary cross products occur in dimensions 3 and 7. Therefore neither the {3,7} restriction nor rejection of 7 by importing familiar Lie/Jacobi structure is PDT novelty.

## Status
- binary normed VCP existence => n in {3,7}: **IMPORTED/KNOWN**
- explicit n=7 octonionic survivor: **PROVED** (standard construction; imported mathematics)
- binary normed VCP => n=3: **FALSIFIED**
- smallest decisive higher-dimensional counterexample: **n=7**
- `VCP + Jacobi => n=3` as PDT-native physical derivation: **OPEN / NOT PDT-JUSTIFIED**
- PDT-native composition law: **OPEN**
- same-input P_PDT != P_QM prediction: **OPEN**
- breakthrough candidate: **NO**

## Research consequence
After Cycle 263, ambient-sensitive selectors were the correct place to search. This cycle shows that even a famous genuinely dimension-sensitive structure fails uniqueness because of an exceptional n=7 survivor. Future n=3 candidates must therefore be tested explicitly against exceptional 7-dimensional/octonionic structures, not merely against generic n>3 embeddings.
