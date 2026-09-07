# Akhtar Equation v2 — Exact Semigroup Embedding and Spectral Distinction Closure

## Status

This file supersedes the continuous-time rate used in `akhtar_equation_heavy_attack_2026-09-07.md`. The earlier choice

\[
\gamma=(1-2^{-\chi})/\tau
\]

is valid as a **discrete one-step mixing fraction divided by a time window**, but it does **not** embed the retention law \(s(\chi)=2^{-\chi}\) exactly into a continuous semigroup. Exact embedding forces a different rate. This correction strengthens the theory by removing an internal mismatch.

The resulting equation remains a candidate physical law, not an experimentally established law.

---

# 1. Exact retention law

Assume the retained fraction of an independently composable distinction deficit obeys

\[
s(0)=1,
\qquad
s(\chi_1+\chi_2)=s(\chi_1)s(\chi_2),
\qquad
s(1)=1/2,
\]

with continuity. Then

\[
\boxed{s(\chi)=2^{-\chi}}.
\]

This is the unique continuous solution.

---

# 2. Exact continuum-embedding theorem

Let \(\mathcal P\) be a CPTP idempotent channel and define

\[
\mathcal G_\gamma=\gamma(\mathcal P-I).
\]

Because \(\mathcal P^2=\mathcal P\),

\[
T_t=e^{t\mathcal G_\gamma}
=e^{-\gamma t}I+(1-e^{-\gamma t})\mathcal P.
\]

For any operator \(X\in\ker \mathcal P\),

\[
T_tX=e^{-\gamma t}X.
\]

If one resource-refresh window of duration \(\tau\) must retain exactly the fraction \(2^{-\chi}\) of the unsupported distinction sector, then

\[
e^{-\gamma\tau}=2^{-\chi}.
\]

Taking logarithms gives the unique nonnegative rate

\[
\boxed{
\gamma_{\rm A}(\chi,\tau)=\frac{\ln2}{\tau}\,\chi.
}
\tag{A-rate}
\]

Hence the exact continuous-time Akhtar Resource-Distinction Equation is

\[
\boxed{
\frac{d\rho}{dt}
=-\frac{i}{\hbar}[H,\rho]
+\frac{\ln2}{\tau_R(t)}\chi_R(t)
\big(\mathcal P_R[\rho]-\rho\big).
}
\tag{AE-v2}
\]

This is the unique generator in the conditional-expectation semigroup family that exactly realizes the multiplicative bit-retention law at each refresh window.

---

# 3. Discrete/continuous consistency

The exact discrete update associated with one window is

\[
\rho_{n+1}
=2^{-\chi}\rho_n+(1-2^{-\chi})\mathcal P\rho_n.
\tag{D-AE}
\]

The continuous semigroup with rate \(\gamma_A=(\ln2)\chi/\tau\) satisfies

\[
T_\tau
=2^{-\chi}I+(1-2^{-\chi})\mathcal P,
\]

so

\[
\boxed{T_\tau=\text{exact discrete Akhtar update}.}
\]

This resolves the discrete/continuous mismatch in the first attack.

---

# 4. Exact composition theorem

For independent deficits \(\chi_A,\chi_B\),

\[
\chi_{AB}=\chi_A+\chi_B.
\]

Therefore

\[
\gamma_{AB}
=\frac{\ln2}{\tau}(\chi_A+\chi_B)
=\gamma_A+\gamma_B
\]

for a common refresh time. Equivalently, the retained fractions multiply:

\[
e^{-\gamma_{AB}\tau}
=e^{-\gamma_A\tau}e^{-\gamma_B\tau}
=2^{-(\chi_A+\chi_B)}.
\]

Thus the fundamental composition law is additive in hazard and multiplicative in retained distinction.

---

# 5. Time-dependent exact law

If \(\chi_R(t)\) and \(\tau_R(t)\) vary in time while \(\mathcal P_R\) is fixed on the interval, the unsupported sector obeys

\[
X(t)
=\exp\!\left[-\ln2\int_0^t\frac{\chi_R(s)}{\tau_R(s)}ds\right]X(0).
\]

Hence the experimentally testable integrated relation is

\[
\boxed{
-\log_2\frac{\|X(t)\|}{\|X(0)\|}
=\int_0^t\frac{\chi_R(s)}{\tau_R(s)}ds
}
\tag{AE-P1-v2}
\]

whenever the measured component lies completely in the unsupported sector and Hamiltonian mixing with that sector is controlled.

