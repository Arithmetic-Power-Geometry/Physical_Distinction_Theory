# Cycle 040 — Infinitesimal-independence composition rigidity

**Status:** CONDITIONAL theorem; proof exact. Underlying associative-function / one-dimensional semigroup mathematics is IMPORTED/KNOWN. The physical axiom introduced below is not yet derived from PDT, so this is **not** a BREAKTHROUGH CANDIDATE.

## Question

Cycle 039 proved that associativity, symmetry, identity, monotonicity and product-accessibility do not uniquely determine a scalar composite capacity. The family

\[
F_k(a,b)=ab+k(a-1)(b-1),\qquad k\ge 0,
\]

satisfies all of those conditions and gives different composite capacities.

This cycle asks for the weakest transparent additional condition, expressed directly as a resource/distinction marginal, that kills this holism freedom.

## Candidate physical condition: Independent Marginal Revelation (IMR)

Let `q>=1` be a continuously extended effective accessible distinction capacity, normalized so that `q=1` is the trivial system. Let

\[
F:[1,\infty)^2\to[1,\infty)
\]

be a continuously differentiable scalar composition law. IMR is the local condition

\[
\partial_2F(a,1)=a. \tag{IMR}
\]

Operational reading: when a trivial second subsystem acquires an infinitesimal amount of independently accessible distinction, the first-order increase of the joint accessible capacity is proportional to the already accessible capacity `a` of the first system. This is a new **axiom candidate**, not something presently derived from the PDT primitive.

## Theorem 40.1 — Conditional scalar composition rigidity

Assume:

1. `F` is `C^1` on its domain;
2. `F(a,1)=a` (trivial unit);
3. `F(F(a,b),c)=F(a,F(b,c))` (associativity);
4. IMR: `partial_2 F(a,1)=a` for every `a>=1`.

Then

\[
\boxed{F(a,b)=ab}
\]

for all `a,b>=1` in the connected domain.

### Proof

Start from associativity:

\[
F(F(a,b),c)=F(a,F(b,c)).
\]

Differentiate with respect to `c` and set `c=1`. By the chain rule,

\[
\partial_2F(F(a,b),1)
=
\partial_2F(a,F(b,1))\,\partial_2F(b,1).
\]

The unit law gives `F(b,1)=b`. IMR gives

\[
\partial_2F(F(a,b),1)=F(a,b),
\qquad
\partial_2F(b,1)=b.
\]

Therefore

\[
F(a,b)=b\,\partial_2F(a,b),
\]

or, for fixed `a`,

\[
\frac{\partial F(a,b)}{\partial b}=\frac{F(a,b)}{b}.
\]

This first-order ODE has solution `F(a,b)=C(a)b`. Applying `F(a,1)=a` gives `C(a)=a`. Hence

\[
F(a,b)=ab.
\]

No commutativity assumption is needed for this conclusion once the right-unit and IMR conditions are stated as above. QED.

## Cycle-039 family is killed sharply

For

\[
F_k(a,b)=ab+k(a-1)(b-1),
\]

we have

\[
\partial_2F_k(a,1)=a+k(a-1).
\]

Thus for every nontrivial `a>1`, IMR holds iff `k=0`. The entire previously surviving holism family collapses to ordinary multiplication.

The implementation audits `a=1..12`, `k=0..5`, exact integer associativity over all triples in `1..12`, and randomized floating-point triples. Tests also scan the IMR exclusion through `k=19` and the product reference law through `a=100`.

## What this proves — and what it does not

This is the first post-Cycle-039 result in the branch that gives a **uniqueness theorem** rather than another non-uniqueness witness. However, it remains conditional. PDT has not yet independently proved IMR from finite-resource discrimination, composition of admissible experiments, or another primitive. Treating IMR as self-evident would simply move the composition assumption into a derivative condition.

The theorem concerns a scalar effective-capacity composition law. It does not by itself determine the full composite state cone, effect space, reversible group, entanglement structure, tensor product, or nonlocal observables. Therefore it is not yet the sought PDT-native composite-system theorem.

## Prior-art boundary

The associativity equation and its continuous/monotone representation theory are classical. Aczel-type representation theorems show that broad classes of continuous strictly monotone associative operations on intervals are conjugate to addition by a change of coordinate. One-dimensional formal-group theory likewise describes associative laws through an invariant differential/logarithm. These bodies of mathematics make clear that the differential technique used here is established mathematical infrastructure, not a new mathematical field.

Useful prior-art anchors:

- C.-H. Ling, *Representation of associative functions*, Publicationes Mathematicae Debrecen 12 (1965), which reviews Aczel's classical representation theorem for continuous strictly increasing associative functions: https://publi.math.unideb.hu/paper/2966/download/10_5486_PMD_1965_12_1-4_19.pdf
- Standard one-dimensional formal-group logarithm/invariant-differential machinery (see e.g. Hazewinkel, *Formal Groups and Applications*).

The potentially PDT-specific contribution is therefore only the **operational interpretation and placement of IMR as a falsifiable composition axiom candidate**, together with the exact proof that it restores scalar multiplicativity. Historical novelty is OPEN and must not be claimed without a dedicated literature search.

## Falsification / kill tests

1. Find a `C^1`, associative right-unital law satisfying IMR but not `F(a,b)=ab`; this would falsify the proof or expose a hidden domain assumption.
2. Show that physically admissible PDT capacities are inherently discrete with no meaningful differentiable extension; then IMR is inapplicable as stated.
3. Exhibit a PDT-native composition whose scalar accessible capacity is nonmultiplicative while still satisfying the operational content intended by IMR; then the proposed interpretation is too strong or incorrectly formalized.
4. Derive IMR from a known GPT/local-tomography/resource axiom; then its physical content may be imported rather than PDT-native.

## Research consequence

The open composition problem is now sharper. To obtain product scalar composition, PDT does not need to assume full local tomography at the outset; it is sufficient to derive the local marginal law IMR plus associativity and a unit. The next obligation is therefore **derive or falsify IMR from the actual PDT resource/distinction primitives**, and separately determine whether scalar multiplicativity can constrain the full composite state/effect structure.
