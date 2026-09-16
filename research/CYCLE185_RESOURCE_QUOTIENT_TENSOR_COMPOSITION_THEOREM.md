# Cycle 185 — Resource-quotient tensor composition theorem

Status: **PROVED / CONDITIONAL / IMPORTED-KNOWN / OPEN**

## Targets attacked
PDT-II (1) composition law and (4) resource-relative revelation, with explicit consequences for (2), (3), and (5).

## Exact hypotheses
Let V_A,V_B be finite-dimensional real operational vector spaces. Let E_A subseteq V_A^* and E_B subseteq V_B^* be the linear spans of effects available in declared resource windows R_A,R_B. Define

K_A = intersection_{e in E_A} ker(e),   Q_A=V_A/K_A,
K_B = intersection_{f in E_B} ker(f),   Q_B=V_B/K_B.

Assume only for this theorem that the ambient bilinear composite vector space is the algebraic tensor product V_AB=V_A tensor V_B and that the declared composite effect span is exactly the product-generated span E_AB=span{e tensor f : e in E_A, f in E_B}. No Born rule, inner product, Hilbert space, cone, norm, probability selector, local tomography of a larger physical composite, or gravity law is assumed.

## Theorem 185A — exact kernel of product-generated observations
Let K_AB be the common kernel of E_AB. Then

K_AB = K_A tensor V_B + V_A tensor K_B.

Consequently there is a canonical vector-space isomorphism

Q_AB := (V_A tensor V_B)/K_AB  ~=  Q_A tensor Q_B.

### Proof
Define evaluation maps T_A:V_A -> E_A^* and T_B:V_B -> E_B^* by T_A(v)(e)=e(v) and T_B(w)(f)=f(w). By construction ker(T_A)=K_A and ker(T_B)=K_B. The product effects evaluate a tensor z through T_A tensor T_B. Hence K_AB=ker(T_A tensor T_B).

Choose complements V_A=K_A direct-sum A_0 and V_B=K_B direct-sum B_0. The restrictions of T_A and T_B to A_0 and B_0 are injective. Decompose
V_A tensor V_B = (K_A tensor K_B) direct-sum (K_A tensor B_0) direct-sum (A_0 tensor K_B) direct-sum (A_0 tensor B_0).
The tensor evaluation vanishes on the first three summands and is injective on A_0 tensor B_0 because tensor products of injective linear maps between finite-dimensional vector spaces are injective. Thus its kernel is exactly K_A tensor V_B + V_A tensor K_B. The standard quotient-tensor isomorphism then gives Q_AB ~= Q_A tensor Q_B. QED.

## Corollary 185B — multiplicative revelation rank
With D_X=dim Q_X,

D_AB = D_A D_B.

If D_A,D_B>0 and C_X=log D_X, then

C_AB = C_A + C_B.

The logarithmic statement is only a reparameterization of dimension and is not asserted as thermodynamic entropy or a physical conservation law.

## Corollary 185C — associativity at the observable quotient level
For three systems satisfying the same product-generated hypotheses,

Q_ABC ~= Q_A tensor Q_B tensor Q_C,
D_ABC=D_A D_B D_C.

The result extends inductively to any finite number of factors and is compatible with the standard associator/symmetry maps of vector spaces.

## Resource-refinement compatibility
If E_A subseteq E_A' and E_B subseteq E_B', Cycle 184 gives canonical surjections Q_A' -> Q_A and Q_B' -> Q_B. Their tensor product gives a canonical surjection

Q_A' tensor Q_B' -> Q_A tensor Q_B.

Under Theorem 185A this is exactly the product-window coarse-graining map Q_AB' -> Q_AB. Thus resource revelation and product composition commute at the quotient level under the stated hypotheses.

## Exact stress tests n=1..12
For V_A=R^n, V_B=R^m and coordinate-effect spans of ranks a<=n,b<=m, K_A has dimension n-a and K_B dimension m-b. The kernel formula gives

