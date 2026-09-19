# Cycle 255 — Information-causality selector boundary

## Candidate
Test whether Information Causality (IC), interpreted as a distinction-capacity principle, can provide either (i) the missing PDT-native composition law or (ii) a non-circular selector of n=3.

## Exact hypotheses
Alice holds an N-bit classical database, Bob receives an index, Alice communicates m classical bits, and Alice/Bob may share a nonsignalling resource. IC requires the total accessible information Bob can gain about Alice's database to be at most m. In the standard binary isotropic/CHSH setting, IC excludes correlations beyond the quantum Tsirelson ceiling.

## Prove-or-falsify result
**FALSIFIED as an n=3 selector.** The standard quantum CHSH witness achieving S=2 sqrt(2) is supported on a two-dimensional subspace. The same state and observables embed isometrically into C^n for every n>=2 without changing any probabilities. Therefore any selector based only on satisfying/saturating the IC-implied CHSH/Tsirelson ceiling is dimension-blind: n=2 already survives, as do n=3,... . `experiments/cycle255_information_causality_dimension_stress.py` checks the invariant exact value S^2=8 for n=2..12. The embedding argument proves arbitrary finite n>=2.

**FALSIFIED as a unique composition selector.** IC is a constraint on operational correlations under a communication task. It does not by itself specify a unique composite state/effect cone. Published work explicitly treats the search for principles that single out the quantum correlation set as incomplete; almost-quantum/post-quantum correlation sets survive several major information-theoretic principles. Therefore satisfying IC cannot simply be equated with deriving the quantum tensor product.

A 2022 paper by Patra et al., *Principle of information causality rationalizes quantum composition* (arXiv:2208.13996), is especially important prior art: it already uses IC to rule out minimal/maximal candidate compositions and argues toward self-duality for composites. Thus an IC-based composition restriction is **IMPORTED/KNOWN territory**, not a PDT-native breakthrough. Moreover, restricting extremes is weaker than proving a unique full composite rule.

## Dimension / edge stress
- n=1: degenerate; no nontrivial embedded Bell pair.
- n=2: exact nontrivial survivor with S^2=8; smallest decisive competitor to n=3.
- n=3..12: same two-level embedding, exact S^2=8 regression.
- arbitrary finite n>=2: analytic isometric embedding of the qubit support.
- Classical/local CHSH ceiling has S^2=4; nonsignalling algebraic ceiling has S^2=16. These values are recorded only as comparison anchors, not as PDT predictions.

## Prior-art boundary
- M. Pawlowski et al., *Information causality as a physical principle*, Nature 461, 1101–1104 (2009): introduces IC and derives important restrictions on nonsignalling correlations.
- M. Navascues et al., *Almost quantum correlations*, Nature Communications 6, 6288 (2015): demonstrates a correlation set strictly larger than the quantum set compatible with several proposed physical principles; the broader programme of uniquely recovering quantum correlations remains nontrivial.
- R. K. Patra et al., *Principle of information causality rationalizes quantum composition*, arXiv:2208.13996 (2022): directly explores IC as a constraint on quantum composition, so this route cannot be presented as new PDT provenance.

## Status ledger
- Two-level quantum witness embeds unchanged for every finite n>=2: **PROVED**.
- n=1..12 regression of S^2: **NUMERICALLY/EXACTLY SUPPORTED** (integer/rational regression; analytic embedding is the proof).
- Information Causality principle and Tsirelson-bound application: **IMPORTED/KNOWN**.
- IC-based restrictions on candidate quantum compositions: **IMPORTED/KNOWN**.
- IC/Tsirelson saturation as unique n=3 selector: **FALSIFIED**; smallest nontrivial competitor n=2.
- IC alone as unique PDT composition selector: **FALSIFIED** as presently stated; it constrains correlations but does not supply a unique PDT-native state/effect/dynamics construction.
- PDT-native composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input P_PDT(O|I,R) != P_QM(O|I,R): **OPEN**.
- PDT-native experimentally distinctive inequality: **OPEN**.
- Gravity/capacity law: **OPEN**; no import permitted.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving requirement
A viable PDT-II route must do more than reproduce a known information-theoretic quantum boundary. It must define PDT's admissible composite objects and operational probabilities independently, and then either derive a genuinely new restriction or produce a same-input, resource-declared prediction differing quantitatively from QM. Otherwise the construction remains a reconstruction/import rather than a PDT-native physical law.
