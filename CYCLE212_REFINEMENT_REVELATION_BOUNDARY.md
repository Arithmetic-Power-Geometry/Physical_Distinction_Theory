# Cycle 212 — Resource refinement: monotonicity survives; eventual revelation fails

## Status

- Refinement monotonicity of accessible distinctions: **PROVED (conditional)**.
- Eventual revelation from refinement alone: **FALSIFIED**.
- Data-processing / resource-order component: **IMPORTED/KNOWN**.
- PDT-native resource-selection/composition principle: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Exact hypotheses

Let `X` be a finite microscopic state space. A resource window `R` determines an admissible observation family `A_R` of maps `a:X->Y_a`. Define resource refinement by inclusion:

`R <= S  iff  A_R subseteq A_S`.

Define operational indistinguishability

`x ~_R x'  iff  a(x)=a(x') for every a in A_R`.

The accessible quotient is `Q_R = X / ~_R`.

## Theorem 212.1 — refinement monotonicity

If `R <= S`, then `~_S subseteq ~_R`. Consequently every `S`-class lies inside an `R`-class, so `Q_S` refines `Q_R` and `|Q_S| >= |Q_R|` for finite X.

### Proof

If `x ~_S x'`, all observations in `A_S` agree on x and x'. Since `A_R subseteq A_S`, all observations in `A_R` also agree. Hence `x ~_R x'`. QED.

This is an order/data-processing fact; it does not select the observation family and is not claimed as PDT novelty.

## Candidate principle attacked

> Repeatedly increasing resources must eventually reveal every dynamically relevant microscopic distinction.

This statement is false without an additional separation/completeness axiom.

## Smallest decisive counterexample

Take `X={0,1,2}` and microscopic deterministic dynamics

`F(0)=0, F(1)=1, F(2)=0`.

Thus 0 and 1 are dynamically different (indeed both are distinct fixed microscopic states), while 2 flows to 0.

For every resource level `k>=1`, let `A_k` contain only observations that factor through

`q(0)=q(1)=A, q(2)=B`.

Choose a strictly nested family, for example add at level k a new labelled copy / post-processing of q not present at lower levels. Then `A_k subsetneq A_{k+1}` for every k, so the resource family genuinely grows, but no admissible observation ever separates 0 from 1. Therefore

`0 ~_k 1` for every finite k and also for the union window `A_infty = union_k A_k`.

Resource refinement alone therefore does **not** imply eventual revelation of all microscopic or dynamically relevant distinctions.

The same obstruction embeds into every finite `n>=3` by adjoining states whose observations may be independently refined while preserving the permanent identification `0~1`. Hence it covers n=3,...,12 exactly and all higher finite dimensions analytically. For n=1 no hidden pair exists; for n=2 the analogous two-state constant observation already gives the degenerate obstruction, but strict nontrivial refinement requires an added observable degree/state.

## Surviving theorem

Eventual revelation follows only under an explicit point-separation condition. If for every distinct microscopic pair `x != x'` there exists some resource level R and admissible observation `a in A_R` with `a(x) != a(x')`, then the union resource family separates points and the limiting equivalence is equality. This is essentially the assumption needed for the conclusion; it is not a derivation of that assumption.

A weaker dynamically targeted version replaces all distinct pairs by pairs whose difference matters to the declared future task/dynamics. Again, a task-separation axiom is required.

## Consequence for PDT-II

Cycle 211 showed that a restricted intervention/observation algebra can hide dynamically different quotients. Cycle 212 closes the obvious repair: merely asserting that resources can be refined does not guarantee that the hidden distinctions ever enter the admissible algebra. PDT must independently derive a physically motivated resource-refinement mechanism with a non-circular separation/revelation criterion. Otherwise the desired n=3/composition structure can be permanently invisible.

No same-input PDT-vs-QM deviation, experimental inequality, or gravity/capacity law is inferred from this result.

## Prior-art boundary

Monotonicity under richer operational resources and data processing is standard in statistical comparison and resource theories. Blackwell comparison orders experiments by decision value/garbling; general resource theories use monotones under free transformations; distinguishability resource theories formalize related operational orders. Therefore Theorem 212.1 is classified IMPORTED/KNOWN in conceptual content. The PDT contribution of this cycle is only the explicit no-go boundary for the proposed refinement rescue, not a novelty claim for refinement monotonicity itself.