For constant \(\chi_R,\tau_R\),

\[
\boxed{
\Gamma_{\rm dist}=\frac{\ln2}{\tau_R}\chi_R
}
\tag{AE-P2-v2}
\]

and after \(N\) refresh windows,

\[
\boxed{
\frac{\|X(N\tau_R)\|}{\|X(0)\|}=2^{-N\chi_R}.
}
\]

---

# 6. The missing object: selecting \(\mathcal P_R\)

A physically useful theory cannot choose a dephasing basis by hand. We therefore replace the broad worst-case optimization by a quadratic distinction-power selector in the Hilbertian sector already obtained from PDT/BQDC.

Let \(V_D\) be a finite-dimensional real distinction space and let the available resource window define a positive semidefinite operator \(G_R\) such that the resource-accessible quadratic distinction power is

\[
Q_R(x)=\langle x,G_Rx\rangle_D.
\]

For a \(k\)-dimensional retained distinction subspace \(S\subset V_D\), let \(\Pi_S\) be the orthogonal projector and define retained power

\[
\mathcal J_R(S)=\operatorname{Tr}(\Pi_SG_R).
\]

The resource-stable subspace is selected by

\[
\boxed{
S_R^{(k)}\in\arg\max_{\dim S=k}\operatorname{Tr}(\Pi_SG_R).
}
\tag{SDP-select}
\]

---

# 7. Akhtar spectral-selection theorem

Let the eigenvalues of \(G_R\) be

\[
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n\ge0
\]

with orthonormal eigenvectors \(v_i\). By the Ky Fan maximum principle,

\[
\max_{\dim S=k}\operatorname{Tr}(\Pi_SG_R)
=\sum_{i=1}^k\lambda_i.
\]

Therefore one optimal retained distinction sector is

\[
\boxed{
S_R^{(k)}=\operatorname{span}\{v_1,\ldots,v_k\}.
}
\]

If

\[
\lambda_k>\lambda_{k+1},
\]

then this \(k\)-dimensional subspace is unique.

Thus:

\[
\boxed{
\text{finite-dimensional quadratic PDT distinction geometry}
+\text{rank budget}
\Longrightarrow
\text{existence of an optimal retained distinction subspace}
}
\]

and it is generically unique when the spectral cutoff is nondegenerate.

This is a direct theorem once \(G_R\) is operationally specified; the Ky Fan variational principle itself is classical prior mathematics.

---

# 8. Covariance theorem

Let a reversible transformation act orthogonally on distinction space by \(U\), and suppose

\[
G_R\mapsto G'_R=UG_RU^T.
\]

If the spectral cutoff is nondegenerate, then spectral projectors transform as

