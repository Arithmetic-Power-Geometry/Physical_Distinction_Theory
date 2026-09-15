# Cycle 166 — Functorial resource consistency still does not determine composition

Status: **PROVED / CONDITIONAL / FALSIFIED / IMPORTED-KNOWN / OPEN**

## Targets attacked
PDT-II (1) PDT-native composition law, with consequences for (2) non-circular n=3 and (4) resource refinement/revelation.

Cycle 165 established that scalar revelation data cannot determine which composite equivalence relation is physically generated. A stronger candidate is therefore natural: require a composite-resource rule to be monotone under local resource refinement, symmetric under exchange, associative across three or more factors, and compatible with local relabelings. Does this structural/functorial consistency uniquely determine the joint operational partition?

## Theorem 166A — functorial consistency is not composition-complete
No. Even on finite classical possibility spaces there are at least two inequivalent composition rules satisfying these structural requirements.

Let each resource R_X induce an equivalence relation E_X on X.

**Rule P (product/local rule).** On X x Y define

(x,y) E_P (x',y') iff x E_X x' and y E_Y y'.

This is the ordinary product partition. It is symmetric up to factor swap, associative under canonical tuple identification, monotone under refinement of either local relation, and equivariant under bijective relabelings.

**Rule B (blind-composite rule).** For every composite with at least two nontrivial factors, define E_B to be the universal equivalence relation: every joint state is operationally equivalent. This rule is likewise symmetric, associative, monotone under arbitrary local refinements, and invariant under all local relabelings.

They disagree already for two binary systems with discrete local resources. Rule P yields four singleton blocks; Rule B yields one block. Hence symmetry + associativity + local-refinement monotonicity + relabeling covariance do not uniquely determine a composite operational relation. QED.

The blind rule is intentionally extreme: its role is adversarial. A uniqueness theorem must exclude it by a physical PDT axiom, not by preference.

## Theorem 166B — adding product distinguishability selects Rule P only conditionally
Assume the stronger hypothesis:

(PD) whenever x is locally distinguishable from x' or y from y', the corresponding product records (x,y) and (x',y') are jointly distinguishable, and no extra relational observable is introduced beyond the paired local records.

Then the joint equivalence relation is exactly E_X x E_Y, i.e. Rule P.

Proof: the no-loss half of (PD) forbids merging different product equivalence classes; the no-extra-relational-observable half forbids splitting a product class. Therefore the classes coincide exactly with Cartesian products of local classes. QED.

This is a valid conditional composition theorem, but its conclusion is essentially encoded in the two halves of (PD). It is therefore **not** yet a non-circular PDT-native derivation.

## Dimension stress test
The witness exists for every n >= 2. For n binary factors with discrete local relations, iterated Rule P has 2^n blocks while Rule B has 1. Both rules remain associative, permutation symmetric, refinement-monotone and relabeling-covariant. Thus n=2..12 and arbitrarily high n do not restore uniqueness.

Degenerate n=1 is identical by construction and therefore cannot distinguish the rules. This explicitly demonstrates why single-system consistency cannot fix composites.

## Alternative-rule stress
Intermediate countermodels also exist: a composition may deliberately retain only a permutation-invariant coarse joint statistic (for example Hamming weight) rather than all local labels. Such rules can satisfy substantial symmetry while differing from both P and B. Therefore excluding only the blind extreme is insufficient; PDT needs a positive physical generation principle.

## Prior-art boundary
The mathematics used here is standard: equivalence relations correspond to partitions and are ordered by refinement; congruence/equivalence relations form lattices, while closure operators are characterized by extensivity, monotonicity and idempotence. Associativity/symmetry/refinement consistency are therefore generic structural constraints, not PDT novelty. The Cycle-166 result is a falsification boundary, not a breakthrough claim.

## Consequence for PDT-II
A PDT-native composition theorem now requires at least one substantive primitive connecting *physical availability of distinctions* across factors. Merely demanding algebraic coherence of the composition operator cannot select it.

The strongest surviving research obligation is to formulate such a primitive without restating the desired product/tensor rule. A promising prove-or-falsify form is a **witness-lifting principle**: every locally realizable distinction witness has a specified resource-bounded lift to a composite witness, with an explicit cost law. Unlike bare product distinguishability, the cost law could potentially make a quantitative PDT prediction. It must be derived and adversarially tested rather than assumed.

## Classification
- Uniqueness from symmetry + associativity + refinement monotonicity + relabeling covariance: **FALSIFIED**.
- Binary smallest witness and all-n family: **PROVED**.
- Product rule under explicit product-distinguishability/no-extra-observable hypothesis: **PROVED; CONDITIONAL; IMPORTED/KNOWN in structure**.
- PDT-native witness-lifting/cost composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input PDT != QM quantitative prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.