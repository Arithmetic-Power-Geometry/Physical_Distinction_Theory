# Akhtar Equation Heavy Attack — 2026-09-07

## Status

This document records a **candidate new PDT dynamical law**. It is not claimed here to be experimentally established, unique in all possible theories, or already peer-validated. The purpose is to identify the strongest mathematically defensible PDT-native evolution equation that (i) reduces exactly to ordinary quantum dynamics when there is no resource deficit, (ii) remains completely positive and trace preserving under finite deficit, (iii) makes the resource-bounded distinction structure operational rather than merely kinematic, and (iv) yields a quantitative falsifiable relation between distinction deficit and coherence loss.

The bare conditional-expectation semigroup used below is known in quantum Markov-semigroup theory. The **candidate novelty is the PDT selection rule for the projection, the capacity-deficit hazard law, and their combination into one resource-selected dynamical equation**.

---

# 1. Physical target

PDT already contains resource-bounded distinctions

\[
\Delta_R(\rho,\sigma)
=\sup_{a\in\mathcal A_R}|u_R(a,\rho)-u_R(a,\sigma)|,
\]

and a resource-bounded distinction capacity \(\mathscr K_\epsilon\). What was missing was a law saying **how a state evolves when the distinctions required by the dynamics exceed those physically maintainable under the available resource window**.

The target law must satisfy:

1. **Zero-deficit quantum limit:** no resource deficit implies ordinary von Neumann/Schroedinger evolution.
2. **CPTP consistency:** finite-deficit evolution must preserve positivity and unit trace.
3. **No arbitrary basis:** the erased/coarse-grained sector must be selected operationally from PDT's accessible distinction structure, not inserted by hand.
4. **Independent-deficit composition:** independent missing distinction bits should compose multiplicatively at the retention-probability level.
5. **Falsifiability:** the theory must predict a measurable rate as a function of an independently measurable distinction deficit.

---

# 2. Resource-optimal distinction projection

Let \(R=(E,\tau,\mathcal A,\mathcal R,\epsilon)\) denote the physical resource window.

Let \(\mathfrak C_R\) be the set of CPTP idempotent maps \(\mathcal P\) satisfying the admissible output-capacity constraint for the window \(R\):

\[
\mathcal P^2=\mathcal P,
\qquad
\mathcal P\ \text{CPTP},
\qquad
\mathscr K_\epsilon(\operatorname{Im}\mathcal P;R)\le K_R.
\]

Define the worst-case loss of resource-accessible distinction produced by \(\mathcal P\):

\[
\mathcal L_R(\mathcal P)
:=
\sup_{\rho,\sigma}
\Big[
\Delta_R(\rho,\sigma)
-
\Delta_R(\mathcal P\rho,\mathcal P\sigma)
\Big].
\]

The **resource-optimal distinction projection** is

\[
\boxed{
\mathcal P_R
\in
\operatorname*{arg\,min}_{\mathcal P\in\mathfrak C_R}
\mathcal L_R(\mathcal P).
}
\]

Interpretation: \(\mathcal P_R\) is the admissible idempotent physical reduction that throws away as little *operationally usable distinction* as possible under the actual resource limit.

If the available resource is sufficient to retain the full state space, the identity channel is feasible and has zero loss, so one may choose

\[
\boxed{\mathcal P_R=I\quad\text{when there is no capacity deficit}.}
\]

This makes the coarse-graining basis/resource sector a derived optimization object rather than a manually selected pointer basis.

---

# 3. Distinction-capacity deficit

Define an operational demand capacity \(K_{\rm req}(t)\) for the set of dynamically relevant alternatives during the window, and available capacity \(K_R(t)\). Define

\[
\boxed{
\chi_R(t)
:=
\big[K_{\rm req}(t)-K_R(t)\big]_+.
}
\]

\(\chi_R\) is measured in bits. It is zero when all currently required distinctions are physically maintainable and positive when the dynamics requires more distinction capacity than the physical resource window can support.

---

# 4. Deficit-retention theorem

Let \(s(\chi)\in(0,1]\) be the fraction of distinction retained across one resource-refresh window when the deficit is \(\chi\) bits.

Assume only:

