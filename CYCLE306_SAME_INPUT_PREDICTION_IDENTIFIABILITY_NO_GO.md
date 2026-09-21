# PDT Cycle 306 — Same-input quantitative prediction identifiability no-go

## Target
Attack PDT-II target (3): obtain a defensible same-input quantitative prediction

`P_PDT(O | I,R) != P_QM(O | I,R)`

under identical microscopic inputs `I` and an explicitly declared resource/measurement window `R`, without importing the desired discrepancy.

## Candidate principle tested
Can the currently retained PDT-II distinction architecture itself determine an outcome-probability map once the microscopic preparation and operational resource family are fixed?

The retained architecture supplies structural constraints on distinction, composition, resource refinement, and coarse-graining, but no independently derived PDT response rule assigning a normalized probability distribution to every preparation-measurement pair.

## Result
**FALSIFIED as a derivation from the current premises.**

The current premises do not identify a unique response map. Therefore they cannot yet imply a same-input numerical deviation from quantum mechanics.

## Exact underdetermination construction
Fix any finite experiment with outcome set `O={1,...,n}`, `n>=2`, microscopic input `I`, and declared admissible resource/measurement window `R`. Let the quantum prediction be

`q=(q_1,...,q_n)`, with `q_i>=0` and `sum_i q_i=1`.

The current PDT structural premises are compatible with the response assignment

`p^(0)=q`.

Whenever the experiment has at least two outcomes that permit an interior perturbation, choose indices `a != b` and sufficiently small nonzero `epsilon` such that

`p^(epsilon)_a=q_a+epsilon`,
`p^(epsilon)_b=q_b-epsilon`,
`p^(epsilon)_j=q_j` otherwise.

Then `p^(epsilon)` is also a normalized probability vector, but `p^(epsilon) != q`.

Nothing in the currently retained dimension-free distinction/composition/refinement premises selects `epsilon=0`, a nonzero `epsilon`, its sign, or its dependence on `I,R`. Thus those premises admit both an empirically quantum-matching completion and empirically deviating completions.

This is an identifiability obstruction, not a proposed alternative physical law.

## Boundary cases
- If `q` is interior, both positive and negative sufficiently small perturbations are available.
- If `q` lies on the boundary, a one-sided transfer from a positive component to another component supplies a valid perturbation whenever `n>=2` and the distribution is not constrained by an independently derived deterministic rule.
- If `q` is a deterministic vertex, one may transfer `epsilon` from its unit component to another outcome; normalization and positivity still hold for `0<epsilon<1`. Such a completion may violate additional physical assumptions, but those assumptions must be stated independently to exclude it.
- `n=1` is degenerate and has no probability-level deviation.
- For every `n=2..12`, the construction is exact; it extends to arbitrary finite `n`.

## Same-input requirement
This no-go keeps `I` and `R` fixed. The ambiguity is not produced by changing a measurement basis, resource budget, microscopic state, or detector model. It arises because a theory needs a response/probability rule in addition to structural constraints on distinguishability.

Therefore a future PDT-vs-QM comparison must specify all of:

1. identical microscopic preparation `I`;
2. identical operational resource/measurement family `R`;
3. the QM response rule for that pair;
4. an independently derived PDT response rule for exactly the same pair; and
5. a parameter-free or independently calibrated numerical difference.

Changing `R`, silently changing the measurement, fitting a free discrepancy parameter to the desired result, or defining PDT probability as 'whatever differs from QM' is circular and inadmissible.

## Relation to known foundations
This boundary is not a novelty claim. Operational/GPT frameworks treat probabilities for preparation-measurement pairs as primitive operational data or as values supplied by a specified state/effect pairing. Quantum mechanics supplies the Born rule. Bell-type tests become experimentally discriminating only after extra physical assumptions imply probability constraints/inequalities different from quantum predictions. Gleason-type results likewise derive the Born form only after substantial Hilbert-space and additivity/noncontextuality structure; importing such structure would not constitute a PDT-native derivation.

Accordingly, the logical underdetermination identified here is **IMPORTED/KNOWN in spirit**; its role is to prevent PDT-II from manufacturing a numerical deviation without a native response law.

## Consequence for PDT-II
The same-input target should now be split into two obligations:

**T3a — Response-law derivation.** Derive a PDT-native map `Phi_PDT:(I,R)->Delta(O)` from independently motivated PDT postulates, with normalization/positivity and consistency under allowed coarse-graining/composition.

**T3b — Empirical separation.** Only after T3a, search for a fully specified `(I,R,O)` for which `Phi_PDT(I,R)` differs numerically from the corresponding QM distribution and survives nuisance/resource matching.

Without T3a, T3b is mathematically underdetermined.

## Status ledger
- Current PDT-II structural premises uniquely determine `P_PDT(O|I,R)`: **FALSIFIED**.
- Current premises imply a nonzero same-input PDT-QM discrepancy: **FALSIFIED**.
- Exact finite-outcome underdetermination construction for `n=2..12`: **PROVED**.
- Extension to arbitrary finite `n>=2`: **PROVED**.
- Operational probability/state-effect and Born-rule background: **IMPORTED/KNOWN**.
- PDT-native response-law derivation: **OPEN**.
- Fully specified parameter-free same-input `P_PDT != P_QM`: **OPEN** pending response law.
- Experimentally distinctive PDT inequality: **OPEN** pending additional PDT-native physical constraint.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Search for a PDT-native response-law postulate that is not merely Born's rule, a renamed GPT state-effect pairing, or an inserted discrepancy parameter. Every candidate must first reproduce normalization and operational consistency, then be adversarially tested on binary systems, `n=3`, `n=4..12`, composites, coarse-graining, restricted resources, pure/mixed states, and sequential/controlled records. Only a surviving independently motivated law can support a legitimate same-input experimental prediction.
