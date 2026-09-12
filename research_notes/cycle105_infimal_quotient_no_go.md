# Cycle 105 — Infimal quotient functoriality: path independence does not select Euclidean geometry

## Question attacked

Cycle 104 established path-independent transport for positive-definite quadratic costs. The strongest next question was whether this refinement-composition law could carry physical content strong enough to select a Hilbert/Euclidean metric and thereby help the PDT composition or non-circular `n=3` programs.

The answer is **no**.

## Exact theorem

Let

\[
X\xrightarrow{q_1}Y\xrightarrow{q_2}Z
\]

be maps, and let \(C:X\to[0,+\infty]\) be any extended-real cost. Define the infimal pushforward along \(q\) by

\[
(q_*C)(y)=\inf_{q(x)=y} C(x),
\]

with the empty-fiber infimum interpreted as \(+\infty\).

Then

\[
\boxed{q_{2*}(q_{1*}C)=(q_2\circ q_1)_*C.}
\]

For each \(z\), both sides are exactly

\[
\inf\{C(x):q_2(q_1(x))=z\}.
\]

The iterated form merely partitions the same feasible set by the intermediate value \(y=q_1(x)\). No inner product, linearity, convexity, differentiability, positive definiteness, or even vector-space structure is required.

## Decisive falsification

Therefore the candidate implication

\[
\boxed{\text{minimum-cost refinement path independence}\Longrightarrow\text{quadratic/Hilbert geometry}}
\]

is **FALSIFIED**.

A smallest useful linear witness is \(\mathbb R^2\) with the \(\ell_1\) norm. For \(e_1=(1,0)\) and \(e_2=(0,1)\),

\[
\|e_1+e_2\|_1^2+\|e_1-e_2\|_1^2=8,
\]

while

\[
2\|e_1\|_1^2+2\|e_2\|_1^2=4.
\]

Hence the parallelogram identity fails by exactly \(4\), so this norm is not induced by an inner product. Nevertheless its quotient costs remain exactly path independent under infimal pushforward.

The same obstruction applies to selecting dimension:

\[
\boxed{\text{refinement associativity/path independence}\not\Longrightarrow n=3.}
\]

The law survives in arbitrary dimensions and even for arbitrary sets equipped with arbitrary costs.

## Stress tests

The proof is exact; computation is used only as a regression and adversarial audit.

- Exact coordinate quotient chains: dimensions `1..12,16,24,32,48,64,96,128`.
- Norms tested: \(p=1,1.5,2,3,\infty\).
- Exact chain cases: **755**.
- Nonquadratic exact cases: **604**.
- Path-independence violations: **0**.
- Random coordinate-chain trials: **4000**, including **3195** nonquadratic cases; violations above `1e-12`: **0**.
- Random finite-fiber trials with arbitrary integer costs/maps: **5000**; exact violations: **0**.
- Unreachable/empty target fibers explicitly encountered: **9248**; the `+infinity` convention remained consistent.
- Local Cycle-105 tests: **6/6 passed**.

The two-dimensional parallelogram witness also distinguishes the tested norms: \(p=2\) satisfies the witness to floating precision, while \(p=1,1.5,3,\infty\) fail it.

## Prior-art boundary

This is not claimed as new functional analysis. The quotient norm of a normed space is classically defined by an infimum over representatives,

\[
\|x+M\|=\inf_{m\in M}\|x+m\|,
\]

and the fact that inner-product norms are characterized by the parallelogram identity is the classical Jordan-von Neumann theorem. The associativity of nested infima used here is elementary. The PDT contribution of this cycle is a **no-go boundary**: Cycle 104's quadratic metric transport is only one special realization of a much broader resource coarse-graining rule and cannot be used, by itself, to infer Euclidean geometry.

Prior-art anchors checked in this cycle:

- Standard quotient-norm construction in Banach/normed-space theory.
- P. Jordan and J. von Neumann, *On Inner Products in Linear, Metric Spaces*, Annals of Mathematics 36 (1935), 719–723 (parallelogram characterization).
- Standard \(\ell_p\) norm examples: \(p\ne2\) need not be inner-product norms.

## Classification

| Claim | Status |
|---|---|
| Infimal pushforward is path independent under composition | **PROVED / IMPORTED-KNOWN** |
| Path independence forces a quadratic/Hilbert metric | **FALSIFIED** |
| Path independence alone selects `n=3` | **FALSIFIED** |
| Dimension/norm/finite-fiber stress audit | **NUMERICALLY SUPPORTED** |
| PDT derives the minimum-cost quotient rule from physical distinction primitives | **OPEN** |
| PDT has an independent principle selecting the parallelogram identity / `p=2` | **OPEN** |
| Same-input PDT-vs-QM probability departure | **OPEN** |
| BREAKTHROUGH CANDIDATE | **NO** |

## Consequence for PDT-II

Cycle 104 remains correct, but its composition law is now demoted as a route to geometry selection:

\[
\text{quadratic quotient transport}
\subset
\text{general infimal cost transport}.
\]

Thus **resource-refinement associativity cannot carry the burden of deriving either Euclidean geometry or `n=3`**.

The next viable prove-or-falsify target must add an independently motivated physical identity that distinguishes Hilbertian from general normed/resource geometry. A sharp candidate is a PDT-native operational parallelogram/polarization or interference identity. It must be derived from distinctions, records, and composition rather than assumed, and then tested against \(\ell_1,\ell_p\), octonionic, GPT, and same-input quantum constructions.
