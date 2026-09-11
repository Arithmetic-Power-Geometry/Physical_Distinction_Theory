# Cycle 087 — Preparation-equivalence no-go for nonlinear PDT state updates

## Target
PDT-II targets (3) and (5): test whether a genuinely nonlinear deterministic pre-measurement state update can yield a same-input quantitative departure from QM while preserving ordinary preparation equivalence and no-signalling semantics.

## Exact hypothesis
Let `Phi_R` be the deterministic state update associated with a fixed declared resource window `R`. Assume operational preparation equivalence: whenever a density operator admits an ensemble preparation

`rho = sum_i p_i rho_i`, 

the unrecorded ensemble and the density operator represent the same physical input for subsequent evolution. Then consistency requires

`Phi_R(rho) = sum_i p_i Phi_R(rho_i)`.

This is exactly affinity on the convex state space. Therefore any genuinely nonlinear deterministic map on density operators violates preparation equivalence for some ensemble. If the affine map is additionally completely positive and trace preserving, it is an ordinary quantum channel. Thus a same-input PDT deviation cannot be obtained merely by inserting a deterministic nonlinear state map while simultaneously retaining ensemble independence, standard subsystem extension, and no-signalling.

## Smallest explicit witness
Take a qubit state

`rho = diag(3/4, 1/4)`

and the nonlinear candidate

`N(rho) = rho^2 / Tr(rho^2)`.

Direct application gives

`N(rho) = diag(9/10, 1/10)`.

But the same rho is the unrecorded spectral ensemble consisting of `|0><0|` with probability 3/4 and `|1><1|` with probability 1/4. Since `N` fixes every pure projector, ensemble-wise application followed by forgetting the classical preparation label gives back

`diag(3/4, 1/4)`.

Hence the same density operator receives two different outputs, with maximum probability-coordinate gap `0.15`. This is a preparation-context dependence, not a defensible same-input prediction under the stated assumptions.

## Stress audit
The frozen regression audit used dimensions `d=1..12,16,24,32,48,64,96,128`, seed 8701, and 20 random diagonal mixed states per nontrivial dimension. All 360 nontrivial cases violated preparation equivalence for `N(rho)=rho^2/Tr(rho^2)`. Dimension 1 is explicitly degenerate. The numerical sweep is a regression test only; the no-go statement follows from convex preparation equivalence itself.

## Prior-art boundary
This is not a PDT novelty claim. Gisin-type no-signalling arguments and later re-derivations show that nonlinear ensemble-dependent quantum evolution generically enables superluminal signalling or otherwise forces linear statistical evolution. Simon, Buzek and Gisin (Physical Review Letters 87, 170405, 2001; DOI 10.1103/PhysRevLett.87.170405) derive linear completely positive density-matrix dynamics from standard quantum kinematics, the trace rule and no-superluminal signalling. Polchinski (Physical Review Letters 66, 397, 1991; DOI 10.1103/PhysRevLett.66.397) showed the signalling pathology for Weinberg nonlinear quantum mechanics. Bassi and Hejazi (European Journal of Physics 36, 055027, 2015; DOI 10.1088/0143-0807/36/5/055027) provide a later re-derivation of the no-signalling/linear-evolution boundary.

## Classification
- PROVED: preparation equivalence forces affinity of a deterministic state update.
- FALSIFIED: a genuinely nonlinear deterministic PDT state update can preserve unrestricted preparation equivalence while supplying a same-input deviation.
- NUMERICALLY SUPPORTED: the explicit normalized-square family failed in all 360 nontrivial regression cases.
- IMPORTED/KNOWN BOUNDARY: the no-signalling/linearity territory is established prior art.
- BREAKTHROUGH CANDIDATE: no.

## Surviving PDT route
A defensible PDT deviation must now do at least one of the following explicitly rather than hiding it: introduce a new physical preparation record, use stochastic dynamics whose operational state includes additional variables, alter subsystem composition/accessibility, restrict the allowed preparation equivalences, or derive a new physical interaction/channel with a quantitative parameter fixed independently of the tested data. Any such route must then pass no-signalling, complete-positivity/extension, composition, and prior-art checks.
