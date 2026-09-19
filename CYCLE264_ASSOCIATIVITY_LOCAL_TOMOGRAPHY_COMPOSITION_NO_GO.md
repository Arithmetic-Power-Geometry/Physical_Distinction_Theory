# Cycle 264 — Associativity + local tomography + multiplicative capacity do not determine PDT composition

## Target attacked
PDT-II (1) PDT-native composition law, with consequences for (2) a non-circular n=3 derivation.

## Status

- **PROVED:** Associativity, symmetric product composition, local tomography, and multiplicative finite capacity do not uniquely determine a composite theory.
- **FALSIFIED:** The claim that those properties alone force complex-quantum tensor composition.
- **FALSIFIED:** Any n=3 selector based only on those dimension-uniform composition properties.
- **IMPORTED/KNOWN:** Local tomography and dimension/capacity multiplicativity are standard reconstruction/GPT constraints; they are not PDT-native by themselves.
- **OPEN:** A genuinely PDT-native cross-system selector that distinguishes competing composites.
- **OPEN:** Same-input quantitative PDT/QM deviation after an explicit operational primitive is changed.

## Exact hypotheses
Let a finite system A have an unnormalised real state-space dimension K(A) and distinguishable-state capacity N(A). Consider the candidate package H:

1. composites exist symmetrically and associatively;
2. product preparations/effects exist;
3. composites are locally tomographic, so joint states are fixed by product-effect statistics;
4. K(AB)=K(A)K(B);
5. N(AB)=N(A)N(B).

Candidate claim: H uniquely fixes the composite rule relevant to PDT (in particular the complex-quantum tensor product), or supplies a route to n=3.

## Countermodels
### Classical finite probability theory
For an N-level classical system, states form the simplex Delta_N. The unnormalised vector-space dimension is K=N. The standard Cartesian/product sample-space composite has

K(AB)=N_A N_B=K(A)K(B),
N(AB)=N_A N_B,

and is symmetric, associative and locally tomographic.

### Finite-dimensional complex quantum theory
For a d-level complex quantum system, Hermitian operators form a real vector space of dimension K=d^2 and N=d. The usual Hilbert tensor product gives

K(AB)=(d_A d_B)^2=K(A)K(B),
N(AB)=d_A d_B=N(A)N(B),

and is symmetric, associative and locally tomographic.

These theories are inequivalent already for N=d=2: the classical bit has a line-segment normalized state space with two pure states, while the qubit has the Bloch ball with a continuum of pure states. Their reversible groups, effect geometries and attainable correlations differ. Therefore H cannot uniquely determine the complex-quantum composite rule.

This is a decisive counterexample because both theories satisfy every hypothesis H while giving inequivalent state/effect/composite structures.

## Dimension stress test n=1,...,12
For every n in {1,...,12}:

- classical: K=n, and two-copy K_2=n^2; N_2=n^2;
- complex quantum: K=n^2, and two-copy K_2=n^4=(n^2)^2; N_2=n^2.

Thus the candidate equations hold identically at every tested n. Nothing singular occurs at n=3. The same algebra proves the statement for every finite n, so randomized higher-dimensional testing is unnecessary for this candidate.

Degenerate n=1 is correctly included: both theories collapse to the trivial one-state system, so it cannot distinguish the models.

## Why this matters for PDT
Composition constraints that mention only associativity, local tomography and scalar multiplicativity are too coarse. They constrain bookkeeping dimensions but do not specify the geometry of the state cone, effect cone, reversible transformations, or nonlocal correlations. PDT therefore needs an additional cross-system distinction principle with operational content beyond these standard constraints.

A useful search filter follows: reject any proposed PDT composition theorem whose hypotheses are satisfied simultaneously by classical simplices and complex quantum state spaces unless an additional PDT-native hypothesis separates them.

## Prior-art boundary
Local tomography and multiplicative state-space dimension are established reconstruction/GPT ideas. This cycle does **not** claim novelty for them. The contribution of this cycle is only the explicit no-go application to the current PDT-II search: these ingredients cannot, by themselves, close the composition target or select n=3.

Relevant established reconstruction context includes Hardy's probabilistic reconstruction programme and subsequent GPT reconstructions. The no-go here is elementary and does not depend on a novelty claim.

## Same-input prediction consequence
No new P_PDT != P_QM prediction is asserted. Until PDT specifies a primitive (state set, effect set, dynamics, composition, probability rule, or resource admissibility) that differs operationally from QM, manufacturing a numerical deviation would be circular or fabricated.

## Breakthrough gate
**BREAKTHROUGH CANDIDATE: NO.** This is a decisive pruning/falsification result, not a new physical law.
