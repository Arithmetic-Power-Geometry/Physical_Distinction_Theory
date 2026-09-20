# Cycle 276 — Tensorizable f-divergence prior-art collision

## Target
PDT-II target (1): derive a PDT-native composition law rather than importing a known statistical tensorization law.

## Candidate route attacked
A possible route after Cycles 272–275 was to search inside classical/commuting state pairs for a scalar distinction functional D_f whose independent-product value is determined by a fixed low-dimensional algebraic operation on the local values, and then promote that tensorization law as the missing PDT composition principle.

## Prior-art check
This route collides directly with recent prior art:

1. Rodrigo Cruz, Flavio P. Calmon, Qian Yu, **A Complete Characterization of Tensorizable f-divergences**, arXiv:2608.28556 (submitted 28 Aug 2026). The abstract states that, under its adopted notion of tensorization, any possible tensorization formula has a multi-affine form characterized by one parameter and identifies all tensorizable f-divergences.
2. Rodrigo Cruz, Mario Diaz, Flavio P. Calmon, **Tensorization of f-Divergences**, IEEE ISIT 2025, DOI 10.1109/ISIT63088.2025.11195387. This earlier work formalized f-divergence tensorization and obtained necessary conditions / low-degree classifications.
3. Mu, Pomatto, Strack, Tamuz, **From Blackwell Dominance in Large Samples to Rényi Divergences and Back Again**, Econometrica 89 (2021), DOI 10.3982/ECTA17548. It shows, in its setting, that additive divergences satisfying data processing are integrals of Rényi divergences.

## Decisive conclusion
Within the classical f-divergence sector covered by the hypotheses of Cruz–Calmon–Yu, discovering another exact independent-product scalar tensorization formula is not a defensible PDT-native breakthrough. The relevant mathematical classification now exists independently of PDT.

This does **not** prove that no PDT-native composition theorem exists. It proves that the theorem must contain genuinely PDT-specific structure absent from generic f-divergence tensorization — for example, a derivation of the admissible *joint experiment/resource window* from local resource windows, a nonclassical operational quotient, or a theorem linking resource admissibility to composite state/effect structure.

## Relation to prior cycles
- Cycle 272: total variation showed scalar local values need not determine product distinction.
- Cycle 273: Hellinger/Bhattacharyya showed some scalar distinctions do tensorize exactly.
- Cycle 274: a distinct Rényi-derived functional can obey the same probabilistic-sum operation.
- Cycle 275: faithfulness + relabelling + DPI + tensor additivity do not uniquely select a distinction functional.
- Cycle 276: even the broader program of classifying scalar f-divergence tensorization is already substantially/completely occupied by external prior art under explicit hypotheses.

Thus the surviving PDT composition target moves from **find an algebraic scalar tensorization law** to **derive a resource-window composition selector that determines admissible joint experiments/effects and is not reducible to an existing f-divergence/GPT composition theorem**.

## Status ledger
| Claim | Status |
|---|---|
| Generic f-divergence tensorization is a PDT-native unexplored mathematical sector | **FALSIFIED** |
| Existing literature substantially/classificatorily covers exact f-divergence tensorization under stated notions | **IMPORTED/KNOWN** |
| A newly found Hellinger/KL/chi-square/Rényi-like product formula alone can qualify as PDT-II breakthrough | **FALSIFIED** |
| PDT-native resource-window composition selector | **OPEN** |
| Non-circular PDT-native n=3 derivation | **OPEN** |
| Same-input PDT-vs-QM quantitative deviation | **OPEN** |
| BREAKTHROUGH CANDIDATE | **NO** |

## Guardrail for future cycles
Before promoting any candidate composition law, first reduce it on commuting classical states and test whether it is an f-divergence tensorization, monotone transform of one, Rényi/additive-generator law, or known GPT tensor-product choice. If yes, mark the mathematical component IMPORTED/KNOWN and require an additional PDT-native resource/admissibility theorem.
