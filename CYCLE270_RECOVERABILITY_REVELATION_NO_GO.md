# Cycle 270 — Recoverability/revelation equality is dimension-blind

## Target attacked
PDT-II target (4), with consequences for targets (2) and (3): can a law equating preserved distinction with recoverability/revelation select n=3 or create a PDT-vs-QM same-input deviation?

## Candidate principle
Let D be a distinguishability divergence and Phi an admissible coarse-graining. Define distinction loss

L_D(rho,sigma;Phi) = D(rho||sigma) - D(Phi(rho)||Phi(sigma)).

Candidate: zero distinction loss iff the relevant information is perfectly recoverable; perhaps this equality/revelation law is PDT-native and constrains physical dimension.

## Exact falsification of the dimension-selector claim
The candidate is dimension-blind even in the classical commuting sector. For every n >= 2 choose distributions p != q and let Phi be any permutation of n outcomes. Its inverse permutation R satisfies R Phi = id. KL divergence is exactly invariant under the relabelling, hence

D_KL(p||q) = D_KL(Phi p || Phi q),

so L_D=0 and exact recovery holds. This gives nontrivial witnesses in every n >= 2. n=2 is a counterdimension to uniqueness of n=3; n=4 defeats an inferred upper bound n<=3.

The same structural fact persists quantum mechanically: relative-entropy data processing is saturated exactly in the sufficient/recoverable case under the standard support hypotheses (Petz sufficiency/recovery). This is established quantum-information theory, not PDT novelty.

## Stronger surviving theorem
If a proposed PDT revelation/conservation axiom is satisfied whenever an admissible channel is reversible on the tested state family, and reversible embeddings/relabelings exist in arbitrarily large dimensions, then that axiom alone cannot impose a finite ambient-dimension ceiling. To select n=3 it must contain an additional ambient-sensitive restriction that fails for at least n=4.

## Same-input consequence
When PDT uses the same state pair, channel, recovery map, measurement/effect set and probability rule as QM inside the declared resource window, recoverability cannot itself generate P_PDT(O|I,R) != P_QM(O|I,R). A deviation requires a changed operational primitive or a resource admissibility rule that excludes/changes an operation used by QM; that change must be stated independently rather than inferred from the equality case.

## Prior-art boundary
Petz sufficiency/equality in relative-entropy data processing and later quantitative recoverability refinements are established. Relevant checks include Berta, Lemm & Wilde (2015), *Monotonicity of quantum relative entropy and recoverability*, and Jenčová (2024), *Recoverability of quantum channels via hypothesis testing*. Therefore the recovery equivalence itself is IMPORTED/KNOWN.

## Status
- KL invariance under reversible relabelling in every finite n: **PROVED**.
- Exact n=1..12 rational regression: **PROVED** by `tests/test_cycle270_recoverability_dimension_blind.py`.
- Recoverability/equality as a unique n=3 selector: **FALSIFIED**.
- Recoverability/equality as an n<=3 ceiling: **FALSIFIED**.
- Quantum Petz/sufficiency boundary: **IMPORTED/KNOWN**.
- PDT-native ambient-sensitive recovery restriction: **OPEN**.
- PDT-native composition law: **OPEN**.
- Same-input PDT/QM quantitative deviation with an explicitly changed primitive: **OPEN**.
- Breakthrough candidate: **NO**.

## Smallest decisive counterexamples
- n=2: nontrivial exact-recovery witness already satisfies the candidate.
- n=4: nontrivial exact-recovery witness survives above three.

No gravity/capacity claim is promoted in this cycle.