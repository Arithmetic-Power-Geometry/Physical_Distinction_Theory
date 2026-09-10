# Cycle 060 — Gaussian-shift countermodels block a composition/resource derivation of `n=3`

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN mathematics.**

This cycle does **not** establish a PDT breakthrough. It closes a dimension-selection route that had remained logically possible in the previous ledger.

## Claim tested

Could the already-surviving PDT ingredients — Euclidean scalar distinction, exact independent composition, resource/revelation monotonicity, two-point isotropy (TPI), and genuinely noncommuting connected reversibility (NCR) — force Pairwise Calibration Closure (PCC), and thereby make the earlier `TPI + PCC + NCR => n=3` theorem non-circular?

The answer is **no**.

## Countermodel family

For every integer `n>=1`, let an elementary preparation labelled by `x in R^n` generate the observation law

`E_x = N(x, I_n)`.

For two preparations `x,y`, use total-variation operational distinction

`D_n(x,y) = TV(N(x,I_n), N(y,I_n))`.

Equal-covariance Gaussian hypothesis testing gives

`D_n(x,y) = 2 Phi(||x-y||_2/2) - 1`.

Hence the distinction is a strictly increasing function of Euclidean separation. Orthogonal transformations preserve it.

### 1. Euclidean isotropy and TPI

`SO(n)` acts by `x -> gx`. Since `||gx-gy||=||x-y||`, the operational distinction is invariant. For a fixed nonzero reference direction, its stabilizer `SO(n-1)` is transitive on every fixed-angle sphere, so the model has TPI for `n>=2`.

### 2. NCR

For every `n>=3`, `SO(n)` is connected and non-Abelian. Thus the model has genuinely noncommuting reversible transformations.

### 3. Exact independent composition

For independent Gaussian-shift experiments, likelihood ratios multiply and log-likelihood ratios add. Explicitly,

`ell_{x,y}(z) = (x-y).z - (||x||^2-||y||^2)/2`,

and for two independent sectors,

`ell_{(x,u),(y,v)}(z,w) = ell_{x,y}(z) + ell_{u,v}(w)`.

Therefore the same exact likelihood-profile/product structure established in Cycles 055–058 is present in every dimension.

### 4. Resource restriction / revelation monotonicity

Any observation coarse-graining is a Markov kernel, so total variation obeys data processing. Coordinate projections provide an explicit closed Gaussian subfamily: projecting `N(x,I_n)` to `k` coordinates yields `N(Pi_k x, I_k)` and

`||Pi_k(x-y)|| <= ||x-y||`,

hence

`D_k(Pi_k x, Pi_k y) <= D_n(x,y)`.

The likelihood-ratio conditional-expectation law used in Cycle 056 is ordinary statistical-experiment data processing and therefore also applies.

### 5. PCC nevertheless fails for every `n>=4`

Fix an ordered pair of linearly independent reference directions `e1,e2`. Their pointwise stabilizer in `SO(n)` contains `SO(n-2)`. For `n>=4` this stabilizer is nontrivial.

An explicit witness rotates only the `e3-e4` plane while fixing `e1,e2` exactly. Therefore one ordered reference pair does **not** determine the reversible transformation, so PCC fails.

The smallest decisive countermodel is consequently `n=4`:

- Euclidean/isotropic operational distinction: yes;
- TPI: yes;
- connected noncommuting reversibility: yes;
- exact independent likelihood composition: yes;
- resource monotonicity / revelation law: yes;
- PCC: **no**.

Thus

`composition + resource laws + TPI + NCR  !=>  PCC`

and therefore these ingredients cannot by themselves yield a non-circular derivation of `n=3`.

## Computational audit

`cycle060_gaussian_shift_dimension_no_go.py` checks dimensions `n=1..12` with 200 randomized trials each and dimensions `16,24,32,48,64,96,128` with 50 trials each. It audits orthogonal invariance, projection monotonicity, exact product log-likelihood additivity, and explicit nonidentity ordered-pair stabilizers for `n>=4`.

The regression suite is in `tests/test_cycle060_gaussian_shift_dimension_no_go.py`.

The numerical audit is consistency evidence only; the no-go itself is analytic.

## Prior-art boundary

Nothing in the Gaussian/statistical machinery is claimed as historically new. Gaussian shift experiments, exact equal-variance Gaussian TV formulas, likelihood-ratio product rules, `SO(n)` group actions, and data-processing inequalities are established mathematics. The PDT contribution of this cycle is only the model-theoretic obstruction: these already-adopted ingredients cannot logically derive the missing PCC principle.

Relevant prior-art checkpoints include standard statistical-decision theory/Blackwell comparison and modern summaries of total variation between Gaussian laws. Kelbert (2023, *Analytics*, 2(1), 225–245) gives the equal-variance Gaussian TV expression in one dimension; the multivariate equal-covariance result reduces to the one-dimensional discriminant direction. Data processing of total variation under Markov kernels is standard and is also explicitly used in contemporary information-theory work.

## Surviving target

A genuine non-circular PDT `n=3` derivation must add or derive a principle that excludes the entire `n>=4` Gaussian-shift countermodel family. PCC still does that, but this cycle proves PCC cannot be obtained from the present composition/resource/TPI/NCR package alone.

Therefore the strongest unresolved question becomes:

> What independent PDT-native physical principle forces finite reference calibration (PCC or a weaker substitute) rather than merely isotropic distinguishability, ordinary composition, and resource data processing?
