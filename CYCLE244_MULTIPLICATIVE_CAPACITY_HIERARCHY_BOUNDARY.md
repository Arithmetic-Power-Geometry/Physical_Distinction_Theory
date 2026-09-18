# Cycle 244 — Multiplicative capacity hierarchy boundary

## Target
Strongest unresolved PDT-II item: a PDT-native composition law, with the n=3 selector and same-input deviation as downstream obligations.

## Candidate hypotheses
Let N be a positive integer operational capacity and K(N) a positive integer state-parameter count. Test the structural package:

1. unit: K(1)=1;
2. strict subspace monotonicity: K(N+1)>K(N);
3. composite multiplicativity: K(N_A N_B)=K(N_A)K(N_B).

These are deliberately stronger than marginal consistency alone and are natural candidates for a distinction-capacity composition rule.

## Exact adversarial family
For every positive integer r define

K_r(N)=N^r.

Then exactly:

- K_r(1)=1;
- K_r(N+1)>K_r(N) for every N>=1;
- K_r(N_A N_B)=K_r(N_A)K_r(N_B).

Hence the hypotheses admit infinitely many mutually different laws. The repository regression program checks r=1,...,8 and N=1,...,12 exactly with Python integers, including all pairwise composites in that window. The analytic identity proves the result for all finite positive N and all r>=1.

## Consequences
**PROVED:** unit + strict subspace monotonicity + multiplicative composition do not uniquely determine K.

**FALSIFIED:** this structural package, by itself, is a unique PDT-native composition selector.

**FALSIFIED:** it cannot non-circularly select n=3. Every N, including N=3, belongs to every member of the hierarchy; nothing in the hypotheses privileges 3.

**OPEN:** a PDT-native extra principle that selects one member of a hierarchy (or a different composition law) without importing the desired result.

**OPEN:** same-input P_PDT != P_QM. Choosing a different exponent by stipulation is not a prediction; an independently derived operational probability rule and identical microscopic input/resource window remain required.

## Prior-art boundary
This route is not novel as stated. Hardy's 2001 reconstruction uses a subspace condition together with composite-system multiplicativity to obtain a power-law hierarchy K=N^r (positive integer r), and then requires additional axioms such as simplicity/continuity to select the quantum case. Later operational reconstructions likewise use information/tomographic locality plus further postulates. Therefore relabeling N or K as PDT distinction capacity would be IMPORTED/KNOWN, not a PDT breakthrough.

Primary references checked:
- L. Hardy, *Quantum Theory From Five Reasonable Axioms*, arXiv:quant-ph/0101012 (2001), especially the K=N^r derivation.
- L. Hardy, *Reformulating and Reconstructing Quantum Theory*, arXiv:1104.2066 (2011), operational postulates including information locality and tomographic locality.

## Status ledger
- Multiplicative-capacity uniqueness: **FALSIFIED**.
- Infinite power-law survivor family: **PROVED**.
- Provenance as a new PDT result: **IMPORTED/KNOWN boundary**.
- PDT-native composition law: **OPEN**.
- Non-circular n=3 derivation: **OPEN**.
- Same-input quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Do not add a simplicity/minimal-exponent axiom merely to force a preferred exponent: Hardy already uses such a selector. Search instead for a PDT-native operational constraint derived from distinction resources that (i) acts on joint admissibility, (ii) is not equivalent to known reconstruction axioms, and (iii) produces a falsifiable probability consequence under the same microscopic input.
