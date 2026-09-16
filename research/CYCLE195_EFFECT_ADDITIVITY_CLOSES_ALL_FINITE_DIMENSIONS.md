# Cycle 195 — Effect additivity closes the probability-deviation route in every finite dimension

## Status

- **PROVED (conditional)**: normalized positive finite-additive response rules on the full quantum effect interval have trace/Born form.
- **IMPORTED/KNOWN**: this is the finite-dimensional Busch/Gleason-type effect theorem, not PDT novelty.
- **FALSIFIED**: a PDT response rule cannot differ from QM while retaining the full quantum effect space plus noncontextual finite additivity and normalization.
- **OPEN**: PDT-native derivation of a physically justified event/effect structure or response principle that does not simply assume the quantum effect algebra.
- **BREAKTHROUGH CANDIDATE: NO**.

## Target attacked

PDT-II targets (2) and (3): non-circular n=3 derivation and same-input quantitative PDT/QM separation.

## Exact hypotheses

Let H be a finite-dimensional complex Hilbert space and

E(H) = {E : 0 <= E <= I}

be the full quantum effect interval. Suppose a candidate PDT response functional f:E(H)->[0,1] satisfies:

1. positivity: f(E)>=0;
2. normalization: f(I)=1;
3. noncontextuality: f depends on the effect E, not on the POVM/context in which E occurs;
4. finite effect additivity: if E,F,E+F are effects, then f(E+F)=f(E)+f(F).

No Born rule is assumed in these four hypotheses.

## Theorem

There exists a unique density operator rho such that

f(E)=Tr(rho E)

for every E in E(H).

Hence, under identical microscopic state rho and identical accessible effect E,

P_PDT(E | rho,R_full) = P_QM(E | rho,R_full).

This applies in dimension 2 as well as dimension 3 and higher, so enlarging the event domain from projectors to all effects removes the familiar projection-only n=2 loophole.

## Finite-dimensional proof sketch

Additivity gives f(0)=0 and f(mE)=m f(E) whenever mE is an effect. For rational q in [0,1], repeated subdivision yields f(qE)=q f(E). Positivity implies monotonicity: E<=F gives f(E)<=f(F), because F=E+(F-E). Monotonicity plus rational approximation extends homogeneity continuously to real t in [0,1]. The resulting positive affine functional extends linearly to the real vector space of Hermitian operators. Finite-dimensional Hilbert-Schmidt duality therefore gives a Hermitian rho with f(E)=Tr(rho E). Positivity of f makes rho positive semidefinite; f(I)=1 gives Tr(rho)=1. Uniqueness follows because effects span the Hermitian operators.

## Dimension stress boundary

The argument is analytic and dimension-independent for every finite n, therefore in particular n=1,...,12. Degenerate effects E=0 and E=I, rank-deficient effects, pure/mixed rho, commuting/noncommuting POVM elements, and coarse-grainings are included. Tensor products do not create an escape if the composite again uses its full effect interval and the same hypotheses.

## Decisive falsification

Conjecture: "PDT can retain the complete quantum effect space, ordinary noncontextual coarse-graining/additivity, and normalization, yet derive a different same-input probability rule."

**FALSIFIED.** The hypotheses force trace/Born form. Therefore a genuine PDT/QM separation must alter or derive additional physical structure before the probability rule: e.g. a resource-restricted event domain, contextual response structure, different composite/event algebra, or another independently motivated microscopic response mechanism. Merely changing terminology from effects to distinctions cannot produce the separation.

## Prior-art boundary

This theorem is a known Gleason-type result for effects (Busch 2003 and related finite-dimensional formulations). It must be cited as prior art and must not be promoted as a PDT theorem of novelty.

Useful references:

- P. Busch, *Quantum States and Generalized Observables: A Simple Proof of Gleason's Theorem*, Phys. Rev. Lett. 91, 120403 (2003), DOI: 10.1103/PhysRevLett.91.120403.
- Gleason-type effect-space formulations proving normalized positive additive functions on effects have f(E)=Tr(rho E).

## Consequence for the PDT-II search

Cycle 193 showed the projector/noncontextual route collapses to Born form for n>=3. Cycle 195 strengthens the boundary: if PDT uses all effects and ordinary effect additivity, the collapse occurs already in dimension 2 (and trivially in dimension 1). The surviving research obligation is therefore not to search for an exotic additive probability formula on the same effect algebra; it is to derive-or-falsify a genuinely PDT-native operational structure that justifies departing from at least one hypothesis above while remaining physically coherent and testable.
