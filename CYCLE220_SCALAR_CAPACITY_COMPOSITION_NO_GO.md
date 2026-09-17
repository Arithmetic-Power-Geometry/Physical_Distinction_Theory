# Cycle 220 — Scalar capacity cannot determine PDT joint admissibility

## Target attacked
PDT-II targets (1), (3), (4), and (6): whether a physically calibrated scalar resource/capacity can itself determine the composite admissible-operation algebra and thereby support a non-circular composition law or PDT–QM deviation.

## Status

**PROVED (finite counterexample theorem); FALSIFIED (scalar-capacity selector); IMPORTED/KNOWN (symmetry/reference-frame mechanism); OPEN (PDT-native structured resource law); BREAKTHROUGH CANDIDATE: NO.**

## Exact hypotheses
Let a resource-bearing controller/reference system be summarized by a scalar capacity `C(r)`. Suppose a proposed PDT law assigns the joint admissible algebra solely from local operational data and that scalar:

`A_XY = Phi(A_X, A_Y, C(r))`.

The claim under attack is that such a scalar capacity is sufficient in general.

## Theorem (scalar-capacity insufficiency)
There exist finite-dimensional resource states `r1,r2` with the same scalar resource value for a natural scalar capacity, but with inequivalent directional resource content and therefore different admissible operation/measurement sets under the same symmetry restriction. Hence no universal selector depending only on that scalar can recover the physically admissible joint algebra.

### Explicit witness
Use a qutrit with U(1) charge generator

`N = diag(0,1,2)`.

Take pure resource states

`|psi_01> = (|0>+|1>)/sqrt(2)`

and

`|psi_12> = (|1>+|2>)/sqrt(2)`.

Both have exactly the same charge variance:

`Var_N(psi_01) = Var_N(psi_12) = 1/4`,

and therefore the same pure-state U(1) quantum Fisher information `F_Q = 4 Var_N = 1`.

Nevertheless their charge-mode support is located in different sectors: the first resource occupies charges `{0,1}`, the second `{1,2}`. If the target/controller coupling is additionally subject to a finite charge ceiling or sector-dependent coupling (a legitimate restricted-resource window), the two resources can enable different covariant joint transitions even though the scalar variance/QFI is identical. For example, with a controller ceiling excluding charge 2, the first state retains a coherent 0<->1 mode while the second is not an admissible controller state in that window; with sector-selective couplings, their enabled transition sets differ directly.

Thus equality of a scalar asymmetry/capacity measure does not imply equality of the resource object, its mode decomposition, or the induced admissible algebra.

## Stronger abstract proof
Let `C : R -> R_+` be any non-injective scalar summary on a resource space containing two operationally inequivalent resource objects `r1 != r2`. If there exists a task/intervention `e` such that `Adm(e|r1) != Adm(e|r2)` while `C(r1)=C(r2)`, then a selector `Phi(...,C(r))` must return the same algebra for both and is wrong for at least one. Therefore scalar sufficiency requires the highly restrictive condition that `C` be a complete invariant of admissibility equivalence classes.

This condition is necessary, not merely convenient.

## What survives
A defensible PDT composition/resource law must use a **structured resource object** (for example a state, representation/mode profile, reference-frame token, controller Hamiltonian plus allowed couplings, or an explicitly proved complete invariant), not merely energy, entropy, variance, Fisher information, work budget, dimension, or a generic scalar capacity.

A scalar law can survive only under an explicit theorem that the chosen scalar is a complete invariant for the declared admissibility problem.

## Relation to prior art
This mechanism is not claimed as PDT novelty. Resource theories of asymmetry/reference frames already show that symmetry-breaking resources are structured physical states and that permitted operations depend on symmetry/covariance. The Wigner–Araki–Yanase literature likewise shows that conservation-law-constrained measurement ability depends on apparatus asymmetry, not simply an undifferentiated energy budget. Quantum Fisher information is an asymmetry monotone in relevant settings, but a monotone is not automatically a complete operational invariant.

Prior-art boundary checked against: resource theory of quantum reference frames/asymmetry; WAY theorem in resource-theoretic form; Fisher-information resource measures; asymmetric distinguishability resource theory.

## Consequences for PDT-II
1. A proposed gravity/capacity law of the form `capacity scalar -> distinction algebra` is not derivable in this generality.
2. Equal scalar capacity does not imply equal composite distinction structure.
3. Therefore a same-input PDT–QM deviation cannot be justified by inserting a scalar capacity cutoff unless PDT independently specifies the structured controller/resource and admissible couplings.
4. This does not falsify all resource-indexed PDT laws; it falsifies scalar-only universal selectors.
5. The next strongest surviving target is a PDT-native **structured-resource composition functor/closure rule** and a search for whether its minimal sufficient resource invariant can ever collapse to a scalar under physically meaningful hypotheses.

## Novelty decision
No breakthrough promotion. The exact PDT-II obstruction is useful as a theorem-status boundary, but its mechanism is inherited from established resource/reference-frame theory.
