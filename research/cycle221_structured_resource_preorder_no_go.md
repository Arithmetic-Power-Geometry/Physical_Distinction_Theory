# Cycle 221 — Structured-resource preorder no-go

## Target
Test whether the Cycle-220 repair — replacing a single scalar capacity by a finite list of scalar resource monotones — can determine the PDT joint-admissibility law without importing a complete resource theory.

## Candidate claim attacked
A finite vector of ordinary scalar resource monotones is generically sufficient to determine resource convertibility/admissibility, and therefore can select the PDT composite admissibility algebra.

## Status
**FALSIFIED as a general principle. IMPORTED/KNOWN boundary.**

This is not promoted as PDT novelty.

## Exact hypotheses and surviving theorem
Let `(R, ->)` be a resource preorder. A family `M_1,...,M_k` is complete only when

`r -> s  iff  M_i(r) >= M_i(s) for every i`.

Monotonicity gives only the forward implication. Hence a finite vector of monotones determines admissibility only after a separate **completeness theorem** for the physical resource preorder. It is invalid to infer completeness from monotonicity alone.

For quantum resource theories the obstruction is stronger: Datta, Ganardi, Kondra and Streltsov (arXiv:2212.02473) prove, under their stated hypotheses (including a resource-free pure state), that no finite set of resource monotones completely determines all state transformations. Complete operational families can instead be infinite; related discrimination-task constructions provide complete families for broad convex resource theories.

Therefore a PDT composition proposal of the form

`A_XY = F(M_1(r),...,M_k(r))`

cannot be claimed universal merely because the `M_i` are physically meaningful monotones. PDT must prove that its chosen resource descriptor is complete for the declared admissibility problem, or retain the full structured resource/preorder.

## Finite adversarial sanity family
For `n=1,...,12`, use resources `S subseteq {1,...,n}` with free conversion `S -> T` iff `T subseteq S`. The scalar cardinality `|S|` is monotone but not complete: for every `n>=2`, `{1}` and `{2}` have equal cardinality and are incomparable. The smallest decisive witness is `n=2`.

This finite family is only a sanity counterexample to the inference 'monotone => complete'; it is not the quantum no-finite-monotone theorem.

## Edge/degenerate cases
- `n=1`: cardinality happens to be complete for this tiny chain.
- `n>=2`: equal-cardinality incomparable resources exist.
- A specially constructed injective scalar label could encode a finite preorder, so the correct theorem is **not** 'no scalar can ever be complete'. The obstruction concerns assuming completeness from scalar monotonicity/physical capacity without proving it.
- Totally ordered resource theories are exceptional cases in which a single complete monotone can exist.

## Prior-art boundary
Relevant known results include:
1. Datta et al., *Is there a finite complete set of monotones in any quantum resource theory?*, arXiv:2212.02473 — no finite complete set under their stated general hypotheses.
2. Takagi & Regula, *General Resource Theories in Quantum Mechanics and Beyond: Operational Characterization via Discrimination Tasks*, arXiv:1901.08127 — discrimination tasks can form complete operational families in broad resource theories.
3. Resource-theory literature distinguishes monotones from complete families and emphasizes that complete families may be infinite.

Accordingly this cycle is a **decisive falsification of a proposed PDT route**, not a breakthrough candidate.

## Consequence for PDT-II
The surviving composition obligation is now

`(structured resource r, controller/coupling class C, local admissibility A_X,A_Y) -> A_XY(r,C)`

with an explicit proof that the retained resource descriptor is complete for the relevant operation preorder. Compressing `r` to one or finitely many familiar capacities before proving completeness can erase operationally decisive distinctions.

This does not derive `n=3`, does not produce a same-input PDT/QM probability difference, and does not justify a gravity/capacity law.
