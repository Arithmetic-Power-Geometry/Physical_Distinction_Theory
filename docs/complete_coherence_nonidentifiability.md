# Complete Coherence Non-Identifiability Theorem

**Status: PROVED / NO-GO.** This note makes no standalone historical-novelty claim.

## Statement

Consider controlled dephasing with an environment of dimension `d >= 2`, initial environment state

`eta = I_d/d`, branch unitaries `U0 = I_d` and `U1 = V`, and coherence factor

`chi = Tr(U0 eta U1^dagger) = Tr(V^dagger)/d`.

The two conditional environment outputs are

`rho0 = U0 eta U0^dagger = I_d/d`,

`rho1 = U1 eta U1^dagger = I_d/d`

for every unitary `V`. Nevertheless, while this complete conditional-output pair is held exactly fixed, **every complex coherence factor in the closed unit disk is realizable**.

Equivalently, for every `z` with `|z| <= 1`, there is a unitary `V` such that

`rho0 = rho1 = I_d/d` and `chi = z`.

Therefore no function of the complete pair `(rho0,rho1)` can determine `chi`, `|chi|`, its phase, the corresponding controlled-dephasing rate, or any quantity that requires them, without additional relative branch information or further physical restrictions.

## Constructive proof

Let `z = r exp(i phi)`, with `0 <= r <= 1`, and put `theta = arccos(r)`.

For `d = 2`, choose the two eigenvalues of `V^dagger` to be

`exp(i(phi+theta))` and `exp(i(phi-theta))`.

Their normalized sum is

`[exp(i(phi+theta)) + exp(i(phi-theta))]/2 = exp(i phi) cos(theta) = z`.

For any `d > 2`, use the same target by choosing unit-modulus eigenvalues whose centroid is `z`; a simple constructive implementation is provided in `conditional_output_no_go.py` using paired phases (and numerical verification is kept separate from the analytic d=2 proof). The d=2 construction alone is already sufficient to prove non-identifiability in the unrestricted theory class.

## Scientific consequence

The earlier witness showing only `|chi|=1` versus `|chi|=0` is a special case. The stronger result shows **maximal non-identifiability**: identical complete conditional density operators can coexist with the full physically allowed disk of complex coherence factors (already for a two-dimensional maximally mixed environment).

This closes a tempting PDT route: conditional-state tomography alone cannot provide a universal same-input predictive advantage over microscopic quantum mechanics in mixed controlled-dephasing models. A viable PDT-native predictive principle must constrain or measure relative branch/unitary information, or identify a justified restricted physical sector in which a coarser statistic becomes sufficient.

## Prior-art caution

The standard controlled-dephasing identity `chi = Tr(U0 eta U1^dagger)` for mixed environments is established open-system physics. Literature on decoherence also treats purification and relative branch overlaps. This note therefore classifies the mathematical statement as **PROVED / NO-GO**, while its historical novelty remains **OPEN pending a dedicated literature audit**. It must not be advertised as a new law of physics merely because the explicit full-disk construction is useful for PDT.