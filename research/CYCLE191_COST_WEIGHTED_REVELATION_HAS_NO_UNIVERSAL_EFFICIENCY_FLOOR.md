# Cycle 191 — Cost-weighted revelation has no universal efficiency floor

## Status

- **PROVED (conditional):** finite-dimensional linear resource-relative revelation model with externally assigned nonnegative resource costs.
- **FALSIFIED:** any universal positive lower bound on distinction revelation per unit cost from the quotient/rank structure alone.
- **IMPORTED/KNOWN:** rank accumulation, weighted sensor selection, and budgeted submodular optimization are established mathematics/control/optimization territory.
- **OPEN:** whether PDT supplies an independently derived physical cost functional coupled to distinction geometry strongly enough to imply a non-generic inequality.
- **BREAKTHROUGH CANDIDATE:** NO.

## Target attacked

This cycle attacks PDT-II targets (4) resource-refinement/revelation/conservation and (5) experimentally distinctive inequalities, following Cycle 190's sharp rank-increment bound.

## Hypotheses

Let V be a finite-dimensional microscopic linear state space. A resource action a contributes an observable row subspace U_a <= V* of rank r_a and has declared cost c_a > 0. For an accumulated resource set A define

D(A) = dim span(U_a : a in A).

For adding action a to A define the revelation increment

Delta_D(a|A) = D(A union {a}) - D(A)

and, when c_a>0, the revelation efficiency

eta(a|A) = Delta_D(a|A)/c_a.

No relation between c_a and U_a is assumed beyond positivity of cost. This is deliberate: the question is whether quotient/rank revelation alone forces a cost-efficiency law.

## Theorem 1 — exact cost-weighted increment bound

For every action a,

0 <= Delta_D(a|A) <= r_a,

hence

0 <= eta(a|A) <= r_a/c_a.

This is immediate from the dimension formula for adjoining U_a to the accumulated row span. The upper bound is attained when U_a is independent of the previous span.

## Theorem 2 — no universal positive efficiency floor

There is no constant epsilon > 0, independent of the declared positive costs and admissible resource action, such that every genuinely revealing action satisfies

eta(a|A) >= epsilon.

### Proof

Take V=F, A empty, and one nonzero scalar effect U_a=V*. Then Delta_D(a|A)=1. Assign cost c_a=M for arbitrary M>0. Therefore eta=1/M. Given any proposed epsilon>0 choose M>1/epsilon, obtaining 0<eta<epsilon. QED.

Thus a positive resource cost plus quotient revelation does not by itself imply a minimum distinction yield per cost.

## Stronger falsification — cost is not determined by revealed quotient

Even fixing the same microscopic V, same effect U_a, same initial resource window, same final quotient, and same revelation increment leaves c_a unconstrained under the present hypotheses. Two models can therefore be observationally identical at the quotient level yet assign costs 1 and M to the identical revealing operation. Any claimed universal cost-capacity or gravity/capacity law would require additional physical structure that derives cost rather than labels it.

## Degenerate and adversarial cases

1. **Redundant expensive action:** U_a lies in the existing span, so Delta_D=0 while c_a can be arbitrarily large; eta=0.
2. **Independent expensive action:** Delta_D=r_a but c_a can be arbitrarily large; eta approaches 0.
3. **Independent cheap action:** with arbitrarily small positive c_a, eta can be arbitrarily large unless a lower cost scale is physically imposed.
4. **Rescaling obstruction:** replacing all costs c_a by lambda c_a, lambda>0, leaves every quotient and rank unchanged but rescales every eta by 1/lambda. Therefore no dimensionless numerical efficiency constant can follow from rank data alone.

## Dimension stress boundary

The one-dimensional witness already falsifies a universal positive floor at n=1. It embeds directly in every n=2,...,12 by using one coordinate effect and extends to every finite higher dimension. Reversible coordinate changes, norm changes, direct-sum spectator sectors, pure/mixed labels, and Markovian or non-Markovian bookkeeping do not repair the missing coupling between cost and observable row geometry.

For composite systems the same obstruction persists: even when Cycle 185's conditional quotient tensor law Q_AB ~= Q_A tensor Q_B holds, an externally declared composite cost can be rescaled independently unless a composition rule for physical cost is separately derived.

## Prior-art boundary

Weighted/budgeted sensor selection and submodular optimization already study information/observability objectives under costs. Adaptive submodularity likewise treats sequential sensing/resource allocation under partial observations. Accordingly, the generic mathematical structure is not claimed as PDT novelty.

## Consequence for PDT-II

The rank/quotient revelation programme now has a sharp negative boundary:

**observable distinction geometry does not determine physical resource cost.**

Therefore an experimentally distinctive PDT inequality cannot be obtained by merely dividing revealed quotient dimension by an assigned cost. PDT-II must independently derive a cost functional C from microscopic physical operations and then prove a nontrivial coupling between C and distinction revelation that survives rescaling/counterexample tests.

In particular, no gravity/capacity law is justified from the present quotient machinery. Importing an energy, action, entropy, Fisher metric, computational complexity, or thermodynamic cost and then recovering its known bound would be classified IMPORTED/KNOWN unless PDT derives the coupling from its own physical postulates.

## Next strongest attack

Search for a PDT-native operational cost generated by the same distinction structure rather than externally attached to it. Candidate tests should include minimal path length under an explicitly derived reversible generator set, intervention count under a fixed admissibility algebra, or environment-record creation cost. Each candidate must first be attacked for representation dependence, arbitrary unit rescaling, spectator ancillas, catalytic shortcuts, and tensor-composition ambiguity before any inequality is promoted.
