# Cycle 290 — Jacobi selector boundary for the PDT n=3 target

## Status

This cycle attacks the strongest survivor from Cycle 289: a normed bilinear antisymmetric distinction cross-product leaves the known dimensions n=3 and n=7. The question is whether a non-circular reassociation/closure law can eliminate n=7.

## Candidate hypotheses

Let V be a finite-dimensional real Euclidean distinction space with a bilinear operation x × y satisfying:

1. antisymmetry: x × y = -(y × x);
2. orthogonality: <x × y,x>=<x × y,y>=0;
3. norm/area law: ||x × y||^2 = ||x||^2||y||^2 - <x,y>^2;
4. nontriviality;
5. Jacobi closure: x × (y × z)+y × (z × x)+z × (x × y)=0 for all x,y,z.

Hypotheses 1–4 are the Cycle-289 cross-product package. Hypothesis 5 is tested here as a possible operational reassociation/closure principle; it is NOT yet claimed PDT-native.

## Exact result

**CONDITIONAL / IMPORTED-KNOWN mathematical selector.** Under 1–4, the classical vector-cross-product classification leaves n in {3,7} (apart from trivial dimensions). The 3D cross product satisfies Jacobi. The 7D octonionic cross product does not. Therefore hypotheses 1–5 select n=3 among the nontrivial normed binary cross-product cases.

This is not a PDT breakthrough: both the {3,7} classification and failure of Jacobi for the octonionic 7D product are established mathematics. PDT still owes an independently physical reason why distinction composition must obey Jacobi closure rather than merely alternative/Moufang structure.

## Small exact n=7 witness

Use the oriented Fano triples

(1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5).

For x=e1, y=e2, z=e4:

- e2 × e4 = e6 and e1 × e6 = -e7;
- e4 × e1 = -e5 and e2 × (-e5) = -e7;
- e1 × e2 = e3 and e4 × e3 = -e7.

Hence

J(e1,e2,e4) = e1×(e2×e4)+e2×(e4×e1)+e4×(e1×e2) = -3 e7 != 0.

So the n=7 survivor is decisively excluded **if and only if** Jacobi is independently justified.

## Dimension stress test

- n=1: only trivial binary normed cross product; not a nontrivial survivor.
- n=2: no nontrivial binary vector cross product with the full orthogonality + area norm package.
- n=3: survivor; Jacobi holds.
- n=4,5,6: excluded by the known cross-product classification.
- n=7: survives 1–4 but is falsified by Jacobi; exact witness above.
- n=8,9,10,11,12: excluded by the same classification.
- higher finite n: no additional nontrivial binary vector cross-product dimensions under 1–4.

## Adversarial interpretation check

It would be circular to add “associativity” merely because quaternions are associative. Jacobi is weaker/different and has a clean closure interpretation, but that does not make it PDT-native. A valid PDT-II derivation must derive Jacobi from an operational statement about sequential distinctions, path/reassociation independence, reversible generators, or observable records without mentioning dimension 3, SO(3), quaternions, or Jacobi as a desired algebraic answer.

Moufang/alternative octonionic composition remains the adversarial control: if the proposed operational principle is also satisfied by that structure, n=7 survives.

## Prior-art boundary

The key facts are classical: nontrivial binary normed vector cross products occur in dimensions 3 and 7; the 7D product is the imaginary-octonion cross product; its Jacobiator is proportional to the octonion associator and is generally nonzero. These facts must be cited as prior art, not PDT novelty.

## Theorem-status ledger delta

| Claim | Status |
|---|---|
| Cross-product package 1–4 implies n=3 | FALSIFIED (Cycle 289; n=7 countermodel) |
| Cross-product package 1–5 implies n=3 among nontrivial cases | CONDITIONAL / IMPORTED-KNOWN |
| 7D octonionic cross product violates Jacobi | PROVED here by exact witness; IMPORTED/KNOWN generally |
| Jacobi is forced by PDT operational distinction principles | OPEN |
| Non-circular PDT-native n=3 derivation | OPEN |
| Same-input PDT-vs-QM quantitative deviation | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Next prove-or-falsify obligation

Formalize the weakest operational sequential-distinction/reassociation statement that could imply Jacobi, then test it explicitly against quaternionic/3D, octonionic/Moufang 7D, classical/GPT, restricted-resource, and controlled-environment models. If the operational statement merely restates Jacobi algebraically, reject it as circular/imported.
