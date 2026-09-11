# Cycle 084 — Proper-Marginal Composition No-Go

## Target
PDT-II target (1): determine whether the full multipartite quadratic distinction ledger can be reconstructed universally from all proper subsystem states/ledgers.

## Exact witness family
For local dimension d >= 2 and N >= 2, define

rho_c = 1/2 (|0^N><0^N| + |1^N><1^N|) + c (|0^N><1^N| + |1^N><0^N|),

with |c| <= 1/2. Positivity follows because the nonzero 2x2 block has eigenvalues 1/2 +/- c.

## Theorem — proper marginals are blind to c
Trace out any nonempty subset of parties. Every off-diagonal term |0^N><1^N| contains at each traced site the factor |0><1|, whose trace is zero. Hence every proper reduced state is

rho_T = 1/2 (|0^|T|><0^|T|| + |1^|T|><1^|T||)

for every proper nonempty T, independent of c.

Therefore the complete collection of all proper subsystem density matrices, and hence every quantity determined solely by those marginals, is identical for the entire family {rho_c}.

## Yet the global quadratic distinction changes
Let D=d^N and E_D(rho)=D Tr(rho^2)-1. Directly,

Tr(rho_c^2)=1/2 + 2 c^2,

so

E_D(rho_c)=D(1/2+2c^2)-1.

Relative to c=0,

Delta E_D = 2 D c^2 = 2 d^N c^2 > 0 for c != 0.

Moreover, the perturbation

Delta_c = c(|0^N><1^N|+|1^N><0^N|)

has zero partial trace on every site. It therefore lies wholly in the all-party traceless subset sector of the Cycle-083 Hilbert-Schmidt decomposition. Its sector contribution is exactly

Delta C_{1...N}=D ||Delta_c||_2^2 = 2 d^N c^2.

Thus all proper subset sectors can be fixed while the genuine N-party sector changes continuously.

## Smallest decisive tripartite witness
For three qubits (d=2, N=3):

- c=0 gives the incoherent GHZ mixture and E_8=3.
- c=1/2 gives the pure GHZ state and E_8=7.
- Every one- and two-qubit marginal is identical in the two cases.
- The hidden three-party sector increment is exactly 4.

Therefore no universal map

F({rho_T : T proper subset of {1,...,N}})

can reconstruct the full quadratic distinction ledger for arbitrary multipartite states.

## Classification
- Proper-marginal nonidentifiability theorem: **PROVED**.
- Universal proper-marginal closure of the full quadratic ledger: **FALSIFIED**.
- Dense regression checks and formula sweeps: **NUMERICALLY SUPPORTED**.
- GHZ/quantum-marginal nonuniqueness mechanism: **IMPORTED/KNOWN**.
- **BREAKTHROUGH CANDIDATE: NO**.

## Stress audit
The executable audit checks dense tripartite matrices for local dimensions d=2,...,6 and finds zero proper-marginal difference between c=0 and c=1/2, with zero residual against the exact energy formula at floating-point precision in these sparse witnesses. The exact formula is swept for d=2,...,12,16,24,32,48,64,96,128 and N=2,...,12. d=1 is correctly classified as degenerate because two distinct local basis states do not exist.

The proof is algebraic; numerical checks are regression evidence only.

## Prior-art boundary
This mechanism is not novel quantum foundations. The quantum-marginal literature has long studied when global multipartite states are or are not fixed by reduced density matrices. Linden and Wootters showed generic determination from sufficiently large collections of parts, while exceptional GHZ-type families exhibit residual global information not contained in lower-order marginals. Sawicki, Walter and Kus (2012) explicitly identify GHZ-related exceptions in three-qubit marginal reconstruction. Therefore PDT must not claim novelty for marginal nonidentifiability itself.

Relevant references:
- Linden, N., & Wootters, W. K. (2002). The Parts Determine the Whole in a Generic Pure Quantum State. Physical Review Letters, 89, 277906. DOI: 10.1103/PhysRevLett.89.277906.
- Sawicki, A., Walter, M., & Kus, M. (2012). When is a pure state of three qubits determined by its single-particle reduced density matrices? arXiv:1207.3849.

## PDT-II consequence
Cycle 083's subset-sector ledger remains exact, but Cycle 084 proves that a genuinely multipartite sector cannot in general be generated from all lower-order sector data. Any defensible PDT-native composition law for correlated systems must therefore carry an independent N-body datum, rule, dynamical generator, accessibility cost, or constraint. Assuming that datum away would contradict the witness family above.
