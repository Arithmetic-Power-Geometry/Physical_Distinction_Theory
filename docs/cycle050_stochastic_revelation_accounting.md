# Cycle 050 — Exact stochastic revelation accounting

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT operational corollary.** Not a breakthrough candidate.

## Hypotheses

Let `p,q` be finite probability distributions on input outcomes and let `K(j|i)` be any column-stochastic resource/post-processing map. Put `delta_i=p_i-q_i` and `D(p,q)=1/2 sum_i |delta_i|`.

## Theorem

For every stochastic `K`,

`D(p,q)-D(Kp,Kq) = 1/2 sum_j [ sum_i K(j|i)|delta_i| - |sum_i K(j|i)delta_i| ]`.

Each bracket is nonnegative by the triangle inequality. Hence the identity refines the usual total-variation data-processing inequality by locating the exact loss at each output record.

### Equality condition

`D(Kp,Kq)=D(p,q)` iff for every output `j`, the set of input indices with `K(j|i)>0` does not contain both a positive and a negative value of `delta_i` (zero values are irrelevant). Equivalently, every output record is sign-pure with respect to the hypothesis difference.

## Proof

Because `K` is column-stochastic,

`sum_i |delta_i| = sum_j sum_i K(j|i)|delta_i|`.

Also

`2 D(Kp,Kq)=sum_j |sum_i K(j|i)delta_i|`.

Subtracting gives the identity. Equality in the triangle inequality for real numbers occurs exactly when all nonzero summands have one sign, giving the iff condition.

## Interpretation for PDT-II

The deterministic partition law from cycle 049 is a special case. For genuinely stochastic resource maps, distinction loss is exactly the amount of positive/negative hypothesis evidence mixed into the same accessible output records. This is an accounting identity, not a conservation law for a new physical substance.

## Stress test

`cycle050_stochastic_revelation_audit.py` uses deterministic seeds and exact `Fraction` arithmetic. It tests 200 randomized distributions/kernels for each input dimension n=1..12. The committed CSV reports zero identity failures and zero equality-condition failures in all 2400 trials.

## Prior-art boundary

Total-variation contraction under Markov kernels/data processing and Jordan decomposition of signed measures are standard. The proof here is an elementary refinement of that known mathematics. PDT may use the identity operationally but must not claim the mathematical identity itself as historically novel.

## Surviving open target

A genuinely PDT-native conservation/revelation law would need an independently defined hidden/environment distinction quantity and a derived exchange rule. Defining the hidden term merely as `D_fine-D_accessible` would be tautological and does not satisfy the breakthrough criterion.
