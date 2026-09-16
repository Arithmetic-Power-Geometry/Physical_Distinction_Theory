# Cycle 192 — Quotient structure alone cannot force a PDT–QM probability gap

## Status

- **PROVED:** operational quotient invariance theorem below.
- **FALSIFIED:** the claim that the current resource-relative quotient/rank structure by itself forces a same-input probability discrepancy with quantum mechanics.
- **IMPORTED/KNOWN:** operational equivalence under restricted effects and restricted GPT/resource-theory descriptions are established ideas.
- **OPEN:** a genuinely PDT-native response/selection functional that assigns probabilities and differs from the Born rule under an identical microscopic preparation, measurement and declared resource window.
- **BREAKTHROUGH CANDIDATE:** NO.

## Target attacked

PDT-II target (3): construct a same-input quantitative prediction

`P_PDT(O | I,R) != P_QM(O | I,R)`

without changing the microscopic input `I`, measurement/outcome `O`, or resource window `R`.

## Hypotheses

Let `V` be a finite-dimensional real state-vector space and let `E_R <= V*` be the linear span of all effects accessible in the declared resource window `R`. Define

`K_R = intersection_{e in E_R} ker(e)`

and the observable quotient

`Q_R = V / K_R`.

Suppose a theory assigns outcome probabilities only through the accessible effects, i.e. for every allowed outcome effect `e in E_R`, its probability on state `x` is a function of the operational value `e(x)`. This includes ordinary finite-dimensional quantum mechanics restricted to an allowed set of POVM effects: writing Hermitian operators as a real vector space, `e_E(rho)=Tr(E rho)`.

## Theorem — quotient invariance of all declared-resource statistics

If `x-y in K_R`, then every accessible effect has identical value on `x` and `y`:

`e(x)=e(y)` for every `e in E_R`.

Therefore every probability rule that uses only those declared operational effect values is constant on quotient classes `[x] in Q_R`. Equivalently, all such statistics factor through the quotient map `pi_R: V -> Q_R`.

### Proof

By definition, `x-y in K_R` implies `e(x-y)=0` for every `e in E_R`. Hence `e(x)=e(y)` for every accessible effect. Any outcome probability depending only on these accessible operational values is consequently identical on `x` and `y`. Thus the probability assignment factors through `V/K_R`. QED.

## Corollary — no probability-gap theorem from quotient/rank data alone

The tuple `(V,E_R,K_R,Q_R,D(R))`, where `D(R)=dim Q_R`, determines which state differences are invisible to the declared effects, but it does **not** determine a unique probability law on visible outcomes.

In particular, take any quantum preparation `rho`, allowed POVM `{E_o}`, and resource window `R`. The restricted quantum model itself realizes the same quotient construction with

`p_QM(o|rho,R)=Tr(E_o rho)`.

Hence the current PDT quotient/rank axioms admit at least one model whose same-input predictions are exactly quantum predictions. Therefore those axioms cannot logically imply a strict universal inequality

`P_PDT(O|I,R) != P_QM(O|I,R)`.

A strict PDT–QM gap requires an additional PDT-native axiom or derived physical mechanism that fixes a response/selection functional and excludes the restricted-QM realization. Merely relabeling quotient classes, changing norms, or counting quotient dimension cannot do this.

## Minimal decisive witness

A two-outcome classical/quantum diagonal system is sufficient. Let states be probability vectors `(p,1-p)` and accessible effects be coordinate readout. The quotient is already the full one-dimensional normalized state degree of freedom, while the standard outcome probabilities are `(p,1-p)`. The quotient construction contains no equation forcing a different pair. Thus even the smallest nontrivial operational system defeats the assertion that quotient structure itself implies a probability discrepancy.

For `n=3`, take a diagonal qutrit state `rho=diag(p1,p2,p3)` and computational-basis POVM `E_i=|i><i|`. The accessible quotient distinguishes the diagonal probabilities, and restricted QM gives exactly `(p1,p2,p3)`. No current PDT quotient/rank theorem selects a different triple. This directly blocks a non-circular generic `n=3` probability derivation from quotient dimension alone.

