# Breakthrough Lab Cycle 002 — Conditional-output identifiability audit

## Result

**Classification: PROVED / NO-GO.** This is a rigorous design constraint for PDT record-based prediction. It is **not** being claimed as a new-physics breakthrough.

For controlled dephasing,

\[
\rho_E^{(0)}=U_0\eta U_0^\dagger,\qquad
\rho_E^{(1)}=U_1\eta U_1^\dagger,\qquad
\chi=\operatorname{Tr}(U_0\eta U_1^\dagger).
\]

Complete knowledge of the conditional environment-state pair does **not** identify the coherence multiplier \(\chi\) in general.

### Exact witness

Let \(\eta=I_d/d\) and \(U_0=I_d\). For any unitary \(V\), choose \(U_1=V\). Then

\[
\rho_E^{(0)}=\rho_E^{(1)}=I_d/d,
\]

but

\[
\chi=\frac{1}{d}\operatorname{Tr}(V^\dagger).
\]

Model A uses \(V=I_d\), giving \(|\chi|=1\). Model B uses the diagonal unitary whose entries are the \(d\)-th roots of unity, giving \(\operatorname{Tr}V=0\) and hence \(|\chi|=0\). The conditional density operators are identical in both models.

Therefore there is no universal function

\[
F(\rho_E^{(0)},\rho_E^{(1)})=\chi
\]

valid for all mixed-environment controlled-dephasing realizations. The same obstruction applies to any statistic determined solely by the conditional pair, including trace distance and fidelity.

## Numerical stress audit

The exact construction was evaluated for environment dimensions \(d=2,\dots,8\). Conditional-output residuals were zero to approximately machine precision (largest observed residual below \(1.3\times10^{-16}\)); Model A retained \(|\chi|\approx1\), while Model B gave \(|\chi|\lesssim1.3\times10^{-16}\).

This numerical audit checks implementation of the constructive proof; it is not the proof itself.

## Consequence for PDT

A predictive PDT law that attempts to infer open-system coherence decay only from the two conditional environment density operators is underdetermined in the unrestricted mixed-environment setting. To obtain a valid same-input prediction, PDT must do at least one of the following:

1. include additional operational information sensitive to the **relative unitary/dilation structure** between the conditional branches;
2. impose a physically justified restricted model class in which that missing structure is fixed or recoverable; or
3. identify a different operational statistic proven sufficient for the target observable.

This sharpens the existing same-input criterion: not only is a scalar distinguishability such as \(D_E\) insufficient in general, even complete tomography of the conditional pair can be insufficient.

## Prior-art boundary checked in this cycle

A targeted literature search found substantial pre-existing work on mixed-state pure-dephasing environments, environment-conditioned states, wave-particle distinguishability/coherence tradeoffs, and resource-theoretic discrimination. In particular, Roszak (2019/2020-era arXiv:1912.07317) explicitly emphasizes that pure-state intuitions about decoherence do not transfer directly to mixed environments. Takagi & Regula (2019, arXiv:1901.08127) and Wang & Wilde (2019, arXiv:1905.11629) already establish broad resource-theoretic links between distinguishability and operational tasks.

**Novelty decision for this cycle:** the exact conditional-pair non-identifiability formulation remains a candidate useful PDT-specific theorem statement, but current search is insufficient to claim that the mathematical fact itself is historically new. It therefore remains labeled **PROVED / NO-GO; NOVELTY UNRESOLVED**.

## Dimension-selection route

The concurrent dimension audit remains negative for a breakthrough: CEU+CER+RDE are satisfied by all Euclidean balls \(B^n\), while resolution-dependent codebook growth recovers an already-existing metric dimension through standard packing/covering asymptotics. This identifies \(n\) operationally when the geometry is given but does not select \(n=3\).

## Next strongest target

Search for an operational observable that captures the missing **relative branch information** without requiring full microscopic unitaries. A genuine advance would be a theorem of the form

\[
S_R(\text{operationally measurable data})\Longrightarrow \chi
\]

for a nontrivial physical model class, together with an experimentally implementable protocol and a proof that the statistic is strictly coarser than the complete microscopic input while remaining sufficient for the prediction.
