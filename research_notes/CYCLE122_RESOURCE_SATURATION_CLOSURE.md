# Cycle 122 — Resource-saturation closure theorem

## Target
PDT-II targets (1), (2), and (4): determine whether a non-circular resource law can rule out dynamically generated hidden sectors strongly enough to support same-sector composition.

## Exact theorem
Let the microscopic carrier decompose as `A = V ⊕ M`. Let

`Q(v,m) = Q_V(v) + H(m)`,

where `H(m) >= 0` and `H(m)=0` iff `m=0`. For visible inputs `x,y in V`, let `B(x,y)` be a declared composition budget. If

1. `Q(C(x,y)) = B(x,y)` (exact total-budget conservation), and
2. `Q_V(pi C(x,y)) = B(x,y)` (exact visible-budget saturation),

then

`H(hidden(C(x,y))) = Q(C(x,y)) - Q_V(pi C(x,y)) = 0`,

hence `hidden(C(x,y))=0` and `C(x,y) in V`.

**Status: PROVED / CONDITIONAL.** The proof is exact bookkeeping plus faithfulness of `H`.

## Decisive falsification retained
Total conservation alone is insufficient. For any positive budget `B` and any `delta` with `1 <= delta <= B`, the split

`Q_V = B-delta`, `H = delta`

obeys exact total conservation while carrying nonzero hidden resource. The smallest witness is `B=1`, `Q_V=0`, `H=1`.

Thus

`exact total conservation  !=>  same-sector closure`.

**Status: FALSIFIED.**

## Dimension stress test
The deterministic seeded audit covers `n=1..12,16,24,32,48,64,96,128`, 50 trials per dimension (950 total). Frozen result:

- saturation failures: 0
- leaking witnesses under total conservation alone: 934
- smallest leakage budget: 1

The theorem itself is dimension-independent and exact; randomized trials are regression tests only.

## Prior-art boundary
The logical core is not claimed as novel mathematics. Resource theories commonly define nonnegative monotones and free sectors, while ordinary conservation/resource-ledger arguments are standard. Recent resource-theory work also studies families of monotones and inequalities, so the mere existence of a conserved/monotone budget cannot be treated as PDT novelty. The potentially PDT-specific burden is different: derive an independently measurable `Q_V` and an independently justified saturation law from PDT distinction/revelation primitives rather than stipulating them to obtain closure.

Relevant boundary checks include dynamical resource theory of coherence (Saxena, Chitambar & Gour, *Phys. Rev. Research* 2, 023298, 2020) and sequences of resource monotones from modular-Hamiltonian polynomials (*Phys. Rev. Research* 5, 043082, 2023).

## Circularity guard
Visible saturation must not be defined as "whatever part of the total budget remains when no hidden sector is generated." That would restate closure. To become PDT-native, `Q_V` and its saturation equation must be computable/observable without presupposing microscopic same-sector closure.

## Consequence for n=3 route
This theorem supplies a mathematically sufficient bridge to `V x V -> V` only **if** PDT independently derives visible-budget saturation. It therefore does not yet make the downstream `n=3` selector non-circular.

## Classification
- Resource-saturation closure theorem: **PROVED / CONDITIONAL**
- Total conservation implies closure: **FALSIFIED**
- Underlying resource-ledger mathematics: **IMPORTED/KNOWN**
- Stress audit: **NUMERICALLY SUPPORTED**
- PDT-native derivation of visible saturation: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