## Dimension stress test

The proof is dimension-free. For every finite `n`, including `n=1,...,12`, choose diagonal density matrices and the computational-basis POVM. The resource-restricted quotient is realized inside quantum mechanics itself and all declared effects factor through it. Higher-dimensional embeddings preserve the witness. Degenerate effects only enlarge `K_R`; full tomography makes `K_R` trivial; neither case creates a probability gap.

The argument is independent of norm choice and invariant under simultaneous invertible coordinate changes of states/effects. Product systems likewise inherit the obstruction: product-restricted quantum effects provide a model satisfying the quotient composition law while retaining Born probabilities.

## Edge cases and dynamics

- **Zero resource window:** no nontrivial outcome statistics are declared; no PDT–QM discrepancy follows.
- **Redundant effects:** quotient rank is unchanged; no new response law appears.
- **Full tomography:** `K_R={0}`; state identification improves but probabilities still require the effect pairing/response rule.
- **Pure/mixed states:** both are covered because the proof uses only equality under allowed effects.
- **Markovian/non-Markovian dynamics:** after enlarging the operational state to include whatever history/environment record is declared accessible, the same kernel argument applies to the resulting allowed effects. Dynamics alone does not manufacture a different probability rule.
- **Controlled environment records:** adding records refines `E_R` and can shrink `K_R`; it does not by itself select non-Born probabilities.
- **Thermodynamic costs:** attaching costs to effects does not change the theorem unless a new physical axiom couples cost to outcome response.

## Adversarial alternatives checked conceptually

1. **Different norm on `Q_R`:** cannot force a probability gap because the restricted-QM realization can be equipped with that norm without altering `Tr(E rho)`.
2. **Dimension/count weighting:** imports an extra probability/selection rule and fails to follow from quotient equivalence alone.
3. **Tensor/product quotient:** Cycle 185's conditional tensor quotient can be realized by product-restricted operational models; it does not exclude Born statistics.
4. **Resource refinement:** shrinking the kernel reveals more coordinates but does not specify how an outcome is sampled.
5. **Hidden global sectors:** inaccessible sectors are precisely invisible to `E_R`; they cannot change declared outcome statistics without adding an effect/coupling that makes them accessible.

## Prior-art boundary

Restricted operational/GPT theories explicitly model restrictions on accessible states/effects/measurements; operational equivalence under allowed effects is standard. General resource theories also characterize operational advantages through discrimination tasks. Relevant references include:

- Plávala et al., *Incompatibility in restricted operational theories: connecting contextuality and steering*, J. Phys. A (2022), https://doi.org/10.1088/1751-8121/ac5afe
- Takagi and Regula, *General Resource Theories in Quantum Mechanics and Beyond: Operational Characterization via Discrimination Tasks*, Phys. Rev. X 9, 031053 (2019), https://doi.org/10.1103/PhysRevX.9.031053
- Guff et al., *A Resource Theory of Quantum Measurements*, arXiv:1902.08490, https://arxiv.org/abs/1902.08490

Accordingly, the quotient-invariance mathematics is not claimed as PDT novelty. Its value here is a rigorous **no-go boundary** for PDT-II: quotient/revelation structure cannot be advertised as already predicting deviations from quantum mechanics.

## Consequence for PDT-II

Target (3) remains OPEN but is now sharply constrained. A valid future same-input prediction must supply all of:

1. identical microscopic preparation and measurement specification on both sides;
2. identical declared resource window `R`;
3. a PDT-native, independently motivated response/selection functional;
4. a proof that the functional is not merely Born/GPT probability in disguise;
5. a numerical outcome probability differing from QM for at least one feasible input;
6. counterexample and prior-art screening plus an experimentally measurable inequality.

Until such a functional is derived, `P_PDT != P_QM` is not a theorem of the current quotient framework.
