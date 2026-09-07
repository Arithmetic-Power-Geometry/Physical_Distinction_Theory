# Same-input PDT identifiability protocol

A PDT-specific controlled-record experiment must not compare only against fitted phenomenological models. Standard microscopic quantum mechanics must receive the same environmental information available to PDT.

## Baseline ladder

- `M0`: Schrödinger / no-decay null model.
- `M1`: fitted GKLS / Markovian open-system baseline.
- `M2`: fitted non-Markovian baseline.
- `M3`: standard microscopic quantum mechanics supplied with the measured environment state and controlled interaction information.
- `M4`: PDT / ADDE supplied with independently measured distinction-record information.

## Blind protocol

1. Prepare the controlled interaction.
2. Characterize the environment independently of the target coherence curve.
3. Reconstruct `D_E`, `kappa`, `chi`, or the complementary-channel statistic needed by the declared PDT sector.
4. Fix event statistics independently.
5. Freeze and hash the PDT prediction before revealing target-system coherence.
6. Independently construct `M3` from exactly the same available environmental inputs.
7. Reveal target-system data and compute predeclared error, calibration, uncertainty coverage and complexity metrics.
8. Claim PDT-specific predictive content only if the PDT result is not already fixed by `M3`, or if PDT establishes a strictly coarser sufficient operational statistic with a predictive guarantee unavailable to the same-input standard model.

For controlled dephasing with the same `eta_E`, `U0`, and `U1`, both descriptions give

`c(t)=c(0) chi(t)`.

Therefore success of a blind environment-to-coherence prediction is scientifically valuable but is not by itself evidence that microscopic quantum mechanics fails.
