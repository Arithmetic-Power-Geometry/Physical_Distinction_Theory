# Cycle 116 — Operational quotient does not force same-sector closure

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED + OPEN**  
**BREAKTHROUGH CANDIDATE: NO**

## Question attacked

Can the exact operational/resource quotient developed in Cycle 070 be strengthened into the missing PDT-II same-sector closure law `V x V -> V` solely by requiring exact visible composition, recursive composability, and associativity?

## Countermodel

Take `V = R^n` with coordinatewise visible multiplication `a*b`. Add an auxiliary copy `M = R^n` and define on `A = V + M`

`(a,m)*(b,n) = (a*b, a*n + m*b + lambda*a*b)`

with every product coordinatewise and fixed nonzero `lambda`.

Projection `pi(a,m)=a` gives exactly

`pi(x*y)=pi(x)*pi(y)`.

For primitive visible inputs `(a,0)` and `(b,0)`, however,

`(a,0)*(b,0)=(a*b, lambda*a*b)`,

so the composite generally leaves the visible sector even though every projected prediction obeys the original composition law.

## Exact proof of associativity

The construction is coordinatewise, so it is enough to check one scalar coordinate. Write

`(a,m)*(b,n)=(ab, an+mb+lambda ab)`.

Expanding either bracketing gives the same visible term `abc` and the same auxiliary term

`ab p + a n c + m b c + 2 lambda abc`.

Therefore the augmented product is associative for every `n` and every `lambda`.

## No-go statement

Any proposed principle stated entirely in terms of the quotient-visible law `pi(x*y)` cannot distinguish the visible model from this associative extension. Therefore quotient-visible compositional consistency, even together with recursive associativity, does **not** imply ontic same-sector closure.

The smallest decisive counterexample is already `n=1`: with `lambda=1`,

`(2,0)*(3,0)=(6,6)`.

The visible result is exactly `6`, while a nonzero auxiliary component is generated.

## Stress audit

`cycle116_extension_audit.py` was independently executed with seed `1160913`.

Dimensions: `1..12, 16, 24, 32, 48, 64, 96, 128`.

- randomized integer trials: **2960**
- associativity failures: **0**
- visible-projection failures: **0**
- trials producing nonzero auxiliary output: **2839**

The randomized audit is regression evidence only; the theorem is algebraic.

## Relation to earlier PDT cycles

Cycle 070 proved that a declared resource window naturally induces an exact quotient/restricted-functional state and exact refinement maps. Cycle 116 establishes a different boundary: even if the quotient-visible composition is exact, that fact alone cannot determine whether composition closes in the microscopic carrier or in a larger extension.

Thus the quotient formalism is operationally complete for the declared window but is not an ontological sector-selection theorem.

## Prior-art boundary

The algebraic mechanism is not historically new. Square-zero and algebra extensions are standard; extension theory explicitly studies surjections `E -> R` whose kernel is an ideal, including square-zero ideals. The present construction is a simple associative extension/cocycle-style example. Accordingly, no novelty is claimed for the extension mathematics itself.

## PDT-II consequence

The surviving target is stronger and experimentally oriented. To derive `V x V -> V`, PDT must supply at least one independently physical principle that constrains the auxiliary/kernel sector itself—for example a measurable resource cost, a revelation rule that eventually exposes every dynamically generated sector, or a conservation law violated by nontrivial extensions. A condition depending only on already-visible quotient predictions cannot do the job.

This also blocks a circular `n=3` route: same-sector closure cannot be inferred merely from operational quotient consistency and then fed into a known dimensional selector.
