# PDT Breakthrough Proof State

This folder is the canonical theorem-development record for the Physical Distinction Theory (PDT) quantum-reconstruction program. It separates proven statements, imported literature theorems, conditional bridges, failed implications, and open targets so that later manuscript/software revisions do not accidentally overclaim.

## Current strongest reconstruction chain

1. **Elementary binary capacity**: maximal perfectly distinguishable frame size is two.
2. **Complete elementary resolution**: an elementary mixed state contains no irreducible residual distinction beyond one maximal binary distinction and its bias.
3. **Unbiased complete erasure**: erasing any maximal elementary distinction without bias gives the reversible-invariant state.
4. **Continuous reversible equivalence**: the connected reversible group is transitive on pure elementary states.
5. These imply a centrally symmetric convex state space whose entire boundary is pure and on which the reversible group acts transitively.
6. Haar-averaging an auxiliary inner product over the compact reversible group makes the boundary a Euclidean sphere. Hence the elementary state space is an ellipsoid, affinely equivalent to a Euclidean ball `B^n`.
7. Therefore quadratic distinction geometry and the parallelogram identity (BQDC) are **derived**, not primitive.
8. For locally tomographic bipartite composites with continuous reversible dynamics, existence of genuine reversible interaction/entanglement selects `n=3` from the Euclidean-ball family (Masanes, Müller, Pérez-García, Augusiak, J. Math. Phys. 55, 122203, 2014; DOI 10.1063/1.4903510).
9. Thus the elementary nonclassical state space is the Bloch ball `B^3`.
10. With suitable Jordan/composite assumptions and local tomography, established reconstruction theorems select ordinary finite-dimensional complex quantum theory.
11. Born probabilities then arise from the normalized positive affine/trace pairing of states and effects; continuous reversible dynamics yields unitary dynamics in the connected component.

## Independent cross-checks

- Bit symmetry implies self-duality: Müller & Ududec, PRL 108, 130401 (2012).
- Strong symmetry + spectrality characterizes simple Euclidean Jordan state spaces or simplices: Barnum & Hilgert, arXiv:1904.03753; Journal of Lie Theory 30 (2020) 315-344.
- Rank-two monotone Bregman divergence forces ball/spin-factor geometry: Harremoës, arXiv:1707.03222.
- Euclidean-ball composites + local tomography + continuous reversible dynamics + entanglement/interaction select the three-dimensional Bloch ball: Masanes et al., DOI 10.1063/1.4903510.

## Critical novelty boundary

The mathematical ingredients above have substantial prior art. PDT must **not** claim those literature theorems as new. The strongest potential PDT novelty lies in the upstream operational derivation:

`resource-bounded physical distinction -> elementary resolution/erasure structure -> transitive convex rigidity -> Euclidean distinction geometry -> BQDC`,

and in connecting the same physical primitive to quantum correlations, causal geometry, and capacity.

## Current highest-value unresolved theorem

The remaining foundational bridge is:

> Can the global finite-resource distinction capacity `K_epsilon` itself imply the elementary radial-resolution/erasure conditions, rather than those conditions being added as separate postulates?

A bare statement that the maximal codebook has size two is **not sufficient by itself** to force spectrality or radial binary decomposition. A successful theorem must add an operational completeness/sufficiency property that genuinely links global codebook capacity to the local convex geometry.

See `quantum_reconstruction_proof.md` and `proof_status.md` for the formal chain and exact proof-status labels.
