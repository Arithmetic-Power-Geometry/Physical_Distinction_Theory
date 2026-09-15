# PDT-II Cycle 151 — Operational Quotient Boundary

## Target

This cycle attacks the Cycle-150 open bridge: when may a split/merge pair be declared operationally free without assuming the desired scalar composition law?

## Theorem — quotient-extensional invariance

Fix a declared resource window R and let `pi_R(x)` denote the complete operational record visible through that window. Define operational equivalence by `x ~_R y` iff `pi_R(x)=pi_R(y)`.

Let a ledger `M_R` be **quotient-extensional**, meaning there exists a function `m_R` on operational equivalence classes such that

`M_R(x)=m_R(pi_R(x))`.

If a refinement `E` is observationally neutral in the declared window,

`pi_R(E x)=pi_R(x)`

for every admissible `x`, then

`M_R(E x)=M_R(x)`.

Likewise, if an exact merge `C` satisfies `pi_R(C y)=pi_R(y)` on the refined image, it preserves every quotient-extensional ledger.

**Proof.** Substitute equality of operational records into the factorization `M_R=m_R o pi_R`. QED.

Classification: **PROVED**, but the factor-through-a-quotient mechanism is general mathematics and is not claimed as novel.

## Why this helps — and why it does not close PDT composition

This removes one circularity from Cycle 150: one need not first assume scalar additivity to certify invariance of a refinement. It is enough to prove from PDT primitives that the refinement changes only representation labels and leaves the complete declared operational record unchanged, *and* that the PDT resource ledger is defined extensionally on that operational quotient.

However, the second clause is essential. Observational neutrality/recoverability does **not** imply invariance of an arbitrary representation-sensitive ledger.

### Decisive counterexample

For nonnegative share vectors define

`L(q)=sum_i q_i + 0.1 * #(positive components)`.

Split one positive component `q_i` into any `k>=2` positive daughters whose weights sum to one. The daughters merge exactly back to the original component and the total share is unchanged, but

`L(Eq)-L(q)=0.1*(k-1) > 0`.

Thus the stronger statement

> exact recoverability + preservation of coarse observable mass => every resource ledger is invariant

is **FALSIFIED**.

The counterexample is intentionally elementary: it isolates the logical gap rather than claiming new mathematics.

## Exact audit

The executable audit uses exact rational arithmetic over dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`

with random positive rational daughter weights and edge cases containing zero components.

Frozen results:

- cases: **570**
- exact split/merge recovery failures: **0**
- additive/coarse-mass ledger failures: **0**
- representation-sensitive ledger changes: **570/570**

The audit validates the implementation examples only; the theorem is analytic.

## Prior-art boundary

Factoring a quantity through an equivalence relation/quotient and invariance under maps that preserve the quotient class are standard mathematical constructions. In information/resource theories, data-processing and sufficient-statistic/recovery ideas similarly distinguish operationally relevant information from representation detail. No novelty is claimed for that abstract mechanism.

## Surviving PDT-native obligation

Cycle 151 sharpens the bridge to two independent prove-or-falsify questions:

1. **Operational neutrality:** can PDT primitives prove that local refinement/merge leaves the complete declared resource-window record `pi_R` unchanged?
2. **Extensionality:** can PDT define the target resource ledger from that operational record alone, without smuggling additive/quadratic composition into `pi_R` or `m_R`?

Only if both are independently established does Cycle 151 imply local refinement invariance; Cycle 149 can then force additive resolved composition.

This is a stronger non-circular formulation than simply declaring split and merge to be free.

## Status ledger

- quotient-extensional invariance theorem: **PROVED**
- application to PDT if operational neutrality + extensionality are derived: **CONDITIONAL**
- recoverability/coarse-mass preservation implies invariance of every ledger: **FALSIFIED**
- quotient/data-processing mechanism: **IMPORTED/KNOWN**
- exact rational implementation audit: **NUMERICALLY SUPPORTED**
- PDT-native operational-neutrality proof: **OPEN**
- PDT-native quotient-extensional resource definition without imported composition: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
