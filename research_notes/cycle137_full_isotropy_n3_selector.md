# Cycle 137 — Full-isotropy selector theorem: a non-circular conditional route to n=3

## Target

Attack PDT-II target (2): a non-circular, PDT-native derivation of \(n=3\).

The aim is not to assume a three-dimensional cross product and rediscover three dimensions. Instead ask what dimensions permit a **nonzero local distinction interaction**

\[
B:V\times V\to V
\]

under three dimension-independent structural hypotheses:

1. **bilinearity**;
2. **alternation**, \(B(x,x)=0\), equivalently \(B(x,y)=-B(y,x)\);
3. **full proper-rotation covariance**,
   \[
   B(Rx,Ry)=R\,B(x,y)\qquad\forall R\in SO(n).
   \]

No norm identity, associativity, Jacobi identity, quantum postulate, tensor-product rule, Born rule, or gravity law is used.

## Exact conditional theorem

Let \(V=\mathbb R^n\), \(n\ge 1\). If \(B:V\times V\to V\) is alternating, bilinear and \(SO(n)\)-equivariant, then:

- for \(n\ne3\), \(B=0\);
- for \(n=3\), nonzero examples exist (the ordinary cross product, up to overall scale/orientation convention).

Hence existence of a **nonzero** interaction with the three properties selects

\[
\boxed{n=3}.
\]

### Elementary stabilizer proof

For \(n=1\), alternation immediately gives \(B=0\).

Now take \(n\ge2\), an orthonormal pair \(e_1,e_2\), and put

\[
v=B(e_1,e_2).
\]

Let \(R_\theta\) be any proper rotation in the \(e_1e_2\)-plane, acting identically on its orthogonal complement. By bilinearity and alternation,

\[
B(R_\theta e_1,R_\theta e_2)
=\det(R_\theta|_{\mathrm{span}(e_1,e_2)})\,B(e_1,e_2)
=v.
\]

By equivariance, the same left side equals \(R_\theta v\). Therefore

\[
R_\theta v=v\quad\text{for every }\theta.
\]

A vector fixed by every plane rotation has no component in \(\mathrm{span}(e_1,e_2)\), so

\[
v\in \mathrm{span}(e_1,e_2)^\perp.
\]

Next let \(S\) be any proper rotation that fixes \(e_1,e_2\) pointwise and rotates their orthogonal complement. Equivariance yields

\[
Sv=S B(e_1,e_2)=B(Se_1,Se_2)=B(e_1,e_2)=v.
\]

Thus \(v\) must be fixed by all of \(SO(n-2)\) acting on the \((n-2)\)-dimensional complement.

- \(n=2\): the complement is zero-dimensional, so \(v=0\).
- \(n=3\): the complement is one-dimensional and \(SO(1)\) is trivial, so a nonzero \(v\) can survive.
- \(n\ge4\): \(SO(n-2)\) has no nonzero vector fixed by every rotation, hence \(v=0\).

Because every orthonormal pair can be moved to \((e_1,e_2)\) by a proper rotation, \(B\) vanishes on all orthonormal pairs when \(n\ne3\). Bilinearity and alternation then give \(B=0\) everywhere.

At \(n=3\), the ordinary vector cross product satisfies the hypotheses and is nonzero, proving existence.

## Why the seven-dimensional cross product does not evade the theorem

Classical vector-product theory permits normed binary cross products in dimensions 3 and 7 (nontrivially), but the seven-dimensional octonionic cross product is not invariant under the **full** group \(SO(7)\); its automorphism group is the proper subgroup \(G_2\).

The audit contains an exact coordinate witness. Use the standard Fano-plane multiplication and the determinant-\(+1\) quarter-turn

\[
R:e_1\mapsto e_2,\qquad e_2\mapsto-e_1
\]

in the \((e_1,e_2)\)-plane. For the input pair \((e_1,e_4)\),

\[
B(Re_1,Re_4)=e_6,
\qquad
R\,B(e_1,e_4)=e_5.
\]

Therefore

\[
B(Re_1,Re_4)\ne R\,B(e_1,e_4),
\]

so full \(SO(7)\) covariance fails decisively.

## Stress audit

The theorem is exact and dimension-general. The generated ledger explicitly covers

\[
n=1,\ldots,12,16,24,32,48,64,96,128.
\]

Only \(n=3\) is marked as surviving the nonzero full-isotropy selector theorem.

For the actual \(n=3\) cross product, 500 seeded random axis-angle proper rotations and random vector pairs were checked:

- failures at tolerance \(10^{-10}\): **0**;
- maximum absolute floating residual: `7.105427357601002e-15`.

For \(n=7\), the exact signed-coordinate quarter-turn witness above has squared equivariance gap \(2\).

Five regression tests pass locally.

## Prior-art boundary

This mathematical fact is **not claimed as novel**.

Classical work on vector cross products includes Brown & Gray (1967), and Darpö (2009) gives an elementary account of vector-product algebras in dimensions \(0,1,3,7\). The crucial stronger condition here is **full isotropy**: the familiar 3D cross product is \(SO(3)\)-equivariant, whereas a fixed 7D cross product is preserved only by \(G_2\), not all of \(SO(7)\).

References checked:

- Brown, R. B. & Gray, A. (1967), *Vector cross products*, Commentarii Mathematici Helvetici 42, 222–236, DOI 10.1007/BF02564418.
- Darpö, E. (2009), *Vector product algebras*, Bulletin of the London Mathematical Society 41(5), 898–902, DOI 10.1112/blms/bdp066; arXiv:0810.5464.
- Standard 7D cross-product literature records the automorphism group as \(G_2\) rather than \(SO(7)\).

Accordingly the theorem is an imported/known mathematical boundary. Its possible PDT value is architectural, not a novelty claim.

## PDT-II interpretation

This is the cleanest non-circular **conditional** \(n=3\) selector found so far:

\[
\boxed{
\text{nonzero}
+\text{bilinear}
+\text{alternating}
+\text{full local proper-rotation covariance}
\Longrightarrow n=3.
}
\]

It is stronger than the earlier route through normed cross products, because no norm identity is needed, and it avoids the \(n=7\) branch by making isotropy explicit rather than adding Jacobi or associativity afterward.

However, this is **not yet a PDT-native derivation**. PDT-II must still derive, rather than merely choose, the three structural hypotheses—especially why the relevant distinction interaction should transform covariantly under the full \(SO(n)\) rather than under a proper subgroup such as \(G_2\).

That derivation is the remaining obligation. If PDT primitives independently imply those hypotheses, the dimension step itself is complete and non-circular.

## Classification

- **PROVED:** the stabilizer theorem under the stated hypotheses.
- **CONDITIONAL:** its use as a PDT dimension derivation.
- **IMPORTED/KNOWN:** the underlying isotropic cross-product boundary and 7D \(G_2\) prior art.
- **NUMERICALLY SUPPORTED:** the 3D covariance audit and explicit 7D counterexample.
- **FALSIFIED:** the idea that the 7D normed cross product also obeys full \(SO(7)\) isotropy.
- **OPEN:** deriving bilinearity, alternation and full proper-rotation covariance from PDT-native primitives.
- **BREAKTHROUGH CANDIDATE:** **NO**.
