# PDT-II Cycle 324 — Bit-symmetry route audit

## Target
Attack the strongest unresolved PDT-II targets without importing the desired conclusion: can a PDT-native-looking symmetry of perfectly distinguishable alternatives select spatial/state dimension `n=3`, uniquely determine composition, or force a same-input departure from quantum theory?

## Candidate principle
**Bit symmetry:** for any two pairs of perfectly distinguishable pure states `(a,b)` and `(c,d)`, there is a reversible transformation taking `a -> c` and `b -> d`.

Status of the principle itself: **IMPORTED/KNOWN**. In GPT literature, bit symmetry is an established operational postulate; it is known to imply self-duality under appropriate assumptions. It is therefore not PDT-native merely by renaming distinguishability.

## Exact adversarial family
For every classical simplex with `n >= 2` pure states, every ordered pair of distinct vertices is perfectly distinguishable. The reversible group contains the full permutation group `S_n`. Given ordered distinct pairs `(i,j)` and `(k,l)`, a permutation exists with `i -> k` and `j -> l`, extendable arbitrarily to the remaining vertices. Hence every finite classical `n`-simplex is bit-symmetric.

Therefore the same candidate principle holds at `n=2,3,4,...`; it cannot select `n=3`.

### n=1 edge case
There is no pair of distinct perfectly distinguishable pure states, so the universal pair condition is vacuous. It supplies no selector.

### Exact stress n=2..12
For each `n`, choose all ordered pairs `(i,j), i != j`. For every source and target ordered pair, define a bijection by mapping the two specified source vertices to the two specified target vertices and bijecting the remaining `n-2` vertices. Thus the condition holds exactly for every `n=2..12`; the proof extends to every finite `n>=2`.

## Decisive falsification
Claim: `bit symmetry => n=3`.

**FALSIFIED.** Smallest nontrivial countermodel: the classical bit (`n=2`) satisfies bit symmetry. Classical simplexes at every finite `n>=2` provide an infinite counterfamily. In particular, `n=4` satisfies exactly the same principle, decisively defeating uniqueness of `n=3`.

Claim: `bit symmetry => unique PDT composite law`.

**FALSIFIED as an inference.** Bit symmetry is a single-system reversible-symmetry property. It does not specify a tensor product, correlated state cone, correlated effect cone, or quantitative composite distinction norm. The previous PDT-II tensor/crossnorm no-go results therefore remain untouched.

Claim: `bit symmetry => P_PDT(O|I,R) != P_QM(O|I,R)`.

**FALSIFIED as an inference.** Quantum state spaces satisfy the relevant bit-symmetry idea as well, so the principle alone cannot force a quantitative deviation from QM under identical microscopic inputs/resources.

## Surviving theorem
**Finite-simplex bit-symmetry no-selector theorem.** Let `Delta_n` be a classical finite simplex with reversible group containing `S_n`, and define perfectly distinguishable pure pairs as ordered distinct vertices. Then `Delta_n` is bit-symmetric for every finite `n>=2`. Consequently, any arity/dimension selector based solely on bit symmetry cannot uniquely select any particular finite `n`, including `n=3`.

Proof: `S_n` is 2-transitive on ordered pairs of distinct elements. QED.

Classification: **PROVED** (elementary group action), while the use/name of bit symmetry is **IMPORTED/KNOWN**.

## Prior-art guard
Known GPT work by Müller and Ududec introduced/studied bit symmetry and its relation to self-duality. This cycle therefore makes **no novelty claim** for bit symmetry or the self-duality consequence. The PDT contribution here is only a negative audit entry: this established route cannot supply the missing PDT-II selector.

## PDT-II ledger after cycle
- PDT-native correlated-composite selector: **OPEN**
- Non-circular PDT-native `n=3` derivation: **OPEN**
- Bit symmetry as `n=3` selector: **FALSIFIED**
- Bit symmetry as unique composition law: **FALSIFIED as an inference**
- Bit symmetry as same-input PDT/QM separator: **FALSIFIED as an inference**
- Finite-simplex all-`n` counterfamily: **PROVED**
- Underlying bit-symmetry literature: **IMPORTED/KNOWN**
- Breakthrough candidate: **NO**

## Next strongest attack
Do not spend further cycles stacking generic reconstruction axioms unless they generate a genuinely PDT-native correlated-composite quantity. Search instead for a selector expressed directly in PDT distinction/refinement operations whose value is fixed independently of dimension, then adversarially test it against classical simplexes, real/complex/quaternionic quantum models, spin factors, injective/projective tensor extremes, and restricted-resource quotients.