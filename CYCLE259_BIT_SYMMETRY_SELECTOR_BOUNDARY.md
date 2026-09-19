# Cycle 259 — Bit symmetry is not an n=3 or unique-composition selector

## Target attacked
1. PDT-native composition law.
2. Non-circular PDT-native derivation of n=3.

## Candidate principle
**Bit symmetry:** for any two logical bits, i.e. ordered pairs of perfectly distinguishable pure states, there is a reversible transformation mapping one ordered pair to the other.

## Exact hypotheses
Finite-dimensional complex quantum state space on C^n, pure states represented by rays, perfect distinguishability by orthogonality, reversible transformations including unitary transformations.

## Proof / counterfamily
For every n >= 2 and any two ordered orthonormal pairs (psi0,psi1) and (phi0,phi1), extend each pair to an orthonormal basis. The linear map sending the first basis to the second is unitary and maps psi_i to phi_i for i=0,1. Hence complex quantum theory is bit-symmetric in every finite dimension n>=2. In particular n=2 is already a nontrivial survivor distinct from n=3. Therefore bit symmetry cannot select n=3.

The repository harness `experiments/cycle259_bit_symmetry_dimension_stress.py` supplies an exact rational witness for n=2,...,12 (basis-bit swap, identity on the complement). n=1 is explicitly classified as degenerate because no nontrivial logical bit exists. The analytic argument covers all finite n>=2, so higher-dimensional random tests cannot overturn the selector falsification.

## Composition boundary
Bit symmetry constrains the reversible automorphism group of an already specified state/effect model. It does not by itself specify the bipartite positive cone, admissible entangled states/effects, or tensor product. Therefore using bit symmetry alone as the missing PDT composition law is underdetermined. Published GPT work does show that bit symmetry entails self-duality and imposes bipartite restrictions stronger than no-signalling; these are constraints, not a unique composite construction.

## Prior-art audit
Müller & Ududec, *Physical Review Letters* 108, 130401 (2012), prove that bit symmetry entails self-duality in GPTs and discuss restrictions on bipartite states. This principle and that consequence are therefore IMPORTED/KNOWN, not PDT novelty.

Barnum & Hilgert (2019), *Strongly symmetric spectral convex bodies are Jordan algebra state spaces*, prove that strong symmetry plus spectrality leads to simple Euclidean Jordan algebra state spaces (or simplices). This further blocks novelty claims based merely on strengthening bit symmetry to frame/strong symmetry; additional assumptions are needed to isolate ordinary complex quantum theory.

## Adversarial result
Smallest decisive nontrivial dimension counterexample to an n=3 selector: n=2. It satisfies the candidate exactly. The same construction embeds in every n>=2.

## Status
- Bit symmetry in finite-dimensional complex QM for every n>=2: **PROVED**.
- Exact n=1,...,12 basis witness: **PROVED** (n=1 degenerate; n>=2 survive).
- Bit symmetry as unique n=3 selector: **FALSIFIED**.
- Bit symmetry alone as unique PDT composition law: **FALSIFIED AS STATED / UNDERDETERMINED**.
- Bit symmetry => self-duality: **IMPORTED/KNOWN**.
- Strong symmetry + spectrality => Jordan-algebraic boundary: **IMPORTED/KNOWN**.
- PDT-native composition law: **OPEN**.
- Same-input quantitative P_PDT != P_QM: **OPEN**.
- PDT-native experimentally distinctive inequality: **OPEN**.
- Gravity/capacity law: **OPEN; not promoted**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Do not spend further cycles renaming established GPT reconstruction axioms. Search instead for a genuinely PDT-native cross-system operation whose admissible composite cone is mathematically forced, or derive a same-input probability law differing from QM under a declared finite resource window. Any proposed law must first survive n=2 and embedding counterfamilies.
