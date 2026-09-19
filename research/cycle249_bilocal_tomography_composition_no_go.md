# Cycle 249 — bilocal tomography is not a PDT-native composition selector

## Status

- **PROVED:** local/bilocal reconstructibility is logically weaker than specification of the composite state cone/tensor rule.
- **FALSIFIED:** replacing local tomography by bilocal tomography cannot by itself determine a unique PDT composition law.
- **FALSIFIED:** bilocal tomography cannot by itself select `n=3`.
- **IMPORTED/KNOWN:** bilocal tomography and its real-quantum realization are established prior art (Hardy & Wootters, 2012; D'Ariano, Erba & Perinotti, 2020).
- **OPEN:** PDT-native composition law.
- **OPEN:** PDT-native non-circular `n=3` derivation.
- **OPEN:** same-input quantitative `P_PDT(O|I,R) != P_QM(O|I,R)` prediction.
- **OPEN:** experimentally distinctive PDT inequality.
- **NOT PROMOTED:** BREAKTHROUGH CANDIDATE.

## Candidate principle attacked

Candidate: weaken local tomography to **bilocal tomography**: an arbitrary multipartite state is determined by statistics of measurements acting on at most pairs of elementary components, possibly together with one-component statistics.

The hope would be that PDT's primitive distinctions live naturally on pairwise relations and that pairwise reconstruction therefore fixes composition.

## Theorem — tomography/composition separation

A tomography condition constrains which measurement statistics suffice to identify an already-admitted composite state. It does not, without an additional axiom, specify which composite states are admitted, the positive cone, or the tensor/composition product. Therefore bilocal tomography alone cannot be a unique composition rule.

### Proof

Let a theory `T` provide a composite state set `S_T(A1...Am)` and a family `M_<=2` of effects supported on at most two elementary components. Bilocal tomography is injectivity of the evaluation map

`E_T : S_T -> R^{M_<=2}`,  `E_T(s)=(e(s))_{e in M_<=2}`.

Injectivity determines a state *conditional on membership in `S_T`*. It does not determine the domain `S_T`: two different domains can each admit injective evaluation maps. Hence injectivity of `E_T` cannot logically imply a unique state cone or tensor product. QED.

## Exact dimension stress `n=1..12`

Two established theory families already defeat an `n=3` inference:

1. finite classical probability theory is locally tomographic, hence automatically bilocally tomographic, for every finite local alphabet size `n`;
2. finite-dimensional real-vector-space quantum theory is not locally tomographic but is bilocally tomographic (Hardy–Wootters), again with no distinguished `n=3`.

Thus for each `n=1..12`, bilocal reconstructibility is compatible with at least the classical family, and the property continues in arbitrary finite dimension. The smallest nontrivial competitor to `n=3` is `n=2`.

## Adversarial composition check

The prior-art literature contains still stronger counterpressure: operational probabilistic theories with locally classical/simplicial systems can be given nonstandard parallel composition rules, including bilocal-tomographic constructions with entangled pure composites. Thus pairwise reconstructibility is not equivalent to the ordinary classical or complex-quantum tensor product.

This directly attacks the candidate inference

`pairwise distinction sufficiency => unique PDT tensor/composition law`.

The implication is false without further independently derived PDT structure.

## Prior-art boundary

- L. Hardy and W. K. Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, Foundations of Physics 42, 454–473 (2012), arXiv:1005.4870. They formulate bilocal tomography and show real-vector-space quantum theory is bilocally tomographic although not locally tomographic.
- G. M. D'Ariano, M. Erba and P. Perinotti, *Classicality without local discriminability: Decoupling entanglement and complementarity*, Phys. Rev. A 102, 052216 (2020), arXiv:2008.04011. They construct a causal operational theory with classical local systems and a nonstandard composition rule, and give composition results specialized to bilocal-tomographic theories.

Consequently, importing pairwise tomography under PDT terminology is not PDT-native novelty.

## Consequence for PDT-II

The composition target must now specify more than **how many-body measurement records suffice to reconstruct a state**. A viable PDT-native law must independently determine or restrict the admissible joint cone/tensor structure itself and survive comparison with classical, complex-QM, real-QM and nonstandard bilocal GPT composites. Bilocality supplies no non-circular route to `n=3`, no same-input PDT/QM deviation, and no experimental inequality by itself.