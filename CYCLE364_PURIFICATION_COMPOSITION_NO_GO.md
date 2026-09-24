# Cycle 364 — Purification / reversible-dilation composition no-go

## Target attacked
PDT-II priorities (1) PDT-native composition law, (2) non-circular n=3 derivation, and (3) same-input PDT/QM probability separation.

## Candidate principle
**Purification selector.** Every mixed state of a system is the marginal of a pure state of a composite system, with purifications unique up to a reversible transformation on the purifying system.

This is a strong compositional candidate because it links mixed states, composites, environment records, reversible groups, and irreversible effective dynamics.

## Exact hypotheses
Let the local theory be ordinary finite-dimensional complex quantum theory on C^n. Composition is the Hilbert tensor product. Reversible transformations are unitaries. For density operator rho with spectral decomposition

rho = sum_i lambda_i |i><i|,

a purification is

|Psi_rho> = sum_i sqrt(lambda_i) |i>_S |i>_E,

with dim(E) at least rank(rho). Partial trace over E returns rho. Two purifications of the same rho on a sufficiently large common purifying space are related by an isometry/unitary on E (standard purification uniqueness).

## Prove-or-falsify result
### Theorem 364A — all-dimensional counterfamily [PROVED]
For every finite n >= 2, take

rho_n = diag(1/2, 1/2, 0, ..., 0) on C^n.

Then

|Psi_n> = (|0,0> + |1,1>)/sqrt(2)

in C^n tensor C^n is a pure state and Tr_E |Psi_n><Psi_n| = rho_n exactly. Hence the existence of nontrivial purification is dimension-uniform for every n >= 2.

The smallest nontrivial counterexample to `purification => n=3` is n=2. n=4 is the smallest higher-dimensional counterexample to uniqueness of n=3.

### Theorem 364B — arbitrary-state construction [PROVED / IMPORTED-KNOWN]
For any finite-dimensional rho >= 0 with Tr rho=1 and rank r, the spectral construction above gives a purification using an r-dimensional environment. This proof has no n=3-specific step.

### Corollary 364C — no same-input PDT/QM gap from purification alone [PROVED as an inference]
If PDT adopts exactly the ordinary quantum state space, tensor product, unitary reversible group, Born rule and purification rule under the same resource window, purification supplies no altered outcome probability. Therefore a statement `P_PDT(O|I,R) != P_QM(O|I,R)` cannot be inferred from purification alone; an additional PDT-native operational restriction or probability law is required.

## Exact n=1..12 stress audit
The accompanying CSV records the canonical rank-2 family. n=1 admits only the trivial one-dimensional state, so it cannot host this nontrivial rank-2 witness. Every n=2..12 has the same Schmidt rank 2, reduced spectrum (1/2,1/2,0,...), unit trace, and zero reconstruction error analytically. There is no n=3 singularity.

The construction embeds unchanged in every higher finite dimension, so randomized high-dimensional testing is unnecessary for the existence claim: the analytic embedding is stronger.

## Edge / degenerate cases
* Pure rho (rank 1): purification is a product state; no dimension selector.
* Rank-deficient rho: minimal purifying dimension is rank(rho), not ambient n.
* Maximally mixed rho=I_n/n: canonical purification has Schmidt rank n for every n; again no n=3 selector.
* Composite/environment interpretation: tracing out E produces the mixed state in every finite n.
* Reversible group: U(n) supplies the standard equivalence freedom; nothing selects n=3.

## Prior-art boundary [IMPORTED/KNOWN]
Purification is not PDT-native. Chiribella, D'Ariano and Perinotti, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348 (2010), formulate purification as a GPT principle, including uniqueness up to reversible channels, and connect it to reversible realizations of physical processes. Their later informational reconstruction uses purification as one postulate in a package deriving finite-dimensional quantum theory. Therefore neither purification, reversible dilation, nor their use as a compositional axiom is novel to PDT.

References:
- DOI 10.1103/PhysRevA.81.062348
- DOI 10.1103/PhysRevA.84.012311

## Status ledger
| Claim | Status |
|---|---|
| finite-dimensional quantum purification | IMPORTED/KNOWN |
| explicit rank-2 counterfamily for all n>=2 | PROVED |
| purification => n=3 | FALSIFIED |
| purification alone => unique PDT composition | FALSIFIED as an inference |
| purification alone => same-input PDT/QM probability gap | FALSIFIED as an inference |
| purification/reversible-dilation principle is PDT-native | FALSIFIED by prior art |
| additional PDT-native composition selector | OPEN |
| PDT-native same-input quantitative deviation | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Consequence for PDT-II
Do not spend further cycles attempting to obtain n=3 merely from purification, environmental completion, or reversible dilation. Any surviving PDT-II composition proposal must add a precisely stated constraint not already satisfied by ordinary finite-dimensional quantum theory and must then survive the same all-dimensional counterexample search.
