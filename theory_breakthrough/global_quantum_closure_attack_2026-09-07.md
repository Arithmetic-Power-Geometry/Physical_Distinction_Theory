# PDT Global Quantum Closure — Heavy Attack (2026-09-07)

## Purpose

This note attacks the final quantum-side gap after the elementary PDT rigidity result. The target is to close the chain from a PDT elementary generalized bit to all finite-dimensional complex quantum systems without hiding the remaining assumptions.

The strongest honest result is a **conditional completion theorem** plus a **no-go on deriving global closure from elementary axioms alone**.

---

## 1. What elementary PDT already gives

Under the elementary assumptions already isolated in the repository — binary rank, Complete Distinction Sufficiency (CDS), unbiased erasure/common neutral state, and continuous reversible pure-state transitivity — the centered elementary state space is an ellipsoid and hence affinely a Euclidean ball

\[
\Omega_{\rm elem}\simeq B^n.
\]

Therefore a quadratic distinction form exists and the parallelogram identity/BQDC follows. With local tomography and genuine continuous reversible interaction, the established Masanes–Müller–Pérez-García–Augusiak classification selects

\[
 n=3,
\]

so the elementary nonclassical system is the Bloch ball/qubit.

This does **not** determine every higher-rank state space. A theory can contain a qubit sector plus additional unrelated admissible systems unless one imposes a principle tying all faces/ranks to the same distinction structure. Thus the implication

\[
\text{qubit exists}\Rightarrow\text{all systems are complex quantum}
\]

is false without global structure.

---

## 2. No-go: elementary closure does not imply global closure

### Proposition (Elementary-to-global underdetermination)

Let a probabilistic theory contain at least one system satisfying all elementary PDT axioms and yielding a qubit state space. Unless the axioms constrain every other system and every face/composite, one may enlarge the theory by adjoining an independent finite-dimensional convex operational model with its own admissible effects and transformations. The elementary qubit sector remains unchanged.

Hence

\[
\boxed{
\text{elementary PDT reconstruction alone}
\not\Rightarrow
\text{global complex quantum theory}.
}
\]

### Proof

Take the original theory T containing the reconstructed qubit Q. Form a disjoint operational extension T' by adjoining another system X and closing only under the declared product operations. None of the state/effect/transformation data of Q changes. Therefore every elementary theorem about Q remains true, while X can fail spectrality, strong symmetry, Jordan structure, or subspace closure. Consequently no theorem stated only about Q can determine X. QED.

### Consequence

A genuinely global principle is logically necessary. This is not a technical gap that can be removed by more algebra on the qubit alone.

---

## 3. PDT-native global principle: Recursive Distinction Closure (RDC)

We introduce the following operational condition.

### RDC-1 — Sharp face closure

For every physically realizable sharp distinction outcome e, the normalized exposed face

\[
F_e=\{\omega:e(\omega)=1\}
\]

is itself a physically realizable subsystem with inherited states, effects, reversible transformations, and resource accounting.

### RDC-2 — Recursive binary refinement

Every non-singleton physical face F admits a sharp binary distinction that splits F into two nonempty perfectly distinguishable exposed subfaces F_0 and F_1 such that every state \(\omega\in F\) has a decomposition

\[
\omega=p\,\omega_1+(1-p)\,\omega_0,
\qquad
\omega_i\in F_i,
\qquad 0\le p\le1.
\]

The same property holds recursively inside F_0 and F_1.

### RDC-3 — Finite termination

For every finite-dimensional system the recursion terminates after finitely many steps at singleton pure-state faces.

### RDC-4 — Frame reversible equivalence

For any two ordered frames of N perfectly distinguishable pure states,

\[
(\alpha_1,\ldots,\alpha_N),\qquad(\beta_1,\ldots,\beta_N),
\]

there exists a reversible transformation g with

\[
g\alpha_i=\beta_i\quad\forall i.
\]

RDC-4 is the global-rank extension of the earlier reversible equivalence principle for elementary distinctions.

---

## 4. New theorem: RDC implies spectrality

### Theorem (Recursive Distinction Spectrality)

In a finite-dimensional operational state space satisfying RDC-1, RDC-2 and RDC-3, every state is a convex combination of a finite set of perfectly distinguishable pure states.

Equivalently, the state space is spectral in the GPT sense.

### Proof

Proceed by induction on the finite recursion depth d(F) of a face F.

**Base case d(F)=0.** By RDC-3, F is a singleton pure-state face, so every state in F is trivially a convex combination of one pure state.

**Induction step.** Assume the statement holds for every face of depth at most d-1. Let F have depth d and let \(\omega\in F\). By RDC-2 there is a sharp binary split into perfectly distinguishable faces F_0,F_1 and

\[
\omega=p\omega_1+(1-p)\omega_0.
\]

