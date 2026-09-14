# Cycle 136 — Universal coarse-graining no-go for scalar probability reweighting

## Target

Attack PDT-II target (3): obtain, or decisively constrain, a same-input quantitative deviation from ordinary quantum probabilities without changing the microscopic input or declared resource window.

Cycle 064 exhibited contextuality for specific nonlinear normalized transforms. This cycle asks for the exact functional boundary.

## Hypotheses

Let raw mutually exclusive outcome weights be nonnegative and additive under ordinary coarse-graining. Let

\[
f:[0,\infty)\to[0,\infty),\qquad f(0)=0,\qquad f(x)>0\text{ for }x>0,
\]

and define, inside any finite outcome context,

\[
P_f(i\mid q)=\frac{f(q_i)}{\sum_j f(q_j)}.
\]

When exclusive outcomes of raw weights \(a,b\) are merged, suppose their raw merged weight is \(a+b\). Require the probability of the merged event to be independent of whether it is computed before or after this coarse-graining, in any context containing at least one outside outcome of weight \(c>0\).

## Exact theorem

Coarse-graining consistency gives

\[
\frac{f(a)+f(b)}{f(a)+f(b)+f(c)}
=
\frac{f(a+b)}{f(a+b)+f(c)}.
\]

Cross multiplication cancels the common product and leaves

\[
f(c)\,[f(a)+f(b)-f(a+b)]=0.
\]

Because \(f(c)>0\),

\[
\boxed{f(a+b)=f(a)+f(b)}.
\]

Thus \(f\) is additive on the nonnegative reals. Nonnegativity makes an additive function monotone: if \(0\le x\le y\), then \(f(y)=f(x)+f(y-x)\ge f(x)\). The standard monotone-Cauchy result then forces

\[
f(x)=Cx.
\]

With calibration \(f(1)=1\), \(f(x)=x\).

### Classification

- **PROVED (conditional theorem):** within the explicitly stated scalar-normalization/additive-raw-merge class.
- **FALSIFIED:** any genuinely nonlinear scalar transform as a route to a same-input probability deviation while preserving ordinary coarse-graining semantics.
- **IMPORTED/KNOWN:** finite event additivity and the monotone additive-function linearity ingredient are classical; no novelty is claimed for them.
- **NUMERICALLY SUPPORTED:** seeded regression audit below.
- **OPEN:** structurally nonseparable, context-dependent, resource-dependent, or altered-event-composition probability laws remain possible and require separate derivation/testing.
- **BREAKTHROUGH CANDIDATE:** NO.

## Smallest decisive witness

Three outcome channels are the smallest nontrivial setting because a merge requires an outside reference event. For

\[
f(q)=q^2,\qquad (a,b,c)=(1,2,3),
\]

fine-grained addition gives

\[
P_{\mathrm{fine}}(a\lor b)=\frac{1^2+2^2}{1^2+2^2+3^2}=\frac5{14},
\]

whereas coarse-graining first gives

\[
P_{\mathrm{coarse}}(a\lor b)=\frac{(1+2)^2}{(1+2)^2+3^2}=\frac12.
\]

Hence the exact discrepancy is

\[
\boxed{\frac12-\frac5{14}=\frac17}.
\]

A zero-weight member of the merged pair is a degenerate case and may accidentally satisfy the equality for nonlinear rules; it does not evade the all-\(a,b\) theorem.

## Regression stress audit

Outcome cardinalities tested:

`3..12, 16, 24, 32, 48, 64, 96, 128`.

For each cardinality the audit generated strictly positive seeded random weights and tested power transforms \(f(q)=q^\alpha\) with \(\alpha\in\{1/2,1,2,3\}\). There were 1,280 cases per exponent.

- \(\alpha=1\): 0/1,280 violations; maximum floating residual `1.1102230246251565e-16`.
- \(\alpha=1/2\): 1,280/1,280 violations.
- \(\alpha=2\): 1,280/1,280 violations.
- \(\alpha=3\): 1,280/1,280 violations.
- Total nonlinear: 3,840/3,840 violations.
- Smallest observed nonlinear gap: `0.0002546724775186471`.
- Largest observed nonlinear gap: `0.3332205290256422`.

The theorem is algebraic and dimension-free; this sweep varies outcome cardinality rather than pretending it is a physical state-space dimension sweep.

## Prior-art boundary

The mathematical ingredients belong to standard probability/functional-equation foundations: probabilities of disjoint alternatives are finitely additive under ordinary event semantics, and nonnegative/monotone solutions of Cauchy's additive equation are linear. Accordingly, this cycle does **not** claim those ingredients as new mathematics. The PDT-specific value is a clean no-go boundary for one proposed deviation mechanism.

## Consequence for PDT-II

A defensible same-input PDT-vs-QM deviation cannot be obtained merely by replacing Born/raw weights by a nonlinear scalar function and renormalizing, if PDT simultaneously retains additive raw coarse-graining and ordinary event consistency.

The next viable search space is narrower:

1. derive a genuinely nonseparable probability law from PDT primitives;
2. derive a resource-dependent operational rule that changes more than a scalar weight map;
3. derive a different event-composition law and expose its experimentally testable consequence;
4. or prove that PDT collapses to the standard rule under its surviving axioms.

Any claimed deviation must state exactly which one of the hypotheses above it abandons and why that abandonment is PDT-native rather than inserted to force disagreement.
