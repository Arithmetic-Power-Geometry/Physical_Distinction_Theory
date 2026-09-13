# Cycle 127 — Resource-naturality no-go for nonzero bilinear composition

## Target
Attack the strongest unresolved PDT-II composition / non-circular n=3 route after Cycle 126. Cycle 126 reduced the desired selector to a nonzero same-sector bilinear composition plus proper-rotation covariance, with bilinearity obtainable conditionally from separate affinity and null absorption. A tempting next postulate is that the same composition should also be natural under every resource attenuation or coarse-graining map.

## Exact hypothesis under test
Let `V` be a real vector space and let

\[
B:V\times V\to V
\]

be bilinear. Let a uniform resource attenuation be

\[
T_\lambda=\lambda I,
\]

for some fixed \(\lambda\notin\{0,1\}\). Test the naive naturality law

\[
B(T_\lambda x,T_\lambda y)=T_\lambda B(x,y)
\quad\forall x,y.
\]

## Theorem — single-contraction naturality kills every nonzero bilinear law
By bilinearity,

\[
B(\lambda x,\lambda y)=\lambda^2 B(x,y).
\]

Naive resource naturality instead requires this to equal

\[
\lambda B(x,y).
\]

Therefore

\[
\lambda(\lambda-1)B(x,y)=0
\]

for all \(x,y\). Since \(\lambda\notin\{0,1\}\),

\[
\boxed{B=0.}
\]

The converse is immediate. Thus a *single* nontrivial uniform contraction is already sufficient to make exact same-map naturality incompatible with the nonzero bilinear composition needed by the current n=3 route.

**Classification:** PROVED + FALSIFIED.

## Smallest decisive counterexample to the candidate postulate
Already in dimension one, take

\[
B(x,y)=xy,\qquad x=y=1,\qquad \lambda=\tfrac12.
\]

Then

\[
B(T_\lambda x,T_\lambda y)=\tfrac14,
\qquad
T_\lambda B(x,y)=\tfrac12.
\]

Hence the proposed naturality law fails by \(-1/4\). No high-dimensional or quantum construction is needed.

## Surviving strengthened law
The correct homogeneous covariance for a degree-two composition is

\[
\boxed{
B(T_\lambda x,T_\lambda y)=T_{\lambda^2}B(x,y)
}
\]

rather than same-map covariance. More generally, a homogeneous operation of total degree \(k\) scales with \(\lambda^k\).

This matters conceptually: **reversible symmetry covariance and resource/coarse-graining transport cannot automatically be represented by the same naturality equation.** The SO(n) covariance used in the conditional n=3 selector is degree-preserving because rotations do not attenuate magnitude. Resource restriction generally changes scale and needs its own transport law.

## Stress audit
Executable audit: `cycle127_resource_naturality_no_go.py`.

Dimensions:

`1..12, 16, 24, 32, 48, 64, 96, 128`

Attenuations:

`lambda = 0.25, 0.5, 0.75`

20 deterministic seeded trials per dimension/attenuation pair, total 1,140 trials, using the nonzero same-sector bilinear witness \(B(x,y)=x\odot y\).

Frozen result:

- naive same-map naturality had nonzero residual: **1,140 / 1,140**;
- exact residual identity \(B(\lambda x,\lambda y)-\lambda B(x,y)=\lambda(\lambda-1)B(x,y)\): **0 failures**;
- corrected degree-two covariance \(B(\lambda x,\lambda y)=\lambda^2B(x,y)\): **0 failures**.

The numerical sweep is regression evidence only; the theorem is exact and dimension-independent.

## Prior-art / novelty boundary
The proof is elementary homogeneity and is **not claimed as a new mathematical theorem**. General resource theories distinguish free transformations, resource-preserving properties, and compositional structure; those frameworks already caution against identifying distinct operational maps merely because they are all called resource transformations. Relevant established resource-theory work includes resource preservability and compositional resource theories. The PDT-specific value here is a falsification guard: the current n=3 program must not impose identical input/output attenuation naturality on a nonzero bilinear composition.

**Classification:** IMPORTED/KNOWN boundary + PDT-specific no-go formulation.

## Consequence for PDT-II
The surviving composition route is now constrained to separate two transformation classes:

1. **reversible geometric symmetry**, for which ordinary SO(n)-equivariance of a nonzero same-sector bilinear law remains the conditional n=3 selector;
2. **resource restriction/refinement**, for which composition must obey a degree-aware or otherwise independently derived transport law, not naive same-map covariance.

A future PDT-native derivation must explain the resource transport exponent/law physically. Simply demanding commutation with every resource map would kill the desired composition before any dimensional selection occurs.

## Status
- **PROVED:** single nontrivial contraction + bilinearity + same-map naturality implies zero composition.
- **FALSIFIED:** arbitrary-resource-map same-map naturality as a route to a nonzero PDT composition.
- **NUMERICALLY SUPPORTED:** deterministic dimension stress audit has no regression failures.
- **IMPORTED/KNOWN:** underlying homogeneity argument and general resource-theory setting.
- **OPEN:** derive a PDT-native resource transport law and same-sector composition without assuming the desired n=3 structure.
- **BREAKTHROUGH CANDIDATE:** NO.
