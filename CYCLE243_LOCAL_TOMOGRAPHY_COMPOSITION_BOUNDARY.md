# Cycle 243 — Local tomography is not a PDT-native composition selector

## Target attacked
PDT-II target (1), with consequences for targets (2) and (3): can **local tomography** provide the missing independently motivated joint-admissibility/composition law?

## Candidate principle
For systems A and B, a composite is locally tomographic when its global state is uniquely determined by the joint probabilities of local measurement effects. In finite-dimensional GPT language this is commonly represented by the parameter-counting identity

`K_AB = K_A K_B`

when the local effect spaces separate states.

## Exact falsification of the selector claim
Local tomography is an injectivity/reconstructibility requirement once a composite has been specified; it does not uniquely specify the state cone, effect cone, tensor product, dynamics, or physical theory.

Two inequivalent theories already satisfy the same structural identity:

* finite classical n-level theory: `K_A=n`, `K_AB=n^2=K_A^2`;
* finite complex quantum n-level theory: `K_A=n^2`, `K_AB=n^4=K_A^2`.

They are physically inequivalent state-space families despite both being locally tomographic. Therefore local tomography alone cannot be the missing PDT composition selector.

A still more elementary within-class witness is given by the two classical joint distributions

`P_ind(a,b)=1/n^2` and `P_corr(a,b)=delta_ab/n`.

They have identical uniform marginals and both live in a locally tomographic classical composite, but `P_ind(A=B)=1/n` whereas `P_corr(A=B)=1`. Local tomography makes these distinct joint states *detectable* by local-product statistics; it does not choose which state nature prepared.

The smallest nondegenerate witness is n=2. n=1 collapses as required. `cycle243_local_tomography_selector_no_go.py` verifies exact integer/Fraction identities for n=1..12 and performs 200 seeded higher-dimensional checks through n=10000.

## Consequences
1. **Composition law:** FALSIFIED as a unique selector. Local tomography constrains representation/reconstruction, not which admissible composite/state theory is physically correct.
2. **n=3:** FALSIFIED as a selector. The principle holds uniformly across all finite n in both example families; nothing privileges n=3.
3. **Same-input PDT vs QM prediction:** OPEN. A probability difference cannot be manufactured by assigning PDT and QM different unspecified global completions while claiming identical microscopic input.
4. **Resource/refinement laws:** OPEN. Local tomography supplies no PDT-native resource monotone or conservation law by itself.
5. **Distinctive inequality:** OPEN. No new PDT inequality follows from this principle alone.
6. **Gravity/capacity:** OPEN; not imported.

## Prior-art boundary
Local/tomographic locality is established GPT and reconstruction machinery, not PDT-native. Hardy's operational/GPT work treats classical and quantum theories in a common locally structured framework. Barnum and Wilce show that local tomography becomes highly restrictive only when combined with substantial additional hypotheses (Jordan structure/homogeneity-self-duality and a qubit). Real quantum theory is a standard counterpoint: it fails local tomography and has extra global degrees of freedom inaccessible to local measurements. Recent 2026 work continues to study tomographically nonlocal theories, confirming that this is an active established distinction rather than a PDT invention.

Relevant literature checked in this cycle:
- Lucien Hardy, *A formalism-local framework for general probabilistic theories including quantum theory*, arXiv:1005.5164.
- Howard Barnum and Alexander Wilce, *Local tomography and the Jordan structure of quantum theory*, arXiv:1202.4513.
- Roberto D. Baldijao et al., *Tomographically-nonlocal entanglement*, arXiv:2602.16280 (2026).
- Paulo J. Cavalcanti et al., *Decomposing all multipartite non-signalling channels via quasiprobabilistic mixtures of local channels in generalised probabilistic theories*, J. Phys. A 55 (2022) 404001.

## Status ledger
- The statement "local tomography uniquely fixes the PDT composite" — **FALSIFIED**.
- Classical and complex-quantum finite-dimensional families both satisfy the local-tomography parameter identity — **IMPORTED/KNOWN**, with exact regression checks.
- Local tomography does not privilege n=3 — **PROVED** for the displayed finite families and all n>=1.
- The uniform-marginal independent/correlated witness — **PROVED** exactly for every finite n>=2.
- A genuinely PDT-native `J_PDT(A,B,R)` stronger than the previously rejected generic principles — **OPEN**.
- Same-input `P_PDT(O|I,R) != P_QM(O|I,R)` — **OPEN**.
- BREAKTHROUGH CANDIDATE — **NO**.

## Surviving obligation
The next candidate must add independently physical PDT content, not merely reconstructibility of an already chosen composite. In particular, it must specify or derive a restriction on the admissible global cone/couplings/effects from PDT primitives and declared resources, survive n=1..12 plus higher-dimensional stress tests, and be separated from established GPT reconstruction axioms before any novelty claim.
