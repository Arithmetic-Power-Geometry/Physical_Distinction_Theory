# Cycle 277 — Resource-refinement revelation law

Status: **PROVED (elementary operational theorem); NOT a breakthrough candidate**

## Setup
Let `T_R` be the family of binary tests admissible under resource window `R`. For a traceless state difference `X`, define

`Delta_R(X) = sup_{E in T_R} |Tr(E X)|`,

and the operational null space

`N_R = {X : Delta_R(X)=0}`.

Write `R <= R'` when every test admissible under `R` remains admissible under `R'`, i.e. `T_R subseteq T_R'`.

## Theorem 277.1 — refinement monotonicity and null-space antitonicity
If `R <= R'`, then for every admissible state difference `X`,

`Delta_R(X) <= Delta_R'(X)`

and

`N_R' subseteq N_R`.

### Proof
The first claim follows immediately because the supremum defining `Delta_R'` is taken over a superset of the tests defining `Delta_R`. If `X in N_R'`, then `Delta_R'(X)=0`; monotonicity and nonnegativity imply `0 <= Delta_R(X) <= 0`, hence `X in N_R`. QED.

## Corollary 277.2 — exact revelation criterion
A refinement `R <= R'` reveals a previously invisible distinction exactly when

`X in N_R \ N_R'`.

Equivalently, `Delta_R(X)=0` but `Delta_R'(X)>0`.

## Corollary 277.3 — quotient direction
Refinement induces a canonical surjection

`V/N_R' -> V/N_R`, `[X]_{R'} -> [X]_R`,

because `N_R' subseteq N_R`. Thus the refined operational quotient contains at least as much resolved directional information as the coarse quotient. The reverse canonical map generally does not exist.

## Degenerate and dimension checks
- If `T_R=T_R'`, equality holds throughout.
- If `T_R` contains only a null/constant test, every traceless `X` is invisible.
- If `T_R'` is tomographically complete, `N_R'={0}` on the traceless state-difference space.
- The proof is dimension-independent and therefore holds for `n=1,...,12` and all finite dimensions; no numerical approximation is needed.
- The result does **not** select `n=3`.
- The result does **not** select a composite tensor product.
- The result does **not** imply a PDT-vs-QM same-input deviation.

## Adversarial check: strict revelation does not imply a universal quantitative increment
Take a classical bit and a coarse resource family containing only the constant effect. Then all probability differences are null. Add the effect `E=(1,0)`. For `p=(1/2+a,1/2-a)` and `q=(1/2-a,1/2+a)`, the newly accessible distinction is `2|a|`, which can take a continuum of values. Therefore resource refinement alone gives order/monotonicity but no universal nonzero revelation quantum or dimension selector.

## Prior-art boundary
The monotonicity proof is generic supremum/order logic and closely parallels measurement-restricted distinguishability, statistical experiment refinement, and resource-theory monotonicity. It must not be advertised as new mathematics merely because it is written in PDT notation. PDT-specific value is bookkeeping: resource windows generate a filtration of operational null spaces/quotients and make exact revelation events explicit.

## Classification
- `R <= R' => Delta_R <= Delta_R'`: **PROVED**
- `N_R' subseteq N_R`: **PROVED**
- exact revelation criterion `N_R \ N_R'`: **PROVED**
- canonical quotient surjection under refinement: **PROVED**
- universal positive revelation increment: **FALSIFIED**
- refinement law implies `n=3`: **FALSIFIED**
- refinement law fixes composition: **FALSIFIED**
- PDT-native composition selector: **OPEN**
- same-input `P_PDT != P_QM`: **OPEN**
- breakthrough candidate: **NO**
