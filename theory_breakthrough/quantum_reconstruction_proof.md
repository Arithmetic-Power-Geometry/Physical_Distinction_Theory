# PDT Quantum Reconstruction: Formal Proof Chain

## Scope

This note records the strongest defensible quantum-side derivation. Statements marked **PDT proof** are elementary derivations given here. Statements marked **imported theorem** use established literature and must be cited as such in any manuscript.

---

## Definitions

Let `Omega` be a finite-dimensional compact convex normalized state space, `G` its group of reversible affine transformations, and `Pure(Omega)` its pure states. A frame is an ordered list of mutually perfectly distinguishable pure states. An elementary system has maximal frame size two.

Let the resource-bounded PDT code capacity be

`K_epsilon(Omega;R) = sup_C log_2 |C|`,

where `R=(E,tau,A,R_region,...)` is the operational resource profile and the supremum is over physically admissible codebooks meeting the discrimination threshold.

The global code capacity `K_epsilon` must be distinguished from the local quadratic distinction power `Q_D`; equating them is not currently justified.

---

## Theorem 1 — invariant neutral state from reversible transitivity (**PDT proof**)

Assume `G` is compact and transitive on pure states. Choose any pure state `alpha` and define

`mu = integral_G g(alpha) dg`

with normalized Haar measure. Then `mu` is invariant under every reversible transformation and is independent of the chosen pure state.

### Proof
For `h in G`, Haar invariance gives

`h(mu)=integral_G h g(alpha) dg = integral_G g(alpha) dg = mu`.

If `beta=k(alpha)` is another pure state, then

`integral_G g(beta) dg = integral_G g k(alpha) dg = mu`.

By finite-dimensional convexity every state is a convex combination of pure states, so averaging any normalized state also gives `mu`. QED.

Interpretation: the maximally symmetrized neutral state is derived; it need not be postulated independently.

---

## Theorem 2 — unbiased erasure map for a distinguishable pair (**PDT proof**)

Assume ordered perfectly distinguishable pairs are reversibly equivalent, including reversal. For a pair `(alpha,beta)` there exists a reversible `S` with `S alpha=beta` and `S beta=alpha`. Define

`E_ab = (I+S)/2`.

Then

`E_ab(alpha)=E_ab(beta)=(alpha+beta)/2`.

Thus an operationally unbiased erasure channel for the binary label exists.

What is **not** automatic is that `(alpha+beta)/2 = mu`. The latter requires an additional erasure-uniqueness/completeness condition.

---

## Principle CEU — Complete-Erasure Uniqueness

If a process completely erases a maximal elementary distinction without introducing another physical distinction, its output is the invariant state `mu`.

Together with Theorem 2:

`(alpha+beta)/2 = mu`.

Hence, after centering, perfectly distinguishable pure partners are antipodes:

`beta-mu = -(alpha-mu)`.

This principle is operational and falsifiable; it is not a Euclidean, Hilbert, Born, or BQDC assumption.

---

## Principle CER — Complete Elementary Resolution

Every normalized state of an elementary rank-two system is completely specified by one maximal binary distinction and its bias:

`omega = p alpha + (1-p) beta`,  `alpha perp_D beta`, `0<=p<=1`.

Equivalently, an elementary state contains no irreducible residual distinction once a maximal binary direction and its bias are specified.

Important: maximal codebook size two **alone does not prove CER**. CER must either be postulated or derived from a stronger sufficiency/information principle; see `capacity_bridge_attack.md`.

---

## Theorem 3 — radial representation (**PDT proof**)

Assume CEU and CER. Let `x=alpha-mu`. Since `beta-mu=-x`,

`omega-mu = (2p-1)x = r x`, where `-1<=r<=1`.

Therefore

`Omega-mu = { r x : x in P, -1<=r<=1 }`,

where `P={alpha-mu: alpha pure}`.

Consequences:

1. `K:=Omega-mu` is centrally symmetric: `K=-K`.
2. Every interior radial point with `|r|<1` is mixed.
3. Every boundary point is pure, hence `partial K = P`.

For point 2, since `0` is interior and `x` is a boundary endpoint, every strict radial contraction `r x`, `|r|<1`, lies in the interior of a convex body containing `0` in its interior.

---

## Theorem 4 — transitive-boundary rigidity gives a Euclidean ball (**PDT proof using standard compact-group averaging lemma**)

Assume Theorem 3 and pure-state transitivity. Reversible transformations fix `mu`, so after centering they act linearly and preserve `K`. Since `partial K=P`, the group is transitive on the entire boundary.

