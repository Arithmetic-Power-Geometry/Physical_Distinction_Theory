# Cycle 163 — Resource revelation is monotone, but naive composite additivity is false

Status: **PROVED / FALSIFIED / IMPORTED-KNOWN / OPEN**

## Target attacked
PDT-II (4): resource-refinement / revelation / conservation laws, with implications for (1) composition.

## Exact hypotheses
Let X be a finite microscopic possibility set. A declared resource window R induces an operational indistinguishability equivalence relation ~_R on X: x ~_R y iff all tests admissible under R give the same operational record on x and y. Let Pi_R = X/~_R be the resulting partition.

Define the finite uniform revelation capacity

C(R) = log2 |Pi_R|.

Say R' refines R when every R'-equivalence class is contained in an R-equivalence class (Pi_R' refines Pi_R).

## Theorem 163A — refinement monotonicity
If R' refines R, then

C(R') >= C(R).

Proof. A refinement cannot have fewer nonempty blocks than the partition it refines. Taking log2 preserves order. QED.

This is rigorous but not claimed novel: it is standard partition/refinement mathematics expressed in PDT language.

## Theorem 163B — exact revelation increment
For nested resource windows R <= R', define

Delta_C(R -> R') = C(R') - C(R) = log2(|Pi_R'|/|Pi_R|) >= 0.

For a chain R0 <= R1 <= ... <= Rk,

C(Rk)-C(R0) = sum_i [C(R_i)-C(R_{i-1})].

This telescoping conservation/chain identity is exact for this capacity definition. It is bookkeeping, not a new physical conservation law.

## Candidate composite law tested
Naive PDT candidate:

C_AB(R_A x R_B) ?= C_A(R_A) + C_B(R_B)

for arbitrary composites, including correlated/restricted state spaces.

### Smallest decisive counterexample
Let A,B each be binary, but restrict the physically allowed joint microscopic set to

X_AB = {(0,0),(1,1)}.

Let local resources reveal the corresponding local bit perfectly. Then

|Pi_A|=2, C_A=1;
|Pi_B|=2, C_B=1;
|Pi_AB|=2, C_AB=1.

Therefore

C_AB = 1 != 2 = C_A + C_B.

So unrestricted additive revelation across composites is **FALSIFIED** already by a 2-state perfectly correlated composite.

The same construction scales: for q perfectly correlated alternatives {(i,i): i=1,...,q}, C_A=C_B=log2 q while C_AB=log2 q, giving an additive overcount log2 q.

## Surviving theorem
Additivity holds under the stronger Cartesian-product hypothesis:

X_AB = X_A x X_B

and product operational equivalence

(a,b) ~_{R_A x R_B} (a',b') iff a ~_{R_A} a' AND b ~_{R_B} b'.

Then Pi_AB is canonically Pi_A x Pi_B, hence

C_AB = log2(|Pi_A||Pi_B|)=C_A+C_B.

Thus PDT composition cannot infer additivity merely from local revelation. It must specify whether the admissible joint possibility set and resource equivalence factorize.

## Dimension stress family n=1..12
For n perfectly correlated binary components

X_n = {0^n,1^n},

each local marginal has capacity 1 bit, while the complete joint restricted set also has capacity 1 bit. Therefore naive additive sum gives n bits and overcounts by n-1 bits for every n=1,...,12 (and all n>=1).

For independent binary product sets X_n={0,1}^n with product equivalence, joint capacity is exactly n bits. Hence both edge families are covered: perfect correlation and full Cartesian independence.

## Prior-art boundary
Partition refinement, quotient/equivalence-class descriptions, logical information based on distinctions, entropy chain rules, mutual information/correlation corrections, and resource theories of distinguishability are established areas. Therefore Theorems 163A/B and the correlation correction phenomenon are **IMPORTED/KNOWN in mathematical content**, although they sharpen PDT's admissible axioms.

Relevant prior-art directions checked this cycle include David Ellerman's partition/logical-information framework and quantum/resource theories of distinguishability (e.g. Wang & Wilde). No PDT novelty is claimed from the generic partition monotonicity or correlation counterexample.

## Consequence for PDT-II
A defensible PDT-native composition principle must include a rule for the joint admissible possibility space and/or a correlation-sensitive correction. The naive law `revelation(composite)=sum revelation(parts)` is dead.

A candidate next quantity is a PDT redundancy/correlation defect

J_R(A:B) := C_A(R_A)+C_B(R_B)-C_AB(R_AB),

but its sign is NOT asserted without hypotheses: alternative composite rules or globally revealing resources can make C_AB exceed the local sum. Prove-or-falsify monotonicity/sign/submodularity only after exact admissibility hypotheses are declared.

## Classification
- Refinement monotonicity: **PROVED; IMPORTED/KNOWN**.
- Nested-chain revelation identity: **PROVED; IMPORTED/KNOWN**.
- Universal composite additivity: **FALSIFIED**.
- Product-factorized additivity: **PROVED; CONDITIONAL**.
- PDT-native correlation/redundancy law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.
