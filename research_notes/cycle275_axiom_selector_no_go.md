# PDT-II Cycle 275 — operational-axiom selector no-go

## Status

**PROVED (classical/commuting sector):** faithfulness + permutation invariance + data processing under stochastic maps + exact tensor additivity do **not** select a unique scalar distinction functional.

**IMPORTED/KNOWN:** the Rényi-divergence family and its classical data-processing/tensorization properties.

**FALSIFIED:** the candidate claim that these four generic operational axioms are sufficient to derive a unique PDT distinction functional, a unique PDT composition primitive, or `n=3`.

**OPEN:** a genuinely PDT-native selector involving the declared resource window and admissible joint experiments, rather than generic information-theoretic axioms alone.

## Exact hypotheses

Let `D(p||q)` be a scalar functional on strictly positive finite probability vectors. Consider the candidate selector axioms:

1. **Faithfulness:** `D(p||q) >= 0`, with equality iff `p=q`.
2. **Relabelling invariance:** simultaneous permutation of outcomes leaves `D` unchanged.
3. **Data processing:** `D(Tp||Tq) <= D(p||q)` for every stochastic map `T` for which the expression is defined.
4. **Independent-product additivity:** `D(p⊗r||q⊗s)=D(p||q)+D(r||s)`.

These are natural operational requirements, but they are not enough to select one functional.

## Counterfamily

For `alpha>0`, `alpha != 1`, define the classical Rényi divergence

`D_alpha(p||q) = (1/(alpha-1)) log sum_i p_i^alpha q_i^(1-alpha)`.

At `alpha=1` take the continuous limit, the KL divergence. On strictly positive finite distributions, the family is faithful and permutation invariant. Classical stochastic data processing holds in the standard Rényi domain, and product additivity follows directly by factorization:

`sum_{ij} (p_i r_j)^alpha (q_i s_j)^(1-alpha)`
`= (sum_i p_i^alpha q_i^(1-alpha))(sum_j r_j^alpha s_j^(1-alpha))`.

Taking the logarithm yields exact additivity.

The family is genuinely non-unique. For example, with

`p=(1/2,1/2)`, `q=(3/4,1/4)`,

`D_2 = log(4/3)`, whereas

`D_3 = (1/2) log(16/9) = log(4/3)` for this specially symmetric pair, so this pair alone is not a selector witness. A generic asymmetric pair must therefore be used when testing order separation; the accompanying regression uses exact pre-log moments and explicitly verifies unequal order-2/order-3 normalized log values numerically only after the exact moment check.

The decisive point does not depend on one witness: distinct Rényi orders are distinct functionals while satisfying the same four candidate axioms. Therefore these axioms define, at best, a family rather than a unique PDT primitive.

## Dimension stress test

The obstruction is already present at `n=2`. Any strictly positive binary pair embeds into every `n>=2` by adding a common positive tail and renormalizing; independently, the Rényi family itself is defined in every finite dimension. Hence the selector axioms cannot yield `n=3` or an upper ceiling `n<=3`. The accompanying tests cover explicit strictly positive rational distributions for `n=2,...,12` and verify exact product factorization of the pre-log Rényi moments for integer orders 2 and 3.

## PDT consequence

Cycle 274 showed that one attractive scalar composition operation can arise from inequivalent state-pair statistics. Cycle 275 strengthens the obstruction: even adding generic operational desiderata—faithfulness, relabelling symmetry, stochastic data processing and exact product additivity—still does not identify a unique scalar distinction primitive.

A viable PDT-native selector must therefore use additional **resource-window structure** not contained in these generic axioms. Candidate extra structure must itself be independently motivated and adversarially tested; examples include restrictions on admissible joint experiments, refinement/conditioning behavior tied to a physical resource ledger, or a theorem connecting the operational codebook capacity to a state-resolved statistic. None is promoted here.

## Prior-art boundary

This is a PDT-II **no-go/boundary result**, not a claim that Rényi divergence or tensorization is new. Rényi divergences and their data-processing/tensorization properties are established information-theoretic prior art. Recent quantum work also emphasizes that additivity and data processing are common axioms across families of quantum Rényi divergences. The novelty claim, if any, must therefore be limited to how this counterfamily closes a proposed PDT selector route.

## Breakthrough status

**NO BREAKTHROUGH CANDIDATE.** This cycle decisively falsifies a stronger proposed route and narrows the remaining composition problem.
