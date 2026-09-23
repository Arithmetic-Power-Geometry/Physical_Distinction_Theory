# Cycle 342 — Dynamics versus revelation: contractivity and record-access boundary

## Status
PROVED for the stated operational hypotheses; IMPORTED/KNOWN core data-processing structure. Decisive falsification of an unrestricted dynamics-as-revelation law. Not a breakthrough candidate.

## Setup
For hypotheses/states x,y and an admissible observation family R define

D_R(x,y) = sup_{M in R} TV(p_M(.|x), p_M(.|y)).

Let T be a hypothesis-independent stochastic/CPTP preprocessing map. The postprocessed family is R∘T = {M∘T : M in R}.

## Theorem 342.1 — preprocessing cannot create accessible distinction
If T is an admissible hypothesis-independent channel and every M∘T is an admissible experiment on the original hypotheses, then

D_R(Tx,Ty) <= D_{R'}(x,y),

where R' contains all pullbacks M∘T. In particular, under unrestricted classical measurements TV contracts under stochastic maps, and under unrestricted quantum measurements trace distance contracts under CPTP maps.

Proof: each postprocessed experiment M applied after T is itself the composite experiment M∘T on the original hypotheses. Its TV separation therefore cannot exceed the supremum over the corresponding original admissible family. Taking the supremum over M proves the claim. QED.

## Corollary 342.2 — no universal positive revelation from ordinary Markovian processing
A hypothesis-independent Markov/stochastic or CPTP step cannot be postulated to produce strictly positive distinction revelation for every nonidentical pair. Identity/reversible channels give equality; noisy channels can strictly reduce distinction; complete erasure can map distinct inputs to the same output.

Smallest decisive witness: n=2. Classical bit states δ0,δ1 have TV=1. The binary erasure-to-fixed-output channel T sends both to δ0, hence TV(Tδ0,Tδ1)=0. Quantum analogue: orthogonal |0><0| and |1><1| sent by a replacement CPTP channel to the same fixed density matrix have trace distance 0.

## Dimension stress
The two-state witness embeds in every classical n-level and complex quantum n-dimensional system for n>=2, hence exactly covers n=2,...,12 and arbitrarily high finite n. n=1 is degenerate.

## Theorem 342.3 — apparent revival requires changing effective access or non-divisible reduced dynamics
If a reduced-system distinguishability D(t) increases over an interval, this cannot arise from applying a positive/CPTP divisible intermediate channel to the same reduced hypotheses with the same observation class. At least one assumption must fail: the reduced intermediate map is not contractive/positive-divisible, system-environment correlations or memory invalidate a state-only intermediate description, or the effective observation/resource family has changed (for example, a newly accessible environment record).

This is a boundary statement, not a novel non-Markovianity criterion: trace-distance revival as a witness of information backflow/non-Markovianity is established prior art.

## Controlled environment records
There is no contradiction between global conservation under reversible S+E dynamics and reduced-system loss. Distinction can migrate into correlations/environment records. Granting later access to E is a resource refinement, not distinction creation by the reduced channel. Thus PDT-II must keep two axes separate:
1. physical processing of the hypotheses;
2. refinement of the admissible observation/resource window.
Conflating them can manufacture a false 'revelation law'.

## Consequences for remaining PDT-II targets
- This route does not select a tensor/composition rule.
- It does not select n=3.
- It supplies no same-input PDT-vs-QM probability gap because classical probability and ordinary QM obey the same data-processing boundary.
- Any genuinely PDT-native revelation law must specify what new operational resource becomes accessible and must exceed standard channel distinguishability/data-processing structure.
- No gravity/capacity inference is licensed.

## Classifications
- Operational preprocessing inequality: PROVED; core structure IMPORTED/KNOWN.
- Universal positive revelation under Markovian processing: FALSIFIED.
- Erasure counterfamily n=2,...,12 and all finite n>=2: PROVED.
- Reduced distinguishability revival under a fixed positive/CPTP-divisible intermediate map and fixed observation class: FALSIFIED.
- Revival via changed record access/non-Markovian reduced description: CONDITIONAL / IMPORTED-KNOWN boundary.
- n=3 selection from dynamics/revelation: FALSIFIED.
- Unique PDT composition from this route: OPEN / not implied.
- Same-input PDT/QM discriminator from this route: OPEN / not implied.
- BREAKTHROUGH CANDIDATE: NO.
