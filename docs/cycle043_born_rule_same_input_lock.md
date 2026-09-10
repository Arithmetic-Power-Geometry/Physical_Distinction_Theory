# Cycle 043 — Born-rule same-input lock

**Status:** PROVED as an imported/known no-go boundary; PDT-specific consequence. **Not a breakthrough claim.**

## Question

Can PDT predict a different outcome distribution from standard quantum mechanics while keeping the same microscopic Hilbert-space state, the same measurement effects/events, and an ordinary normalized noncontextual probability assignment?

## Theorem (same-event probability lock)

Let `H` be a finite-dimensional complex Hilbert space.

### Projective version

For `dim(H) >= 3`, suppose a PDT probability assignment `mu(P)` is defined on all orthogonal projections, satisfies

1. `mu(I)=1`,
2. `mu(P)>=0`,
3. for every mutually orthogonal family `{P_i}`, `mu(sum_i P_i)=sum_i mu(P_i)`, and
4. the probability assigned to a projection is noncontextual: it depends on the projection itself, not on which complete projective measurement contains it.

Then Gleason's theorem implies that there exists a density operator `rho_*` such that

`mu(P)=Tr(rho_* P)`

for every projection `P`.

If the microscopic input is declared to contain the **same quantum state** `rho` as standard QM, so that state identity is fixed rather than re-fitted, then `rho_*=rho` and therefore

`P_PDT(P | rho,R)=Tr(rho P)=P_QM(P | rho,R)`

for every projective event whose declared resource window does not physically change the event/state.

### POVM version (including qubits)

Gleason-type theorems for generalized measurements extend the lock to Hilbert dimension `>=2` when probabilities are consistently assigned to POVM effects with the corresponding normalization/additivity assumptions. Thus the qubit is not an escape route if PDT retains the full POVM effect structure and effect-noncontextual probability assignment.

## Consequence

A genuine same-input deviation

`P_PDT(O|I,R) != P_QM(O|I,R)`

cannot arise merely by relabelling resources while simultaneously retaining all of the following:

- the same microscopic quantum state assignment,
- the same quantum event/effect operators,
- normalized additive probabilities over complete measurements,
- measurement/effect noncontextuality,
- and no physical modification of the state/effect/dynamics by the resource window.

At least one item must change. Therefore every future PDT same-input proposal must declare its **escape coordinate** explicitly:

1. changed physical state/dynamics,
2. changed admissible effect/event structure,
3. contextual probability law,
4. non-additive/nonstandard probability rule,
5. or a resource interaction that physically modifies the experiment.

If none changes, the proposal is locked to the Born distribution.

## Important precision

This result does **not** prove that all conceivable alternatives to quantum theory are impossible. It proves only a conditional no-go under the stated quantum event structure and probability-consistency assumptions. In particular, contextual ontological models, modified effect spaces, nonlinear/non-additive rules, or genuinely altered dynamics are outside the theorem's hypotheses and must be tested separately for consistency, signaling, composition and experiment.

## Prior-art boundary

The mathematical core is established: Gleason's theorem fixes probability measures on projections in complex Hilbert spaces of dimension greater than two, while POVM-based Gleason-type results recover the quantum probability rule also for qubits under generalized-measurement consistency. PDT novelty is therefore **not** claimed for the mathematical theorem. The PDT contribution of this cycle is the explicit same-input kill-test boundary for the ongoing PDT-II program.

## Research consequence

The highest-value same-input search should no longer look for a numerical correction to the Born rule while silently keeping all standard quantum probabilistic premises. It must instead formulate one explicit modified physical/probabilistic premise and then stress-test that premise for normalization, composition, no-signaling, preparation/measurement contextuality, convex mixing, sequential measurements and empirical constraints.
