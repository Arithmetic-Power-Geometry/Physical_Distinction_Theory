# Cycle 246 — Pure-state transitivity + local tomography do not determine PDT composition

## Status

- **PROVED:** the candidate package below is non-selective.
- **FALSIFIED:** `pure-state transitivity + local tomography (+ multiplicative parameter count)` as a unique PDT-native composition selector.
- **FALSIFIED:** the same package as a non-circular selector of `n=3`.
- **IMPORTED/KNOWN:** transitivity, local discriminability/tomography, and operational reconstruction programmes are established GPT/reconstruction ideas.
- **OPEN:** a genuinely PDT-native joint-admissibility predicate.
- **OPEN:** a same-input quantitative PDT/QM deviation.
- **BREAKTHROUGH CANDIDATE:** NO.

## Candidate attacked

Let a finite system have information capacity `n` (maximum number of perfectly distinguishable pure states), real state-space parameter count `K(n)`, reversible group `G_n`, and a standard composite. Consider the proposed structural package:

1. **Pure-state transitivity:** `G_n` acts transitively on pure states.
2. **Local tomography:** joint states are determined by joint local statistics; in finite parameter counting, `K_AB = K_A K_B` for the standard composite.
3. **Dimension-uniformity:** the principles are stated without inserting `n=3`.

Question: does this package uniquely determine a PDT composition law or select `n=3`?

## Theorem (two-family survivor no-go)

The answer is **no**. For every finite integer `n >= 1`, both of the following established theories satisfy the package under their standard composites:

### Classical family C_n

- normalized states form the `(n-1)`-simplex;
- pure states are its `n` vertices;
- permutations `S_n` act transitively on those vertices;
- `K_C(n)=n` in unnormalised finite parameter counting;
- the standard classical composite has `n_A n_B` outcomes, hence
  `K_C(n_A n_B)=n_A n_B=K_C(n_A)K_C(n_B)`;
- ordinary finite classical theory is locally tomographic.

### Complex quantum family Q_n

- normalized states are density operators on `C^n`;
- pure states are rank-one rays;
- unitary transformations act transitively on pure states;
- Hermitian operators have real dimension `K_Q(n)=n^2`;
- the standard tensor product has Hilbert dimension `n_A n_B`, hence
  `K_Q(n_A n_B)=(n_A n_B)^2=K_Q(n_A)K_Q(n_B)`;
- finite-dimensional complex quantum theory is locally tomographic.

For every `n >= 2`, `K_C(n)=n != n^2=K_Q(n)`, so the two survivor families are inequivalent already by parameter count while satisfying the candidate principles. Therefore the principles do not uniquely determine the state space/composition theory.

Moreover, each family exists for every positive integer `n`; consequently the same principles cannot privilege `n=3`.

## Exact stress test

`cycle246_transitivity_local_tomography_no_go.py` checks exactly, using integers only:

- `n=1,...,12`;
- all pairwise composites `n_A,n_B in {1,...,12}`;
- multiplicative local-tomography parameter scaling for both families;
- survival of dimensions other than three;
- inequivalence `K_C(n) != K_Q(n)` for every tested `n>=2`.

The transitivity statements are analytic group facts and are intentionally not represented as numerical evidence: `S_n` maps any simplex vertex to any other, and a unitary can map any unit ray to any other.

The finite checks are regression tests; the proof above covers every finite `n`.

## Smallest decisive witness

`n=2` already suffices:

- classical bit: `K=2`, pure-state reversible action transitive;
- complex qubit: `K=4`, pure-state unitary action transitive;
- both use locally tomographic standard composites.

Thus no high-dimensional pathology is needed.

## Prior-art boundary

This route is not PDT-native. Operational/GPT reconstructions have long used local discriminability/tomography, reversible transformations, distinguishability and related symmetry principles. Chiribella, D'Ariano and Perinotti (Phys. Rev. A 84, 012311, 2011) derive finite-dimensional quantum theory only from a substantially richer axiom package: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, plus purification. Their earlier purification work (Phys. Rev. A 81, 062348, 2010) develops purification as a general operational principle. D'Ariano, Erba and Perinotti (Phys. Rev. A 101, 042118, 2020) further analyse simplicial/classical theories and local discriminability, underscoring that composition structure itself is a nontrivial independent issue.

Therefore relabelling transitivity or local tomography as a distinction principle would not establish PDT novelty.

## Consequence for PDT-II

A surviving PDT composition proposal must contain an independently motivated **joint** restriction that separates survivor theories which already share symmetry and tomography properties. Symbolically, a useful target must do more than

`TransitivePure(G_n) AND LocalTomography(A,B) AND K_AB=K_A K_B`.

It must derive a PDT-native admissibility predicate `J_PDT(A,B,R)` whose content is not merely a renamed reconstruction axiom, and it must be tested against classical, complex/real quantum, Jordan/GPT and restricted-resource alternatives.

No same-input PDT/QM experimental deviation follows from this cycle.
