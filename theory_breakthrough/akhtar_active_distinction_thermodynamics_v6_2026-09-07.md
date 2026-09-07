# Akhtar Active-Distinction Thermodynamics v6 — Capacity No-Go, Occupied Distinction Entropy, and Corrected Heat–Coherence Law

## Status

This attack corrects the strongest remaining thermodynamic overclaim in v5.

The v5 inequality

\[
\Delta S_{\rm env}\ge k_B\ln2\,\Delta K_D
\]

cannot hold for an arbitrary loss of **capacity** \(K_D\). Capacity counts how many alternatives *could* be distinguished; Landauer cost is controlled by the entropy/information actually carried by the occupied logical ensemble, with further modifications when side information, correlations, nondegenerate Hamiltonians, or finite reservoirs are present.

The key new result of this file is therefore a no-go theorem and a corrected state-resolved quantity.

This file does **not** claim a new proof of Landauer's principle. The thermodynamic inequalities used below are established results. The PDT-specific contribution is the distinction-capacity/occupied-distinction separation and its consequences for the Akhtar dynamics.

---

# 1. Capacity is not occupied information

Let an operational distinction register have \(M\) perfectly distinguishable alternatives \(\{d_i\}_{i=1}^M\). Its distinction capacity is

\[
K_D=\log_2 M.
\]

Let the actually occupied ensemble be

\[
\mathsf D=\{(p_i,d_i)\}_{i=1}^M,
\qquad p_i\ge0,\quad\sum_i p_i=1.
\]

Define its **occupied distinction entropy**

\[
\boxed{
H_D(\mathsf D):=-\sum_i p_i\log_2p_i.
}
\tag{OD}
\]

Then the elementary Shannon bound gives

\[
\boxed{
0\le H_D(\mathsf D)\le K_D,
}
\tag{capacity-entropy}
\]

with equality \(H_D=K_D\) iff the occupied alternatives are equiprobable on the full distinguishable codebook.

Thus capacity and occupied information coincide only in the maximally occupied case.

---

# 2. No-go theorem: capacity loss alone cannot imply a Landauer cost

Consider a two-state memory with distinguishable logical states \(0,1\). It has

\[
K_D=1\ \text{bit}.
\]

But take the known ensemble

\[
p_0=1,\qquad p_1=0.
\]

Then

\[
H_D=0.
\]

Resetting the register to \(0\) performs no logical uncertainty reduction because the state is already known/reset. In an ideal reversible implementation its information-erasure cost can approach zero.

Therefore a universal rule assigning \(k_BT\ln2\) merely because a one-bit *capacity* is removed would give a positive lower bound for a zero-entropy logical state.

Hence

\[
\boxed{
\Delta K_D>0\not\Rightarrow Q_{\rm env}\ge k_BT\ln2\,\Delta K_D.
}
\tag{NG1}
\]

This is a strict counterexample to the capacity-based ADSL as a universal law.

### Consequence

The thermodynamically relevant distinction variable must be state/ensemble resolved. Scalar distinction capacity remains useful as a kinematic resource bound, but it cannot by itself determine erasure heat.

---

# 3. Distinction-register representation

Represent the occupied distinguishable alternatives by an orthogonal logical register

\[
\rho_D=\sum_i p_i|i\rangle\langle i|.
\]

Its von Neumann entropy is

\[
S(\rho_D)
=-k_B\operatorname{Tr}(\rho_D\ln\rho_D)
=k_B\ln2\,H_D.
\]

Therefore

\[
\boxed{
S_D:=k_B\ln2\,H_D
}
\tag{SD}
\]

is the physical entropy associated with uncertainty over perfectly distinguishable occupied logical sectors, provided internal sector entropies are unchanged or separately accounted for.

This gives the exact bridge between an operational distinction ensemble and standard thermodynamic entropy in the orthogonal logical-register regime.

---

# 4. Active Distinction Landauer Theorem

Consider an initially uncorrelated system-plus-thermal-reservoir process in which:

1. the logical distinction sectors are orthogonal;
2. the logical encoding is energetically degenerate, or energetic/free-energy changes are separately accounted for;
3. internal entropy inside each logical sector is unchanged or explicitly subtracted;
4. the reservoir starts thermal at temperature \(T\);
5. the physical evolution is globally reversible/unitary while the logical register is reset/coarse-grained.

