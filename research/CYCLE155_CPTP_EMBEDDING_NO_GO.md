# Cycle 155 — CPTP-Embedding No-Go for a Claimed PDT-vs-QM Probability Deviation

## Status

- **PROVED (mathematical implication):** Any finite-dimensional PDT resource-window map that is CPTP is itself an admissible quantum channel.
- **FALSIFIED:** `Lambda_R^PDT != Lambda_R^baseline` by itself is sufficient to establish a beyond-QM prediction.
- **IMPORTED/KNOWN:** Kraus/Stinespring representation of CPTP maps; quantum-channel operational/resource theory.
- **OPEN:** A PDT-native law that fixes `Lambda_R^PDT` from the same declared microscopic input/resource window and yields either (a) a parameter-free disagreement with a separately fixed QM microscopic model, or (b) an operational point outside the quantum-admissible set while preserving the required consistency conditions.
- **BREAKTHROUGH CANDIDATE:** NO.

## Theorem — CPTP embedding obstruction

Let `H` be finite dimensional. Suppose PDT assigns to a declared resource window `R` a linear map

`Lambda_R^PDT : L(H) -> L(H)`

that is completely positive and trace preserving. Then there exist an environment `E`, an environment state (pure after purification if desired), and an isometry/unitary dilation such that

`Lambda_R^PDT(rho) = Tr_E[V_R rho V_R^dagger]`

(or equivalently the standard unitary-plus-environment form). Therefore `Lambda_R^PDT` is already a quantum-mechanically admissible open-system evolution.

For every quantum effect `0 <= E_O <= I`,

`P_PDT(O|I,R) = Tr[E_O Lambda_R^PDT(rho_I)]`

is consequently a probability obtainable inside ordinary quantum mechanics using that channel.

### Consequence

A numerical inequality

`P_PDT(O|I,R) != P_QM_baseline(O|I,R)`

can falsify a *specified baseline channel/model*, but it does **not** by itself falsify quantum mechanics if `Lambda_R^PDT` remains CPTP. Quantum mechanics contains both channels unless the microscopic controls independently fix which channel must occur.

Thus target (3) needs a stronger benchmark discipline:

1. same externally declared preparation/input;
2. same controlled microscopic Hamiltonian/couplings/environment assumptions (to the extent experimentally fixed);
3. same resource-window definition and readout effect;
4. no PDT-only fitted parameter introduced after seeing the outcome;
5. derive the QM baseline and PDT law independently from those inputs;
6. if the PDT map is CPTP, label disagreement as **model-level** unless the controls uniquely fix the QM channel;
7. reserve **beyond-QM** for an operational prediction outside the quantum-admissible set (or a contradiction with a quantum prediction uniquely fixed by the same microscopic assumptions).

## Why Cycle 154 was not yet enough

Cycle 154 proved equality when state, physical channel, effect and probability pairing are identical. It left open the route `Lambda_R^PDT != Lambda_R^QM`. Cycle 155 shows that merely choosing a *different CPTP* `Lambda_R^PDT` still does not create a beyond-QM theory: Stinespring embeds that map in standard quantum mechanics. Hence a PDT resource-to-channel law must do more than generate a different CPTP map; it must be independently forced by PDT primitives and confronted with a QM channel independently fixed from the same microscopic controls.

## Adversarial examples

Amplitude damping, dephasing, depolarizing, erasure-to-fixed-state, mixtures of unitaries, and non-Markovian reduced dynamics at a fixed input-output time can all produce probabilities different from a chosen identity/unitary baseline while remaining quantum channels. Such differences demonstrate model misspecification or additional environment/resource coupling, not a quantum violation.

The obstruction is dimension independent in finite dimensions, hence covers the requested stress range `n=1..12` and higher dimensions structurally; randomized dimension tests cannot overturn the representation theorem.

## Experimental implication

The next defensible PDT-II task is not to search freely for `P_PDT != P_QM`. It is to derive a PDT-native resource law that maps the *same independently measurable controls* to a channel/effect constraint, then determine whether the resulting operational region is strictly smaller/different than the quantum region. A useful experimental inequality must separate these regions and include nuisance/environment bounds so an ordinary CPTP explanation cannot absorb the deviation.

## Prior-art boundary

This cycle claims no novelty for the channel representation theorem. The standard prior-art boundary is Stinespring/Kraus quantum-channel theory. Operational resource theories of channels likewise treat channel properties and discrimination advantages within the quantum-channel set. PDT novelty, if any, must enter through a new physically derived constraint or operational region, not through relabeling an arbitrary CPTP channel as PDT.

References checked for boundary: Kretschmann, Schlingemann & Werner, IEEE Trans. Inf. Theory 54 (2008), on Stinespring representation/continuity; Li, Bu & Liu, Phys. Rev. A 101, 022335 (2020), operational resource content of quantum channels; Saxena, Chitambar & Gour, Phys. Rev. Research 2, 023298 (2020), dynamical resource theory of coherence.
