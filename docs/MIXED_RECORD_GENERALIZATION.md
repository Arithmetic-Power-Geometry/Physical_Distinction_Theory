# Mixed-Record Distinction Generalization

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License, Version 2.0.

## Purpose

The pure conditional-record identity

\[
C=|\kappa|=\sqrt{1-D_E^2}
\]

is exact only when the two conditional environment records are pure. Real environments can be mixed. The correct general object is therefore the full conditional environment pair

\[
(\rho_E^{(0)},\rho_E^{(1)}),
\]

not a single distinguishability scalar.

## Mixed-record coherence functional

For controlled dephasing with an initially mixed environment state \(\eta_E\),

\[
U=|0\rangle\langle0|\otimes U_0+|1\rangle\langle1|\otimes U_1,
\]

the system off-diagonal element transforms exactly as

\[
c'=c\,\chi,
\qquad
\chi:=\operatorname{Tr}(U_0\eta_E U_1^\dagger).
\]

Hence the exact coherence-retention factor is

\[
\boxed{C_R:=\frac{|c'|}{|c|}=|\chi|.}
\]

Define the mixed-record coherence distinction

\[
\boxed{B_C^{\rm mix}:=-\log_2|\chi|.}
\]

Then

\[
\boxed{C_R=2^{-B_C^{\rm mix}}.}
\]

This is an exact controlled-dephasing identity. It does not require the conditional environment records to be pure.

## Conditional environment states

The two conditional records are

\[
\rho_E^{(0)}=U_0\eta_EU_0^\dagger,
\qquad
\rho_E^{(1)}=U_1\eta_EU_1^\dagger.
\]

Their trace distinguishability is

\[
D_E=\tfrac12\|\rho_E^{(0)}-\rho_E^{(1)}\|_1.
\]

For mixed records, \(D_E\) alone does not generally determine \(|\chi|\). Therefore the pure-record equality \(C=\sqrt{1-D_E^2}\) must not be applied universally.

## Fidelity envelope

Use the root fidelity

\[
f_E:=\|\sqrt{\rho_E^{(0)}}\sqrt{\rho_E^{(1)}}\|_1.
\]

Standard fidelity/trace-distance inequalities give

\[
1-f_E\le D_E\le\sqrt{1-f_E^2}.
\]

The controlled-unitary overlap obeys

\[
|\chi|\le f_E,
\]

because \(\chi\) is the overlap of a particular pair of purifications whereas fidelity is the maximum purification overlap. Therefore

\[
\boxed{C_R\le f_E\le\sqrt{1-D_E^2}.}
\]

The familiar pure-record equality is recovered when the conditional records are pure and the relevant purification overlap saturates the fidelity.

This explains the real photonic stress test: a mixed detector can legitimately lie below the pure-record curve. A discrepancy from \(\sqrt{1-D_E^2}\) is not by itself a falsification unless the purity/saturation assumptions are independently verified.

## General mixed-record experimental observable

A decisive mixed-record test should reconstruct or otherwise independently determine enough of

\[
\rho_E^{(0)},\rho_E^{(1)},U_0,U_1,\eta_E
\]

to determine \(\chi\) without using the target system-coherence curve. The blind prediction is then

\[
\boxed{C_{\rm pred}(t)=|\chi(t)|.}
\]

For independent record-forming events,

\[
\chi_{\rm tot}=\prod_j\chi_j,
\qquad
B_{C,\rm tot}^{\rm mix}=\sum_jB_{C,j}^{\rm mix}.
\]

For identical deterministic events at rate \(\nu\),

\[
\boxed{\Gamma_A=-\nu\ln|\chi|.}
\]

and the Akhtar Distinction Dynamics Equation is

\[
\boxed{
\dot\rho=-\frac{i}{\hbar}[H,\rho]+\Gamma_A(t)(\mathcal E_R-I)[\rho].
}
\]

For non-identical/time-dependent records,

\[
\boxed{\Gamma_A(t)=-\frac{d}{dt}\ln|\chi_{\rm tot}(t)|.}
\]

## General-channel boundary

For an arbitrary CPTP channel, a single \(\chi\), \(D_E\), or fidelity scalar is insufficient. The environment record is the complementary-channel pair

\[
\boxed{(\Phi^c(\rho),\Phi^c(\sigma)).}
\]

The Stinespring dilation preserves global trace distinction,

\[
D_1(V\rho V^\dagger,V\sigma V^\dagger)=D_1(\rho,\sigma),
\]

while both reduced channels satisfy data processing. Thus PDT should use a tensor/operator-valued dynamical distinction geometry for arbitrary channels; the scalar ADDE is the controlled-dephasing sector.

## Falsification protocol

A strong experiment must:

1. prepare a controlled-dephasing interaction with independently characterized \(\eta_E,U_0,U_1\);
2. determine \(\chi(t)\), or a complete conditional-record reconstruction sufficient to calculate it, without using system coherence;
3. freeze \(C_{\rm pred}(t)=|\chi(t)|\) and \(\Gamma_A(t)=-d\ln|\chi|/dt\);
4. reveal the system coherence only after prediction is frozen;
5. compare blind PDT/ADDE prediction with fitted GKLS and established non-Markovian baselines;
6. report uncertainty propagation, held-out error and parameter counts.

Failure of the exact identity inside its controlled-dephasing applicability domain would falsify this microscopic PDT record law. Outside that domain, the general complementary-channel formulation must be used.

## Novelty boundary

Mixed-state fidelity, trace-distance inequalities, Stinespring dilation, complementary channels and which-way duality are established quantum-information results. The candidate PDT contribution is their organization into a resource-resolved distinction architecture, the explicit separation of physical record creation from resource accessibility, and the use of independently reconstructed environmental records to determine the ADDE rate rather than fitting it from the target coherence trace.
