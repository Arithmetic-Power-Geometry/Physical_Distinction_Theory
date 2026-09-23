# Cycle 338 — Causality Selector Boundary

Date: 2026-09-23
Branch: `pdt-breakthrough-lab-24x7`

## Target attacked

Strongest unresolved PDT-II obligations: (1) PDT-native composition law; (2) non-circular PDT-native `n=3` derivation; (3) same-input PDT/QM probability gap.

## Candidate principle

**Operational Causality (C).** For each system there is a unique deterministic effect; equivalently, probabilities of present outcomes do not depend on choices of later tests.

Question: can C, interpreted as temporal consistency of distinctions, select a unique PDT composite, select `n=3`, or force a same-input deviation from ordinary complex quantum theory?

## Exact hypotheses

For each finite system size `n`, assume an operational probabilistic theory in which:

1. preparations and tests define normalized outcome probabilities;
2. every system has a unique deterministic/discarding effect;
3. sequential circuits obey no-signalling from future test choices to earlier outcome probabilities.

No state cone, effect cone, tensor product, Born rule, local tomography, purification axiom, or preferred dimension is assumed.

## Exact counterfamilies

### Classical family

For an `n`-level classical system, normalized states are probability vectors `p=(p_1,...,p_n)`. The deterministic effect is `u(p)=sum_i p_i=1`. It is unique among deterministic effects on the normalized simplex. Future stochastic processing preserves normalization and cannot alter probabilities already assigned to earlier outcomes. Thus C holds for every finite `n>=1`.

### Complex-quantum family

For an `n`-dimensional complex quantum system, normalized states satisfy `rho>=0` and `Tr rho=1`. The deterministic effect is `u(rho)=Tr rho=1`. Trace-preserving future channels preserve normalization and cannot change probabilities already assigned to prior outcomes. Thus C holds for every finite `n>=1`.

The classical and quantum families are operationally inequivalent (simplex versus density-matrix state space; different correlated composites) while satisfying the same causality principle. Therefore causality does not determine a unique composition law.

## Smallest decisive counterexample

`n=2` suffices. A classical bit and a complex qubit both satisfy operational causality, but their normalized state spaces and bipartite correlations are inequivalent. Hence

`Causality => unique physical composition`

is false.

Because both counterfamilies exist for every finite `n`,

`Causality => n=3`

is false. There is no singularity at `n=3`.

## Dimension stress: n=1..12 and beyond

For each `n=1,...,12`, the classical deterministic effect is the all-ones functional and the quantum deterministic effect is trace. Both constructions are exact. They extend algebraically to arbitrary finite `n`; randomized higher-dimensional search cannot overturn an exact all-finite-dimension counterfamily.

## Same-input QM discriminator

Ordinary complex quantum theory itself satisfies C. Therefore C alone cannot imply

`P_PDT(O | I,R) != P_QM(O | I,R)`

under identical microscopic input `I` and declared resource window `R`. Any PDT discriminator must add a PDT-native axiom that excludes the causal quantum model and independently fixes operational probabilities.

## Composite / dynamics / records stress

The falsification survives composites and dynamics: both classical stochastic channels and quantum CPTP channels admit causal sequential composition; discarding future outputs cannot signal to earlier records. Markovianity is not required for the logical counterexample: causality constrains operational ordering, not uniqueness of the memory model. Controlled-environment records likewise do not select `n=3` because both families can be enlarged by finite record systems while retaining a unique deterministic effect.

## Prior-art rejection

Operational causality is established prior art, not PDT-native novelty. Chiribella–D'Ariano–Perinotti formulate causality as independence of present outcome probabilities from later experimental choices and use it in operational reconstructions. Chiribella–Scandolo use Causality as an axiom ensuring well-defined marginals. Later operational work continues to distinguish causality/strong causality from other structural assumptions; it is not a unique composition selector.

Relevant prior art:

- G. Chiribella, G. M. D'Ariano, P. Perinotti, *Informational derivation of quantum theory*, Phys. Rev. A 84, 012311 (2011).
- G. Chiribella, C. M. Scandolo, *Operational axioms for diagonalizing states*, EPTCS 195, 96–115 (2015).
- D. Rolino, M. Erba, A. Tosini, P. Perinotti, *Minimal operational theories: classical theories with quantum features*, New J. Phys. 27, 023004 (2025).

## Surviving strengthened theorem

**Theorem (causality underdetermination boundary).** Operational causality/uniqueness of the deterministic effect, without an independently specified PDT-native correlated-composite rule, is insufficient to determine a unique finite-dimensional operational theory, a unique tensor/composition law, or a preferred finite dimension.

**Proof.** The classical and complex-quantum all-finite-dimension families above satisfy the hypotheses and causality but are operationally inequivalent. Two inequivalent models satisfying the same hypotheses refute uniqueness. Since each exists for every finite `n`, causality cannot select `n=3`. QED.

## Status ledger

| Claim | Status |
|---|---|
| Operational causality / unique deterministic effect | IMPORTED/KNOWN |
| Classical all-finite-`n` causal counterfamily | PROVED |
| Complex-quantum all-finite-`n` causal counterfamily | PROVED |
| Causality implies unique PDT composition | FALSIFIED |
| Causality implies `n=3` | FALSIFIED |
| Causality implies same-input PDT/QM probability gap | FALSIFIED as an inference |
| Causality-underdetermination boundary theorem | PROVED |
| PDT-native selector excluding both counterfamilies | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Consequence for next cycle

Do not use causal ordering or uniqueness of discarding alone as the missing PDT-II selector. A viable principle must constrain correlated distinctions beyond causal normalization and must exclude ordinary complex QM if it is to yield a same-input experimental discriminator.
