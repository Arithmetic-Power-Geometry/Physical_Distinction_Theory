# Cycle 147 — Majorization Squeeze for Resolved Resource Composition

## Status

- **PROVED:** endpoint-calibrated Schur monotonicity forces additive resolved-share accounting on each fixed-total simplex.
- **CONDITIONAL:** this yields PDT composition only if PDT-native operational primitives independently imply Schur monotonicity and the two endpoint calibrations.
- **IMPORTED/KNOWN:** majorization and Schur monotonicity are classical mathematical machinery.
- **NUMERICALLY SUPPORTED:** seeded dimension stress audit through n=128 and exact n=2 witness.
- **FALSIFIED:** the Cycle-146 continuous tensor-multiplicative deformation cannot also satisfy either Schur-convexity or Schur-concavity.
- **OPEN:** derive majorization monotonicity from PDT refinement/revelation/reversible-mixing semantics without importing additivity or entropy.
- **BREAKTHROUGH CANDIDATE:** NO.

## Theorem (majorization squeeze)

Fix n >= 1 and S >= 0. Let Delta_n(S) = {q in R_+^n : sum_i q_i = S}. Suppose F_n: Delta_n(S) -> R obeys:

1. Pure calibration: F_n(S,0,...,0) = S.
2. Uniform calibration: F_n(S/n,...,S/n) = S for S>0 (and F_n(0,...,0)=0).
3. F_n is Schur-monotone on Delta_n(S), in either one globally declared orientation: Schur-convex or Schur-concave.

Then for every q in Delta_n(S), F_n(q) = S = sum_i q_i.

### Proof

For every q in Delta_n(S), standard majorization gives

    (S,0,...,0) majorizes q majorizes (S/n,...,S/n).

If F_n is Schur-convex, monotonicity and endpoint calibration give

    S = F_n(pure) >= F_n(q) >= F_n(uniform) = S.

Hence F_n(q)=S. If F_n is Schur-concave, both inequalities reverse and again squeeze F_n(q) to S. No continuity, differentiability, tensor-product axiom, or explicit unequal-additivity axiom is required. QED.

## Exact counterexample to extending Cycle 146

Cycle 146 used

    Phi(q) = (sum_i q_i^2)^2 / (sum_i q_i^3), q != 0.

For the fixed-total n=2 simplex at S=1, let p=(1,0), m=(3/4,1/4), u=(1/2,1/2). Then p majorizes m majorizes u, but

    Phi(p)=1, Phi(m)=25/28, Phi(u)=1.

Thus Phi is neither Schur-convex nor Schur-concave. The exact midpoint deficit from both calibrated endpoints is -3/28.

## Stress audit

The executable audit tests dimensions 1..12, 16, 24, 32, 48, 64, 96, 128 with frozen seed 147. It contains 1320 majorization chains. Endpoint residual failures: 0; maximum endpoint residual: 6.661338147750939e-16. The Cycle-146 deformation shows 1240 Schur-convex orientation violations and 1240 Schur-concave orientation violations across sampled nontrivial chains. Local regression suite: 6/6 passed.

The numerical audit is implementation and counterexample evidence, not the proof of the squeeze theorem.

## Prior-art boundary

Majorization, Schur-convexity/concavity, and the ordering of pure/intermediate/uniform vectors on a fixed-sum simplex are classical. See Marshall, Olkin & Arnold, *Inequalities: Theory of Majorization and Its Applications*, 2nd ed., Springer (2011), and the Hardy–Littlewood–Polya majorization theorem. The mathematical squeeze mechanism is not claimed as PDT novelty.

## PDT-II implication

This closes a large family of continuous, multiplicative, nonadditive composition alternatives **conditionally**. The remaining native obligation is:

> Can PDT derive one-direction Schur monotonicity of resolved resource under physically defined mixing/refinement/revelation operations, together with pure and uniform endpoint calibration, without assuming the desired additive law?

Only if that bridge is independently derived can this theorem become a PDT-native composition result.