By induction,

\[
\omega_1=\sum_i a_i\alpha_i,
\qquad
\omega_0=\sum_j b_j\beta_j,
\]

where each \(\{\alpha_i\}\subset F_1\) and \(\{\beta_j\}\subset F_0\) is a perfectly distinguishable pure frame inside its face.

Because F_0 and F_1 are perfectly distinguished by the parent sharp test, any pure state in F_0 is perfectly distinguishable from any pure state in F_1. Combining the child tests conditionally with the parent test yields one measurement that distinguishes the union

\[
\{\alpha_i\}_i\cup\{\beta_j\}_j.
\]

Therefore

\[
\omega=\sum_i pa_i\alpha_i+\sum_j(1-p)b_j\beta_j
\]

is a convex decomposition into perfectly distinguishable pure states. QED.

### Significance

RDC is stronger than elementary CDS but is operationally recursive rather than geometric: it does not mention Hilbert spaces, Jordan products, amplitudes, or quadratic norms. Spectrality is now a theorem from the recursive distinction process, not an independent mathematical postulate.

---

## 5. New theorem: RDC-4 gives strong symmetry

### Theorem (Frame Equivalence = Strong Symmetry)

RDC-4 implies that the reversible affine automorphism group acts transitively on ordered perfectly distinguishable frames of each fixed cardinality. This is exactly strong symmetry as used in the Barnum–Hilgert classification.

Hence

\[
\boxed{
\text{RDC} \Rightarrow \text{spectrality + strong symmetry}.
}
\]

---

## 6. Imported rigidity theorem: Euclidean Jordan structure

Barnum and Hilgert prove that finite-dimensional compact convex state spaces that are both spectral and strongly symmetric are precisely simplices or normalized state spaces of simple Euclidean Jordan algebras.

Therefore, for every irreducible nonclassical PDT system satisfying RDC,

\[
\boxed{
\Omega_A\text{ is a simple Euclidean Jordan state space}.
}
\]

The simplex branch represents classical systems. The nonclassical elementary rank-two branch already contains the PDT qubit selected by the Euclidean-ball interaction theorem.

This Jordan classification is established mathematics and is not claimed as a new PDT theorem.

---

## 7. Composite closure principle

For systems A and B impose:

1. product preparations and product effects exist;
2. no-signalling;
3. local tomography: joint states are determined by joint local statistics;
4. reversible local dynamics embed faithfully;
5. the self-dualizing inner product on composites factorizes on product elements;
6. at least one system is the reconstructed qubit;
7. composites remain inside the same RDC/Jordan class.

These conditions are the operational content needed by the Hanche-Olsen/Barnum–Wilce route.

---

## 8. Imported complex-selection theorem

Barnum and Wilce, using Hanche-Olsen's theorem, show that under suitable composite assumptions, a non-signalling theory whose individual systems are Euclidean Jordan algebras, whose composites are locally tomographic, and which contains a qubit is forced into finite-dimensional complex quantum theory, up to superselection/direct-sum structure.

Thus

\[
\boxed{
\text{RDC}
+\text{locally tomographic Jordan composites}
+\text{qubit}
\Rightarrow
\text{finite-dimensional complex C* structure}.
}
\]

Again, this implication uses an imported theorem.

---

## 9. Removing superselection for irreducible PDT systems

A finite-dimensional complex C*-algebra has the form

\[
\mathcal A\cong\bigoplus_k M_{d_k}(\mathbb C).
\]

Suppose PDT additionally requires **continuous reversible pure-state transitivity** for every irreducible system.

Pure states supported in different direct-sum blocks lie in disconnected superselection sectors. The identity component of the reversible group cannot continuously move a pure state from one central block to another because central projections are discrete invariants. Therefore continuous pure-state transitivity is incompatible with more than one nonzero block.

Hence every irreducible nonclassical system has

\[
\boxed{
\mathcal A\cong M_d(\mathbb C)
}
\]

and normalized states are exactly

\[
\boxed{
\rho\ge0,\qquad \operatorname{Tr}\rho=1.
}
\]

This removes superselection at the irreducible-system level. Classical systems may remain simplices, and reducible systems may be assembled explicitly as classical direct sums if desired.

---

## 10. Born rule and dynamics after closure

Once the state/effect spaces are those of complex matrix algebras, normalized affine positive effects have the form

\[
0\le E\le I,
\]

and probabilities are

\[
\boxed{p(E|\rho)=\operatorname{Tr}(\rho E)}.
\]

For a pure state \(\rho=|\psi\rangle\langle\psi|\) and rank-one effect \(E_i=|i\rangle\langle i|\),

\[
\boxed{p_i=|\langle i|\psi\rangle|^2}.
\]

