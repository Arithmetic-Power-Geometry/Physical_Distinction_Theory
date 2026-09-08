# Cycle 016 — Multi-branch Gram compatibility no-go

## Result

For three or more pure conditional environment records, pairwise revelation/coherence constraints are not independently assignable.

Let the conditional record states be normalized vectors `|e_i>` and let the controlled-system coherence multipliers be

`g_ij = <e_i|e_j>`.

The matrix `G=(g_ij)` is a Gram matrix, hence Hermitian positive semidefinite with unit diagonal. For any three branches this gives the exact principal-minor inequality

`1 - |g12|^2 - |g23|^2 - |g31|^2 + 2 Re(g12 g23 g31) >= 0`.

Writing `|g12|=a`, `|g23|=b`, `|g31|=c` and the gauge-invariant loop phase `Phi=arg(g12 g23 g31)`,

`1 - a^2 - b^2 - c^2 + 2abc cos(Phi) >= 0`.

This is a genuinely joint compatibility condition: it is invisible to three separate two-branch checks.

## Decisive counterexample to independent pairwise budgeting

Take equal pairwise magnitudes `a=b=c=r` and loop phase `Phi=pi`. Every individual pair is admissible whenever `0<=r<=1`, but global realizability requires

`1 - 3r^2 - 2r^3 >= 0`.

On `[0,1]` the threshold is exactly `r<=1/2`. Thus, for example, the assignment

`g12=0.9, g23=0.9, g31=-0.9`

passes every pairwise magnitude constraint `|g_ij|<=1` yet has determinant

`1 - 3(0.9)^2 - 2(0.9)^3 = -2.888 < 0`,

so no set of physical record vectors can realize it.

Therefore:

**Pairwise-valid controlled-record revelation/coherence budgets do not imply globally compatible multi-branch records.**

Any PDT composition or resource-change law that independently specifies each pairwise coherence factor must also satisfy positive-semidefinite Gram compatibility for every finite branch set.

## General finite-branch statement

For `k` pure conditional record branches, the complete compatibility condition is

`G >= 0`, `G_ii=1`.

Equivalently, all principal minors are nonnegative. Three-branch determinants are only the first phase-sensitive constraints; larger branch sets add higher-order constraints. This supplies a scalable PDT composite-system kill test.

## Status

**PROVED / IMPORTED-KNOWN Gram-matrix mathematics / DECISIVE FALSIFICATION of independent pairwise composition.**

This is not promoted as a PDT breakthrough. Positive-semidefinite Gram compatibility and multipath coherence/duality are established mathematics and physics. The PDT contribution in this cycle is to make the global compatibility obstruction explicit in the repository's controlled-record variables and to use it as a falsification criterion for candidate composition/resource laws.

## Computational audit

`pdt_multibranch_gram_compatibility.py` implements the three-branch determinant, compatibility test, adversarial phase-frustrated assignment, and fixed-seed random audits.

`tests/test_pdt_multibranch_gram_compatibility.py` checks:

- actual random record Gram matrices across dimensions `1..12` never violate PSD beyond numerical tolerance;
- the analytic determinant equals direct numerical determinant;
- a pairwise-valid `r=0.9`, `Phi=pi` assignment is globally impossible;
- the equal-visibility `Phi=pi` threshold is `r=1/2`.

`results/cycle016_multibranch_gram_compatibility.csv` stores 300 fixed-seed trials per dimension for `d=1..12`. Small negative determinants in dimensions 1 and 2 are floating-point roundoff below `5e-16`, with zero violations below `-1e-12`.

## Prior-art boundary

Relevant established landscape includes:

- M. N. Bera, T. Qureshi, M. A. Siddiqui, and A. K. Pati, “Duality of quantum coherence and path distinguishability,” Phys. Rev. A 92, 012118 (2015), DOI: 10.1103/PhysRevA.92.012118.
- T. Qureshi, “Interference visibility and wave-particle duality in multipath interference,” Phys. Rev. A 100, 042105 (2019), DOI: 10.1103/PhysRevA.100.042105.
- Standard Gram-matrix positivity: every Gram matrix is positive semidefinite, and every positive-semidefinite unit-diagonal matrix is realizable as a Gram matrix of normalized vectors.

No claim of historical novelty is made for these ingredients.
