# Cycle 128 — Composite-carrier dimension no-go

## Status

- **PROVED:** Under the stated product-distinguishability hypothesis, `dim(W) >= dim(V_A) dim(V_B)`.
- **FALSIFIED:** A same-`n` carrier `W = V` for two `n`-dimensional inputs when `n > 1` and all basis-product directions must remain linearly independent.
- **IMPORTED/KNOWN:** Universal bilinear factorization through the tensor product and its dimension formula.
- **OPEN:** A genuinely PDT-native derivation of the appropriate composite carrier, its admissible product effects, and whether PDT should require full product-direction distinguishability.
- **BREAKTHROUGH CANDIDATE:** No.

## Exact hypotheses

Let `V_A`, `V_B`, and `W` be finite-dimensional real vector spaces and let

`mu : V_A x V_B -> W`

be bilinear. Choose bases `{e_i}` and `{f_j}`. Assume the product images

`mu(e_i,f_j)`

are linearly independent. This is the explicit hypothesis being audited; it must not be silently equated with a generic notion of composition.

## Theorem

There are `dim(V_A) dim(V_B)` such independent product images. Therefore

`dim(W) >= dim(V_A) dim(V_B)`.

Equivalently, by the universal property of the tensor product, `mu` factors through a linear map

`M : V_A tensor V_B -> W`.

If all elementary product directions remain independent, `M` is injective, so the same dimension lower bound follows.

For equal local dimensions `n`, forcing `dim(W)=n` gives a kernel of dimension at least

`n^2 - n`.

Thus for every `n>1`, some product directions necessarily collapse.

## Smallest decisive counterexample to same-carrier closure

At `n=2`, four elementary product directions must fit into a 2-dimensional target. Rank-nullity forces kernel dimension at least 2. Hence a same-carrier bilinear composition cannot preserve all product distinctions.

## Consequence for PDT-II architecture

The Cycle-127/earlier `n=3`-selecting interaction bracket should not be identified with complete-system composition. A viable architecture may instead have:

1. a local distinction carrier `V_A` for each subsystem;
2. a separate composite carrier `V_AB` with sufficient dimension to retain whichever product distinctions PDT declares operationally resolvable;
3. a derived local interaction bracket that may map back into a local carrier and select `n=3` under extra symmetry assumptions.

This theorem does **not** derive tensor-product quantum mechanics, entanglement, the Born rule, or local tomography.

## Prior-art boundary

The mathematical mechanism is standard multilinear algebra: tensor products are universal recipients of bilinear maps, and locally tomographic GPT frameworks commonly represent composites in tensor-product vector spaces. Therefore the dimension bound itself is not claimed as a PDT novelty. Its role here is a falsification guard against an internally inconsistent same-carrier composition proposal.

Relevant prior-art anchors checked in this cycle include the standard tensor-product universal property and GPT composite-state frameworks such as Janotta & Lal, *Phys. Rev. A* 87, 052131 (2013), DOI: 10.1103/PhysRevA.87.052131.

## Audit coverage

The exact corollary was checked for `n=1..12` and `n=16,24,32,48,64,96,128`. No nontrivial dimension satisfies `n^2 <= n`. The computation is regression evidence only; the proof is exact.
