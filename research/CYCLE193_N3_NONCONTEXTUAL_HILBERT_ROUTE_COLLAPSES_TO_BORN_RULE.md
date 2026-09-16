# Cycle 193 — The Hilbert/noncontextual n=3 route collapses to the Born rule

## Status

- **PROVED:** conditional no-go theorem below.
- **FALSIFIED:** a PDT-II strategy that seeks a distinct n=3 probability law while simultaneously importing the full qutrit projector event structure, normalized orthogonal additivity, and measurement noncontextuality.
- **IMPORTED/KNOWN:** the uniqueness step is Gleason's theorem and therefore is not PDT novelty.
- **OPEN:** derive a genuinely PDT-native event/composition/response structure that does not merely assume the Hilbert/projector premises that already determine the Born rule.
- **BREAKTHROUGH CANDIDATE:** NO.

## Target attacked

Targets (2) and (3): a non-circular PDT-native n=3 derivation and a same-input quantitative PDT/QM discrepancy.

## Exact hypotheses

Let H be a real or complex Hilbert space with dim(H)=n >= 3. Suppose PDT identifies elementary sharp outcomes with one-dimensional projectors P (or rays), and proposes a response function mu(P) in [0,1] satisfying:

1. **context independence:** mu(P) depends on P, not on which orthonormal measurement basis contains P;
2. **orthogonal normalization/additivity:** for every orthonormal basis with rank-one projectors {P_i}, sum_i mu(P_i)=1.

These hypotheses are deliberately stated because they are tempting candidates for a 'distinction consistency' principle.

## Theorem — conditional collapse to quantum trace probabilities

Under the hypotheses above and n >= 3, there exists a density operator rho such that

`mu(P)=Tr(rho P)`

for every rank-one projector P. Thus, once the same microscopic state rho and same sharp outcome P are identified on the PDT and QM sides,

`P_PDT(P | rho,R_full)=P_QM(P | rho,R_full)`.

### Proof

The assumptions define a nonnegative normalized frame function on the rays/projectors of H. Gleason's theorem applies in Hilbert dimension >=3 and represents every such assignment by a positive trace-one operator rho via `mu(P)=Tr(rho P)`. This is exactly the Born trace rule on projective outcomes. QED.

The proof is **conditional** because PDT has not independently derived Hilbert rays/projectors, all orthonormal contexts, or noncontextual orthogonal additivity. Importing those premises and then invoking their known uniqueness theorem is not a PDT-native derivation.

## n=3 consequence

The qutrit is not an escape hatch; it is the first Hilbert dimension where the projection version of Gleason's theorem has its uniqueness force. Therefore a proposed PDT n=3 law that keeps all of the hypotheses above cannot differ from the Born rule. Any distinct response law must reject or physically restrict at least one premise, for example:

- event space is not the full qutrit projector lattice;
- probabilities are resource/context dependent in a precisely declared way;
- orthogonal additivity is modified because the operational composition of distinctions is different;
- microscopic PDT state is not identified with a density operator/ray and a new map to observed outcomes is derived.

Merely renaming rays as distinctions does not evade the theorem.

## Dimension stress test

- `n=1`: trivial; no nontrivial probability comparison.
- `n=2`: projection-only Gleason uniqueness does not apply; non-Born frame assignments can exist under the weaker projector premises. This is an important edge case, not evidence for a qutrit law.
- `n=3,...,12`: the theorem applies exactly.
- every finite `n>12`: same analytic conclusion.

No numerical simulation is required because this is dimension-independent once `n>=3`.

## Composite and reversible cases

Unitary/orthogonal reversible changes merely map projectors to projectors and do not evade the representation theorem. Product Hilbert systems whose total dimension is at least 3 remain inside the same no-go boundary when the full projector event structure and noncontextual additive response are assumed. Restricting accessible resources may remove enough contexts that Gleason uniqueness no longer follows, but then the response is underdetermined unless PDT supplies a new physical rule.

## Pure/mixed states and dynamics

The density operator delivered by the representation theorem includes pure and mixed states. Markovian or non-Markovian preparation history does not create a probability discrepancy at a fixed final operational state if the response still satisfies the stated full-projector premises. Controlled-environment records can enlarge the Hilbert/event description but do not by themselves change this conclusion. Thermodynamic costs likewise do not alter the theorem unless they enter a new, derived response law that changes one of the hypotheses.

## Adversarial implication for same-input prediction

Suppose a candidate PDT response `f(P,rho,R)` is claimed to differ from `Tr(rho P)` for a qutrit while still being nonnegative, normalized on every orthonormal basis, and independent of the basis context for fixed P. For fixed microscopic state/resource specification, it is a frame function. Gleason then forces trace form with some density operator sigma. If 'same microscopic input' requires sigma=rho, there is no gap. If sigma != rho, the candidate has silently changed the state representation/input and must derive the map rho -> sigma independently; it is not yet a same-input discrepancy.

This closes a common circular escape route.

## Prior-art boundary

This result is a PDT-specific **no-go application** of established mathematics, not a new probability theorem. Relevant prior art:

- A. M. Gleason, *Measures on the Closed Subspaces of a Hilbert Space*, Journal of Mathematics and Mechanics 6 (1957), 885–893.
- Modern expositions of Gleason's theorem: in dimension >=3, normalized noncontextual additive probability measures on projectors have trace form.
- Generalized-effect/POVM versions strengthen related uniqueness statements and can cover dimensions excluded by the original projection-only theorem.

Accordingly, no novelty is claimed for the uniqueness theorem.

## Consequence for PDT-II

A defensible n=3 breakthrough cannot be obtained by assuming exactly the quantum event geometry plus the consistency assumptions that already entail Born probabilities. PDT must first derive a physically different event/resource/composition structure, and only then derive its response functional. The next high-value attack is therefore to ask whether PDT's declared finite resource window yields a **restricted-context event hypergraph** with a uniquely determined response different from the restriction of every quantum state. If it does not, target (3) remains underdetermined; if it does, the smallest explicit hypergraph and probability vector become a falsifiable candidate.