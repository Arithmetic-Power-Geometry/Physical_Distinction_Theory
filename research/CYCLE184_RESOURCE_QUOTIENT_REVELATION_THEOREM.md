# Cycle 184 — Resource-quotient revelation theorem and conservation boundary

Status: **PROVED / CONDITIONAL / IMPORTED-KNOWN / OPEN**

## Targets attacked
PDT-II (4) resource-refinement/revelation/conservation, with consequences for (1) composition and (3) same-input prediction.

## Exact hypotheses
Let V be a finite-dimensional real operational state-vector space. For a declared resource window R, let E_R be the linear span of all admissible real-valued effects/tests available under R. Define the operationally invisible subspace

K_R := {v in V : e(v)=0 for every e in E_R} = intersection_{e in E_R} ker(e).

Define the resource-relative operational quotient

Q_R := V / K_R,

and its linear revelation rank

D(R) := dim Q_R = dim V - dim K_R.

No probability rule, Hilbert structure, Born rule, norm, inner product, tensor product, or gravity law is assumed.

## Theorem 184A — resource refinement induces a canonical revelation map
If R <= R' means E_R is a linear subspace of E_R', then

K_R' subseteq K_R.

Hence there is a canonical surjective linear map

q_{R'->R}: Q_R' -> Q_R,

q([v]_{K_R'})=[v]_{K_R}.

Proof. Any v annihilated by every effect in E_R' is annihilated by every effect in its subset E_R, so K_R' subseteq K_R. The quotient map is well-defined because equality modulo K_R' implies equality modulo K_R; every class in Q_R has a representative v and is the image of its class in Q_R'. QED.

Interpretation: increasing resources can split previously operationally identical directions but cannot erase a distinction already visible to the smaller effect family, provided refinement is literal inclusion of admissible effects.

## Corollary 184B — revelation-rank monotonicity
Under the same hypotheses,

D(R') >= D(R).

Equivalently,

D(R')-D(R)=dim K_R-dim K_R' >= 0.

This is exact finite-dimensional linear algebra, not claimed as novel mathematics.

## Theorem 184C — exact chain conservation identity
For any nested chain R0 <= R1 <= ... <= Rm,

D(Rm)-D(R0) = sum_{j=1}^m [D(Rj)-D(Rj-1)].

This is a telescoping identity. It is valid bookkeeping of newly revealed linear directions, not by itself a physical conservation law.

## Stronger structure: exact sequence
For R <= R', the kernel of q_{R'->R} is canonically K_R/K_R'. Therefore

0 -> K_R/K_R' -> Q_R' -> Q_R -> 0

is exact, and

dim Q_R' = dim Q_R + dim(K_R/K_R').

Thus the increment is precisely the dimension of directions invisible at R but visible by R'.

## Dimension stress test n=1..12 and arbitrary finite n
Take V=R^n and E_k=span{x_1^*,...,x_k^*} for k=0,...,n. Then K_k=span{e_{k+1},...,e_n}, Q_k has dimension k, and every one-step refinement raises D by exactly one. This verifies all edge dimensions n=1,...,12 and proves the pattern for every finite n.

Degenerate cases are included: E_R={0} gives D=0; a separating/full dual family gives K_R={0}, D=dim V; adding linearly dependent effects leaves D unchanged.

## Candidate stronger conservation law — falsification boundary
The identity above does NOT imply that a closed physical system conserves D under dynamics. Let V=R^2, initial admissible effect span E=span{x_1^*}, and later resource span E'=span{x_1^*,x_2^*}. Then D changes from 1 to 2 without any state dynamics at all. Conversely, shrinking the declared effect family lowers D. Therefore unconditional temporal conservation of D is false unless a physical law constrains how resource windows/effect families evolve.

Likewise, a noninvertible physical channel can reduce distinguishable directions after pullback of effects, whereas an invertible change of representation preserves rank. Hence `D is universally conserved by dynamics` must not be asserted.

## Composition boundary
For V_AB=V_A tensor V_B and product-generated effect span E_AB=span(E_A tensor E_B), the annihilator quotient requires care: product effects may fail to separate all globally allowed directions. Additivity of D is not automatic, and hidden global sectors from Cycle 183 survive in the kernel. If local quotients have dimensions d_A,d_B and the composite is explicitly restricted to the product-generated quotient with no extra hidden/global directions, then the product observable quotient has dimension d_A d_B. This is **CONDITIONAL**, not a PDT-native derivation of the full composite.

## Pure/mixed, dynamics, records, thermodynamic settings
The theorem is representation-level and does not depend on labeling states pure/mixed. For Markovian or non-Markovian models it applies at each declared operational window; memory/environment records enlarge E_R only when they are actually admissible effects. Thermodynamic restrictions can shrink E_R and therefore enlarge K_R, but no thermodynamic monotone follows without specifying the allowed operations/resources.

## Same-input QM/GPT comparison
This quotient construction alone does not produce P_PDT(O|I,R). It identifies which linear state directions are operationally resolvable under R, but supplies no probability selector on outcomes. Therefore it cannot honestly generate P_PDT != P_QM under identical microscopic inputs. Any such prediction still requires an independently derived PDT probability law.

## Prior-art boundary
Annihilators, quotient spaces, exact sequences, operational equivalence under restricted effect sets, and distinguishability/resource restrictions are standard linear algebra and GPT/resource-theory ideas. The result is therefore **IMPORTED/KNOWN in mathematical content**. Its value here is to give PDT-II a rigorous resource-relative quotient formalism and to prevent overclaiming conservation.

## Classification
- Resource quotient Q_R=V/K_R: **PROVED; CONDITIONAL on linear operational representation; IMPORTED/KNOWN**.
- Canonical surjection under effect refinement: **PROVED**.
- Revelation-rank monotonicity: **PROVED; IMPORTED/KNOWN**.
- Exact nested-chain increment identity: **PROVED; IMPORTED/KNOWN**.
- Universal temporal conservation of D: **FALSIFIED** without resource/dynamics hypotheses.
- Product quotient dimension d_A d_B: **PROVED only under explicit product-generated/no-hidden-sector hypotheses; CONDITIONAL**.
- PDT-native probability law and same-input deviation from QM: **OPEN**.
- Gravity/capacity law: **OPEN; not imported**.
- BREAKTHROUGH CANDIDATE: **NO**.
