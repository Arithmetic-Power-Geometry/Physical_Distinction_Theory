# PDT-II Cycle 317 — Local tomography does not select the composite distinction law

## Target
Strongest unresolved PDT-II obligation: derive or falsify a PDT-native composition selector.

## Candidate principle attacked
Add **local tomography** to the already-tested composition requirements: the composite vector space is the algebraic tensor product `V_A ⊗ V_B`, so product linear functionals separate composite tensors. Combine this with product multiplicativity, factor symmetry, associativity/coherence, and contraction under local contractions.

## Exact hypotheses
Let `V_A = V_B = R^d` with Euclidean local norm. The composite carrier is exactly `R^d ⊗ R^d`, with no hidden coordinates. Product covectors `f ⊗ g` are admitted and separate tensors. A candidate composite distinction norm must (i) agree with the local product on simple tensors, (ii) be invariant under factor swap/orthogonal relabelling, and (iii) contract under local linear contractions.

## Result
**FALSIFIED:** these hypotheses do not uniquely determine the composite norm.

The injective and projective crossnorms live on the same locally tomographic carrier and satisfy the same simple-tensor rule

`||x ⊗ y|| = ||x||_2 ||y||_2`.

For the correlated witness `Z_d = sum_i e_i ⊗ e_i`, identified with the identity matrix `I_d`,

- injective norm = operator norm = `1`;
- projective norm = nuclear norm = `d`.

Thus local tomography fixes the vector-space dimension/coordinate accessibility but not the norm/cone/effect geometry that assigns quantitative distinction to correlated directions. The smallest separating case is `d=2`.

## Dimension stress
Exact singular-value formulas give `(epsilon, pi)=(1,d)` for every finite `d`. The accompanying artifact records `d=1..12`; `d=1` is degenerate (agreement), and every `d>=2` separates. The same formula proves arbitrary finite-dimensional persistence, so randomized higher-dimensional testing is unnecessary for this witness.

## Edge cases
- `d=1`: no separation; both norms equal 1.
- rank-one/simple tensors: no separation by construction.
- correlated rank >=2 tensors: separation can occur; `I_d` gives factor `d`.
- zero tensor: both norms vanish.

## Prior-art boundary
This is a no-go use of established mathematics, not a PDT novelty claim. Injective/projective crossnorms are standard. In GPTs, local tomography constrains the composite vector-space structure, while composite state/effect sets can still vary between minimal/maximal constructions. Janotta–Lal and subsequent GPT literature explicitly treat non-unique composite structures and restricted effects. Therefore the mechanism is **IMPORTED/KNOWN**; only its role as a PDT-II route closure is recorded here.

## Status ledger
- Local tomography + coherent product crossnorm axioms => unique composite distinction: **FALSIFIED**.
- Minimal witness at d=2: **PROVED**.
- Persistence for d=2..12: **PROVED**.
- Arbitrary finite-d extension for `Z_d=I_d`: **PROVED**.
- Crossnorm/GPT mechanism: **IMPORTED/KNOWN**.
- PDT-native selector for correlated composites: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input parameter-free PDT/QM deviation: **OPEN**.
- Experimentally distinctive PDT inequality: **OPEN**.
- Gravity/capacity law: **OPEN; not imported**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Consequence
Local tomography cannot be the missing PDT selector. Any surviving composition proposal must add independently motivated structure that constrains correlated directions (for example a native cone/effect rule, purification-like principle, spectral rule, or another operational axiom), and that added structure must itself survive prior-art and counterexample analysis rather than being chosen to recover a desired theory.
