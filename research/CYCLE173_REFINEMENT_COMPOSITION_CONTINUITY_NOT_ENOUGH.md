# Cycle 173 — Refinement, composition and continuity do not select a PDT probability law

## Target
PDT-II targets (2) and (3): test whether adding refinement consistency, independent composition, and continuity to operational distinction structure yields a non-circular n=3 probability rule, and hence a same-input PDT-vs-QM prediction.

## Exact hypotheses tested
For each finite resolved outcome set X, a preparation supplies only the PDT distinction quotient plus whatever labels are already present in that quotient. A probability selector F_X returns a distribution on X. Candidate axioms are:
1. normalization and positivity;
2. covariance under relabeling of outcomes;
3. continuity in any continuous preparation parameters already supplied;
4. independent composition: for independently prepared systems, F_{X×Y}=F_X⊗F_Y;
5. coarse-graining/refinement consistency: probabilities of merged events are sums of probabilities of their resolved children.
No Hilbert inner product, amplitudes, squared amplitudes, density operator, Born rule, or preferred measure over distinction classes is imported.

## Theorem 173.1 — No selector from bare resolved distinctions
For every n>=2, including n=3, these axioms do not select probabilities from a bare maximally resolved distinction quotient unless extra preparation weights/geometry are supplied.

### Proof
A maximally resolved quotient on X={1,...,n} contains the event algebra but no preparation-dependent scalar assigning relative mass to singleton events. Coarse-graining consistency constrains a probability measure after singleton masses p_i are chosen: for A⊆X, P(A)=Σ_{i∈A}p_i. It does not choose the p_i. Continuity is vacuous on a discrete quotient absent additional continuous preparation data. Independent composition maps any chosen p on X and q on Y to p⊗q, but again does not select p or q. Relabeling covariance says only that relabeling preparation/outcome data relabels the probabilities. Thus the simplex Δ_{n-1} remains available. In particular Δ_2 remains at n=3. QED.

## Stronger symmetry boundary
If the *complete preparation* is itself invariant under the full S_n action, relabeling invariance forces p_i=1/n. This is conditional and does not solve generic preparations. If the stabilizer has k outcome orbits, probabilities are constant within each orbit but generically k-1 independent orbit masses remain.

## Refinement is bookkeeping, not a selection principle
Suppose a coarse event A is refined into disjoint children A_1,...,A_m. The equation P(A)=Σ_j P(A_j) is finite additivity. It propagates already-selected masses across resolutions. It cannot generate the child masses from the partition alone. Hence invoking refinement consistency as the missing PDT probability principle is circular unless PDT independently derives a measure/weight on distinctions.

## Composition is also insufficient
For arbitrary p∈Δ_{n-1} and q∈Δ_{m-1}, the product distribution p⊗q obeys normalization, positivity, continuity, relabeling covariance, and independent composition. Therefore composition preserves rather than removes the local freedom. Correlated composites enlarge the freedom further unless a correlation rule is independently supplied.

## n=1..12 stress test
- n=1: unique distribution (1), trivial.
- n=2: one free simplex parameter.
- n=3: two free simplex parameters; this is the decisive non-circular PDT-II n=3 obstruction.
- n=4,...,12: n-1 free simplex parameters.
The theorem is analytic for every finite n, so no numerical extrapolation is required.

## Edge/degenerate cases
- Completely coarse quotient: only the coarse event has probability 1; hidden fine masses are even less determined.
- Pure labels without a metric/overlap rule: naming a distinguished preparation does not determine probabilities for other outcomes.
- Mixed preparations: convex mixing is meaningful only after component probability assignments are defined; it does not create them.
- Markovian/non-Markovian dynamics: transition kernels/process tensors are additional dynamical data, not consequences of the static quotient.
- Alternative norms/reversible groups: unless they independently define an operational measure, they do not remove simplex freedom.
- Controlled environment: environmental records can change the operational quotient, but the resulting quotient still does not choose singleton masses.

## Same-input PDT-vs-QM consequence
No defensible P_PDT(O|I,R) != P_QM(O|I,R) follows from these axioms alone. Choosing a non-Born p from the surviving simplex would manufacture the discrepancy. A same-input prediction requires an independently motivated PDT-native preparation measure or probability functional, with explicit hypotheses that differ from quantum probability assumptions.

## n=3 prior-art boundary
Gleason's theorem shows why importing the quantum event geometry changes the problem: for Hilbert dimension >2, a countably additive probability measure on the projection lattice has the density-operator/Born form. Kochen-Specker/Gleason arguments likewise rely on Hilbert-space projection/orthogonality structure and contextual consistency. Therefore a purported PDT-native n=3 derivation that first assumes Hilbert rays/projectors plus orthogonal additivity is not non-circular PDT reconstruction; it has imported the decisive quantum geometry.

Prior art checked this cycle:
- Stanford Encyclopedia of Philosophy, Quantum Logic and Probability Theory, section on Gleason's theorem: dimension >2 projection-lattice probability measures have μ(P)=Tr(WP).
- Stanford Encyclopedia of Philosophy, Kochen-Specker Theorem: Gleason/KS constraints explicitly use Hilbert-space projectors/orthogonal triples and additivity.
- DeBrota, Fuchs & Stacey (2018), arXiv:1805.08721: probabilistic representations of the Born rule require additional quantum physical structure beyond bare probability theory.

## Counterexample catalogue
- C173-01: n=2, same resolved quotient, p=(1/2,1/2) versus p=(3/4,1/4); both extend additively to all coarse events.
- C173-02: n=3, same resolved quotient, p=(1/3,1/3,1/3) versus q=(1/2,1/3,1/6); both satisfy finite refinement additivity.
- C173-03: independent composite of either C173-02 assignment with any q; product composition is satisfied in both theories while local predictions remain different.
- C173-04: any n>=2, the full simplex provides a continuum of selectors compatible with the same bare quotient once no preparation symmetry fixes the masses.

## Status ledger
- Bare distinction quotient + refinement consistency uniquely selects probabilities: **FALSIFIED**.
- Adding independent composition and continuity fixes the selector: **FALSIFIED**.
- Full transitive symmetry of the complete preparation forces uniform probability: **PROVED / CONDITIONAL**.
- Non-circular PDT-native n=3 probability derivation from current bare distinction structure: **OPEN**; current tested route fails.
- Gleason/Born uniqueness after importing Hilbert projection geometry and orthogonal additivity: **IMPORTED/KNOWN**.
- Same-input quantitative PDT != QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Search PDT's existing primitives for a genuinely native preparation-dependent quantity that can serve as a measure on distinctions without importing Hilbert overlap or choosing arbitrary weights. Any candidate must first state why that quantity is physically fixed, then prove refinement/composition behavior, test n=2 and n=3 adversarially, and compare the resulting same-input rule against QM/GPT alternatives. If no such quantity exists in the current axioms, record that as an axiomatic blocker rather than manufacture one.