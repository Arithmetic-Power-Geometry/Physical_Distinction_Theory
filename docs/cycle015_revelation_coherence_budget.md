# Cycle 015 — Controlled-record revelation/coherence budget

## Result

Consider the standard controlled-environment sector with initial environment state `eta` and a relative unitary `V`. The two conditional environment outputs are

`rho_0 = eta`,

`rho_1 = V eta V^dagger`,

and the system coherence multiplier is

`chi = Tr(eta V)`.

Define the record distinguishability

`D = (1/2) ||rho_0-rho_1||_1`.

Then

`D^2 + |chi|^2 <= 1`.

For pure `eta`, equality holds.

## Proof

Let

`f = ||sqrt(eta) V sqrt(eta)||_1`.

This is the root fidelity between `eta` and `V eta V^dagger`. First,

`|chi| = |Tr(sqrt(eta) V sqrt(eta))| <= ||sqrt(eta) V sqrt(eta)||_1 = f`

by `|Tr A| <= ||A||_1`.

Second, the Fuchs–van de Graaf upper bound gives

`D <= sqrt(1-f^2)`.

Hence

`D^2 + |chi|^2 <= D^2 + f^2 <= 1`.

When `eta` is pure, both inequalities are equalities, recovering the usual pure-record complementarity circle.

## PDT interpretation

Within this controlled sector, environmental revelation and residual system coherence share a strict unit budget. A mixed record can move the operating point into the interior of the disk, but it cannot cross the boundary.

This is useful as a **kill test** for proposed PDT resource-change laws: any candidate that leaves the microscopic controlled-unitary model unchanged yet predicts `D^2+|chi|^2>1` is inconsistent with the standard model rather than a bookkeeping refinement.

It does **not** by itself produce a same-input PDT-vs-QM deviation.

## Status

**PROVED / IMPORTED-KNOWN mathematics / PDT operational corollary.**

No historical novelty is claimed. The result sits in the established wave-particle duality and trace-distance/fidelity literature; in particular Englert's two-way distinguishability/visibility inequality and the Fuchs–van de Graaf bounds already supply the mathematical landscape. The contribution of this cycle is to make the constraint explicit in the repository's controlled-record variables and wire it into automated PDT falsification tests.

## Computational audit

`pdt_revelation_coherence_budget.py` implements the quantities directly. `tests/test_pdt_revelation_coherence_budget.py` tests random density matrices and unitaries in dimensions 1–12 and additional cases through dimension 19, plus exact pure-state saturation. `results/cycle015_revelation_coherence_budget.csv` records a fixed-seed 200-trial-per-dimension audit for dimensions 1–12.

Floating-point overshoots in the CSV are at machine precision (~1e-15), not physical violations.

## Prior-art boundary

- B.-G. Englert, *Fringe Visibility and Which-Way Information: An Inequality*, Phys. Rev. Lett. 77, 2154 (1996).
- C. A. Fuchs and J. van de Graaf, *Cryptographic distinguishability measures for quantum-mechanical states*, IEEE Trans. Inf. Theory 45, 1216–1227 (1999).

This result must therefore not be promoted as a PDT breakthrough or as historically new quantum mathematics.
