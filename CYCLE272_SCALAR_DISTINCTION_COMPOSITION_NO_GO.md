# Cycle 272 — Scalar distinction composition no-go

## Target
PDT-II priority (1): test whether a PDT composition law can be a universal scalar rule

    D_AB = F(D_A,D_B)

where D_X is the operational binary distinguishability of the two local hypotheses and the composite hypotheses are independent products.

## Status
**PROVED (scalar insufficiency); FALSIFIED (universal scalar-only composition); IMPORTED/KNOWN (trace/TV distinguishability framework); OPEN (PDT-native joint admissibility/composition law). BREAKTHROUGH CANDIDATE: NO.**

## Exact hypotheses
Use finite classical systems with total-variation distance

    TV(p,q) = (1/2) sum_i |p_i-q_i|.

This is an admissible commuting sector of finite-dimensional quantum theory, where it equals trace distance for diagonal density operators. For two independent components compare p_A⊗p_B against q_A⊗q_B.

Assume only that a proposed universal composition rule receives the two local scalar distinctions TV(p_A,q_A) and TV(p_B,q_B). No hidden orientation, likelihood-ratio, spectrum, or joint record data are supplied.

## Theorem — local scalar distinctions do not determine product distinction
There is no universal function F:[0,1]^2->[0,1] satisfying

    TV(p_A⊗p_B,q_A⊗q_B)=F(TV(p_A,q_A),TV(p_B,q_B))

for all finite probability distributions.

### Small exact binary counterexample
Write Bernoulli(t) as (t,1-t). In both constructions the local distances are exactly

    D_A = D_B = 1/4.

Witness I:

    p_A = Bernoulli(0),     q_A = Bernoulli(1/4)
    p_B = Bernoulli(0),     q_B = Bernoulli(1/4).

The product distributions are

    p_A⊗p_B = (0,0,0,1)
    q_A⊗q_B = (1/16,3/16,3/16,9/16),

so

    D_AB = (1/2)(1/16+3/16+3/16+7/16) = 7/16.

Witness II keeps the same A pair and reverses the B orientation:

    p_B = Bernoulli(1/4),   q_B = Bernoulli(0).

Then

    p_A⊗p_B = (0,0,1/4,3/4)
    q_A⊗q_B = (0,0,0,1),

so

    D_AB = 1/4.

Thus identical inputs (D_A,D_B)=(1/4,1/4) require two different outputs, 7/16 and 1/4. Contradiction.

## Dimension stress test
The decisive witness is binary and therefore embeds by zero-padding into every classical alphabet dimension n>=2, and as diagonal states into every quantum Hilbert-space dimension n>=2. Hence the obstruction survives n=2,...,12 exactly and all higher finite n under resource-preserving embedding. n=1 is the expected degenerate zero-distinction case.

## Consequences
1. A PDT-native composition law cannot be a function of local scalar distinction values alone.
2. This strengthens Cycle 215: even when each local system has nontrivial operational distinction, retaining only its scalar distinguishability loses composition-relevant information.
3. Any surviving PDT composition candidate must carry richer structure: at minimum oriented hypothesis data / likelihood-ratio structure / spectra / admissible joint effects, or a PDT-native joint admissibility law.
4. The result does **not** imply that no PDT composition law exists; it closes only the scalar-only route.
5. It does not produce a same-input PDT-vs-QM deviation. Introducing a different scalar rule would be an extra primitive unless independently derived.

## Prior-art boundary
Total-variation distance is the classical commuting special case of quantum trace distance. Trace distance is operationally tied to binary state discrimination, is subadditive rather than generally multiplicative on tensor products, and product-state trace-distance behavior is an established quantum-information topic. Fidelity, by contrast, is multiplicative on tensor products. These facts make the broad metric/composition landscape **IMPORTED/KNOWN**; the exact binary witness here is retained as a PDT-II falsification/regression artifact, not claimed as a new external theorem.

Relevant references checked in this cycle:
- M. M. Wilde, *Quantum Information Theory* (2nd ed., 2017), distance/fidelity properties.
- J. Maziero, “Non-monotonicity of trace distance under tensor products,” *Brazilian Journal of Physics* 45 (2015), arXiv:1503.03048.
- IBM Quantum Learning, “Fidelity”: tensor-product multiplicativity of fidelity.

## Classification
- Binary exact counterexample: **PROVED**.
- Universal `D_AB=F(D_A,D_B)` for TV/commuting trace distance: **FALSIFIED**.
- Extension to n>=2 by zero-padding/invariant embedding: **PROVED**.
- General trace-distance / TV framework: **IMPORTED/KNOWN**.
- PDT-native richer joint admissibility/composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input quantitative PDT-vs-QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.