Let

\[
\Delta H_D:=H_D^{\rm in}-H_D^{\rm out}\ge0
\]

be the decrease in occupied distinction entropy.

The standard Landauer entropy-decrease inequality

\[
\frac{Q_{\rm env}}{T}\ge S(\rho_D^{\rm in})-S(\rho_D^{\rm out})
\]

combined with (SD) yields

\[
\boxed{
Q_{\rm env}
\ge
k_BT\ln2\,\Delta H_D.
}
\tag{ADLT}
\]

Equivalently,

\[
\boxed{
\Delta S_{\rm env}
\ge
k_B\ln2\,\Delta H_D.
}
\tag{ADLT-S}
\]

This is the corrected **Akhtar Active-Distinction Landauer Theorem**.

It is a PDT specialization of established Landauer thermodynamics, not a replacement for it.

---

# 5. Saturation condition

In the quasistatic reversible infinite-reservoir limit, with no additional entropy production and under the assumptions above,

\[
\boxed{
Q_{\rm env}
=
k_BT\ln2\,\Delta H_D.
}
\tag{ADLT-sat}
\]

For a complete erasure of an equiprobable \(M\)-state register,

\[
H_D^{\rm in}=\log_2M=K_D,
\qquad H_D^{\rm out}=0,
\]

so

\[
Q_{\rm env}=k_BT\ln2\,K_D.
\]

Thus the familiar per-capacity-bit formula is recovered only in the fully occupied equiprobable case.

---

# 6. Occupancy factor

For \(K_D>0\), define the **distinction occupancy factor**

\[
\boxed{
\nu_D:=\frac{H_D}{K_D}.
}
\tag{nu}
\]

By (capacity-entropy),

\[
\boxed{0\le\nu_D\le1.}
\]

Interpretation:

- \(\nu_D=1\): all available distinction capacity is maximally/equiprobably occupied;
- \(0<\nu_D<1\): capacity exists but is only partially informationally occupied;
- \(\nu_D=0\): the logical alternative is known with certainty despite nonzero capacity.

This factor quantifies precisely why capacity-based thermodynamic accounting can overestimate minimum heat.

---

# 7. Rate form: active distinction entropy flux

Define the occupied-distinction entropy-loss flux

\[
\boxed{
\Phi_H(t):=-\frac{dH_D}{dt}\ge0
}
\qquad\text{bits/time}
\tag{PhiH}
\]

for an erasure interval.

Then (ADLT) gives

\[
\boxed{
\dot S_{\rm env}
\ge k_B\ln2\,\Phi_H
}
\tag{rateS}
\]

and, for an isothermal bath,

\[
\boxed{
\dot Q_{\rm env}
\ge k_BT\ln2\,\Phi_H.
}
\tag{rateQ}
\]

At reversible saturation,

\[
\dot Q_{\rm env}=k_BT\ln2\,\Phi_H.
\]

---

# 8. Correct relation to the Akhtar quantum distinction flux

The Akhtar quantum dynamics v3 uses a **capacity-deficit throughput** \(\Phi_K\) through

\[
\boxed{
\Gamma_A=\ln2\,\Phi_K.
}
\tag{AK}
\]

Thermodynamics, however, constrains the occupied distinction entropy flux \(\Phi_H\), not \(\Phi_K\) in general.

Define, whenever \(\Phi_K>0\), the **active-flux fraction**

\[
\boxed{
\nu_\Phi:=\frac{\Phi_H}{\Phi_K}.
}
\tag{nuphi}
\]

For protocols where occupied entropy loss cannot exceed the disappearance of the available distinguishable codebook at the same accounting resolution,

\[
0\le\nu_\Phi\le1.
\]

Then

\[
\Phi_H=\nu_\Phi\Phi_K
=\nu_\Phi\frac{\Gamma_A}{\ln2}.
\]

Substituting into (rateQ) yields the corrected heat–coherence inequality

\[
\boxed{
\dot Q_{\rm env}
\ge
k_BT\,\nu_\Phi\,\Gamma_A.
}
\tag{HC6}
\]

