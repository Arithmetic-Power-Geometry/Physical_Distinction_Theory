# Cycle 033 — Resource-quotient refinement hierarchy

**Status:** PROVED as finite-dimensional linear/operational mathematics; PDT packaging only; historical novelty NOT claimed.

## Theorem

Let `V` be a finite-dimensional real vector space of distinction directions. Represent the linear tests accessible under a resource window `R` by a test matrix `A_R`, and define the operationally invisible subspace

`N_R = ker(A_R)`

and the resolved quotient

`V_R = V / N_R`.

If `R2` genuinely refines `R1` in the sense that every linear test available under `R1` is in the linear span of tests available under `R2`, equivalently

`row(A_R1) subseteq row(A_R2)`,

then

1. `N_R2 subseteq N_R1`;
2. `dim(V_R1) <= dim(V_R2)`;
3. there is a canonical surjective linear map `V/N_R2 -> V/N_R1`;
4. the revealed quotient-dimension gain

   `g(R1 -> R2) = dim(V_R2) - dim(V_R1)`

   is nonnegative;
5. along any nested chain `R0 <= R1 <= ... <= Rk`, the gains telescope exactly:

   `sum_j g(Rj -> R(j+1)) = dim(V_Rk) - dim(V_R0)`.

## Proof

Row-space inclusion implies that every vector annihilated by all `R2` tests is annihilated by all `R1` tests, hence `ker(A_R2) subseteq ker(A_R1)`. The quotient dimension obeys rank-nullity:

`dim(V/N_R) = dim(V) - dim(N_R) = rank(A_R)`.

Therefore refinement can only increase (or leave unchanged) the resolved quotient dimension. Because `N_R2 subseteq N_R1`, the map

`[v]_(N_R2) -> [v]_(N_R1)`

is well-defined and surjective. Nonnegativity of each gain follows immediately, and the chain identity is an exact telescoping sum.

## Exact/numerical audit

`pdt_resource_quotient_refinement.py` implements the theorem. `tests/test_pdt_resource_quotient_refinement.py` checks:

- exact coordinate filtrations for every `n=1,...,12`;
- deterministic randomized nested row-space tests for every `n=1,...,12`;
- degenerate/redundant tests with zero revelation gain;
- crossed non-refining resource sets, which are rejected rather than falsely labeled monotone;
- exact telescoping of revealed quotient dimension.

## Scientific boundary

This theorem does **not** derive a PDT-specific physical law beyond standard linear algebra or statistical sufficiency. It supplies a rigorous consistency law for the existing PDT resource quotient. A genuine PDT breakthrough would require an independently derived physical rule for how admissible test spaces change with energy/time/control/access resources, or a new quantitative consequence of this filtration that cannot be reproduced by standard quantum/GPT/resource-theory descriptions.

## Classification

- `PROVED`
- `IMPORTED/KNOWN` mathematics
- `PDT-SPECIFIC PACKAGING`
- **not** `BREAKTHROUGH CANDIDATE`