dim K_AB = (n-a)m + n(m-b) - (n-a)(m-b) = nm-ab,

so D_AB=ab. This covers every n,m in 1..12 exactly and proves the formula for arbitrary finite n,m. Degenerate cases a=0 or b=0 give D_AB=0; full-effect cases a=n,b=m give D_AB=nm. Linearly dependent added effects do not change the quotient.

## Adversarial/counterexample boundary
The theorem does NOT prove that nature's full composite is V_A tensor V_B, nor that every globally admissible effect is product-generated, nor local tomography of an enlarged composite. Cycle 183's hidden-sector construction C_hidden=(V_A tensor V_B) direct-sum H remains a decisive counterexample to that stronger claim: every product effect can annihilate H. Theorem 185 says something narrower and exact: once one quotients by what the declared product resource window cannot observe, the observable tensor sector composes canonically.

Likewise, allowing entangled/global effects can shrink K_AB and reveal additional directions, so D_AB may exceed D_A D_B relative to the product-only resource window. This is revelation by a stronger resource set, not a contradiction.

## Different norms, groups, states and dynamics
The kernel/isomorphism theorem is algebraic and therefore independent of norm choice. Reversible local linear groups descend to quotient actions when they preserve K_A,K_B, and their product action descends naturally to Q_A tensor Q_B. Pure/mixed labels are irrelevant at this linear level. Markovian/non-Markovian dynamics, controlled-environment records, or thermodynamic restrictions matter only through which effects belong to the declared E_R; enlarging the admissible record/effect family is handled by Cycle 184 refinement maps.

## Same-input QM/GPT comparison
The theorem supplies no outcome probability selector. It therefore cannot by itself yield P_PDT(O|I,R) != P_QM(O|I,R). It also cannot supply the non-circular n=3 probability derivation. Any such claim remains OPEN until PDT derives additional physical structure beyond the observable quotient.

## Experimentally distinctive inequalities
The exact equality D_AB=D_A D_B is a test of the explicitly product-generated observable quotient, not yet a novel empirical inequality against QM. If a physical PDT postulate later asserts that a specified laboratory resource window is exhaustive and product-generated, an observed excess revelation rank would falsify that postulate. No such exhaustiveness postulate is established here.

## Prior-art boundary
The mathematical core is standard finite-dimensional tensor/quotient linear algebra: tensor products preserve the relevant quotient construction over a field, and dim(U tensor W)=dim U dim W. GPT literature also treats composite systems via tensor structures and emphasizes that the full composite is not uniquely fixed by local systems. Therefore the algebraic theorem is **IMPORTED/KNOWN**, not a novelty claim. The PDT value is organizational: it gives an exact composition law for Cycle 184's resource-relative observable quotient while preserving Cycle 183's no-go boundary for full physical composites.

## Classification
- Kernel identity K_AB=K_A tensor V_B + V_A tensor K_B: **PROVED; IMPORTED/KNOWN**.
- Canonical quotient composition Q_AB ~= Q_A tensor Q_B: **PROVED; CONDITIONAL on ambient tensor and product-generated effect hypotheses; IMPORTED/KNOWN**.
- Revelation-rank law D_AB=D_A D_B: **PROVED under the same hypotheses**.
- Log-rank additivity: **PROVED algebraically; not a physical entropy/conservation law**.
- Compatibility with nested resource refinement: **PROVED under product-window hypotheses**.
- Unique full physical composite/local tomography: **FALSIFIED as a consequence of local data alone (Cycle 183)**.
- PDT-native n=3 probability rule: **OPEN**.
- Same-input PDT-vs-QM probability deviation: **OPEN**.
- Experimentally distinctive inequality: **OPEN** absent an independently justified exhaustiveness postulate.
- Gravity/capacity law: **OPEN; not imported**.
- BREAKTHROUGH CANDIDATE: **NO**.