or

\[
\boxed{
\nu_\Phi\Gamma_A
\le
\frac{\dot Q_{\rm env}}{k_BT}.
}
\]

### Important correction

The v5 inequality

\[
\Gamma_A\le\frac{\dot Q}{k_BT}
\]

is recovered only when

\[
\nu_\Phi=1.
\]

Therefore it is not universal.

This closes a hidden logical gap between kinematic capacity deficit and thermodynamic information erasure.

---

# 9. Revised distinction efficiency

Define

\[
\boxed{
\eta_D^{\rm act}
:=
\frac{k_BT\ln2\,\Phi_H}{\dot Q_{\rm env}}
=
\frac{k_BT\,\nu_\Phi\Gamma_A}{\dot Q_{\rm env}}
}
\tag{eta6}
\]

when \(\dot Q_{\rm env}>0\).

The corrected active-distinction Landauer theorem gives

\[
\boxed{0\le\eta_D^{\rm act}\le1.}
\]

Equality means reversible saturation for the **actually occupied distinctions**, not merely full use of the available capacity.

The excess entropy-production rate is

\[
\boxed{
\dot\Sigma_A^{\rm act}
=
\dot S_{\rm env}
-k_B\ln2\,\Phi_H
\ge0.
}
\tag{Sigma6}
\]

---

# 10. Side-information correction

If an observer/memory \(M\) carries information about the distinction label \(D\), the thermodynamic cost can be reduced.

For a classical distinction label with quantum side memory, use the conditional entropy

\[
\boxed{
H_D(D|M)
=
\frac{1}{\ln2}
\big[S(\rho_{DM})-S(\rho_M)\big]
}
\tag{cond}
\]

in bits (with von Neumann entropies measured in natural units before division by \(\ln2\)).

The appropriate operational message is therefore:

\[
\boxed{
\text{erasure cost depends on occupied distinction uncertainty conditional on available side information, not on raw codebook capacity.}
}
\]

This is consistent with established quantum-information thermodynamics. It also gives PDT a clear rule for avoiding false per-bit claims in correlated settings.

For fully quantum memories, conditional entropy may become negative and work can in principle be extracted while consuming correlations/entanglement. Hence no unconditional positive \(k_BT\ln2\) cost per nominal distinction bit can be universally valid in that regime.

---

# 11. Finite-reservoir correction

For a finite thermal reservoir, the asymptotic Landauer bound need not be tight. Established finite-size results add positive corrections depending on reservoir size and entropy change.

Therefore the PDT thermodynamic hierarchy is

\[
\boxed{
Q_{\rm env}
\ge
k_BT\ln2\,\Delta H_D
+Q_{\rm finite/residual},
\qquad
Q_{\rm finite/residual}\ge0
}
\]

under the corresponding finite-reservoir assumptions.

PDT should not claim the bare \(k_BT\ln2\) coefficient is an exact finite-reservoir cost.

---

# 12. Covariant active-distinction form

Let \(j_H^a\) denote a current of **occupied distinction entropy bits**, not capacity bits. Define local active distinction destruction

\[
\sigma_H:=-\nabla_a j_H^a\ge0.
\]

Then the corrected local inequality is

\[
\boxed{
\nabla_a s^a
\ge
k_B\ln2\,\sigma_H.
}
\tag{CADSL6}
\]

The excess entropy-production density is

\[
\boxed{
\sigma_A^{\rm act}
=
\nabla_a s^a-k_B\ln2\,\sigma_H
\ge0.
}
\]

A current of mere *unused capacity* cannot appear on the right-hand side without an occupation law.

---

# 13. Horizon consequence

The horizon quantity

\[
K_H=\frac{A}{4\ell_P^2\ln2}
\]

is a capacity-like count. To insert it directly into a Landauer equality one therefore needs an additional horizon condition identifying the relevant horizon distinction modes as thermodynamically fully active, effectively

\[
\boxed{\nu_H=1.}
\]

Only with this saturation/occupation hypothesis does

\[
dS_H=k_B\ln2\,dK_H
\]

follow as the thermodynamically active entropy change associated with the full horizon capacity variation.

