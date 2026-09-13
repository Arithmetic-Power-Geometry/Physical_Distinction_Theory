# Cycle 118 — Exact multiplicative resource conservation does not force same-sector closure

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED + OPEN**  
**BREAKTHROUGH CANDIDATE: NO**

## Question attacked

Cycle 117 showed that finite revealability of generated auxiliary components is insufficient to force the PDT-II closure premise `V x V -> V`. Cycle 118 tests a stronger escape route: can an exact positive resource-conservation law prohibit auxiliary-sector generation?

## Exact construction

For one coordinate let a microscopic state be `(a,m)` with visible coordinate `a` and auxiliary coordinate `m`. Define the linear identification

`phi(a,m) = a + i(m+a)`.

Transport ordinary complex multiplication through `phi`:

`x*y = phi^{-1}(phi(x) phi(y))`.

Writing `x=(a,m)` and `y=(b,r)`, this gives

`A = ab - (m+a)(r+b)`

`I = a(r+b) + b(m+a)`

and

`x*y = (A, I-A)`.

Because the law is transported from ordinary complex multiplication, it is associative.

Define the nonnegative resource

`q(a,m) = |phi(a,m)|^2 = a^2 + (m+a)^2`.

The complex modulus is multiplicative, hence exactly

`q(x*y) = q(x) q(y)`.

Equivalently, on nonzero states the logarithmic charge `L=log q` is additive under composition. On the unit-resource shell `q=1`, composition preserves `q=1` exactly.

## Decisive counterexample

Take two visible-sector states (`m=r=0`):

`(a,0)*(b,0) = (0,2ab)`.

Thus the visible sector is generically not closed even though the positive resource law is exact.

The smallest explicit integer witness is already `n=1`:

`(2,0)*(3,0)=(0,12)`.

Its resource accounting is

`q(2,0)=8`, `q(3,0)=18`, and `q(0,12)=144=8*18`.

Therefore

`associativity + exact positive multiplicative resource accounting`

**does not imply**

`same-sector closure V x V -> V`.

Restricting to normalized inputs does not rescue the implication: for `a=b=1/sqrt(2)`, both visible inputs satisfy `q=1`, while their product is `(0,1)` with `q=1`, entirely in the auxiliary direction.

## Higher dimensions

Apply the construction coordinatewise on `A=(R^2)^n`. Each coordinate resource obeys

`q_i(x*y)=q_i(x)q_i(y)`

exactly, so a vector of independently conserved/multiplicative resource charges exists in every tested dimension. The construction does not privilege `n=3`.

## Stress audit

`cycle118_multiplicative_resource_no_go.py` was executed with seed `1180913` over dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`.

Frozen results:

- scalar exact associativity cases: **21,609**
- scalar associativity failures: **0**
- scalar resource-law failures: **0**
- randomized vector trials: **1,480**
- vector associativity failures: **0**
- vector resource-law failures: **0**
- randomized visible-input trials generating a nonzero auxiliary component: **1,442**

The audit is regression evidence. The no-go itself is analytic because the product is an algebra transport of complex multiplication and `q` is the squared complex modulus.

## Prior-art boundary

No novelty is claimed for complex multiplication, algebra transport under a bijection, or multiplicativity of the complex modulus. These are standard mathematical facts. The only PDT-II result claimed here is the explicit no-go boundary: an exact positive multiplicative resource law, even one that becomes an additive logarithmic charge, does not by itself prohibit dynamically generated auxiliary sectors.

## PDT-II consequence

A viable PDT-native conservation principle must therefore do more than assign a conserved or multiplicative total resource. It must independently constrain **where the resource may reside** or attach an experimentally excluded cost/signature to transfer into extra sectors. Ordinary total-resource conservation permits redistribution among sectors and cannot non-circularly establish the same-sector premise required by the current `n=3` selectors.

This leaves open a stronger possibility: a PDT-native *sector-resolved* conservation/revelation law with independently measurable charges and superselection-like constraints. That stronger principle must itself be derived rather than chosen to make `n=3` emerge.
