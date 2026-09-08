# Cycle 006 — Operational quotient sufficiency criterion

## Status: PROVED PDT formulation / factorization mathematics IMPORTED-KNOWN / not new physics

This cycle addresses the central same-input question in a theory-independent way.

Let `I` denote the complete microscopic input, let `Q(I)` be the reference outcome distribution (for example the distribution predicted by microscopic quantum mechanics), and let

`S_R : I -> Sigma_R`

be the statistic actually retained by a PDT resource window `R`.

### Exact factorization theorem

There exists an exact predictor `G_R` depending only on the resource statistic,

`Q = G_R o S_R`, 

if and only if

`S_R(I_1) = S_R(I_2)  =>  Q(I_1) = Q(I_2)`.

**Proof.** Necessity is immediate from applying `G_R` to equal statistic values. For sufficiency, define `G_R(s)` to be `Q(I)` for any `I` in the fibre `S_R^{-1}(s)`; the fibre-constancy condition makes this definition independent of the representative. QED.

Equivalently, the resource statistic must refine the prediction-equivalence quotient

`I_1 ~_Q I_2  iff  Q(I_1)=Q(I_2)`.

This gives a precise kill test for every proposed PDT predictive statistic: if two microscopic inputs collapse to the same accessible statistic while the reference theory predicts different outcome distributions, no exact law based only on that statistic can reproduce all same-input predictions.

### Quantitative approximate no-go

Equip outcome distributions with total-variation distance `d_TV`. For each accessible value `s`, define the prediction diameter of its fibre

`Delta(s) = sup_{I,J in S_R^{-1}(s)} d_TV(Q(I),Q(J))`.

Then every resource-only predictor `G_R` obeys

`sup_I d_TV(Q(I), G_R(S_R(I))) >= (1/2) sup_s Delta(s)`.

**Proof.** For any two inputs in one fibre, the triangle inequality gives

`d_TV(Q(I),Q(J)) <= d_TV(Q(I),G_R(s)) + d_TV(G_R(s),Q(J))`.

At least one of the two errors is therefore at least half their separation. Taking suprema proves the bound. QED.

The result does not assert that the lower bound is always attained in an arbitrary metric prediction space; it is a universal obstruction.

## Connection to the controlled-record no-go

The earlier controlled-dephasing results become concrete instances of this theorem. If `S_R` retains only the pair of conditional environment output states, distinct controlled relative unitaries can lie in the same fibre of `S_R` while giving different coherence factors and hence different system predictions. Therefore that statistic fails the exact factorization criterion.

The theorem shows what a successful PDT extension must do: either

1. retain a statistic fine enough to separate every prediction-relevant fibre; or
2. introduce a genuinely new physical law that changes the reference prediction map itself.

Merely re-expressing or post-processing a coarse statistic cannot create a same-input deviation while remaining exactly equivalent to the same microscopic quantum model.

## Computational audit

`pdt_predictive_sufficiency.py` computes within-fibre total-variation diameters, exact finite-family sufficiency, and the universal minimax lower bound. The unit tests include:

- a sufficient statistic whose repeated fibres carry identical predictions; and
- a maximally insufficient fibre containing binary predictions `(1,0)` and `(0,1)`, producing diameter `1` and unavoidable worst-case error at least `1/2`.

This machinery can be applied to any future PDT candidate statistic before a new-physics claim is considered.

## Prior-art discipline

Factorization through fibres/quotients, sufficient-statistic logic, and diameter-based approximation lower bounds are established mathematical ideas. Related modern work explicitly uses fibre criteria for identifiability of composed predictors. Therefore historical mathematical novelty is **not claimed**. The PDT contribution is the explicit operational use of the criterion as a universal same-input kill test and design rule for resource-window statistics.

## Research consequence

A candidate PDT observable/statistic should now be rejected early if its sampled or analytic fibres contain reference predictions with nonzero diameter. The search for a genuine same-input PDT breakthrough is thereby narrowed to either a predictively sufficient operational quotient or an explicit modification of state space, composition, dynamics, or measurement law.
