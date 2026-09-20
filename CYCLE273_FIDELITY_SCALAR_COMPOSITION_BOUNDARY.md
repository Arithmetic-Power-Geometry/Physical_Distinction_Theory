# Cycle 273 — Fidelity/Hellinger scalar-composition boundary

## Target attacked
PDT-II target (1), PDT-native composition law, with consequences for target (2), a non-circular n=3 derivation.

## Candidate
For finite classical distributions p,q define the Bhattacharyya coefficient

B(p,q) = sum_i sqrt(p_i q_i)

and squared Hellinger distinction

H2(p,q) = 1 - B(p,q).

For independent product hypotheses, ask whether a scalar-only composition law exists.

## Theorem (PROVED)
For arbitrary finite distributions p,q on A and r,s on B,

B(p tensor r, q tensor s) = B(p,q) B(r,s),

hence

H2_AB = H2_A + H2_B - H2_A H2_B.

### Proof
Direct factorization gives

sum_{i,j} sqrt(p_i r_j q_i s_j)
= (sum_i sqrt(p_i q_i))(sum_j sqrt(r_j s_j)).

Substituting B=1-H2 gives the second identity. No dimension assumption enters.

## Stress-test consequence
The identity holds for n=1 through n=12 and, analytically, for every finite local dimension. Zero-padding preserves B and H2, so it cannot impose an ambient upper bound n<=3. It also applies to degenerate distributions and boundary points; if p=q then H2=0 and the law reduces correctly, while mutually disjoint support gives H2=1.

The accompanying exact regression uses rational perfect-square distributions so every Bhattacharyya coefficient is rational and checks n=1..12 without floating-point tolerance.

## Counterexample to a stronger PDT claim
A universal statement that scalar local distinction can never admit an exact product-composition rule is false: Hellinger/Bhattacharyya distinction supplies one. Conversely, Cycle 272 proved that total-variation/trace distinction does not admit a universal rule depending only on the two local scalar TV values. Therefore the existence or nonexistence of scalar composition is metric-dependent, not a PDT selector by itself.

## Quantum/GPT comparison and prior-art boundary
The corresponding quantum fidelity is standard quantum-information structure and is multiplicative on tensor products. Thus importing fidelity/Hellinger multiplicativity would not be PDT-native. Recent resource-theory work also explicitly studies multiplicativity/additivity properties of fidelity-derived monotones (Rubboli, Takagi & Tomamichel, Quantum 8, 1492 (2024), DOI 10.22331/q-2024-10-04-1492). The classical identity above is elementary and known.

A genuinely PDT-native composition result must therefore do more than choose a distinction functional with a convenient tensor law: PDT must independently derive why that functional and its operational resource window are forced, or predict a composition statistic differing from QM/GPT under identical microscopic inputs.

## Status ledger
- Bhattacharyya product multiplicativity: **PROVED**.
- Hellinger-squared scalar product law: **PROVED**.
- Exact n=1..12 regression: **PROVED** by accompanying test.
- Extension to all finite dimensions: **PROVED** analytically.
- Fidelity/Hellinger composition as PDT novelty: **IMPORTED/KNOWN**.
- Scalar composition law => n=3: **FALSIFIED**.
- Scalar-composition impossibility for all distinction metrics: **FALSIFIED**.
- PDT-native composition selector: **OPEN**.
- Same-input P_PDT != P_QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Research decision
Do not spend further cycles searching for n=3 from bare multiplicativity of a scalar metric. Any surviving composition candidate must contain a PDT-derived operational restriction that is absent from ordinary fidelity/Hellinger theory and must be tested against classical, quantum, and GPT realizations under the same declared resource window.
