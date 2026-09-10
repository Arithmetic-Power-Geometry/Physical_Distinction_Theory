# Cycle 059 — Quantum spectral-profile nonclosure

## Status

**PROVED / FALSIFIED / IMPORTED-KNOWN boundary.** Not a `BREAKTHROUGH CANDIDATE`.

## Question attacked

Can the classical PDT distinction-profile idea be lifted to a quantum pair `(rho,sigma)` simply by replacing the classical likelihood ratio with the sandwich operator

`L = sigma^{-1/2} rho sigma^{-1/2}`

and retaining the complete `sigma`-weighted spectral measure of `L`?

If this were sufficient, operational trace distinction would be a function of that one-dimensional measure.

## Counterexample family

Let

`Sigma = diag(0.50,0.25,0.15,0.10)`

and let the eigenvalues of `L` be

`lambda = (1.8,1.2,0.7,0.3)`.

For every phase `theta`, use the unitary complex-Hadamard family

```
H(theta) = (1/2) [[1,1,1,1],
                  [1,z,-1,-z],
                  [1,-1,1,-1],
                  [1,-z,-1,z]],  z=exp(i theta).
```

Define

`L_theta = H(theta) diag(lambda) H(theta)^dagger`

and

`rho_theta = Sigma^(1/2) L_theta Sigma^(1/2)`.

Because every entry of `H(theta)` has squared modulus `1/4`, every eigenvector of `L_theta` has the same `Sigma`-weight `1/4`. Therefore the entire reference-weighted spectral measure is phase-independent:

`mu = (1/4) delta_1.8 + (1/4) delta_1.2 + (1/4) delta_0.7 + (1/4) delta_0.3`.

Normalization also holds because the mean of the four eigenvalues is one.

However direct Hermitian diagonalization gives

`D_tr(rho_0,Sigma) = 0.2397855636768688`

while

`D_tr(rho_pi,Sigma) = 0.2110635316661873`.

Hence

`mu_0 = mu_pi` but `D_tr(rho_0,Sigma) != D_tr(rho_pi,Sigma)`.

The naive quantum analogue of the classical one-dimensional distinction profile is therefore insufficient.

## Dimension stress test

The witness embeds by direct sum with an identical tail sector. The executable audit scans 129 phases on `[0,pi]` and dimensions `d=4,...,12`. Every dimension has nonzero trace-distance spread while the underlying four-dimensional weighted spectral measure remains fixed. No normalization or positivity failures occurred.

Dimensions `1..3` are not claimed to realize this particular continuous Hadamard witness; the smallest explicit witness found here is `d=4`.

## Interpretation for PDT-II

The result blocks a tempting route:

`quantum distinction object = weighted spectrum of one likelihood operator`.

Noncommutative orientation relative to the reference state carries operational information not captured by that one-dimensional spectral measure. Any PDT-native quantum composition object must retain genuinely noncommutative data (for example an operator/algebraic relation, compatibility structure, or another invariant strong enough to determine operational statistics), not merely a scalar divergence or classical-like spectral profile.

This is a structural no-go, not a new physical prediction and not a historical novelty claim. Quantum relative modular operators, Petz-type quasi-entropies/f-divergences, and quantum comparison-of-experiments are established prior art; the present role is to reject an over-aggressive PDT reduction.

## Falsified statement

> For faithful finite-dimensional quantum state pairs, the complete reference-weighted spectral measure of `sigma^{-1/2} rho sigma^{-1/2}` determines trace distance and therefore provides a sufficient PDT composition state.

This statement is false.
