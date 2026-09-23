# Cycle 340 — Distinction-Monotone Refinement Boundary

Date: 2026-09-23
Branch: `pdt-breakthrough-lab-24x7`

## Targets attacked

Primary PDT-II target (4), resource-refinement/revelation/conservation laws, with consequences for targets (1) composition, (2) non-circular `n=3`, and (3)/(5) same-input experimental discrimination.

## Candidate PDT-native-looking law

Let `D_R(x,y)` denote the operational distinguishability of two preparations `x,y` when only measurements in resource window `R` are admissible. Define

`D_R(x,y) = sup_{M in R} TV(p_M(.|x), p_M(.|y))`,

where `TV` is total-variation distance.

For nested resource windows `R1 subseteq R2`, ask whether a PDT resource-refinement/revelation law follows without importing quantum structure.

## Exact hypotheses

1. A preparation and admissible measurement determine an ordinary outcome distribution.
2. `R1 subseteq R2` means every measurement allowed at `R1` remains allowed at `R2`.
3. `D_R` is defined by the supremum above.
4. No Hilbert space, Born rule, tensor product, preferred dimension, or quantum channel is assumed.

## PROVED theorem — Resource-Refinement Monotonicity

For every pair of preparations `x,y`,

`R1 subseteq R2  =>  D_R1(x,y) <= D_R2(x,y)`.

### Proof

The set over which the supremum defining `D_R1` is taken is a subset of the set over which the supremum defining `D_R2` is taken. A supremum cannot decrease when its feasible set is enlarged. QED.

This is genuinely representation-independent, but the mathematical mechanism is elementary optimization monotonicity and therefore is not by itself a PDT breakthrough.

## PROVED corollary — Revelation increment is nonnegative

Define

`Rev(R1 -> R2; x,y) = D_R2(x,y) - D_R1(x,y)`.

Then `Rev >= 0` for every nested pair `R1 subseteq R2`.

For a chain `R0 subseteq R1 subseteq ... subseteq Rk`, exact telescoping gives

`D_Rk - D_R0 = sum_i [D_R{i+1} - D_Ri]`.

This is an accounting identity, not a physical conservation law. Calling it conservation would overclaim.

## Decisive falsification — refinement does NOT imply strict revelation

Candidate stronger claim:

`R1 proper-subset R2  =>  D_R1(x,y) < D_R2(x,y)` for every distinct `x,y`.

This is false.

### Smallest classical counterexample

Take binary preparations `x=0`, `y=1`. Let `R1` contain the identity readout, which already perfectly distinguishes them, so `D_R1=1`. Let `R2` strictly enlarge `R1` by adding any noisy or constant measurement. Since TV distinguishability is bounded by 1 and `R1` already attains 1, `D_R2=1`. Thus `R1 proper-subset R2` but revelation increment is zero.

### Quantum counterfamily

For any finite Hilbert dimension `n>=2`, choose orthogonal states `rho=|0><0|`, `sigma=|1><1|`. A resource window containing their projective discriminator already attains trace/operational distinguishability 1. Strictly enlarge the measurement set arbitrarily: distinguishability remains 1. Hence strict revelation fails for every `n>=2`, including all `n=2,...,12` and arbitrary higher finite dimensions.

## Dimension stress n=1..12

- `n=1`: no distinct pair exists in the trivial model; strict-revelation claim is vacuous for distinct preparations.
- Every `n=2,...,12`: embed the binary classical pair or two orthogonal quantum states; choose `R1` already containing a perfect discriminator and `R2` a strict enlargement. Then `D_R1=D_R2=1` exactly.
- Higher finite dimensions: the same 2-dimensional embedded construction is an exact adversarial counterfamily, so randomized tests cannot rescue universal strict revelation.

## Composition and n=3 consequences

The proved monotonicity is dimension-agnostic and holds in classical operational theories as well as quantum ones. It therefore cannot select `n=3`, cannot determine a unique tensor/composition rule, and cannot imply a same-input PDT/QM probability gap.

Any stronger PDT theorem must add a nontrivial hypothesis ensuring that the newly admitted measurements separate at least one equivalence class that was unresolved under the smaller resource window. That condition must itself be derived rather than assumed merely to force strictness.

## Prior-art boundary

Distinguishability monotones and their contraction under physical processing are established quantum-information/resource-theory machinery. Wang and Wilde, *Physical Review Research* 1, 033170 (2019), develop asymmetric distinguishability as a resource under quantum channels. Takagi and Regula, *Physical Review X* 9, 031053 (2019), show that discrimination tasks characterize general convex resources, including GPT settings. Salzmann et al., *New Journal of Physics* (2021), develop symmetric distinguishability as a quantum resource. Therefore generic distinguishability monotonicity or resource-language alone is not PDT novelty.

The present resource-window direction is the opposite order from data processing: enlarging the admissible measurement family enlarges an optimization feasible set. The theorem is exact but elementary; novelty would require a PDT-specific nontrivial structure for which measurements become admissible and a new consequence not reducible to standard discrimination/resource theory.

## Status ledger

| Claim | Status |
|---|---|
| Resource-window monotonicity `R1 subseteq R2 => D_R1 <= D_R2` | PROVED |
| Nonnegative revelation increment | PROVED |
| Telescoping revelation identity along nested windows | PROVED |
| Telescoping identity is a physical conservation law | FALSIFIED as an inference / unsupported |
| Strict resource enlargement always gives strict revelation | FALSIFIED |
| Smallest decisive nontrivial witness | `n=2`, exact |
| All `n=2..12` strict-revelation counterfamily | PROVED |
| Generic distinguishability/resource monotonicity | IMPORTED/KNOWN |
| Refinement monotonicity selects `n=3` | FALSIFIED |
| Refinement monotonicity determines PDT composition | FALSIFIED as an inference |
| Refinement monotonicity forces same-input PDT/QM gap | FALSIFIED as an inference |
| PDT-native admissibility dynamics producing nontrivial strict revelation | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Next attack

Do not promote generic monotonicity. The strongest surviving PDT-native route is to define the rule by which physical resources change the admissible measurement equivalence relation, then prove or falsify a *conditional strict-revelation theorem*: strict increase occurs exactly when the refinement splits an unresolved preparation-equivalence class. Test whether that structure yields any composition-sensitive invariant beyond standard Blackwell/discrimination orderings before attempting `n=3` or experimental claims.
