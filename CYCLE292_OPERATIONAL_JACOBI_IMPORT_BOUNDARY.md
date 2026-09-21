# Cycle 292 — Operational Jacobi import boundary

## Target
Attack the strongest surviving PDT-II n=3 route after Cycles 289–291: derive the Jacobi identity from an operational sequential-distinction principle rather than postulating Jacobi algebraically.

## Candidate principle tested
Let reversible distinction operations form a smooth local composition structure. Define the infinitesimal distinction bracket by the leading noncommutativity of a reversible commutator loop,

\[
[X,Y] := \lim_{\epsilon\to0}\epsilon^{-2}\big( e^{\epsilon X}e^{\epsilon Y}e^{-\epsilon X}e^{-\epsilon Y}-I\big),
\]

where the expression is understood in the tangent algebra of the reversible transformation group.

Operational reading: a small closed sequence X,Y,-X,-Y records the second-order failure of the two distinction operations to commute. Require ordinary reversible path composition (group composition), smoothness near the identity, and closure of the infinitesimal generators.

## Result
**PROVED / IMPORTED-KNOWN:** under these hypotheses the tangent bracket is a Lie bracket and therefore satisfies Jacobi,

\[
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
\]

This is not PDT-specific. It is the standard Lie-group/Lie-algebra consequence of smooth reversible group composition (equivalently obtainable from associative operator commutators/BCH/Hall–Witt at infinitesimal order).

Combining this imported Jacobi property with the already-tested normed binary cross-product hypotheses removes the n=7 octonionic survivor and leaves n=3 among the nontrivial cross-product dimensions. But this does **not** constitute a PDT-native derivation of n=3 unless PDT independently derives why its physical distinction operation must be the tangent commutator bracket of a smooth reversible group and why the same bracket must also obey the normed cross-product/area law.

## Adversarial check: dimension selection
The smooth-reversible-group hypothesis itself does not select dimension. Matrix groups SO(n), SU(n), and many other Lie groups exist in arbitrary dimensions/ranks and their tangent brackets satisfy Jacobi. Thus

\[
\text{smooth reversible operational composition} \not\Rightarrow n=3.
\]

The n=3 selection occurs only after adding the separate normed cross-product assumptions. Therefore claiming that operational reversibility alone derives n=3 would be circular/incorrect.

## Relation to the n=7 countermodel
The 7D octonionic cross product is normed and antisymmetric but is not a Lie bracket: its Jacobiator is nonzero (Cycle 290 exact witness), while it satisfies weaker Moufang/Malcev structure (Cycle 291). Requiring a Lie tangent bracket excludes that algebra, but the exclusion comes from the imported smooth-group substrate unless PDT supplies an independent physical derivation.

## Prior-art boundary
Classical Lie theory already establishes Jacobi for tangent algebras of smooth local/group transformations; associative commutator brackets also satisfy Jacobi identically. Classical vector-cross-product results establish the 3/7 normed-cross-product alternatives and the Jacobi failure of the 7D octonionic product. Accordingly none of those mathematical implications is claimed as PDT novelty.

## Status ledger
- Smooth reversible group composition => infinitesimal Jacobi: **PROVED / IMPORTED-KNOWN**.
- Smooth reversible group composition => n=3: **FALSIFIED** (arbitrary-dimensional Lie-group families).
- Normed cross product + imported Lie/Jacobi bracket => n=3 among nontrivial binary cross-product dimensions: **CONDITIONAL / IMPORTED-KNOWN**.
- PDT-native reason that physical distinctions must simultaneously be normed cross products and Lie tangent brackets: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input quantitative PDT-vs-QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Consequence for next cycle
Do not spend further cycles merely renaming Lie/Jacobi as path consistency. The next viable attack must either (a) derive the bracket identification from a PDT-native operational postulate with independent empirical meaning, then adversarially test whether that postulate holds outside n=3; or (b) return to the higher-priority composition/same-input prediction targets and seek a genuinely PDT-specific constraint. Any proposal that assumes an associative operator algebra, Lie group, SO(3), quaternionic structure, or Jacobi at the outset is imported rather than a PDT derivation.
