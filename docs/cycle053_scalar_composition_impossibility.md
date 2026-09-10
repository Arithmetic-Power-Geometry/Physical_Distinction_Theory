# Cycle 053 — Scalar Composition Impossibility Witness

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN boundary + PDT operational consequence.**

This cycle attacks PDT-II target (1): whether the composite accessible distinction can be determined by a universal scalar law `D_AB = F(D_A,D_B)` when subsystem distinction is total variation distance and composition is the ordinary independent product.

## Theorem (no universal scalar composition law)

There is no function `F:[0,1]^2 -> [0,1]` such that for all finite probability pairs `(p,q)` and `(r,s)`,

`TV(p⊗r,q⊗s) = F(TV(p,q),TV(r,s))`.

### Small binary witness

Let

- `p=(0,1)`, `q=(1/4,3/4)`;
- case A: `r=(0,1)`, `s=(1/4,3/4)`;
- case B: `r'=(1/4,3/4)`, `s'=(0,1)`.

In both cases the scalar subsystem data are identical:

`TV(p,q)=TV(r,s)=TV(r',s')=1/4`.

But exact product distances differ:

- aligned orientation: `TV(p⊗r,q⊗s)=7/16`;
- reversed orientation: `TV(p⊗r',q⊗s')=1/4`.

Therefore the ordered pair `(D_A,D_B)=(1/4,1/4)` does not determine `D_AB`. A universal scalar `F(D_A,D_B)` is impossible even for binary classical records under ordinary independent composition.

## Exact calculation

For case A,

`p⊗r=(0,0,0,1)` and `q⊗s=(1/16,3/16,3/16,9/16)`,

so `TV = (1/2)(1/16+3/16+3/16+7/16)=7/16`.

For case B,

`p⊗r'=(0,0,1/4,3/4)` and `q⊗s'=(0,1/4,0,3/4)`,

so `TV=(1/2)(1/4+1/4)=1/4`.

## Consequence for PDT-II

The obstruction is stronger than failure of additive or multiplicative formulas. **No scalar function whatsoever of the two marginal TV distinctions can exactly encode ordinary product composition.** Exact composition must retain additional structure (for example likelihood/evidence orientation, overlap geometry, or an equivalent richer object).

This does not itself determine the PDT-native full composite state/effect cone. It is a no-go theorem that narrows the target: a successful PDT composition law cannot close on a single scalar distinction coordinate.

## Prior-art boundary

This is consistent with established probability-theory work on tensorization of total variation and product distributions, where marginal TV values do not determine product TV exactly. No claim of historical novelty is made for the underlying probability fact. The PDT-specific value is the explicit minimal operational obstruction to scalar closure.

## Breakthrough gate

Not promoted to `BREAKTHROUGH CANDIDATE`: the theorem is rigorous and decisive for one candidate architecture, but its mathematical core is known/anticipated by product-TV literature. The full PDT-native composition law remains OPEN.