- \(s(0)=1\);
- independent deficits compose additively in bits and multiplicatively in retention:
  \[
  s(\chi_1+\chi_2)=s(\chi_1)s(\chi_2);
  \]
- \(s\) is continuous;
- one completely unresolved binary distinction has retention calibration
  \[
  s(1)=\tfrac12.
  \]

Then the continuous multiplicative Cauchy equation gives

\[
\ln s(\chi)=c\chi.
\]

The one-bit calibration yields \(e^c=1/2\), hence \(c=-\ln2\). Therefore

\[
\boxed{
 s(\chi)=2^{-\chi}.
}
\]

Thus the fraction requiring resource-induced projection within one refresh window is

\[
\boxed{
 q(\chi)=1-2^{-\chi}.
}
\]

This is not an arbitrary exponential ansatz: it is uniquely fixed by continuity, independent-deficit composition, and the one-bit calibration.

For refresh time \(\tau_R\), define the minimal PDT deficit rate

\[
\boxed{
\gamma_R(t)
=
\frac{1-2^{-\chi_R(t)}}{\tau_R(t)}.
}
\]

Properties:

\[
\gamma_R=0\quad\text{iff}\quad\chi_R=0,
\]

and

\[
0\le \gamma_R < \frac1{\tau_R}.
\]

---

# 5. The Akhtar Resource-Distinction Equation

The proposed **Akhtar Equation** (more precisely, the Akhtar Resource-Distinction Equation, ARDE) is

\[
\boxed{
\frac{d\rho}{dt}
=
-\frac{i}{\hbar}[H,\rho]
+
\frac{1-2^{-\chi_R(t)}}{\tau_R(t)}
\big(\mathcal P_R[\rho]-\rho\big).
}
\tag{AE}
\]

Equivalently,

\[
\boxed{
\dot\rho
=
\mathcal L_H(\rho)
+\gamma_R(\mathcal P_R-I)(\rho),
\qquad
\mathcal L_H(\rho)=-\frac{i}{\hbar}[H,\rho].
}
\]

Physical reading:

- the commutator term transports distinctions reversibly;
- the second term removes only the component that cannot be maintained by the resource-optimal distinction-preserving reduction;
- the strength of that reduction is not a free decoherence constant but is tied to the measurable deficit \(\chi_R\) and refresh time \(\tau_R\).

---

# 6. Theorem: exact quantum limit

If \(\chi_R(t)=0\), then

\[
\gamma_R(t)=0.
\]

Therefore (AE) reduces exactly to

\[
\boxed{
\dot\rho=-\frac{i}{\hbar}[H,\rho].
}
\]

For a pure state this is equivalent to the Schroedinger equation up to the usual global phase freedom:

\[
\boxed{
 i\hbar\frac{d}{dt}|\psi\rangle=H|\psi\rangle.
}
\]

Thus standard isolated quantum mechanics is the zero-distinction-deficit sector of the candidate equation.

---

# 7. Theorem: the resource term generates a CPTP semigroup

Assume \(\mathcal P_R\) is CPTP and idempotent.

Consider the pure resource generator

\[
\mathcal G_R=\gamma_R(\mathcal P_R-I).
\]

Because \(\mathcal P_R^2=\mathcal P_R\),

\[
 e^{t\mathcal G_R}
 =e^{-\gamma_R t}I
 +(1-e^{-\gamma_R t})\mathcal P_R.
\]

Proof: decompose operator space into the fixed-point image of \(\mathcal P_R\) and the kernel of \(\mathcal P_R\). The generator eigenvalue is \(0\) on the image and \(-\gamma_R\) on the complementary sector.

Since \(I\) and \(\mathcal P_R\) are CPTP and the coefficients form a convex pair, \(e^{t\mathcal G_R}\) is CPTP for every \(t\ge0\).

Hence \(\mathcal G_R\) is a legitimate finite-dimensional quantum Markov generator. Adding the Hamiltonian derivation preserves GKLS admissibility.

Therefore, for piecewise-continuous externally determined \(R(t)\), (AE) gives a valid time-local CPTP evolution provided each instantaneous \(\mathcal P_R\) is a CPTP conditional expectation/projection.

---

# 8. Theorem: trace, Hermiticity and positivity

Because both the Hamiltonian term and \(\mathcal P_R-I\) are trace preserving,

