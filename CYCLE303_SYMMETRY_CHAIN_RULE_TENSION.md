# PDT Cycle 303 — Symmetry / ordinary chain-rule tension

## Target
Stress-test the strongest surviving composition selector from Cycle 302. In particular, test whether a symmetric distinction functional can be obtained by the most direct symmetrization of KL while retaining the ordinary P-weighted conditional chain rule.

## Candidate
Let

J(P,Q) = D_KL(P||Q) + D_KL(Q||P)

(the Jeffreys divergence). It is symmetric, nonnegative, continuous on the strict interior, product-additive, and obeys data processing because each KL term does.

Candidate claim: J also obeys the ordinary sequential rule

J(P_XY,Q_XY) ?= J(P_X,Q_X) + sum_x P_X(x) J(P_{Y|x},Q_{Y|x}).

## Exact algebra
Applying the two KL chain rules gives instead

J(P_XY,Q_XY)
= J(P_X,Q_X)
+ sum_x P_X(x) D_KL(P_{Y|x}||Q_{Y|x})
+ sum_x Q_X(x) D_KL(Q_{Y|x}||P_{Y|x}).

The reverse conditional term is weighted by Q_X, not P_X. Therefore the proposed P-weighted chain rule has defect

Delta = sum_x [Q_X(x)-P_X(x)] D_KL(Q_{Y|x}||P_{Y|x}).

This is generically nonzero.

## Small strict-interior witness
Use

P_X=(3/4,1/4), Q_X=(1/4,3/4),
P_{Y|0}=(3/4,1/4), Q_{Y|0}=(1/2,1/2),
P_{Y|1}=Q_{Y|1}=(1/2,1/2).

All joint probabilities are positive. The x=1 reverse conditional KL vanishes, while at x=0

D_KL((1/2,1/2)||(3/4,1/4)) = (1/2) ln(4/3) > 0.

Hence

Delta = (1/4-3/4)*(1/2 ln(4/3)) = -(1/4) ln(4/3) != 0.

So the ordinary P-weighted chain rule fails exactly for J.

## Dimension stress
The witness is already binary. It embeds into n=2,...,12 and higher alphabets by splitting positive atoms identically under both hypotheses; the chain-rule defect survives under such common refinements. This is a structural obstruction, not a numerical accident.

## Prior-art boundary
KL chain rules and Jeffreys/symmetrized relative entropy are established information theory. Characterization results for relative entropy also predate PDT (e.g. Hobson 1969; later short axiomatic characterizations). Therefore neither KL nor this symmetry tension is claimed as PDT novelty.

## Consequence for PDT-II
Cycle 302 found that the ordinary conditional chain rule is a stronger selector than product additivity + DPI. Cycle 303 shows that imposing the most natural exchange symmetry simultaneously does not preserve that selector. PDT must therefore justify the orientation/branch weighting physically, or derive a different native sequential law. Calling a symmetrized imported divergence the PDT composition law would not solve the problem.

## Status
- Jeffreys symmetry/product additivity/DPI: IMPORTED/KNOWN.
- Jeffreys ordinary P-weighted conditional chain rule: FALSIFIED.
- Exact strict-interior binary witness: PROVED.
- Structural defect formula above: PROVED.
- Nontrivial symmetric PDT-native sequential law: OPEN.
- PDT-native composition selector: OPEN.
- Non-circular PDT-native n=3 derivation: OPEN.
- Same-input quantitative PDT-vs-QM prediction: OPEN.
- BREAKTHROUGH CANDIDATE: NO.
