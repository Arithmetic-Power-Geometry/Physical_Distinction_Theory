# Cycle 011 — Non-Markovian Same-Process Lock

## Status

**PROVED + IMPORTED/KNOWN framework mathematics + DECISIVE FALSIFICATION of a candidate route.**

This result is not claimed as historically new process-tensor mathematics and is not a PDT-vs-QM breakthrough.

## Claim

Let a multi-time experiment be specified by a microscopic process `Upsilon`, an intervention sequence/instrument `J`, and a declared resource window represented only by the same classical post-processing kernel `K_R` on observed records. If PDT and standard quantum mechanics use the same `Upsilon`, the same `J`, and the same `K_R`, then

`P_PDT(records | Upsilon,J,R) = P_QM(records | Upsilon,J,R)`.

This holds whether the process is Markovian or non-Markovian.

Equivalently, non-Markovian memory by itself cannot generate a same-input prediction difference. A difference requires at least one genuinely different physical ingredient: process/dynamics, state assignment, intervention/instrument, measurement/effect rule, probability rule, or a resource interaction that physically modifies the experiment.

## Proof

The process-tensor / quantum-comb generalized Born rule maps the pair `(Upsilon,J)` to one unique joint outcome distribution `p`. Under the stated same-input hypothesis, both descriptions therefore produce the same pre-resource distribution:

`p_PDT = p_QM = p`.

Applying the identical resource post-processing gives

`K_R p_PDT = K_R p_QM`.

Hence the resource-window distributions are equal exactly.

The accompanying total-variation statement follows from the standard data-processing inequality for stochastic maps:

`TV(K_R p, K_R q) <= TV(p,q)`.

Thus resource readout processing cannot manufacture or amplify a discrepancy that was absent in the underlying multi-time process.

## Stress tests

The code uses a normalized two-time four-outcome family in which the second-time conditional probabilities explicitly depend on the first-time record when the memory parameter is nonzero. It checks exact PDT/QM equality under identical process assumptions across memory strengths and randomized TV contraction tests for outcome dimensions 1–12 (with a minimum binary outcome space for the `n=1` audit).

The toy family is a software stress test only; it is not claimed as experimental data or as a novel physical model.

## Prior-art boundary

The process-tensor formalism is established quantum open-systems theory: a process tensor is a multilinear map from sequences of interventions to output states/probabilities and is specifically designed to encompass non-Markovian memory. Resource theories for multi-time processes and non-Markovianity are also established. Therefore PDT must not relabel this lock as new process-tensor mathematics.

Relevant current literature checked in this cycle includes:

- Berk et al., *Resource theories of multi-time processes: A window into quantum non-Markovianity*, Quantum 5, 435 (2021), DOI 10.22331/q-2021-04-20-435.
- White et al., *Non-Markovian Quantum Process Tomography*, PRX Quantum 3, 020344 (2022), DOI 10.1103/PRXQuantum.3.020344.
- Garbellini et al., *Uniform process tensor approach for the calculation of multi-time correlation functions of non-Markovian open systems*, Journal of Chemical Physics (2026), DOI 10.1063/5.0331783.

## PDT consequence

The surviving same-input breakthrough target is narrower than before: PDT cannot obtain a quantitative deviation merely by invoking environmental memory or non-Markovianity while retaining the same operational process and interventions. Any candidate deviation must identify the exact physical law or process component that differs and then survive a same-input comparison against the corresponding quantum process prediction.
