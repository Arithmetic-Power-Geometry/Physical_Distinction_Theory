# PDT Breakthrough Lab — Research Cycle 002

## Result: scalar environmental distinguishability does not identify coherence for mixed records

**Status: PROVED / NO-GO.**

This cycle closes a tempting same-input shortcut. For a mixed environment, the scalar trace distinguishability

\[
D_E=\frac12\|\rho_E^{(0)}-\rho_E^{(1)}\|_1
\]

does not by itself determine the controlled-dephasing coherence factor

\[
|\chi|=\left|\mathrm{Tr}(U_0\eta_EU_1^\dagger)\right|.
\]

### Explicit counterfamily

Take a qubit environment with

\[
\eta_E=I/2,\qquad U_0=I,\qquad U_1(\theta)=e^{-i\theta\sigma_z/2}.
\]

Because the maximally mixed state is invariant under every unitary,

\[
\rho_E^{(0)}=\rho_E^{(1)}=I/2
\]

for every `theta`, hence

\[
D_E=0.
\]

However,

\[
\chi(\theta)=\frac12\mathrm{Tr}\,U_1(\theta)^\dagger=\cos(\theta/2),
\]

so `|chi|` ranges continuously from 1 at `theta=0` to 0 at `theta=pi` while `D_E` remains exactly zero.

Therefore there cannot exist a universal single-valued function `f` such that

\[
|\chi|=f(D_E)
\]

for all mixed environmental records under controlled unitary dephasing.

### Consequence

Any PDT same-input prediction that attempts to infer the exact coherence decay or ADDE rate from `D_E` alone is non-identifiable in the mixed-record regime. A valid exact predictor needs additional information, for example the relative unitary/phase-sensitive overlap itself or a sufficiently rich operational statistic that provably determines it.

This strengthens the existing mixed-record envelope

\[
|\chi|\le f_E\le\sqrt{1-D_E^2}
\]

by giving a constructive witness that the rightmost scalar `D_E` is generally insufficient for equality or exact prediction.

### Computational audit

`mixed_record_no_go.py` implements the family and `tests/test_mixed_record_no_go.py` verifies:

- `D_E=0` to floating-point precision across a sweep of `theta`;
- computed `|chi|` agrees with `|cos(theta/2)|`;
- two cases with the same `D_E=0` have maximally different coherence factors (`|chi|=1` and `|chi|=0`).

`results/mixed_record_nonidentifiability.csv` records the parameter sweep.

### Prior-art boundary checked 2026-09-08

This is not claimed as new quantum mechanics. It is consistent with established wave-particle duality and mixed-environment decoherence literature, where pure-state equalities generally weaken to inequalities for mixed marker/environment states. In particular, Roszak, *Physical Review Research* 2, 043062 (2020), explicitly emphasizes that pure-state conclusions about qubit decoherence do not transfer directly to mixed environments. Contemporary wave-particle duality work also treats the inadequacy of a single trace-distance path-distinguishability scalar for mixed marker states as an active issue.

The PDT contribution here is the explicit identifiability no-go and its role as a kill test for candidate PDT same-input laws.

## Breakthrough status

**No breakthrough claim.** This is a rigorous elimination result. It rules out an entire class of scalar-`D_E` exact coherence laws and narrows the search to richer operational statistics or genuinely new dynamical principles.
