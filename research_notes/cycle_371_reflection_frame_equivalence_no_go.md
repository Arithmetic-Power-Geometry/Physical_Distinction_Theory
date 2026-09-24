# Cycle 371 — Reflection/frame-equivalence stress test of the conditional n=3 selector

## Status

- **PROVED:** the ordinary 3D vector cross product is SO(3)-equivariant but is not O(3)-equivariant as a polar-vector-valued product.
- **FALSIFIED:** strengthening Cycle 370's H4 from proper rotations SO(n) to all orthogonal frame changes O(n) destroys the n=3 survivor rather than deriving it.
- **CONDITIONAL:** the Cycle 370 n=3 selector therefore requires an orientation structure (or an operational restriction to orientation-preserving reversible frames).
- **IMPORTED/KNOWN:** cross products are axial vectors/pseudovectors under improper orthogonal transformations; the Hodge star depends on orientation.
- **OPEN:** PDT has not derived a physically preferred orientation or proved that only SO(n), rather than O(n), is the reversible frame group.
- **NOT A BREAKTHROUGH CANDIDATE.**

## Candidate under attack

Cycle 370 used H1–H3 (alternating, orthogonal, normed internal product) plus

H4: (Rx)×(Ry)=R(x×y) for every R in SO(n).

That package selects n=3 mathematically. The present cycle asks whether H4 follows from the apparently more PDT-native statement that **all distinction frames preserving the distinction norm are operationally equivalent**. Without an independently supplied orientation, that natural frame group is O(n), not SO(n).

## Exact n=3 counterexample to full frame equivalence

Let e1,e2,e3 be the standard orthonormal basis and use the ordinary cross product, so e1×e2=e3. Take the reflection

Q = diag(-1,1,1),  det(Q)=-1.

Then

(Qe1)×(Qe2)=(-e1)×e2=-e3,

whereas

Q(e1×e2)=Qe3=e3.

Hence

(Qe1)×(Qe2) != Q(e1×e2).

So the unique Cycle-370 survivor fails as soon as H4 is extended from SO(3) to O(3).

More generally, in three dimensions

(Qx)×(Qy)=det(Q) Q(x×y).

Thus the product is an axial/pseudovector-valued operation. It is equivariant under SO(3), but under O(3) it transforms in the determinant-twisted representation, not the polar-vector representation assumed by H4.

## Dimension audit

For n=1 there is no nontrivial independent input pair. For n=2 H1–H3 already fail. For n=3 H1–H3 survive but polar O(3)-equivariance fails by the explicit reflection above. For n=4,5,6 and n>=8 H1–H3 fail by the normed vector-product classification. For n=7 H1–H3 survive, but even full SO(7) equivariance already fails (Cycle 370), so O(7) cannot rescue it. Therefore no nontrivial n in 1..12 survives H1–H3 plus polar O(n)-equivariance; the same analytic arguments exclude all higher finite n.

## What survives

A correct orientation-aware statement is possible: in n=3 the cross product maps two polar vectors to an **axial** vector. Equivalently one may regard the Hodge-star construction as using a chosen orientation. This repairs covariance mathematically, but it changes the ontology/codomain and imports orientation data. It does not provide a PDT-native derivation of orientation.

## Consequences for PDT-II

1. **PDT-native composition law:** OPEN. The internal cross product is not a composite-system tensor law.
2. **Non-circular n=3 derivation:** remains CONDITIONAL. SO(n) covariance selects 3 only after orientation-preserving frames are privileged.
3. **Same-input P_PDT != P_QM:** OPEN; this route still supplies no probability law.
4. **Resource refinement/revelation/conservation:** OPEN.
5. **Distinctive inequality:** OPEN.
6. **Gravity/capacity:** not invoked.

## Prior-art boundary

The parity behavior is standard mathematics/physics: the cross product is a pseudovector and acquires the determinant twist under improper orthogonal transformations; the Hodge star is orientation-dependent. PDT cannot claim this as novel.

## Decisive conclusion

A generic "reversible indistinguishability of norm-preserving frames" principle does **not** derive Cycle 370's SO(n) hypothesis. If it means all norm-preserving frames, it naturally yields O(n), and the n=3 cross product fails the required polar-vector covariance. To retain the selector, PDT must independently derive orientation or an operational reason that reflection-related frames are not equivalent. Until then the n=3 route is conditional, not foundational.

## Next strongest attack

Test whether an orientation can emerge from PDT's resource/refinement structure without being assumed: search for an operationally definable pseudoscalar/handedness witness invariant under allowed dynamics. If no such witness exists, prove an orientation-blind no-go theorem; if it does, compare it against known chirality/parity resources before making any novelty claim.
