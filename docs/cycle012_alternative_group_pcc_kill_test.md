# Cycle 012 — Alternative reversible-group kill test for PCC

**Status: DECISIVE FALSIFICATION of an over-broad PCC claim / explicit higher-dimensional counterexamples / NOT A BREAKTHROUGH**

## Question

Does Pairwise Calibration Closure (PCC) plus genuinely noncommuting connected reversibility select `n=3` without assuming the full connected isotropy group `SO(n)`?

## Result

No. The full-isotropy assumption is essential.

Consider the natural action of `SU(m)` on `C^m`, viewed as a real Euclidean action on `R^(2m)`. This is a connected compact nonabelian subgroup of `SO(2m)` for `m>=2`.

If `r` complex-linearly independent reference vectors are fixed pointwise, the remaining connected pointwise stabilizer is `SU(m-r)`. Therefore the minimal number of independent reference vectors required to identify a generic `SU(m)` control is

`b_SU(m) = m-1`.

Hence two references suffice for `m<=3`.

This gives two explicit higher-dimensional counterexamples to the over-broad claim:

- `SU(2)` acting on `R^4`: noncommuting and pairwise-calibratable (indeed one generic complex reference vector is enough);
- `SU(3)` acting on `R^6`: noncommuting and exactly pairwise-calibratable.

Thus

`PCC + noncommuting connected reversibility`

alone does **not** imply `n=3`.

## Proof of the SU(m) reference count

Let `x_1,...,x_r` be complex-linearly independent reference vectors. Any `U in SU(m)` fixing them pointwise fixes their complex span. On its orthogonal complement of complex dimension `m-r`, the remaining freedom is `SU(m-r)`. This stabilizer is nontrivial whenever `m-r>=2`. If `r=m-1`, the orthogonal complement is one-dimensional; determinant one forces the remaining phase to be one, so the stabilizer is trivial. Therefore the minimal base size is `m-1`.

## Computational audit

`pdt_pairwise_group_counterexamples.py` scans the natural `SU(m)` family. `tests/test_pdt_pairwise_group_counterexamples.py` verifies the exact reference-count formula and checks that the real dimensions `n=4` and `n=6` are higher-dimensional PCC+noncommuting counterexamples. Results are stored in `results/cycle012_alternative_group_pcc_counterexamples.csv`.

## Prior-art boundary

This is standard compact-group representation / base-size reasoning, not new mathematics. Base-size theory is established group-action theory; minimal-probe questions also appear in quantum process characterization. The PDT value here is negative: the result prevents Pairwise Calibration Closure from being advertised as a dimension-selection principle unless the reversible-group assumption is stated explicitly.

## Research consequence

Cycle 011 remains correct **only** in the full-isotropy Euclidean family `G=SO(n)`. Any attempt to promote PCC as a standalone PDT derivation of spatial/Bloch dimension three is falsified by `SU(2)` on `R^4` and `SU(3)` on `R^6`.

The viable dimension-selection target must therefore derive, rather than assume, a sufficiently strong isotropy/completeness condition on the elementary reversible group, or replace PCC by a deeper composition/resource principle that excludes these higher-dimensional subgroup counterexamples for an operational reason.
