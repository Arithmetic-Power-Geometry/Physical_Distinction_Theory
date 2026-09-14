# Cycle 133 — Resolved-channel mixing selects quadratic composite resource

## Status

- **Theorem:** PROVED / CONDITIONAL / IMPORTED-KNOWN ingredients / NUMERICALLY SUPPORTED.
- **Candidate “discrete reversible symmetry is sufficient”:** FALSIFIED.
- **Extension to n=1:** FALSIFIED.
- **PDT-native derivation of resolved composite-channel additivity:** OPEN.
- **BREAKTHROUGH CANDIDATE:** NO.

The result is mathematically exact, but it is not promoted to a PDT breakthrough because the key resolved-channel additivity hypothesis has not yet been derived from PDT primitives.

## Hypotheses

Let the composite carrier be `M_n(R)` with `n >= 2`, and let `R(A) >= 0` be a composite resource with `R(0)=0`.

H1. **Resolved product-channel additivity.** In a resolved product basis,

`A = sum_ij a_ij E_ij` and `R(A) = sum_ij q_ij(a_ij)`.

H2. **Continuous local reversible covariance.** `R(U A V^T)=R(A)` for local reversible groups containing all proper two-plane rotations; `SO(n) x SO(n)` is sufficient.

H3. **Unit product-channel calibration.** `R(E_ij)=1`.

## Theorem

Under H1–H3,

`R(A) = sum_ij a_ij^2 = ||A||_F^2`.

Thus quadratic/Frobenius composite resource accounting is forced without assuming the full parallelogram law and without assuming an SVD revelation rule.

## Proof

1. `SO(n) x SO(n)` is transitive on unit coordinate directions for `n >= 2`, so H2 makes all scalar channel functions identical: `q_ij=q`.
2. A proper pi rotation in a two-plane maps a selected coordinate direction to its negative. Hence `q(-t)=q(t)`; reflections are unnecessary.
3. Let `u,v >= 0` and `r=sqrt(u+v)`. A proper two-plane rotation maps `r E_11` to `sqrt(u) E_11 + sqrt(v) E_21` (up to a harmless sign). H1 and H2 therefore give `q(sqrt(u+v)) = q(sqrt(u)) + q(sqrt(v))`.
4. Define `g(s)=q(sqrt(s))` for `s>=0`. Then `g(u+v)=g(u)+g(v)`. Since the resource is nonnegative, `g>=0`; therefore additive `g` is monotone on `R_+`. Monotonicity eliminates pathological Cauchy solutions and yields `g(s)=c s`.
5. H3 gives `q(1)=1`, hence `c=1`, so `q(t)=t^2`.
6. H1 now gives `R(A)=sum_ij a_ij^2=||A||_F^2`.

No continuity assumption on the resource is required beyond the continuous reversible group action itself; nonnegativity plus additivity supplies the regularity needed in step 4.

## Exact falsification: discrete symmetry is insufficient

Replace continuous two-plane mixing by signed permutations only. Then, for any `p>0`, `R_p(A)=sum_ij |a_ij|^p` is resolved-channel additive, normalized on every `E_ij`, and invariant under signed permutations. Therefore discrete reversible symmetry cannot select `p=2`.

An exact n=2 witness uses the 3-4-5 proper rotation of `E_11`: `E_11 -> (3/5) E_11 + (4/5) E_21`.

The mixed resource equals:

- p=1: `7/5` (violation `+2/5`),
- p=2: `1` (exactly invariant),
- p=4: `337/625` (violation `-288/625`).

This is a decisive counterexample to the weaker discrete-symmetry hypothesis.

## Edge case n=1

`SO(1)` has no nontrivial two-plane rotation. Consequently the selector mechanism disappears. For example, both `q(t)=|t|` and `q(t)=|t|^4` are nonnegative and calibrated by `q(1)=1`. Therefore `n>=2` is an essential hypothesis.

## Stress tests

The deterministic audit tests `n=1..12,16,24,32,48,64,96,128`. For each `n>=2`, 50 seeded random two-plane rotations were applied to random resolved-channel vectors. Quadratic resource had 0 failures in 900 checks. Signed-permutation covariance had 0 failures in 2700 checks across p=1,2,4. The largest relative floating residual in the quadratic rotation audit was approximately `4.35e-16`.

These numerical checks are regression evidence only; the theorem above is exact.

## Prior-art boundary

The mathematical ingredients are classical: Cauchy additivity plus nonnegativity/monotonicity implies linearity, and Frobenius/Euclidean quadratic resource is orthogonally invariant. No novelty is claimed for those facts. The PDT-specific open question is whether its operational primitives imply H1 (resolved additivity across mutually resolvable composite product channels) rather than postulating it.

## Consequence for PDT-II

The remaining bridge is now narrower than the Cycle 130/131 assumptions: `PDT primitives ?=> resolved composite-channel additivity`.

If that bridge is independently derived, continuous local reversible mixing and calibration force quadratic composite accounting automatically. Until then, the result remains conditional and must not be presented as a completed PDT-native derivation.
