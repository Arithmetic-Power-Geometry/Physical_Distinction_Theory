# Cycle 119 — Faithful hidden-sector monotonicity is sufficient for closure

## Status

- Closure theorem: **PROVED**
- PDT-native derivation of the required resource principle: **OPEN**
- Generic resource-theory mechanism: **IMPORTED/KNOWN**
- Dimension stress audit: **NUMERICALLY SUPPORTED**
- Breakthrough candidate: **NO**

## Exact theorem

Let the microscopic carrier decompose as `A = V ⊕ M`, where `V` is the proposed visible/primitive sector and `M` is an auxiliary sector. Let `H : A -> [0,∞)` satisfy:

1. **Faithfulness to the hidden sector:** `H(v,m)=0` iff `m=0`.
2. **Compositional monotonicity at zero:** for the binary composition `C`, whenever `H(x)=H(y)=0`, one has `H(C(x,y)) <= H(x)+H(y)` (more generally any nonnegative bound with right-hand side zero on two zero-resource inputs is sufficient).

Then `V` is closed under composition.

### Proof

Take `x,y in V`. Faithfulness gives `H(x)=H(y)=0`. Monotonicity gives `H(C(x,y)) <= 0`. Since `H` is nonnegative, `H(C(x,y))=0`. Faithfulness then implies that the hidden component of `C(x,y)` vanishes. Therefore `C(x,y) in V`. QED.

## Why this matters

Cycles 116-118 showed that exact quotient composition, finite revealability, and even an exact positive total conservation law do not force same-sector closure. Cycle 119 identifies a sufficient strengthening: the conservation/monotonicity must be **sector resolved and faithful**, so that hidden-sector creation from zero hidden input is forbidden.

This does **not** yet derive `n=3`. It only supplies the missing logical bridge *if* PDT can independently derive such a hidden-sector resource from its own distinction primitives. Combining this theorem with a previously established conditional `SO(n)`-equivariant alternating same-sector composition selector remains conditional until that physical premise is obtained without importing the desired dimensional result.

## Counterexample guard

The extension-style rule used in earlier cycles,

`(a,m)*(b,r) = (a⊙b, a⊙r + m⊙b + a⊙b)`,

creates hidden resource from two zero-hidden inputs. For `(2,0)` and `(3,0)`, the hidden output is `6`, so `H_out=36` for `H(m)=||m||_2^2`; therefore it is excluded exactly because it violates the new premise, not because it was algebraically inconsistent.

## Stress audit

The deterministic seeded audit covers `n=1..12` and `16,24,32,48,64,96,128`: 1,340 visible-input trials, zero failures for a composition respecting the zero-hidden closure condition, and 1,289 hidden-sector generations for the extension counter-rule.

The numerical audit is regression evidence only; the theorem itself is elementary and exact.

## Prior-art/novelty guard

The abstract pattern is standard resource-theory logic: a faithful nonnegative resource monotone whose zero set is the free set makes the free set invariant under operations that cannot generate the resource. No novelty is claimed for that abstract mechanism. PDT novelty would require deriving the relevant sector-resolved resource and its monotonicity from independently motivated PDT primitives, and ideally connecting it to a falsifiable same-input prediction.

## Next prove-or-falsify obligation

Attempt to derive a **PDT-native faithful sector resource** from distinction/revelation accounting. Required kill tests:

- coarse-graining and refinement;
- reversible group actions and alternative norms;
- composites/tensor rules;
- pure/mixed states;
- Markovian and non-Markovian dynamics;
- controlled-environment records;
- thermodynamic settings;
- same-input comparison against QM/GPT/resource-theory models.

If no such native resource can be derived, same-sector closure and the downstream `n=3` selector remain conditional.
