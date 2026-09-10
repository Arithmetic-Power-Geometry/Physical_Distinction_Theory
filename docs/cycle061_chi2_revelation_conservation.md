# Cycle 061 — Exact chi-square revelation conservation

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT resource-accounting theorem.**

This is not a historical-novelty or breakthrough claim. It completes a stronger form of PDT-II target (4) for the classical full-support binary-experiment sector.

## Hypotheses

Let `P,Q` be finite distributions with `Q_i>0`. Let `K:X->J` and `H:J->Y` be stochastic channels. Define the likelihood-ratio random variable `L=P/Q` under `Q` and Pearson chi-square distinction

`C(P,Q)=chi2(P||Q)=E_Q[(L-1)^2]`.

## Theorem 1: exact revelation loss

For `J~K(.|X)`, the accessible likelihood ratio is `L_J=E_Q[L|J]`. Hence

`C(P,Q)-C(PK,QK) = E_Q[(L-E[L|J])^2] = E_Q Var(L|J) >= 0`.

Thus the distinction removed by a resource restriction is exactly the unresolved conditional variance of the microscopic likelihood ratio, not merely bounded by it.

## Theorem 2: nested resource conservation

For the nested resource chain `X -> J -> Y`,

`Delta(X->Y) = Delta(X->J) + Delta(J->Y)`,

where each Delta is the corresponding chi-square revelation loss. Equivalently,

`chi2(P||Q) = chi2(PK||QK) + E_Q Var(L|J)`

and applying the identity again after `H` gives exact telescoping across any finite resource filtration.

## Proof

`L_J=E[L|J]` follows by Bayes algebra. Since `E_Q[L]=1`, chi-square is `Var_Q(L)`. The law of total variance gives

`Var(L)=Var(E[L|J])+E Var(L|J)`.

The first variance is exactly `chi2(PK||QK)`. Applying the same identity to `J -> Y` and subtracting yields the nested conservation law.

## Adversarial/edge checks

The executable audit used exact rational arithmetic for 200 random cases at every `n=1,...,12`, then 50 cases each at `n=16,24,32,48,64`, with randomized positive distributions and randomized nested stochastic channels. It also includes identity and complete-erasure edge cases. Observed failures: 0.

## Prior-art boundary

The mathematics is a direct specialization of conditional expectation, the law of total variance, f-divergence data processing, and chi-square divergence. These are established results. PDT may use the identity as an exact resource-accounting law, but must not present the underlying probability theorem as historically novel.

## PDT consequence

Within this sector, any proposed PDT resource law that predicts negative hidden distinction or violates additive revelation loss along a declared nested stochastic resource filtration is falsified. The result supplies an exact conservation ledger but does not create a same-input PDT-vs-QM deviation and does not solve native composition or native `n=3` selection.
