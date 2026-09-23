# Cycle 334 — Distinction-capacity multiplicativity does not determine composition or n=3

## Target
Attack PDT-II targets (1) PDT-native composition and (2) a non-circular n=3 derivation using a principle stated directly in distinction language rather than importing another generic reconstruction axiom.

## Candidate principle
For a system A define its distinction capacity C(A) as the maximum cardinality of a set of states that can be perfectly distinguished in one admissible measurement. Test the apparently PDT-native composition rule

C(A ⊗ B) = C(A) C(B).

Candidate claims tested:
1. exact multiplicativity determines the correlated composite;
2. exact multiplicativity selects C=3 as the elementary nontrivial capacity;
3. exact multiplicativity forces a same-input probability law distinct from complex quantum theory.

## Exact counterfamilies
### Classical
For an n-level classical simplex, C=n. The ordinary Cartesian/product simplex has C(A⊗B)=nm=C(A)C(B).

### Complex quantum
For a d-dimensional complex quantum system, C=d: an orthonormal basis gives d perfectly distinguishable states, and no measurement can perfectly distinguish more mutually orthogonal nonzero states than the Hilbert-space dimension. The standard tensor product has dimension d_A d_B, hence C(A⊗B)=d_A d_B=C(A)C(B).

The two theories have radically different state/effect geometry and correlated composites while satisfying exactly the same capacity-multiplication law. Therefore capacity multiplicativity does not determine composition.

## Exact n=1..12 stress
For every n=1,...,12 both the classical n-level model and complex quantum dimension n have C=n. For two identical systems both give C(composite)=n^2. The same proof works for every finite n, so the finite table is only the requested explicit stress window.

| n | C_classical | C_quantum | C_AA both | selects n=3? |
|---:|---:|---:|---:|:---:|
|1|1|1|1|no|
|2|2|2|4|no|
|3|3|3|9|no|
|4|4|4|16|no|
|5|5|5|25|no|
|6|6|6|36|no|
|7|7|7|49|no|
|8|8|8|64|no|
|9|9|9|81|no|
|10|10|10|100|no|
|11|11|11|121|no|
|12|12|12|144|no|

Smallest nontrivial decisive witness: n=2. A classical bit and a qubit both have distinction capacity 2 and multiplicative capacity 4 on a pair, while their normalized state spaces and correlated structures are inequivalent.

## Stronger surviving statement
Capacity multiplicativity constrains only one coarse invariant of a composite. It cannot recover the composite cone/state space/effect space, tensor norm, entangled-state content, or probability functional. Any viable PDT-native composition principle must therefore constrain correlated distinctions beyond the maximum size of a perfectly distinguishable frame.

This is an underdetermination theorem for the proposed inference, not a new characterization of GPT composition.

## Same-input consequence
Complex quantum theory itself satisfies exact distinction-capacity multiplicativity. Therefore the principle cannot logically entail P_PDT(O|I,R) != P_QM(O|I,R). A deviation requires an additional PDT-native rule fixing correlated states/effects, the declared resource window R, and the outcome functional.

## Prior-art check
Perfect distinguishability, information capacity and operational reconstructions are established GPT/quantum-information concepts. Chiribella, D'Ariano & Perinotti's informational reconstruction uses perfect distinguishability among established operational principles; the present capacity notion is therefore not claimed as novel merely by renaming it PDT distinction capacity. Recent GPT work also continues to study universal constraints linking state discrimination/distinguishability to other operational resources. No novelty claim is made for multiplicative capacity itself.

## Status
- Classical finite-family capacity multiplicativity: **PROVED / IMPORTED-KNOWN model**.
- Complex-quantum finite-family capacity multiplicativity: **PROVED / IMPORTED-KNOWN model**.
- Exact n=1..12 stress: **PROVED**.
- C(AB)=C(A)C(B) => unique PDT composition: **FALSIFIED**.
- C(AB)=C(A)C(B) => n=3: **FALSIFIED**.
- C(AB)=C(A)C(B) => same-input PDT/QM deviation: **FALSIFIED**.
- Need for a correlated-distinction invariant beyond capacity: **PROVED as a logical requirement for this route**.
- Independently justified PDT-native correlated-composite selector: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
Stop testing scalar capacity axioms as selectors. The next useful candidate must depend on correlated distinction structure itself (for example a PDT-defined defect under composition/refinement) and must first be checked for invariance/triviality on classical and quantum all-n counterfamilies before any n=3 claim.