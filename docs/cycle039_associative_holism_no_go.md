# Cycle 039 — Associativity does not determine PDT composition

**Status:** PROVED exact parameter-counting no-go; underlying algebra/GPT tomography landscape IMPORTED/KNOWN; not a breakthrough claim.

## Question attacked

Can the current PDT composition gap be closed by imposing only very natural monoidal consistency conditions on the accessible quotient dimension `q_X`: commutativity, associativity, a trivial unit, monotonicity, and faithful inclusion of all product-accessible directions (`q_AB >= q_A q_B`)?

## Exact holism-balance identity

Write

`q_AB = q_A q_B + h_AB`,

where `h_AB >= 0` is the dimension excess not accounted for by product-accessible directions. If composition is associative at the level of accessible dimensions, then computing `q_ABC` as `(AB)C` and as `A(BC)` gives

`h_AB q_C + h_(AB),C = q_A h_BC + h_A,(BC)`.

This identity is exact. It is a necessary consistency condition on any associative PDT holism bookkeeping, but it does not fix `h`.

## Infinite associative counterfamily

For every nonnegative integer `k`, define

`F_k(a,b) = ab + k(a-1)(b-1)`.

For all positive integers `a,b,c`:

1. `F_k(a,b)=F_k(b,a)` (commutative);
2. `F_k(a,1)=a` (trivial unit);
3. `F_k(a,b) >= ab` (faithful product lower bound);
4. it is monotone in each argument;
5. `F_k(F_k(a,b),c)=F_k(a,F_k(b,c))` exactly.

The associativity is transparent after introducing

`T_k(q)=1+(k+1)(q-1)`,

because

`T_k(F_k(a,b)) = T_k(a) T_k(b)`.

Thus every `k>=0` supplies a distinct associative composition-dimension law. The elementary witness is

`F_k(2,2)=4+k`,

so even a pair of two-dimensional accessible quotients is compatible with infinitely many different composite dimensions while all of the listed axioms remain true.

## Consequence

The following proposed route is decisively falsified:

> PDT composition is uniquely fixed by associativity + commutativity + unit + monotonicity + preservation of product-accessible distinctions.

These assumptions are insufficient even before one asks for a full convex state space, effect cone, reversible group, dynamics, or tensor rule. A successful PDT-native composition theorem must constrain **which genuinely holistic distinction directions are admissible**, not merely demand abstract monoidal consistency.

## Scope and limitation

This is a parameter-counting no-go. It does **not** claim that every `F_k` is realized by a physically sensible GPT or quantum-like theory. That stronger realizability question would require state/effect cones, probabilities, nonsignalling, transformations and composition maps. One counterfamily at the dimension-law level is sufficient to refute uniqueness from the stated dimension-level axioms.

## Computational audit

`pdt_holism_associativity.py` checks the exact identities. `tests/test_pdt_holism_associativity.py` exhausts dimensions `1..12` for `k=0..4`, scans unit/commutativity/product-lower-bound behavior through dimension `100`, and verifies fifty distinct laws with `F_k(2,2)=4+k`. `results/cycle039_associative_holism_self_composition.csv` records the `n=1..12` self-composition values for `k=0..3`.

## Prior-art boundary

Local tomography, its parameter-counting identity, and non-locally-tomographic/bilocally-tomographic alternatives are established in GPT and reconstruction literature, including Hardy–Wootters on limited holism/real-vector-space quantum theory and Barnum–Wilce on local tomography in Jordan-algebraic reconstructions. Therefore no historical novelty is claimed for the general idea that monoidal composition can contain holistic degrees of freedom. The present `F_k` family is retained as an explicit PDT kill test and exact bookkeeping witness.

## Next target

Search for a PDT-native axiom that acts below the dimension-counting level—for example, a resource-derived rule on admissible global effects or a compositional sufficiency principle—and then attack that axiom with real/complex/quaternionic, GPT minimal/maximal, and restricted-resource countermodels.
