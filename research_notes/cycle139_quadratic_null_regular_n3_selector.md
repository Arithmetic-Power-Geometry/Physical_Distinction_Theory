# Cycle 139 — quadratic-null regularity bridge to bilinearity and the n=3 selector

## Status
**PROVED (conditional theorem) / FALSIFIED (two weakened routes) / IMPORTED-KNOWN / NUMERICALLY SUPPORTED / OPEN.**

**BREAKTHROUGH CANDIDATE: NO.** Bilinearity no longer has to be assumed as a primitive in Cycle 137; it follows from a weaker exact scaling/regularity bridge. PDT still has to derive that bridge from its own operational primitives.

## Conditional theorem
Let V=R^n and B:VxV->V. Put F(x,y)=B(x,y) on W=V⊕V. Assume: (1) F(tz)=t^2F(z) for all t>=0; (2) F is twice Frechet differentiable at z=0; (3) B(x,0)=B(0,y)=0; (4) B(y,x)=-B(x,y); (5) B(Rx,Ry)=RB(x,y) for every R in SO(n); (6) B is nonzero. Then n=3.

### Proof
Degree-2 homogeneity gives F(0)=0. Differentiability at 0 gives DF(0)=0 because F(tz)/t=tF(z)->0. Taylor expansion gives F(tz)=t^2/2 D^2F(0)[z,z]+o(t^2). Divide by t^2 and use exact homogeneity; t->0+ yields the global identity F(z)=1/2 D^2F(0)[z,z]. Thus F is exactly quadratic.

Let H=D^2F(0), symmetric bilinear on W. For z=(x,y), sector-nullness kills the two pure blocks, leaving B(x,y)=H((x,0),(0,y)), hence B is separately bilinear. Assumptions 4-6 now reduce to Cycle 137's nonzero alternating bilinear SO(n)-equivariant map; the stabilizer argument forces n=3.

## Kill tests
### Degree-2 scaling without C2 is insufficient
For every n>=1, B2(x,y)=||y||x-||x||y is nonzero, alternating, sector-null, O(n)-equivariant and exactly positive 2-homogeneous. It survives every dimension but is not quadratic/C2 at the joint null point. Smallest exact witness: n=1, u=(1,1), v=(1,-1); the quadratic parallelogram identity has LHS 0 and RHS 4.

### Smoothness without degree-2 scaling is insufficient
Cycle 138's B3(x,y)=||y||^2x-||x||^2y is C-infinity, alternating, sector-null and O(n)-equivariant in every dimension, but joint degree 3, not degree 2.

## Stress audit
Dimensions n=1..12,16,24,32,48,64,96,128; seed 139; 1300 random cases per family. All intended covariance, alternation, sector-nullness and correct-degree scaling checks had zero failures. Maximum residual <=1.47e-15. The smooth cubic family violated degree-2 scaling in 1300/1300 tests. Local regression suite: 3/3 passed.

## Prior-art boundary
The second-order Taylor/Hessian step and quadratic-form/symmetric-bilinear correspondence are standard analysis/linear algebra and are not PDT novelty. Classical vector-cross-product literature includes Brown & Gray, *Vector Cross Products*, Comment. Math. Helv. 42 (1967), 222-236. PDT novelty, if eventually established, must lie in a native operational derivation of the scaling/regularity hypotheses, not these imported implications.

## Next obligation
Derive or falsify from PDT-native distinguishability/revelation/composition primitives the exact response law F(tz)=t^2F(z), together with enough second-order null regularity to justify the Hessian bridge. Do not assume these merely to obtain n=3.
