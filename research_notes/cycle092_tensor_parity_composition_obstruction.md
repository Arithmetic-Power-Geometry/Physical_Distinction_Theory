# Cycle 092 — Tensor-parity obstruction to antisymmetric-only composition

## Target

PDT-II target (1): obtain or falsify a PDT-native composition law before using composition to support dimension selection or new predictions.

## Result

**PROVED + FALSIFIED + IMPORTED/KNOWN boundary + NUMERICALLY SUPPORTED + OPEN.**

A broad and tempting composition candidate is decisively false: a nonzero alternating local closure cannot be lifted to a bipartite alternating closure merely by tensoring the same alternating operation on the two factors.

This is **not** a BREAKTHROUGH CANDIDATE. The exchange-parity algebra is elementary, and two-product Lie/Jordan composition is established prior art.

## Exact hypotheses and theorem

Let each local bilinear map have a definite exchange parity

\[
A_i(y,x)=\epsilon_i A_i(x,y),\qquad \epsilon_i\in\{+1,-1\}.
\]

Define on pure tensors

\[
C(x_1\otimes\cdots\otimes x_N,\;y_1\otimes\cdots\otimes y_N)
 =\bigotimes_{i=1}^N A_i(x_i,y_i)
\]

and extend bilinearly. Then

\[
C(Y,X)=\left(\prod_i\epsilon_i\right)C(X,Y).
\]

Therefore a factorized term is alternating exactly when it contains an **odd** number of alternating local factors.

### Bipartite corollary

If both local maps are alternating,

\[
B_A(y,x)=-B_A(x,y),\qquad B_B(v,u)=-B_B(u,v),
\]

then

\[
(B_A\otimes B_B)(Y,X)
=(-1)(-1)(B_A\otimes B_B)(X,Y)
=(B_A\otimes B_B)(X,Y).
\]

So \(B_A\otimes B_B\) is **symmetric**, not alternating. Its antisymmetrization is identically zero. Any linear combination consisting solely of such alternating\(\otimes\)alternating factorized terms remains symmetric.

## Smallest decisive witness

Use any dimension \(n\ge2\) and the alternating map

\[
B(x,y)=(x_0y_1-x_1y_0)e_0.
\]

Set

\[
z=e_0\otimes e_0+e_1\otimes e_1.
\]

Then

\[
(B\otimes B)(z,z)=2e_0\otimes e_0\ne0.
\]

An alternating bilinear operation must satisfy \(C(z,z)=0\), so the candidate fails already at \(n=2\). The same embedded witness works in every higher dimension.

## What survives

A symmetric local companion repairs the exchange parity. Let

\[
S(x,y)=S(y,x).
\]

Then each of

\[
B_A\otimes S_B,\qquad S_A\otimes B_B
\]

is alternating, and so is

\[
C_{AB}=B_A\otimes S_B+S_A\otimes B_B.
\]

The audit uses \(S(x,y)=\langle x,y\rangle e_0\) and verifies a nonzero repaired composite with exactly zero swap-sum residual in floating arithmetic for all tested nondegenerate dimensions.

This does **not** derive the PDT composition law. It gives a necessary structural lesson:

> If PDT wants an elementary alternating closure to survive ordinary binary tensor composition through factorized bilinear rules, the alternating product alone is insufficient. PDT must derive an independently meaningful symmetric companion, or abandon the factorized-bilinear ansatz and derive a different composite structure.

## Dimension and multipartite stress tests

The executable audit covers

\[
n=1,2,\ldots,12,16,24,32,48,64,96,128.
\]

- \(n=1\) is degenerate because every alternating map vanishes.
- In every tested \(n\ge2\), the explicit \(B\otimes B\) diagonal witness has norm exactly `2.0`.
- In every tested \(n\ge2\), the repaired \(B\otimes S+S\otimes B\) witness is nonzero with norm `1.0` and swap-sum residual `0.0`.
- For the all-alternating factorized N-partite term \(B^{\otimes N}\), the exchange parity alternates with party number: odd \(N\) is alternating, even \(N\) is symmetric. The frozen audit records \(N=1,\ldots,12\).

The proof itself is exact and dimension-independent; the computational sweep is a regression/edge-case audit, not evidence from which the theorem is inferred.

## Alternative rules and boundaries

This cycle **does not** claim:

1. that no composite alternating operation can exist;
2. that every PDT composition must be tensor-factorized;
3. that the symmetric companion must be the quantum anticommutator/Jordan product;
4. that the repaired two-product structure uniquely implies quantum mechanics;
5. that this result supplies the missing same-input PDT-vs-QM prediction.

The theorem only kills the antisymmetric-only factorized route. A nonfactorized rule, additional primitive structure, a quotient-dependent rule, or another independently derived product remains logically open and must be tested on its own hypotheses.

## Prior-art check

Historical novelty is rejected for the core algebraic observation.

- Grgin and Petersen, *Algebraic implications of composability of physical systems*, Communications in Mathematical Physics 50 (1976), 177–188, DOI `10.1007/BF01617995`, already study composability through a two-product algebra and consistency of composition classes.
- Moldoveanu, *Derivation of Quantum Mechanics algebraic structure from invariance of the laws of Nature under system composition and Leibniz identity*, arXiv:1505.05577 (2015), explicitly gives a composite antisymmetric product of the form
  \[
  \Delta(\alpha)=\alpha\otimes\sigma+\sigma\otimes\alpha,
  \]
  pairing the skew product with a symmetric product.
- Standard operator algebra gives the same parity structure directly:
  \[
  [A\otimes B,C\otimes D]
   =\tfrac12\big([A,C]\otimes\{B,D\}+\{A,C\}\otimes[B,D]\big).
  \]
  Thus quantum composition already exhibits the symmetric/antisymmetric pairing; PDT cannot claim that pairing itself as novel.

## Status ledger

- **PROVED:** exchange parity of a factorized multilinear tensor term is the product of local exchange parities.
- **FALSIFIED:** `B_AB = B_A tensor B_B` as a nonzero bipartite alternating composition law when both local `B` are alternating.
- **NUMERICALLY SUPPORTED:** executable regression witnesses for `n=1..12,16,24,32,48,64,96,128` and N-party parity through `N=12`.
- **IMPORTED/KNOWN:** Lie/Jordan two-product composability and the corresponding quantum commutator/anticommutator structure.
- **OPEN:** a genuinely PDT-native derivation of the required symmetric companion, or a defensible nonfactorized alternative composition law.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Next prove-or-falsify obligation

The strongest surviving target-(1) route is now sharper: test whether a symmetric companion can be derived from existing PDT distinction/resource primitives **without importing the quantum Jordan product**. If not, produce a no-go showing which additional primitive is unavoidable. Only after that should the axial/alternating `n=3` selector be coupled to composite dynamics.
