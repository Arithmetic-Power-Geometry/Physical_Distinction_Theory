# Akhtar Equation v3 — Operational Closure, Deficit Flux, and Canonical Distinction Geometry

## Status

This document strengthens the Akhtar Equation by removing two avoidable free choices from v2:

1. the refresh-time parameter is replaced by an operational **distinction-deficit flux** measured directly in bits per unit time;
2. the resource geometry is derived canonically from the accessible distinguishability body by a unique extremal ellipsoid, avoiding an arbitrary weighted frame tensor.

The equation below is a candidate physical law. Its mathematical consistency is established under the stated finite-dimensional assumptions, but experimental validity and world-priority novelty remain open empirical/literature questions.

---

# 1. Operational distinction norm

Let \(V_0\) be the real vector space of traceless Hermitian operators on a finite-dimensional system. For a physical resource condition \(R\), let \(\mathcal E_R\) be the set of admissible effects. Define the accessible distinction seminorm

\[
\|X\|_R:=\sup_{E\in\mathcal E_R}|\operatorname{Tr}(EX)|.
\]

After quotienting by the kernel

\[
N_R:=\{X:\|X\|_R=0\},
\qquad
\widetilde V_R:=V_0/N_R,
\]

\(\|\cdot\|_R\) is a norm on \(\widetilde V_R\) whenever the accessible effects separate the quotient states.

Its closed unit ball is

\[
B_R:=\{x\in\widetilde V_R:\|x\|_R\le1\}.
\]

Because the norm is symmetric, \(B_R\) is a compact centrally symmetric convex body when finite-dimensional and nondegenerate.

---

# 2. Canonical resource-distinction ellipsoid

By the John/Löwner ellipsoid theorem, every finite-dimensional centrally symmetric convex body has a unique maximum-volume inscribed ellipsoid. Let that ellipsoid be

\[
\mathcal J_R\subseteq B_R.
\]

There is therefore a unique positive-definite operator \(G_R\) on \(\widetilde V_R\), relative to any auxiliary Euclidean coordinate system, such that

\[
\boxed{
\mathcal J_R=\{x:\langle x,G_Rx\rangle\le1\}.
}
\tag{J}
\]

The coordinate representation changes covariantly, but the ellipsoid itself is intrinsic.

## Theorem 1 — canonicality

If an invertible reversible transformation \(U\) preserves the accessible distinction body,

\[
U(B_R)=B_R,
\]

then uniqueness of the John ellipsoid implies

\[
U(\mathcal J_R)=\mathcal J_R.
\]

Hence

\[
U^{\mathsf T}G_RU=G_R.
\]

Thus the resource tensor is not chosen by an arbitrary averaging measure over effects: it is fixed by the full accessible distinguishability geometry.

---

# 3. Canonical stable sectors

Let the eigenvalues of \(G_R\) be

\[
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n>0.
\]

For a permitted retained dimension \(k\), define

\[
S_R^{(k)}:=\operatorname{span}\{v_1,\ldots,v_k\}.
\]

By the Ky Fan variational principle,

\[
\boxed{
S_R^{(k)}\in\arg\max_{\dim S=k}\operatorname{Tr}(\Pi_SG_R).
}
\tag{KF}
\]

If

\[
\lambda_k>\lambda_{k+1},
\]

then this maximizing subspace is unique.

For a qubit, \(\widetilde V_R\cong\mathbb R^3\). If \(n_R\) is the principal eigenvector of \(G_R\), define

\[
\Pi_\pm=\frac12(I\pm n_R\cdot\sigma),
\]

and the unique associated dephasing conditional expectation

\[
\boxed{
\mathcal E_R(\rho)=\Pi_+\rho\Pi_++\Pi_-\rho\Pi_-.
}
\tag{Q-proj}
\]

when \(\lambda_1>\lambda_2\). Exact degeneracy correctly produces a nonunique symmetry-related family rather than an artificial preferred basis.

---

# 4. Higher-dimensional algebra selection

For \(d>2\), an arbitrary leading eigenspace need not be a unital \(*\)-subalgebra. Therefore the physical retained object is selected at the algebra level.

Let \(\mathfrak A_R\) be a nonempty closed family of admissible unital \(*\)-subalgebras of \(M_d(\mathbb C)\) satisfying the resource budget. For each \(\mathcal A\in\mathfrak A_R\), let \(E_\mathcal A\) be the trace-preserving conditional expectation onto \(\mathcal A\), and \(\Pi_{\mathcal A,0}\) the Hilbert-Schmidt projector onto its traceless self-adjoint part.

