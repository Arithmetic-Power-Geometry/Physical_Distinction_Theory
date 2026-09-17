# Cycle 214 — Calibrated Energy Does Not Force Revelation

## Target
PDT-II target (4), with consequences for (1)–(3): test the strongest surviving proposal from Cycle 213 — whether replacing an arbitrary scalar resource parameter by a physically calibrated resource such as energy is sufficient to force eventual revelation of dynamically relevant distinctions.

## Exact hypotheses
Let the microscopic state space be finite, `X={0,...,n-1}`, with `n>=3`. Let `E>=0` be an energy budget measured in fixed physical units. For each E let `A_E` be the admissible observation family. Assume only:

1. **Nested access:** `E<=E' => A_E subseteq A_E'`.
2. **Physical calibration:** E is not freely reparameterized; it denotes the declared apparatus/control energy budget.
3. **Symmetry restriction:** every admissible observation is invariant under a fixed nontrivial microscopic symmetry `g` exchanging states 0 and 1: `a(0)=a(1)` for every `a in A_E`, at every finite E.
4. **Dynamical relevance:** microscopic dynamics distinguishes the pair, e.g. `F(0)=0`, `F(1)=1`, `F(2)=0` (and arbitrary extension for higher n).

Define resource-relative operational equivalence by

`x ~_E y iff a(x)=a(y) for every a in A_E`.

## Theorem 214.1 — calibrated-resource revelation no-go
Under hypotheses 1–4, `0 ~_E 1` for every E, even though 0 and 1 are dynamically distinct. Therefore no theorem of the form

> sufficiently large physically calibrated energy necessarily reveals every dynamically relevant distinction

follows from resource calibration + nested accessibility alone.

### Proof
Hypothesis 3 directly gives `a(0)=a(1)` for every admissible a at every E. By definition, `0 ~_E 1` for every E. Hypothesis 4 makes the hidden pair dynamically relevant. Increasing E may enlarge `A_E` strictly through additional symmetry-invariant observables, but none separates the pair. QED.

## Strict-growth witness
For n>=4, one may add states 3,...,n-1 and let increasing budgets successively admit indicator observables of these states while retaining `a(0)=a(1)`. Thus the admissible algebra can grow strictly at many thresholds without revealing the protected pair. For arbitrarily large finite n this gives arbitrarily many genuine resource-refinement events with zero revelation of the protected distinction.

For n=3 the constant family already supplies the smallest decisive witness. The theorem is not based on a lack of resource growth; the n>=4 construction demonstrates strict growth explicitly.

## Boundary / surviving theorem
A positive revelation theorem requires an additional **separation hypothesis**. One sufficient form is:

For every dynamically relevant pair x,y there exists a finite physical threshold `E_xy` and an admissible observation `a in A_{E_xy}` with `a(x) != a(y)`.

Then all dynamically relevant pairs are revealed by `E_* = max_{x,y} E_xy` on a finite state space. This statement is mathematically immediate but **CONDITIONAL**: the separation hypothesis contains the substantive physics that PDT must derive rather than assume.

## Prior-art boundary
Energy calibration does not by itself remove symmetry/superselection restrictions. Resource theories of asymmetry and symmetric-operation frameworks already study operational restrictions imposed by symmetry; thermodynamic resource theories likewise distinguish energetic resources from other restrictions. Consequently the generic symmetry obstruction is **IMPORTED/KNOWN in spirit**, not a PDT-native breakthrough.

The PDT-specific value of this cycle is negative: it closes another proposed escape from the quotient-selection/revelation no-go chain. PDT must derive a mechanism by which a declared physical resource breaks, bypasses, or otherwise resolves the relevant operational symmetry. Merely naming the resource energy, time, work, precision, or capacity is insufficient.

## Stress-test plan and exact dimensional coverage
`cycle214_calibrated_energy_revelation_no_go.py` checks n=1..12. n=1 and n=2 are recorded as edge/degenerate relative to the three-state dynamical witness. For n=3..12 it verifies the protected pair remains equivalent at every tested budget while the dynamics separates it; for n>=4 it also verifies strict enlargement of the observation signatures as additional unprotected-state indicators become affordable. The construction analytically extends to every finite n>=3.

## Classification
- **PROVED:** Theorem 214.1 under stated hypotheses.
- **FALSIFIED:** calibration + nested resource growth alone implies eventual revelation.
- **CONDITIONAL:** finite-threshold revelation given an independently justified pairwise separation axiom.
- **IMPORTED/KNOWN:** symmetry-restricted accessibility / superselection-style obstruction.
- **NUMERICALLY SUPPORTED:** exact finite witness checks n=3..12 supplement the proof.
- **OPEN:** PDT-native physical law deriving the separation thresholds without encoding the desired distinctions; PDT-native composition; non-circular n=3; same-input PDT-vs-QM prediction; distinctive experimental inequality; gravity/capacity law.
- **BREAKTHROUGH CANDIDATE:** NO.

## Consequence for PDT-II
A calibrated resource axis is necessary for quantitative experimental meaning but not sufficient for revelation. Any defensible PDT prediction must specify both (i) the physical cost calibration and (ii) the resource-dependent admissible operation/observation algebra, including how otherwise protected distinctions become accessible. Without (ii), no n=3 selection or same-input deviation from QM follows.
