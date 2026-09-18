# Cycle 242 — Wiring/operational closure does not determine PDT composition

## Target attacked
PDT-II target (1), with consequences for (2), (3), and (5): can the missing PDT-native joint-admissibility/composition rule be obtained by requiring closure under physically natural classical post-processing, composition, post-selection, and wirings?

## Candidate principle
Let C be the admissible family of multipartite input-output correlations. Require C to be closed under classical operations: relabelling/coarse-graining of inputs and outputs, shared randomness/convex mixing, parallel composition, post-selection where defined, and causal wirings in which later local inputs may depend on earlier local outputs.

This is physically motivated as a consistency requirement: admissible resources should not generate an inadmissible resource by free classical processing.

## Result
**FALSIFIED as a unique PDT composition selector. IMPORTED/KNOWN as a consistency principle.**

Closure under wirings constrains a *set* of admissible composites but does not uniquely select that set or a joint completion for fixed local data.

### Exact smallest witness
For every finite n >= 2 define two zero-input bipartite distributions

P_ind(a,b)=1/n^2,
P_corr(a,b)=delta[a=b]/n.

Both are classical/local, hence lie in the local set L. They have identical uniform marginals. Yet

P_ind[A=B]=1/n,
P_corr[A=B]=1.

The local set L is closed under classical wirings. Thus even imposing wiring closure leaves both physically distinct composites admissible. The obstruction already occurs at n=2 and embeds exactly for n=2,...,12 and every finite n>12. n=1 is degenerate.

More strongly, multiple distinct correlation theories are themselves closed under wirings/classical operations (including standard local, quantum and no-signalling families). Therefore closure is a consistency filter, not a unique composition axiom.

## Strong prior-art boundary: almost-quantum correlations
Navascues, Guryanova, Hoban & Acin, Nature Communications 6, 6288 (2015), introduced the almost-quantum set Q~. Their paper proves Q~ is stable under classical post-processing, including post-selection, grouping/composition and wirings, while Q~ strictly contains the quantum correlation set. It also satisfies several proposed physical/information principles (including Macroscopic Locality and Local Orthogonality, with evidence/analysis for others).

Allcock et al., Physical Review A 80, 062107 (2009), explicitly developed closed sets of nonlocal correlations and argued that physically consistent correlation sets should be closed under natural operations. Hence operational/wiring closure cannot be claimed as PDT-native novelty.

This creates a particularly sharp no-go boundary after Cycles 238–241: adding closure under classical operations to positivity, normalization, no-signalling and the previously audited information principles still does not by itself identify the quantum set, because a known strictly supra-quantum almost-quantum set survives these consistency demands.

## Same-input consequence
A purported PDT/QM prediction gap cannot be manufactured by selecting P_corr for PDT and P_ind for QM while declaring only their identical marginals as the input. Those are different global microscopic preparations. A valid comparison must fix the same global preparation, accessible operations/records and resource window on both sides.

Wiring closure supplies no probability rule that yields P_PDT(O|I,R) != P_QM(O|I,R) for such an identical fully specified input.

## n=3 consequence
Nothing in wiring closure privileges n=3. The exact obstruction is present for every n >= 2, so this principle cannot provide a non-circular PDT-native n=3 derivation.

## Surviving theorem/obligation
Any PDT-native composition law J_PDT must do more than require closure of the admissible family under free classical operations. It must independently derive which joint states/correlations are admissible from PDT primitives, and must be shown not to reduce to a known closed correlation set, GPT tensor construction, NPA/almost-quantum relaxation, or existing information-principle reconstruction.

## Status ledger
- Wiring/classical-processing closure as consistency requirement: **IMPORTED/KNOWN**.
- Wiring closure uniquely determines PDT composition: **FALSIFIED**.
- Wiring closure selects n=3: **FALSIFIED**.
- Exact n=2,...,12 witness: **PROVED** (analytic formula; no floating-point assumption).
- Extension to every finite n >= 2: **PROVED**.
- Same-input PDT != QM quantitative prediction from this principle: **OPEN / NOT DERIVED**.
- Experimentally distinctive PDT inequality from this principle: **OPEN / NOT DERIVED**.
- Gravity/capacity implication: **OPEN / NOT DERIVED**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Prior-art references
1. M. Navascues, Y. Guryanova, M. J. Hoban, A. Acin, “Almost quantum correlations,” Nature Communications 6, 6288 (2015), DOI: 10.1038/ncomms7288.
2. J. Allcock, N. Brunner, N. Linden, S. Popescu, P. Skrzypczyk, T. Vertesi, “Closed sets of nonlocal correlations,” Physical Review A 80, 062107 (2009), DOI: 10.1103/PhysRevA.80.062107.

## Research integrity note
No PDT novelty is claimed for wiring closure, closed correlation sets, almost-quantum correlations, or the general consistency requirement. No experimental deviation is claimed. This cycle records a no-go result and narrows the remaining PDT-II composition obligation.
