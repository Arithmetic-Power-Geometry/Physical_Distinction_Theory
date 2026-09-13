# Cycle 123 — Same-input probability-deformation no-go

## Target
Can PDT obtain a quantitative same-input deviation from quantum mechanics merely by making the probability assignment resource-dependent while leaving the microscopic quantum state and measurement effect unchanged?

## Candidate family
For a binary quantum event with Born probability q in [0,1], consider the normalized power deformation

p_lambda(q;R) = q^alpha / (q^alpha + (1-q)^alpha),  alpha = 1 + lambda R > 0.

For alpha != 1 this gives an explicit same-state/same-effect numerical deviation for generic q. Example: q=1/4 and alpha=2 gives p=1/10, hence Delta=-3/20.

## Exact falsification: affine-mixture consistency
A preparation probability rule compatible with ordinary classical randomization must satisfy

p(t q1 + (1-t) q2) = t p(q1) + (1-t) p(q2)

for all q1,q2,t in [0,1]. The power deformation violates this whenever alpha != 1. Small exact witness for alpha=2:

q1=0, q2=1/2, t=1/2.

The mixed Born probability is q=1/4, so p(1/4)=1/10, whereas the classical mixture of the deformed probabilities is (1/2)p(0)+(1/2)p(1/2)=1/4. Residual = -3/20.

Thus this candidate obtains P_PDT != P_QM only by abandoning ordinary affine preparation mixing. It is not a free same-input correction.

## Stronger surviving theorem
For a binary event, if f:[0,1]->[0,1] obeys affine mixture consistency for all q1,q2,t and retains certainty endpoints f(0)=0 and f(1)=1, then

f(q)=q.

Proof: q = q*1 + (1-q)*0, hence by affinity f(q)=q f(1)+(1-q)f(0)=q.

Therefore any scalar resource-conditioned probability deformation f_R(q) that keeps classical randomization affine and certainty endpoints fixed is exactly Born on the binary probability coordinate, for every fixed R.

## Consequence for PDT-II
A genuine same-input PDT deviation cannot be obtained from a scalar remapping of Born probability while retaining ordinary mixture affinity and certainty. It must identify an explicit physical escape coordinate: non-affine/contextual preparation statistics, changed dynamics/process, changed physical effect, or a resource window that physically changes the experiment. Any such escape must then be tested for no-signalling, preparation-context dependence, sequential consistency and existing experimental bounds.

## Prior-art boundary
The affinity/no-signalling/Gleason family of constraints is established quantum-foundations mathematics. Recent 2025–2026 Born-rule tests and proposals also explicitly constrain nonlinear probability assignments. This cycle is a PDT falsification guard, not a novelty claim.

## Status
- Binary affine-lock theorem: PROVED; IMPORTED/KNOWN boundary.
- Normalized power deformation as same-input PDT law: FALSIFIED under ordinary affine preparation mixing.
- Quantitative witness Delta=-3/20: PROVED.
- Genuine PDT-native same-input deviation: OPEN.
- BREAKTHROUGH CANDIDATE: NO.
