# Cycle 042 — Tsirelson-compatible correlator-composite nonuniqueness

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN boundary. Not a BREAKTHROUGH CANDIDATE.**

## Target attacked

PDT-II targets (1) composition and (5) experimentally distinctive inequalities.

The candidate shortcut under test was:

> Euclidean local distinction geometry + local tomography + full local rotational symmetry + the exact CHSH Tsirelson value uniquely determine the bipartite correlation structure.

This shortcut is false already in real local dimension `n=3`.

## Construction

Work in the centered binary-correlation sector. A bipartite correlator is represented by a real `n x n` matrix `T`, with local unit-vector settings `x,y` giving

`E(x,y) = x^T T y`.

Positivity of the centered binary probabilities

`p(a,b|x,y) = (1 + ab x^T T y)/4`

for all unit `x,y` is ensured by `||T||_op <= 1`.

Define two convex, centrally symmetric, `O(n) x O(n)`-invariant bodies:

- `C_op = {T : ||T||_op <= 1}`;
- `C_cap = {T : ||T||_op <= 1 and ||T||_* <= 2}`,

where `||.||_*` is the nuclear norm.

Every product correlator `T = a b^T` with `||a||,||b|| <= 1` lies in both because

`||a b^T||_op = ||a b^T||_* = ||a|| ||b|| <= 1`.

Both sets are invariant under independent local orthogonal transformations because operator and nuclear norms are unitarily/orthogonally invariant.

## Exact separation

For `n>=3`, take `T=I_n`.

`||I_n||_op = 1`, so `I_n in C_op`, while

`||I_n||_* = n > 2`, so `I_n notin C_cap`.

Thus the two correlation bodies are physically distinct at the correlator level. The smallest decisive dimension is `n=3`.

For `n=2`, the nuclear cap does not separate the identity witness because `||I_2||_*=2`; this is why the first decisive dimension is three.

## Same CHSH optimum

Let the canonical CHSH coefficient matrix be built from

`x0=e1`, `x1=e2`,

`y0=(e1+e2)/sqrt(2)`, `y1=(e1-e2)/sqrt(2)`.

The CHSH coefficient has two nonzero singular values, both `sqrt(2)`. For every `T` with `||T||_op<=1`, norm duality gives

`|<C,T>| <= ||C||_* ||T||_op = 2 sqrt(2)`.

Now choose the aligned rank-two partial isometry

`W = C/sqrt(2)`.

Its singular values are `(1,1,0,...)`, hence

`||W||_op=1`, `||W||_*=2`,

so `W` belongs to both `C_op` and `C_cap`, and

`<C,W> = 2 sqrt(2)`.

Therefore both distinct bodies have the identical exact CHSH optimum

`S_max = 2 sqrt(2)`.

## Consequence

The implication

`Euclidean local geometry + local tomography + local O(n) symmetry + exact CHSH Tsirelson bound`

`=> unique centered bipartite correlation composite`

is **FALSIFIED**.

Consequently PDT-II cannot use recovery of the CHSH Tsirelson value as evidence that its composite law has been uniquely derived. At minimum, additional higher-rank/multi-setting/composition structure must be fixed. A useful next discriminator is an inequality or operational task whose coefficient matrix has rank at least three, because `C_cap` and `C_op` first differ in that sector.

## Stress tests

The branch audit covers `n=2..12`, with 200 randomized product correlators per dimension and randomized independent orthogonal left/right transformations. Product-state containment has zero failures. Rotation invariance errors remain at floating-point roundoff. The exact separating witness exists for every `n>=3`.

The code intentionally records the scope boundary: this is a centered binary-correlator-sector construction, not a claim that `C_cap` has already been promoted to a unique full unrestricted GPT composite.

## Prior-art boundary

The ingredients are established mathematics/physics: Tsirelson's CHSH bound, norm duality, orthogonally invariant matrix norms, and the general non-uniqueness of GPT composites. Therefore no historical novelty is claimed for those ingredients. The PDT-specific value of the result is as a sharp kill test against a tempting but insufficient reconstruction route.
