# Cycle 134 — Exact refinement conservation does not imply resolved-channel additivity

## Status

- Candidate bridge `exact orthogonal refinement conservation + reversible covariance + calibration => resolved-channel additivity`: **FALSIFIED**.
- Counterfamily: **PROVED**.
- Numerical stress audit: **NUMERICALLY SUPPORTED**.
- Orthogonal/Frobenius ingredients: **IMPORTED/KNOWN**.
- PDT-native extensivity/additivity bridge: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Candidate bridge under test

Cycle 133 reduced quadratic composite accounting to one unresolved assumption: additive accounting across mutually resolved product channels. The strongest obvious PDT-native route was to derive that assumption from exact refinement/revelation conservation.

The present cycle shows that route is not valid without an additional extensivity principle.

## Counterfamily

Let

`S(A) = sum_ij a_ij^2 = ||A||_F^2`

and, for any `alpha > 0`, define

`R_alpha(A) = S(A)^alpha`.

Every member of this family has all of the following properties.

1. **Nonnegativity and null calibration:** `R_alpha(A) >= 0` and `R_alpha(0)=0`.
2. **Unit product-channel calibration:** `R_alpha(E_ij)=1`.
3. **Continuous local reversible covariance:** for `U,V in SO(n)`, `R_alpha(U A V^T)=R_alpha(A)`.
4. **Exact orthogonal refinement/re-basing conservation:** any refinement that only redistributes a channel into orthogonal components while preserving the quadratic ledger `S` leaves `R_alpha` exactly unchanged.
5. **Same resource ordering:** because `x -> x^alpha` is strictly increasing on `R_+`, every `R_alpha` induces exactly the same state ordering as `S`.

Nevertheless, for `alpha != 1`, `R_alpha` is not additive across resolved orthogonal channels.

## Smallest decisive witness

Take `n=2`, `A=E_11`, `B=E_22`. They are orthogonal resolved product channels and

`R_alpha(A)=R_alpha(B)=1`.

But

`R_alpha(A+B)=2^alpha`,

whereas resolved-channel additivity would require

`R_alpha(A+B)=R_alpha(A)+R_alpha(B)=2`.

Thus:

- `alpha=1/2`: `sqrt(2) != 2`,
- `alpha=2`: `4 != 2`,
- `alpha=3`: `8 != 2`.

Only `alpha=1` is additive.

Therefore

`exact refinement conservation + SO(n)xSO(n) covariance + unit calibration + identical resource ordering`

**does not imply**

`resolved-channel additivity`.

This is an exact algebraic falsification, not a numerical conjecture.

## What survives

Cycle 133 remains valid *conditional on* resolved-channel additivity. But that additivity cannot be obtained merely by saying that refinement conserves the resource, even if conservation is exact and even if all resource orderings and reversible symmetries agree.

The missing hypothesis must control **scale/extensivity**, not merely conservation or ordering. A viable strengthened bridge must operationally justify something equivalent to finite additivity for independently resolved sectors, e.g.

`R(A direct-sum B) = R(A)+R(B)`

for genuinely independent resolved sectors, or another experimentally grounded rule that fixes the numerical resource scale rather than only its ordering.

This distinction matters because monotone reparameterizations are a standard ambiguity for resource measures: order/monotonicity alone does not fix an extensive numerical scale. No novelty is claimed for that general mathematical fact.

## Stress audit

The deterministic audit used dimensions

`n=1..12,16,24,32,48,64,96,128`

with `alpha in {1/2,1,2,3}` and 20 seeded random `SO(n)xSO(n)` transformations per dimension.

Results:

- covariance cases: `1520`,
- covariance failures above `1e-10`: `0`,
- maximum relative covariance residual: `2.632851477831755e-15`,
- exact nonadditive smallest witnesses: `3` (`alpha=1/2,2,3`).

The numerical sweep is regression evidence only; the falsification is exact.

## Consequence for PDT-II

The strongest surviving resource-law obligation is now:

`PDT primitives ?=> numerical extensivity across genuinely independent resolved composite sectors`.

If that bridge is derived, Cycle 133 can force the quadratic/Frobenius law. If it is not derivable, the resource scale remains reparameterization-ambiguous and no unique same-input quantitative deviation from QM can be claimed from the present resource ledger alone.
