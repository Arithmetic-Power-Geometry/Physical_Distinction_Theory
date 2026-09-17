# Cycle 203 — Microscopic dynamics alone does not select a PDT-native composition law

## Status

**PROVED (conditional no-go)** / **FALSIFIED (uniqueness claim)** / **IMPORTED/KNOWN boundary** / **OPEN (PDT-native composition)**

## Target

Test the strongest surviving Cycle-202 route: whether specifying an independently motivated microscopic interaction dynamics is sufficient to derive a unique PDT composite/interaction rule.

## Exact hypotheses

Let a microscopic state space be a finite set X and let U:X→X be a reversible microscopic dynamics. Let a declared resource window R expose only an observation map q_R:X→Y. A proposed PDT operational dynamics is the induced map on accessible equivalence classes [x]_R defined by q_R.

For the induced dynamics to be well-defined it is necessary and sufficient that

q_R(x)=q_R(x') => q_R(Ux)=q_R(Ux')  (compatibility / lumpability).

## Theorem 203.1 — Quotient-dynamics existence criterion

There exists a unique map U_R:Y_R→Y_R satisfying U_R(q_R(x))=q_R(Ux) for all x iff the equivalence relation induced by q_R is U-compatible.

### Proof

Necessity: if q_R(x)=q_R(x'), both represent the same accessible state, hence applying U_R gives q_R(Ux)=q_R(Ux').

Sufficiency: define U_R(q_R(x)):=q_R(Ux). Compatibility makes this independent of the representative x. Uniqueness follows because every accessible class has a representative.

## Theorem 203.2 — Microscopic dynamics does not determine the resource quotient

Fix the same microscopic state space and the same reversible dynamics. Distinct resource maps can be U-compatible while inducing non-isomorphic accessible composites.

### Smallest decisive witness

Take X={00,01,10,11} and U the identity (or bit swap). Define

q_full(a,b)=(a,b),
q_parity(a,b)=a XOR b.

Both are compatible with identity dynamics. Under bit swap both remain compatible because parity is swap-invariant. Yet q_full has four accessible classes whereas q_parity has two. Thus identical microscopic dynamics does not select the operational distinction/composite structure.

The witness embeds in arbitrary higher finite dimensions by adjoining inert coordinates. Therefore the obstruction persists through n=1..12 wherever a nontrivial quotient is available, and asymptotically.

## Consequence

Cycle 202's statement that PDT should derive G_R from microscopic dynamics must be strengthened. Microscopic dynamics is necessary input but is not sufficient. PDT must independently derive both:

1. the resource-relative observation/equivalence map q_R (which microscopic distinctions are physically accessible), and
2. compatibility of q_R with the microscopic dynamics.

Only then is the operational interaction law induced rather than chosen.

## Markovian / non-Markovian boundary

A one-time quotient can hide environmental records. When future responses depend on those hidden records, no closed Markovian map on the current quotient state exists; the operational object must retain memory/history or enlarge the accessible state. Hence importing process tensors, quantum combs, or generic memory kernels would solve representation, not derive PDT's resource quotient.

## Prior-art boundary

The mathematical idea that coarse-graining must be compatible with dynamics is established through lumpability / quotient dynamics. Operational multi-time quantum processes and process tensors already describe interventions and non-Markovian memory; restricted process tensors already treat experimentally restricted operation spans. These are comparison frameworks, not PDT novelty.

## Breakthrough decision

**BREAKTHROUGH CANDIDATE: NO.**

The new defensible PDT-II obligation is a *joint derivation problem*: derive q_R from physical resource constraints and microscopic dynamics together, rather than deriving dynamics first and selecting a quotient afterward. A same-input PDT/QM prediction cannot be claimed until this joint derivation selects a response inaccessible to the quantum model under the identical declared resource window.
