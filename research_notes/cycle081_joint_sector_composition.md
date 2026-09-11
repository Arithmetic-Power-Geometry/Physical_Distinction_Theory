# Cycle 081 — Exact quadratic local/joint-sector composition

## Status

- **PROVED**: exact decomposition of normalized quadratic distinction energy into local A, local B, and nonnegative joint operator sectors.
- **IMPORTED/KNOWN**: the mathematical decomposition is a direct consequence of the generalized Bloch/coherence-vector representation and Hilbert–Schmidt orthogonality; it is not claimed as historically new.
- **NUMERICALLY SUPPORTED**: regression audit through local dimensions 1–12 with dense random states and higher-dimensional commuting tests through 128.
- **BREAKTHROUGH CANDIDATE: NO**.

## Statement

For a bipartite density operator `rho_AB` on dimensions `d_A x d_B`, define

`E_d(rho) = d Tr(rho^2) - 1`.

Let

`J_AB = rho_AB - rho_A tensor I_B/d_B - I_A/d_A tensor rho_B + I_AB/(d_A d_B)`.

Then

`C_AB = d_A d_B Tr(J_AB^2) >= 0`

and exactly

`E_AB = E_A + E_B + C_AB`.

For product states `rho_AB = rho_A tensor rho_B`,

`J_AB = (rho_A-I_A/d_A) tensor (rho_B-I_B/d_B)`,

so

`C_AB = E_A E_B`.

Hence the earlier product pseudo-additivity is recovered as a special case:

`E_AB = E_A + E_B + E_A E_B`.

## Proof

Choose Hilbert–Schmidt orthonormal Hermitian bases

`F_0 = I_A/sqrt(d_A), F_i (i>0)` and `G_0 = I_B/sqrt(d_B), G_j (j>0)`,

with every nonzero-index basis element traceless. Expand

`rho_AB = sum_{mu,nu} r_{mu,nu} F_mu tensor G_nu`.

Normalization fixes `r_00 = 1/sqrt(d_A d_B)`. The sectors `(i,0)`, `(0,j)`, and `(i,j)` are mutually Hilbert–Schmidt orthogonal. Direct partial tracing gives

`E_A = d_A d_B sum_i r_{i0}^2`,

`E_B = d_A d_B sum_j r_{0j}^2`,

while

`C_AB = d_A d_B sum_{i,j} r_{ij}^2`.

Because

`E_AB = d_A d_B Tr(rho_AB^2)-1`,

orthogonality yields

`E_AB = E_A + E_B + C_AB`.

Nonnegativity follows because `C_AB` is a squared Hilbert–Schmidt norm.

## Important boundary

`C_AB` must **not** be called connected correlation or correlation beyond independence. It can be nonzero for product states, where it equals `E_A E_B`. The genuinely connected correction relative to product pseudo-additivity,

`K_AB = E_AB-E_A-E_B-E_AE_B = C_AB-E_AE_B`,

remains sign-indefinite, as established in Cycle 075. Thus Cycle 081 repairs the composition ledger only by distinguishing the nonnegative *joint operator sector* from the signed *connected correlation residual*.

## Stress audit

Frozen result: `results/cycle081_joint_sector_composition.json`.

- Dense random bipartite states: local dimensions 1–12, 60 cases.
- Higher-dimensional commuting/diagonal states: 16, 24, 32, 48, 64, 96, 128, 56 cases.
- Minimum observed `C_AB`: 0.0 (degenerate/maximally mixed boundary).
- Maximum decomposition residual: `8.881784197001252e-16`.
- Unit tests additionally cover product states, maximally mixed states, and the Bell state (`C_AB=3` for two qubits).

The numerical audit is regression evidence only; the theorem is algebraic.

## Prior-art boundary

Generalized Bloch/coherence-vector decompositions of bipartite density matrices and their correlation tensors are established. Relevant examples include:

- Maziero, *Computing Coherence Vectors and Correlation Matrices with Application to Quantum Discord Quantification* (2016), DOI 10.1155/2016/6892178.
- Shen et al., *Improved Separability Criteria Based on Bloch Representation of Density Matrices*, Scientific Reports 6, 28850 (2016).
- Morelli et al., *Correlation constraints and the Bloch geometry of two qubits*, Physical Review A 109, 012423 (2024), DOI 10.1103/PhysRevA.109.012423.

These works are sufficient to reject a novelty claim for the Hilbert–Schmidt/Bloch-sector decomposition itself.

## Consequence for PDT-II

The composition target is now separated into two layers:

1. **Solved but known mathematical layer:** quadratic distinction has an exact nonnegative decomposition into local and joint operator sectors.
2. **Still OPEN PDT-native layer:** derive a new physical law governing the *accessible cost, dynamics, scaling, conservation, or experimental constraint* of the joint sector `J_AB` (or of connected cumulants) that is not simply generalized Bloch algebra or standard quantum information.

Any future PDT composition claim must preserve this distinction.
