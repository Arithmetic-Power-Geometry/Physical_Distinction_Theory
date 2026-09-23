# PDT-II Cycle 353 — Monoidal-coherence composition no-go

## Target attacked
1. PDT-native composition law; secondarily the non-circular n=3 selector and same-input PDT/QM prediction target.

## Candidate
Suppose physical composition is required only to be a symmetric monoidal operation: it has a unit object, is associative up to coherent reversible identification, and is symmetric under interchange of factors. Ask whether these coherence requirements determine the PDT composite, select n=3, or force a same-input departure from quantum mechanics.

## Exact hypotheses
For systems A,B,C with composite `⊗` and unit `I`, assume natural reversible identifications
`(A⊗B)⊗C ≅ A⊗(B⊗C)`, `I⊗A ≅ A ≅ A⊗I`, and `A⊗B ≅ B⊗A`, satisfying the standard coherence equations. No Hilbert tensor product, Born rule, state cone, or correlation set is assumed.

## Result
**FALSIFIED as a selector.** Symmetric-monoidal coherence constrains how an already supplied composition behaves; it does not specify which composite state/effect cone or probability rule is physically admissible.

Two inequivalent all-dimension counterfamilies suffice:

* finite classical systems with Cartesian/product probability composition;
* finite-dimensional complex quantum systems with the usual tensor product and completely positive processes.

Both obey unit, associativity and swap coherence for every finite system size, while they have inequivalent state geometries and correlation structure. Therefore the coherence package cannot uniquely determine PDT composition and cannot select n=3. The smallest nontrivial witness is n=2; dimensions 1..12 are an immediate exact audit and the counterfamily extends to every finite n.

## Stronger surviving statement
**PROVED (logical boundary):** any PDT-native composition selector must contain physical content beyond symmetric-monoidal coherence. In particular, coherence alone cannot choose the admissible correlated states/effects, nor can it imply `P_PDT(O|I,R) != P_QM(O|I,R)`, because ordinary finite-dimensional quantum theory itself satisfies the hypotheses.

This does not prove that a richer monoidal axiom package cannot select a theory. It only falsifies the bare coherence route.

## Prior-art audit
This is not a PDT novelty claim. Symmetric monoidal categories are standard compositional infrastructure in categorical quantum mechanics and operational probabilistic theories. Barnum, Duncan and Wilce (2013, J. Philosophical Logic; arXiv:1004.2920) explicitly study symmetric monoidal categories of convex operational models, including classical and quantum cases. Wilce's work on symmetry/composition constructs monoidal probabilistic theories. Coecke et al. (2018, arXiv:1803.00708) obtain a uniqueness theorem only after substantially stronger assumptions (free finite-dimensional modules, bilinearity and compact closure), underscoring that bare coherence is not such a uniqueness theorem.

## Dimension/adversarial audit
| n | classical symmetric monoidal witness | complex-QM symmetric monoidal witness | n=3 selected? |
|---:|:---:|:---:|:---:|
| 1 | yes | yes | no |
| 2 | yes | yes | **no — decisive** |
| 3 | yes | yes | no |
| 4–12 | yes | yes | no |
| arbitrary finite n | yes | yes | no |

Degenerate unit systems are covered by n=1. Mixed states do not repair uniqueness: both families are convex and closed under their standard composites. Pure product states also exist in both families. Markovian/non-Markovian dynamics and thermodynamic restrictions are additional structure and therefore cannot be inferred from coherence alone.

## Status ledger delta
- symmetric-monoidal coherence: **IMPORTED/KNOWN**
- coherence ⇒ unique PDT composition: **FALSIFIED**
- coherence ⇒ n=3: **FALSIFIED**
- coherence ⇒ same-input PDT/QM deviation: **FALSIFIED as an inference**
- necessity of extra physical joint structure beyond bare coherence for uniqueness over these counterfamilies: **PROVED**
- PDT-native joint selector: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**

No gravity/capacity claim is made.