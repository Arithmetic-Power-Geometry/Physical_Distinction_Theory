# Cycle 094 — Minimal scalar/unit augmentation: associativity obstruction and unique 3D repair

## Target

PDT-II target (1), following Cycle 093: test the smallest isotropic scalar/unit enlargement
\[
A=\mathbb R\oplus V
\]
before treating it as a viable PDT-native composition law.

## Result

**PROVED + FALSIFIED + IMPORTED/KNOWN boundary + NUMERICALLY SUPPORTED + OPEN.**

This cycle gives two exact statements.

### Theorem A — metric-only scalar augmentation is not associative

Let \(V=\mathbb R^n\), and define the unital bilinear product
\[
(a,x)\star(b,y)=
\big(ab+\alpha\langle x,y\rangle,\; ay+bx\big).
\]

For every \(n\ge2\), if \(\alpha\ne0\), this product is not associative.

Take orthonormal \(e_1,e_2\) and the pure-vector elements
\[
X=(0,e_1),\qquad Y=(0,e_1),\qquad Z=(0,e_2).
\]
Then
\[
(X\star Y)\star Z=(0,\alpha e_2),\qquad
X\star(Y\star Z)=0,
\]
so the associator is
\[
\boxed{[X,Y,Z]_\star=(0,\alpha e_2)\ne0.}
\]

Thus the scalar/unit route left open by Cycle 093 does **not** by itself give an associative composition law unless the metric coupling is killed (\(\alpha=0\)) or \(n=1\).

The \(n=1\) case is a genuine algebraic exception, but it has no nonzero alternating elementary closure and therefore does not solve the current PDT target.

### Theorem B — in 3D the alternating term repairs associativity only at one coefficient relation

In \(V=\mathbb R^3\), consider the most direct isotropic oriented ansatz
\[
(a,x)\star(b,y)=
\left(
ab+\alpha\,x\!\cdot\! y,\;
ay+bx+\beta\,x\times y
\right).
\]

For three pure vectors, direct expansion gives
\[
[(0,x),(0,y),(0,z)]_\star
=
\left(
0,\;
(\alpha+\beta^2)
\big[(x\!\cdot\!y)z-(y\!\cdot\!z)x\big]
\right).
\]

Hence associativity requires
\[
\boxed{\alpha=-\beta^2.}
\]

Conversely, when \(\alpha=-\beta^2\), after the rescaling \(u=\beta x\) (for \(\beta\ne0\)) this is the standard quaternion scalar-vector product, so it is associative. The \(\beta=0,\alpha=0\) case is the degenerate square-zero vector ideal.

Therefore, inside this minimal ansatz,
\[
\boxed{
\text{nonzero metric coupling + associativity + nonzero alternating 3D term}
\Longrightarrow
\alpha=-\beta^2.
}
\]

## Combined PDT consequence with Cycles 089/093

Cycle 093 proved that a nonzero isotropic symmetric companion cannot close as \(\operatorname{Sym}^2V\to V\), leaving the scalar metric as the minimal symmetric sector.

Cycle 089 established, under the current full \(SO(n)\) standard-vector symmetry assumption, that a nonzero equivariant alternating vector closure \(\Lambda^2V\to V\) exists only for \(n=3\).

Combining those exact results with this cycle gives a **conditional selector**:

> Within the minimal unital ansatz on \(\mathbb R\oplus V\), if PDT independently requires a nonzero isotropic metric coupling, associative grouping, and a nonzero alternating vector closure under full \(SO(n)\), then the nondegenerate solution is \(n=3\), with the coefficients locked to the quaternion relation \(\alpha=-\beta^2\).

This is mathematically useful for PDT, but it is **not** a non-circular PDT derivation yet: the premises must still be derived from PDT primitives rather than selected because they recover quaternionic structure.

## Dimension and adversarial audit

The executable audit covers
\[
n=1,\ldots,12,16,24,32,48,64,96,128.
\]

For every tested \(n\ge2\), the exact witness above has associator norm \(|\alpha|\) at \(\alpha=1\), hence exactly `1.0`.

For the 3D repair, 1,000 random triples were tested for representative coefficient pairs. On-relation cases \((-1,1),(-4,2),(-1/4,1/2)\) had maximum floating associator residuals between \(4.01\times10^{-15}\) and \(2.41\times10^{-14}\). Off-relation cases had large nonzero residuals, as expected. These numerical checks are regression evidence only; the coefficient relation is analytic.

Local unit tests: **5/5 passed**.

## Prior-art boundary

This is not a breakthrough candidate.

- The 3D scalar-vector law with \(-x\cdot y\) and \(x\times y\) is standard quaternion multiplication, and quaternion multiplication is associative.
- Frobenius' classical theorem states that the finite-dimensional associative real division algebras are \(\mathbb R\), \(\mathbb C\), and \(\mathbb H\); generalized statements place the octonions in the alternative but nonassociative case.
- The metric-only commutative unitized product is in the orbit of standard spin-factor/Jordan-algebra constructions, where nonassociativity is not a surprise.

Accordingly, the novelty claim is **rejected** for the mathematical core. The PDT contribution of this cycle is the exact prove-or-falsify narrowing of the proposed composition route.

## Status ledger

- **PROVED:** metric-only scalar augmentation with \(\alpha\ne0\) is nonassociative for every \(n\ge2\).
- **PROVED:** in the 3D dot/cross ansatz, associativity is equivalent to \(\alpha=-\beta^2\).
- **FALSIFIED:** the Cycle-093 scalar/unit enlargement, by itself, supplies a nontrivial associative PDT composition law.
- **NUMERICALLY SUPPORTED:** dimension audit through \(n=128\) and 3D random coefficient stress tests.
- **IMPORTED/KNOWN:** quaternion multiplication, real associative division-algebra classification, and the Jordan/spin-factor boundary.
- **CONDITIONAL:** combining the present theorem with the earlier full-\(SO(n)\) alternating-closure selector yields \(n=3\) only under independently justified PDT premises.
- **OPEN:** derive (or falsify) associativity/grouping and the nonzero scalar + alternating sectors from PDT distinction/resource primitives; then test restricted resources, composites, dynamics, and same-input predictions.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Next prove-or-falsify obligation

Do not promote the quaternion relation as PDT-native. The next strongest question is whether PDT's operational composition assumptions actually force **associative grouping** and a nonzero scalar metric coupling, or whether resource-restricted composition is instead nonassociative/alternative. Any attempt must be tested against the \(n=7\) octonionic/G2 boundary and against experimentally meaningful same-input consequences.