Define

\[
J_R(\mathcal A):=\operatorname{Tr}(\Pi_{\mathcal A,0}G_R).
\]

Because the admissible family is compact under the stated closed finite-dimensional budget and \(J_R\) is continuous,

\[
\boxed{
\exists\;\mathcal A_R\in\arg\max_{\mathcal A\in\mathfrak A_R}J_R(\mathcal A).
}
\tag{A-exist}
\]

Set

\[
\boxed{\mathcal E_R:=E_{\mathcal A_R}.}
\]

Thus a CPTP idempotent retained algebra exists under this formulation. Uniqueness holds whenever the maximizer is isolated; degeneracy is a physical symmetry case, not a mathematical failure.

---

# 5. Remove the arbitrary refresh time: distinction-deficit flux

The v2 quantity \(\chi/\tau\) suggests the actually fundamental quantity is not a window duration but a **deficit throughput**.

For a time interval of length \(T\), define the operationally required distinction capacity

\[
K_{\rm req}(T)
\]

and the physically available accessible distinction capacity

\[
K_R(T),
\]

both in bits, using the same PDT codebook/discrimination criterion.

Define the cumulative unsupported distinction exposure

\[
B_R(T):=[K_{\rm req}(T)-K_R(T)]_+
\]

when the task admits a cumulative capacity accounting, and in a stationary throughput regime define the **Akhtar distinction-deficit flux**

\[
\boxed{
\Phi_R:=\limsup_{T\to\infty}\frac{B_R(T)}{T}
}
\qquad\text{bits/time}.
\tag{flux}
\]

For a nonstationary process, use a locally measurable nonnegative flux \(\Phi_R(t)\) with cumulative exposure

\[
\boxed{
\mathcal B_R(t)=\int_0^t\Phi_R(s)\,ds.
}
\tag{cum}
\]

This removes \(\tau_R\) as a primitive dynamical constant. The earlier v2 model is recovered when

\[
\Phi_R=\chi_R/\tau_R.
\]

---

# 6. Retention theorem in flux form

Let \(s(b)\) be the retained fraction of an unsupported distinction component after cumulative deficit exposure \(b\) bits. Assume

\[
s(0)=1,
\qquad
s(b_1+b_2)=s(b_1)s(b_2),
\qquad
s(1)=\frac12,
\]

and continuity. Then the multiplicative Cauchy equation gives uniquely

\[
\boxed{s(b)=2^{-b}.}
\tag{retention}
\]

Differentiating with \(b=\mathcal B_R(t)\) gives

\[
\frac{d}{dt}\ln s=-\ln2\,\Phi_R(t).
\]

Therefore the only continuous Markovian hazard compatible with additive deficit bits and one-bit halving is

\[
\boxed{\gamma_R(t)=\ln2\,\Phi_R(t).}
\tag{hazard}
\]

No refresh-time convention is required.

---

# 7. The Akhtar Distinction-Flux Equation

The sharpened single-constraint equation is

\[
\boxed{
\frac{d\rho}{dt}
=-\frac{i}{\hbar}[H,\rho]
+\ln2\,\Phi_R(t)\big(\mathcal E_R(t)[\rho]-\rho\big).
}
\tag{AE3}
\]

The reversible term transports quantum distinctions. The second term contracts precisely the sector not retained by the resource-selected conditional expectation, at a rate fixed by independently measured missing distinction throughput.

---

# 8. Multi-constraint Akhtar Equation

A single projection is insufficient for genuinely independent resource restrictions on different subsystems or sectors. The natural closure is a family of constraints \(a=1,\dots,m\), each with flux \(\Phi_a(t)\ge0\) and CPTP idempotent conditional expectation \(\mathcal E_a(t)\).

Define

\[
\boxed{
\dot\rho
=-\frac{i}{\hbar}[H,\rho]
+\ln2\sum_{a=1}^m\Phi_a(t)\big(\mathcal E_a(t)-I\big)[\rho].
}
\tag{MAE}
\]

This is the **multi-constraint Akhtar Equation**.

## Theorem 2 — CPTP consistency

For each fixed time, every generator

\[
\mathcal G_a=\ln2\,\Phi_a(\mathcal E_a-I)
\]

generates a CPTP semigroup because

\[
e^{t\mathcal G_a}=e^{-\ln2\Phi_at}I+
(1-e^{-\ln2\Phi_at})\mathcal E_a.
\]

A nonnegative sum of GKLS generators plus a Hamiltonian derivation is again a valid GKLS generator in finite dimension. Therefore the time-ordered propagator of (MAE) is CPTP for piecewise-continuous data.

