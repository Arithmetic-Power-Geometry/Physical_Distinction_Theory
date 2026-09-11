# Cycle 065 — Relative-modular-spectrum nonclosure

## Target
PDT-II target (1): find a genuinely quantum/PDT-native distinction object with a defensible composition law, or falsify insufficient candidates.

## Candidate tested
For faithful finite-dimensional quantum states, consider the relative modular superoperator

`Delta_{rho|sigma}(X) = rho X sigma^{-1}`.

Because left and right multiplication commute, its eigenvalues are all ratios `r_i/s_j`, where `{r_i}` and `{s_j}` are the separate spectra of `rho` and `sigma`. Under tensor products the superoperators tensor, so the spectrum has an attractive exact multiplicative composition rule.

The question was whether this full spectrum is also operationally complete enough to retain quantum distinction.

## Decisive counterexample
Take

`rho_0 = diag(0.7,0.3)`,

`rho_1 = diag(0.3,0.7)`,

`sigma = diag(0.8,0.2)`.

`rho_0` and `rho_1` have the same spectrum and `sigma` is unchanged. Therefore both relative modular superoperators have the identical spectrum

`{0.375, 0.875, 1.5, 3.5}`.

Yet

`D_tr(rho_0,sigma)=0.1`,

while

`D_tr(rho_1,sigma)=0.5`.

Hence identical relative-modular spectrum does not imply identical operational trace distinction.

## Theorem
For faithful density operators `rho,sigma` on a finite-dimensional Hilbert space,

`spec(L_rho R_{sigma^{-1}}) = { r_i/s_j : i,j }`.

Consequently this spectrum is invariant under independent changes of the eigenbases of `rho` and `sigma`. Any operational quantity that depends on their relative eigenbasis cannot be a function of that spectrum alone. Trace distance supplies an explicit two-dimensional witness.

The proof is immediate from the commuting superoperators `L_rho` and `R_{sigma^{-1}}`: on matrix units formed from eigenvectors of `rho` on the left and `sigma` on the right, the eigenvalue is `r_i/s_j`.

## Stress tests
The executable audit keeps the separate state spectra fixed and randomizes the relative basis. Dimensions 1 through 12 are included; dimension 1 is the expected degenerate case. For dimensions 2–12, 100 random unitary orientations were tested per dimension. Higher-dimensional tests used 25 orientations at dimensions 16, 24, 32, 48 and 64.

No relative-modular-spectrum invariance failures were observed. Every tested nontrivial dimension produced a positive spread in trace distance. The minimum observed spread over the tested nontrivial dimensions was `0.01258416704662535`.

These numerical tests are regression/stress evidence; the qubit construction and superoperator spectral identity provide the proof.

## Prior-art boundary
Relative modular operators, Petz quasi-entropies, quantum relative entropy and associated monotonicity/divergence constructions are established operator-algebra and quantum-information machinery. This cycle therefore makes no novelty claim for the modular formalism itself.

## Classification
- Spectral identity: **PROVED / IMPORTED-KNOWN mathematics**.
- Claim that the relative-modular spectrum alone is a complete quantum distinction object: **FALSIFIED**.
- PDT implication: **PROVED search boundary**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving requirement for PDT-II target (1)
An exact nonclassical composition object must retain information beyond separate spectral ratios. In particular, it must encode enough noncommutative relational structure—relative eigenbasis/orientation, operator-system compatibility, or an equivalent operational invariant—to recover the distinctions relevant to measurements. Exact tensor-product closure without such relational information is insufficient.
