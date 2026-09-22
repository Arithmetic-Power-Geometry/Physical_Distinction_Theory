# Cycle 313 — Resource-Revelation Submodularity Boundary

## Target
PDT-II target (4): resource-refinement / revelation / conservation laws.

## Setup
Fix two operational states x,y and a universe E of admissible probes/effects. For each probe e define its pairwise distinguishing score

    w_e(x,y) >= 0.

For a nonempty finite resource window R subset E define accessible distinction

    D_R(x,y) = max_{e in R} w_e(x,y).

Set D_empty(x,y)=0. This covers the standard restricted-effect distinguishability construction when w_e=|e(x)-e(y)|. No quantum structure is assumed.

## Theorem 313.1 — monotone resource revelation
If R subset S, then

    D_R(x,y) <= D_S(x,y).

**Status: PROVED.** Immediate because the maximization domain only grows.

## Theorem 313.2 — exact diminishing returns / submodularity
For all finite resource windows A,B,

    D_A + D_B >= D_{A union B} + D_{A intersection B}.

Equivalently, for A subset B and a new probe e,

    D_{A union {e}}-D_A >= D_{B union {e}}-D_B.

**Status: PROVED.** Write a=max_{i in A} w_i and b=max_{i in B} w_i and assume without loss a>=b. Then D_{A union B}=a. Since A intersection B subset B, D_{A intersection B}<=b. Hence a+b >= a+D_{A intersection B}. The empty-set convention handles degenerate cases. The diminishing-returns form follows directly because max(0,w_e-D_R) decreases as D_R increases.

## Corollary 313.3 — revelation increment formula
For a newly admitted probe e,

    Delta_e(R) := D_{R union {e}}-D_R = max(0, w_e-D_R).

Thus probe revelation has exact diminishing returns for this max-over-probes resource model.

**Status: PROVED.**

## Dimension / model stress
The proof is dimension-free and depends only on a fixed nonnegative score per admissible probe. Therefore it survives n=1 through n=12 and arbitrary finite/higher-dimensional classical, quantum, or GPT state spaces whenever the restricted-resource distinction is literally a supremum/max over individually available probes. Edge cases (empty windows, duplicate probes, zero-score probes, ties, deterministic states) are included.

## Important boundary / attempted strengthening
This theorem does **not** establish a physical conservation law. It concerns set inclusion of independently available probes. It need not survive resource activation, collective measurements, adaptive protocols, tensor-composite probes, or context-dependent scores, because adding resources can create new joint probes whose score was not present as an element-wise weight beforehand. Therefore no claim of submodularity is made for operational closures R -> cl(R), adaptive trees, or composite-resource generation without an additional closure theorem.

Likewise, telescoping along a nested chain R0 subset ... subset Rk,

    D_Rk-D_R0 = sum_j (D_Rj-D_R{j-1}),

is algebraic bookkeeping, not a physical conservation principle.

## Prior-art / novelty classification
Monotonicity of distinguishability under enlarging an allowed measurement/effect family is standard restricted-measurement/GPT reasoning. The fact that a set function of the form max_{e in R} w_e is monotone submodular is standard combinatorial optimization. Accordingly these results are not promoted as PDT novelty.

- max-over-probe monotonicity: PROVED / IMPORTED-KNOWN mechanism
- max-over-probe submodularity: PROVED / IMPORTED-KNOWN mechanism
- physical conservation law from the above: FALSIFIED as an inference (not implied)
- extension through adaptive/composite closure: OPEN
- PDT-native composition law: OPEN
- non-circular n=3 selector: OPEN
- same-input PDT/QM deviation: OPEN
- BREAKTHROUGH CANDIDATE: NO

## Consequence for PDT-II
A viable PDT-native revelation law must concern how the *operational closure* of resources generates genuinely new distinguishers, not merely the trivial enlargement of a fixed probe set. The next strongest attack should test whether closure-generated distinction obeys any submodular, supermodular, or conservation inequality; explicit activation counterexamples are the first adversarial target.
