# Cycle 080 — Resource visibility dichotomy

## Target attacked
PDT-II targets (3) and (5): can a declared resource restriction by itself generate a same-input quantitative prediction that differs from QM under the same microscopic state and the same resource window?

## Exact hypotheses
Let `Herm_d` be the real Hilbert space of Hermitian operators with Hilbert–Schmidt pairing `<A,B>=Tr(AB)`. For a declared resource window `R`, let `S_R` be the real span of effects operationally accessible in that window. The microscopic quantum input state is `rho`. A candidate resource-induced representative is `sigma`.

The phrase *resource restriction only* means that `R` changes which effects are accessible; it does not silently change the microscopic preparation, dynamics, detector effect, or introduce a new hidden physical variable.

## Theorem — visibility/annihilator dichotomy
For density operators `rho,sigma`, the following are equivalent:

1. `Tr(rho E)=Tr(sigma E)` for every accessible `E in S_R`;
2. `sigma-rho in S_R^perp`.

This is immediate from the definition of the Hilbert–Schmidt annihilator.

Consequences:

- If `S_R` is not informationally complete, nonzero changes can exist in `S_R^perp`, but they are exactly invisible to every experiment available inside the same resource window.
- If `S_R = Herm_d` (informational completeness), then `S_R^perp={0}` and equality on the accessible effects forces `sigma=rho`.

Hence a resource restriction alone cannot produce an experimentally distinctive same-window probability shift while keeping the same microscopic input. A purported shift must come from extra physical structure: modified state/dynamics/effect, a contextual rule, a hidden record, a different resource window, or failure of the operational assumptions already isolated in Cycles 077–079.

## Explicit finite-dimensional witness family
For every `d>=2`, choose a full-rank diagonal state `rho`, diagonal accessible effects, and

`H=(|0><1|+|1><0|)/sqrt(2)`.

Then `H` is Hermitian, traceless, and orthogonal to every diagonal accessible effect. For sufficiently small positive `epsilon`, `sigma=rho+epsilon H` remains a density operator. Therefore all probabilities in the diagonal resource window are unchanged exactly, while the valid effect

`E=(I+H/||H||_op)/2`

outside that resource window separates the two states. This demonstrates both halves of the dichotomy: the hidden direction is real but experimentally unavailable within `R`.

## Stress audit
The executable audit checks `d=1..12,16,24,32,48,64,96,128`. Dimension 1 is degenerate. All 18 nondegenerate cases retained positivity, had maximum accessible probability gap exactly `0.0` in the constructed diagonal resource window, and had a strictly positive outside-resource witness gap. Largest witness gap in the frozen run was `0.08858332371717079`.

The numerical run is regression evidence only; the theorem is linear algebra.

## Prior-art boundary
This is not a breakthrough claim. Informationally complete measurements are standard quantum tomography: a spanning measurement determines the state. Restricted measurements/operator systems naturally induce equivalence classes of states modulo the annihilator of the accessible observables. Generalized Gleason results likewise constrain probability assignments on sufficiently rich effect sets.

Relevant prior art checked in this cycle includes:

- Caves, Fuchs, Manne & Renes, *Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements* (2003), arXiv:quant-ph/0306179.
- Busch, *Quantum states and generalized observables: a simple proof of Gleason's theorem* (1999), arXiv:quant-ph/9909073.
- Barnett, Cresser, Jeffers & Pegg, *Quantum probability rule: a generalisation of the theorems of Gleason and Busch* (2013), arXiv:1308.0946.

## Classification
- **PROVED** — visibility/annihilator equivalence and informational-completeness corollary.
- **FALSIFIED** — resource-restriction-only same-window route to `P_PDT != P_QM` under unchanged microscopic state/effect.
- **NUMERICALLY SUPPORTED** — regression witness family through `d=128`.
- **IMPORTED/KNOWN BOUNDARY** — tomography/operator-system/Gleason framework is established mathematics/physics.
- **BREAKTHROUGH CANDIDATE: NO**.

## Surviving research target
A defensible PDT same-input deviation must now identify a genuinely PDT-native physical variable or law that is not merely an inaccessible quotient direction, and must state exactly how that variable changes an accessible operational probability while surviving coarse-graining, preparation mixing, no-signalling/composition, and prior-art comparison.
