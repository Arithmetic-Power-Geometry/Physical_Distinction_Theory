# Cycle 200 — Generic closure axioms do not derive PDT physical synergy

## Target
PDT-II target (1)/(4): can a resource-generation rule be obtained merely by replacing linear span with a generic closure operator, thereby permitting jointly generated distinctions?

## Status
**PROVED no-go / FALSIFIED uniqueness claim / IMPORTED-KNOWN mathematics / OPEN physical selection.**

**BREAKTHROUGH CANDIDATE: NO.**

## Setup
Let X be a finite set of candidate physically accessible effects/distinctions. A resource-generation map C:2^X -> 2^X is assumed only to satisfy the standard closure axioms:

1. Extensivity: A subset C(A).
2. Monotonicity: A subset B implies C(A) subset C(B).
3. Idempotence: C(C(A))=C(A).

Define a genuinely joint generated effect for resources x,y as any z in C({x,y}) \ (C({x}) union C({y})).

## Theorem 200.1 — closure underdetermination
The three closure axioms, even together with identical singleton resource closures, do not determine whether joint synergy exists.

### Smallest decisive witness
Take X={x,y,z}. Define

C0(A)=A

for every A subset X, and define

C1(A)= A union {z} if {x,y} subset A,
       A otherwise.

Both C0 and C1 are extensive, monotone and idempotent. Moreover

C0({x})=C1({x})={x},
C0({y})=C1({y})={y}.

But

C0({x,y})={x,y},
C1({x,y})={x,y,z}.

Thus identical isolated-resource behavior and the generic closure laws permit either zero joint novelty or one newly generated distinction. Therefore generic closure structure cannot derive a unique PDT composition/revelation law.

### Minimality
With fewer than three ground elements there is no third effect z that can be absent from both singleton closures yet newly appear only in their joint closure. Hence this is the smallest set-theoretic witness of this form.

## Theorem 200.2 — exact synergy criterion
For any closure C and resources A,B, define

J_C(A,B)=C(A union B) \ (C(A) union C(B)).

Then closure-generated synergy exists iff J_C(A,B) is nonempty. This criterion is exact but is only bookkeeping: the closure axioms do not specify C and hence do not predict J_C.

If C additionally preserves binary unions,

C(A union B)=C(A) union C(B),

then J_C(A,B)=empty identically. Thus any PDT proposal seeking genuine joint generation must explicitly violate union preservation (while supplying a physical reason for the chosen closure).

## Dimension stress boundary
The three-element witness embeds unchanged in any larger finite candidate-effect set by adjoining inert labels. Therefore the underdetermination survives all tested bookkeeping dimensions n=3,...,12 and arbitrary finite n. For n=1,2 the specific three-label synergy witness is unavailable, which is an edge case rather than evidence for a unique law.

No numerical simulation is needed for this theorem: it is finite and exact.

## Consequences for PDT-II
1. Cycle 199 proved that static linear-span revelation is submodular and cannot generate strict superadditive revelation.
2. Allowing a nonlinear/generative closure can permit synergy, but Cycle 200 proves that extensivity + monotonicity + idempotence do not determine which synergy occurs.
3. Therefore `replace span by closure` is not a PDT-native composition law.
4. PDT still needs a microscopic physical rule selecting the closure/generation operation. Candidate rules must then be tested for associativity, reversible covariance, coarse-graining consistency, resource monotonicity, composites, dynamics, and same-input QM/GPT countermodels.
5. No probability deviation, experimental inequality, or gravity/capacity statement follows from generic closure axioms alone.

## Prior-art boundary
Closure operators with extensivity, monotonicity and idempotence are standard mathematics; linear span is a standard example, while stronger structures such as matroid closure add exchange. Consequently neither the three closure axioms nor generic generated-substructure language can be claimed as PDT novelty. The potentially PDT-specific content, if any, must be the independently physically derived generator/closure rule and a consequence not already inherited from known closure, matroid, effect-algebra, GPT, or contextuality machinery.

## Next strongest attack
Derive-or-falsify a microscopic **resource activation rule** G(A,B,state,dynamics) that predicts when a joint resource creates an effect outside the separate closures. Reject any candidate whose rule is merely stipulated or is an existing algebraic/GPT composition under new terminology. The first useful candidate must make a same-input quantitative consequence or a structural theorem stronger than generic closure theory.