\[
\Pi_{S'_R}=U\Pi_{S_R}U^T.
\]

Hence the selector is reversible-covariant:

\[
\boxed{
S_R\mapsto US_R.
}
\]

No preferred coordinate system is inserted by the selector.

---

# 9. Qubit closure: explicit CPTP projection

For a qubit, write

\[
\rho=\frac12(I+r\cdot\sigma),\qquad r\in\mathbb R^3.
\]

Let \(G_R\) be the \(3\times3\) positive semidefinite accessible-distinction tensor. Under a one-axis resource budget, the spectral-selection theorem chooses the principal unit eigenvector \(n_R\) of \(G_R\).

The corresponding trace-preserving conditional expectation onto the commutative algebra generated by \(n_R\cdot\sigma\) is

\[
\boxed{
\mathcal P_R(\rho)
=\sum_{s=\pm}\Pi_s\rho\Pi_s,
\qquad
\Pi_s=\frac12(I+s\,n_R\cdot\sigma).
}
\]

In Bloch form,

\[
r\mapsto(n_R\cdot r)n_R.
\]

This map is CPTP, unital and idempotent. Therefore, for the qubit, the Akhtar Equation v2 is fully explicit once the experimentally estimated \(G_R\), \(\chi_R\), and \(\tau_R\) are supplied.

If the largest eigenvalue of \(G_R\) is nondegenerate, the axis \(n_R\) is unique up to sign, and the dephasing algebra is sign-independent. Thus the **qubit physical projection is genuinely unique** in the generic case.

---

# 10. Higher-dimensional existence theorem via operator algebras

For \(M_d(\mathbb C)\), an arbitrary orthogonal projection in operator space need not be CPTP. Therefore the higher-dimensional selector must optimize over physical fixed-point algebras rather than arbitrary linear subspaces.

Let \(\mathfrak A_{d,m}\) be the set of unital *-subalgebras \(\mathcal A\subseteq M_d(\mathbb C)\) satisfying a chosen algebra-size/resource budget \(m\). For every such \(\mathcal A\), there is a unique trace-preserving conditional expectation

\[
E_\mathcal A:M_d\to\mathcal A,
\]

which is the Hilbert-Schmidt orthogonal projection onto \(\mathcal A\) and is CPTP.

Define

\[
\mathcal J_R(\mathcal A)
=\operatorname{Tr}(\Pi_{\mathcal A,0}G_R),
\]

where \(\Pi_{\mathcal A,0}\) projects onto the traceless self-adjoint distinction directions contained in \(\mathcal A\).

In finite dimension, the set of subalgebras obeying a closed dimension bound can be represented as a closed subset of the relevant Grassmannian: closure follows because containment of the identity, *-closure, and multiplication closure are polynomial/continuous closed conditions. The Grassmannian is compact. Therefore the admissible family is compact.

Since \(\mathcal J_R\) is continuous,

\[
\boxed{
\exists\ \mathcal A_R\in\arg\max_{\mathcal A\in\mathfrak A_{d,m}}\mathcal J_R(\mathcal A).
}
\]

Set

\[
\boxed{\mathcal P_R=E_{\mathcal A_R}.}
\]

Hence an optimal physical CPTP idempotent projection **exists** for every finite-dimensional system under this algebra-budget formulation.

Uniqueness is not guaranteed in symmetric/degenerate cases and must not be claimed generally.

---

# 11. Degeneracy is physical, not a proof failure

If the selector has several maximizing algebras, the resource window itself does not distinguish among them. Any claim of a unique pointer algebra would then add information not present in the physics.

Thus PDT predicts:

- nondegenerate resource tensor / objective -> unique stable algebra generically;
- exact symmetry -> an orbit or family of equally optimal stable algebras.

A symmetry-breaking perturbation of \(G_R\) resolves a generic degeneracy continuously when an eigengap opens.

This is preferable to inserting an arbitrary basis-selection rule.

---

# 12. Qutrit construction

Choose an orthonormal Hermitian operator basis

\[
\{I/\sqrt3,\lambda_1/\sqrt2,\ldots,\lambda_8/\sqrt2\}
\]

with Gell-Mann matrices \(\lambda_i\). Estimate the \(8\times8\) positive semidefinite accessible-distinction tensor \(G_R\).

Candidate physical retained algebras include, for example:

1. a maximal diagonal algebra \(U\mathcal D_3U^\dagger\), with dephasing conditional expectation;
2. block algebras such as \(U(M_2\oplus\mathbb C)U^\dagger\);
3. the trivial scalar algebra;
4. the full algebra if the resource budget permits it.

For each allowed algebra compute \(\mathcal J_R(\mathcal A)\). Compactness guarantees a maximizer over unitary embeddings. Its unique trace-preserving conditional expectation supplies \(\mathcal P_R\).

This gives a constructive qutrit algorithm, although a closed-form global optimizer for arbitrary \(G_R\) is not claimed.

---

# 13. Composite-system closure

For independent systems whose distinction tensors factor as a direct sum at the generator level,

\[
G_{AB}=G_A\oplus G_B,
\]

and whose deficits add,

\[
\chi_{AB}=\chi_A+\chi_B,
\]

the exact Akhtar hazards add:

\[
\gamma_{AB}=\gamma_A+\gamma_B
\]

for equal refresh calibration.

If the selected stable algebra factorizes,

\[
\mathcal A_{AB}=\mathcal A_A\otimes\mathcal A_B,
\]

then

\[
E_{\mathcal A_{AB}}=E_{\mathcal A_A}\otimes E_{\mathcal A_B}.
\]

The resource generator becomes the sum of commuting local distinction-loss generators. Genuine interaction appears when \(G_{AB}\) contains cross-system distinction modes; then the maximizing algebra need not factorize. Thus the same selector can, in principle, choose genuinely relational stable distinctions rather than a local pointer basis.

---

# 14. Falsifiable predictions upgraded

The corrected equation yields sharper tests than v1.

## P1. One-window bit law

For a controlled unsupported coherence mode,

\[
\boxed{
\frac{|c(\tau_R)|}{|c(0)|}=2^{-\chi_R}.
}
\]

## P2. Multi-window law

\[
\boxed{
|c(N\tau_R)|=|c(0)|2^{-N\chi_R}.
}
\]

## P3. Time-varying deficit law

\[
\boxed{
-\log_2\frac{|c(t)|}{|c(0)|}
=\int_0^t\chi_R(s)/\tau_R(s)\,ds.
}
\]

## P4. Principal-distinction axis

For a one-axis qubit budget, the observed stable/dephasing axis must coincide with the principal eigenvector of the independently estimated resource-accessible distinction tensor \(G_R\).

Thus the theory predicts **both a basis/sector and a rate**, not merely a free decoherence constant.

---

# 15. Kill tests

AE-v2 is falsified or requires revision if:

1. independently determined \(\chi_R,\tau_R\) do not satisfy the bit-retention law;
2. the observed stable qubit axis disagrees systematically with the principal axis of \(G_R\);
3. a no-deficit regime \(\chi_R=0\) exhibits an irreducible AE-specific correction after ordinary environmental channels are accounted for;
4. independent deficits fail multiplicative retention/additive hazard under conditions where independence is operationally verified;
5. higher-dimensional stable sectors cannot be represented by the selected physical conditional-expectation algebra despite accurate resource characterization.

---

# 16. Novelty boundary

Known ingredients that must be credited:

- GKLS/quantum Markov dynamics;
- conditional expectations and their trace-preserving uniqueness onto finite-dimensional unital *-subalgebras;
- Ky Fan spectral variational principle;
- PCA/principal-subspace optimization;
- data processing and distinguishability contraction;
- standard dephasing channels.

Candidate PDT novelty is the integrated rule:

\[
\boxed{
\text{resource-accessible distinction tensor }G_R
\xrightarrow{\text{spectral/algebra optimization}}
\mathcal P_R
}
\]

combined with

\[
\boxed{
\text{bit deficit }\chi_R
\xrightarrow{\text{exact semigroup embedding}}
\gamma_A=(\ln2)\chi_R/\tau_R
}
\]

and therefore

\[
\boxed{
\dot\rho
=-\frac{i}{\hbar}[H,\rho]
+\frac{\ln2}{\tau_R}\chi_R(\mathcal P_R\rho-\rho).
}
\]

The exact synthesis and its empirical laws require comprehensive literature review before a priority claim.

---

# 17. Current proof ledger

| Target | Result |
|---|---|
| Exact continuum embedding of \(2^{-\chi}\) retention | **PROVED** |
| Correct Akhtar rate | **PROVED: \(\gamma=(\ln2)\chi/\tau\)** |
| Discrete/continuous consistency | **PROVED** |
| CPTP semigroup for fixed conditional expectation | **PROVED / standard semigroup mathematics** |
| Exact zero-deficit quantum limit | **PROVED** |
| Additivity of hazard for independent deficits | **PROVED** |
| Existence of optimal \(k\)-dimensional distinction subspace | **PROVED via Ky Fan** |
| Generic uniqueness of spectral subspace | **PROVED when \(\lambda_k>\lambda_{k+1}\)** |
| Reversible covariance of selector | **PROVED under covariant \(G_R\)** |
| Explicit qubit \(\mathcal P_R\) | **PROVED** |
| Generic uniqueness of qubit dephasing algebra | **PROVED for nondegenerate top eigenvalue** |
| Higher-dimensional physical \(\mathcal P_R\) existence | **PROVED under closed algebra-size budget formulation** |
| Higher-dimensional uniqueness | **FALSE in general; degeneracy counterpossibility retained** |
| Closed-form qutrit optimizer for arbitrary \(G_R\) | **OPEN computational problem, not a logical gap** |
| Operational estimation of \(G_R\) | **REQUIRES experimental protocol** |
| Operational estimation of \(\chi_R\), \(\tau_R\) without fitting decay | **REQUIRES experimental protocol** |
| Nature obeys AE-v2 | **OPEN / empirical** |

---

# 18. Strongest defensible statement

The Akhtar Equation v2 is now mathematically sharper than v1: the resource-loss rate is no longer an arbitrary conversion of a discrete loss fraction into a derivative. It is uniquely fixed by exact semigroup embedding of the bit-retention law, while the physically retained sector is selected by a resource-accessible quadratic distinction tensor and, in finite-dimensional quantum systems, by trace-preserving conditional expectations onto optimal physical subalgebras.

The remaining work is experimental operationalization, not another algebraic patch: define and estimate \(G_R\), \(\chi_R\), and \(\tau_R\) independently, then test the predicted axis and bit-retention law.