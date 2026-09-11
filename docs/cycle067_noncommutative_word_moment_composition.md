# Cycle 067 — Noncommutative trace-word composition boundary

## Target
PDT-II target (1): find a composition object that retains the genuinely noncommutative relational information killed by the scalar, spectral, relative-modular-spectrum and Nussbaum–Szkoła/Petz-family candidates.

## Candidate object
For a finite-dimensional density-operator pair `(rho,sigma)` and every finite word `w` over the noncommuting alphabet `{r,s}`, define

`M_w(rho,sigma) = Tr[w(rho,sigma)]`.

Examples are `Tr(rho sigma)`, `Tr(rho^2 sigma)`, and `Tr(rho sigma rho sigma)`.

## Exact tensor composition theorem — PROVED
For independent pairs `(rho_A,sigma_A)` and `(rho_B,sigma_B)`, let

`rho_AB = rho_A tensor rho_B`, `sigma_AB = sigma_A tensor sigma_B`.

For every word `w`,

`M_w(rho_AB,sigma_AB) = M_w(rho_A,sigma_A) M_w(rho_B,sigma_B)`.

### Proof
Each factor in `w(rho_AB,sigma_AB)` is either `rho_A tensor rho_B` or `sigma_A tensor sigma_B`. Repeated use of `(X_A tensor X_B)(Y_A tensor Y_B)=(X_A Y_A) tensor (X_B Y_B)` gives

`w(rho_AB,sigma_AB)=w(rho_A,sigma_A) tensor w(rho_B,sigma_B)`.

Taking traces and using `Tr(X tensor Y)=Tr(X)Tr(Y)` proves the identity.

Thus the complete word-moment fingerprint has an exact componentwise multiplicative product law.

## Operational completeness boundary — IMPORTED/KNOWN
For Hermitian matrix tuples, equality of traces of all noncommutative words is an established simultaneous-unitary-equivalence criterion (Specht-type trace invariant theory and its tuple generalizations). Since density matrices are Hermitian, the complete family `{M_w}` determines the pair up to simultaneous unitary conjugation. Consequently any operational quantity invariant under simultaneous unitary conjugation, including trace distance, is determined by the complete family.

This is therefore **not a PDT-native breakthrough**. It is a useful boundary result: scalar/spectral summaries can fail because they discard word ordering, whereas the full noncommutative trace algebra is complete but imports essentially the whole joint operator orbit.

Relevant prior art includes Specht's unitary-similarity criterion and later simultaneous-equivalence/tuple extensions; see Futorny, Horn & Sergeichuk (2017), arXiv:1701.08826, and Jing (2015), arXiv:1504.06790.

## Separation of the Cycle-066 Petz counterfamily — PROVED
For the exact `d=4` phase family from Cycle 066, all Nussbaum–Szkoła data are phase-independent, but the first separating mixed word occurs already at length four:

`w = r s r s`.

At `theta=0`,

`Tr(rho sigma rho sigma) = 0.0303`,

while at `theta=pi`,

`Tr(rho sigma rho sigma) = 0.0282`.

Hence the gap is exactly `0.0021` to the displayed precision. This explicitly shows the operator-order information missed by the complete Petz scalar hierarchy.

## Numerical stress audit — NUMERICALLY SUPPORTED
The executable audit checks the exact tensor-factorization identity for seven representative words across `d_A=1..12` (20 random pairs per dimension) and `d_A in {16,24,32,48,64}` (8 pairs each), with a second factor of dimension one or two. Total tested word identities: **1,960**. Failures at tolerance `1e-10`: **0**. Maximum observed floating-point error: about `3.33e-16`.

These computations are regression evidence only; the tensor law itself is algebraically proved above.

## Classification
- Exact tensor composition of every mixed-word moment: **PROVED**.
- Complete mixed-word trace fingerprint as simultaneous-unitary orbit invariant: **IMPORTED/KNOWN**.
- Dimension stress audit: **NUMERICALLY SUPPORTED**.
- `BREAKTHROUGH CANDIDATE`: **NO**.

## Consequence for PDT-II
The search boundary is now sharper. A useful PDT-native composition law must lie strictly between two failures:

1. scalar/spectral/Petz summaries are too compressed and can lose operational distinction;
2. the complete noncommutative trace-word algebra is sufficient, but it is established invariant theory and effectively retains the full joint operator orbit.

The unresolved task is therefore to derive a **smaller PDT-native operational algebra or finite resource-indexed subset of noncommutative invariants** whose closure under composition is physically motivated and that yields a new falsifiable consequence not already implied by standard quantum operator theory.
