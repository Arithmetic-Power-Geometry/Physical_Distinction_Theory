# Cycle 217 — Purification cannot serve as a PDT-native composition selector without importing the target theory

## Status

- **PROVED (conditional methodological no-go)**: if PDT adopts an axiom package already sufficient to reconstruct ordinary complex quantum theory, then that package cannot simultaneously yield a genuinely PDT-native same-input prediction different from quantum theory on the reconstructed operational domain without adding a further independent PDT postulate.
- **IMPORTED/KNOWN**: purification and purification-based reconstruction are established operational/GPT principles.
- **FALSIFIED**: the proposed shortcut “add purification as the missing PDT composition law, derive the quantum composite/n=3, and then claim a PDT-vs-QM deviation from those same axioms.”
- **OPEN**: a PDT-native resource-indexed joint-admissibility law; non-circular n=3; a same-input PDT-vs-QM prediction with a declared resource window.
- **BREAKTHROUGH CANDIDATE: NO**.

## Candidate attacked

After Cycle 216, an obvious escape route is to strengthen the composite axioms by adding **purification** (possibly together with causality, local discriminability/tomography, ideal compression, perfect distinguishability and related reconstruction assumptions) and use the resulting structure as PDT's missing composition selector.

That route is scientifically useful only if the added principle is independently PDT-native. Otherwise it imports an existing reconstruction.

## Exact conditional theorem

Let `A` be an operational axiom set and let `Q(A)` denote the class of operational theories satisfying it. Assume a reconstruction theorem establishes

`A  =>  operational theory is ordinary complex quantum theory Q`

on the domain under discussion (states, transformations, composites and outcome rule). Suppose PDT-II uses exactly `A` to determine its operational predictions on that domain and introduces no additional prediction-changing postulate. Then for every identical microscopic/operational input `I`, declared resource window `R` represented inside that reconstructed domain, and outcome `O`,

`P_PDT(O | I,R) = P_Q(O | I,R)`.

### Proof

By hypothesis, every PDT operational model satisfying `A` on the stated domain is operationally quantum. Operational equivalence means that corresponding preparations, transformations and measurements have the same outcome probabilities. Therefore the conditional outcome distributions coincide for every corresponding `(I,R,O)`. A strict inequality requires at least one additional assumption that either (i) changes the operational theory, (ii) changes the admissible resource/intervention set, or (iii) changes the input correspondence. In cases (i)-(ii) the new assumption, not purification/reconstruction alone, is the source of the deviation; in case (iii) the comparison is no longer a same-input comparison. QED.

This is intentionally conditional. It does **not** claim purification alone reconstructs quantum theory.

## Prior-art boundary

Purification is established GPT/operational-reconstruction machinery. Chiribella, D'Ariano and Perinotti define purification as existence of a purification for every mixed state with essential uniqueness up to reversible channels on the purifying system, and show strong consequences including reversible dilation of physical processes. Their 2011 informational reconstruction uses five additional informational axioms plus purification to derive quantum theory. Therefore simply adopting that reconstruction package cannot count as a PDT-native composition breakthrough.

The boundary is even sharper: purification by itself is not a unique selector of ordinary complex quantum theory. The literature on sharp theories with purification explicitly includes non-identical theories, including complex and real quantum theory and other examples. Real-vector-space quantum theory satisfies purification while failing local tomography. Thus “purification” should be classified as a powerful constraint, not as a uniquely PDT or uniquely complex-quantum composition law.

Primary literature anchors:

- G. Chiribella, G. M. D'Ariano, P. Perinotti, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348 (2010), DOI 10.1103/PhysRevA.81.062348.
- G. Chiribella, G. M. D'Ariano, P. Perinotti, *Informational derivation of quantum theory*, Phys. Rev. A 84, 012311 (2011), DOI 10.1103/PhysRevA.84.012311.
- G. Chiribella, C. M. Scandolo, *Entanglement as an axiomatic foundation for statistical mechanics*, arXiv:1608.04459; sharp theories with purification include multiple non-identical theories.

## Consequence for n=3

If a distinguished `n=3` appears only after importing an axiom package already known to reconstruct the desired quantum geometry/composition, the derivation is not PDT-native. To be non-circular, PDT must first state an independently motivated physical distinction/resource principle and then prove that `n=3` follows from it without selecting the target quantum structure by assumption.

## Consequence for the same-input prediction target

This cycle rules out a common but invalid strategy: reconstruct QM and then search algebraically inside the reconstructed theory for a PDT-vs-QM discrepancy under identical inputs. There can be none unless PDT contributes an additional operational restriction or law. The next high-value search therefore must target such an independently physical PDT ingredient, preferably a resource-indexed admissibility law with a measurable calibration.

## Stress-test interpretation

The theorem is logical rather than numerical, so dimensions 1..12 do not require simulation: wherever the reconstruction hypothesis holds, equality of operational predictions follows pointwise in every dimension covered by the reconstruction. Where the hypothesis does not hold (e.g. alternative GPTs, real quantum theory, restricted-resource subtheories), the theorem makes no equality claim; those are precisely the domains in which a PDT-native selector must be tested.

## Surviving target

Do **not** promote purification, self-duality, spectrality, or reversible-group closure merely because they narrow the GPT cone. For each proposed selector, first ask:

1. Is it independently derived from PDT's physical-distinction/resource semantics?
2. Is it already an axiom in a known reconstruction?
3. Does it uniquely fix the composite, or only narrow a family?
4. If it fixes ordinary QM, what additional PDT postulate could still produce a same-input quantitative deviation without changing the declared inputs?

Until those questions have a non-imported answer, composition, n=3 and the PDT-vs-QM prediction remain **OPEN**.
