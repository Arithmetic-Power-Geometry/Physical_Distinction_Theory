# Cycle 165 — Relational synergy is real but does not determine composition

Status: **PROVED / CONDITIONAL / FALSIFIED / IMPORTED-KNOWN / OPEN**

## Targets attacked
PDT-II (1) PDT-native composition and (4) resource-refinement/revelation laws.

Cycle 164 showed that the revelation defect J=C_A+C_B-C_AB has no universal sign when joint resources may expose distinctions unavailable locally. A natural repair is to define positive relational synergy

S_R(A:B) := max{0, C_AB-C_A-C_B}

and ask whether S, together with local capacities, determines the joint operational structure.

## Theorem 165A — capacity triple is not composition-complete
The numerical triple (C_A,C_B,C_AB), and therefore J and S, does not determine the joint partition or composition law.

Small decisive witness: X={00,01,10,11}. Let both local resources be blind, so Pi_A=Pi_B={X}, C_A=C_B=0. Consider two different joint resources:

Pi_parity={{00,11},{01,10}},
Pi_first={{00,01},{10,11}}.

Both have two blocks, hence C_AB=1 and S=1. Nevertheless they reveal different physical distinctions: parity versus first-bit value. Their equivalence relations are unequal. Therefore equal local capacities, equal global capacity, equal revelation defect, and equal synergy do not imply equal composite operational structure. QED.

This remains true even if all blocks have equal cardinality. Hence adding block-size entropy does not repair the witness.

## Theorem 165B — arbitrarily many inequivalent structures share the same capacities
On X={0,1}^n with blind local resources, any nonconstant binary label f:X->{0,1} induces a two-block partition (when both fibers are nonempty) with C_AB=1. Distinct labels modulo output relabeling can induce distinct partitions while all have the same capacity triple (0,...,0,1). For n>=2 this already gives multiple inequivalent relational structures; their number grows rapidly with n.

Thus stress testing n=2..12 does not select a unique composition from capacities. The obstruction worsens with dimension rather than disappearing.

## Conditional surviving statement
If PDT specifies the full resource-induced equivalence relation Pi_R, then refinement is composable at the partition level: combining two independently available tests corresponds to the common refinement of their equivalence relations, provided the combined resource is exactly the joint execution of those tests and introduces no additional relational observable.

Under that explicit no-extra-observable hypothesis,

Pi_combined = Pi_R1 meet Pi_R2

(in the convention where meet is common refinement), and its capacity is C=log2(number of blocks). This is rigorous but standard partition-lattice mathematics, not a PDT breakthrough.

## Counterexample-search implications
Scalar summaries such as C, J, S, Shannon entropy, logical entropy, rank, or dimension can agree while operational partitions differ. Therefore a candidate PDT composition principle stated only in terms of one or finitely many coarse scalar summaries must be checked for non-injectivity before it is promoted.

Different norms or reversible groups cannot repair this particular obstruction because the witness is purely operational/combinatorial: no norm is used. Pure/mixed-state or Markovian/non-Markovian embellishments likewise do not select parity versus first-bit partitions without an additional physical rule.

## Prior-art boundary
Partition refinement/lattice structure and indiscernibility partitions are established mathematics and granular-information theory. Quantum information also has established examples where global measurements reveal information unavailable to restricted local measurements. Accordingly, neither relational synergy nor the existence of globally accessible distinctions is claimed as PDT novelty.

## Consequence for PDT-native composition
The next composition target must operate at the level of **which equivalence relation/resources are physically generated**, not merely how many distinctions they reveal. A defensible PDT-native law would need to derive a map

(R_A,R_B, coupling/resource data) -> Pi_AB

from PDT primitives and then survive competing-partition counterexamples. Capacity can be a monotone/output of this map, but cannot define the map.

## Classification
- Capacity/synergy completeness for composition: **FALSIFIED**.
- Smallest decisive witness: **PROVED** (two binary components).
- Common-refinement rule under explicit joint-test/no-extra-observable hypothesis: **PROVED; CONDITIONAL; IMPORTED/KNOWN**.
- PDT-native resource-to-equivalence-relation composition map: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.
