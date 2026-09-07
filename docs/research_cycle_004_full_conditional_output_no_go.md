# Research cycle 004 — full conditional-output identifiability no-go

## Result

**Status: PROVED / NO-GO.**

In a controlled-dephasing model let

- `eta = I_d/d`,
- `U0 = I_d`,
- `U1 = V` for any unitary `V`.

Then

`rho_E^(0) = rho_E^(1) = I_d/d`

for every `V`, but

`chi = Tr(V^dagger)/d`.

Hence the complete conditional-output pair `(rho_E^(0), rho_E^(1))` does not identify the system coherence factor `chi`.

For every `d>=2`, choose model A with `V=I_d` and model B with diagonal entries equal to the `d`-th roots of unity. Both models have exactly the same conditional environment states, while `|chi_A|=1` and `|chi_B|=0`.

This strictly strengthens the earlier scalar statement that trace distinguishability `D_E` alone is insufficient: **no statistic computed solely from the two conditional density operators can resolve this witness pair.** Extra process-level/interferometric information is required.

## Computational audit

`tests/test_conditional_output_no_go.py` checks dimensions 2 through 8 and verifies:

1. conditional-output pair residual `<1e-12`;
2. model A has `|chi|=1`;
3. root-of-unity model B has `|chi|<1e-12`;
4. a continuous qubit phase family keeps the conditional outputs fixed while `|chi|` varies continuously from 1 to 0 over `alpha in [0,pi]`.

The Streamlit page `pages/3_Full_Conditional_Output_No_Go.py` exposes the witness interactively.

## Prior-art boundary checked in this cycle

This result is **not promoted as a breakthrough or as new quantum mechanics**. Closely related literature already establishes important mixed-state interferometric and which-way limitations:

- B.-G. Englert, *Fringe Visibility and Which-Way Information: An Inequality*, Phys. Rev. Lett. 77, 2154 (1996), DOI: 10.1103/PhysRevLett.77.2154.
- J. Martinez-Linares and D. A. Harmin, *Quality of a which-way detector*, Phys. Rev. A 69, 062109 (2004), DOI: 10.1103/PhysRevA.69.062109.
- D. K. L. Oi and J. Aberg, *Fidelity and Coherence Measures from Interference*, Phys. Rev. Lett. 97, 220404 (2006), DOI: 10.1103/PhysRevLett.97.220404.
- C. L. Hasse, *Limits on the observable dynamics of mixed states*, Phys. Rev. A 85, 062124 (2012), DOI: 10.1103/PhysRevA.85.062124.
- K. Roszak, *Measure of qubit-environment entanglement for pure dephasing evolutions*, Phys. Rev. Research 2, 043062 (2020), DOI: 10.1103/PhysRevResearch.2.043062.

The defensible PDT contribution of this cycle is therefore the **explicit identifiability boundary and root-of-unity witness family inside PDT's same-input audit architecture**, not a claim that mixed-state visibility limitations were previously unknown.

## Breakthrough implication

A future PDT law that predicts controlled-dephasing coherence from an operational environmental statistic must use information richer than the unordered/ordered pair of conditional output density matrices alone, or it will fail on this family. Candidate statistics should therefore be process-sensitive or interferometric and must be compared against known quantum process information before any novelty claim.
