# Akhtar Operational Free Energy v7 — One-Shot Distinction Divergence, Thermodynamic Monotonicity, and the Asymptotic Quantum Limit

## Status

This attack closes the next thermodynamic bridge without confusing raw distinction capacity with entropy. It constructs two state-resolved PDT divergences directly from resource-limited physical discrimination, proves data processing from the existing PDT pullback principle, and uses them to define finite-resource free-energy monotones.

The key improvement over v6 is that the thermodynamic state function is now built directly from **physical hypothesis testing**, which is already native to PDT, rather than inserted as an abstract entropy formula.

The standard facts about relative entropy, hypothesis-testing relative entropy, thermal operations/Gibbs-preserving maps, and quantum Stein asymptotics are established prior art and must be credited. The candidate PDT contribution is the resource-window-resolved synthesis and the operational bridge to the distinction architecture.

---

# 1. Resource-restricted hypothesis testing

Let \(R=(E,\tau,\mathcal A,\mathcal R,\epsilon)\) be a PDT resource window. Let \(\mathcal T_R\) be the set of binary tests physically implementable under that resource window, with each test represented by an effect

\[
0\le T\le I.
\]

For states \(\rho\) and \(\sigma\), and type-I error tolerance \(0<\varepsilon<1\), define the resource-restricted type-II error

\[
\boxed{
\beta_{\varepsilon,R}(\rho\Vert\sigma)
:=
\inf_{T\in\mathcal T_R}
\left\{
\operatorname{Tr}(T\sigma):
\operatorname{Tr}(T\rho)\ge1-\varepsilon
\right\}.
}
\tag{HT1}
\]

Define the **PDT hypothesis-testing distinction divergence** in bits

\[
\boxed{
D_{H,R}^{\varepsilon}(\rho\Vert\sigma)
:=-\log_2\beta_{\varepsilon,R}(\rho\Vert\sigma).
}
\tag{HT2}
\]

This quantity answers a directly physical question:

> at fixed allowed false-rejection rate, how strongly can the resource-limited observer rule out \(\sigma\) when \(\rho\) is true?

It is therefore much closer to PDT's original physical-distinction primitive than a purely formal entropy.

---

# 2. Theorem — resource data processing for hypothesis-testing distinction