---

# 9. Exact independent-composition theorem

For independent systems \(A,B\), use

\[
\mathcal E_A\otimes I_B,
\qquad
I_A\otimes\mathcal E_B,
\]

with fluxes \(\Phi_A,\Phi_B\). These maps commute. The resource propagator factorizes:

\[
T_t^{AB}=T_t^A\otimes T_t^B.
\]

An operator component unsupported by both constraints acquires the factor

\[
\exp[-\ln2(\Phi_A+\Phi_B)t]
=2^{-(\Phi_A+\Phi_B)t}.
\]

Hence deficit bits add exactly while retention probabilities multiply:

\[
\boxed{
\mathcal B_{AB}=\mathcal B_A+\mathcal B_B,
\qquad
s_{AB}=s_As_B.
}
\tag{composition}
\]

This closes a weakness of the single-projection version, which did not correctly represent all independent local constraints.

---

# 10. Exact coherence law

Suppose \(X\) lies in the kernel of a time-independent retained projection and commutes with the Hamiltonian sector apart from a phase rotation. Then its amplitude \(c(t)\) obeys

\[
\dot c=-(i\omega+\ln2\,\Phi_R)c.
\]

Therefore

\[
\boxed{
c(t)=c(0)e^{-i\omega t}2^{-\mathcal B_R(t)}.
}
\tag{P1}
\]

Equivalently,

\[
\boxed{
-\log_2\frac{|c(t)|}{|c(0)|}=\mathcal B_R(t).
}
\tag{P1-test}
\]

This is parameter-free once \(\mathcal B_R\) is independently measured from discrimination throughput rather than inferred from the observed decoherence.

---

# 11. Basis/sector prediction

The accessible distinction body determines the unique John ellipsoid. For a generic qubit,

\[
\boxed{
\text{stable axis}=\text{principal axis of }\mathcal J_R.
}
\tag{P2}
\]

Thus the theory predicts both:

1. which distinction sector is retained;
2. how unsupported components decay.

For higher dimensions, the predicted stable algebra is

\[
\boxed{
\mathcal A_R\in\arg\max_{\mathcal A\in\mathfrak A_R}
\operatorname{Tr}(\Pi_{\mathcal A,0}G_R).
}
\tag{P2A}
\]

---

# 12. Operational measurement protocol

No Akhtar parameter may be estimated from the same coherence curve used to test the equation.

## Step A — estimate the accessible distinction body

Choose a spanning set of independently calibrated traceless perturbations \(X_j\). For each direction, solve the constrained binary-discrimination problem experimentally using only the allowed effects \(\mathcal E_R\). Estimate

\[
\|X\|_R=\sup_{E\in\mathcal E_R}|\operatorname{Tr}(EX)|.
\]

Use these support-function measurements to reconstruct the convex body \(B_R\) or a certified outer/inner approximation.

## Step B — compute the canonical ellipsoid

Solve the standard maximum-volume inscribed-ellipsoid convex program for the reconstructed body. This produces \(\mathcal J_R\) and hence \(G_R\) without selecting weights over measurements.

## Step C — predict the stable sector

For qubits, diagonalize \(G_R\); its principal eigenvector predicts the retained axis. For higher dimensions, optimize the algebra score \(J_R(\mathcal A)\).

## Step D — independently measure deficit throughput

Run codebook/discrimination tasks over windows of duration \(T\), obtaining

\[
K_{\rm req}(T),\qquad K_R(T),
\]

from operational success/error thresholds. Estimate

\[
\Phi_R\approx\frac{[K_{\rm req}(T)-K_R(T)]_+}{T}
\]

in the stationary regime, or reconstruct cumulative \(\mathcal B_R(t)\) in a time-dependent protocol.

## Step E — blind prediction

Without fitting a decoherence constant, predict

\[
|c(t)|_{\rm pred}=|c(0)|2^{-\mathcal B_R(t)}
\]

and the stable basis/algebra from \(G_R\). Only then compare with the observed quantum evolution.

---

# 13. Identifiability theorem

If \(\mathcal B_R(t)\) is independently measured and the unsupported mode is known from the independently reconstructed \(\mathcal E_R\), then the Akhtar equation has no free decay-rate parameter for that mode.

Indeed

\[
\Gamma_A(t)=\ln2\,\Phi_R(t)
\]

is already fixed. Therefore any measured residual rate \(\Gamma_{\rm obs}\) can be compared directly against

\[
\boxed{\Gamma_{\rm obs}(t)\stackrel{?}{=}\ln2\,\Phi_R(t).}
\]

