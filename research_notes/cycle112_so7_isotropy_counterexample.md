# Cycle 112 — explicit SO(7) isotropy counterexample

## Target

PDT-II targets (1) and (2): test whether the seven-dimensional normed-cross-product branch can survive the full proper-rotation covariance premise used by the existing Cycle-089 conditional selector.

## Prior-art guard

Cycle 089 already records the imported representation-theoretic result that a nonzero alternating bilinear map `B: R^n x R^n -> R^n` equivariant under the full standard `SO(n)` action exists only at `n=3`. Cycle 090 records the failure of polar `O(3)` covariance under reflections, and Cycle 091 records the determinant-twisted axial repair in three dimensions. Therefore Cycle 112 does **not** claim any of those selector statements as new.

The seven-dimensional imaginary-octonion cross product is also known mathematics. Its full linear cross-product symmetry group is the compact exceptional group `G2`, a proper subgroup of `SO(7)`; see John C. Baez, *The Octonions*, Bulletin of the American Mathematical Society 39 (2002), 145–205, arXiv:math/0105155.

## Exact falsification witness

Use the standard imaginary-octonion convention

`e1 x e2 = e3`.

Let `R` swap `e1 <-> e2` and independently swap `e4 <-> e5`, fixing the other basis vectors. Since `R` is a product of two transpositions,

`det(R)=+1`,

and `R^T R = I`, so `R in SO(7)`.

But

`(R e1) x (R e2) = e2 x e1 = -e3`,

whereas

`R(e1 x e2) = R e3 = +e3`.

Therefore

`||(R e1)x(R e2) - R(e1 x e2)|| = 2`.

Hence the claim

> the standard seven-dimensional octonionic cross product is equivariant under the full `SO(7)` group

is **FALSIFIED** by an exact proper-rotation witness.

## PDT consequence

This closes one possible escape from the Cycle-089 selector: the existence of a perfectly good normed cross product in dimension seven is not enough to preserve full rotational isotropy of that product. The seven-dimensional structure preserves only the smaller `G2` symmetry.

However, this is **not** a non-circular PDT derivation of `n=3`. PDT still has to derive, from its own operational/reversible distinction primitives, all of the physically substantive premises needed by the conditional selector: nonzero primitive composition, bilinearity/alternation, vector-valued closure, and covariance under the full proper-rotation group. Importing those assumptions merely reproduces known mathematics.

## Classification

- Exact `SO(7)` witness: **PROVED / FALSIFIED**.
- `G2` stabilizer fact and full-SO(n) selector: **IMPORTED/KNOWN**.
- PDT derivation of full `SO(n)` covariance and vector-valued closure: **OPEN**.
- **BREAKTHROUGH CANDIDATE: NO**.

## Next prove-or-falsify obligation

Derive or falsify the full-`SO(n)` covariance premise from PDT operational/reversible distinction primitives without assuming a cross product, Hodge star, generator-state dimension equality, or the desired dimensional answer.
