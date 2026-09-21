# PDT Cycle 307 — Affine response-law selector no-go

## Target
Attack the strongest prerequisite exposed by Cycle 306: T3a, a PDT-native response law `Phi_PDT:(I,R)->Delta(O)`.

## Candidate principle tested
Could the standard operational consistency requirements themselves select a unique response law?

Assume a finite-dimensional convex preparation space `Omega` and, for each measurement event `e`, require:

1. normalization/positivity: `0 <= p(e|omega) <= 1` and complete measurements sum to one;
2. mixture consistency: for `omega=lambda omega_1+(1-lambda)omega_2`,
   `p(e|omega)=lambda p(e|omega_1)+(1-lambda)p(e|omega_2)`;
3. coarse-graining consistency: probabilities of disjoint merged outcomes add;
4. operational equivalence: the same event functional has the same probability independent of a redundant implementation label.

These are natural consistency requirements for a response law and do not assume quantum Hilbert space.

## Result
**FALSIFIED as a unique PDT response-law selector.**

Mixture consistency forces each event response to be affine on the convex state space. In finite dimensions an affine functional can be represented linearly after adjoining the normalization coordinate. Positivity and the unit-probability bound restrict it to an allowed effect interval. Hence the candidate response law has the generic form

`p(e|omega)=e(omega)`

with `e` an allowed affine effect and complete measurements satisfying `sum_i e_i=u`.

But this is precisely the generic state/effect architecture of convex operational or generalized probabilistic theories. The consistency axioms determine the *form* of operational probabilities once an effect set is supplied; they do **not** select the physical state cone, effect cone, no-restriction rule, tensor product, or a unique numerical pairing for a microscopic PDT input.

Therefore this route does not supply a PDT-native `Phi_PDT` and cannot by itself generate a same-input deviation from QM.

## Exact finite counterfamily
For every `n>=2`, let the normalized state space be the classical simplex

`Delta_(n-1)={p in R^n: p_i>=0, sum_i p_i=1}`.

For any vector `a in [0,1]^n`, define the affine event

`e_a(p)=sum_i a_i p_i`.

Every such event obeys positivity and mixture consistency. A measurement is any finite family `{a^(k)}` satisfying `sum_k a_i^(k)=1` for each `i`. This yields normalized outcome probabilities and is stable under outcome coarse-graining.

There are infinitely many admissible effect choices already for fixed `n`, and the construction exists for every `n=2..12` and arbitrary finite `n`. Thus the operational consistency requirements neither select `n=3` nor a unique response law.

A second family is supplied by quantum state spaces with affine effects `e_E(rho)=Tr(rho E)`, `0<=E<=I`; obtaining this family requires quantum operator/Hilbert-space structure and therefore cannot be counted as a PDT-native derivation.

## Stronger boundary
If PDT postulates convex mixing of preparations and demands that an event probability respect that physical randomization, **affinity is not optional**. Any proposed nonlinear state-only rule must either:

- violate mixture consistency;
- distinguish different decompositions/implementations that represent the same operational preparation; or
- introduce additional physical state variables beyond the convex operational state.

The third possibility is logically open, but then those variables and their dynamics must be independently specified and experimentally matched; they cannot be introduced solely to manufacture a PDT/QM discrepancy.

## n=1..12 and edge cases
- `n=1`: degenerate unique normalized state; no nontrivial probability distinction.
- `n=2..12`: exact simplex/effect construction above supplies a counterfamily.
- arbitrary finite `n`: same proof.
- pure states: simplex vertices are included.
- mixed states: all convex mixtures are included and affinity holds exactly.
- restricted resources: choosing a strict subset of effects preserves the same generic form but changes accessible statistics; consistency still does not select that subset.
- composites: minimal/classical product constructions preserve affine responses, so single-system consistency cannot select a unique tensor rule.

## Prior-art boundary
This is **IMPORTED/KNOWN in substance**. Convex operational/GPT frameworks represent states by convex sets and measurement events by affine/linear effects whose evaluation gives probabilities. Quantum Gleason/Busch-type results obtain the Born form only after adding specifically quantum measurement/operator structure and noncontextual/additivity assumptions. Those stronger assumptions cannot be silently imported as a PDT-native selector.

## Consequence for PDT-II
Cycle 306's T3a is now sharpened further. A viable PDT-native response law must identify, from independent PDT physics, at least one ingredient not fixed by generic convex operational consistency, such as:

- the physical state/effect geometry;
- a principled restriction on allowed effects/resources;
- a composition rule that constrains effects on composites; or
- independently observable additional state variables that make an otherwise nonlinear response operationally well-defined.

Only after such an ingredient is derived can PDT compute a parameter-free same-input probability and test it against QM.

## Status ledger
- Mixture consistency implies affine event probabilities on a convex operational state space: **PROVED / IMPORTED-KNOWN**.
- Normalization + positivity + affinity uniquely select a PDT probability law: **FALSIFIED**.
- Generic affine state/effect representation is PDT-native novelty: **FALSIFIED; IMPORTED/KNOWN**.
- Exact simplex counterfamily for `n=2..12`: **PROVED**.
- Extension to arbitrary finite `n`: **PROVED**.
- Nonlinear response on the same convex operational state while preserving mixture consistency: **FALSIFIED** unless extra physical variables/context are supplied.
- PDT-native selector of state/effect geometry or extra variables: **OPEN**.
- PDT-native response law `Phi_PDT`: **OPEN**.
- Same-input parameter-free PDT/QM deviation: **OPEN**.
- Non-circular `n=3` derivation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Test whether PDT's own distinction primitive can independently restrict the allowed effect set rather than merely define a metric after effects are already supplied. In particular, attempt prove-or-falsify statements connecting operational distinguishability, reversible symmetry and composition to a unique effect cone. Reject any route that simply assumes self-duality, Hilbert-space effects, the Born rule, or `n=3`.
