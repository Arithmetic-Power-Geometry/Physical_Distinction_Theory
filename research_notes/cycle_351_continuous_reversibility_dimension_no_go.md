# Cycle 351 — Continuous reversible transitivity does not select n=3

## Target attacked
PDT-II target (2): a non-circular PDT-native derivation of n=3, while checking implications for targets (1) and (3).

## Candidate principle
(CRT) For every pair of pure states of a nontrivial elementary system there exists a continuous reversible transformation connecting them.

## Exact hypotheses
Let the normalized pure-state space X_n of an n-level complex quantum system be the complex projective space CP^{n-1}. Reversible dynamics contains the projective unitary action induced by U(n). The candidate inference tested is

CRT => n=3.

## Proof of the counterfamily
For every integer n>=2 and every two unit vectors psi,phi in C^n, extend each to an orthonormal basis. There is a unitary U with U psi=phi. U(n) is path connected: diagonalize U=V diag(exp(i theta_j)) V^*, and define U(t)=V diag(exp(i t theta_j)) V^*, 0<=t<=1. Hence U(t) is a continuous path of reversible transformations from the identity to U, taking psi continuously to phi. Therefore CRT holds for every complex quantum dimension n>=2.

The smallest counterexample to CRT=>n=3 is n=2. n=4 is the smallest counterexample above 3. No singularity occurs at n=3.

For n=1 the pure-state space is a singleton, so transitivity is vacuous; this is recorded separately rather than treated as a nontrivial success.

## Exact n=1..12 stress
The accompanying CSV records the analytic verdict for n=1..12. For n>=2 CRT holds by the constructive unitary/path proof above. Thus the candidate dimension selector fails throughout the requested range and analytically in every higher finite dimension.

## Adversarial / edge checks
- n=1: vacuous singleton case.
- n=2: decisive nontrivial counterexample (qubit).
- n>3: infinite counterfamily, including n=4.
- Degenerate spectra/mixed states do not rescue the claim: CRT concerns pure-state transitivity, while unitary orbits of mixed states are instead classified by spectrum.
- Restricting the reversible group can destroy transitivity, but that supplies an extra model choice; it cannot make CRT alone select n=3.
- Composition is not fixed by CRT: CRT is a single-system reversible-dynamics condition and supplies no intrinsically joint cone/tensor selector.

## Prior-art audit
This route is not PDT-native. Hardy's 2001 reconstruction explicitly uses continuous reversible transformations between pure states to rule out classical probability theory; it does not select Hilbert dimension 3. Later reconstruction work likewise combines reversibility/continuity with additional operational assumptions. Mueller and Masanes (2012) obtain three spatial dimensions only after adding a specific directional-information and interaction framework; that is evidence that continuity/reversibility alone is insufficient.

Relevant prior art:
- L. Hardy, “Quantum Theory From Five Reasonable Axioms,” arXiv:quant-ph/0101012.
- M. P. Mueller and L. Masanes, “Three-dimensionality of space and the quantum bit: an information-theoretic approach,” arXiv:1206.0630.

## PDT-II classification
- CRT for finite-dimensional complex QM, all n>=2: PROVED / IMPORTED-KNOWN structure.
- CRT => n=3: FALSIFIED.
- CRT => unique PDT composition: FALSIFIED as an inference.
- CRT => P_PDT(O|I,R) != P_QM(O|I,R): FALSIFIED as an inference.
- A PDT-native principle that excludes n=2 and every n>=4 without importing the desired dimensionality: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Surviving lesson
Continuous reversible transitivity can separate discrete classical pure-state geometry from continuous quantum-like geometry, but it is dimension-blind inside the entire complex-quantum family. Any PDT n=3 theorem must contain additional PDT-native structure whose hypotheses demonstrably fail for n=2 and n>=4; merely appealing to continuity, reversibility, or pure-state homogeneity is circularly insufficient.
