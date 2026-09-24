# Cycle 368 — Rank-3 Jordan selector no-go

## Target
PDT-II targets (1) PDT-native composition and (2) a non-circular derivation of n=3.

## Candidate
Attempt to select rank 3 by combining distinction-state cones with homogeneous/self-dual (Jordan) geometry and a compositional closure requirement.

## Exact hypotheses tested
H1. Finite-dimensional ordered state spaces are homogeneous/self-dual, hence Jordan-algebraic under the standard Koecher–Vinberg route.
H2. The candidate physical dimension is identified with Jordan rank/capacity.
H3. Composite systems are required to exist non-signallingly and satisfy standard Jordan-composite consistency; stronger variants additionally require local tomography.
H4. No premise may explicitly assume rank 3 or the exceptional algebra H_3(O).

## Result
**FALSIFIED as an n=3 selector.**

Homogeneous/self-dual geometry does not isolate rank 3: the simple Euclidean Jordan families include H_n(R), H_n(C), and H_n(H) across arbitrarily many ranks (subject to their usual definitions), plus spin factors and the exceptional H_3(O). Thus rank 2 and rank 4 countermodels already defeat uniqueness of rank 3.

Adding composition does not rescue the selector. Known EJA-composite results sharply restrict exceptional factors: under the standard composite assumptions, no nonclassical composite exists with an exceptional factor except essentially classical partners. Conversely, imposing local tomography with Jordan structure and a qubit selects ordinary complex quantum structure under known reconstruction hypotheses, not rank 3. Hence composition pushes toward known complex-QM families rather than selecting n=3.

The exceptional H_3(O) route is circular for PDT-II: its rank 3 is part of the chosen algebra's definition/classification, not a consequence of a PDT-native distinction principle; moreover its compositional obstruction conflicts with target (1).

## Dimension audit n=1..12
For the complex Jordan family H_n(C), each n=1..12 is admissible as a single-system Jordan model, with real vector-space dimension n^2 and rank n. Therefore the candidate axioms have no n=3 singularity. Smallest decisive nontrivial countermodel: n=2. Higher-rank decisive countermodel: n=4.

## Prior-art boundary
- Barnum & Wilce, *Local tomography and the Jordan structure of quantum theory* (2014): Jordan structure + local tomography + a qubit, under stated composite assumptions, characterizes finite-dimensional complex quantum mechanics (with superselection qualifications), rather than dimension three.
- Barnum, Graydon & Wilce, *Composites and Categories of Euclidean Jordan Algebras*, Quantum 4, 359 (2020): exceptional Jordan factors are obstructed in the relevant non-signalling composite framework except for essentially classical partners; simple non-exceptional composites are strongly constrained by universal tensor products.
- Barnum, Ududec & van de Wetering (2023): homogeneity/pure-transitivity routes to self-duality/Jordan structure are already reconstruction prior art.

## Status ledger
- Homogeneous/self-dual -> Jordan structure: IMPORTED/KNOWN.
- Jordan rank/capacity = n identification: CONDITIONAL (model choice).
- Jordan structure -> n=3: FALSIFIED.
- Composition + Jordan structure -> n=3: FALSIFIED under tested hypotheses.
- Exceptional H_3(O) -> PDT-native n=3: FALSIFIED (circular/imported selector).
- Exceptional H_3(O) -> general nonclassical PDT composition: FALSIFIED under standard EJA-composite hypotheses.
- Same-input PDT/QM probability gap: OPEN; nothing in this candidate changes the Born probabilities for identical complex-QM inputs.
- BREAKTHROUGH CANDIDATE: NO.

## Surviving requirement
A viable PDT-II n=3 theorem must contain a genuinely PDT-native operational condition whose truth value changes between n=2, n=3 and n>=4, while remaining compatible with a nontrivial composite rule. Jordan classification or generic compositional consistency alone cannot provide that condition.
