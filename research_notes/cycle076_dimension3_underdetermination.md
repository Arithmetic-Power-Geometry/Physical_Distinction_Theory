# Cycle 076 — Non-circular n=3 derivation: model-multiplicity no-go

## Status

- **PROVED**: the currently surviving PDT-II structural axioms used here do not entail Hilbert-space dimension `d=3`.
- **NUMERICALLY SUPPORTED**: regression audit over `d=1..12,16,24,32,48,64`.
- **FALSIFIED**: any claim that quadratic revelation plus the present independent-product composition law alone selects `n=3`.
- **OPEN**: discovery of a genuinely PDT-native, independently motivated dimension-selective physical postulate.
- **NOT A BREAKTHROUGH CANDIDATE**: the logical underdetermination principle is general and the operational-reconstruction literature routinely keeps system capacity/dimension as an explicit parameter unless additional postulates constrain it.

## Hypotheses attacked

Take the surviving PDT-II structures already established on this branch:

1. finite-dimensional density states;
2. quadratic distinction energy
   `E_d(rho)=d Tr(rho^2)-1`;
3. orthogonal quadratic revelation / Pythagorean refinement accounting;
4. exact independent-product composition
   `1+E_AB=(1+E_A)(1+E_B)`;
5. ordinary tensor composition for independent systems.

Question: do these structures force `d=3` non-circularly?

## Theorem (model-multiplicity no-go)

They do not.

For every integer `d>=1`, let the state space be the density operators on `C^d`, use the Hilbert-Schmidt quadratic distinction above, and use tensor products for independent composition. Then all five hypotheses hold in that dimension.

### Proof

For every density operator `rho` on `C^d`, the quantity `E_d(rho)` is well-defined. Orthogonal revelation is the ordinary Pythagorean identity in the real Hilbert space of Hermitian operators (or any orthonormal coordinate representation thereof), so it does not single out a particular finite dimension.

For independent states `rho` on `C^d` and `sigma` on `C^e`,

`Tr[(rho tensor sigma)^2] = Tr(rho^2) Tr(sigma^2)`.

Therefore

`1+E_de(rho tensor sigma)
 = de Tr(rho^2)Tr(sigma^2)
 = [d Tr(rho^2)][e Tr(sigma^2)]
 = (1+E_d(rho))(1+E_e(sigma))`.

Thus each `d=1,2,3,...` supplies a model of the same axiom family. Since at least two non-isomorphic dimensions (for example `d=2` and `d=4`) satisfy all hypotheses, those hypotheses cannot logically entail `d=3`.

`QED`.

## Dimension-sensitive diagnostic

For a pure state,

`E_d(|psi><psi|)=d-1`.

Hence the formalism can *report* dimension once dimension is already supplied, but this is not a derivation of `d=3`. Setting `E=2` and solving `d-1=2` would simply hide the desired answer in a dimension-selective numerical premise.

## Stress audit

`cycle076_dimension3_underdetermination.py` tests the identities in dimensions

`1..12, 16, 24, 32, 48, 64`.

A deterministic local run with seed `76076` used 265 randomized cases. Maximum residuals were approximately:

- product composition: `1.7763568394002505e-15`;
- quadratic revelation: `1.9326762412674725e-12`.

The numerical audit is regression evidence only; the theorem is algebraic.

## Prior-art boundary

This no-go is not claimed as a novel foundations theorem. Operational reconstructions of quantum theory commonly reconstruct finite-dimensional quantum structure while retaining a system-size/capacity parameter; additional principles are needed to constrain particular physical systems. Hardy's operational reconstruction, for example, explicitly uses capacity variables such as the maximal number of distinguishable states and reconstructs the quantum relationship between operational parameters rather than deriving that every physical system has dimension three.

Relevant background:

- L. Hardy, *Reformulating and Reconstructing Quantum Theory*, arXiv:1104.2066.
- L. Hardy, *Reconstructing Quantum Theory*, arXiv:1303.1538.

## Consequence for PDT-II

The `n=3` target remains **OPEN**, but the search space is now sharply constrained. A defensible derivation must introduce and independently justify at least one PDT-native premise whose model class excludes `d!=3`. Acceptable examples would have to be genuinely physical rather than algebraic restatements of `d=3`: e.g. a resource/capacity extremum, a composition obstruction, a stability condition, or an experimentally motivated invariant that has a unique solution at three dimensions.

Any future candidate should be rejected as circular if its numerical constant, rank condition, number of generators, number of mutually distinguishable alternatives, or assumed symmetry group already encodes three.
