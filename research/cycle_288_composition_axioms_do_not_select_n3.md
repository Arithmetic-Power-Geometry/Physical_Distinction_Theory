# PDT-II Cycle 288 — composition consistency does not select n=3

## Status

- **FALSIFIED:** generic composition requirements (associativity, a unit object, multiplicative informational capacity, and local tomography) do not derive the distinguished value `n=3`.
- **PROVED:** there are explicit model families satisfying the same composition requirements for every finite `n>=1`, including `n=1,...,12`.
- **IMPORTED/KNOWN:** finite classical probability theory, finite-dimensional complex quantum theory, tensor-product composition, and GPT/reconstruction results concerning local tomography and capacity.
- **OPEN:** a PDT-native axiom that excludes the `n != 3` members without inserting three-dimensionality, an equivalent parameter count, or the desired geometry into the hypotheses.
- **OPEN:** same-input quantitative PDT/QM deviation.
- **BREAKTHROUGH CANDIDATE:** NO.

## Claim attacked

A tempting PDT-II route is that a sufficiently natural composition principle might force the special value `n=3` non-circularly. The following no-go shows that the generic composition package is insufficient.

Let a theory assign each system a finite informational capacity `N`, with a composite rule satisfying:

1. **unit:** `N(A tensor 1)=N(A)`;
2. **associativity:** `(A tensor B) tensor C` and `A tensor (B tensor C)` are operationally equivalent up to the canonical reassociation;
3. **capacity multiplicativity:** `N(AB)=N(A)N(B)`;
4. **local tomography:** composite states are determined by joint statistics of local fiducial measurements.

These hypotheses do not imply `N=3` for an elementary or otherwise distinguished system.

## Exact countermodel family 1: classical probability theory

For every integer `n>=1`, take the state space to be the simplex `Delta_(n-1)` of probability distributions on `n` perfectly distinguishable outcomes. Compose two systems by the ordinary Cartesian product of outcomes. Then

`N(n tensor m)=nm`.

The unit is the one-outcome system. Cartesian product is associative up to canonical relabelling. A joint classical distribution is determined by the probabilities of product outcome effects, so the finite classical model is locally tomographic. Nothing in the four hypotheses selects `n=3`; `n=2,3,4,...` all occur in the same theory.

## Exact countermodel family 2: finite-dimensional complex quantum theory

For every integer `n>=1`, take `H_n = C^n`, density operators as normalized states, POVM effects as measurements, and the standard tensor product. Then

`H_n tensor H_m ~= H_(nm)`

and the maximum number of perfectly distinguishable states multiplies: `N_nm=nm`. The one-dimensional Hilbert space is a unit, tensor product is associative up to canonical unitary equivalence, and finite-dimensional complex quantum theory is locally tomographic because product operator bases span the Hermitian operators on the composite.

Again the same structural laws hold for `n=1,...,12` and for arbitrary finite `n`; they do not select `3`.

## Dimension stress table

| n | classical simplex exists | complex quantum system exists | unit/associativity compatible | local tomography compatible |
|---:|:---:|:---:|:---:|:---:|
| 1 | yes | yes | yes | yes |
| 2 | yes | yes | yes | yes |
| 3 | yes | yes | yes | yes |
| 4 | yes | yes | yes | yes |
| 5 | yes | yes | yes | yes |
| 6 | yes | yes | yes | yes |
| 7 | yes | yes | yes | yes |
| 8 | yes | yes | yes | yes |
| 9 | yes | yes | yes | yes |
| 10 | yes | yes | yes | yes |
| 11 | yes | yes | yes | yes |
| 12 | yes | yes | yes | yes |

This is stronger than a numerical stress test: the constructions are exact for every finite `n`.

## Smallest decisive counterexample

If the proposed theorem says the generic package uniquely forces `n=3`, `n=2` already defeats it. A classical bit and a complex qubit both satisfy the relevant family-level composition framework without having capacity three. Thus no higher-dimensional search can repair the implication unless an additional hypothesis excludes these models.

## Why this matters for PDT-II

This closes a broad class of circular `n=3` derivations. PDT cannot obtain three merely from tensor consistency, multiplicative capacity, associativity, or local tomography. Any successful derivation needs an additional independently physical PDT-native principle `P` such that:

`composition package + P => n=3`,

while `P` itself must not mention `3`, an equivalent three-component representation, a preselected three-dimensional rotation group, or a parameter count already encoding the conclusion.

The falsification also prevents using ordinary quantum tensor structure as evidence for a PDT-specific value of `n`: standard complex quantum theory realizes the same tensor structure at every finite Hilbert dimension.

## Prior-art gate

This is a PDT boundary result, not a novelty claim about GPTs or quantum reconstruction. Hardy-style reconstructions explicitly distinguish informational capacity from the number of state parameters and use additional operational postulates beyond composition/local tomography. Standard GPT literature treats classical and quantum systems of arbitrary finite capacity and their composites. Consequently the countermodels and tensor/local-tomographic facts are **IMPORTED/KNOWN**; the contribution here is to use them as a decisive falsification test for this specific remaining PDT-II route.

Representative background:

- Lucien Hardy, *Reformulating and Reconstructing Quantum Theory*, arXiv:1104.2066 (2011): operational reconstruction with information locality, tomographic locality, compound permutability, sharpness and sturdiness.
- Lucien Hardy, *A formalism-local framework for general probabilistic theories including quantum theory*, arXiv:1005.5164 / Math. Struct. Comp. Sci. 23 (2013).
- Hardy & Wootters, *Limited Holism and Real-Vector-Space Quantum Theory*, arXiv:1005.4870 (2010), for the role and non-universality of local tomography.

## Surviving target

Do not spend further cycles trying to obtain `n=3` from generic tensor/composition consistency alone. The next strongest obligation is to formulate candidate PDT-native operational principles that make a nontrivial exclusion among the exact `n=1,...,12` countermodel family, then adversarially test whether each principle is independent, non-circular, already known in reconstruction/GPT theory, or inconsistent. In parallel, any claimed same-input PDT/QM prediction must specify identical microscopic preparation, controls, admissible effects, environment records, and resource window before a probability difference is meaningful.
