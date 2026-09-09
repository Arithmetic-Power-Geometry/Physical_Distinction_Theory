# Cycle 041 — Scalar composition gauge no-go

**Status:** PROVED as a smooth associativity representation; underlying functional-equation/formal-group mathematics is IMPORTED/KNOWN. PDT consequence is a no-go for treating an uncalibrated scalar composition law as new physics.

## Setup
Let `F : I x I -> I` be a `C^1` associative composition law on a real interval `I` containing the neutral element `1`, with

`F(a,1)=F(1,a)=a`.

Assume the right marginal speed

`phi(x) = partial_2 F(x,1)`

is strictly positive on `I`.

Define the calibration logarithm

`L(x) = integral_1^x du / phi(u)`.

## Theorem (smooth scalar composition linearization)
For every `a,b` in the connected domain on which the above assumptions hold,

`L(F(a,b)) = L(a) + L(b)`.

Hence

`F(a,b) = L^{-1}(L(a)+L(b))`.

So every smooth associative scalar composition law with nonvanishing marginal speed is merely ordinary addition in a monotone calibration coordinate. Multiplication is the special case `phi(x)=x`, for which `L(x)=ln x` and `F(a,b)=ab`.

## Proof
Associativity gives

`F(F(a,b),c) = F(a,F(b,c))`.

Differentiate with respect to `c` and set `c=1`. Using `F(b,1)=b` yields

`phi(F(a,b)) = partial_2 F(a,b) phi(b)`.

Therefore

`partial_2 L(F(a,b)) = L'(F(a,b)) partial_2 F(a,b)`

`= partial_2 F(a,b)/phi(F(a,b))`

`= 1/phi(b)`

`= L'(b)`.

Thus `L(F(a,b))-L(b)` is independent of `b`. Setting `b=1` and using `L(1)=0`, `F(a,1)=a`, gives the constant `L(a)`. Hence

`L(F(a,b))=L(a)+L(b)`.

## PDT consequence
A scalar-capacity composition formula by itself cannot carry invariant physical novelty under these hypotheses: a nonlinear-looking law can be removed by a monotone recalibration of the scalar. To obtain PDT-native physics, the scalar coordinate must be operationally fixed independently (for example by a declared coding/error/resource protocol), or the theory must add structure not reducible to one scalar: state/effect geometry, admissible global distinctions, dynamics, or experimentally distinct probabilities.

This also explains Cycle 040. Independent Marginal Revelation `phi(x)=x` does not merely choose one arbitrary associative law; it fixes the calibration gauge to logarithmic capacity and thereby forces multiplication.

## Kill tests / limitations
1. The theorem requires `C^1` regularity and `phi>0`; singular, noncancellative, idempotent, or merely discontinuous operations are outside scope.
2. It does not determine the full PDT composite state/effect space.
3. It does not produce a same-input deviation from quantum mechanics.
4. The representation is classical associativity-equation / one-dimensional formal-group mathematics; historical novelty is not claimed.
5. A future PDT scalar-composition claim must state which operational procedure fixes the scalar calibration. Otherwise laws related by `L` are coordinate-equivalent.

## Research consequence
The composition program should stop searching for novelty in an unconstrained one-number law `F(a,b)`. The remaining scientifically meaningful composition target is the admissible **global distinction structure** and an independently justified operational calibration that makes a particular scalar representative physically distinguished.