\[
\frac{d}{dt}\operatorname{Tr}\rho=0.
\]

Hermiticity preservation follows from complete positivity/Hermiticity preservation of \(\mathcal P_R\) and the commutator structure. Positivity follows from the CPTP propagator established above.

Thus

\[
\boxed{
\rho(0)\ge0,\ \operatorname{Tr}\rho(0)=1
\Longrightarrow
\rho(t)\ge0,\ \operatorname{Tr}\rho(t)=1.
}
\]

---

# 9. Theorem: resource-stable distinctions are protected

If

\[
\mathcal P_R(\rho)=\rho,
\]

then the resource-induced term vanishes on that state:

\[
\gamma_R(\mathcal P_R\rho-\rho)=0.
\]

Therefore the finite-resource correction acts only on distinctions lying outside the resource-stable image of \(\mathcal P_R\).

This gives an operational version of pointer stability:

\[
\boxed{
\text{resource-maintainable sector}
=
\operatorname{Fix}(\mathcal P_R).
}
\]

But unlike a phenomenological preferred-basis choice, the sector is selected by minimization of PDT distinction loss.

---

# 10. Theorem: monotonic contraction of inaccessible distinction under the resource flow

For the pure resource semigroup

\[
T_t=e^{-\gamma t}I+(1-e^{-\gamma t})\mathcal P_R,
\]

we have

\[
T_{t+s}=T_tT_s.
\]

Since each \(T_t\) is CPTP and PDT's operational distinction measure is contractive under admissible processing,

\[
\boxed{
\Delta_R(T_{t+s}\rho,T_{t+s}\sigma)
\le
\Delta_R(T_t\rho,T_t\sigma).
}
\]

Thus distinction inaccessible to the resource-stable algebra cannot spontaneously reappear under the Markovian resource term.

---

# 11. Qubit worked limit and falsifiable rate relation

Take a qubit and let \(\mathcal P_R\) be dephasing onto the \(\sigma_z\) distinction algebra:

\[
\mathcal P_R
\begin{pmatrix}
\rho_{00}&\rho_{01}\\
\rho_{10}&\rho_{11}
\end{pmatrix}
=
\begin{pmatrix}
\rho_{00}&0\\
0&\rho_{11}
\end{pmatrix}.
\]

Assume \(H=(\hbar\omega/2)\sigma_z\) and constant resource window. Then (AE) yields

\[
\dot\rho_{01}
=-(i\omega+\gamma_R)\rho_{01}.
\]

Hence

\[
\boxed{
\rho_{01}(t)
=ho_{01}(0)e^{-i\omega t}
\exp\left[-\frac{1-2^{-\chi_R}}{\tau_R}t\right].
}
\]

The new candidate PDT relation is therefore

\[
\boxed{
\Gamma_{\rm dist}\,\tau_R
=1-2^{-\chi_R}.
}
\tag{AE-P1}
\]

Equivalently, if \(0\le\Gamma_{\rm dist}\tau_R<1\),

\[
\boxed{
\chi_R
=-\log_2(1-\Gamma_{\rm dist}\tau_R).
}
\tag{AE-P1-inverse}
\]

This is the first clean falsifiable target of the Akhtar Equation: independently estimate the distinction-capacity deficit \(\chi_R\) and refresh time \(\tau_R\), then test whether the residual resource-linked coherence-loss rate follows the predicted nonlinear law.

For small deficit,

\[
1-2^{-\chi}
=(\ln2)\chi-\frac{(\ln2)^2}{2}\chi^2+O(\chi^3),
\]

so

\[
\boxed{
\Gamma_{\rm dist}
=\frac{\ln2}{\tau_R}\chi_R
-\frac{(\ln2)^2}{2\tau_R}\chi_R^2
+O(\chi_R^3).
}
\]

The quadratic correction is fixed, not fitted independently.

---

# 12. Composition prediction

For independent deficits \(\chi_A,\chi_B\),

\[
s(\chi_A+\chi_B)=s(\chi_A)s(\chi_B).
\]

Therefore

\[
1-\Gamma_{AB}\tau
=
(1-\Gamma_A\tau)(1-\Gamma_B\tau)
\]

for equal refresh windows. Hence

