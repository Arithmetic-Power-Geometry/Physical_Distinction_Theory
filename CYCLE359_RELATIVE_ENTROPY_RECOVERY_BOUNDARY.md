# Cycle 359 — Relative-entropy refinement/recovery boundary

## Target attacked
PDT-II targets (1), (2), (3), and especially (4): whether a resource-refinement/revelation/conservation principle based on distinguishability loss can supply a PDT-native composition law, select n=3, or force a same-input departure from finite-dimensional quantum mechanics.

## Candidate
For density operators rho,sigma and an admissible resource-losing channel Phi, define distinction by Umegaki relative entropy

D(rho||sigma)=Tr[rho(log rho-log sigma)]

when supp(rho) is contained in supp(sigma), and +infinity otherwise. Candidate law:

D(Phi(rho)||Phi(sigma)) <= D(rho||sigma).

Strengthen it compositionally by requiring additivity on independent products and recoverability at equality.

## Exact hypotheses
1. finite-dimensional complex Hilbert spaces;
2. normalized density operators;
3. CPTP maps as admissible processing;
4. finite relative entropy where numerical values are compared;
5. independent composition represented by tensor product.

## Result
**IMPORTED/KNOWN:** quantum relative entropy obeys data processing under CPTP maps in every finite dimension. Equality is tied to recoverability (Petz-type recovery). Relative entropy is additive on product pairs:

D(rho_A tensor rho_B || sigma_A tensor sigma_B)
= D(rho_A||sigma_A)+D(rho_B||sigma_B).

**PROVED (elementary product identity):** the additivity equation follows from log(A tensor B)=log A tensor I + I tensor log B on supports and trace factorization.

**FALSIFIED:** the conjunction {data processing + tensor additivity + equality/recovery structure} does not imply n=3. Complex quantum theory realizes it for every finite n. n=2 is the smallest nontrivial counterexample; n=4 is the smallest higher-dimensional counterexample to uniqueness at 3.

**FALSIFIED AS AN INFERENCE:** these properties alone cannot imply P_PDT(O|I,R) != P_QM(O|I,R) for identical microscopic inputs and the same declared resource window, because ordinary QM itself is a model satisfying the hypotheses.

## Dimension stress test
For n=1,...,12 the structural verdict is dimension-uniform: product additivity and CPTP data processing are available in every n; no n=3 singularity occurs. This is theorem-level rather than a Monte-Carlo claim. Higher finite n follow from the same arguments.

## Edge/degenerate cases
- n=1: distinction is trivial.
- rho=sigma: D=0 and equality is saturated.
- reversible/unitary Phi: relative entropy is invariant.
- replacement/coarse-graining channels can strictly reduce distinction.
- support failure gives +infinity, so finite-value numerical claims require the stated support condition.
- tensoring an identical independent ancilla pair contributes its own additive term; tensoring the same reference state to both hypotheses leaves the original distinction unchanged because D(tau||tau)=0.

## Adversarial counterexample family
Take any finite n>=2, full-rank sigma=I/n, any non-maximally-mixed rho, and Phi a unitary channel. All candidate structural laws hold and equality is saturated. Nothing selects n=3. Taking n=2 or n=4 decisively refutes dimension selection.

For strict contraction, take a replacement channel Phi(X)=Tr(X) tau. Distinct rho,sigma map to the same tau, giving output relative entropy 0 while input relative entropy can be positive. This shows that a naive conservation equality is false even though monotonicity survives.

## Prior-art boundary
Data processing of quantum relative entropy, equality/recovery via Petz-type maps, and recoverability refinements are established quantum-information results. They are not PDT novelty. Recent work also extends sufficiency/recovery questions beyond CPTP maps, reinforcing that merely relabeling this structure as PDT would be a rediscovery.

Representative checks: Carlen & Vershynina, *Recovery map stability for the Data Processing Inequality* (2017), arXiv:1710.02409; Berta, Lemm & Wilde, *Monotonicity of quantum relative entropy and recoverability* (2014), arXiv:1412.4067; van Luijk & Wilming, *Sufficiency and Petz recovery for positive maps* (2026), arXiv:2604.08380.

## Surviving PDT requirement
A PDT-native resource law must contain additional operational content not already implied by standard distinguishability monotones/recovery theory. In particular it must specify a resource-indexed restriction or revelation mechanism that (i) is not satisfied dimension-uniformly by ordinary QM, and (ii) produces a concrete same-input observable difference before it can support target (3).

## Status ledger
- quantum relative-entropy DPI: **IMPORTED/KNOWN**
- product additivity: **PROVED / IMPORTED-KNOWN**
- equality/recovery structure: **IMPORTED/KNOWN**
- these laws => n=3: **FALSIFIED**
- exact conservation under arbitrary resource-losing processing: **FALSIFIED**
- these laws => unique PDT composition: **FALSIFIED AS AN INFERENCE**
- these laws => same-input PDT/QM deviation: **FALSIFIED AS AN INFERENCE**
- stronger PDT-native resource-indexed revelation law: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
