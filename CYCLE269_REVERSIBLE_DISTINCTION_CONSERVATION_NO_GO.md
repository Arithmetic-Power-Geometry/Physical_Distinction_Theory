# Cycle 269 — Reversible distinction conservation is dimension-blind

## Target attacked
PDT-II targets (2) non-circular `n=3` derivation and (4) resource-refinement/revelation/conservation laws, with consequences for (3)/(5).

## Candidate principle
Let `D_R(x,y)` be operational distinguishability under a declared resource window `R`. Consider the proposed conservation package:

1. **Reversible conservation:** for every reversible resource-preserving map `U`,
   `D_R(Ux,Uy)=D_R(x,y)`.
2. **Irreversible monotonicity:** for every allowed coarse-graining/channel `Phi`,
   `D_R(Phi(x),Phi(y)) <= D_R(x,y)`.

Question: can this package select ambient dimension `n=3`, or supply an upper-bound/capacity law needed by PDT-II?

## Exact counterfamily
Take the commuting/diagonal sector of finite-dimensional quantum theory. A state is a probability vector `p` and trace distance reduces to total-variation distance

`D(p,q) = (1/2) sum_i |p_i-q_i|`.

For every finite `n >= 2`:

* every permutation matrix `P` is reversible and preserves `D` exactly;
* every stochastic coarse-graining `S` contracts `D`;
* the same statements hold for quantum trace distance under unitary channels and CPTP maps.

Therefore the conservation/monotonicity package is satisfied in dimensions 2, 3, 4, ... . Dimension 2 is already a counterdimension to necessity of 3; dimension 4 decisively defeats any inferred ceiling `n <= 3`.

The accompanying exact rational regression `tests/test_cycle269_distinction_conservation.py` checks `n=1..12`. For each `n>=2` it uses rational diagonal states, an exact cyclic permutation, and the exact uniformizing stochastic map. `n=1` is retained as the degenerate zero-distinction case rather than counted as positive evidence.

## Proof
Permutation invariance follows because a permutation only reorders the summands of the `l1` norm:

`sum_i |(Pp)_i-(Pq)_i| = sum_i |p_i-q_i|`.

For a column-stochastic map `S`,

`||S(p-q)||_1 <= sum_i sum_j S_ij |p_j-q_j| = sum_j |p_j-q_j| sum_i S_ij = ||p-q||_1`.

Thus total variation is exactly conserved by reversible relabellings and non-increasing under stochastic processing for every finite dimension. The quantum extension is the standard unitary invariance and CPTP contractivity of trace distance.

## Smallest decisive counterexample
`n=2` already obeys both laws nontrivially, so the implication

`reversible distinction conservation + channel monotonicity => n=3`

is false. `n=4` independently shows that these laws do not imply `n<=3`.

## Prior-art boundary
Trace-distance unitary invariance and contractivity under quantum channels are standard quantum-information results. Resource monotonicity under free operations is likewise standard resource-theory structure. Accordingly, neither conservation under reversible free operations nor contraction under irreversible processing is claimed as PDT novelty.

Relevant established literature includes Nielsen & Chuang's treatment of quantum distance measures and the general quantum-resource-theory framework; Brandao and Gour, *Phys. Rev. Lett.* 115, 070503 (2015), DOI 10.1103/PhysRevLett.115.070503, gives a broad reversible resource-theory framework.

## Consequences for PDT-II
A viable PDT-native `n=3` derivation cannot rely only on generic conservation/contractivity of distinguishability. It still needs an independently derived **ambient-sensitive** ingredient that fails above dimension 3, or a genuine PDT capacity ceiling. Likewise, conservation/contractivity by itself changes no microscopic operational primitive, so it cannot produce a same-input probability deviation from QM when state, channel, measurement and resource admissibility are otherwise identical.

## Status

| Claim | Status |
|---|---|
| permutation/reversible conservation of total-variation distinction | PROVED |
| stochastic coarse-graining contraction | PROVED |
| quantum trace-distance unitary invariance/CPTP contractivity | IMPORTED/KNOWN |
| generic resource monotonicity framework | IMPORTED/KNOWN |
| conservation + monotonicity uniquely selects `n=3` | FALSIFIED |
| conservation + monotonicity implies `n<=3` | FALSIFIED |
| PDT-native ambient-sensitive capacity ceiling | OPEN |
| PDT-native composition law | OPEN |
| same-input `P_PDT != P_QM` with an explicitly changed operational primitive | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

No gravity/capacity law is promoted: none was derived in this cycle.
