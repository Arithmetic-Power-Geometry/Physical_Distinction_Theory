# Cycle 049 — Exact revelation accounting under deterministic resource coarse-graining

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT operational corollary.**

This is not a BREAKTHROUGH CANDIDATE. The underlying mathematics is the standard total-variation/Jordan-decomposition structure of a signed measure. The PDT contribution here is the explicit resource-accounting interpretation and a sharp equality test for whether a coarse resource window has hidden any operational distinction.

## Hypotheses

Let `p=(p_i)` and `q=(q_i)` be two probability distributions on a finite fine outcome set. Let a deterministic resource map partition fine outcomes into coarse cells `C_j`. Write

`delta_i = p_i - q_i`.

Define the fine and coarse operational distinctions by total variation,

`D_fine = (1/2) sum_i |delta_i|`,

`D_coarse = (1/2) sum_j |sum_{i in C_j} delta_i|`.

For each coarse cell define

`P_j = sum_{i in C_j, delta_i>0} delta_i`,

`N_j = sum_{i in C_j, delta_i<0} (-delta_i)`.

## Theorem: exact revelation accounting

For every deterministic coarse-graining partition,

`D_fine - D_coarse = sum_j min(P_j,N_j)`.

Equivalently,

`D_fine - D_coarse = (1/2) sum_j [sum_{i in C_j}|delta_i| - |sum_{i in C_j}delta_i|]`.

### Proof

Inside a fixed cell `C_j`,

`sum_{i in C_j}|delta_i| = P_j + N_j`,

while

`|sum_{i in C_j}delta_i| = |P_j-N_j|`.

Hence the cell contribution to `D_fine-D_coarse` is

`(1/2)[P_j+N_j-|P_j-N_j|] = min(P_j,N_j)`.

Summing over cells proves the identity.

## Sharp equality condition

`D_coarse = D_fine` if and only if every coarse cell is sign-pure with respect to `delta`: after zero entries are ignored, no cell contains both positive and negative values of `p_i-q_i`.

Thus a resource coarse-graining loses no operational distinction exactly when it never merges outcomes that favor opposite hypotheses.

## PDT interpretation

The quantity

`R_hidden = D_fine-D_coarse`

is not an arbitrary residual introduced to force conservation. It has an explicit microscopic decomposition:

`R_hidden = sum_j min(P_j,N_j)`.

It measures contrast cancellation caused specifically by the resource map. Therefore along a deterministic refinement chain, the distinction newly revealed by splitting cells is exactly the cancellation removed by those splits.

This gives a defensible accounting law:

`accessible distinction + unresolved cancellation = fine distinction`,

provided the fine reference partition is explicitly declared. It does **not** assert that total distinction is a new conserved physical substance, and it does not extend automatically to arbitrary stochastic kernels without additional bookkeeping.

## Smallest decisive witness

Take

`p=(1,0)`, `q=(0,1)`

and merge both fine outcomes into one coarse cell. Then

`D_fine=1`, `D_coarse=0`, `P_1=N_1=1`,

so

`D_fine-D_coarse=1=min(P_1,N_1)`.

This is the smallest full-hiding example.

## Stress tests

The implementation uses exact rational arithmetic. For each `n=1,...,12`, 200 deterministic pseudo-random rational pairs and pseudo-random partitions were tested. The maximum identity error was exactly zero in every dimension, and the sign-purity iff equality test had zero failures.

The generated audit is in `results/cycle049_exact_revelation_accounting.csv`.

## Prior-art boundary

Total variation is the variation norm of the signed measure `p-q`; contraction under measurable/coarse maps and its relation to Hahn/Jordan decomposition are standard. Therefore no novelty claim is made for the identity as abstract measure theory. Any future PDT novelty claim must come from a new physical principle that fixes the operational resource map or yields a new experimentally falsifiable consequence from this accounting law.
