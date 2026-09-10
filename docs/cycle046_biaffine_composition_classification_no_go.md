# Cycle 046 — Biaffine composition classification no-go

## Status

**PROVED + FALSIFIED route + IMPORTED/KNOWN algebraic mathematics.**

This result is not a PDT breakthrough candidate. It closes a tempting route to a native scalar composition law.

## Question attacked

Can PDT select a unique scalar composition law by requiring, in addition to symmetry and a trivial unit, that the composite capacity be affine in each subsystem capacity separately?

The answer is **no**.

## Exact hypotheses

Let `F:[1,∞)^2 -> R` be separately affine (biaffine):

`F(a,b) = A ab + B a + C b + D`.

Assume:

1. subsystem exchange symmetry: `F(a,b)=F(b,a)`;
2. trivial-system unit: `F(a,1)=a` for every `a>=1`.

No associativity assumption is initially needed.

## Classification theorem

Symmetry gives `B=C`. The unit identity gives

`A+B=1`, and `B+D=0`.

Writing `k=A-1`, every such law is therefore exactly

`F_k(a,b)=ab+k(a-1)(b-1)`.

Conversely every `F_k` is symmetric, separately affine, and has unit `1`.

More strongly, **every member of this entire classified family is associative**:

`F_k(F_k(a,b),c)=F_k(a,F_k(b,c))`.

A direct linearizing coordinate is

`T_k(q)=1+(k+1)(q-1)`, for which

`T_k(F_k(a,b))=T_k(a)T_k(b)`.

Thus associativity adds no new restriction inside the biaffine symmetric-unit class.

## Domain restrictions still do not select the product law

On `[1,∞)`:

- coordinate monotonicity holds globally iff `k>=-1`;
- preservation of the product-sector lower bound `F_k(a,b)>=ab` for all `a,b>=1` holds iff `k>=0`.

Hence even after demanding symmetry, unit, separate affinity, associativity, monotonicity, and `F>=ab`, infinitely many laws survive: every `k>=0`.

The smallest nontrivial witness is already `a=b=2`:

`F_k(2,2)=4+k`.

So identical local capacities `2,2` admit `4,5,6,...` while satisfying the whole axiom package.

## Falsified route

The implication

> symmetry + unit + separate affinity + associativity + monotonicity + product-sector preservation => `F(a,b)=ab`

is **FALSIFIED**.

The surviving requirement remains the same as in Cycles 039–041: PDT must derive an independent operational calibration or a law governing genuinely global distinction effects. Scalar regularity conditions alone do not determine physical composition.

## Stress tests

The branch implementation performs exact-integer checks for `a,b,c=1..12` and `k=0..11`, plus exact rational coefficient-reduction checks. For each tested `k`, associativity, symmetry, the unit law and the product lower bound are exact. The witness values `F_k(2,2)` run from `4` through `15`.

These tests verify the implementation; the theorem itself is algebraic and does not depend on numerical evidence.

## Prior-art boundary

The classification is elementary functional/algebraic manipulation, while associative binary-operation representation theory is classical. It must not be presented as historically new mathematics. The PDT contribution here is only the **no-go interpretation**: even imposing separate affinity does not rescue uniqueness of scalar distinction composition.

## Consequence for PDT-II

Do not spend further cycles trying to obtain uniqueness by stacking scalar properties of the form continuity/affinity/symmetry/associativity/monotonicity. The high-value composition target is now the admissible **global effect/distinction sector**, or an operationally derived calibration condition strong enough to fix its relation to local sectors.
