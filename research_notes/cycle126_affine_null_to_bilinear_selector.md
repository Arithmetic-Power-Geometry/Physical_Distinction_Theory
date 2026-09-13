# Cycle 126 — From affine null-distinction composition to the n=3 selector

## Targets attacked

PDT-II target (1), a PDT-native composition law, and target (2), a non-circular PDT-native derivation of `n=3`.

## Candidate bridge

Cycle 124 used the known conditional selector

`nonzero SO(n)-equivariant bilinear B: V x V -> V  =>  n=3` for `n>=2`.

The open issue was whether bilinearity itself had to be inserted as an algebraic axiom. This cycle weakens that requirement.

Assume only that the composition `C: V x V -> V` is **separately affine** in its two arguments and that the null distinction is absorbing:

`C(x,0)=0` and `C(0,y)=0` for all `x,y`.

Any finite-dimensional separately affine map has the decomposition

`C(x,y)=B(x,y)+Lx+My+c`,

where `B` is bilinear, `L,M` are linear, and `c` is constant. Setting `y=0` gives

`Lx+c=0` for every `x`,

hence `L=0` and `c=0`. Setting `x=0` then gives `My=0` for every `y`, so `M=0`. Therefore

`C(x,y)=B(x,y)`

is bilinear.

### Theorem

**Separate affinity + two-sided null absorption implies bilinearity.**

Consequently, if PDT independently derives:

1. a nonzero same-sector composition `C: V x V -> V`;
2. separate affinity under independent preparation mixing;
3. two-sided null absorption;
4. proper-rotation covariance under `SO(n)`;

then, for nontrivial `n>=2`, Cycle 124's imported invariant-theory result gives

`n=3`.

The chain is therefore

`mixture/separate affinity + null absorption -> bilinearity`,

followed by

`nonzero same-sector bilinearity + SO(n) covariance -> n=3`.

## Exact dimension guard

The executable audit uses the diagonal even-sign subgroup of `SO(n)`. Lowering the output index of a bilinear map gives a rank-3 invariant tensor `T_ijk`. Invariance under every two-coordinate sign flip requires the parity of the occurrence count of every coordinate in `(i,j,k)` to be identical.

For rank 3 this yields the exact survivor counts:

- `n=1`: 1;
- `n=2`: 0;
- `n=3`: 6 tensor coordinates survive the sign subgroup (the permutations of three distinct indices);
- `n>=4`: 0.

For `n=3`, the remaining continuous/proper-rotation constraints reduce the invariant space to the familiar one-dimensional Levi-Civita tensor, reproducing the cross-product intertwiner. The rank-3 invariant classification is established mathematics and is not claimed as PDT novelty.

## Stress tests

Exact parity filtering was checked for `n=1..12`; the analytic higher-dimensional guard was recorded for `n=16,24,32,48,64,96,128`.

A deterministic `SO(3)` covariance regression used 2,000 random proper rotations and random vector pairs. There were zero violations at tolerance `1e-10`; the maximum floating residual was `4.864753555590494e-15`.

The affine-null regression was checked in dimensions `1..12`; with affine offsets removed by the null-axis hypotheses, the implemented biaffine and bilinear forms agreed exactly in all regression cases.

## Counterexample / boundary checks

This result does **not** derive the full PDT premises.

- Separate affinity without null absorption does not force bilinearity: linear and constant affine terms survive.
- Null absorption without separate affinity does not force bilinearity: nonlinear maps can vanish on both axes.
- Bilinearity plus null absorption without same-sector closure does not stop auxiliary-sector generation.
- Replacing `SO(n)` by `O(n)` kills a nonzero bilinear vector product, as recorded in Cycle 124.
- The `n=1` edge case remains because `SO(1)` is trivial; the selector is for nontrivial `n>=2`.

Thus the remaining PDT-native obligations are physical, not algebraic: justify separate preparation affinity for the distinction carrier, justify why the null distinction is genuinely absorbing, derive same-sector closure independently, and justify proper-rotation rather than full-reflection covariance.

## Prior-art boundary

No novelty is claimed for the mathematical facts that affine maps decompose into linear plus constant parts, that separate linearity defines bilinearity, or that the three-dimensional cross product is the `SO(3)`-equivariant vector-valued bilinear product. These are standard affine/multilinear algebra and invariant-theory facts.

The PDT-specific contribution of this cycle is a **sharpened dependency graph**: bilinearity need not be a primitive assumption if PDT can physically justify independent mixture-affinity and a two-sided null-distinction law.

## Status

- affine-null implication to bilinearity: **PROVED**;
- `SO(n)` bilinear selector used downstream: **IMPORTED/KNOWN**;
- numerical/dimensional regression: **NUMERICALLY SUPPORTED**;
- use as PDT `n=3` derivation: **CONDITIONAL**;
- PDT-native derivation of same-sector closure, separate affinity, null absorption and proper-rotation covariance: **OPEN**;
- `BREAKTHROUGH CANDIDATE`: **NO**.

## Next obligation

Attack whether PDT's own refinement/revelation primitives can justify the two physically meaningful ingredients in this bridge—independent mixture-affinity and null absorption—without simply postulating vector-space composition. If either fails, record the smallest countermodel and abandon this route rather than forcing the `n=3` conclusion.
