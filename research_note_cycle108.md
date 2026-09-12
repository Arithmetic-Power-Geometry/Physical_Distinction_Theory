# Cycle 108 — Same-input stochastic-window no-go

## Question

Can PDT-II target (3) obtain a same-input probability departure from quantum mechanics merely by imposing a finite resource/detector window on an otherwise identical microscopic probability law?

## Result

No, if the declared resource window is the same stochastic post-processing for both theories.

Let `p_PDT(.|I)` and `p_QM(.|I)` be microscopic distributions and let `K_R` be a column-stochastic map representing the declared resource window. If

`p_PDT(.|I) = p_QM(.|I)`,

then

`K_R p_PDT = K_R p_QM`

exactly. More generally,

`TV(K_R p_PDT, K_R p_QM) <= TV(p_PDT, p_QM)`.

Thus common post-processing cannot create a disagreement and cannot amplify one. It can erase one completely: `p=(1,0)`, `q=(0,1)`, `K=(1,1)` gives microscopic TV distance 1 and resource-limited TV distance 0.

## Classification

- Same-input/common-window equality preservation: **PROVED**
- Total-variation contraction: **PROVED**
- Claim that common resource coarse-graining alone can generate/amplify a PDT-QM departure: **FALSIFIED**
- Mathematical ingredients: **IMPORTED/KNOWN**
- Dimension/random stress tests: **NUMERICALLY SUPPORTED**
- PDT-native pre-window probability modification: **OPEN**
- Breakthrough candidate: **NO**

## Prior-art boundary

This is standard stochastic-channel/data-processing/Blackwell-garbling mathematics. No novelty is claimed for the mathematical no-go.

## PDT consequence

Target (3) now has a stricter admissibility rule. A genuine PDT-vs-QM same-input prediction must come from at least one independently derived PDT-native ingredient before common resource coarse-graining:

1. a different microscopic probability law;
2. an additional operational state variable with a calibrated preparation rule;
3. or a physically different apparatus response that PDT predicts from independent dynamics rather than choosing after seeing the result.

A resource window represented only by ordinary common post-processing is not enough.
