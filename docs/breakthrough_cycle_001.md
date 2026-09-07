# PDT Breakthrough Lab — Cycle 001

## Outcome

No breakthrough is claimed in this cycle. The cycle produced one useful boundary result and one research-direction constraint.

### Result A — operational dimension identifiability from fine-resolution capacity scaling

For the Euclidean unit ball `B_2^n`, let `M_epsilon` be the maximum cardinality of an epsilon-separated codebook. Standard packing/covering volume bounds give

`epsilon^{-n} <= M_epsilon <= (1 + 2/epsilon)^n`.

Therefore, with `K_epsilon = log2 M_epsilon`,

`n <= K_epsilon / log2(1/epsilon) <= n * log2(1 + 2/epsilon) / log2(1/epsilon)`.

As `epsilon -> 0`, the upper and lower bounds converge to `n`. Hence the fine-resolution distinction-capacity slope identifies Euclidean dimension under the explicit Euclidean/codebook assumptions.

**Status:** CONDITIONAL / IMPORTED-KNOWN MATHEMATICS OPERATIONALIZATION.

**Novelty boundary:** this is standard metric-entropy/packing-covering asymptotics expressed in PDT language. It is not claimed as new mathematics.

**Consequence:** PDT can operationally estimate `n` from sufficiently fine resolution once Euclidean geometry is already assumed, but this does not select `n=3`.

### Result B — local axioms remain dimension-blind

The existing constructive audit confirms that CEU, CER and RDE are compatible with Euclidean balls `B^n` for all tested `n>=2`, matching the analytical no-go argument. Therefore another purely local rotational/symmetry axiom cannot by itself solve the dimension-selection problem unless it is explicitly dimension-sensitive.

**Status:** PROVED / NO-GO at the stated local-axiom level.

## Numerical audit

Machine-readable output is stored in `results/cycle001_operational_dimension_audit.csv`.

Examples:

- `n=3, epsilon=0.1`: slope interval `[3.000000, 3.966658]`.
- `n=3, epsilon=0.01`: slope interval `[3.000000, 3.454794]`.
- `n=3, epsilon=1e-8`: slope interval `[3.000000, 3.112886]`.

The tightening is consistent with the asymptotic squeeze theorem. It does not constitute empirical evidence for physical three-dimensionality.

## Prior-art audit

The dimension-selection frontier strongly overlaps established reconstruction work and must not be presented as new without a genuinely different theorem:

1. L. Masanes and M. P. Mueller, *A derivation of quantum theory from physical requirements*, arXiv:1004.1483. This work derives quantum structure from operational postulates and explicitly includes a group-theoretic explanation of the Bloch ball and its three-dimensionality. https://arxiv.org/abs/1004.1483
2. L. Masanes, M. P. Mueller, R. Augusiak and D. Perez-Garcia, *Existence of an information unit as a postulate of quantum theory*, arXiv:1208.0493. The derivation uses information-unit structure together with continuity/reversibility and local characterization of composites. https://arxiv.org/abs/1208.0493
3. M.-O. Renou et al., *Quantum theory based on real numbers can be experimentally falsified*, Nature 600, 625–629 (2021), DOI 10.1038/s41586-021-04160-4. This is a key warning that compositional/network structure can distinguish theories that single-system experiments cannot. https://doi.org/10.1038/s41586-021-04160-4

## Breakthrough search narrowed for the next cycles

The highest-value unresolved route is now more specific:

> Find a PDT-native, physically motivated composite/interventional principle `P_D` such that the family of locally admissible Euclidean balls is reduced nontrivially, ideally to `n=3`, without merely restating local tomography, continuous reversible interaction, complex Hilbert-space composition, or another known reconstruction axiom.

Every candidate must be attacked by counterexamples in `B^2`, `B^4`, higher-dimensional spin factors, real/complex/quaternionic quantum models where applicable, and minimal/maximal GPT composites before any theorem claim is promoted.

The second route remains a same-input experiment: specify an observable for which a new PDT law gives a quantitative prediction different from standard quantum mechanics under identical microscopic inputs. No such validated deviation is established in this cycle.
