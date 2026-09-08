# Cycle 003 — Spectral coherence annulus theorem

**Status:** PROVED as a mathematical statement; historical novelty OPEN. This is not a new-physics claim.

## Setup
Let the environment state have spectral decomposition

\[\eta=\sum_{j=1}^d p_j |j\rangle\langle j|,\qquad p_j\ge0,\quad \sum_j p_j=1.\]

Take `U0 = I` and a relative branch unitary commuting with eta,

\[U_1=\sum_j e^{-i\theta_j}|j\rangle\langle j|.\]

Then both conditional environment outputs are exactly unchanged:

\[\rho_E^{(0)}=\rho_E^{(1)}=\eta,\]

while the system coherence factor is

\[\chi=\operatorname{Tr}(\eta U_1^\dagger)=\sum_j p_j e^{i\theta_j}.\]

## Theorem
Let `p_max = max_j p_j`. As the phases vary independently, the attainable coherence set is exactly the closed annulus

\[\boxed{\{z\in\mathbb C: r_{\min}\le |z|\le1\}},\qquad r_{\min}=\max(0,2p_{\max}-1).\]

### Proof
The upper bound follows from the triangle inequality: `|chi| <= sum p_j = 1`. For the lower bound, isolate a largest weight `p_max`; the reverse triangle inequality gives

\[|\chi|\ge p_{\max}-(1-p_{\max})=2p_{\max}-1,\]

and zero is the effective lower bound when this quantity is negative.

Attainability is the standard polygon closure fact for vectors of prescribed lengths. The resultant magnitude of segments of lengths `p_j` varies continuously from `max(0,2p_max-1)` to `sum p_j=1`; a common rotation of all phases supplies every complex argument. Hence every point of the annulus is attained.

## Consequences
1. If `p_max <= 1/2`, unchanged conditional-state tomography leaves the **entire unit disk** of coherence factors possible.
2. If `p_max > 1/2`, it leaves an annulus with a nonzero inaccessible central disk.
3. For a pure environment (`p_max=1`), only `|chi|=1` is possible in this unchanged-record commuting construction.
4. The earlier maximally mixed qubit disk theorem is the boundary case `p_max=1/2`.

This gives a quantitative relation between environment spectrum and coherence non-identifiability, while preserving identical conditional environment states.

## PDT implication
Any PDT law that tries to infer controlled-dephasing coherence solely from the pair of conditional density operators fails even when those operators are known exactly. In the unchanged-record sector, the spectrum alone bounds the ambiguity through `p_max`, but does not identify `chi`. A predictive PDT extension therefore requires relative branch information or an independently justified restriction on allowed microscopic unitaries.

## Novelty discipline
The proof uses elementary polygon/triangle geometry and standard unitary quantum mechanics. The mathematical ingredients are known; this note does **not** claim historical novelty. The PDT-specific value is the explicit identifiability audit and quantitative spectral classification of the same-input obstruction. Prior-art review remains required before any novelty claim.
