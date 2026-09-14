# Cycle 132 — Local-marginal composite no-go

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED + OPEN**

**BREAKTHROUGH CANDIDATE: NO.**

## Target attacked

PDT-II target (4): derive a composite resource/refinement/revelation law from PDT-native operational data, without choosing the desired composite geometry by hand.

## Candidate principle falsified

> The complete composite resource geometry is determined by the quadratic revelation budgets visible in each local row and column sector, together with ordinary local reversible covariance.

This is false already in dimension 2.

## Exact counterfamily

For each n >= 1 define

- A_n = I_n,
- B_n = J_n / sqrt(n), where J_n is the all-ones matrix.

Every row and every column of both A_n and B_n has Euclidean norm exactly 1. Thus any rule that records only the full collection of local row/column quadratic revelation budgets assigns the same local profile to both witnesses.

However their singular spectra are different for every n > 1:

- sigma(A_n) = (1, ..., 1),
- sigma(B_n) = (sqrt(n), 0, ..., 0).

Therefore any unitarily/orthogonally invariant composite resource that depends nontrivially on singular-value distribution can distinguish the two despite identical local revelation profiles.

For the Schatten p norms,

- ||A_n||_p = n^(1/p) for finite p and ||A_n||_inf = 1,
- ||B_n||_p = sqrt(n) for every finite p and ||B_n||_inf = sqrt(n).

Hence p=1, p=4 and p=infinity distinguish A_n and B_n for every n>1, while p=2 does not. The p=2 equality is exactly the Frobenius fact that the squared global norm equals the sum of squared row norms.

### Smallest decisive witness

At n=2,

A = [[1,0],[0,1]],
B = (1/sqrt(2)) [[1,1],[1,1]].

Both have row-norm profile (1,1) and column-norm profile (1,1), but

- ||A||_1 = 2 versus ||B||_1 = sqrt(2),
- ||A||_4 = 2^(1/4) versus ||B||_4 = sqrt(2),
- ||A||_inf = 1 versus ||B||_inf = sqrt(2).

Thus local quadratic budgets cannot determine the composite spectrum or a general composite resource norm.

## Surviving theorem / architecture constraint

Any successful PDT-native composite revelation law must include a genuinely **correlation-sensitive** datum or axiom. Single-party/local marginal quadratic ledgers are insufficient.

Possible surviving directions include a derived rule for mutually resolvable composite channels, connected/correlation sectors, singular-spectrum-equivalent operational data, or another invariant that cannot be reconstructed from local row/column budgets alone. These are research directions, not established PDT results.

This result does **not** select the Frobenius norm. Rather, it shows why a purely local derivation cannot select it. The stronger biorthogonal composite-revelation hypothesis from Cycle 131 remains sufficient to force Frobenius geometry through SVD, but that hypothesis is still OPEN as a PDT-native derivation.

## Dimension stress test

The executable audit checks n=1..12 and n=16,24,32,48,64,96,128 with p in {1,2,4,infinity}. There are 76 dimension/norm cases. Local-profile failures: 0. Maximum floating local-profile discrepancy: 7.77e-16. For every tested n>1, p=1,4,infinity distinguish the witnesses while p=2 does not.

The theorem itself is exact; the numerical sweep is regression evidence only.

## Prior-art boundary

No novelty is claimed for Schatten/unitarily invariant norms, SVD, or the fact that singular values are preserved by orthogonal left/right multiplication. These are standard matrix-analysis results. The PDT contribution here is only the **negative architectural consequence** for the proposed local-revelation derivation route.

Useful standard references checked in this cycle:

- Encyclopedia of Mathematics, *Hilbert-Schmidt norm*: https://encyclopediaofmath.org/wiki/Hilbert-Schmidt_norm
- Encyclopedia of Mathematics, *Frobenius matrix norm*: https://encyclopediaofmath.org/wiki/Frobenius_matrix_norm
- Standard characterization of unitarily invariant norms via symmetric gauge functions is discussed in Horn & Johnson, *Matrix Analysis*; a concise pointer is https://math.stackexchange.com/questions/3310916/what-are-some-lesser-known-unitary-invariant-norms-for-matrices

## Files

- `cycle132_local_marginal_composite_no_go.py`
- `tests/test_cycle132_local_marginal_composite_no_go.py`
- `results/cycle132_local_marginal_composite_no_go.json`