\[
\boxed{
\Gamma_{AB}\tau
=
\Gamma_A\tau+
\Gamma_B\tau-
(\Gamma_A\tau)(\Gamma_B\tau).
}
\tag{AE-P2}
\]

This nonlinear composition law is another experimentally distinguishable consequence of the deficit-retention postulates.

---

# 13. What is mathematically old and what is candidate-new

## Known mathematical ingredients

The following must **not** be claimed as new:

- Hamiltonian von Neumann evolution;
- CPTP maps and GKLS/Lindblad generators;
- conditional expectations in operator algebras;
- the semigroup generated by \(\mathcal P-I\) for an idempotent CPTP projection;
- trace-distance/data-processing contraction under CPTP dynamics;
- resource theories and distinguishability monotones.

## Candidate PDT novelty

The potentially new object is the combined structure:

1. define the physically retained algebra by **resource-optimal minimization of PDT distinction loss**;
2. define the deficit in **bits of physically required versus available distinction capacity**;
3. derive the retention law \(2^{-\chi}\) from independent-deficit composition plus one-bit calibration;
4. use the resulting rate in the dynamical equation
   \[
   \dot\rho=-\frac{i}{\hbar}[H,\rho]+
   \frac{1-2^{-\chi_R}}{\tau_R}(\mathcal P_R\rho-\rho);
   \]
5. predict the parameter-free functional relation
   \[
   \Gamma\tau_R=1-2^{-\chi_R}
   \]
   once \(\chi_R\) and \(\tau_R\) are independently operationalized.

A literature search is required before asserting priority for this exact synthesis.

---

# 14. Kill tests

The Akhtar Equation should be rejected or weakened if any of the following occurs:

1. the optimization defining \(\mathcal P_R\) has no physically meaningful minimizer in relevant systems;
2. \(K_{\rm req}\) cannot be operationally measured independently of the observed decoherence rate;
3. the one-bit calibration \(s(1)=1/2\) lacks a defensible physical interpretation for the chosen distinction task;
4. experimental residual coherence loss does not obey \(\Gamma\tau_R=1-2^{-\chi_R}\) after known environmental channels are accounted for;
5. independent deficits violate the multiplicative retention law;
6. causal/locality constraints cannot be imposed on \(\mathcal P_R\) consistently in relativistic settings.

These are not weaknesses to hide; they make the proposal falsifiable.

---

# 15. Strongest present theorem statement

### Akhtar Resource-Distinction Evolution Theorem (conditional)

Let \(\rho\) be a finite-dimensional quantum state, let \(\mathcal P_R\) be a CPTP idempotent resource-optimal distinction projection, let \(\chi_R\ge0\) be a distinction-capacity deficit satisfying independent additive composition in bits, and let the one-bit retention calibration be \(1/2\). Then the minimal continuous multiplicative retention law is uniquely \(2^{-\chi_R}\), and the evolution

\[
\dot\rho
=-\frac{i}{\hbar}[H,\rho]
+
\frac{1-2^{-\chi_R}}{\tau_R}
(\mathcal P_R\rho-\rho)
\]

is trace preserving, Hermiticity preserving and completely positive for fixed/piecewise regular resource windows; it reduces exactly to unitary quantum dynamics at zero deficit, leaves the resource-stable image of \(\mathcal P_R\) invariant under the correction term, and predicts the resource-linked coherence-decay relation

\[
\Gamma_{\rm dist}\tau_R=1-2^{-\chi_R}.
\]

The theorem proves consistency of the proposed dynamics. It does **not** prove that Nature obeys it.

---

# 16. Next research steps

1. Prove existence/uniqueness conditions for the optimizer \(\mathcal P_R\).
2. Replace the abstract output-capacity constraint by an explicit computable finite-resource SDP for finite-dimensional systems.
3. Derive \(K_{\rm req}(t)\) from dynamically reachable alternative codebooks rather than defining it externally.
4. Test AE-P1 and AE-P2 numerically on qubits/qutrits under controlled coarse-graining.
5. Compare against ordinary dephasing, Davies, collision, repeated-measurement and information-bottleneck models.
6. Search the literature for the exact combination of resource-optimal distinction projection + deficit law \(1-2^{-\chi}\).
7. Only after those checks decide whether the eponym **Akhtar Equation** is scientifically justified in the manuscript.