Because `K` is compact, convex, centrally symmetric and contains `0` in its interior, its Minkowski functional

`||x||_K = inf {lambda>0 : x in lambda K}`

is a norm with unit ball `K`. Reversible transformations are linear isometries of this norm.

Choose any auxiliary positive-definite inner product `(.,.)_0` and Haar-average it:

`<x,y>_D = integral_G (g x, g y)_0 dg`.

This is positive definite and `G`-invariant. Boundary transitivity implies `<x,x>_D` has one constant value on all `x in partial K`. Therefore `partial K` is a Euclidean sphere for `<.,.>_D`, and `K` is its Euclidean ball (an ellipsoid in the original coordinates).

Thus

`Omega ≅ B^n` affinely.

---

## Corollary 4.1 — BQDC is derived (**PDT proof**)

Define

`Q_D(x)=<x,x>_D`.

Then

`Q_D(x+y)+Q_D(x-y)=2Q_D(x)+2Q_D(y)`.

Equivalently,

`||x+y||_D^2+||x-y||_D^2 = 2||x||_D^2+2||y||_D^2`.

Hence BQDC is downstream of elementary resolution, complete-erasure uniqueness and reversible symmetry; it need not be a primitive axiom.

---

## Independent cross-check A — information geometry (**imported theorem**)

Harremoës (arXiv:1707.03222) shows that for a rank-two convex body:

- existence of a Bregman divergence satisfying sufficiency implies spectrality;
- monotonicity of such a divergence forces the state space to be a ball/spin factor.

This provides an independent route to the same `B^n` geometry and motivates deriving CER from a resource-bounded distinction divergence.

---

## Independent cross-check B — strong symmetry and Jordan structure (**imported theorem**)

Barnum & Hilgert (arXiv:1904.03753; Journal of Lie Theory 30 (2020) 315-344) show that strongly symmetric spectral compact convex state spaces are precisely normalized state spaces of simple finite-dimensional Euclidean Jordan algebras and simplices.

For elementary rank two, the nonclassical simple Jordan branch is a spin factor, again giving a Euclidean ball.

---

## Theorem 5 — interaction selects the three-dimensional Bloch ball (**imported theorem applied to PDT output**)

Assume the elementary PDT theorem has produced `B^n`. Add:

1. local tomography of bipartite states;
2. continuous reversible dynamics;
3. existence of genuine nonlocal reversible interaction (equivalently, entanglement in the classified ball-composite setting).

Masanes, Müller, Pérez-García & Augusiak, *J. Math. Phys.* 55, 122203 (2014), DOI 10.1063/1.4903510, classify such Euclidean-ball composites. Except for the quantum two-qubit case, the allowed non-3-dimensional ball theories have no entangled states / interacting reversible dynamics.

Therefore

`B^n + local tomography + continuous reversible interaction => n=3`.

Hence the nonclassical elementary state space is

`Omega_elem ≅ B^3`,

the Bloch ball.

This dimension-selection theorem is established literature; PDT's new contribution can only be the upstream derivation of the ball and the physical-distinction interpretation of its premises.

---

## Corollary 5.1 — qubit representation

For `B^3`, define

`rho(x)=(I+x·sigma)/2`, `||x||<=1`.

This is the standard affine identification of the Bloch ball with qubit density matrices. Pure states are `||x||=1`.

---

## Full current quantum chain

`resource-bounded physical distinction`

`=> [OPEN BRIDGE: derive CER + CEU from capacity/sufficiency]`

`=> radial elementary resolution`

`=> centrally symmetric transitive boundary`

`=> Euclidean ball B^n`

`=> BQDC / inner-product distinction geometry`

`=> local tomography + continuous interaction`

`=> B^3 (imported Masanes et al. classification)`

`=> qubit`

`=> suitable Jordan/composite reconstruction assumptions`

`=> finite-dimensional complex QM`

`=> standard trace/Born probabilities, unitary dynamics, entanglement, Tsirelson bound`.

---

## What must NOT be claimed

- `K_epsilon=1 bit` alone does not yet imply CER.
- BQDC has not been derived from the original six broad PDT principles alone.
- The `n=3` classification is not new PDT mathematics.
- Complex quantum theory is not yet derived from `K_epsilon` alone.
- Born additivity / state-effect representation must be tracked explicitly.
- Exact Bekenstein-Hawking normalization and Einstein gravity remain conditional on established semiclassical inputs.