Therefore the gravity chain is more accurately

\[
\boxed{
K_H\propto A
+\nu_H=1
+\text{reversible local equilibrium}
\Rightarrow
\delta Q=T\,dS_H
\Rightarrow
\text{Einstein equation (Jacobson)}.
}
\]

This exposes one previously hidden assumption: horizon capacity must be thermodynamically occupied/saturated, not merely geometrically available.

---

# 14. New no-go theorem for gravity

Area-proportional **capacity** alone does not imply area-proportional entropy.

Indeed a capacity \(K_H\) specifies the logarithm of the number of available distinguishable states, whereas entropy depends on their occupation distribution. Different distributions over the same state space have the same capacity but different entropy.

Therefore

\[
\boxed{
K_H\propto A
\not\Rightarrow
S_H=k_B\ln2\,K_H
}
\tag{NG2}
\]

without a maximal-mixing/saturation/occupation principle or an independent microcanonical argument.

This no-go is important because it prevents PDT from silently identifying geometric capacity with thermodynamic entropy.

---

# 15. What is now proved, imported, and open

| Claim | Status |
|---|---|
| Raw distinction capacity loss universally costs \(k_BT\ln2\) per bit | **False / explicit no-go** |
| \(H_D\le K_D\) | **Proved (Shannon bound)** |
| Orthogonal occupied distinction entropy equals logical von Neumann entropy | **Proved** |
| \(Q\ge k_BT\ln2\Delta H_D\) under degenerate logical erasure assumptions | **Conditional theorem from established Landauer inequality** |
| Capacity-based v5 heat–coherence bound is universal | **False / corrected** |
| \(\dot Q\ge k_BT\nu_\Phi\Gamma_A\) | **Proved conditionally** |
| Active distinction efficiency is in \([0,1]\) | **Proved conditionally** |
| Side information changes erasure cost | **Imported established quantum-information result** |
| Finite reservoirs sharpen Landauer cost | **Imported established result** |
| Area capacity alone implies area entropy | **False / no-go** |
| Horizon area entropy requires occupation/saturation principle | **Open PDT microphysical bridge** |
| Akhtar quantum capacity flux equals occupied entropy flux | **False in general; equality requires \(\nu_\Phi=1\)** |

---

# 16. Strongest remaining microscopic target

The key open quantity is no longer a generic second law. It is the **occupation law** linking kinematic distinction capacity to state-resolved active distinction entropy.

The target is to derive, for the relevant equilibrium sectors,

\[
\boxed{
\nu_D=1
}
\]

from a deeper PDT principle rather than assume maximal occupation.

A possible route is a maximum-entropy/equiprobability theorem from:

1. reversible transitivity of micro-distinction states;
2. no privileged state within an equilibrium capacity shell;
3. compositional independence;
4. thermodynamic stationarity.

If these imply the uniform distribution over a finite accessible distinction shell, then

\[
H_D=\log_2M=K_D,
\]

and the capacity-to-entropy bridge closes in equilibrium.

This is the next high-value proof target.

---

# 17. Novelty boundary

The following are established and must not be claimed as PDT discoveries:

- Shannon entropy bound \(H(p)\le\log M\);
- Landauer's principle;
- quantum conditional-entropy erasure with side information;
- finite-reservoir corrections to Landauer;
- von Neumann entropy of an orthogonal classical register.

The potentially distinctive PDT contribution is instead the explicit three-layer separation

\[
\boxed{
\text{distinction capacity }K_D
\quad\neq\quad
\text{occupied distinction entropy }H_D
\quad\neq\quad
\text{thermodynamic cost}
}
\]

and its use to repair the Akhtar quantum/thermodynamic/gravity bridge.

The strongest new falsifiable relation after correction is

\[
\boxed{
\dot Q_{\rm env}
\ge
k_BT\,\nu_\Phi\Gamma_A,
}
\]

with \(\nu_\Phi\) independently measured from the occupied distinction ensemble rather than fitted to the heat or coherence curve.

A violation after independent measurement of \(\nu_\Phi\), \(\Gamma_A\), \(T\), and \(\dot Q\) rejects this minimal active-distinction thermodynamic coupling in the tested regime.
