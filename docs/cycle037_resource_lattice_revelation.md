# Cycle 037 — Resource-lattice revelation modularity

**Status:** PROVED as finite-dimensional linear algebra; **IMPORTED/KNOWN** mathematics; PDT-specific bookkeeping only. **Not a breakthrough candidate.**

## Setup
Let `V` be a finite-dimensional real vector space of microscopic distinction directions. Represent a resource window `R` by the linear subspace `E_R <= V*` spanned by all effects accessible under that window. Its operational null space is

`N_R = {x in V : e(x)=0 for every e in E_R}`.

By rank-nullity / annihilator duality,

`dim(V/N_R) = dim(E_R)`.

Define the resource join and meet by

`E_(R∨S) = E_R + E_S`,

`E_(R∧S) = E_R ∩ E_S`.

The join means access to both linear effect families; the meet means only effect directions shared by both resource windows.

## Theorem — exact revelation modularity
For any finite-dimensional `E_R,E_S <= V*`,

`d(R∨S) + d(R∧S) = d(R) + d(S)`,

where `d(R)=dim(V/N_R)=dim(E_R)`.

Equivalently,

`d(R∨S)-d(S) = d(R)-d(R∧S)`.

Thus the number of distinction directions newly revealed by adding `R` to `S` is exactly the number of directions available in `R` that were not already shared with `S`.

### Proof
Grassmann's formula gives

`dim(E_R+E_S) = dim(E_R)+dim(E_S)-dim(E_R∩E_S)`.

Rearranging gives the theorem. The quotient-dimension form follows from `dim(V/N_R)=dim(E_R)`.

## Consequences
1. **Redundant effects cannot create revelation.** Adding linearly dependent detector/effect directions does not change `d(R)`.
2. **Nested refinement is monotone.** If `E_R <= E_S`, then `d(R)<=d(S)`, and the gain is `dim(E_S)-dim(E_R)`.
3. **Exact inclusion-exclusion for linear resource windows.** Distinction dimension behaves modularly on the lattice of effect subspaces.
4. **Kill test.** Any PDT model using this linear-effect representation that reports a nonzero modular residual is internally inconsistent, numerically rank-unstable, or is using a resource operation that is not the stated linear join/meet.
5. **No same-input new physics.** The identity does not alter standard quantum probabilities and cannot generate `P_PDT != P_QM` by itself.

## Stress tests
`pdt_resource_lattice.py` implements rank, join, meet, modular residual, unique revelation, and deterministic coordinate audits. `tests/test_pdt_resource_lattice.py` checks dimensions `n=1..12`, random integer effect families, identical/nested resources, redundant effects, and invalid ambient dimensions. `results/cycle037_resource_lattice_audit.csv` records an exact zero residual for the deterministic `n=1..12` family.

## Prior-art boundary
The proof is exactly the classical Grassmann dimension formula and the modular-lattice structure of vector subspaces. Closely related rank language appears in linear matroids. Therefore historical mathematical novelty is not claimed. The only PDT-specific content is the interpretation of quotient rank as resource-relative revealed distinction dimension and its use as a theorem-status consistency check.

## Research consequence
This result strengthens the resource-refinement layer but does **not** solve composition or dimension selection. A genuinely new PDT theorem must leave the purely linear subspace-rank setting—for example by deriving physically constrained nonlinear/composite admissibility, a new operational composition rule, or a same-input law not fixed by standard microscopic quantum mechanics.
