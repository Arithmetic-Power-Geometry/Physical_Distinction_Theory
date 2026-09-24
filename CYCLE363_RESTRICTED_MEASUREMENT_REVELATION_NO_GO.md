# Cycle 363 — Restricted-measurement revelation is real but not a PDT selector

## Target attacked
PDT-II priorities (1)–(5), especially whether a resource window defined by admissible measurements can supply a PDT-native refinement/revelation law and then force either n=3 or a same-input PDT/QM probability gap.

## Exact hypotheses
Let M_R be the family of measurements available at resource window R. For equal-prior states rho,sigma define the operational bias

D_R(rho,sigma) = sup_{M in M_R} TV(p_M(.|rho),p_M(.|sigma)).

Assume resource refinement means M_R subseteq M_R'.

## Theorem 363.1 — nested-window revelation monotonicity
If M_R subseteq M_R', then

D_R(rho,sigma) <= D_R'(rho,sigma)

for every state pair.

### Proof
The supremum defining D_R is taken over a subset of the feasible measurements defining D_R'. Enlarging a feasible set cannot decrease its supremum. QED.

Classification: **PROVED**, but the structure is not PDT-native; restricted-measurement distinguishability norms are established prior art.

## Exact adversarial counterfamily against n=3
For every local complex Hilbert dimension n >= 2, embed

|Phi+> = (|00>+|11>)/sqrt(2),
|Phi-> = (|00>-|11>)/sqrt(2)

in C^n tensor C^n.

Take the restricted resource window R_comp to contain only the local computational-basis product measurement. Both states produce exactly the same classical distribution:

p(00)=p(11)=1/2,

with all other outcomes zero. Hence

D_Rcomp(Phi+,Phi-) = 0,
P_success(R_comp) = 1/2.

At the refined global window R_global, the two orthogonal projectors onto |Phi+> and |Phi-> are admissible, so

D_Rglobal(Phi+,Phi-) = 1,
P_success(R_global) = 1.

Therefore the exact revelation jump is 1/2 -> 1 for every n >= 2. It occurs already at n=2 and persists unchanged for n=3,4,... . There is no n=3 singularity.

The n=1 case is degenerate: the two-state construction collapses because there is only one local basis vector.

## Consequences
1. Resource refinement can reveal previously inaccessible distinctions without changing the microscopic input states.
2. This fact alone cannot select n=3: n=2 is a smallest decisive counterexample and the family embeds in every n >= 2.
3. This fact alone cannot produce P_PDT(O|I,R) != P_QM(O|I,R), because the entire probability change is already an ordinary quantum prediction once the measurement resource window is declared.
4. Merely replacing the trace norm by a restricted-measurement distinguishability norm is not PDT novelty.
5. A genuine PDT-II deviation must specify a PDT-native admissible-measurement/resource rule that excludes or weights operations differently from QM/GPT resource theories and yields a numerical outcome difference for identical I and R.

## Prior-art rejection
Matthews, Wehner and Winter, *Distinguishability of quantum states under restricted families of measurements with an application to quantum data hiding*, Communications in Mathematical Physics 291, 813–843 (2009), DOI 10.1007/s00220-009-0890-5, explicitly develops distinguishability norms induced by restricted measurement families, including local/LOCC/separable/PPT restrictions and data hiding. Later work extends the same program and GPT data-hiding comparisons. Therefore restricted-measurement revelation is **IMPORTED/KNOWN**, not a PDT breakthrough.

## Status ledger
- Nested measurement-window monotonicity: **PROVED**.
- Restricted-measurement distinguishability norms: **IMPORTED/KNOWN**.
- Exact Bell-phase revelation jump 1/2 -> 1: **PROVED**.
- Resource-window revelation => n=3: **FALSIFIED** (smallest nontrivial counterexample n=2).
- Restricted-measurement quotient => unique PDT composition: **FALSIFIED as an inference**.
- Restricted-measurement revelation => same-input PDT/QM deviation: **FALSIFIED as an inference**.
- PDT-native admissible-measurement selector producing a numerical non-QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest unresolved obligation
Do not spend further cycles rediscovering generic restricted-measurement monotonicity. The next candidate must add a genuinely PDT-native rule for which distinctions become physically admissible at a declared resource window, then be compared numerically against QM on the same microscopic input.