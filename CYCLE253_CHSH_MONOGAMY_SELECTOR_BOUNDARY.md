# Cycle 253 — CHSH-monogamy selector boundary

## Candidate
Test whether a PDT-native "one distinction cannot be maximally nonlocal with two independent partners" / CHSH-monogamy principle could (i) determine the composite rule or (ii) non-circularly select n=3.

## Exact hypotheses
Three systems A,B,C admit two dichotomic observables per party. Let S_AB and S_AC denote the corresponding CHSH expectation values sharing A's two observables. Candidate selector: admissible composites obey a monogamy trade-off of the quantum form S_AB^2 + S_AC^2 <= 8.

## Prove-or-falsify result
**FALSIFIED as an n=3 selector.** Toner & Verstraete proved the quantum CHSH monogamy trade-off for shared states of arbitrary dimension. Therefore the property is explicitly dimension-uniform and cannot single out n=3. The smallest nontrivial competing local dimension is n=2.

An explicit survivor family embeds a Bell pair in a two-dimensional AB subspace for every n>=2 and takes C uncorrelated. Standard CHSH observables on the support give S_AB=2 sqrt(2), while the AC correlators vanish because A's reduced state is maximally mixed on the support and the two A observables are traceless there. Hence S_AB^2+S_AC^2=8 for every n>=2. The construction is independent of unused dimensions.

**FALSIFIED as a unique composition selector.** A Bell-correlation inequality constrains an operational projection of an already-specified composite; it does not by itself specify the full composite state/effect cones or tensor rule. Moreover, monogamy is not exclusive to a single quantum tensor construction: Barrett, Kent & Pironio proved monogamy statements for correlations under the broader nonsignalling constraint. Thus a generic monogamy requirement is insufficient to identify a unique PDT composite.

## Dimension and edge stress
`experiments/cycle253_chsh_monogamy_dimension_stress.py` checks the explicit embedded witness for n=1..12. n=1 is marked degenerate; every n=2..12 saturates S_AB^2+S_AC^2=8 numerically to floating-point tolerance. Because the same 2D support embeds in every n>=2, this is also an analytic arbitrary-dimension counterfamily; random higher-dimensional tests cannot rescue an n=3 selector.

Edge cases: n=1 has no nontrivial two-level CHSH witness. Product AC gives S_AC=0. Unused dimensions are assigned reversible dichotomic extensions but have zero state support, so they do not affect the witness.

## Prior-art boundary
- B. Toner & F. Verstraete, *Monogamy of Bell correlations and Tsirelson's bound*, quant-ph/0611001 (2006): characterizes the AB/AC CHSH trade-off for quantum states of arbitrary dimension.
- J. Barrett, A. Kent & S. Pironio, *Maximally Nonlocal and Monogamous Quantum Correlations*, Phys. Rev. Lett. 97, 170409 (2006), DOI 10.1103/PhysRevLett.97.170409: establishes monogamy results within nonsignalling correlations using chained Bell inequalities.

Therefore CHSH/Bell monogamy itself is **IMPORTED/KNOWN**, not PDT novelty.

## Status ledger
- Embedded Bell-pair survivor for every n>=2: **PROVED** analytically; n=2..12 regression is **NUMERICALLY SUPPORTED**.
- Quantum CHSH monogamy theorem: **IMPORTED/KNOWN**.
- CHSH monogamy as unique n=3 selector: **FALSIFIED**; smallest competitor n=2.
- Generic Bell monogamy as unique composition selector: **FALSIFIED**.
- PDT-native composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input P_PDT(O|I,R) != P_QM(O|I,R): **OPEN**.
- PDT-native experimentally distinctive inequality: **OPEN**.
- Gravity/capacity law: **OPEN**; no import permitted.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving requirement
A viable PDT-II composition principle must constrain the full admissible composite, not merely one Bell projection, and a viable n=3 selector must contain a genuinely PDT-native dimension-sensitive obstruction that fails already for n=2 and for every n>=4 without encoding three in its assumptions.
