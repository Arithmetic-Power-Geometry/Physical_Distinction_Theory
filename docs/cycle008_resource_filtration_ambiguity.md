# Cycle 008 — Resource-filtration ambiguity contraction

**Status:** PROVED as elementary operational mathematics; PDT packaging only; historical novelty NOT claimed.

Let a microscopic input space carry a prediction map `Q(I)` into outcome distributions, and let a resource statistic `S_R(I)` partition microscopic inputs into operationally indistinguishable fibres. Define the residual predictive ambiguity

`A_R(Q) = sup{ TV(Q(I),Q(J)) : S_R(I)=S_R(J) }`.

If `R2` refines `R1` in the precise sense that every `S_R2` fibre is contained in an `S_R1` fibre, then

`A_R2(Q) <= A_R1(Q)`.

The proof is immediate because the supremum defining `A_R2` is taken over a subset of the admissible pairs defining `A_R1`.

For a nested chain `R0 <= R1 <= ... <= Rk`, define the distinction-revelation increment

`Delta_j = A_Rj(Q) - A_R(j+1)(Q) >= 0`.

Then the increments telescope exactly:

`sum_j Delta_j = A_R0(Q) - A_Rk(Q)`.

Thus additional resources cannot increase worst-case predictive ambiguity when they genuinely refine the operational statistic, and the total ambiguity removed along any fixed nested chain is exactly the endpoint difference.

## Kill tests and limitations

1. `pdt_resource_filtration.py` computes fibre diameters in total variation and checks refinement explicitly.
2. `tests/test_pdt_resource_filtration.py` verifies contraction, exact telescoping, and rejection of crossing/non-refining partitions.
3. This does **not** provide a same-input deviation from quantum mechanics.
4. The underlying mathematics is elementary partition refinement / factorization / statistical sufficiency logic and is not claimed as historically new.
5. A genuine PDT advance would require a physically derived resource filtration whose ambiguity law yields a new quantitative consequence not already contained in standard statistical decision theory, quantum information, GPT, or resource-theory formalisms.

## Research consequence

Any proposed PDT resource hierarchy that predicts increasing ambiguity under a claimed refinement either (a) is not actually a refinement of the accessible statistic, (b) changes the microscopic prediction map, or (c) violates the stated operational setup. This gives the project a clean consistency audit for future resource-change laws.
