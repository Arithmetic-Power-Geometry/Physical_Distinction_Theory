# Cycle 009 — Operational self-calibration dimension filter

**Status: CONDITIONAL theorem / PDT-native operational axiom candidate / metric-entropy and Lie-group mathematics IMPORTED-KNOWN / NOT A BREAKTHROUGH**

## Motivation

Cycle 007 showed that Generator Economy (GE), `dim G <= n`, plus genuinely noncommuting connected reversibility isolates `n=3` when the elementary distinction body is the Euclidean ball `B^n` and the full connected reversible isotropy group is `SO(n)`. The weakness was that GE was an unexplained dimension-counting assumption.

This cycle replaces GE by an explicitly resource/distinction statement.

## Operational Self-Calibration (OSC)

Let `X_n` be the elementary distinction state body and `G_n` its connected reversible control group. For resolution `epsilon`, let `N_X(epsilon)` be the number of distinguishable calibration states required to cover the state body and `N_G(epsilon)` the number of distinguishable controls required to cover the reversible group in a compatible operational metric.

**OSC hypothesis.** A physically elementary system can self-calibrate all of its connected reversible controls using its own distinction degrees of freedom without an asymptotically larger calibration alphabet:

`limsup_{epsilon -> 0} log N_G(epsilon) / log(1/epsilon) <= limsup_{epsilon -> 0} log N_X(epsilon) / log(1/epsilon)`.

This is not asserted as an established law. It is a candidate PDT-native physical principle whose experimental/operational justification remains open.

## Conditional theorem

Assume:

1. the elementary distinction body is a finite-dimensional Euclidean ball `B^n`;
2. its full connected reversible isotropy group is `SO(n)`;
3. OSC holds;
4. connected reversible dynamics is genuinely noncommuting.

Then `n=3`.

### Proof

For an `n`-dimensional Euclidean body, standard finite-dimensional metric entropy gives

`log N_X(epsilon) = n log(1/epsilon) + O(1)`.

For the compact Lie group `SO(n)` in any compatible smooth Riemannian/Finsler metric, the small-scale covering exponent is its manifold dimension,

`dim SO(n) = n(n-1)/2`,

so

`log N_G(epsilon) = [n(n-1)/2] log(1/epsilon) + O(1)`.

OSC therefore implies

`n(n-1)/2 <= n`.

For positive `n`, this gives `n <= 3`. But `SO(1)` is trivial and `SO(2)` is abelian. Genuine noncommuting connected reversibility therefore requires `n >= 3`. Hence `n=3`.

## Computational stress test

`pdt_self_calibration.py` audits the state and control entropy exponents. `tests/test_pdt_self_calibration.py` verifies the exact formula and scans `n=1..1000`; the OSC+noncommutativity intersection is exactly `{3}`. The manuscript-facing table `results/cycle009_operational_self_calibration.csv` records `n=1..12`.

## Prior-art boundary

The mathematical ingredients are known. Metric entropy/covering estimates for classical compact Lie groups are established (for example Szarek's work on metric entropy of homogeneous spaces and classical Lie groups). Separately, generalized Bloch-ball reconstruction literature already shows special roles for dimension three from bipartite composition, entanglement, interacting reversible dynamics and local tomography (Masanes et al.; Krumm and Mueller). Self-calibrating quantum tomography is also established as an estimation technique.

The exact OSC postulate above was not identified in the limited search performed in this cycle, but absence from this search is not evidence of historical novelty. In particular, OSC must not be advertised as a new law unless a substantially broader prior-art review and an independent physical derivation or experiment support it.

## Kill tests

1. If OSC is merely imposed because it algebraically yields `dim G <= n`, the argument is circular and fails the PDT-native requirement.
2. If a physically admissible elementary system requires a control calibration alphabet with larger small-scale exponent than its state distinction alphabet, OSC is falsified.
3. If the operational metric on controls is singular or quotient-degenerate so that its covering exponent is not `dim G`, the theorem's metric regularity assumption fails.
4. Replacing full isotropy `SO(n)` by a smaller nonabelian subgroup can evade the dimension conclusion; therefore full isotropy remains a substantive assumption.
5. Existing entanglement/interacting-dynamics Bloch-ball reconstructions cannot be relabeled as this PDT theorem.

## Research consequence

OSC is a better-motivated bridge from PDT's distinction-capacity language to Generator Economy, but it remains a **conditional axiom candidate**, not a validated fundamental principle. The next admissible step is to derive OSC from a deeper resource/composition principle or formulate a direct calibration experiment capable of falsifying its scaling claim.