A systematic mismatch falsifies this minimal Akhtar law for the tested regime rather than being absorbed by a fitted coupling constant.

---

# 14. Qutrit construction

Use the eight-dimensional traceless Hermitian space spanned by Gell-Mann matrices. Reconstruct \(B_R\), compute the John tensor \(G_R\), and consider admissible qutrit subalgebras such as:

- a maximal diagonal algebra \(\mathbb C^3\);
- a block algebra \(M_2(\mathbb C)\oplus\mathbb C\);
- the full algebra \(M_3(\mathbb C)\) when capacity permits.

For each admissible algebra, compute

\[
J_R(\mathcal A)=\operatorname{Tr}(\Pi_{\mathcal A,0}G_R).
\]

The maximum defines the predicted retained algebra and its trace-preserving conditional expectation. Thus the qutrit problem is a finite-dimensional optimization, not an undefined preferred-basis choice.

---

# 15. Novelty boundary and prior-art collision tests

The following components are established mathematics/physics and must not be claimed as new:

- restricted-measurement distinguishability norms;
- state/channel discrimination as an operational resource characterization;
- quantum Fisher information and frame-operator analyses;
- John/Löwner ellipsoids and Ky Fan variational principles;
- conditional expectations and GKLS/Lindblad semigroups;
- decoherence and information accessibility relations;
- direct experimental estimation of decoherence rates.

The candidate-new synthesis to test against the literature is specifically:

\[
\boxed{
\text{accessible distinction body}
\to
\text{canonical extremal ellipsoid}
\to
\text{resource-selected conditional expectation}
\to
\text{independently measured deficit-bit flux}
\to
\text{CPTP dynamics}
}
\]

with the parameter-constrained prediction

\[
\boxed{
-\log_2(|c(t)|/|c(0)|)=\mathcal B_R(t)
}
\]

and the simultaneous stable-sector prediction from the same accessible distinction geometry.

A 2026 literature check must explicitly compare against recent operator-frame/Fisher-information work, resource-constrained measurement theory, reconstruction-limited irreversibility, and finite-accessibility rank-collapse approaches. Similar ingredients do not by themselves invalidate novelty; an exact prior occurrence of the full operational chain or the same bit-flux evolution law would.

---

# 16. Kill tests

The v3 Akhtar law fails as a fundamental law in a tested regime if any of the following occurs:

1. independently reconstructed \(B_R\) predicts a stable sector inconsistent with the observed one beyond uncertainty;
2. independently measured \(\mathcal B_R(t)\) does not satisfy the predicted base-2 attenuation of unsupported components;
3. independent deficits fail additive-bit/multiplicative-retention composition in a regime where the independence assumptions hold;
4. no admissible conditional expectation/algebra corresponds to the experimentally stable sector under the stated resource budget;
5. the same observed decay can only be matched by defining \(\Phi_R\) from the decay itself, making the theory circular;
6. a prior publication is found containing the same canonical resource-body selection plus the same deficit-bit-flux dynamical law.

---

# 17. What is now closed and what remains

| Target | v3 status |
|---|---|
| Remove arbitrary refresh time | **Closed** by deficit flux \(\Phi_R\) |
| Exact continuous retention law | **Closed**: \(2^{-\mathcal B_R}\) |
| Canonical geometry from accessible distinctions | **Closed mathematically** by unique John ellipsoid |
| Generic qubit stable axis | **Closed conditionally** |
| Higher-dimensional retained algebra existence | **Closed under compact admissible algebra family** |
| Independent subsystem composition | **Closed** by multi-constraint generator |
| CPTP dynamics | **Closed** under CPTP conditional expectations |
| Parameter-free decay rate after independent resource measurement | **Closed structurally** |
| Qutrit prescription | **Closed algorithmically** |
| Experimental operationalization | **Specified, not yet executed** |
| World-priority novelty | **Not proved; requires exhaustive search** |
| Experimental truth | **Open** |
| Gravity from the same equation | **Open** |

---

# 18. Strongest defensible current statement

The strongest scientifically defensible result is not that a new law of nature has been discovered. It is:

> PDT now has a mathematically consistent, operationally noncircular candidate dynamical law in which the resource-stable sector is selected canonically from constrained distinguishability geometry and the irreversible rate is fixed by independently measurable unsupported distinction throughput in bits per unit time. In commuting/independent sectors the law predicts exact base-2 attenuation with additive deficit exposure.

The next decisive step is experimental/computational validation and an exhaustive novelty audit, not adding another free phenomenological term.
