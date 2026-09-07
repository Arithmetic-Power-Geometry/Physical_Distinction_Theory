# PDT Equation Registry - manuscript synchronized

This registry mirrors the submission-ready paper. Logical status is explicit: PDT-native, conditional, imported/standard, or open frontier.

## Core and geometry
1. Resource window: `R=(E,tau,A,R_region,epsilon)`.
2. Finite-resource capacity: `K_epsilon=sup_C log2|C|`.
3. Separation: `K_epsilon != Q_D`.
4. CEU/CER insufficiency: the `l_p` family with `p != 2` violates the parallelogram identity.
5. Under CEU+CER+RDE plus finite dimensionality, closed reversible group and maximal-pair coverage: elementary body is an ellipsoid, affinely `B^n`.
6. BQDC: `Q_D(x+y)+Q_D(x-y)=2Q_D(x)+2Q_D(y)`.
7. CEU+CER+RDE do not select `n=3`.
8. Local state spaces do not determine a unique composite.
9. `B^n -> B^3` under local tomography + continuous reversible interaction is an imported reconstruction boundary.

## Probability and correlation
10. Conditional quadratic probability theorem: normalized positive orthogonal additivity implies `F(q)=q`.
11. Conditional Born form: `p_i=|a_i|^2/sum_j|a_j|^2` after amplitude assumptions are supplied.
12. Centered separate affinity gives `E(a,b)=a^T T b`.
13. If `||T||_op<=1` in Euclidean local spaces, `|S_CHSH|<=2 sqrt(2)`.

## Channels and records
14. Restricted norm: `||X||_R=sup_E |Tr(EX)|` and quotient by its null kernel.
15. John ellipsoid: `J_R={x:x^T G_R x<=1}` and reversible covariance `U^T G_R U=G_R`.
16. Stinespring global trace-distinction invariance and reduced-channel contraction.
17. Pure record: `kappa=<e1|e0>`, `c'=c kappa`, `D_E=sqrt(1-|kappa|^2)`.
18. Mixed record: `chi=Tr(U0 eta U1^dagger)`, `c'=c chi`.
19. Mixed-record envelope: `|chi| <= f_E <= sqrt(1-D_E^2)`.
20. General CPTP record object: complementary-channel pair, not a universal scalar.

## ADDE and dynamics
21. `Gamma_A=-d ln|chi_tot|/dt` where the overlap is nonzero and differentiable.
22. `dot rho=-i[H_eff,rho]/hbar + Gamma_A(E_R-I)[rho]` in the controlled-record sector.
23. Deterministic pure records: `Gamma_A=-nu ln|kappa|=-(nu/2)ln(1-D_E^2)`.
24. Weak-record expansion: `Gamma_A=nu D_E^2/2+O(D_E^4)`.
25. Poisson event counts: `Gamma_A^Pois=nu(1-kappa)` for real `0<=kappa<=1`.
26. Phase-complete relation: `dot c / c = -Gamma_A + i dot(phi)`.
27. **Canonical total distinction tensor**: `A_R^tot=-(1/2)(dot G_R+L^T G_R+G_R L)`.
28. Exact identity: `-(1/2)d(X^T G_R X)/dt=X^T A_R^tot X`.
29. The old `-(1/2)dot G_R` is only the resource/metric-motion component, never the total tensor.
30. Negative quadratic directions of `A_R^tot` witness resource-relative distinction backflow.
31. Same-input controlled-record equivalence: PDT and microscopic QM give the same `chi(t)` for the same environment state and controlled unitaries.

## Thermodynamic / hypothesis-testing sector
32. Keep `K_D`, `H_D^R`, `B_C`, and thermodynamic entropy production distinct.
33. Conditional Landauer setting: `Q_env >= k_B T ln2 H_D^R`.
34. `Gamma_A=ln2 Phi_C` is a record identity, not a generic thermodynamic entropy-production law.
35. Resource-restricted `beta_{epsilon,R}` and `D^epsilon_{H,R}=-log2 beta`.
36. Resource-restricted free-energy monotone `F^epsilon_{H,R}`.

## Frontier only
37. Horizon/capacity and gravity formulae are conjectural targets, not PDT theorems.
