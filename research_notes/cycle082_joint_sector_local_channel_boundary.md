# Cycle 082 — Local-channel boundary of the quadratic joint sector

## Status

- **PROVED:** local-unitary invariance of the quadratic joint-sector energy.
- **PROVED:** monotonicity under local bistochastic (unital, trace-preserving) completely positive maps.
- **FALSIFIED:** monotonicity under arbitrary local CPTP maps.
- **IMPORTED/KNOWN:** the operator-norm mechanism is standard Hilbert–Schmidt/Kadison-Schwarz territory; related Hilbert–Schmidt correlation measures are known to fail monotonicity under local operations.
- **NUMERICALLY SUPPORTED:** regression audit through dimensions 1–12, with exact reset witnesses additionally frozen through 128.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Quantity under attack

For a bipartite state `rho_AB` on dimensions `d_A x d_B`, define

\[
J_{AB}=\rho_{AB}-\rho_A\otimes I_B/d_B-I_A/d_A\otimes\rho_B+I_{AB}/(d_A d_B),
\]

and

\[
C_{AB}=d_A d_B\,\mathrm{Tr}(J_{AB}^{\dagger}J_{AB}).
\]

Cycle 081 proved the exact local-plus-joint decomposition

\[
E_{AB}=E_A+E_B+C_{AB},\qquad E_d(\rho)=d\,\mathrm{Tr}(\rho^2)-1.
\]

The present cycle asks whether `C_AB` could serve as a physical correlation/resource quantity with a conservation or monotonicity law under local processing.

## The surviving theorem: bistochastic local contraction

Let `Phi_A` and `Phi_B` be unital, trace-preserving completely positive maps. Because they fix maximally mixed states and preserve partial traces in the required way,

\[
J'_{AB}=(\Phi_A\otimes\Phi_B)(J_{AB}).
\]

For a unital completely positive map, the Kadison-Schwarz inequality gives

\[
\Phi(X)^\dagger\Phi(X)\le \Phi(X^\dagger X).
\]

Taking the trace and using trace preservation yields

\[
\|\Phi(X)\|_2^2\le \|X\|_2^2.
\]

Therefore

\[
\boxed{C'_{AB}\le C_{AB}}
\]

for local bistochastic channels. Local unitaries saturate the inequality and hence leave `C_AB` invariant.

## Decisive falsification for arbitrary local CPTP maps

The statement fails as soon as nonunital local maps are allowed.

Take the maximally mixed product state

\[
\rho_{AB}=I_A/d_A\otimes I_B/d_B.
\]

Then

\[
J_{AB}=0,\qquad C_{AB}=0.
\]

Apply independent local reset channels sending every input state to fixed pure states `|0><0|`. The output remains a product state,

\[
\rho'_{AB}=|00\rangle\langle 00|.
\]

For a pure product state Cycle 081 gives

\[
C'_{AB}=E_AE_B=(d_A-1)(d_B-1).
\]

Thus, for every `d_A,d_B > 1`,

\[
\boxed{0=C_{AB}<C'_{AB}=(d_A-1)(d_B-1).}
\]

The smallest nontrivial witness is two qubits:

\[
\boxed{C:0\rightarrow 1}
\]

under purely local reset maps, with no correlation generated at any point.

This decisively falsifies the interpretation of `C_AB` as a correlation monotone or conserved correlation resource under arbitrary local operations. `C_AB` measures an orthogonal joint operator sector relative to maximally mixed local references; local nonunital bias can populate that sector even for product states.

## Strengthened surviving statement

The correct boundary is therefore:

\[
\boxed{\text{local unitary: invariant}}
\]

\[
\boxed{\text{local bistochastic CPTP: nonincreasing}}
\]

\[
\boxed{\text{general local CPTP: no monotonicity law}}
\]

Any PDT-native resource interpretation must either (i) restrict free operations to a class preserving the reference structure, or (ii) replace `C_AB` with a quantity that subtracts local bias and satisfies an independently justified operational monotonicity principle.

## Numerical regression

The executable audit uses random dense bipartite states for dimensions `1..12` and local depolarizing channels. For these channels,

\[
C'=(\lambda_A\lambda_B)^2 C,
\]

which was verified in 28 dense cases with maximum numerical residual `5.551115123125783e-17` and zero monotonicity failures.

The exact reset witness was frozen for dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`,

with `C_after=(d-1)^2` in the equal-local-dimension case.

## Prior-art boundary

This result is not promoted as novel. The broader failure of Hilbert–Schmidt-based quantities to obey desirable monotonicity under local/open-system operations is established. Relevant examples include:

- X. Wang and S. G. Schirmer, *Contractivity of the Hilbert-Schmidt distance under open-system dynamics*, Physical Review A 79, 052326 (2009), which shows that Hilbert–Schmidt norm/distance is generally not contractive for open-system dynamics.
- M. Piani, *Problem with geometric discord*, Physical Review A 86, 034101 (2012), which demonstrates that Hilbert–Schmidt geometric discord can increase under trivial local reversible operations.
- F. M. Paula, T. R. de Oliveira, and M. S. Sarandy, *Geometric quantum discord through the Schatten 1-norm*, Physical Review A 87, 064101 (2013), emphasizing the monotonicity problem of the Hilbert–Schmidt 2-norm and contrasting it with the trace norm.

## PDT-II consequence

Cycle 082 closes one tempting path: the Cycle-081 nonnegative joint sector cannot itself be elevated to a universal PDT correlation conservation law. The next composition-law attack must target a genuinely operational quantity whose free-operation class is independently derived rather than selected merely to make Hilbert–Schmidt monotonicity hold.
