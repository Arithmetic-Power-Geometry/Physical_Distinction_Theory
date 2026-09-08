# Cycle 004 — Purity-accessible coherence floor

## Status: PROVED corollary; experimentally actionable; historical novelty NOT claimed

Assume the controlled-dephasing sector and the identical-conditional-output condition of the spectral coherence annulus result,

`rho_E^(0) = rho_E^(1) = eta`.

Let `P = Tr(eta^2)` and let `p_max` be the largest eigenvalue of `eta`. The spectral annulus theorem gives

`|chi| >= max(0, 2 p_max - 1)`.

Because

`P = sum_j p_j^2 <= p_max sum_j p_j = p_max`, 

we immediately obtain the tomography-free bound

`|chi| >= max(0, 2 P - 1)`.

Thus any environment with purity `P>1/2` cannot exhibit complete controlled-dephasing cancellation while its two conditional output states remain identical. Conversely, `P<=1/2` makes this purity-only witness trivial, although the full spectrum can still provide a stronger floor.

## Why this matters

The previous annulus theorem requires the largest eigenvalue, hence spectral information. Purity is a single scalar and can in principle be estimated without reconstructing the full density matrix (for example through standard two-copy purity-estimation protocols). This turns the identifiability theorem into a directly testable inequality:

`visibility >= max(0, 2 purity - 1)`

within the theorem's controlled-sector assumptions.

## Kill tests

1. The proof uses only positivity and normalization of the eigenvalues plus the already-proved spectral annulus result.
2. `purity_coherence_bound.py` samples random spectra in dimensions 2–12 and checks that the purity floor never exceeds the exact spectral floor.
3. This is not a same-input deviation from quantum mechanics; it is a QM-compatible PDT operational corollary.
4. Historical novelty is not claimed. Purity/coherence relations and purity estimation are established topics; this formulation is retained as a PDT identifiability diagnostic.

## Research consequence

A claimed experiment with identical conditional outputs, measured `P>1/2`, and observed `|chi| < 2P-1` would falsify at least one assumption entering this controlled-unitary model. It would not by itself establish PDT over QM because the inequality follows from standard unitary quantum mechanics in this sector.
