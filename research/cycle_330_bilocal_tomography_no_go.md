# PDT-II Cycle 330 — Bilocal-tomography route audit

## Target attacked
1. PDT-native composition law.
2. Non-circular PDT-native `n=3` derivation.
3. Same-input PDT/QM prediction.

## Candidate
Replace local tomography by bilocal tomography: global states are determined by observables involving at most pairs of elementary subsystems. Ask whether this weaker composition principle uniquely selects PDT composition or `n=3`.

## Exact counterfamily
Real-vector-space quantum theory supplies a finite-dimensional counterfamily for every local Hilbert dimension `N >= 1`. Define

- `K(N)=N(N+1)/2`, the number of real parameters of an unnormalised real-symmetric state;
- `L(N)=N(N-1)/2`, the complementary latent count.

For a standard real tensor product with `N_AB=N_A N_B`, direct algebra gives

`K(N_A N_B) = K(N_A)K(N_B) + L(N_A)L(N_B)`.

Proof: expanding the RHS gives

`[N_A(N_A+1)N_B(N_B+1)+N_A(N_A-1)N_B(N_B-1)]/4`
`= N_A N_B(N_A N_B+1)/2 = K(N_A N_B)`.

Thus the same bilocal composition identity holds for every positive integer local dimension. There is no algebraic singularity or selector at `N=3`. The smallest nontrivial countermodel is `N=2`, where `K=3` and `L=1`; `N=3` merely gives `K=6`, `L=3`.

## Consequences
- Bilocal tomography does **not** imply `n=3`.
- It does **not** uniquely determine a PDT-native composite law: real quantum theory is an already-known non-PDT realization.
- It does **not** by itself entail a same-input probability deviation from complex QM. A 2026 result by Hoffreumon and Woods goes further: under operational source independence, every finite network correlation of complex QT can be reproduced in real QT with the same measurement locality structure, extending to finite sequential multipartite protocols. Hence failure of local tomography alone is especially unsafe as a route to a claimed experimental discriminator.
- No gravity/capacity law follows.

## Dimension stress
Exact integer checks for `N=1..12` are recorded in `artifacts/cycle_330_bilocal_tomography_n1_12.csv`. The identity is polynomial, so the proof covers all finite positive integer `N`, not only the tested range.

## Prior art
- L. Hardy and W. K. Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, Foundations of Physics 42 (2012), arXiv:1005.4870: real-vector-space quantum theory is bilocally tomographic and motivates the `K/L` composition structure.
- T. Hoffreumon and M. P. Woods, *Quantum theory based on real numbers cannot be experimentally falsified*, arXiv:2603.19208 (19 Mar 2026): operational-independence equivalence results sharply constrain attempts to turn real-vs-complex composition differences into an experimental discriminator.

## Status ledger
| Claim | Status |
|---|---|
| Real-QT `K/L` composition identity | PROVED / IMPORTED-KNOWN model |
| Identity for `N=1..12` | PROVED |
| Bilocal tomography selects `n=3` | FALSIFIED |
| Bilocal tomography uniquely fixes PDT composition | FALSIFIED |
| Bilocal tomography alone forces `P_PDT != P_QM` | FALSIFIED as an inference |
| Bilocal tomography yields PDT gravity/capacity law | OPEN / unsupported |
| PDT-native correlated-composite selector | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Research direction after falsification
Do not spend further cycles stacking generic `k`-local tomography axioms as dimension selectors unless a PDT-native mechanism independently fixes `k` or supplies an additional invariant. The next composition candidate must arise from the internal distinction/refinement algebra and must constrain correlated tensors beyond merely declaring the maximum locality order of tomography.
