# Cycle 013 — Resource coarse-graining same-input no-go

## Status

**PROVED / IMPORTED-KNOWN mathematics / DECISIVE FALSIFICATION of a PDT breakthrough route.**

This result does **not** claim new quantum mathematics. It is a PDT research-boundary theorem obtained by applying standard stochastic post-processing/coarse-graining structure to the same-input breakthrough criterion.

## Theorem

Fix a microscopic experiment `I` whose standard-quantum prediction for a fine-grained outcome `x` is `p_QM(x|I)`. Let a declared resource window `R` alter only what is read out, through a stochastic kernel `K_R(y|x)`, while leaving the microscopic preparation, dynamics, measurement interaction, and probability rule unchanged. Then the accessible prediction is

`p_R(y|I) = sum_x K_R(y|x) p_QM(x|I)`.

Any PDT model whose only change relative to the microscopic QM model is exactly the same resource coarse-graining must therefore satisfy

`p_PDT(y|I,R) = p_QM,R(y|I,R)`

for every `I`, `R`, and `y`.

Consequently, a quantitatively different same-input prediction cannot come from resource-relative bookkeeping, quotienting, inaccessible distinctions, or classical post-processing alone. A genuine same-input deviation requires at least one additional physical change: a different microscopic state assignment, dynamics/channel, measurement/effect, probability functional, or a resource interaction that physically alters the experiment rather than merely its accessible record.

## Data-processing corollary

For any two microscopic distributions `p,q` and stochastic resource kernel `K_R`,

`TV(K_R p, K_R q) <= TV(p,q)`.

Thus readout coarse-graining alone cannot increase operational distinguishability. Any PDT candidate claiming an increase under a restriction that is represented solely by post-processing fails this kill test.

## Adversarial check

`pdt_resource_coarse_graining.py` audits dimensions 1 through 12 with seeded random probability vectors and stochastic kernels. The identical coarse-graining path agrees to machine precision by construction. The audit also applies a nonlinear power reweighting. That deformation generally produces a nonzero total-variation gap, demonstrating the diagnostic distinction: a different prediction is possible only after changing the response law, not from the same coarse-graining itself.

The unit test additionally checks total-variation contraction over many random kernels and outcome sizes.

## Prior-art boundary

This theorem is deliberately not labeled historically novel. Quantum observables are routinely coarse-grained by stochastic kernels/post-processing, and resource theories of quantum measurements use post-processing as a free degradation of measurement information. Gudder (2022) explicitly treats finite observable coarse-graining as stochastic-matrix post-processing. Guff et al. (2021) formulate a resource theory of quantum measurements in which free transformations deteriorate information acquisition. Current quantum-instrument resource theory likewise embeds POVMs/channels as established operational objects.

## Research consequence

This closes the route:

`resource relativity alone -> same-input PDT != QM`.

The surviving same-input breakthrough target must identify a concrete new physical law or resource-dependent physical interaction, specify the exact microscopic inputs, and produce a falsifiable numerical deviation from standard QM that cannot be reproduced by applying the same coarse-graining or instrument restriction inside QM.
