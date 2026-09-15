# Cycle 158 — POVM/instrument escape boundary

## Status

- Same single-time POVM statistics determine the full measurement process: **FALSIFIED**.
- Same POVM plus unspecified post-measurement dynamics is sufficient for a same-input PDT-vs-QM deviation: **FALSIFIED as a comparison protocol**.
- Full-instrument equality implies equality of every sequential experiment built from the same preparations, intermediate controls and final effects: **PROVED (standard operational composition)**.
- PDT-native instrument law distinct from the quantum-admissible instrument set: **OPEN**.
- Breakthrough candidate: **NO**.

## Smallest decisive witness

Use a qubit and the two-outcome projective POVM

E_0 = |0><0|,  E_1 = |1><1|.

Define two instruments with identical outcome effects:

I^L_a(rho) = E_a rho E_a,

I^F_a(rho) = X^a E_a rho E_a X^a,

where X is Pauli-X and a in {0,1}. For every input rho,

Tr I^L_a(rho) = Tr(E_a rho) = Tr I^F_a(rho),

so the first measurement has exactly the same outcome probabilities. But for input |1><1| and outcome a=1,

I^L_1(|1><1|) / p(1) = |1><1|,

I^F_1(|1><1|) / p(1) = |0><0|.

A subsequent Z measurement therefore distinguishes the instruments with certainty: the Lüders instrument returns Z=1, while the conditional-flip instrument returns Z=0.

Thus equality of POVM effects does not fix sequential probabilities or back-action.

## Consequence for PDT-II target (3)

A claimed PDT/QM difference in a sequential or feedback experiment is not a same-input comparison if the comparator fixes only the initial state and POVM effects while leaving the instrument/back-action unspecified. The microscopic input specification must include, or independently determine, the relevant quantum instrument (or an experimentally complete implementation model).

Conversely, if PDT and QM use the same preparation, the same sequence of instruments/channels, the same classical conditioning, and the same final effects, their sequential probabilities are identical by direct composition. Hence a genuine PDT deviation must derive a physical instrument/process outside, or more constrained than, the quantum-admissible instrument/process set under the same externally specified controls.

## Prior-art boundary

This is not claimed as PDT novelty. Quantum instruments are the standard formalism that jointly describes outcome probabilities and post-measurement state change; distinct instruments may induce the same POVM. Recent work studies instrument incompatibility and simulation precisely because the instrument contains operational information beyond the induced POVM/channel.

Relevant literature checked in this cycle:

- L. Leppäjärvi and M. Sedlák, *Incompatibility of quantum instruments*, Quantum 8, 1246 (2024), DOI 10.22331/q-2024-02-12-1246.
- S. Khandelwal and A. Tavakoli, *Simulating Quantum Instruments with Projective Measurements and Quantum Postprocessing*, Phys. Rev. Lett. 135, 040202 (2025), DOI 10.1103/bhr5-g71p.
- S. Manna et al., *Single-shot distinguishability and antidistinguishability of quantum measurements*, Phys. Rev. A 111, 022221 (2025).

## Surviving obligation

The strongest target is now:

1. specify PDT's primitive laboratory controls and declared resource window;
2. derive a PDT-native full instrument/process tensor from those controls without inserting the desired deviation;
3. derive the quantum instrument/process independently from the identical controls;
4. search for a parameter-free inequality or probability gap that cannot be absorbed into ordinary quantum instrument freedom, environment records, detector memory, or feedback;
5. only then promote an experimental distinction.

Classification: **PROVED / FALSIFIED / IMPORTED-KNOWN / OPEN**.
