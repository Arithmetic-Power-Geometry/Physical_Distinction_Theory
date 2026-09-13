# Cycle 121 — Visible-quotient underdetermination no-go

## Result

Let `A` be a microscopic carrier, `V` a visible quotient, and `pi : A -> V` a surjective homomorphism for composition. Suppose a proposed PDT law is formulated entirely in terms of projected states `pi(x)` and functions of those projected states (visible probabilities, visible resource scalars, visible refinement records, or algebraic identities in the quotient).

Then every microscopic extension having the same quotient dynamics satisfies exactly the same visible-only law. Consequently, no such law can by itself imply that the microscopic composition of two visible representatives remains in the visible sector.

Formally, if `L` is any statement whose arguments factor through `pi`, and `pi(C_A(x,y)) = C_V(pi(x),pi(y))`, then the truth value of `L` is determined solely by `C_V` and the projected data. Replacing `A` by a nontrivial extension with the same quotient leaves `L` unchanged.

## Explicit associative countermodel

Take `V = R^n` with coordinatewise multiplication `a odot b`. Let `A = V direct_sum V` and define

`(a,m) * (b,r) = (a odot b, a odot r + m odot b + a odot b)`.

Projection `pi(a,m)=a` is a homomorphism:

`pi(x*y)=pi(x) odot pi(y)`.

The product is associative by direct expansion. Yet two visible representatives can generate a hidden component:

`(a,0)*(b,0)=(a odot b, a odot b)`.

The smallest witness is already `n=1`:

`(1,0)*(1,0)=(1,1)`.

Thus every observable or resource law that depends only on the projected value sees exactly the base product `1`, while microscopic same-sector closure fails.

## Consequence

This strictly sharpens the Cycle-120 circularity boundary. It is not enough for a candidate conservation, refinement, revelation, or probability law to be global if the law still factors entirely through the visible quotient. Such a law cannot distinguish the base model from a hidden-sector extension that reproduces all projected data.

Therefore a non-circular PDT route to `V x V -> V` must contain at least one premise with genuinely microscopic/sector-sensitive content: for example, a quantity that does not factor through `pi`, a dynamical constraint on the kernel of `pi`, or an experimentally accessible refinement that couples to the generated sector and changes a same-input prediction.

## Stress audit

Deterministic seeded integer tests covered dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`.

Across 3,040 visible transcript/resource checks there were zero visible mismatches and zero associativity failures. Hidden leakage occurred in 1,472 sampled two-input compositions. These computations are regression evidence; the no-go itself follows algebraically from factorization through the quotient.

## Prior-art boundary

Algebra extensions, square-zero/trivial extensions, ideals, and quotient homomorphisms are standard algebraic constructions. General resource theories likewise distinguish operationally accessible/free structure through specified maps and monotones. This cycle does **not** claim novelty for algebra extensions or quotient theory. The PDT-specific contribution at this stage is only the application of the quotient-underdetermination argument as a falsification guard against claiming that visible-only PDT laws derive microscopic same-sector closure.

Relevant prior-art anchors include standard algebra-extension/idealization constructions and the general quantum-resource-theory framework (e.g. Chitambar & Gour, Rev. Mod. Phys. 91, 025001 (2019)).

## Classification

- **PROVED:** quotient-factorization no-go: laws determined solely by projected data are invariant under microscopic extensions with the same quotient.
- **FALSIFIED:** visible-only conservation/refinement/revelation laws as sufficient non-circular derivations of microscopic same-sector closure.
- **IMPORTED/KNOWN:** algebra extensions, quotient homomorphisms, and generic resource-theory machinery.
- **NUMERICALLY SUPPORTED:** dimension/adversarial transcript audit.
- **OPEN:** a PDT-native sector-sensitive law that does not factor through the visible quotient and yields a falsifiable consequence.
- **BREAKTHROUGH CANDIDATE:** NO.

## Next strongest target

Construct or falsify a PDT-native kernel-sensitive law. Any candidate must be tested against hidden extensions while holding the same visible microscopic input and declared resource window fixed. If it cannot separate the extension from the quotient model, it cannot support either the `n=3` derivation or a same-input deviation from QM.
