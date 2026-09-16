# Cycle 197 — Minimality does not derive PDT composition

## Target
PDT-II target (1): determine whether the local resource-relative quotient data can be upgraded to a unique PDT-native composition law by imposing a minimality/no-hidden-sector principle.

## Setup
Let local accessible quotient spaces be finite-dimensional real vector spaces Q_A and Q_B, with D_A = dim Q_A and D_B = dim Q_B. Assume declared product effects span Q_A^* \otimes Q_B^*. Let a candidate composite quotient Q_AB admit these product effects as linear functionals.

Define the product-observation map

T: Q_AB -> (Q_A^* \otimes Q_B^*)^*,
T(x)(f \otimes g) = (f \otimes g)(x).

The locally invisible sector is H = ker T.

## Proposition 197.1 — dimension lower bound
If every bilinear product statistic on Q_A x Q_B is representable independently, then

    dim Q_AB >= D_A D_B.

Proof: the image of T must have dimension D_A D_B, hence rank-nullity gives dim Q_AB = D_A D_B + dim ker T >= D_A D_B. QED.

Classification: PROVED; IMPORTED/KNOWN linear algebra.

## Proposition 197.2 — minimality implies local tomography, but does not derive it
Under the same hypotheses, if one additionally postulates the minimality condition

    dim Q_AB = D_A D_B,

then ker T = {0}; therefore product statistics separate composite quotient states and Q_AB is linearly isomorphic to Q_A \otimes Q_B.

Proof: Proposition 197.1 plus rank-nullity. QED.

Classification: PROVED conditional; IMPORTED/KNOWN.

Crucial logical point: minimality is an extra physical postulate. It is not implied by the current PDT quotient construction. Thus using 'no inaccessible global distinctions' or 'choose the smallest compatible composite' to obtain D_AB = D_A D_B simply restates local tomography/minimality in PDT language and is circular as a PDT-native derivation.

## Counterfamily to uniqueness without minimality
For every h >= 0,

    Q_AB^(h) = (Q_A \otimes Q_B) direct-sum H_h,
    dim H_h = h,

with all declared product effects annihilating H_h, reproduces exactly the same local/product data while

    dim Q_AB^(h) = D_A D_B + h.

Hence local quotient data do not select h=0.

Smallest case: D_A=D_B=1. Both R and R direct-sum R are compatible with the same one-dimensional product statistics when the second coordinate is invisible.

Classification: uniqueness from local data FALSIFIED.

## Dimension stress test
The proof is symbolic and dimension-independent. It therefore covers D_A,D_B in 1..12 exactly and all finite higher dimensions. Degenerate case D_A=0 or D_B=0: the product-statistic rank is zero and no nonzero lower bound follows; hidden sectors remain unconstrained. Redundant effects do not change D_A or D_B. Invertible local coordinate changes preserve all dimensions and kernels.

## Norms and reversible groups
No norm enters the argument. Any local reversible group acting invertibly on Q_A and Q_B preserves D_A D_B. Such covariance does not remove H_h unless an additional axiom constrains the global representation. Therefore norm choice and local reversible covariance do not derive h=0.

## Prior-art boundary
Tomographic locality in GPT/operational reconstructions is precisely the condition that a composite state is determined by local/product measurement statistics. Complex quantum theory has this property, while real-vector-space quantum theory is a standard counterexample with additional global degrees of freedom. Hardy's reconstructions explicitly use tomographic locality as a postulate; Hardy-Wootters show real quantum theory is bilocally rather than locally tomographic. Thus Proposition 197.2 is not a PDT breakthrough.

Relevant literature checked in this cycle:
- Lucien Hardy, Reformulating and Reconstructing Quantum Theory, arXiv:1104.2066.
- Lucien Hardy and William K. Wootters, Limited Holism and Real-Vector-Space Quantum Theory, arXiv:1005.4870.
- Howard Barnum and Alexander Wilce, Local tomography and the Jordan structure of quantum theory, arXiv:1202.4513.
- Lucien Hardy, On the theory of composition in physics, arXiv:1303.1537.

## Status ledger
- Universal dimension lower bound under independent product-statistic representability: PROVED / IMPORTED-KNOWN.
- Minimality => tensor-product dimension/local tomography: PROVED / CONDITIONAL / IMPORTED-KNOWN.
- Minimality derived from current PDT axioms: OPEN; no derivation found.
- Unique composite from local quotient data alone: FALSIFIED (Cycle 196, strengthened here).
- PDT-native composition law: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Consequence for next cycle
Do not promote 'minimal composite', 'no hidden distinctions', or D_AB=D_A D_B as PDT-native unless a new PDT principle independently forces ker T=0. The strongest next attack is whether PDT's distinction/resource primitives impose a nontrivial compositional consistency condition across three systems (associativity plus resource refinement) that constrains hidden sectors without assuming local tomography; compare against bilocal/n-local tomography and monoidal/GPT prior art before novelty claims.
