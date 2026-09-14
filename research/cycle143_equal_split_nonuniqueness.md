# PDT-II Cycle 143 — Equal-split conservation does not determine a composition law

## Status

- **PROVED:** the Cycle-142 binary/ternary equal-split laws select the radial exponent 2 under continuity, but do not determine how unequal resolved components compose.
- **FALSIFIED:** `2-way + 3-way equal-split conservation + continuity + symmetry` is insufficient to imply the full quadratic/Frobenius composition law.
- **OPEN:** a PDT-native principle relating unequal resolved components is still required.
- **BREAKTHROUGH CANDIDATE:** NO.

## Counterfamily

For a finite nonnegative resolved resource vector `x=(x_1,...,x_m)`, define

\[
R_\varepsilon(x)=\sum_i x_i^2+\varepsilon\,V(x),
\]

where

\[
V(x)=\sum_i x_i^4-\frac{(\sum_i x_i^2)^2}{m},\qquad m\ge2,
\]

and set `V(x)=0` for `m=1`.

By Cauchy-Schwarz, `V(x)>=0`. It is permutation invariant and vanishes exactly when all component squares are equal. Therefore every equal-amplitude refinement of a scalar resource `r` into `k` resolved channels `r/sqrt(k)` has

\[
R_\varepsilon(r/\sqrt{k},\ldots,r/\sqrt{k})=r^2
\]

for **every** `k>=1`, not merely k=2 and 3.

Nevertheless unequal compositions differ from the quadratic ledger. For the exact witness `x=(1,2)` and `epsilon=1`,

\[
R_0(1,2)=5,
\]

while

\[
V(1,2)=1+16-25/2=9/2,
\]

so

\[
R_1(1,2)=19/2.
\]

Thus even conservation under *all equal-amplitude split multiplicities* does not fix the resource of an unequal resolved composition.

## Consequence

Cycle 142 correctly fixes the radial degree once its hypotheses are granted, but it does not by itself establish a PDT-native composition law. The surviving bridge must constrain **unequal** resolved components—for example a separately justified refinement consistency, pairwise orthogonal additivity, or another operational law that cannot be reduced to equal splitting.

No quantum, gravity, or experimental deviation is inferred from this result.
