# Cycle 248 — sharp-purification thermodynamic structure is dimension-blind

## Status

- **PROVED:** the spectral normalization, exact refinement conservation, and delta-majorizes-uniform statements in the accompanying regression hold for every finite `n >= 1`; exact code covers `n=1..12`.
- **FALSIFIED:** these dimension-uniform resource/majorization properties cannot, by themselves, be a non-circular selector of `n=3`.
- **IMPORTED/KNOWN:** majorization/thermodynamic structure in sharp theories with purification is established prior art (Chiribella & Scandolo, 2016/2017).
- **OPEN:** PDT-native composition law.
- **OPEN:** PDT-native non-circular `n=3` derivation.
- **OPEN:** same-input quantitative `P_PDT(O|I,R) != P_QM(O|I,R)` prediction.
- **OPEN:** experimentally distinctive PDT inequality.
- **NOT PROMOTED:** BREAKTHROUGH CANDIDATE.

## Exact hypotheses tested

Let a finite system have `n` perfectly distinguishable alternatives and a normalized spectral weight vector `p=(p_1,...,p_n)`. Consider only dimension-uniform requirements:

1. `sum_i p_i = 1`;
2. refinement may split one weight `p_i -> (p_i/2,p_i/2)` without changing total weight;
3. the pure spectrum `(1,0,...,0)` majorizes the uniform spectrum `(1/n,...,1/n)`;
4. the same rule is applied for every finite `n` without an `n=3` constant or predicate.

## Theorem (dimension-blindness)

For every positive integer `n`, hypotheses 1–4 are satisfiable. Hence they cannot imply `n=3` uniquely.

### Proof

Normalization is immediate for both spectra. Splitting `p_i` into two halves preserves its contribution exactly, so total spectral weight is conserved. For the pure spectrum `d_n=(1,0,...,0)` and uniform spectrum `u_n=(1/n,...,1/n)`, every ordered partial sum obeys `sum_{i<=k} d_{n,i}=1 >= k/n=sum_{i<=k}u_{n,i}` for `1<=k<=n`, with equality at `k=n`. Thus `d_n` majorizes `u_n` for every finite `n`. None of these statements changes at `n=3`. QED.

## Counterexample to an n=3 inference

The smallest competing nontrivial dimension is `n=2`: `d_2=(1,0)` majorizes `u_2=(1/2,1/2)`, and exact refinement conserves normalization. Therefore any argument claiming these resource/thermodynamic properties force `n=3` is already falsified at `n=2`.

## Prior-art boundary

Chiribella and Scandolo's sharp-theories-with-purification programme derives general spectral, majorization and thermodynamic structure from Causality, Purity Preservation, Pure Sharpness and Purification. Their class includes complex and real quantum theory and a suitable extension of classical probability theory. Their microcanonical resource framework studies random-reversible, noisy and unital operations and majorization. Therefore importing those properties and relabeling them as PDT distinctions is not PDT-native novelty.

References:
- G. Chiribella and C. M. Scandolo, *Entanglement as an axiomatic foundation for statistical mechanics*, arXiv:1608.04459.
- G. Chiribella and C. M. Scandolo, *Microcanonical thermodynamics in general physical theories*, arXiv:1608.04460.

## Consequence for PDT-II

Thermodynamic/resource structure can become useful only after PDT independently supplies a primitive that is not dimension-uniform in this vacuous sense. A valid `n=3` result still requires an independently derived feasibility predicate `C(n,R)` whose hypotheses contain neither the desired dimension nor an equivalent hidden selector. Gravity/capacity claims remain deferred until such a law is derived rather than imported.
