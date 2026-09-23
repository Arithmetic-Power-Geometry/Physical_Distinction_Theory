# PDT-II Cycle 352 — Purity-preservation no-go

## Target attacked
1. PDT-native composition law.
2. Non-circular PDT-native `n=3` derivation.
3. Same-input PDT/QM deviation.

## Candidate principle
**Pure-product preservation (PPP).** If `a` and `b` are pure states of two systems, their independently prepared composite `a ⊗ b` is pure.

This is a genuinely compositional-looking requirement, so it is stronger than a merely local scalar condition. The question is whether PPP can select a unique PDT composition or dimension `n=3`.

## Exact hypotheses
- finite-dimensional normalized state spaces;
- a specified independent-preparation map `(a,b) -> a ⊗ b`;
- purity means extremality of the normalized state space;
- PPP requires products of pure local states to be pure joint states.

## Counterexample families
### Classical family
For every finite `n,m >= 1`, normalized states are simplices `Δ_n, Δ_m`. Pure states are vertices `e_i,e_j`. Under the standard independent product, `e_i ⊗ e_j = e_(i,j)`, a vertex of `Δ_(nm)`, hence pure.

### Complex-quantum family
For every finite `n,m >= 1`, pure states are rank-one projectors. If `ρ=|ψ><ψ|` and `σ=|φ><φ|`, then `ρ⊗σ=|ψ⊗φ><ψ⊗φ|` has rank one and is pure.

The classical and complex-quantum families are inequivalent operational theories but both satisfy PPP in every finite dimension. Therefore PPP cannot uniquely determine composition and cannot select `n=3`.

## Smallest decisive witness
At `n=2`, both a classical bit and a qubit satisfy PPP. Thus `PPP => n=3` is false before any high-dimensional issue arises.

## Dimension stress
The accompanying exact audit covers `n=1..12`. The analytic constructions above extend to all finite `n`; there is no `n=3` singularity.

## Same-input prediction consequence
PPP is already obeyed by ordinary complex QM. Therefore PPP alone cannot entail a same-input quantitative prediction `P_PDT(O|I,R) != P_QM(O|I,R)`. Any such deviation needs an additional PDT-native rule that changes admissible joint states, effects, transformations, or probabilities while holding microscopic input and resource window fixed.

## Prior-art boundary
Purity-preservation/pure-product assumptions occur in operational/GPT reconstruction work and ordinary classical/quantum composition. They are not by themselves a PDT-native novelty. Reconstruction programs require additional axioms to obtain quantum theory; purity constraints alone do not select spatial/Hilbert dimension three.

## Surviving theorem
**PPP non-selection theorem.** Over any model class containing finite classical probability theory and finite-dimensional complex quantum theory with their standard independent composition, pure-product preservation neither uniquely determines the composite theory nor selects `n=3`.

Proof: both inequivalent all-dimension families satisfy PPP; `n=2` is already a counterexample to dimension selection. QED.

## Status
- PPP in finite classical theory: **PROVED**.
- PPP in finite complex QM: **PROVED / IMPORTED-KNOWN**.
- `PPP => n=3`: **FALSIFIED**.
- `PPP => unique PDT composition`: **FALSIFIED**.
- `PPP => same-input PDT/QM deviation`: **FALSIFIED as an inference**.
- PDT-native intrinsically joint selector: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

No gravity/capacity law is promoted: this cycle supplies no derivation connecting PPP to gravity.