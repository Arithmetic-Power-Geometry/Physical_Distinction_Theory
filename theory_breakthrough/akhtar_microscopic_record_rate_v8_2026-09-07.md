# Akhtar Microscopic Record-Rate v8 — Deriving Coherence Decay from Environment-Record Distinguishability

## Status

This attack targets the strongest unresolved dynamical gap left after v7: the coefficient in the Akhtar coherence-loss law.

The previous phenomenological rule

\[
\Gamma_A=\ln 2\,\Phi_H
\]

cannot be derived from free-energy monotonicity alone. This file therefore derives an exact microscopic decay law in a controlled dephasing/repeated-interaction model and identifies the physically measurable quantity that actually fixes the rate.

The main correction is important:

> generic Shannon/distinction-entropy loss is not automatically the same quantity as logarithmic coherence attenuation.

The exact microscopic quantity is the logarithmic overlap of the conditional environment records. For pure conditional records this overlap is algebraically tied to optimal record distinguishability, producing an exact parameter-free rate once the interaction rate and per-interaction record distinguishability are independently measured.

The controlled-unitary dephasing formula, visibility-distinguishability duality, collision models, and Chernoff/record distinguishability are established prior art. The candidate PDT contribution is the integration of these results with the resource-bounded distinction architecture and the explicit correction of the earlier one-bit calibration.

---

# 1. Microscopic system-environment model

Consider an elementary binary distinction with preferred states \(|0\rangle,|1\rangle\). Let the environment start in a pure probe state \(|e\rangle\). A pure dephasing interaction has controlled-unitary form

\[
U
=
|0\rangle\langle0|\otimes U_0
+
|1\rangle\langle1|\otimes U_1.
\]

Define conditional environment records

\[
|e_0\rangle:=U_0|e\rangle,
\qquad
|e_1\rangle:=U_1|e\rangle.
\]

If initially

\[
\rho_S=
\begin{pmatrix}
 p & c\\
 c^* & 1-p
\end{pmatrix},
\]

then after the interaction and tracing out the environment,

\[
\rho_S'
=
\begin{pmatrix}
 p & c\,\kappa\\
 c^*\kappa^* & 1-p
\end{pmatrix},
\]

where

\[
\boxed{
\kappa:=\langle e_1|e_0\rangle.
}
\tag{M1}
\]

Hence

