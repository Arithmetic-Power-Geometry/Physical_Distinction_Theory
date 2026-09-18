# Cycle 241 — Macroscopic locality does not determine PDT composition

## Target
Test whether macroscopic locality (ML), added to positivity, normalization and no-signalling, can serve as the missing PDT-native joint-admissibility/composition law.

## Status
- Unique PDT composition selector: **FALSIFIED**.
- PDT-native provenance: **FALSIFIED / IMPORTED-KNOWN**.
- n=3 selector: **FALSIFIED**.
- Same-input PDT-vs-QM prediction: **OPEN**.
- Breakthrough candidate: **NO**.

## Exact obstruction
For every finite alphabet size n >= 2 define two zero-input bipartite preparations

P_ind(a,b)=1/n^2,
P_corr(a,b)=delta_{ab}/n.

Both are ordinary classical local correlations. Hence they satisfy no-signalling and any macroscopic-locality requirement obeyed by the local polytope. They also have exactly the same local marginals:

P_A(a)=P_B(b)=1/n.

Nevertheless for the joint event W=[A=B],

P_ind(W)=1/n,
P_corr(W)=1.

Therefore ML cannot determine a unique joint state/composition from the same local data. The smallest nondegenerate witness is n=2. The construction is exact for n=2,...,12 and analytically for every finite n>=2; n=1 is degenerate.

## Stronger prior-art obstruction
Macroscopic locality is not PDT-native. In the established device-independent literature ML corresponds to the first NPA-type outer approximation Q1 rather than the full quantum set. Moreover, the almost-quantum set is strictly supra-quantum while satisfying macroscopic locality together with several other proposed information principles. Thus importing ML, even together with familiar principles already tested in previous cycles, does not provide a novel PDT composition law or uniquely recover quantum composition.

## Same-input discipline
Choosing P_corr as the PDT completion while comparing with P_ind in QM is not a PDT-vs-QM prediction: it changes the global preparation. A legitimate separation still requires identical microscopic preparation I, identical retained records/environment, identical measurement O, and identical declared resource window R, followed by a PDT-native rule yielding a quantitatively different probability.

## Consequence
The surviving composition target must be stronger than positivity + normalization + local consistency + no-signalling + exclusivity/LO + information causality + macroscopic locality, and must be independently derived from PDT primitives rather than imported from NPA/GPT/information-principle machinery.

## Dimension audit
n=1: degenerate, P_ind=P_corr.
n=2..12: exact obstruction above.
n>12 finite: same analytic construction.

## Novelty decision
No breakthrough is claimed. This cycle removes another imported candidate and sharpens the prove-or-falsify obligation.
