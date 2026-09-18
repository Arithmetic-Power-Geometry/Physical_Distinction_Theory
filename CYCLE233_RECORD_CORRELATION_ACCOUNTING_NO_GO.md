# Cycle 233 — Record/Correlation Accounting No-Go

## Target
PDT-II target (4), with consequences for targets (3) and (5): test whether the surviving idea from Cycle 232 — an additive accounting identity splitting distinction among system, environment record, and correlations — follows from PDT refinement/revelation primitives without importing an entropy/divergence calculus.

## Candidate attacked
A natural proposal is that a globally conserved distinction budget admits a scalar decomposition

    D_global = D_S + D_E + D_corr

with nonnegative terms interpreted respectively as locally accessible system distinction, locally accessible environment-record distinction, and distinction hidden in correlations.

## Exact classical counterexample
Use equiprobable hypothesis H in {0,1}. Let the observed variables S,E be deterministic encodings of H.

State A (redundant record):

    H=0 -> (S,E)=(0,0)
    H=1 -> (S,E)=(1,1).

The joint pair (S,E) identifies H perfectly. S alone identifies H perfectly. E alone also identifies H perfectly.

For any normalized perfect-distinction scalar with D(H;S)=D(H;E)=D(H;SE)=1, additive nonnegative accounting would require

    1 = 1 + 1 + D_corr,

hence D_corr=-1, contradicting D_corr >= 0.

Therefore no universal nonnegative additive decomposition of this form can hold for a distinction measure that counts redundant local records at full value.

State B (synergistic/correlation-only record):

Take independent uniform bit R and set S=R, E=R xor H. Then neither S nor E alone contains any information about H, while the pair (S,E) determines H exactly. Thus a correlation/synergy term can be positive even when both local terms vanish.

Together A and B show that overlap/redundancy and synergy have opposite accounting signs. A single universally nonnegative scalar 'correlation remainder' cannot represent both.

## Dimension stress test
The binary constructions embed into every finite alphabet n>=2 by restricting to labels {0,1}. Hence the obstruction is exact for n=2,...,12 and all finite n>=2. n=1 is degenerate. The argument does not depend on Euclidean, trace, or total-variation geometry; it uses only the operational normalization that a perfect binary discriminator has unit value.

## Reversible controlled-environment realization
Both patterns can arise inside reversible classical circuits with explicit ancillas. Redundant records arise by reversible copying of a classical basis label into a blank register (CNOT). Synergistic encodings arise by reversible XOR/one-time-pad style transformations when the random key register is retained. Thus reversibility does not remove the obstruction.

## Surviving statement
Any exact scalar accounting law must explicitly handle overlap/redundancy and synergy, or use a quantity whose algebra already contains inclusion-exclusion/conditional-information structure. Schematically one needs more than

    local + local + nonnegative-correlation.

But once Shannon/von-Neumann mutual information, conditional mutual information, relative entropy, PID-like redundancy/synergy, or a chosen divergence is introduced, the resulting identities inherit that external information calculus and are not PDT-native merely because the terms are renamed 'distinction'.

## Quantum/prior-art boundary
Quantum information already contains system-apparatus-environment information-conservation and information-disturbance relations. The no-hiding theorem additionally gives a specifically quantum restriction when arbitrary quantum-state information disappears from a subsystem: under the theorem's hypotheses it resides in the environment rather than solely in correlations. Quantum Darwinism/discord work also decomposes environment information into classically accessible and nonclassical correlation contributions. These are prior-art boundaries, not PDT novelty.

## Same-input consequence
A PDT-vs-QM prediction cannot count redundant copies as independent conserved distinction units unless the operational task explicitly rewards multiple accessible records. Conversely, a synergistic joint record cannot be credited to PDT while the identical QM comparator is denied joint access. The hypothesis ensemble, registers, allowed joint/local measurements, retained records, and resource window must be identical.

## Status
- Universal nonnegative additive law D_global=D_S+D_E+D_corr for normalized operational distinction: **FALSIFIED**.
- Smallest decisive witness: binary redundant record, n=2: **PROVED**.
- Correlation-only/synergistic witness: binary XOR encoding, n=2: **PROVED**.
- Embedding through n=12 and all n>=2: **PROVED**.
- Shannon/von-Neumann/relative-entropy/PID/no-hiding style accounting: **IMPORTED/KNOWN** unless independently derived from PDT primitives.
- PDT-native signed or lattice-valued refinement/revelation accounting law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Stronger surviving obligation
Do not search next for another scalar conservation slogan. Search for a PDT-native valuation on a refinement lattice/partition structure that distinguishes (i) unique information, (ii) redundant revelation, and (iii) synergistic joint revelation, and prove its composition/refinement law before mapping it to entropy or information theory. Then adversarially test whether the valuation is merely Möbius inversion, inclusion-exclusion, partition entropy, Blackwell order, or partial-information decomposition in disguise.
