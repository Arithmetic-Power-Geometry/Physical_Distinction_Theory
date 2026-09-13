# Cycle 120 — Circularity guard for sector-resource monotonicity

## Result

Let the microscopic carrier be `A = V ⊕ M`. Let `H : A -> [0,∞)` be faithful to the auxiliary sector in the sense

`H^{-1}(0) = V`.

For any composition law `C : A × A -> A`, the following statements are equivalent when restricted to visible inputs:

1. **Same-sector closure:** `C(V,V) ⊂ V`.
2. **Zero-resource compositional monotonicity:** for every `x,y in V`,
   `H(C(x,y)) <= H(x)+H(y)`.

### Proof

If (2) holds and `x,y in V`, faithfulness gives `H(x)=H(y)=0`. Nonnegativity then yields `0 <= H(C(x,y)) <= 0`, hence `H(C(x,y))=0`; faithfulness implies `C(x,y) in V`.

Conversely, if (1) holds, then for `x,y in V`, all three of `x,y,C(x,y)` lie in `V`, so all three have zero H. Thus the monotonicity inequality holds with equality.

Therefore the Cycle-119 condition, **if imposed only on zero-resource/visible inputs**, is not an independent derivation of closure. Under `H^{-1}(0)=V`, it is a reformulation of closure itself.

## Smallest decisive witness

Take `V=M=R`, `H(a,m)=m^2`, and the associative extension used in the preceding audit,

`(a,m)*(b,r) = (ab, ar + mb + ab)`.

Then

`(1,0)*(1,0) = (1,1)`.

The inputs have `H=0`, while the output has `H=1`. Thus both same-sector closure and zero-input monotonicity fail together already at `n=1`.

The closure-preserving comparison law

`(a,m)∘(b,r) = (ab, ar + mb)`

satisfies both properties on visible inputs.

## Stress audit

Exact integer arithmetic was used over dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`.

There were 5,216 visible-pair/property checks, with zero mismatches between the truth value of closure and the truth value of zero-resource monotonicity. The leaking rule generated 1,094 nonzero hidden outputs; the preserving rule generated none. These computations are regression evidence; the equivalence theorem is algebraic.

## Observation-separation boundary

Suppose hidden-sector observations are linear maps `O_R : M -> Y_R`. If

`K = intersection_R ker(O_R)`

contains a nonzero vector, no resource determined solely by the complete observation record can be faithful to hidden-state identity: `m in K` and `0` have the same observation record.

In finite dimension, if the observations separate hidden states (`K={0}`), a finite separating subfamily exists. For such a finite family one may construct

`H(m)=sum_j ||O_j m||^2`,

which is nonnegative and faithful. This is elementary finite-dimensional linear algebra/informational-completeness logic, not a PDT novelty claim.

Crucially, Cycle 117 already showed that finite revealability does not imply dynamical closure. Observation separation can therefore ground **faithfulness**, but it does not supply the missing independent **dynamical non-generation law**.

## Prior-art boundary

General resource theories conventionally define free operations so that the free-state set is invariant or so that resource is not generated from free states. Chitambar and Gour, *Reviews of Modern Physics* 91, 025001 (2019), review this framework. Liu, Hu and Lloyd, *Physical Review Letters* 118, 060502 (2017), likewise relate free states, free operations and monotones via resource-destroying maps. Informational completeness/tomographic separation is also established measurement theory. None of those mechanisms is claimed as new here.

## Consequence for PDT-II

Cycle 119's sufficient theorem remains mathematically correct, but its zero-input monotonicity premise must be downgraded as an **independent PDT-native explanation** of same-sector composition. To escape circularity, PDT must derive a structural law with content beyond `V`-invariance—for example a global inequality applying to arbitrary hidden-resource inputs that has separately motivated operational meaning, and from which the zero-resource case follows as a theorem rather than being stipulated.

A useful next target is therefore:

`PDT primitives -> independently motivated global resource law -> sector non-generation -> same-sector composition`.

The first arrow remains OPEN.

## Classification

- **PROVED:** equivalence of visible-sector closure and zero-resource monotonicity under `H^{-1}(0)=V`.
- **FALSIFIED:** zero-resource monotonicity, by itself, as a non-circular independent route to closure.
- **IMPORTED/KNOWN:** generic free-operation/resource-nongeneration and informational-completeness mechanisms.
- **NUMERICALLY SUPPORTED:** dimension and adversarial regression audit.
- **OPEN:** a PDT-native global dynamical/resource law with independent physical content.
- **BREAKTHROUGH CANDIDATE:** NO.
