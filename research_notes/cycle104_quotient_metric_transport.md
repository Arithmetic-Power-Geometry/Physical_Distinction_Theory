# Cycle 104 — Quotient-metric transport and path-independent refinement

## Question

Cycle 103 proved that resource refinement canonically supplies a quotient map from the finer resolved space to the coarser resolved space, but a reverse isometric section required metric structure. The open question was whether PDT really needs **one fixed metric shared by every resource window**, or whether a weaker transport law is enough.

## Exact result

Let \(Q:X\to Y\) be a surjective linear map and let the fine space \(X\) carry a positive-definite quadratic metric \(G\). Define

\[
H=(QG^{-1}Q^\top)^{-1},
\qquad
S=G^{-1}Q^\top H.
\]

Then

\[
QS=I,\qquad S^\top GS=H.
\]

For every \(y\in Y\), \(Sy\) is the unique minimizer of

\[
\min_{Qx=y} x^\top Gx,
\]

and the minimum is

\[
y^\top Hy.
\]

Thus a fine-level metric canonically induces the coarser quotient metric if coarse squared operational distance/cost is defined as the **minimum fine-resource quadratic cost among all representatives**.

### Path independence

For composable surjections \(X\xrightarrow{Q_1}Y\xrightarrow{Q_2}Z\), transporting \(G\) directly through \(Q_2Q_1\) gives the same metric on \(Z\) as transporting first through \(Q_1\) and then through \(Q_2\). This follows algebraically because

\[
H_1^{-1}=Q_1G^{-1}Q_1^\top
\]

and hence

\[
H_2^{-1}=Q_2H_1^{-1}Q_2^\top=Q_2Q_1G^{-1}Q_1^\top Q_2^\top.
\]

Therefore the resource metric has an exact composition law **conditional on** the minimum-cost quotient interpretation.

## Decisive falsification

The weaker statement that positive-definite metrics may be independently assigned at each resource level and quotient refinement will automatically make them compatible is false.

Smallest nontrivial quotient witness:

\[
Q=[1\;0]:\mathbb R^2\to\mathbb R,\qquad G=I_2.
\]

The induced metric is \(H=[1]\). Independently declaring the coarse metric to be \([4]\) leaves a perfectly valid positive-definite metric but makes the canonical minimum-norm section non-isometric. The isometry residual in this exact witness is \(3\).

Thus **positivity/isotropy at each level is not enough**; inter-level calibration is required.

## Stress tests

- Exact coordinate chains: dimensions \(1,\ldots,12,16,24,32,48,64,96,128\); 87 chain cases; all path-independent exactly.
- Random weighted audit: 600 seeded trials over dimensions \(1,\ldots,12,16,24,32,48,64\).
- Minimum-norm violations above \(10^{-8}\): 0.
- Path-independence violations above \(10^{-8}\): 0.
- Maximum right-inverse residual: \(1.61\times10^{-13}\).
- Maximum isometry residual: \(1.75\times10^{-11}\).
- Maximum path-independence residual: \(8.67\times10^{-12}\).
- Maximum metric-orthogonality residual: \(3.70\times10^{-12}\).
- Local regression tests: 6/6 passed.

The higher 96,128 dimensions are covered by the exact coordinate ledger; the random dense SPD audit is intentionally capped at 64 for numerical cost.

## Classification

| Claim | Status |
|---|---|
| Weighted minimum-norm quotient metric formula | PROVED / IMPORTED-KNOWN |
| Unique minimum-cost representative | PROVED / IMPORTED-KNOWN |
| Metric transport is path independent | PROVED |
| Independent per-level positive metrics are automatically compatible | FALSIFIED |
| Random/dimension stress audit | NUMERICALLY SUPPORTED |
| PDT physically identifies quotient distance with minimum fine-resource cost | OPEN / CONDITIONAL |
| Same-input PDT-vs-QM quantitative departure follows | OPEN; not obtained |
| BREAKTHROUGH CANDIDATE | NO |

## Prior-art boundary

The mathematical machinery is standard weighted minimum-norm / Moore–Penrose and Hilbert quotient geometry. Penrose's generalized inverse and standard quotient-norm constructions already establish the underlying mathematics; no novelty is claimed for these linear-algebra facts. The PDT-specific value is the logical boundary: Cycle 103's *fixed shared metric at all resource levels* can be replaced by the weaker minimum-cost quotient transport rule, but that rule must still be physically derived from PDT rather than postulated.

Relevant prior-art anchors:

- R. Penrose, “A generalized inverse for matrices,” *Proceedings of the Cambridge Philosophical Society* 51 (1955), 406–413.
- Standard quotient norm: \(\|[x]\|=\inf_{n\in N}\|x+n\|\); in a finite-dimensional Hilbert space the infimum is attained uniquely by the orthogonal representative.
- Weighted pseudoinverse/minimum-norm formulations are established extensions of the Moore–Penrose construction.

## PDT consequence / next kill test

The sharp remaining obligation is now:

\[
\text{PDT resource semantics}
\stackrel{?}{\Longrightarrow}
d_R([x])^2
=
\min_{\pi_{R'\to R}x'= [x]} d_{R'}(x')^2.
\]

If this minimum-cost rule can be derived from the existing distinction/resource semantics, metric transport becomes PDT-native and associative along refinement chains. If not, it must remain an additional conditional axiom.

The next cycle should attack that implication directly and test whether the resulting metric-accounting law constrains three-history composition defects without smuggling in associativity.
