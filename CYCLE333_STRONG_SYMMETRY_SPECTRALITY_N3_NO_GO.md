# Cycle 333 — Strong symmetry + spectrality does not select n=3

## Target
Attack PDT-II targets (1) PDT-native composition and (2) a non-circular n=3 derivation by testing whether a natural distinction-native-looking package — spectral decomposability into perfectly distinguishable pure states plus strong symmetry on distinguishable frames — singles out three alternatives.

## Hypotheses tested
For a finite-dimensional normalized state space Ω:

1. **Spectrality:** every state is a convex combination of perfectly distinguishable pure states.
2. **Strong symmetry:** for each k, the reversible affine group acts transitively on ordered k-tuples of perfectly distinguishable pure states (where such tuples exist).

Candidate claim: these hypotheses force distinguished capacity n=3, or uniquely determine a PDT composite/probability law.

## Exact counterfamily
For every integer n >= 1 take the classical simplex Δ_(n-1).

* Pure states are the n vertices e_1,...,e_n.
* Every probability vector p=(p_1,...,p_n) has the spectral decomposition p = Σ_i p_i e_i into perfectly distinguishable pure states.
* The reversible group contains S_n. For every k <= n, S_n is transitive on ordered k-tuples of distinct vertices. Hence strong symmetry holds.

Therefore the same hypotheses hold for every n. In particular n=2 and n=4 are immediate countermodels to any implication selecting n=3. The smallest nontrivial witness is n=2.

## n=1..12 exact stress
| n | simplex spectral | strong symmetry | selects n=3? |
|---:|:---:|:---:|:---:|
|1|yes|yes|no|
|2|yes|yes|no|
|3|yes|yes|no|
|4|yes|yes|no|
|5|yes|yes|no|
|6|yes|yes|no|
|7|yes|yes|no|
|8|yes|yes|no|
|9|yes|yes|no|
|10|yes|yes|no|
|11|yes|yes|no|
|12|yes|yes|no|

This is analytic for all finite n; the table is only an explicit requested stress range.

## Composition and same-input consequence
Neither hypothesis specifies a tensor/composite rule. More strongly, the package is not PDT-native novelty: prior GPT reconstruction work proves that strongly symmetric spectral convex bodies are Jordan-algebra state spaces or simplices. Thus importing these assumptions cannot itself be promoted as a PDT breakthrough.

Since ordinary classical simplexes already satisfy both assumptions at arbitrary n, the assumptions do not entail a unique correlated-composite selector. They consequently cannot entail a parameter-free same-input inequality P_PDT(O|I,R) != P_QM(O|I,R). Any such prediction needs an additional independently justified PDT-native rule that fixes the composite/resource window and probability functional.

## Prior-art rejection
Barnum & Hilgert, *Strongly symmetric spectral convex bodies are Jordan algebra state spaces* (2019), arXiv:1904.03753, establishes that strongly symmetric spectral convex compact sets are precisely normalized state spaces of finite-dimensional simple Euclidean Jordan algebras and simplices. Therefore spectrality + strong symmetry is established GPT/Jordan reconstruction structure, not PDT novelty.

## Status
- Spectrality + strong symmetry on every finite classical simplex: **PROVED**.
- All-n counterfamily, including exact n=1..12 stress: **PROVED**.
- Strong symmetry / spectrality reconstruction mechanism: **IMPORTED/KNOWN**.
- spectrality + strong symmetry => n=3: **FALSIFIED**.
- spectrality + strong symmetry => unique PDT composition: **FALSIFIED as an inference**.
- spectrality + strong symmetry => same-input PDT/QM deviation: **FALSIFIED as an inference**.
- Independently derived PDT-native correlated-composite selector: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
Do not stack further generic GPT reconstruction axioms merely to force n=3. Search instead for a rule defined directly from PDT distinction/refinement operations whose content is not equivalent to known spectrality, symmetry, tomography, purification, no-restriction, or tensor-norm assumptions. Any candidate must first survive the all-n simplex counterfamily before expensive numerical testing.
