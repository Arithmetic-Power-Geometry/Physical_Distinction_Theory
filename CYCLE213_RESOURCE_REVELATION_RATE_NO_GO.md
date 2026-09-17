# Cycle 213 — Resource-to-revelation rate no-go

## Target
PDT-II target (4): determine whether increasing a scalar resource budget forces a quantitative rate of revelation of previously hidden distinctions.

## Definitions
Let X be a finite microscopic state set. At resource level R let A_R be the admissible observation family and define

x ~_R x' iff a(x)=a(x') for every a in A_R.

Let Pi_R be the induced partition and let

D(R) = #{ unordered pairs {x,x'} : x not~_R x' }.

Assume only resource nesting: R <= S implies A_R subseteq A_S.

## Theorem 213.1 — monotone distinction count [PROVED; elementary/known]
If A_R subseteq A_S, then ~_S subseteq ~_R and therefore D(S) >= D(R).

Proof. Any pair separated by an observation already in A_R remains separated after enlarging the family. Hence the set of separated pairs is nested. QED.

For a nested chain R_0 < ... < R_m there is the exact telescoping identity

D(R_m)-D(R_0) = sum_{j=1}^m [D(R_j)-D(R_{j-1})].

This is bookkeeping on a filtration/partition lattice, not a PDT-native conservation law.

## Theorem 213.2 — no universal positive revelation rate from scalar resource increments [PROVED NO-GO]
From nesting alone there is no universal c>0 such that

D(S)-D(R) >= c (S-R)

for every R<S.

Proof by decisive counterexample. Take X={0,1,2}. Let every admissible observation at every finite resource level factor through q with q(0)=q(1)=0 and q(2)=1. Enlarge A_R strictly with arbitrarily many distinct redundant functions of q as R increases. Then the resource/operation family grows strictly while Pi_R is constant and D(S)-D(R)=0 for all R<S. Thus every claimed c>0 fails. QED.

The same construction embeds in every finite |X|=n>=3 by leaving additional states separately labelled or dynamically inert.

## Stronger calibration obstruction [PROVED]
Even when a particular refinement occurs, its location on a scalar resource axis is not fixed by the operational partition chain. If phi is any strictly increasing reparameterization of R, the same nested family can be labelled by R'=phi(R). Therefore any numerical slope dD/dR, threshold R*, or inequality involving an absolute resource increment is representation-dependent unless PDT independently fixes the physical calibration and units of R.

Consequently a claimed universal resource-to-revelation coefficient cannot be derived from quotient nesting alone.

## Adversarial checks
- n=1,2: degenerate boundary cases recorded; no nontrivial three-state hidden-pair witness exists at n<3.
- n=3..12: exact finite embeddings preserve a permanently hidden pair under strictly growing redundant observation families.
- Degenerate dynamics: identity dynamics does not rescue a revelation rate.
- Nontrivial dynamics: choose F(0)=0,F(1)=1,F(2)=0; 0 and 1 are dynamically different but can remain observationally merged.
- Markovian/non-Markovian records: adding records that are measurable functions of the existing quotient cannot split its fibers.
- Pure/mixed or probabilistic preparations: post-processing the same quotient can enrich output alphabets without increasing microscopic separation.
- Norm choice: irrelevant to this combinatorial obstruction unless the norm is used to add a new calibrated accessibility axiom.

## Prior-art boundary [IMPORTED/KNOWN]
Monotonicity under enlarging an allowed measurement/operation class is standard operational/resource-theory structure. Restricted-measurement distinguishability and general resource theories already make distinguishability explicitly relative to the allowed class. The telescoping identity is elementary. Do not claim these as PDT inventions.

Relevant prior art checked in this cycle:
- Matthews, Wehner & Winter, *Distinguishability of Quantum States Under Restricted Families of Measurements with an Application to Quantum Data Hiding*.
- Takagi & Regula, *General Resource Theories in Quantum Mechanics and Beyond: Operational Characterization via Discrimination Tasks*, Phys. Rev. X 9, 031053 (2019).
- Piani, *Relative Entropy of Entanglement and Restricted Measurements*, Phys. Rev. Lett. 103, 160504 (2009).

## Status ledger
- Refinement monotonicity: **PROVED / IMPORTED-KNOWN boundary**.
- Exact increment telescoping: **PROVED / elementary**.
- Positive universal revelation rate from scalar resource growth alone: **FALSIFIED**.
- Absolute revelation threshold without independently calibrated resource variable: **FALSIFIED as a consequence of nesting alone**.
- PDT-native calibrated accessibility law: **OPEN**.
- PDT-native n=3 derivation: **OPEN**.
- Same-input PDT-vs-QM quantitative deviation: **OPEN**.
- Breakthrough candidate: **NO**.

## Consequence for PDT-II
The next viable target cannot be another monotonicity statement. PDT must derive a physically calibrated accessibility law tying a declared resource (energy, time, control precision, apparatus size, thermodynamic work, etc.) to a specific enlargement of the admissible observation/intervention algebra. Only then can a nonzero revelation rate, an n=3 threshold, or an experimentally distinctive inequality become falsifiable rather than coordinate-dependent.
