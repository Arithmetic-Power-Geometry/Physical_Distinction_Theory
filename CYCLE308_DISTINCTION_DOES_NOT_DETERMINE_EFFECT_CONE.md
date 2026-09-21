# PDT Cycle 308 — Distinction does not determine the allowed effect set

## Target
Attack Cycle 307's strongest open prerequisite: can PDT's distinction primitive itself uniquely restrict the allowed effects and thereby supply a native response law?

## Candidate principle
Let a normalized convex state space `Omega` have an allowed convex effect set `E`, containing `0,u` and closed under complements `e -> u-e`. Define operational distinction

`D_E(omega,sigma)=sup_{e in E} |e(omega)-e(sigma)|`.

Candidate: knowing `Omega`, reversible symmetry, and the full pairwise function `D_E` determines `E`.

## Result
**FALSIFIED.** The distinction function sees only differences of effect values. Distinct effect sets can have exactly the same extremal slope on every state difference while differing in their offsets and hence in absolute response probabilities.

## Small exact counterexample: classical bit
Take `Omega=[0,1]`, with normalized states labelled by `p`. Write affine effects as

`e_{s,t}(p)=1/2 + s(p-1/2)+t`.

Positivity on the entire bit requires `|t|+|s|/2 <= 1/2`.

Fix `c=1/2`. Define

`E1 = conv{0,u,e_{c,0},e_{-c,0}}`.

Equivalently, in `(s,t)` coordinates centered at `u/2`,

`E1: |s|/c + 2|t| <= 1`.

Now let `f=e_{1/4,1/5}` and define

`E2 = conv(E1 union {f,u-f})`.

`f` is a valid effect because `1/5 + (1/4)/2 = 13/40 < 1/2`. It is not in `E1`, because

`|1/4|/(1/2) + 2|1/5| = 1/2+2/5 = 9/10 <= 1`.

This particular value is actually inside `E1`, so it is not a counterexample. Strengthen the offset to `t=3/10` instead. Then positivity remains valid:

`3/10+1/8=17/40 < 1/2`,

while the `E1` membership expression is

`1/2+3/5=11/10>1`.

Therefore use `f=e_{1/4,3/10}` below.

Both sets are convex, contain `0,u`, and are complement-closed. `E2` is a strict enlargement of `E1`.

For any two states `p,q`,

`e_{s,t}(p)-e_{s,t}(q)=s(p-q)`.

Every effect in either set has `|s|<=c=1/2`, while `e_{c,0}` is present in both. Hence exactly

`D_E1(p,q)=D_E2(p,q)=(1/2)|p-q|`

for every pair `p,q`.

Yet the response theories differ. For example at `p=1/2`, the new effect gives

`f(1/2)=1/2+3/10=4/5`,

whereas `f` is not an allowed event in `E1`.

Thus even complete knowledge of all pairwise operational distinctions does not reconstruct the event/effect set.

## General mechanism
On a normalized affine state space, state differences lie in the zero-normalization tangent subspace. `D_E` depends on the support function of the projection of the centered effect set onto the dual of that difference subspace. Components that change absolute offsets while leaving that projection's extremal support unchanged are invisible to pairwise distinction. Complement closure does not remove this freedom.

The bit witness is already decisive. It embeds into every finite `n>=2` simplex by making the effects depend only on two coordinates / a one-dimensional face, so the obstruction survives the required `n=2..12` stress range and arbitrary higher finite dimensions.

## Consequences
1. A PDT primitive consisting only of pairwise distinguishability cannot uniquely derive the allowed effect cone/set.
2. Therefore it cannot, by itself, close T3a (`Phi_PDT`) or generate a parameter-free same-input PDT/QM probability difference.
3. A valid PDT response theory needs additional native information beyond the distinction metric: e.g. absolute calibration/order-unit structure plus a rule selecting effects, richer multi-event data, or an independently derived physical restriction.
4. Any such additional structure must be tested for whether it merely reimports GPT/quantum assumptions.

## Prior-art boundary
The mechanism is convex-geometric/operational rather than claimed PDT novelty: distinguishability norms are induced by allowed measurements/effects, and restricted-measurement norms are established in GPT/quantum information. This cycle records a PDT-specific no-go obligation: inversion from the distinction metric back to the full allowed effect set is non-unique without extra assumptions.

## Status ledger
- `D_E` uniquely determines a convex complement-closed allowed effect set: **FALSIFIED**.
- Exact classical-bit counterexample with `E1 != E2` but identical `D_E`: **PROVED**.
- Persistence for `n=2..12` and arbitrary finite `n` by embedding: **PROVED**.
- Convex-geometric/restricted-measurement mechanism: **IMPORTED/KNOWN in substance**.
- PDT distinction primitive alone selects `Phi_PDT`: **FALSIFIED** under the stated pairwise-metric formulation.
- PDT-native richer invariant/effect selector: **OPEN**.
- Non-circular `n=3` derivation: **OPEN**.
- Same-input parameter-free PDT/QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Test whether augmenting pairwise distinction by a PDT-native multi-event or sequential-distinction object can determine the missing absolute effect structure without simply assuming a GPT effect cone. Prove injectivity under explicit hypotheses or construct the smallest counterexample. In parallel, reject any proposed experimentally distinctive inequality whose bound depends only on `D_E` if two response theories with the same `D_E` can give different absolute event probabilities.