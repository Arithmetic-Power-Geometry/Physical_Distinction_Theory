# Cycle 093 — Isotropic same-space symmetric-companion no-go

## Target

PDT-II target (1): test the strongest surviving Cycle-092 route — whether the symmetric companion required by a factorized alternating composition law can be derived inside the same elementary distinction space without importing the quantum Jordan product.

## Result

**PROVED + FALSIFIED + IMPORTED/KNOWN boundary + NUMERICALLY SUPPORTED + OPEN.**

Under the full connected rotational isotropy used by the current PDT dimension-selection route, a nonzero symmetric bilinear companion with the same vector codomain does not exist.

This is **not** a BREAKTHROUGH CANDIDATE. The representation-theoretic content is standard; the PDT value is the precise obstruction it places on the Cycle-092 composition route.

## Exact theorem

Let `V = R^n`, `n >= 2`, carry the standard action of `SO(n)`. Suppose

\[
S:V\times V\to V
\]

is bilinear, symmetric,

\[
S(x,y)=S(y,x),
\]

and `SO(n)`-equivariant,

\[
S(Rx,Ry)=R S(x,y) \qquad \forall R\in SO(n).
\]

Then

\[
\boxed{S\equiv 0.}
\]

Equivalently,

\[
\boxed{\operatorname{Hom}_{SO(n)}(\operatorname{Sym}^2 V,V)=0,\qquad n\ge2.}
\]

### Proof for `n=2`

`-I` belongs to `SO(2)`. Bilinearity gives

\[
S(-x,-y)=S(x,y),
\]

while equivariance gives

\[
S(-x,-y)=-S(x,y).
\]

Hence `S(x,y)=0` for all `x,y`.

### Proof for `n>=3`

Fix a unit vector `x`. The stabilizer of `x` contains the standard `SO(n-1)` action on `x^perp`. Equivariance implies that `S(x,x)` is fixed by this stabilizer, hence

\[
S(x,x)=a_x x.
\]

Choose a determinant-`+1` pi rotation `R` in a plane containing `x`; then `Rx=-x`. Bilinearity gives

\[
S(Rx,Rx)=S(-x,-x)=S(x,x),
\]

whereas equivariance gives

\[
S(Rx,Rx)=R S(x,x)=-S(x,x).
\]

Therefore `S(x,x)=0` for every unit `x`, and by homogeneity for every `x`. Polarization then yields

\[
S(x,y)=\tfrac12\big(S(x+y,x+y)-S(x,x)-S(y,y)\big)=0.
\]

So the theorem holds for every `n>=2`.

### Degenerate exception

For `n=1`, `SO(1)` is trivial, so `S(x,y)=cxy` is allowed. This does not supply the nontrivial alternating local closure required by the current PDT route.

## Decisive countercandidate

A tempting construction from the metric and a fixed direction is

\[
S_u(x,y)=\langle x,y\rangle u.
\]

It is symmetric and bilinear but the fixed `u` breaks isotropy. Take `u=x=e_1` and the determinant-`+1` pi rotation flipping `e_1,e_2`. Then

\[
S_u(Rx,Rx)=u,
\qquad
R S_u(x,x)=-u,
\]

so the covariance residual has norm exactly

\[
\boxed{2}.
\]

The same embedded witness works in every `n>=2`.

## Surviving scalar/enlarged-codomain route

The no-go is specifically for a **same-space vector-valued** symmetric companion. The Euclidean inner product

\[
g(x,y)=\langle x,y\rangle
\]

is a nonzero symmetric `SO(n)`-invariant map

\[
\operatorname{Sym}^2 V\to\mathbb R.
\]

Thus isotropy does not forbid a symmetric companion; it forces the natural companion out of `V` and into a scalar/unit sector (or some larger representation/algebra).

For `n=3`, the familiar pair

\[
\langle x,y\rangle,\qquad x\times y
\]

is the scalar-symmetric/vector-antisymmetric decomposition underlying quaternion/geometric-algebra multiplication. That observation is established mathematics and is **not** claimed as PDT novelty.

The composition lesson is therefore sharper than Cycle 092:

> If PDT keeps full rotational isotropy and an alternating elementary vector closure, the parity-correct composite cannot be repaired by adding a nonzero symmetric product `V x V -> V`. A scalar/unit sector, a larger codomain/algebra, broken isotropy, or a genuinely nonfactorized rule is unavoidable.

## Dimension stress audit

The executable audit freezes the exact theorem status for

\[
n=1,2,\ldots,12,16,24,32,48,64,96,128.
\]

- `n=1`: degenerate `SO(1)` exception.
- Every tested `n>=2`: exact theorem status `ZERO_ONLY` for same-space symmetric `SO(n)`-equivariant companions.
- Every tested `n>=2`: the fixed-axis symmetric countercandidate has decisive residual exactly `2.0`.
- Random `SO(n)` tests verify the scalar inner product companion to floating tolerance; the largest recorded residual is generated in `results/cycle093_isotropic_symmetric_companion_no_go.json`.

The dimension sweep is a regression audit; the no-go theorem is analytic and does not depend on numerical evidence.

## Alternative symmetry/output boundaries

This theorem does **not** say that:

1. no symmetric product can exist after isotropy is reduced to a proper subgroup;
2. no scalar- or tensor-valued symmetric companion exists;
3. no enlarged unital algebra can contain both symmetric and antisymmetric sectors;
4. the quaternion/Jordan structure is uniquely forced by PDT;
5. the result supplies a same-input PDT-vs-QM probability deviation.

A future candidate must state which of these boundaries it crosses and pay the associated physical-resource/composition cost explicitly.

## Prior-art check

Historical novelty is rejected for the mathematical core.

- Standard `SO(3)` Clebsch-Gordan decomposition gives `3 tensor 3 = 1 + 3 + 5`; the symmetric square is `1 + 5`, so it contains no vector (`3`) summand. This is the representation-theory version of the elementary proof above.
- Grgin and Petersen (1976) and later composability reconstructions use distinct symmetric and skew products on an observable algebra rather than demanding that both close on a bare elementary vector representation.
- Standard quaternion/geometric-algebra multiplication combines a scalar symmetric dot-product sector with a vector antisymmetric cross-product sector in three dimensions.

Accordingly, this cycle is a **PDT-specific no-go application of known mathematics**, not a new representation theorem.

## Status ledger

- **PROVED:** for every `n>=2`, `Hom_SO(n)(Sym^2 V,V)=0` for the standard real vector representation.
- **FALSIFIED:** the Cycle-092 repair can use a nonzero same-space `SO(n)`-isotropic symmetric companion `S:V x V -> V`.
- **NUMERICALLY SUPPORTED:** frozen dimension/edge audit through `n=128`, including explicit residual-2 countercandidate and random scalar-invariance checks.
- **IMPORTED/KNOWN:** representation decomposition, dot/cross/quaternion structure, and two-product composability literature.
- **OPEN:** derive a PDT-native scalar/unit augmentation or alternative composition mechanism, then test associativity/grouping, resources, quotients, and same-input predictions without importing the desired quantum algebra.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Next prove-or-falsify obligation

The strongest target-(1) question is now whether a **minimal scalar/unit augmentation** is forced by PDT primitives and whether its bilinear composition law is unique under independently justified axioms. The next cycle should test the smallest ansatz on `A = R direct-sum V`, actively searching for associativity, norm, isotropy and dimension counterexamples before coupling it to the `n=3` selector.
