# PDT Completion Attack — 2026-09-07

## Purpose

This file records the strongest theorem closure currently defensible for Physical Distinction Theory (PDT). It deliberately separates: (i) exact PDT-native theorems, (ii) imported reconstruction theorems, (iii) no-go results showing what cannot follow from the present primitive alone, and (iv) the minimal additional operational principles required for a complete quantum-side reconstruction.

## 1. Exact PDT-native data-processing theorem

For a resource profile R, let A_R be the admissible decision procedures and let u_R(a,omega) be the expected distinction payoff. Define

Delta_R(omega,sigma) = sup_{a in A_R} |u_R(a,omega)-u_R(a,sigma)|.

Assume physical closure under precomposition: for every admissible channel Phi taking R to R', and every b in A_{R'}, the pulled-back decision b o Phi belongs to A_R with the required resource accounting. Then

Delta_{R'}(Phi omega, Phi sigma) <= Delta_R(omega,sigma).

Proof: substitute the pulled-back procedures into the supremum. No Hilbert-space, Born-rule, BQDC, or quantum assumption is used.

If a recovery map Psi is admissible for the pair, Psi Phi omega=omega and Psi Phi sigma=sigma, then data processing in both directions gives equality:

Delta_{R'}(Phi omega,Phi sigma)=Delta_R(omega,sigma).

Thus PDT has an exact operational sufficiency/recoverability theorem.

## 2. Scalar-capacity no-go theorem

The scalar one-bit condition K_epsilon=1 bit (maximal perfectly distinguishable code size two) cannot determine local geometry. Distinct compact convex operational state spaces can have the same binary capacity while having inequivalent norms and correlation structures.

A concrete foil family is the strictly convex l_p ball B_p^d for 1<p<infinity. Binary perfect discrimination is possible for antipodal states, while strict convexity prevents a three-state perfectly distinguishable frame under the standard full-dual effect setting. Yet for x=e_1 and y=e_2,

||x+y||_p^2 + ||x-y||_p^2 = 2^(1+2/p),

whereas 2||x||_p^2+2||y||_p^2=4. Equality occurs only for p=2.

Therefore

K_epsilon=1 bit does NOT imply BQDC, Euclidean geometry, self-duality, spectrality, or quantum theory.

Logical corollary: no theorem whose only state-space input is the scalar value K_epsilon can select the Bloch ball, because the same scalar value occurs in non-Euclidean foils.

## 3. Neutral-state and erasure lemmas

Let G be a compact reversible group acting transitively on pure states. Haar averaging any pure state gives

mu = integral_G g alpha dg.

This state is G-invariant and independent of the chosen pure state. Hence the completely symmetrized neutral state is derived from reversible transitivity.

If ordered perfectly distinguishable pairs are reversibly equivalent, then for each pair (alpha,beta) there is a reversible swap S with S alpha=beta and S beta=alpha. The randomized map

E=(I+S)/2

sends both endpoints to (alpha+beta)/2. Thus unbiased pair erasure is derived.

What is not automatic is the identification (alpha+beta)/2=mu. That requires an additional physical statement: complete unbiased erasure of a maximal elementary distinction leaves no residual label of which distinction was erased.

## 4. Elementary Euclidean rigidity theorem (conditional but direct)

Assume for an irreducible elementary system:

E1. Binary maximal distinguishability.
E2. Complete elementary resolution: every state is a mixture of one maximal perfectly distinguishable pair.
E3. Unbiased erasure uniqueness: the midpoint of every maximal pair equals the invariant neutral state mu.
E4. Continuous reversible pure-state transitivity.

Center K=Omega-mu. Then perfectly distinguishable partners are antipodal. Every state has the radial form

omega-mu = r x,  -1<=r<=1,

for a centered pure state x. Interior points have |r|<1, so the full boundary equals the pure-state set. Reversible transformations fix mu and act linearly on K; by pure transitivity the reversible group is transitive on the full boundary.

Choose any auxiliary inner product and Haar-average it over the compact reversible group. The resulting positive-definite inner product is group-invariant. Since the boundary is one group orbit, its averaged Euclidean norm is constant on the full boundary. Therefore the boundary is one Euclidean sphere in that inner product and K is an ellipsoid. After affine normalization,

Omega is B^n.

Consequently BQDC follows as the parallelogram identity of the derived inner product.

This proof is direct convex/group geometry. The compact-group averaging lemma is standard mathematics; the potentially new PDT contribution is the upstream physical-distinction/erasure interpretation and theorem chain.

## 5. Independent information-geometric route

Define a state-resolved decision value F_R(omega)=sup_a u_R(a,omega). Convexity follows because it is a supremum of affine functions. Proper scoring theory can turn a smooth convex entropy/value function into Bregman regret. However, the exact PDT metric Delta_R being contractive does NOT by itself imply that an arbitrary Bregman regret generated from F_R is contractive, because the supporting action at the reference state can change after coarse graining.

Hence the bridge

PDT discrimination -> canonical monotone Bregman regret

is not yet derived from the existing primitive alone.

If such a monotone Bregman regret is supplied or independently derived, Harremoes' rank-two theorem implies ball/spin-factor geometry. This is an imported theorem and must be cited, not claimed as new.

## 6. Why the missing Bregman bridge cannot be forced from scalar capacity alone

There is a structural obstruction. The map omega -> K_epsilon is a global integer/code-size statistic, whereas a Bregman divergence depends on local directional curvature (the Hessian of a convex generator where smooth). Two state spaces can have the same maximal code size while carrying inequivalent tangent geometries. Therefore local Hessian geometry is not identifiable from the scalar capacity value without additional state-resolved operational data.

Thus any claimed derivation

K_epsilon alone -> unique monotone Bregman geometry

is underdetermined. A valid completion must add a state-resolved principle (proper decision sufficiency, purification/sharpness, subspace equivalence, or equivalent structure).

## 7. Quantum completion using explicit operational principles

Once the elementary state space is B^n, established reconstruction results can be used. Under local tomography, continuous reversible dynamics, and a genuine reversible interaction of two generalized bits, known ball-composite classification singles out the three-dimensional Bloch ball in the relevant setting:

B^n -> B^3.

B^3 is affinely the qubit state space rho=(I+x.sigma)/2.

To reconstruct arbitrary finite-dimensional complex quantum systems, one must add suitable composite/Jordan or equivalent reconstruction assumptions. Known routes include Masanes-Muller physical-requirements reconstructions and Barnum-Wilce/Hanche-Olsen-type Jordan composite selection. These are imported results, not PDT-native theorems.

Thus a defensible complete quantum-side theorem is conditional:

PDT elementary resolution + unbiased erasure + continuous reversible symmetry
+ local tomography + genuine reversible interaction
+ suitable global composite/subspace principle
=> finite-dimensional complex quantum theory.

The novelty can only reside in deriving or physically motivating the upstream PDT principles more economically than prior reconstruction axioms.

## 8. Born and dynamics status

Once complex quantum state/effect structure is reconstructed, affine normalized effects give the standard trace pairing p(E|rho)=Tr(rho E), and rank-one projectors yield the Born rule. Connected continuous reversible transformations are unitary, giving standard Hamiltonian/Schrodinger evolution. These are standard consequences of reconstructed quantum structure, not separate PDT discoveries.

Before full complex-QM reconstruction, PDT also has a narrower conditional Born theorem: if outcome weight is a continuous nonnegative function F of quadratic distinction power Q_D and mutually exclusive orthogonal coarse-graining is additive, then F(s+t)=F(s)+F(t) forces F(s)=c s and normalized probabilities are quadratic.

## 9. Gravity-side normalization no-go theorem

Suppose PDT determines only a local capacity measure up to proportionality,

d mu_K = kappa_0 dV_g,

or a screen law up to an unknown constant,

K_partial = c A/l_P^2.

The transformation K -> lambda K for any lambda>0 preserves order, additivity, monotonicity, distinguishability rankings, and all dimensionless qualitative operational statements, but changes kappa_0 and c. Therefore the exact coefficient 1/(4 ln 2) cannot be fixed from scale-free distinction axioms alone.

An absolute physical calibration connecting one distinction bit to energy/entropy/action is mathematically necessary. Importing the Bekenstein bound plus Schwarzschild saturation supplies the coefficient, but that is not a PDT-only derivation.

This is a normalization no-go theorem: exact horizon entropy normalization is unidentifiable until PDT contains an absolute calibration principle.

## 10. Gravity-dynamics no-go theorem

A measure relation d mu_K proportional to dV_g determines a measure/volume structure but not a gravitational field equation. Distinct metric dynamics can share the same local volume element and causal kinematics. Therefore capacity-volume proportionality alone cannot imply Einstein's equation.

To obtain Einstein dynamics one must add a dynamical relation such as local horizon thermodynamic equilibrium/Clausius response, an action principle, or another law linking capacity variation to stress-energy. Jacobson's route is a valid imported conditional bridge, not an independent PDT derivation.

## 11. Final theorem-closure statement

The present PDT primitive does not contain enough information to derive every remaining quantum and gravity structure without further operational/dynamical principles. This is not a missing algebra trick; it is an identifiability obstruction demonstrated by explicit foil families and normalization freedom.

What is now complete is the logical map:

(A) Exact PDT-native results:
- resource-bounded distinction data processing;
- equality under recoverability;
- neutral state by Haar averaging;
- unbiased erasure map from pair reversal;
- conditional radial/ellipsoid rigidity;
- conditional BQDC;
- scalar-capacity no-go;
- horizon-normalization no-go;
- gravity-dynamics no-go.

(B) Imported but rigorous completion bridges:
- rank-two monotone Bregman divergence -> ball/spin factor;
- Euclidean generalized-bit composites under the stated interaction/local-tomography hypotheses -> B^3;
- suitable global reconstruction/composite principles -> complex finite-dimensional QM;
- Bekenstein/Jacobson relations for the gravitational conditional limits.

(C) Irreducible principles still required if the goal is a full theory rather than a conditional reconstruction:
1. A state-resolved elementary completeness principle (or a derivation of spectrality/resolution from a new PDT-native principle).
2. A global composition/subspace principle sufficient to reconstruct all complex quantum systems, not only the elementary B^3 sector.
3. An absolute distinction-to-entropy/energy calibration fixing the horizon coefficient.
4. A dynamical capacity-stress relation fixing gravitational field equations.

## 12. Recommended paper claim

Do NOT claim 'PDT derives all quantum mechanics and gravity from K_epsilon alone.'

The strongest defensible claim is:

Physical Distinction Theory supplies a resource-bounded operational distinction primitive with an exact data-processing/sufficiency structure; proves that scalar binary capacity alone is insufficient; identifies physically interpretable resolution/erasure conditions under which elementary state spaces are forced to be Euclidean balls and BQDC follows; and then connects this PDT-derived elementary geometry to established reconstruction theorems selecting the Bloch ball and complex quantum theory under explicit composite assumptions. On the geometry side, PDT yields conditional capacity-measure results and sharp no-go statements showing exactly which absolute calibration and dynamical principles are still necessary.

This theorem/no-go closure is stronger scientifically than an unsupported '100/100 complete' claim because every remaining assumption is now exposed and independently falsifiable.
