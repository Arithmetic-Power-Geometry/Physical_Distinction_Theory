# Cycle 236 — Local-resource additivity cannot select a PDT composite

## Target attacked
PDT-II target (1), with consequences for targets (2) and (3): can the missing PDT-native composition law be selected by requiring symmetric/extensive resource accounting from the local systems, e.g. a composite cost determined additively from local distinction/refinement costs?

## Candidate selector under test
Let local states/records A and B carry PDT resource values C(A), C(B). Suppose a proposed composite rule requires

    C_loc(AB) = C(A) + C(B)

and attempts to choose the physical joint/composite from local states plus this additive resource constraint. More generally, the same obstruction applies to any selector whose input depends only on the two marginals and functions of those marginals.

## Exact counterexample theorem
**Theorem (marginal-resource underdetermination).** For every finite alphabet size n >= 2, local marginals together with any collection of marginal-only resource functionals fail to determine a unique joint state.

**Proof.** It is enough to use the binary subalphabet {0,1}. Let A and B each be uniform. Consider

    P_ind(a,b) = 1/4 for all a,b in {0,1},

and

    P_corr(0,0)=P_corr(1,1)=1/2,
    P_corr(0,1)=P_corr(1,0)=0.

Both joints have exactly the same uniform marginals. Therefore every functional whose arguments are only the local marginals has exactly the same value on the two candidates, including C(A)+C(B), every norm of the local probability vectors, every local entropy, and every local distinction functional. Yet the joints are distinct: under P_ind, Pr[A=B]=1/2, while under P_corr, Pr[A=B]=1. Thus no selector based only on local resource data can choose uniquely between them. The witness embeds unchanged into every n >= 2 by assigning zero probability to symbols 2,...,n. QED.

## Requested dimension/edge stress test
- n=1: unique degenerate joint; obstruction absent for the trivial reason that no correlation degree of freedom exists.
- n=2..12: exact binary witness embeds verbatim; hence failure is exact in every requested nondegenerate dimension.
- all finite n>12: same embedding proves failure analytically, so randomized testing is unnecessary for this theorem.
- different local norms: irrelevant because the marginal vectors coincide exactly.
- convexification/mixed states: both witnesses are ordinary mixed classical states; convex mixtures provide a continuum of further indistinguishable-by-marginals completions.
- reversible relabellings: simultaneous alphabet permutations preserve the construction.
- composites: this is itself a composite-state obstruction.

## Quantum strengthening / same-input consequence
The obstruction is not specifically classical. In quantum theory, local reduced states need not uniquely determine the global state; this is the established quantum marginal problem. Therefore importing a rule such as “choose a joint from its marginals” cannot be advertised as PDT novelty without an additional independently derived physical selector.

For target (3), choosing P_corr for PDT and P_ind for the comparator would *not* be a same-input PDT-vs-QM prediction: it changes the microscopic joint input/correlation structure. A legitimate probability separation must hold after the same global preparation, environment/records, measurement and resource window are fixed.

## Prior-art boundary
The general fact that marginals need not determine a joint is standard probability/coupling theory; the quantum analogue is the quantum marginal problem. Hence the no-go itself is a defensible PDT design constraint, not a novelty claim.

## Classification
- “Local additive/extensive resource accounting uniquely selects the composite”: **FALSIFIED**.
- Marginal-resource underdetermination theorem above: **PROVED**.
- General marginal/coupling and quantum-marginal phenomenon: **IMPORTED/KNOWN**.
- PDT-native correlation/composition selector: **OPEN**.
- Non-circular n=3 derivation from this route: **FALSIFIED** (binary witness embeds for all n>=2).
- Same-input PDT-vs-QM probability difference from choosing different couplings: **FALSIFIED as a valid same-input comparison**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Stronger surviving obligation
A PDT composition law must constrain genuinely joint/correlation data, not merely local resource values. The next candidate must therefore derive, from PDT primitives and the declared resource window, an independent rule on admissible couplings/correlation tensors (or an operational joint test family). That rule must then be attacked against classical coupling/copula theory, quantum marginal constraints, GPT minimal/maximal tensor products, entanglement/resource monotones, and higher-order process constructions before any novelty claim.