# Cycle 052 — Sharp equality structure for product distinction

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT operational corollary.**

Not a breakthrough candidate.

## Statement

For finite probability distributions `p,q` on X and `r,s` on Y, let

- `d1 = TV(p,q)`,
- `d2 = TV(r,s)`,
- `D = TV(p⊗r,q⊗s)`.

The standard product bound is

`D <= d1 + d2 - d1 d2`.

Writing overlap `O(p,q)=sum_i min(p_i,q_i)=1-TV(p,q)`, the proof follows from

`min(p_i r_j, q_i s_j) >= min(p_i,q_i) min(r_j,s_j)`.

Summing yields `O(p⊗r,q⊗s) >= O(p,q)O(r,s)`.

The new PDT-II audit records the exact nonnegative slack decomposition

`[d1+d2-d1 d2]-D`

`= sum_{i,j} { min(p_i r_j,q_i s_j) - min(p_i,q_i)min(r_j,s_j) }`.

Hence the product upper bound is saturated **iff every cell term is zero**. This is the exact finite-alphabet equality criterion and is safer than imposing a global scalar composition law.

For strictly positive entries, in likelihood-ratio variables `x_i=p_i/q_i` and `y_j=r_j/s_j`, a cell has zero slack exactly when

`min(x_i y_j,1)=min(x_i,1)min(y_j,1)`.

Thus strict slack occurs whenever independently composed records carry genuinely opposing likelihood evidence in a cell: one likelihood ratio lies above one and the other below one, away from degenerate boundary cases. Aligned evidence can saturate the upper bound.

## Exact witnesses

Aligned binary witness:

`p=r=(3/4,1/4)`, `q=s=(1/4,3/4)`.

This saturates the bound.

Cross-evidence witness:

`p=s=(3/4,1/4)`, `q=r=(1/4,3/4)`.

This gives strict inequality. Therefore the scalar pair `(d1,d2)` alone cannot determine `D`; the sign/likelihood geometry of the evidence matters.

## PDT-II consequence

A PDT-native composition law based only on subsystem scalar distinction values is underdetermined. Any exact composition principle must retain additional operational structure sufficient to encode evidence alignment/cancellation, rather than assigning `D_AB=F(d_A,d_B)` universally.

This is a decisive obstruction to scalar-only composition reconstruction, but the underlying total-variation/product-measure mathematics is established probability theory and is not claimed as historically novel.

## Validation

`tests/test_cycle052_product_distinction_equality.py` exhaustively checks a rational binary grid with denominator 6 and verifies:

- exact equality of analytic and decomposed slack,
- nonnegativity in every tested case,
- strict cross-evidence witness,
- saturating aligned-evidence witness,
- degenerate identical-factor case.

All checks use exact `fractions.Fraction` arithmetic.