Let \(\Phi:R\to R'\) be an admissible physical process. Assume the existing PDT pullback condition:

for every post-process test \(T'\in\mathcal T_{R'}\), the pulled-back test \(\Phi^*(T')\) belongs to \(\mathcal T_R\).

Then

\[
\boxed{
D_{H,R'}^{\varepsilon}(\Phi\rho\Vert\Phi\sigma)
\le
D_{H,R}^{\varepsilon}(\rho\Vert\sigma).
}
\tag{HT-DPI}
\]

### Proof

Take any feasible post-process test \(T'\):

\[
\operatorname{Tr}(T'\Phi\rho)\ge1-\varepsilon.
\]

By duality,

\[
\operatorname{Tr}(T'\Phi\rho)
=
\operatorname{Tr}(\Phi^*T'\,\rho),
\]

and similarly for \(\sigma\). Pullback admissibility makes \(\Phi^*T'\) a feasible pre-process test with exactly the same type-II error. Hence the pre-process optimization is over a set containing every pulled-back post-process feasible test, so

\[
\beta_{\varepsilon,R}(\rho\Vert\sigma)
\le
\beta_{\varepsilon,R'}(\Phi\rho\Vert\Phi\sigma).
\]

Applying \(-\log_2\) gives the result.

This proof uses the same sup/inf-set logic as the earlier PDT operational distinction DPI.

---

# 3. Equality under physical recovery

Suppose there exists an admissible recovery map \(\Psi:R'\to R\) such that

\[
\Psi\Phi(\rho)=\rho,
\qquad
\Psi\Phi(\sigma)=\sigma.
\]

Applying the DPI to \(\Phi\) and then to \(\Psi\) yields

\[
D_{H,R}^{\varepsilon}(\rho\Vert\sigma)
\ge
D_{H,R'}^{\varepsilon}(\Phi\rho\Vert\Phi\sigma)
\ge
D_{H,R}^{\varepsilon}(\rho\Vert\sigma).
\]

Therefore

\[
\boxed{
D_{H,R'}^{\varepsilon}(\Phi\rho\Vert\Phi\sigma)
=
D_{H,R}^{\varepsilon}(\rho\Vert\sigma).
}
\tag{HT-rec}
\]

So exact physical recoverability is sufficient for equality of the PDT one-shot distinction divergence.

---

# 4. Resource monotonicity

If two resource windows obey

\[
\mathcal T_{R_1}\subseteq\mathcal T_{R_2},
\]

then

\[
\beta_{\varepsilon,R_2}(\rho\Vert\sigma)
\le
\beta_{\varepsilon,R_1}(\rho\Vert\sigma)
\]

and therefore

\[
\boxed{
D_{H,R_1}^{\varepsilon}(\rho\Vert\sigma)
\le
D_{H,R_2}^{\varepsilon}(\rho\Vert\sigma).
}
\tag{HT-resource}
\]

More physical discrimination access cannot reduce operational distinction power.

---

# 5. One-shot PDT thermal reference

For a system with Hamiltonian \(H\) and bath temperature \(T\), define the Gibbs state

\[
\gamma_{H,T}
=
\frac{e^{-\beta H}}{Z},
\qquad
\beta=\frac1{k_BT},
\qquad
Z=\operatorname{Tr}e^{-\beta H}.
\]

Define equilibrium free energy

\[
F_{\rm eq}(H,T)=-k_BT\ln Z.
\]

The thermal state now becomes the physically distinguished reference state.

---

# 6. Akhtar one-shot distinction free energy

Define

\[
\boxed{
\mathcal F_{H,R}^{\varepsilon}(\rho)
:=
F_{\rm eq}(H,T)
+
 k_BT\ln2\,
D_{H,R}^{\varepsilon}(\rho\Vert\gamma_{H,T}).
}
\tag{AOF1}
\]

This is the **Akhtar one-shot operational distinction free energy**.

It is not asserted to equal the standard Helmholtz nonequilibrium free energy for arbitrary finite resources. It quantifies the thermodynamic nonequilibrium that is operationally visible through the physically available one-shot distinction tests.

---

# 7. Theorem — one-shot free-energy monotonicity

Let \(\Phi\) be an admissible map from system \(A\) to system \(B\) satisfying

\[
\Phi(\gamma_A)=\gamma_B
\]

and the PDT test-pullback condition.

Then

\[
\boxed{
\mathcal F_{H,R'}^{\varepsilon}(\Phi\rho)
-F_{\rm eq,B}
\le
\mathcal F_{H,R}^{\varepsilon}(\rho)
-F_{\rm eq,A}.
}
\tag{AOF-DPI}
\]

If the Hamiltonian/reference system is unchanged, this becomes simply

\[
\boxed{
\mathcal F_{H,R'}^{\varepsilon}(\Phi\rho)
\le
\mathcal F_{H,R}^{\varepsilon}(\rho).
}
\]

### Proof

By Gibbs preservation,

\[
D_{H,R'}^{\varepsilon}(\Phi\rho\Vert\gamma_B)
=
D_{H,R'}^{\varepsilon}(\Phi\rho\Vert\Phi\gamma_A).
\]

The hypothesis-testing DPI gives

\[
D_{H,R'}^{\varepsilon}(\Phi\rho\Vert\Phi\gamma_A)
\le
D_{H,R}^{\varepsilon}(\rho\Vert\gamma_A).
\]

Multiplication by the positive constant \(k_BT\ln2\) gives the result.

Thus a finite-resource thermodynamic monotone follows directly from the PDT operational pullback structure.

---

# 8. Average-case distinction divergence

For smooth ensemble-level thermodynamics define the set \(\mathcal M_R\) of admissible POVMs. For a measurement \(M=\{M_y\}\), let

\[
p_\rho^M(y)=\operatorname{Tr}(M_y\rho).
\]

Define the **resource-measured distinction relative entropy**

\[
\boxed{
D_{D,R}(\rho\Vert\sigma)
:=
\sup_{M\in\mathcal M_R}
D_2(p_\rho^M\Vert p_\sigma^M),
}
\tag{MR1}
\]

where

\[
D_2(p\Vert q)=\sum_y p_y\log_2\frac{p_y}{q_y}.
\]

This is a resource-restricted measured relative entropy.

---

# 9. Theorem — measured distinction DPI

Assume every admissible post-process POVM pulls back to an admissible pre-process POVM. Then

\[
\boxed{
D_{D,R'}(\Phi\rho\Vert\Phi\sigma)
\le
D_{D,R}(\rho\Vert\sigma).
}
\tag{MR-DPI}
\]

### Proof

Every admissible measurement after \(\Phi\) corresponds to an admissible pulled-back measurement before \(\Phi\) producing the same pair of classical outcome distributions. Therefore the post-process supremum is taken over a subset of pre-process distinguishability experiments. QED.

The same argument also proves monotonicity under resource restriction:

\[
\mathcal M_{R_1}\subseteq\mathcal M_{R_2}
\Rightarrow
D_{D,R_1}\le D_{D,R_2}.
\]

---

# 10. Akhtar average operational free energy

Define

\[
\boxed{
\mathcal F_D^R(\rho)
:=
F_{\rm eq}
+k_BT\ln2\,
D_{D,R}(\rho\Vert\gamma).
}
\tag{AOF2}
\]

For a Gibbs-preserving admissible process,

\[
\boxed{
\mathcal F_D^{R'}(\Phi\rho)
\le
\mathcal F_D^R(\rho).
}
\tag{AOF2-DPI}
\]

This is now a PDT-native monotonicity theorem in the following limited but meaningful sense: the mathematical proof uses only the operational distinction experiment family, Gibbs-reference preservation, and classical relative-entropy data processing after measurement.

---

# 11. Free-energy sandwich theorem

Let

\[
D_Q^{(2)}(\rho\Vert\gamma)
=
\operatorname{Tr}\rho(\log_2\rho-\log_2\gamma)
\]

be quantum relative entropy in bits.

Standard measured-relative-entropy monotonicity gives

\[
D_{D,R}(\rho\Vert\gamma)
\le
D_Q^{(2)}(\rho\Vert\gamma).
\]

The standard nonequilibrium Helmholtz free energy satisfies

\[
F_{\rm std}(\rho)
-F_{\rm eq}
=
 k_BT\ln2\,
D_Q^{(2)}(\rho\Vert\gamma).
\]

Therefore

\[
\boxed{
F_{\rm eq}
\le
\mathcal F_D^R(\rho)
\le
F_{\rm std}(\rho).
}
\tag{sandwich}
\]

This is the **PDT free-energy sandwich**.

Interpretation:

- equilibrium is the zero-distinction-advantage baseline;
- finite physical access reveals only part of the total nonequilibrium free-energy gap;
- unrestricted quantum distinguishability provides the standard thermodynamic upper limit.

---

# 12. Resource-hidden distinction free energy

Define

\[
\boxed{
\mathcal F_{\rm hidden}^R(\rho)
:=
F_{\rm std}(\rho)-\mathcal F_D^R(\rho)
}
\tag{hidden}
\]

so that

\[
\boxed{
\mathcal F_{\rm hidden}^R
=
 k_BT\ln2
\left[
D_Q^{(2)}(\rho\Vert\gamma)
-
D_{D,R}(\rho\Vert\gamma)
\right]
\ge0.
}
\]

This is not claimed to be the first accessible/inaccessible-free-energy decomposition in thermodynamics; constrained-thermodynamic literature already contains related decompositions. The PDT-specific interpretation is narrower: the gap quantifies free-energy-bearing state distinction that exists in the quantum state but is not operationally accessible under the declared PDT resource window.

Nested resources satisfy

\[
R_1\subseteq R_2
\Rightarrow
\mathcal F_{\rm hidden}^{R_1}
\ge
\mathcal F_{\rm hidden}^{R_2}.
\]

Thus increasing physical distinction access can only shrink the hidden gap.

---

# 13. Exact classical/commuting limit

If \(\rho\) and \(\gamma\) commute and the common eigenbasis measurement is admissible, then measurement in that basis preserves relative entropy:

\[
D_{D,R}(\rho\Vert\gamma)
=
D_Q^{(2)}(\rho\Vert\gamma).
\]

Hence

\[
\boxed{
\mathcal F_D^R(\rho)=F_{\rm std}(\rho)
}
\tag{commuting}
\]

in the fully accessible commuting case.

This gives an exact one-shot classical thermodynamic limit.

---

# 14. Derivation of the biased-memory Landauer cost

Take a degenerate \(d\)-level classical memory with \(H=0\), so

\[
\gamma=I/d,
\qquad
F_{\rm eq}=-k_BT\ln d.
\]

For a diagonal memory distribution \(p\),

\[
D_2(p\Vert u_d)
=
\log_2d-H_2(p).
\]

Therefore

\[
\mathcal F_D(p)
=
-k_BT\ln2\,H_2(p).
\]

The pure reset state has entropy zero and free energy \(0\). Hence its free-energy increase is

\[
\boxed{
\Delta F_{\rm reset}
= k_BT\ln2\,H_2(p).
}
\tag{Landauer-from-F}
\]

Under standard reversible isothermal work-cost assumptions this recovers the entropy-weighted Landauer erasure cost.

So the v6 correction now emerges naturally from the distinction-free-energy construction rather than being attached separately.

---

# 15. Asymptotic unrestricted quantum closure

For unrestricted collective measurements on \(n\) i.i.d. copies, quantum Stein-type asymptotics imply that the optimal hypothesis-testing exponent converges to quantum relative entropy:

\[
\boxed{
\lim_{n\to\infty}
\frac1n
D_H^{\varepsilon}
\big(\rho^{\otimes n}\Vert\gamma^{\otimes n}\big)
=
D_Q^{(2)}(\rho\Vert\gamma)
}
\tag{Stein}
\]

for fixed \(0<\varepsilon<1\), with the standard regularity conditions.

Therefore the per-copy one-shot PDT free energy obeys

\[
\boxed{
\lim_{n\to\infty}
\frac1n
\mathcal F_{H}^{\varepsilon}
(\rho^{\otimes n})
=
F_{\rm std}(\rho).
}
\tag{AOF-limit}
\]

This is an imported asymptotic quantum-information theorem applied to the PDT construction, but it gives a major structural closure:

\[
\boxed{
\text{finite-resource physical hypothesis testing}
\longrightarrow
\text{one-shot PDT free energy}
\longrightarrow
\text{standard quantum free energy asymptotically}.
}
\]

---

# 16. No-go theorem — free-energy monotonicity does not determine Akhtar decay rate

It is tempting to claim that once the PDT free-energy monotone is established, the Akhtar attenuation law follows automatically. This is false.

Let \(\mathcal E\) be a Gibbs-preserving CPTP idempotent map. For every constant \(a>0\),

\[
\mathcal L_a=a(\mathcal E-I)
\]

generates the CPTP semigroup

\[
T_t^{(a)}=e^{-at}I+(1-e^{-at})\mathcal E.
\]

Every member of this one-parameter family respects the same Gibbs fixed point and the same free-energy monotonicity structure, but unsupported modes decay at different rates \(a\).

Therefore

\[
\boxed{
\text{free-energy DPI}
\not\Rightarrow
\Gamma_A=\ln2\,\Phi_H.
}
\tag{NG-rate}
\]

The one-bit attenuation calibration remains an independent dynamical principle or experimental law.

This is a decisive separation between PDT thermodynamic kinematics and PDT dynamics.

---

# 17. No-go theorem — one scalar free energy is not a complete one-shot second law

In finite quantum thermodynamics, one-shot state convertibility generally requires more structure than monotonicity of a single Helmholtz free energy; thermo-majorization and families of generalized free energies/divergences appear in established resource-theoretic treatments.

Therefore PDT must not claim

\[
\boxed{
\mathcal F_D^R\ \text{alone completely determines all finite-size thermal transformations}.
}
\]

The correct claim is narrower:

\[
\boxed{
\mathcal F_D^R\ \text{is a rigorously monotone finite-resource distinction-based thermal witness}.
}
\]

---

# 18. No-go theorem — Gibbs preservation is not the whole physics of thermal operations

A Gibbs-preserving channel can be mathematically admissible as a monotonicity map while failing to belong to a more restrictive physically implemented thermal-operation class, especially for genuinely quantum coherence-bearing states.

Hence

\[
\boxed{
\text{Gibbs-preserving monotonicity}
\not\Rightarrow
\text{full thermal implementability}.
}
\tag{NG-GP}
\]

PDT must state which physical process class it uses when turning a monotone into a work-cost theorem.

---

# 19. Relation to the Akhtar Equation

The thermodynamic and dynamical branches are now cleanly separated.

### Thermodynamic branch

\[
\boxed{
D_{H,R}^{\varepsilon},\ D_{D,R}
\Longrightarrow
\mathcal F_{H,R}^{\varepsilon},\ \mathcal F_D^R
\Longrightarrow
\text{resource/Gibbs monotonicity}.
}
\]

### Dynamical branch

\[
\boxed{
\text{independently measured distinction-entropy loss flux }\Phi_H
+\text{one-bit retention calibration}
\Longrightarrow
\Gamma_A=\ln2\,\Phi_H.
}
\]

The free-energy theorem constrains which transformations are allowed; the Akhtar Equation proposes how quickly unsupported distinctions disappear. The second does not follow from the first.

---

# 20. Horizon consequence

The new free-energy bridge still does not determine

\[
H_{D,H}=\frac{A}{4\ell_P^2\ln2}.
\]

What it does establish is the correct architecture needed if such a horizon distinction entropy is derived microscopically:

1. define a local thermal reference;
2. define finite-resource distinction divergences relative to that reference;
3. obtain monotonic free-energy witnesses by data processing;
4. in equilibrium/unrestricted limits recover standard relative-entropy thermodynamics;
5. only then use an independently derived horizon distinction entropy to connect to Clausius/Jacobson gravity.

The area coefficient remains an independent microscopic target.

---

# 21. Novelty boundary after literature attack

## Established prior art that must not be claimed as PDT discovery

- hypothesis-testing relative entropy;
- measured relative entropy;
- data processing for relative entropies;
- free-energy difference as relative entropy to the Gibbs state;
- Gibbs-preserving maps and thermal operations;
- quantum Stein's lemma;
- generalized one-shot free energies and thermo-majorization;
- accessible/inaccessible free-energy decompositions under constraints.

## Candidate PDT-specific synthesis

The potentially distinctive contribution is the chain

\[
\boxed{
\text{declared physical resource window }R
\to
\text{admissible physical distinction tests}
\to
D_{H,R}^{\varepsilon},D_{D,R}
\to
\text{finite-resource thermodynamic monotones}
\to
\text{canonical retained distinction algebra}
\to
\text{separately testable Akhtar dynamics}.
}
\]

The novelty is therefore architectural and operational, not the invention of relative entropy or free energy.

---

# 22. Proof-status update

| Claim | Status |
|---|---|
| Resource-restricted hypothesis-testing divergence | **PDT definition** |
| Hypothesis-testing DPI from test pullback | **Proved PDT-native** |
| Equality under admissible recovery | **Proved PDT-native** |
| Resource monotonicity of distinction power | **Proved** |
| One-shot distinction free energy | **PDT definition** |
| Free-energy monotonicity under Gibbs-preserving admissible maps | **Proved from PDT DPI** |
| Resource-measured distinction relative entropy | **PDT specialization of known measured relative entropy** |
| Average distinction free-energy monotonicity | **Proved conditionally** |
| Free-energy sandwich | **Proved using known measured-vs-quantum relative entropy inequality** |
| Hidden distinction free-energy gap nonnegative | **Proved** |
| Exact commuting/classical limit | **Proved** |
| Biased-memory Landauer cost | **Recovered using standard thermodynamic work theorem** |
| Asymptotic quantum free-energy recovery | **Imported quantum Stein theorem applied to PDT** |
| Free-energy monotonicity fixes Akhtar decay rate | **False / no-go** |
| One scalar free energy gives complete one-shot thermodynamics | **False / no-go** |
| Gibbs-preserving map = all physically thermal operations | **False / no-go** |
| Horizon area entropy derived microscopically from PDT | **Still open** |
| Akhtar one-bit attenuation calibration derived | **Still open** |
| Experimental validation | **Still open** |

---

# 23. Highest-value next theorem

After v7 the remaining high-value targets are sharply separated.

## Target A — derive the Akhtar attenuation calibration

Find a microscopic principle that singles out

\[
\boxed{
\Gamma_A=\ln2\,\Phi_H
}
\]

from the infinitely many Gibbs-compatible contraction rates. A plausible route is a **minimal irreversible distinction-loss principle** or a stochastic survival law derived from independently composable physical erasure events. This must not be assumed if it can be derived.

## Target B — horizon distinction entropy

Derive

\[
\boxed{
H_{D,H}=A/(4\ell_P^2\ln2)
}
\]

from a microscopic PDT boundary code or local causal-screen theory rather than importing Bekenstein-Hawking normalization.

## Target C — physical implementation class

Replace generic Gibbs-preserving maps with a rigorously specified PDT thermal-operation class built from energy-conserving reversible dynamics, bath states, and declared finite-resource controls.

A genuine foundational breakthrough would require at least one of these three remaining targets to be closed without importing the desired result as an axiom.

---

# 24. Kill tests

Reject or weaken the v7 thermodynamic extension if:

1. experimentally accessible PDT tests fail the stated pullback closure under the proposed physical process class;
2. the resource divergence cannot be independently estimated from discrimination experiments;
3. the claimed Gibbs reference is not actually preserved by the allowed process family;
4. the hidden distinction free-energy gap has no operational work interpretation in the intended implementation class;
5. asymptotic collective distinction experiments do not approach the expected quantum Stein exponent under the claimed resource assumptions;
6. a supposedly universal Akhtar attenuation law depends on rates not determined by independently measured distinction-loss statistics.

The kill tests are part of the theorem package, not optional caveats.
