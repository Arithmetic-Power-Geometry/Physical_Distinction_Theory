# Cycle 171 — Abstract process preorder boundary

## Target
Attack the strongest surviving PDT-II obligation after Cycle 170: can a PDT-native abstract process preorder be obtained from distinction structure alone strongly enough to determine physical dynamics/composition?

## Setup
Let a finite operational description at resource R be a quotient Q_R=X/~_R. Define a deterministic distinction process as a map f:Q_R -> Q_R'. Define the preorder f \succeq g when g=h∘f for some allowed deterministic postprocessing h. Operationally, g is a garbling/coarse-graining of f.

## Theorem 171.1 — deterministic revelation cannot increase under postprocessing
For finite Q and deterministic f:Q->Y, g=h∘f:Q->Z,

    |im(g)| <= |im(f)|,

hence C(g)=log2 |im(g)| <= C(f)=log2 |im(f)|.

Proof: im(g)=h(im(f)); the image of a finite set under a function cannot have larger cardinality. Equality holds iff h is injective on im(f).

This is exact for every finite dimension/cardinality, hence in particular n=1,...,12 and arbitrary higher finite n. Degenerate cases (constant maps) saturate C=0; reversible relabelings preserve C exactly.

## Theorem 171.2 — composition telescoping / conservation boundary
For a chain f_1,...,f_k with successive deterministic postprocessings, C_0 >= C_1 >= ... >= C_k and

    C_0-C_k = sum_i (C_{i-1}-C_i).

Thus lost deterministic revelation is additive along a declared coarse-graining chain. This is an accounting identity, not a physical conservation law: a controlled environment can retain the discarded label, in which case global revelation need not fall even though the reduced subsystem revelation does.

## Decisive falsification — the preorder does not determine physical cost or dynamics
The same abstract garbling relation g=h∘f can be implemented by physically inequivalent channels/processes with different temperature, Hamiltonian, time, noise, error tolerance, or environmental record. Therefore

    abstract distinction preorder => unique physical process law

is false without an independent physical bridge. Cycle 170 already gives the minimal erasure witness for the cost part. Here the stronger point is structural: the preorder fixes only convertibility/informativeness, not the physical realization.

Likewise the preorder cannot by itself choose a unique composite tensor/product rule: different composite theories may agree on all local garbling relations while differing on admissible joint states/effects or relational resources.

## Prior-art boundary
This monotonicity is an instance of ordinary data processing / garbling and is therefore IMPORTED/KNOWN mathematics, not a PDT breakthrough. Blackwell informativeness orders experiments by garbling; classical and quantum distinguishability resource theories use analogous channel monotonicity. Strong data-processing inequalities further quantify contraction only after a channel/divergence is specified.

## PDT consequence
The defensible PDT-native object can be an operational distinction preorder, but PDT-II still needs an independently motivated bridge specifying at least:

1. admissible physical carriers/states and joint composition;
2. allowed transformations/channels;
3. resource window R (controls, time, energy/temperature, error, records);
4. a probability rule mapping microscopic input plus R to outcomes.

Without these, target (3), P_PDT(O|I,R) != P_QM(O|I,R), cannot be honestly produced: any discrepancy would be inserted through an arbitrary bridge rather than derived.

## Status
- Deterministic postprocessing monotonicity: PROVED; IMPORTED/KNOWN.
- Telescoping revelation-loss identity: PROVED; IMPORTED/KNOWN.
- Interpretation as universal physical conservation: FALSIFIED without closed-system/environment hypotheses.
- Abstract preorder uniquely determines physical cost/dynamics/composition: FALSIFIED.
- PDT-native physical bridge: OPEN.
- Same-input PDT-vs-QM quantitative prediction: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Next strongest attack
Attempt to derive or falsify a PDT-native probability rule from operational distinction equivalence plus explicit resource windows, while checking whether any proposed rule is merely a restatement of classical/GPT/quantum measurement postulates.
