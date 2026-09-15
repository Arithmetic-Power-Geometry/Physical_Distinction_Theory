# Cycle 170 — Distinction geometry does not determine physical process cost

## Target attacked
Primary: (1) PDT-native composition law via a PDT-native operational cost functional/free-operation class. Secondary: (4) resource/revelation laws and (3)/(5) same-input quantitative predictions.

## Candidate principle
**Candidate C170:** the operational/thermodynamic cost of a distinction-processing map is determined by distinction geometry alone (the input/output operational partition and the logical map between their quotient classes).

Status: **FALSIFIED**.

## Exact hypotheses
Let a finite logical process be represented by a map `f : X -> Y` on operationally distinguishable records. A distinction-only cost rule is any rule `c_D(f)` whose value is fixed once the finite distinction structure `(X,Y,f)` is fixed, with no additional physical scale (temperature, Hamiltonian, clock rate, control restrictions, bath model, error tolerance, etc.).

The strongest simple test is one-bit reset, `r:{0,1}->{0}`. Its distinction geometry is identical in every implementation: two distinguishable inputs are merged into one output.

## Decisive counterexample
Implement the same reset map `r` quasistatically against two heat baths with temperatures `T1 != T2`. Landauer's lower bound for erasing one unbiased bit is

`W_min(T) >= k_B T ln 2`.

Therefore the same distinction map has different physical work floors:

`W_min(T1) / W_min(T2) = T1/T2`.

No function of `(X,Y,r)` alone can equal both values when `T1 != T2`.

This is already the smallest nontrivial logical witness: a two-to-one map on a binary record. No increase of dimension can repair the missing physical scale.

## Dimension stress family n=1..12 and beyond
For reset of `n` independent unbiased bits, the logical distinction map is `r_n:{0,1}^n->{0^n}`. At temperature T the standard quasistatic Landauer floor scales as

`W_min(n,T) >= n k_B T ln 2`.

For every `n=1,...,12`, choosing `T1 != T2` yields identical distinction geometry but unequal physical work floors. The same argument holds for every finite n.

This is an analytic stress test; no numerical approximation is needed.

## Stronger boundary
The falsification is stronger than a temperature example. Even logically reversible operations can require physical energy when implemented on processors with nondegenerate energy levels, and finite-time erasure costs depend on implementation details. Hence logical reversibility/irreversibility and distinction loss constrain physical cost but do not generally determine it uniquely.

## Surviving theorem
A distinction-only functional may still define an **abstract logical resource monotone**. For example, under a specified prior `p(x)`, the information discarded by a deterministic process can be quantified by conditional entropy `H(X|f(X))`. Such a quantity can enter thermodynamic lower bounds once a physical resource model is supplied. But converting it to work/energy requires additional physical data.

Thus the defensible architecture is two-layered:

1. PDT distinction layer: operational quotient, logical process, lost/revealed distinctions, abstract monotones.
2. Physical resource layer: temperature/Hamiltonian/bath/control/error/time assumptions mapping abstract distinction change to implementation cost.

The second layer cannot be derived from bare finite distinction geometry without an independent physical bridge principle.

## Consequence for PDT-II
The post-Cycle-169 route "derive the physical operational cost functional from distinction geometry itself" is too strong and is now falsified.

A valid PDT-native composition program must instead derive an **abstract distinction-processing preorder/cost** and separately state/derive a physical bridge. Any PDT-vs-QM prediction that inserts `k_B T`, energy, gravity, or capacity without such a bridge is IMPORTED/CONDITIONAL, not PDT-native.

This also blocks target (6): a gravity/capacity law cannot follow from bare distinction counts alone because dimensional physical scales are absent.

## Prior-art boundary
This cycle does not claim Landauer's principle or thermodynamic work-cost results as PDT novelty. Established information thermodynamics relates irreversible logical processing to thermodynamic work, while modern results explicitly depend on physical resource models. Quantum resource theories likewise require a declared set of free states/operations; the free-operation class is not fixed by a scalar resource label alone.

Relevant prior art checked in this cycle:
- Faist, Dupuis, Oppenheim & Renner, *The minimal work cost of information processing*, Nature Communications 6, 7669 (2015), DOI 10.1038/ncomms8669.
- Chiribella et al., *Fundamental Energy Requirement of Reversible Quantum Operations*, Physical Review X 11, 021014 (2021).
- Giorgini et al., *Thermodynamic cost of erasing information in finite time*, Physical Review Research 5, 023084 (2023).
- Zanoni & Scandolo, *Choi-defined resource theories*, Physical Review A 111, 062407 (2025).

## Classification
- Claim that bare distinction geometry uniquely fixes physical process cost: **FALSIFIED**.
- Binary reset counterexample and all-n temperature family: **PROVED** given the standard Landauer framework.
- Landauer/work-cost physics: **IMPORTED/KNOWN**.
- Abstract distinction-loss monotones as PDT bookkeeping: **CONDITIONAL** until PDT selects exact primitives and operational semantics.
- PDT-native physical bridge from distinction change to energy/work: **OPEN**.
- Same-input PDT != QM prediction: **OPEN**.
- PDT-native composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Gravity/capacity law: **OPEN** and blocked absent an independent physical bridge.

## Breakthrough gate
**BREAKTHROUGH CANDIDATE: NO.**

This is a decisive falsification/boundary result, not a positive breakthrough. It prevents a circular or dimensionally incomplete physical-cost derivation and narrows the next obligation to a PDT-native abstract process preorder plus an independently justified physical bridge.
