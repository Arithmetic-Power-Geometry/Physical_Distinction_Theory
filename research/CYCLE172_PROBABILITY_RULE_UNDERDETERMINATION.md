# Cycle 172 — Operational distinction equivalence does not determine a probability rule

## Target
PDT-II target (3): derive or falsify the claim that operational distinction equivalence, together with a declared resource window, uniquely determines a PDT-native probability rule and therefore can support a same-input prediction distinct from quantum mechanics.

## Exact hypotheses tested
Let a finite experiment have outcome set O={1,...,n}. Assume PDT supplies only:
1. an operational distinction quotient (which outcomes/preparations are identified or distinguishable under resource window R);
2. normalization and non-negativity of outcome probabilities;
3. invariance under permutations that preserve the declared distinction structure.
No Hilbert-space inner product, Born rule, amplitude rule, or desired PDT-QM discrepancy is imported.

## Theorem 172.1 — Probability underdetermination
For every n>=2, the above data do not uniquely determine P(O|I,R).

### Proof
Take the maximally resolved quotient with n singleton outcome classes and a preparation/resource specification with no nontrivial outcome permutation required to fix the preparation. The distinction structure fixes only the sample space. Every point p=(p_1,...,p_n) in the probability simplex Delta_{n-1} is a normalized nonnegative probability assignment on exactly the same distinction structure. In particular p != q can be chosen while all operational equivalence classes and the resource window remain unchanged. Hence distinction equivalence plus the stated probability axioms is insufficient to select a unique probability law. QED.

The smallest witness is n=2: p=(1/2,1/2) and q=(3/4,1/4) share the same two singleton distinction classes but predict different frequencies.

## Symmetry strengthening and surviving theorem
If the full symmetric group S_n acts transitively on outcomes and the complete preparation/resource specification is invariant under that action, invariance forces p_i=1/n for every i. This is a genuine conditional uniqueness result, but it yields only the uniform distribution in that highly symmetric case; it does not determine probabilities for generic asymmetric preparations.

More generally, symmetry fixes equality of probabilities only within group orbits. If there are k outcome orbits, normalization leaves generically k-1 free orbit weights. Therefore symmetry plus distinction structure is still non-unique whenever k>=2.

## Dimension stress test
The theorem is analytic for all finite n. For n=1 uniqueness is trivial. For every n=2,...,12, Delta_{n-1} has dimension n-1>0, so there are infinitely many probability rules compatible with the same maximally resolved distinction quotient. The obstruction therefore persists beyond n=12 and does not require numerical extrapolation.

Degenerate quotient: if all outcomes are operationally identified, the quotient determines only the probability of the single coarse event (=1), not a unique distribution over hidden fine outcomes. Thus coarse resource windows worsen rather than cure the underdetermination.

## Same-input PDT vs QM consequence
A defensible statement P_PDT(O|I,R) != P_QM(O|I,R) cannot be generated merely by choosing a different point of the compatible simplex. Such a choice would insert the discrepancy. PDT first needs an independently derived probability-selection principle. Conversely, if PDT adopts the Hilbert-space/projector structure together with the noncontextual orthogonal-additivity hypotheses of Gleason-type results in dimension >=3, the Born form is already forced; an alternative same-input rule would then require PDT to violate or replace at least one explicit hypothesis.

The qubit edge case is important: standard Gleason assumptions alone do not force the Born rule in dimension 2, while stronger Gleason-type assumptions (for example POVM or suitable mixture assumptions) can recover it. This means an n=2 deviation is not automatically PDT-native or novel; the additional PDT principle must itself be derived and experimentally meaningful.

## Counterexample catalogue
- C172-01 (smallest): n=2, same singleton partition, p=(1/2,1/2), q=(3/4,1/4).
- C172-02 (generic n): same singleton partition, uniform p_i=1/n versus q_1=1/2 and q_i=1/[2(n-1)] for i>1.
- C172-03 (restricted-resource degeneracy): one coarse equivalence class; arbitrarily many fine distributions induce the same coarse probability 1.
- C172-04 (orbit obstruction): any symmetry action with >=2 outcome orbits permits independent orbit weights subject to normalization.

## Prior-art boundary
This is not claimed as a PDT breakthrough. Gleason's theorem is precisely a uniqueness result obtained only after adding substantial Hilbert/projector and noncontextual additivity structure (dimension >=3). Qubit extensions require strengthened measurement/mixture assumptions. Therefore the negative sufficiency result here is a boundary/diagnostic theorem, not a new probability reconstruction.

Relevant prior art checked in this cycle:
- Gleason theorem / standard projector probability measures: Born form is forced under its hypotheses for Hilbert dimension >=3.
- Wright & Weigert (2018), *A Gleason-type theorem for qubits based on mixtures of projective measurements*, arXiv:1808.08091: recovers Born rule for dimension >=2 using consistent assignments to projective measurements and classical mixtures.
- De Zela (2016), *Gleason-Type Theorem for Projective Measurements, Including Qubits*, Foundations of Physics 46:1293–1306, DOI 10.1007/s10701-016-0020-0.

## Status ledger
- Distinction equivalence + normalization uniquely determines probabilities: **FALSIFIED**.
- Full transitive symmetry + invariant preparation forces uniform probabilities: **PROVED / CONDITIONAL**.
- Generic symmetry determines all probabilities: **FALSIFIED** when >=2 orbits.
- Gleason/Born uniqueness under Hilbert/projector/noncontextual-additivity hypotheses: **IMPORTED/KNOWN**.
- PDT-native probability-selection principle: **OPEN**.
- Same-input quantitative PDT != QM prediction: **OPEN**; no discrepancy may be claimed until such a principle is independently derived.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Attack whether PDT's existing distinction geometry supplies a non-circular probability-selection functional (for example via refinement consistency, composition, continuity, or resource covariance) without smuggling in amplitude-squared/Born structure. Any candidate must be checked first against the binary witness, then n=3 (especially because standard Gleason uniqueness begins at Hilbert dimension 3), then n=4,...,12 and adversarial GPT/simplex alternatives.
