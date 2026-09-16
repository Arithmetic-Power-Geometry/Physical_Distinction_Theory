# Cycle 190 — Sequential revelation increment bound

## Status

- **PROVED (conditional):** finite-dimensional linear observation protocol.
- **IMPORTED/KNOWN:** the proof is elementary rank/observability mathematics; no PDT novelty claim.
- **FALSIFIED:** any conjecture that one new scalar observation can reveal more than one new linear distinction at a single step.
- **OPEN:** whether PDT-native physical restrictions impose a stronger non-generic inequality, or yield a same-input PDT/QM prediction.
- **BREAKTHROUGH CANDIDATE:** NO.

## Hypotheses

Let the microscopic state space be a finite-dimensional vector space V of dimension n. Let a sequential protocol generate accumulated observable row spaces

W_t = span(W_{t-1} union rows(C_t Phi_t)),

where Phi_t is the known state-transition/intervention product up to step t and C_t has output rank at most r_t. Define the resource-relative revealed distinction dimension D_t = dim W_t (equivalently the quotient dimension by the common kernel of accumulated effects).

No commutativity, Markovian stationarity, norm, orthogonality, or unitarity assumption is required for the rank statement; only linear finite-dimensional evaluation is used.

## Theorem — bounded revelation increment

For every step t,

0 <= D_t - D_{t-1} <= r_t.

Hence

D_T <= min(n, D_0 + sum_{t=1}^T r_t).

For scalar observations r_t=1,

D_T <= min(n, D_0+T),

and every one-step revelation increment is exactly 0 or 1.

### Proof

W_{t-1} is a subspace of W_t, so D_t >= D_{t-1}. Adding the row space of C_t Phi_t can increase dimension by at most rank(C_t Phi_t), which is at most rank(C_t) <= r_t. Summing the inequalities telescopes, and D_T <= n because W_T is a subspace of V*. QED.

## Sharpness

For V=F^n, take successive scalar effects e_1,...,e_n in a dual basis (or obtain them from one scalar effect under suitable reversible coordinate permutations). Starting from D_0=0, each new independent row raises D by exactly one until saturation at n. Thus the scalar upper bound is sharp in every finite dimension.

## Dimension stress boundary

The proof is dimension-independent and therefore covers n=1 through n=12 exactly and every finite n analytically. Degenerate zero effects give increment 0; repeated/redundant effects give increment 0; independent effects attain the upper bound. Invertible reversible transformations preserve row rank but can change whether a transported row is independent of the accumulated span, consistent with Cycle 188 order dependence and Cycle 189's two-intervention defect theorem.

## Consequence for PDT-II

This closes a tempting but false route to an anomalously large single-step 'revelation burst' in the present linear quotient model. Any experimentally distinctive PDT inequality must therefore arise from additional physical structure (cost, admissibility, nonlinear/nonclassical effect geometry, environment constraints, composition closure, etc.), not from finite-dimensional rank accumulation alone.

The theorem does **not** derive probability, Born weights, an n=3 law, a PDT/QM discrepancy, thermodynamic conservation, or gravity/capacity.

## Prior-art boundary

The accumulated-row-space construction is the standard mathematical core of linear observability: observability is tested by the rank of stacked transported/output rows. Therefore the bounded-increment theorem is elementary linear algebra/control theory and is classified IMPORTED/KNOWN rather than PDT-native novelty.
