# Cycle 208 — Entropy-budget quotient selection no-go

## Target
PDT-II composition / resource-relative distinction selection.

## Candidate principle attacked
Given independently specified microscopic dynamics and a scalar resource budget measured by the Shannon entropy of the accessible quotient under a declared microscopic prior, select an autonomous quotient at that budget. A hoped-for claim would be that replacing crude quotient cardinality by an information-theoretic resource budget removes the Cycle-207 ambiguity.

## Exact hypotheses
Let X={0,1,2,3}, with uniform microscopic prior mu(x)=1/4 and deterministic dynamics f:X->X,

f(0)=0, f(1)=0, f(2)=0, f(3)=3.

A partition Pi is dynamically admissible when it is an exact deterministic lumping: x~Pi x' implies f(x)~Pi f(x'). Define the scalar information budget

B_mu(Pi)=H_mu(Pi)=-sum_{C in Pi} mu(C) log2 mu(C).

Consider

Pi_A={{0,1,2},{3}},
Pi_B={{0,1,3},{2}}.

## Proposition — entropy-budget non-uniqueness
Both Pi_A and Pi_B are exact autonomous quotients and have the identical information budget

B_mu(Pi_A)=B_mu(Pi_B)=H_2(1/4)=0.8112781244591328... bits,

but their induced deterministic quotient dynamics are non-isomorphic.

### Proof
For Pi_A, f maps {0,1,2} into {0,1,2} and {3} into {3}; hence the induced two-state map is (0->0,1->1), with two fixed points.

For Pi_B, f maps both {0,1,3} and {2} into {0,1,3}; hence the induced map is (0->0,1->0), with one fixed point.

Both partitions have block sizes 3+1 under the uniform prior, so their Shannon entropies are exactly equal. Fixed-point count is invariant under relabelling, so the quotient dynamics cannot be isomorphic. QED.

## Dimension stress test
The four-state witness embeds in every n>=4 by adjoining states to the large block and mapping them to 0. For n=4..12 the paired partitions have common block-size profile (n-1,1), identical entropy H_2(1/n), remain exact deterministic lumpings, and retain respectively two versus one quotient fixed points. n<4 is not claimed for this witness.

## Interpretation
A scalar budget based on accessible Shannon information is strictly more meaningful than bare quotient cardinality, but it still cannot in general choose a unique PDT operational quotient. The failure is not numerical and not caused by quotient relabelling.

This does NOT prove that every possible scalar physical resource functional fails; an injective scalar can encode a partition. It proves failure for the natural entropy-budget proposal under the stated hypotheses.

## Prior-art boundary
Shannon rate-distortion theory and the information bottleneck already optimize representations under information/fidelity or relevance tradeoffs. Therefore entropy-constrained representation selection is IMPORTED/KNOWN machinery, not PDT novelty. This cycle's defensible contribution is a PDT-specific no-go boundary for using entropy budget + exact autonomous microscopic dynamics as a sufficient selector.

## Status
- Exact proposition: PROVED.
- Uniqueness of entropy-budget selector: FALSIFIED.
- Shannon entropy / rate-distortion / information bottleneck machinery: IMPORTED/KNOWN.
- General PDT-native resource functional selecting q_R: OPEN.
- PDT-native n=3 derivation: OPEN.
- Same-input P_PDT != P_QM prediction: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Next surviving obligation
A viable PDT selection rule must use independently motivated structure beyond microscopic dynamics plus a one-number information budget—e.g. a physically derived task/relevance observable, intervention geometry, or operational cost functional—and must then be tested for uniqueness without encoding the desired quotient or n=3 result in that added structure.