Thus the Born rule is an ordinary consequence of the reconstructed complex state/effect pairing.

Continuous connected reversible dynamics on \(M_d(\mathbb C)\) are implemented by unitary conjugations (up to the standard antiunitary/disconnected alternatives). For a differentiable one-parameter connected group,

\[
U(t)=e^{-iHt/\hbar},
\]

so

\[
\boxed{i\hbar\dot\psi=H\psi}.
\]

These are standard consequences, not PDT-original theorems.

---

## 11. Complete quantum-side closure theorem

### PDT Conditional Quantum Closure Theorem

Consider a finite-dimensional non-signalling operational theory satisfying:

- resource-bounded physical realizability;
- elementary CDS and continuous reversible pure-state transitivity;
- RDC-1 through RDC-4 for all finite-dimensional faces/systems;
- local tomography and compatible product composition;
- factorization of the self-dualizing composite pairing;
- existence of genuine continuous reversible interaction for elementary systems.

Then:

1. elementary systems are Euclidean balls;
2. genuine interacting locally tomographic elementary composites select the three-dimensional Bloch ball;
3. RDC implies spectrality;
4. RDC-4 implies strong symmetry;
5. Barnum–Hilgert then gives Euclidean Jordan state spaces (or simplices);
6. the qubit plus locally tomographic compatible Jordan composites triggers the Hanche-Olsen/Barnum–Wilce complex-selection theorem;
7. continuous pure-state transitivity removes nontrivial direct-sum superselection in irreducible nonclassical systems;
8. every irreducible nonclassical system is therefore \(M_d(\mathbb C)_{\rm sa}\) with density matrices, POVM effects, trace-rule probabilities and connected unitary dynamics.

Symbolically,

\[
\boxed{
\text{PDT elementary distinction}
+\text{RDC}
+\text{composition}
\Longrightarrow
\text{finite-dimensional complex QM}
}
\]

**with the Jordan and complex-selection steps explicitly imported from established reconstruction theorems.**

---

## 12. What has actually been closed

### Closed by PDT-native proof in this attack

- elementary axioms alone cannot determine arbitrary higher-rank systems;
- recursive binary face resolution implies spectrality by induction;
- frame reversible equivalence implies strong symmetry;
- connected pure-state transitivity eliminates nontrivial direct-sum superselection after complex C*-structure is obtained.

### Closed conditionally using established theorems

- spectrality + strong symmetry -> Euclidean Jordan state spaces;
- qubit + suitable locally tomographic Jordan composites -> complex finite-dimensional quantum theory;
- Born trace rule and unitary/Schrodinger dynamics then follow in the standard representation.

### Still not derivable from the original scalar capacity alone

RDC itself is not a consequence of the scalar maximum codebook capacity \(\mathscr K_\epsilon\). The earlier l_p-ball/no-go logic already shows that scalar capacity cannot encode all local face geometry. Thus a global recursive principle or an equivalent state-resolved structural condition is logically necessary unless a deeper new primitive is introduced.

---

## 13. Breakthrough-status firewall

The scientifically defensible strong claim is now:

> PDT supplies a new distinction-centered upstream route to elementary Euclidean geometry and BQDC, proves a recursive distinction-resolution theorem yielding spectrality, and connects that structure to established Jordan/composite reconstruction theorems to obtain finite-dimensional complex quantum mechanics under explicit global closure assumptions.

Do **not** claim:

- scalar one-bit capacity alone derives quantum mechanics;
- Barnum–Hilgert, Hanche-Olsen, Barnum–Wilce, or Masanes et al. are PDT results;
- the complex field is selected without composite assumptions;
- gravity has been independently derived without thermodynamic calibration/equilibrium assumptions.

---

## 14. Final compact chain

\[
\boxed{
\mathscr K_\epsilon\text{-based physical distinctions}
+\text{CDS}
+\text{reversible symmetry}
}
\]

\[
\Downarrow
\]

\[
\boxed{B^n\ \text{and BQDC}}
\]

\[
\Downarrow\quad\text{(local tomography + interaction)}
\]

\[
\boxed{B^3=\text{qubit}}
\]

and globally

\[
\boxed{\text{RDC}\Rightarrow\text{spectrality + strong symmetry}}
\]

\[
\Downarrow\quad\text{(Barnum--Hilgert)}
\]

\[
\boxed{\text{Euclidean Jordan systems}}
\]

\[
\Downarrow\quad\text{(qubit + local tomography + compatible composites)}
\]

\[
\boxed{\mathbb C\text{-QM}}
\]

\[
\Downarrow
\]

\[
\boxed{p(E|\rho)=\operatorname{Tr}(\rho E),\quad U(t)=e^{-iHt/\hbar}}.
\]

This is the current strongest complete quantum-side theorem architecture that does not hide logical gaps.