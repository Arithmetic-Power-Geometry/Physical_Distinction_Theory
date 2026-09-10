# Cycle 044 — Affine effect absorption theorem

**Status:** PROVED as finite-dimensional convex/linear mathematics; IMPORTED/KNOWN; PDT-specific same-input no-go corollary.

## Statement

Fix a resource context `R` and a finite-dimensional complex Hilbert space. Let `f_R(rho)` be a probability assigned to every density matrix. Assume:

1. **Preparation-mixture affinity:** `f_R(t rho + (1-t) sigma) = t f_R(rho) + (1-t) f_R(sigma)` for every `t in [0,1]`.
2. **Probability bounds:** `0 <= f_R(rho) <= 1` for every density matrix.

Then there exists a Hermitian operator `E_R` such that

`f_R(rho) = Tr(E_R rho)`

for every density matrix, and the probability bounds force

`0 <= E_R <= I`.

Thus `E_R` is an ordinary quantum effect.

## Proof

The density matrices affinely span the trace-one Hermitian hyperplane. Any affine real functional on that hyperplane extends to a linear functional on the finite-dimensional real vector space of Hermitian matrices (an additive constant on trace-one matrices can be absorbed into a multiple of the identity because `Tr(rho)=1`). By the Hilbert-Schmidt/Riesz representation, there is a unique Hermitian `E_R` with

`f_R(rho)=Tr(E_R rho)`.

For every unit vector `psi`, the pure state `rho=|psi><psi|` gives

`0 <= <psi|E_R|psi> <= 1`.

The variational characterization of Hermitian eigenvalues then yields `0 <= E_R <= I`.

## PDT consequence

Suppose PDT keeps ordinary classical preparation mixing and standard density matrices but proposes a resource-dependent affine probability rule. The theorem says that, for every fixed resource context, the rule is operationally equivalent to replacing the declared measurement effect `E` by an effective effect `E_R`.

Therefore a claimed same-input deviation cannot simultaneously assert all of the following:

- the microscopic density matrix is unchanged;
- the physical measurement/effect is unchanged;
- classical preparation-mixture equivalence is unchanged;
- the probability law remains affine;
- nevertheless probabilities differ.

If the affine prediction differs, then the effective effect differs. That is a changed physical measurement/effect assignment, not a free-standing new probability calculus.

## Escape coordinates

A same-input PDT deviation must explicitly change at least one of:

1. preparation-mixture affinity/equivalence;
2. the microscopic state assignment;
3. the physical measurement/effect assignment;
4. dynamics/process;
5. the probability framework itself (e.g. contextual or non-affine structure).

A nonlinear correction such as a purity-dependent term can escape effect absorption, but it immediately fails ordinary preparation-mixture affinity in generic mixed-state decompositions. The code records this only as a kill-test example, not as a proposed physical model.

## Prior-art boundary

The underlying result is standard finite-dimensional convex operational mathematics: quantum effects are bounded positive affine functionals on the quantum state space. GPT frameworks likewise formulate effects as affine/linear functionals on states. No historical novelty is claimed for this representation theorem.

The PDT-specific contribution of this cycle is the explicit no-go ledger entry: **resource dependence plus affinity is absorbed into an effective effect**. Therefore target (3), a same-microscopic-input PDT-vs-QM probability difference, must expose which physical/operational premise actually changes.

## Computational audit

`pdt_affine_effect_absorption.py` and `tests/test_pdt_affine_effect_absorption.py` audit:

- dimensions 1 through 12;
- random density matrices and effects;
- probability bounds from effect spectra;
- exact preparation-mixture affinity up to floating-point roundoff;
- an explicit purity-dependent nonlinear candidate that generically violates affinity.

The computations illustrate the theorem; they are not substitutes for the proof.
