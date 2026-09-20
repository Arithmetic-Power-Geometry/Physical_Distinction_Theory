# Cycle 271 — Non-Markovian distinction-revival no-go

## Target attacked
PDT-II targets (3) same-input quantitative deviation and (5) experimentally distinctive inequalities, with the requested non-Markovian stress test.

## Candidate principle
A temporary increase/revival of operational distinguishability under open-system evolution is a PDT-specific revelation effect and can therefore serve as an experimentally distinctive PDT inequality or same-input departure from quantum mechanics.

## Exact hypotheses
Let rho_0,rho_1 be two system states and Lambda_t a family of reduced dynamical maps. Define D_t = (1/2)||Lambda_t(rho_0-rho_1)||_1. Candidate witness: there exist t2>t1 with D_t2>D_t1.

## Result
**FALSIFIED as a PDT-specific witness.** Standard quantum mechanics with non-Markovian reduced dynamics already permits trace-distance revivals. This is the established Breuer-Laine-Piilo information-flow construction. Hence observing D_t2>D_t1, even with identical declared system inputs, does not imply P_PDT != P_QM unless PDT predicts a quantitatively different value after the full system-environment microscopic input, preparation, Hamiltonian/coupling, initial correlations, readout, and resource window are matched.

The no-go is stronger than a terminology collision: a revival inequality of the form D_t2-D_t1>0 has an explicit QM-allowed model class, so it cannot by itself be an experimentally distinctive PDT inequality.

## Dimension stress test
The obstruction is dimension-independent once a two-dimensional invariant sector is available. A qubit non-Markovian witness embeds isometrically into every n>=2 carrier by acting identically on the orthogonal complement. Therefore the same witness survives n=2,...,12 and all higher finite n under resource-preserving embedding. It cannot select n=3 or establish n<=3.

## Controlled-environment qualification
A reduced-system revival is not automatically evidence of literal environment-to-system information backflow. Recent work distinguishes information revival from genuine causal backflow. Therefore PDT must not equate the two without a controlled-environment/causal condition.

## Prior-art boundary
- Breuer, Laine and Piilo / Laine, Piilo and Breuer: trace-distance information-flow non-Markovianity is established quantum open-systems theory (PRL 103, 210401 (2009); PRA 81, 062115 (2010)).
- Settimo, Breuer and Vacchini (PRA 106, 042212, 2022): trace-distance and entropic non-Markovianity witnesses need not agree.
- Buscemi et al. (2024 preprint): information revival and genuine causal backflow can be distinct.

## Surviving theorem
**PROVED (conditional on resource-preserving sector embedding):** Any PDT inequality whose only positive signature is a revival of a standard quantum distinguishability monotone under reduced non-Markovian dynamics is not PDT-distinctive if standard QM admits the same input-output probability table in the declared resource window.

This does not rule out PDT. It narrows target (5): a viable inequality must exceed a QM-achievable bound under a fully specified same-input microscopic model, rather than merely display non-Markovian distinguishability revival.

## Status ledger
- Trace-distance revival under non-Markovian QM: **IMPORTED/KNOWN**.
- `D(t2)>D(t1)` as uniquely PDT experimental signature: **FALSIFIED**.
- Revival alone implies genuine causal environment backflow: **FALSIFIED as a general inference / prior-art constrained**.
- Revival inequality selects n=3: **FALSIFIED under sector embedding**.
- Quantitative PDT-vs-QM excess under fully matched microscopic inputs: **OPEN**.
- PDT-native composition law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Search for a PDT-native quantitative bound that is not a generic data-processing/revival statement: specify a microscopic controlled-environment model and derive a numerical PDT probability or inequality outside the QM-achievable region without changing hidden inputs or the resource window.
