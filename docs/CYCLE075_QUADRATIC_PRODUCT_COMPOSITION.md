# Cycle 075 — Quadratic product composition and its correlation boundary

## Status

**PROVED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED + FALSIFIED(nonnegative universal correlation residual).**

This cycle attacks PDT-II target (1), using the quadratic revelation geometry isolated in Cycle 074. It does **not** claim a historical breakthrough: purity, Hilbert–Schmidt norm multiplicativity on tensor products, linear/Tsallis-2 entropy, and their product-state pseudo-additivity are established mathematics/physics.

## Exact product law

For a density state `rho` on dimension `d`, define the dimension-normalized quadratic distinction energy

`E_d(rho) = d Tr(rho^2) - 1 = d ||rho - I/d||_2^2`.

Hence `E_d>=0`, with `E_d=0` at the maximally mixed state and `E_d=d-1` on pure states.

For independent product states `rho_AB=rho_A tensor rho_B`,

`1+E_AB = d_A d_B Tr(rho_A^2) Tr(rho_B^2) = (1+E_A)(1+E_B)`.

Therefore

`E_AB = E_A + E_B + E_A E_B`.

The induced binary law `x o y=x+y+xy` is commutative, associative, has identity 0, and is linearized by

`C(rho)=log(1+E_d(rho))=log(d Tr(rho^2))`,

for which `C(rho_A tensor rho_B)=C(rho_A)+C(rho_B)`.

This gives an exact closed scalar composition law for **independent product states**. It does not solve correlated composition.

## Decisive correlated-state falsification

Define the residual relative to the product baseline of the actual marginals,

`K_AB = E_AB - E_A - E_B - E_A E_B`.

A tempting PDT interpretation would call `K_AB` a nonnegative correlation-distinction energy. That statement is false.

### Smallest negative witness

Use the diagonal two-qubit state with classical joint probabilities

`P = [[0,1/5],[1/5,3/5]]`.

Its joint purity is `11/25`; each marginal is `(1/5,4/5)` and has purity `17/25`. Thus

`E_AB = 4(11/25)-1 = 19/25`,

`E_A=E_B=2(17/25)-1=9/25`,

and therefore

`K_AB = 19/25 - 9/25 - 9/25 - 81/625 = -56/625 < 0`.

This witness is purely classical/commuting, so negativity cannot be blamed on quantum phase or entanglement.

Embedding the same 2x2 probability block in any local dimension `n>=2` gives exactly

`K_AB = -14 n^2 / 625 < 0`.

### Positive witness

For a maximally entangled pure state in local dimension `n>=2`, the marginals are maximally mixed, so `E_A=E_B=0` while `E_AB=n^2-1`. Therefore

`K_AB=n^2-1>0`.

Thus the residual is sign-indefinite in every local dimension `n>=2`; `n=1` is degenerate.

## Consequence for PDT-II

The quadratic Cycle-074 geometry now supplies a defensible exact **product-sector** composition law, but not a universal scalar correlated-composition law. In particular:

1. product composition is closed under `E_A o E_B=E_A+E_B+E_AE_B`;
2. `log(1+E)` is exactly additive on independent products;
3. arbitrary correlated composites require additional state information beyond `(E_A,E_B)`;
4. the correction cannot universally be a nonnegative scalar correlation energy;
5. any PDT-native correlated extension must retain signed/contextual higher-order information (for example the connected sectors already isolated in Cycle 072) or impose a new physical constraint.

This is a structural narrowing, not a same-input PDT-vs-QM prediction and not a BREAKTHROUGH CANDIDATE.

## Prior-art boundary

The product identity is the purity/Hilbert–Schmidt tensor-product identity in another normalization. The corresponding pseudo-additivity is closely related to the established `q=2` Tsallis/linear-entropy product law. Therefore novelty must not be claimed for the algebraic identity itself. PDT novelty, if any, would have to arise from an independently justified resource interpretation or from a new constraint/prediction on correlated sectors.

## Audit

`cycle075_quadratic_product_composition.py` checks 1,480 randomized product-spectrum instances over dimensions `1..12,16,24,32,48,64,96,128`; recorded maximum floating error is `1.7763568394002505e-15`, with zero failures. Exact rational formulas, not those numerical runs, prove the sign-indefinite correlated residual.
