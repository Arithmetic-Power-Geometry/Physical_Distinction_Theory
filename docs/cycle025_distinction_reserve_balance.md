# Cycle 025 — Exact Distinction-Reserve Balance

## Status

**PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN.** Not a breakthrough candidate.

For two joint system-environment preparations define total trace distinction `T=D(rho_SE^1,rho_SE^2)`, locally accessible distinction `S=D(rho_S^1,rho_S^2)`, and the inaccessible reserve

`R = T - S >= 0`.

For a common CPTP evolution of the joint system from `s` to `t`, define global distinguishability loss `L=T(s)-T(t)>=0`. Then the following identity is exact:

`S(t)-S(s) = R(s)-R(t)-L`.

Hence

`S(t)-S(s) <= R(s)`.

For a common joint unitary, `L=0`, so the balance becomes the exact conservation/exchange law

`Delta S = - Delta R`.

This sharpens Cycle 024. Its correlation/environment quantity is a convenient upper estimate on the reserve, while `R=T-S` is the exact inaccessible distinguishability budget at the reference time.

## Proof

The identity follows algebraically from `R=T-S`. Contractivity of trace distance under CPTP maps gives `L>=0`, and contractivity under partial trace gives `R>=0`. A unitary preserves trace distance, so `L=0` exactly.

## Same-input kill test

Under standard quantum microscopic inputs and the same allowed dynamics, a local distinction gain greater than the initial reserve is impossible. A PDT candidate exceeding this bound must alter a physical ingredient rather than relabel hidden information. For unitary closed `SE` evolution, every increase of local distinction is paid exactly by a decrease of inaccessible reserve.

## Stress audit

Fixed-seed random mixed-state tests use system dimensions 1 through 12, a two-dimensional environment, and 100 trials per dimension. Both Haar-like unitary evolution and unitary followed by depolarization were checked. Maximum absolute balance residual was `1.11e-16`; no gain exceeded the initial reserve. Unit tests add dimensions 16 and 24.

## Prior-art boundary

The underlying information-flow interpretation is established. Breuer, Laine and Piilo introduced trace-distance distinguishability backflow, and the 2016 review explicitly writes internal plus external information as a conserved quantity under unitary system-environment evolution. Cycle 025 therefore records a clean PDT resource ledger, not historical novelty.

Prior-art anchors: PRL 103, 210401 (2009); PRA 81, 062115 (2010); Rev. Mod. Phys. 88, 021002 (2016), arXiv:1505.01385.
