# PDT Cycle 309 — Binary effect data do not determine multi-outcome measurement structure

## Target
Attack the strongest surviving Cycle-308 route to a PDT-native response/composition law: augment pairwise distinction by *all single-event/binary response probabilities* and ask whether that determines the physically allowed multi-event measurements.

## Candidate principle
Let `Omega` be a normalized convex state space and `E` the full set of individually allowed effects. Suppose every `e in E` is operationally accessible as the binary measurement `{e,u-e}`. Candidate: `(Omega,E)` uniquely determines which finite tuples `(e_1,...,e_k)` with `sum e_i=u` are jointly implementable measurements.

## Result
**FALSIFIED under the stated hypotheses.** Individual accessibility does not imply joint accessibility. The same state space and the same complete set of binary effects can support different declared multi-outcome measurement families unless a further closure/no-restriction axiom is imposed.

## Small exact witness
Take the classical trit state space `Omega=Delta_2`. Let the coordinate effects be

`a(p)=p_1`, `b(p)=p_2`, `c(p)=p_3`, with `a+b+c=u`.

Use the same individual effect set in both operational theories, containing at least `0,u,a,b,c,u-a,u-b,u-c` and their required convex/complement closure. Hence both theories agree on every probability `e(p)` for every common effect and state, and in particular agree on all binary measurements `{e,u-e}`.

Define two measurement specifications:

* `M_restricted`: all the common binary measurements and whatever explicitly declared classical relabellings/coarse-grainings are admitted, but **not** the sharp trit measurement `T={a,b,c}`.
* `M_extended`: the same binary data plus `T={a,b,c}` (and corresponding declared closures).

Then `(Omega,E)` and every binary response probability are identical, while the operational question “is `T` jointly implementable?” has opposite answers. Thus no reconstruction map from binary effect data alone to the multi-outcome measurement family can be injective without an additional axiom tying individual effects to joint measurements.

This is a structural no-go, not a claim that an arbitrary restriction is physically fundamental. Its purpose is to identify the missing hypothesis precisely.

## Why the trit is minimal for this attack
A normalized two-outcome measurement is already specified by one effect and its complement, so complete binary-effect accessibility fixes the two-outcome layer by definition. The first genuinely new joint-implementability question occurs at three outcomes. Therefore a trit supplies the natural smallest finite witness for the binary-to-multi-outcome gap.

## Dimension stress
The witness embeds into every simplex `Delta_{n-1}` for `n>=3` by using a three-coordinate face and extending effects trivially on the remaining coordinates. Hence it survives exactly for `n=3,...,12` and arbitrary larger finite `n`. `n=1` is degenerate; `n=2` has no three perfectly discriminating coordinate outcomes and therefore does not instantiate this particular sharp-trit witness.

## Consequence for PDT-II
1. Pairwise distinction was already insufficient to determine `E` (Cycle 308).
2. Even upgrading the primitive to complete binary response data does not, under the present assumptions, determine multi-outcome joint implementability.
3. Therefore a PDT-native multi-event object cannot be obtained merely by saying “all effects are known.” PDT must derive an additional compatibility/measurement-composition principle.
4. Any axiom of the form “every positive decomposition of `u` is a physical measurement” is a no-restriction-style assumption and must be justified independently rather than counted as a PDT prediction.
5. Experimental inequalities depending on multi-outcome compatibility cannot be claimed from pairwise/binary PDT data alone.

## Prior-art boundary
**IMPORTED/KNOWN in substance.** Restricted GPT/operational-theory literature explicitly distinguishes the allowed effect algebra from the set of allowed multi-outcome measurements and notes that `(K,E)` need not completely specify a restricted theory because independent higher-outcome restrictions may remain. Operational-restriction work also studies restrictions on meters that do not restrict individual effects. Accordingly this cycle records a PDT-specific no-go obligation, not a novelty claim.

Relevant prior-art anchors checked in this cycle:
- Plavala et al., *Incompatibility in restricted operational theories: connecting contextuality and steering*, J. Phys. A (2022): restricted theory `(K,E)` may require a separate allowed-measurement set `M(E)` because higher-outcome restrictions are not fixed by effects alone.
- Filippov et al., *Operational Restrictions in General Probabilistic Theories*, Foundations of Physics (2020): operational meter restrictions can exist even when the accessible effect set is not restricted.
- Wright & Weigert, *General Probabilistic Theories with a Gleason-type Theorem*, Quantum 5, 588 (2021): no-restriction-type assumptions are substantive reconstruction assumptions, not automatic consequences of convex state/effect data.

## Status ledger
- `(Omega,E)` + accessibility of every binary `{e,u-e}` uniquely determines all finite measurements: **FALSIFIED** under the stated hypotheses.
- Classical-trit binary-vs-three-outcome witness: **PROVED** as a logical operational countermodel.
- Persistence for `n=3..12` and arbitrary finite `n>=3`: **PROVED** by face embedding.
- Stronger statement after imposing full closure under arbitrary measurement simulation: **OPEN** here; do not overclaim this cycle beyond its hypotheses.
- Underlying restricted-measurement phenomenon: **IMPORTED/KNOWN**.
- PDT-native compatibility/composition selector: **OPEN**.
- Non-circular PDT-native `n=3` derivation: **OPEN**.
- Parameter-free same-input PDT/QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Impose a precisely specified simulation closure (classical randomization, outcome relabelling, coarse-graining, and conditional composition) and ask whether two closed measurement families can still share the same full binary effect set while differing at three or more outcomes. Either construct the smallest closed counterexample or prove an injectivity theorem under explicit closure hypotheses. This is the correct next composition/effect-structure obligation before using multi-event PDT quantities to claim a same-input experimental inequality.
