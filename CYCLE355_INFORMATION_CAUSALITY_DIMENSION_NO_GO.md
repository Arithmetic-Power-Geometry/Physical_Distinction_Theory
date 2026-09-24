# PDT-II Cycle 355 — Information-causality dimension no-go

## Target attacked

Strongest unresolved PDT-II obligations: a PDT-native composition selector and a non-circular derivation of `n = 3`.

## Candidate principle

**Information causality (IC).** In the standard random-access communication task, if Alice sends `m` classical bits, Bob's total information gain about Alice's initially unknown data is at most `m`, even when they share an allowed nonsignalling resource.

## Exact hypothesis audit

The candidate implication tested is

> IC + finite operational composition => distinguished local dimension `n = 3`.

This implication is false.

Finite-dimensional complex quantum theory satisfies information causality in arbitrary local Hilbert dimension. Therefore dimensions `n = 2,3,4,...` all survive the principle. The smallest nontrivial counterexample to dimension selection is `n = 2`; `n = 4` is the smallest higher-dimensional counterexample to uniqueness of `n = 3`.

The accompanying exact audit records `n = 1..12`. This is not a numerical approximation: the table records membership in an analytic all-finite-dimension counterfamily.

## Proof / falsification

Pawlowski et al. introduced IC and proved that quantum correlations respect it. Their statement is not restricted to qutrits or to local Hilbert dimension three. A finite-dimensional quantum system of arbitrary dimension is consequently an admissible local subsystem of quantum protocols respecting IC.

Hence, if IC implied `n = 3`, quantum systems of dimension 2 or 4 would violate IC. They do not. Contradiction.

So

`IC => n = 3`

is **FALSIFIED**.

This also blocks the inference

`IC => P_PDT(O|I,R) != P_QM(O|I,R)`

because ordinary QM is itself inside the IC-respecting class. A PDT/QM same-input deviation would need an additional PDT-native law that changes a state/effect/transformation/probability prediction under the same microscopic input and declared resource window.

## Composition significance

IC is stronger than a merely local axiom: it constrains correlations available to composites. Prior work by Patra et al. (2022) specifically studies IC as a constraint on quantum composition and argues that minimal and maximal tensor-product extremes are excluded in their setting. That makes IC relevant prior art for PDT-II composition, but not a PDT-native discovery and not a dimension-three selector.

A September 2026 preprint by Gachechiladze and Miklin further reports that generalized IC characterizes the quantum correlation set in the simplest bipartite binary-measurement Bell scenario. This strengthens the prior-art warning: Bell-correlation selection by IC cannot be promoted as PDT novelty, and correlation-set agreement in one scenario still does not constitute a derivation of local dimension three.

## Adversarial checks

- **Lower dimension:** `n=2` survives — decisive counterexample.
- **Target dimension:** `n=3` survives, but is not isolated.
- **Higher dimensions:** every `n=4..12` in the audit survives; analytically the counterfamily continues to every finite `n`.
- **Composite relevance:** IC constrains joint correlations, so this is not dismissed merely as a local-state axiom.
- **Same-input prediction:** no PDT/QM deviation follows because QM respects IC.
- **Prior-art collision:** IC is imported/known; its use to constrain composition is also prior art.

## Status ledger

| Claim | Status |
|---|---|
| Quantum theory respects information causality | IMPORTED/KNOWN |
| Quantum all-finite-dimension family defeats IC-based `n=3` selection | PROVED |
| `IC => n=3` | FALSIFIED |
| `IC => unique PDT composition` | OPEN / not established by IC alone |
| `IC => same-input PDT/QM deviation` | FALSIFIED as an inference |
| IC constraints on composition | IMPORTED/KNOWN |
| PDT-native joint selector beyond IC | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Prior art checked

1. M. Pawlowski et al., *Information Causality as a Physical Principle*, Nature 461, 1101–1104 (2009); arXiv:0905.2292.
2. R. K. Patra et al., *Principle of information causality rationalizes quantum composition*, arXiv:2208.13996 (2022).
3. M. Gachechiladze and N. Miklin, *Information Causality Characterizes the Set of Quantum Correlations in the Simplest Bell Scenario*, arXiv:2609.10508 (2026).

## Surviving PDT-II boundary

The composition search must now demand more than IC-respecting correlations. A viable PDT-native selector has to distinguish among IC-compatible theories/compositions and, if it is intended to explain `n=3`, contain a non-circular mechanism that excludes both `n=2` and every `n>=4`. No such mechanism is established in this cycle.
