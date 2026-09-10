# Cycle 052 — Sharp equality structure for product distinction

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT operational corollary.**

Not a breakthrough candidate.

## Statement

For finite probability distributions `p,q` on X and `r,s` on Y, let `d1=TV(p,q)`, `d2=TV(r,s)`, and `D=TV(p⊗r,q⊗s)`. Then

`D <= d1 + d2 - d1 d2`.

Moreover the exact slack is

`[d1+d2-d1 d2]-D = sum_{i,j}[min(p_i r_j,q_i s_j)-min(p_i,q_i)min(r_j,s_j)] >= 0`.

Hence saturation holds iff every cell term vanishes.

For strictly positive entries, write likelihood ratios `x_i=p_i/q_i`, `y_j=r_j/s_j`. If both pairs are nonidentical, normalization forces each likelihood-ratio family to contain values both above and below one. Choosing `x_i>1` and `y_j<1` gives

`min(x_i y_j,1) > min(x_i,1)min(y_j,1)=y_j`,

so at least one cell has strictly positive slack. Therefore:

**Strict-positivity theorem.** If `p,q,r,s` have full support and `p!=q`, `r!=s`, then

`TV(p⊗r,q⊗s) < d1+d2-d1 d2`.

Thus equality for two genuinely informative factors requires support/boundary degeneracy (or an identical factor).

## Exact witnesses

Strict full-support witness:

`p=(3/4,1/4)`, `q=(1/4,3/4)`, `r=(2/3,1/3)`, `s=(1/3,2/3)`.

Boundary saturation witness:

`p=r=(1,0)`, `q=s=(1/2,1/2)`.

Here `d1=d2=1/2` and `D=3/4=d1+d2-d1d2`.

## PDT-II consequence

The universal upper scalar law is generically not attained in the interior. Product distinction depends on likelihood/support geometry, not only on subsystem scalar values. Therefore a PDT-native exact composition law cannot be reconstructed from `(d_A,d_B)` alone without additional operational structure.

The underlying total-variation/product-measure mathematics is established probability theory and is not claimed as historical novelty.

## Validation

`tests/test_cycle052_product_distinction_equality.py` uses exact rational arithmetic and exhaustively checks the slack identity and nonnegativity on the complete binary probability grid with denominator 6, plus strict full-support, boundary-saturation, and identical-factor witnesses.
