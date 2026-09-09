# Cycle 032 — Tensor-closure no-go for universal finite dimension selectors

## Result

Let `S` be a nonempty set of positive integers interpreted as the dimensions admitted for systems of one universal class. Assume ordinary finite-dimensional tensor composition is allowed and composites remain systems of that same class, so

\[
a,b\in S \implies ab\in S.
\]

If `d>1` lies in `S`, closure implies

\[
d,d^2,d^3,\ldots \in S.
\]

These values are all distinct. Hence `S` is infinite.

Therefore no **finite** universal dimension selector containing a nontrivial dimension can be closed under ordinary tensor composition. In particular,

\[
\{3\},\qquad \{3,7\},\qquad \{1,3,7\}
\]

all fail tensor closure. The immediate witnesses are `3 x 3 = 9` and `7 x 7 = 49`.

For a singleton `{d}`, tensor closure requires `d^2=d`. Over positive integers the unique solution is

\[
\boxed{d=1}.
\]

Thus a universal rule saying **every** distinction space, including composites, has dimension exactly 3 is incompatible with ordinary tensor composition.

## Proof status

**PROVED** as an elementary consequence of multiplicative dimension and closure. The theorem is conditional on the physical interpretation that (i) the chosen dimension is faithful for the full system space, (ii) ordinary tensor products model composition, and (iii) the selector is meant to apply to composites in the same way it applies to irreducible systems.

## Robustness and alternatives

The obstruction is not special to the Cycle 030 NDC construction. It applies to any finite global selector under multiplicative tensor dimensions. An additive/direct-sum composition rule is also incompatible with a globally fixed positive dimension because self-composition gives `d+d=2d>d`.

A more general extensive-composition version is immediate: if a self-composition rule gives `F(d,d)>d`, then a universal rule requiring the composite to retain dimension exactly `d` already fails in one step.

## What this does NOT rule out

1. **Irreducible-sector selection.** PDT may still derive dimension 3 for primitive/irreducible distinction sectors while composite systems occupy larger spaces.
2. **Graded or sector-valued dimensions.** A composite may decompose into irreducible sectors, with the selector acting only on sector labels.
3. **Restricted-resource quotients.** An effective operational dimension may cease to be faithful or multiplicative after quotienting inaccessible distinctions; this requires a separately defined quotient and cannot be assumed.
4. **Nonstandard composition.** A genuinely PDT-native composition law could avoid multiplicative dimension, but it must be independently motivated and tested rather than chosen merely to preserve `n=3`.

## Exact and computational audit

- All pair products for dimensions 1 through 12 are checked by unit test.
- Singleton tensor fixed points are checked through 256; only 1 survives.
- The exact 3-copy ladder through 12 copies is

\[
3,9,27,81,243,729,2187,6561,19683,59049,177147,531441.
\]

The analytic proof covers all positive integer dimensions, so the finite sweep is verification rather than evidence for the theorem.

## Prior-art boundary

No novelty claim is made for dimension multiplicativity or for the elementary closure argument. Finite-dimensional tensor products have multiplicative dimensions, and multiplicative dimension functions are standard in monoidal/tensor-category mathematics. In GPT and quantum-reconstruction work, the structure of composite systems and multiplicative capacities/dimensions are established ingredients. The PDT contribution of this cycle is therefore a **research constraint/no-go ledger item**, not a new mathematical theorem.

Relevant prior-art directions include finite-dimensional tensor products, categorical dimension functions, Hardy-style and Masanes–Müller-style reconstructions, and GPT local-tomography/composition literature.

## Consequence for the PDT n=3 program

The current program should stop trying to make `n=3` a dimension of every composite distinction space under ordinary tensor products. A viable route must instead derive something like

\[
\boxed{\text{primitive/irreducible distinction sector dimension}=3}
\]

plus an independently justified rule for how such sectors compose.

That is a narrower but composition-consistent target.

## Classification

- **PROVED** — closure theorem under stated assumptions.
- **CONDITIONAL** — physical consequence depends on the interpretation of dimension and composition.
- **IMPORTED/KNOWN** — mathematical ingredients are standard prior art.
- **BREAKTHROUGH CANDIDATE:** no.