\[
\boxed{
\frac{|c'|}{|c|}=|\kappa|.
}
\tag{M2}
\]

This is an exact microscopic identity.

---

# 2. Microscopic distinction-record bit

Define the **coherence-record distinction bit** of one interaction by

\[
\boxed{
B_C:=-\log_2|\kappa|.
}
\tag{B1}
\]

Then the exact one-interaction coherence law is

\[
\boxed{
\frac{|c'|}{|c|}=2^{-B_C}.
}
\tag{B2}
\]

This removes the arbitrary normalization that previously imposed “one lost distinction bit halves coherence.” Here the base-2 law is an identity following from the operational definition of \(B_C\).

Important: \(B_C\) is not claimed to equal generic Shannon entropy loss, generic capacity loss, or generic thermodynamic entropy production.

---

# 3. Exact relation to environment-record distinguishability

For two pure conditional environment states with equal priors, the optimal Helstrom trace-distance distinguishability is

\[
\boxed{
D_E
=
\frac12\left\|
|e_0\rangle\langle e_0|
-
|e_1\rangle\langle e_1|
\right\|_1
=
\sqrt{1-|\kappa|^2}.
}
\tag{D1}
\]

Therefore

\[
|\kappa|=\sqrt{1-D_E^2},
\]

and

\[
\boxed{
B_C
=-\frac12\log_2(1-D_E^2).
}
\tag{D2}
\]

Thus the coherence attenuation is predicted directly from an independently measurable environment-record discrimination task:

\[
\boxed{
\frac{|c'|}{|c|}
=
\sqrt{1-D_E^2}.
}
\tag{D3}
\]

This is the pure-record saturation of the established visibility-distinguishability duality relation.

---

# 4. Weak-record limit

When \(D_E\ll1\),

\[
-\ln\sqrt{1-D_E^2}
=
\frac{D_E^2}{2}+O(D_E^4).
\]

Therefore

\[
\boxed{
B_C
=
\frac{D_E^2}{2\ln2}
+O(D_E^4).
}
\tag{W1}
\]

A weak environment record causes a second-order coherence loss in the record distinguishability.

This gives a concrete perturbative scaling rather than an arbitrary linear bit-loss postulate.

---

# 5. Independent repeated interactions

Now let the system collide sequentially with independent fresh environment probes. Let the \(j\)-th collision produce overlap

\[
\kappa_j=\langle e_1^{(j)}|e_0^{(j)}\rangle.
\]

Because the conditional global environment states tensor-factorize,

\[
|E_s^{(N)}\rangle
=
\bigotimes_{j=1}^N|e_s^{(j)}\rangle,
\qquad s\in\{0,1\},
\]

the global overlap is

\[
\langle E_1^{(N)}|E_0^{(N)}\rangle
=
\prod_{j=1}^N\kappa_j.
\]

Hence

\[
\boxed{
\frac{|c_N|}{|c_0|}
=
\prod_{j=1}^N|\kappa_j|
=
2^{-\sum_{j=1}^N B_{C,j}}.
}
\tag{R1}
\]

Define cumulative microscopic record exposure

\[
\boxed{
\mathcal B_C(N):=\sum_{j=1}^N B_{C,j}.
}
\tag{R2}
\]

Then

\[
\boxed{
-\log_2\frac{|c_N|}{|c_0|}
=\mathcal B_C(N).
}
\tag{R3}
\]

This is exact for independent controlled-unitary record formation.

---

# 6. Continuous-time collision-rate theorem

Suppose collisions occur at deterministic rate \(\nu\) per unit time and each collision has identical overlap \(|\kappa|\). Then after time \(t\),

\[
N(t)=\nu t
\]

in the continuum idealization, and

\[
|c(t)|
=|c(0)|\,|\kappa|^{\nu t}.
\]

Therefore

\[
\boxed{
|c(t)|
=|c(0)|e^{-\Gamma_Ct}
}
\]

with the exact microscopic rate

\[
\boxed{
\Gamma_C
=-\nu\ln|\kappa|.
}
\tag{G1}
\]

Equivalently,

\[
\boxed{
\Gamma_C
=\nu\ln2\,B_C.
}
\tag{G2}
\]

For pure conditional records,

\[
\boxed{
\Gamma_C
=-\frac{\nu}{2}\ln(1-D_E^2).
}
\tag{G3}
\]

In the weak-record limit,

\[
\boxed{
\Gamma_C
=\frac{\nu D_E^2}{2}+O(D_E^4).
}
\tag{G4}
\]

Thus the decay rate is fully predicted by two independently measurable microscopic quantities:

1. collision/record-creation rate \(\nu\);
2. single-record distinguishability \(D_E\).

No decay constant is fitted from the system coherence curve.

---

# 7. Poisson collision theorem

If collisions occur as a Poisson process with mean rate \(\nu\), the number \(N_t\) of collisions in time \(t\) satisfies

\[
\mathbb E[z^{N_t}]=e^{\nu t(z-1)}.
\]

For identical real nonnegative overlap \(0\le\kappa\le1\), the ensemble-averaged coherence is

\[
\mathbb E[c(t)]
=c(0)\,\mathbb E[\kappa^{N_t}]
=c(0)e^{\nu t(\kappa-1)}.
\]

Hence

\[
\boxed{
\Gamma_{\rm Pois}=\nu(1-\kappa).
}
\tag{P1}
\]

This differs from the deterministic-collision logarithmic rate

\[
-\nu\ln\kappa.
\]

Therefore the macroscopic decay rate depends not only on per-collision distinction but also on the counting statistics of record-forming events.

This is a crucial correction to any universal rate law based only on a scalar distinction flux.

---

# 8. No-go theorem — generic distinction entropy does not fix coherence decay

Two environments may generate the same Shannon/Holevo entropy increase while having different conditional-state overlaps and therefore different coherence attenuation.

Conversely, two microscopic record processes may have the same \(|\kappa|\) but different thermodynamic entropy production.

Therefore

\[
\boxed{
\Phi_H\text{ alone}
\not\Rightarrow
\Gamma_C.
}
\tag{NG1}
\]

The previous identification

\[
\Gamma_A=\ln2\,\Phi_H
\]

is not a universal theorem when \(\Phi_H\) denotes generic distinction entropy flux.

It is exact only when the flux is specifically defined as the rate of logarithmic conditional-record overlap,

\[
\boxed{
\Phi_C:=\frac{d\mathcal B_C}{dt}
=-\frac{d}{dt}\log_2|\kappa_{\rm tot}(t)|.
}
\tag{Cflux}
\]

Then, by definition plus the microscopic overlap identity,

\[
\boxed{
\Gamma_C=\ln2\,\Phi_C.
}
\tag{Cexact}
\]

This is not a phenomenological calibration; it is an exact bookkeeping identity for controlled dephasing.

---

# 9. Distinction-information hierarchy

The attack now separates four distinct quantities:

\[
\boxed{
K_D\neq H_D\neq B_C\neq \Sigma_{\rm th}.
}
\]

where

- \(K_D\): maximum operational distinction capacity;
- \(H_D\): actual uncertainty/conditional distinction entropy;
- \(B_C\): logarithmic coherence-record overlap;
- \(\Sigma_{\rm th}\): thermodynamic entropy production.

They can coincide in special idealized limits, but no universal equality should be assumed.

This is a major structural correction to the earlier PDT bridge.

---

# 10. Mixed environment records

For a mixed initial environment state \(\rho_E\), define conditional states

\[
\rho_E^{(0)}=U_0\rho_EU_0^\dagger,
\qquad
\rho_E^{(1)}=U_1\rho_EU_1^\dagger.
\]

The system coherence factor is

\[
\boxed{
\kappa
=\operatorname{Tr}(U_0\rho_EU_1^\dagger).
}
\tag{MIX1}
\]

and still

\[
|c'|=|c|\,|\kappa|.
\]

The optimal record distinguishability is

\[
D_E=\frac12\|\rho_E^{(0)}-\rho_E^{(1)}\|_1.
\]

In general the pure-state equality

\[
D_E^2+|\kappa|^2=1
\]

need not hold; only a duality bound is generally available.

Therefore mixed/hazy environments break the one-parameter pure-record closure. Additional state information such as fidelity, Chernoff information, or the full conditional pair is required.

This matches the established quantum-Darwinism observation that mixed environments may decohere a system while having reduced capacity to store accessible records.

---

# 11. Resource-bounded record distinguishability

PDT adds a finite-resource restriction. Let \(\mathcal T_R^E\) be the environment tests physically accessible in resource window \(R\). Define the resource-bounded record distinguishability

\[
\boxed{
D_{E,R}
:=
\sup_{T\in\mathcal T_R^E}
\left|
\operatorname{Tr}[T(\rho_E^{(0)}-\rho_E^{(1)})]
\right|.
}
\tag{RD1}
\]

Then

\[
D_{E,R}\le D_E.
\]

For pure conditional records, if the resource set is rich enough to attain the Helstrom measurement,

\[
D_{E,R}=D_E
\]

and the exact rate formula (G3) is operationally accessible.

If not, \(D_{E,R}\) gives only a resource-limited lower estimate of actual record distinguishability and cannot by itself fix the microscopic coherence rate.

Hence PDT must distinguish:

\[
\boxed{
\text{record physically created}
\neq
\text{record accessible to a given observer/resource window}.
}
\]

---

# 12. Operational non-circular experiment

A decisive experiment can be organized as follows.

## A. Calibrate record events

Independently determine the interaction/collision rate \(\nu\) from apparatus timing or environmental flux.

## B. Prepare pointer alternatives

Prepare the system separately in \(|0\rangle\) and \(|1\rangle\), allow one interaction, and perform environment tomography or optimal binary discrimination on the resulting conditional environment states.

Estimate

\[
D_E
\]

without using a superposition-state coherence decay curve.

## C. Predict coherence decay

For pure records and deterministic collisions, compute

\[
\Gamma_{\rm pred}
=-\frac{\nu}{2}\ln(1-D_E^2).
\]

For Poisson collisions with real overlap,

\[
\Gamma_{\rm pred}
=\nu\left(1-\sqrt{1-D_E^2}\right).
\]

## D. Blind test

Only after fixing \(\Gamma_{\rm pred}\), prepare a superposition and measure the actual coherence decay.

No rate parameter is fitted.

---

# 13. Kill tests

The microscopic record-rate model is falsified in its stated regime if any of the following occurs:

1. independently reconstructed conditional environment states predict overlap \(\kappa\), but measured one-step system coherence does not satisfy
   \[
   c'/c=\kappa;
   \]
2. independent collisions are verified, but total coherence is not the product of per-collision overlaps;
3. deterministic collision data violate
   \[
   \Gamma=-\nu\ln|\kappa|;
   \]
4. pure conditional records violate
   \[
   D_E^2+|\kappa|^2=1;
   \]
5. a proposed PDT entropy flux \(\Phi_H\) is claimed to determine \(\Gamma\), but two processes with equal \(\Phi_H\) have different independently measured overlaps/rates.

---

# 14. Relation to the Akhtar Equation

The safest microscopic replacement for the scalar phenomenological Akhtar rate is

\[
\boxed{
\Gamma_A(t)
:=
-\frac{d}{dt}\ln|\kappa_{\rm tot}(t)|.
}
\tag{AE8-rate}
\]

Whenever the retained conditional expectation \(\mathcal E_R\) is independently selected by the v3 canonical distinction geometry and the microscopic environment coupling produces pure dephasing into the complementary sector, the reduced equation is

\[
\boxed{
\dot\rho
=
-\frac{i}{\hbar}[H,\rho]
+
\Gamma_A(t)
(\mathcal E_R-I)[\rho].
}
\tag{AE8}
\]

In a deterministic i.i.d. collision model,

\[
\boxed{
\Gamma_A
=-\nu\ln|\kappa|
=-\frac{\nu}{2}\ln(1-D_E^2)
}
\tag{AE8-micro}
\]

for pure conditional records.

Thus the equation now has an explicit microscopic closure in a nontrivial open-system class.

---

# 15. What is established prior art

The following ingredients are known and must be credited:

- controlled-unitary pure-dephasing coherence factors;
- environment conditional-state overlap as the decoherence/visibility factor;
- Englert-type distinguishability-visibility duality;
- collision/repeated-interaction models;
- product accumulation of independent environment overlaps;
- quantum Darwinism and environment-as-witness;
- Chernoff information for distinguishability of environment records.

Therefore none of those individual results is a PDT discovery.

---

# 16. Candidate PDT novelty

The defensible candidate contribution is the integrated theorem-development chain:

\[
\boxed{
\text{PDT resource-selected stable distinction sector}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{conditional environment records for that sector}
}
\]

\[
\Downarrow
\]

\[
\boxed{
B_C=-\log_2|\kappa|
}
\]

\[
\Downarrow
\]

\[
\boxed{
\Gamma_A=-\frac{d}{dt}\ln|\kappa_{\rm tot}|
}
\]

with a resource-bounded operational distinction layer and explicit separation of capacity, Shannon distinction entropy, record-overlap bits, and thermodynamic entropy production.

The strongest conceptual advance of v8 is therefore not a new decoherence formula. It is the removal of a false universality assumption and the replacement of the phenomenological one-bit attenuation rule by a microscopically measurable record-overlap law.

---

# 17. Updated proof status

| Claim | Status |
|---|---|
| One-step coherence equals conditional environment overlap | **Proved / standard controlled-unitary result** |
| Pure-record \(D_E^2+|\kappa|^2=1\) | **Proved / established duality** |
| Independent-record overlap multiplication | **Proved** |
| Deterministic collision rate \(\Gamma=-\nu\ln|\kappa|\) | **Proved** |
| Pure-record rate \(\Gamma=-\frac\nu2\ln(1-D_E^2)\) | **Proved** |
| Weak-record rate \(\Gamma\sim\nu D_E^2/2\) | **Proved** |
| Poisson-counting rate \(\Gamma=\nu(1-\kappa)\) for real \(\kappa\) | **Proved** |
| Generic Shannon distinction entropy fixes coherence rate | **False / no-go** |
| Generic thermodynamic entropy production fixes coherence rate | **False / no-go** |
| Resource-accessible record distinguishability equals physical record distinguishability | **Only if Helstrom-optimal test is resource accessible** |
| AE8 microscopic closure for controlled dephasing/collision model | **Proved conditionally** |
| AE8 universal for arbitrary open-system dynamics | **Not proved / false without further structure** |
| Full non-Markovian microscopic closure | **Open** |
| Gravity from the same record-overlap variable | **Open** |

---

# 18. Highest-value next theorem

The next attack should generalize the exact pure-record result beyond simple dephasing without restoring arbitrary parameters.

The strongest target is a **channel-level distinction action** built from the pair of conditional environment channels or complementary channels, for example through fidelity/Bures/Chernoff geometry, and prove a bound or equality of the form

\[
\boxed{
\text{system coherence/contraction rate}
\leftrightarrow
\text{environment record-generation rate}
}
\]

for general CPTP Markovian dynamics.

A particularly valuable route is:

1. Stinespring-dilate an arbitrary CPTP infinitesimal channel;
2. define the complementary-channel record distinguishability generated between selected PDT distinction alternatives;
3. derive the second-order short-time contraction from the environment-record metric;
4. identify when the resulting quadratic form equals a Fisher/Bures metric;
5. test whether the same quadratic object also reproduces the v3 resource-distinction tensor or yields a new consistency condition between static distinguishability geometry and dynamical record creation.

If successful, PDT would have a non-phenomenological route from operational distinction geometry to microscopic open-system dynamics beyond pure dephasing.