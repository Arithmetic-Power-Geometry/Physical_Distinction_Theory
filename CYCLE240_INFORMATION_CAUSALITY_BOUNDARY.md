# Cycle 240 — Information-Causality Composition Boundary

## Target
PDT-II priority (1): test whether information causality (IC), added after positivity, normalization, no-signalling and exclusivity/LO, can provide the missing PDT-native joint-admissibility/composition law.

## Candidate
For an operational random-access communication task, Alice has data X, sends an m-bit classical message M, and Alice/Bob may share an admissible non-signalling resource. A standard IC form requires Bob's total accessible information gain about Alice's data to be no greater than m bits (with the precise information functional/protocol declared).

## Result
### Provenance
This route is not PDT-native. Information causality was introduced by Pawlowski, Paterek, Kaszlikowski, Scarani and Winter (Nature 461, 1101–1104, 2009; arXiv:0905.2292). It is established quantum-foundations machinery. Recasting accessible information as 'accessible distinction' does not establish PDT provenance.

### Composition-selector failure
Even a principle that sharply bounds nonlocal correlations does not uniquely determine the physical joint state/composite from fixed local data. Ordinary classical product and shared-randomness composites both obey information causality. For each finite n>=2 define

    P_ind(a,b)=1/n^2,
    P_corr(a,b)=delta_{a,b}/n.

They have the same uniform marginals, are classical/local and therefore IC-compatible, yet

    P_ind[a=b]=1/n,
    P_corr[a=b]=1.

Thus IC cannot be a unique composition selector from the local state/resource data. The smallest decisive witness is n=2.

### Dimension stress test
- n=1: degenerate.
- n=2..12: the exact independent/shared-uniform pair above gives distinct IC-compatible composites with identical marginals.
- all finite n>=2: same analytic construction.
Therefore IC cannot select n=3. A special bound or protocol at binary/qutrit dimension is not a derivation of physical dimension 3.

### Prior-art strengthening
Recent work continues to strengthen generalized IC. In particular, Gachechiladze and Miklin, arXiv:2609.10508 (9 Sep 2026), report that generalized IC exactly characterizes quantum correlations in the simplest bipartite Bell scenario (two binary measurements), deriving the Tsirelson–Landau–Masanes criterion. This makes provenance discipline even more important: reproducing such a boundary is not a PDT breakthrough. Earlier Jain, Gachechiladze and Miklin, PRL 133, 160201 (2024), derived polynomial IC inequalities in general bipartite Bell scenarios and tighter constraints in the simplest scenario.

The broader boundary also remains: principles such as macroscopic locality can define sets strictly larger than the quantum set, and almost-quantum correlations historically satisfied many proposed information principles. Hence a PDT composition theorem must specify more than membership in a familiar information-principle set.

### Same-input prediction audit
Importing IC supplies no PDT-vs-QM probability difference because quantum correlations satisfy IC. Choosing different IC-compatible completions for PDT and QM changes the global preparation/composite input and fails the required same-input comparison.

### Information-functional warning
The IC statement is not measure-free: literature shows that changing from Shannon to alternative Renyi information can alter whether the familiar Tsirelson boundary is recovered. A PDT 'distinction information' functional therefore cannot be inserted into IC and assumed to inherit standard results; its operational meaning and theorem must be derived independently.

## Classification
- Information causality mathematics: **IMPORTED/KNOWN**.
- IC as PDT-native principle: **FALSIFIED** (provenance).
- IC as unique composition selector from fixed marginals/local resource data: **FALSIFIED**, with explicit exact classical family.
- Failure of this candidate to select n=3: **PROVED**.
- Same-input PDT != QM prediction from IC alone: **OPEN / not obtained**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving strengthened obligation
A PDT-native composition law must constrain or construct genuinely joint structure from independently motivated PDT primitives in a way that is not merely positivity/normalization/no-signalling, LO/exclusivity, information causality, macroscopic locality, NPA/almost-quantum membership, or another known information-principle reconstruction. Any proposed PDT information functional must first be operationally derived, then tested for data processing, composition, degeneracies and counterexamples rather than substituted into known IC formulas.

## Prior-art references checked
1. M. Pawlowski et al., "Information causality as a physical principle," Nature 461, 1101–1104 (2009), arXiv:0905.2292.
2. P. Jain, M. Gachechiladze, N. Miklin, "Information Causality as a Tool for Bounding the Set of Quantum Correlations," Phys. Rev. Lett. 133, 160201 (2024), arXiv:2308.02478.
3. M. Gachechiladze, N. Miklin, "Information Causality Characterizes the Set of Quantum Correlations in the Simplest Bell Scenario," arXiv:2609.10508 (2026).
4. J. Henson, A. B. Sainz, "Macroscopic noncontextuality as a principle for almost-quantum correlations," Phys. Rev. A 91, 042114 (2015), arXiv:1501.06052.
