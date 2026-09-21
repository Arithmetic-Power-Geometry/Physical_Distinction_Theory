# PDT Cycle 308 — Distinction does not determine the allowed effect set

## Target
Attack Cycle 307's strongest open prerequisite: can PDT's distinction primitive itself uniquely restrict the allowed effects and thereby supply a native response law?

## Candidate principle
Let a normalized convex state space `Omega` have an allowed convex effect set `E`, containing `0,u` and closed under complements `e -> u-e`. Define

`D_E(omega,sigma)=sup_{e in E} |e(omega)-e(sigma)|`.

Candidate: knowing `Omega` and the full pairwise function `D_E` determines `E`.

## Result
**FALSIFIED.** Distinction sees differences of effect values; distinct effect sets can have the same extremal slopes on every state difference while differing in offsets and therefore in absolute response probabilities.

## Small exact counterexample: classical bit
Take `Omega=[0,1]`. Write affine effects as

`e_{s,t}(p)=1/2+s(p-1/2)+t`.

Positivity on the entire bit is equivalent to `|t|+|s|/2 <= 1/2`.

Fix `c=1/2` and define

`E1=conv{0,u,e_{c,0},e_{-c,0}}`.

In `(s,t)` coordinates centered at `u/2`, this is exactly

`|s|/c+2|t|<=1`.

Let `f=e_{1/4,3/10}` and

`E2=conv(E1 union {f,u-f})`.

The new effect is physically valid because

`3/10+1/8=17/40<1/2`.

But it is outside `E1`, since

`|1/4|/(1/2)+2(3/10)=1/2+3/5=11/10>1`.

Thus `E1` is a strict subset of `E2`. Both are convex, contain `0,u`, and are complement-closed.

For any states `p,q`,

`e_{s,t}(p)-e_{s,t}(q)=s(p-q)`.

Every effect in either set has `|s|<=1/2`, while `e_{1/2,0}` is present in both. Therefore, exactly,

`D_E1(p,q)=D_E2(p,q)=(1/2)|p-q|`

for every pair `p,q`.

Yet their allowed responses differ: at `p=1/2`, `f(1/2)=4/5`, and `f` is an allowed event only in `E2`.

Hence complete pairwise operational distinction does not reconstruct the event/effect set.

## General mechanism
Normalized state differences lie in the zero-normalization tangent subspace. `D_E` depends on the support function of the projection of the centered effect set onto the dual of that difference subspace. Absolute-offset structure can vary without changing that projected extremal support. Complement closure does not remove the freedom.

The bit witness embeds in every finite `n>=2` simplex by restricting attention to a one-dimensional face / effects depending on two coordinates. Hence the obstruction persists through `n=2..12` and arbitrary higher finite dimensions. `n=1` is degenerate and has no nontrivial state distinction.

## Consequences
1. A PDT primitive consisting only of pairwise distinguishability cannot uniquely derive the allowed effect set.
2. It therefore cannot by itself close T3a (`Phi_PDT`) or yield a parameter-free same-input PDT/QM probability difference.
3. PDT needs additional native information beyond the pairwise distinction metric: absolute calibration/order-unit structure plus an effect-selection law, richer multi-event/sequential data, or another independently derived physical restriction.
4. Any such structure must be checked against GPT/quantum prior art rather than counted as PDT novelty by construction.

## Prior-art boundary
The underlying mechanism is convex-geometric/operational and is **IMPORTED/KNOWN in substance**: distinguishability norms induced by restricted measurements/effects are established in GPT and quantum information. The PDT-specific result here is a no-go obligation, not a novelty claim: inversion from a pairwise distinction metric to the full effect set is non-unique without extra hypotheses.

## Status ledger
- `D_E` uniquely determines a convex complement-closed allowed effect set: **FALSIFIED**.
- Exact classical-bit witness `E1 != E2` with identical `D_E`: **PROVED**.
- Persistence for `n=2..12` and arbitrary finite `n` by embedding: **PROVED**.
- Restricted-measurement / convex-geometric mechanism: **IMPORTED/KNOWN in substance**.
- Pairwise PDT distinction alone selects `Phi_PDT`: **FALSIFIED** under the stated formulation.
- PDT-native richer invariant/effect selector: **OPEN**.
- Non-circular `n=3` derivation: **OPEN**.
- Same-input parameter-free PDT/QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Test whether augmenting pairwise distinction by a PDT-native multi-event or sequential-distinction object determines the missing absolute effect structure without assuming a GPT effect cone. Prove injectivity under explicit hypotheses or find the smallest counterexample. Also reject any proposed experimental inequality whose claimed PDT bound depends only on `D_E` when response theories sharing that `D_E` can differ in absolute event probabilities.