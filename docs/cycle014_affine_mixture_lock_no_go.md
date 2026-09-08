# Cycle 014 — Affine-Mixture Lock No-Go

## Status

**PROVED / IMPORTED-KNOWN convex mathematics / DECISIVE FALSIFICATION of a candidate deviation route.**

No historical novelty is claimed for convex linearity. The PDT contribution here is the use of the result as a same-input kill test.

## Candidate route attacked

Could PDT agree exactly with standard quantum mechanics on every pure microscopic preparation, but generate a quantitatively different prediction only for mixed states while retaining ordinary consistency under classical random preparation mixtures?

## Theorem (Affine-Mixture Lock)

Fix a resource window `R` and an outcome/effect `E`. Let `P_PDT(E|rho,R)` be a candidate PDT probability on density operators. Assume:

1. **Preparation-mixture affinity:** for every finite ensemble, `P_PDT(E|sum_i p_i rho_i,R) = sum_i p_i P_PDT(E|rho_i,R)`.
2. **Pure-state same-input agreement:** for every pure state `psi`, `P_PDT(E| |psi><psi|,R) = Tr(E |psi><psi|)`.

Then for every mixed state `rho`,

`P_PDT(E|rho,R) = Tr(E rho)`.

### Proof

Take a spectral decomposition `rho = sum_i lambda_i |i><i|`. By preparation-mixture affinity,

`P_PDT(E|rho,R) = sum_i lambda_i P_PDT(E||i><i|,R)`.

By pure-state agreement this equals

`sum_i lambda_i Tr(E|i><i|) = Tr(E rho)`.

No dimension restriction is required, including the qubit case, because affinity is assumed operationally rather than derived from Gleason-type projection additivity.

## Robust version

If instead every pure-state deviation obeys

`|P_PDT(E|psi,R) - P_QM(E|psi)| <= epsilon`

and mixture affinity still holds, then every mixed state obeys the same uniform bound

`|P_PDT(E|rho,R) - P_QM(E|rho)| <= epsilon`.

This follows because the mixed-state deviation is a convex combination of the pure-state deviations. Thus classical mixing cannot amplify a uniformly bounded pure-state discrepancy.

## Consequence for the breakthrough search

A PDT same-input deviation cannot be hidden exclusively in mixed preparations while retaining both ordinary preparation mixing and exact pure-state QM agreement. Any such deviation must break at least one of the following:

- pure-state agreement,
- affine consistency under classical preparation mixing,
- the identification of the microscopic state/effect,
- or the physical dynamics/measurement law itself.

This result complements the resource-coarse-graining no-go: neither classical post-processing of outcomes nor classical mixing of otherwise unchanged preparations can manufacture a new same-input microscopic prediction.

## Numerical stress audit

`pdt_affine_mixture_lock.py` checks random complex density operators and effects for dimensions `d=1..12`, comparing the Born probability with the affine reconstruction from the spectral pure-state ensemble. A fixed-seed 100-trial audit gave maximum floating-point reconstruction residual below `8e-16`. The robust `epsilon=0.01` test also remained below the prescribed bound in every tested dimension. Unit tests additionally sample convex mixtures up to dimension 100.

These numerical checks support implementation correctness only; the theorem itself is analytic.

## Prior-art boundary

The underlying convex structure of quantum states and linear Born probabilities is standard. Gleason/Busch-type results go further in deriving quantum probability representations from additivity/noncontextuality assumptions. This cycle therefore makes no mathematical novelty claim. Its role is to eliminate a false PDT breakthrough route and sharpen the conditions any future deviation must violate or modify explicitly.
