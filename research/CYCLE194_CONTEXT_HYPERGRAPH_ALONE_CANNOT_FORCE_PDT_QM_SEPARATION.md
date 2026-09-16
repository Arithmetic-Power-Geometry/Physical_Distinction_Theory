# Cycle 194 — Context hypergraph alone cannot force a PDT–QM probability separation

## Target
PDT-II targets (2), (3), and (5): test the surviving proposal from Cycle 193 that a PDT resource-restricted context hypergraph might itself yield a non-circular n=3 law and a same-input probability/inequality distinct from quantum mechanics.

## Status
**PROVED (conditional no-go) / FALSIFIED (strong claim) / IMPORTED-KNOWN framework / OPEN (extra PDT selection principle)**

**BREAKTHROUGH CANDIDATE: NO.**

## Exact hypotheses
Let H=(V,E) be a finite context hypergraph. Vertices v in V are accessible elementary events/distinctions and hyperedges e in E are declared measurement contexts. A normalized probabilistic model is a map p:V->[0,1] satisfying

sum_{v in e} p(v)=1 for every e in E.

Assume PDT supplies only H, these normalization constraints, and the declared resource window that determines which vertices/contexts are present. No additional PDT-native response functional or state-selection axiom is assumed.

## Theorem 194.1 — hypergraph insufficiency
The context hypergraph and normalization equations alone cannot imply a strict same-input PDT–QM probability discrepancy.

### Proof
The constraints define a convex set G(H) of normalized probabilistic models. Whenever H admits a quantum realization (projectors/effects assigned to vertices and contexts with a density operator rho), the resulting Born model p_Q(v)=Tr(rho E_v) is an element of G(H). Therefore the structural axioms defining G(H) do not exclude p_Q. Hence they cannot logically entail p_PDT != p_Q for every admissible realization. To force a discrepancy PDT must add an independently motivated rule selecting a subset or a point of G(H) that excludes the relevant quantum model under the identical microscopic input and resource declaration. QED.

## Minimal n=3 witness
Take one qutrit context E={{1,2,3}}. Then

G(H)={p_i>=0, p_1+p_2+p_3=1},

the full 2-simplex. For every p in G(H), choose rho=diag(p_1,p_2,p_3) and E_i=|i><i|. Born's rule gives Tr(rho E_i)=p_i exactly. Thus even at n=3, context structure plus normalization does not produce a non-Born law or a same-input discrepancy.

This witness is deliberately stronger than a numerical test: it is an exact realization of every normalized distribution in the single-context model.

## Dimension stress test
For every n>=1, a single n-outcome context gives the simplex Delta_{n-1}. Every p in Delta_{n-1} has the diagonal quantum realization rho=diag(p_1,...,p_n) with standard basis projectors. Therefore the obstruction holds exactly for n=1,...,12 and all finite n. No random search can overturn this exact embedding.

## Degenerate and resource-restricted cases
- Removing outcomes/contexts does not by itself create a unique response law; it generally weakens constraints.
- Redundant contexts add no selection rule.
- Pure-state restrictions are extra structure and therefore cannot be silently imported as a consequence of H.
- Mixed states make the single-context embedding immediate.
- Different norms on a coordinate representation do not alter the normalization polytope unless a norm-dependent physical axiom is separately stated.
- Reversible relabeling groups preserve the no-go: permutations merely relabel the simplex coordinates.

## Composite boundary
For multiple parties/contexts, contextuality-scenario hypergraphs can support classical, quantum, and more general probabilistic model sets. The hypergraph is the scenario, not by itself a unique probability theory. Consequently discovering supraquantum points in G(H) would establish only that they are structurally allowed by the weak hypergraph constraints, not that PDT predicts them.

## Experimentally distinctive inequalities
An inequality separating a larger hypergraph model set from the quantum set is not automatically a PDT prediction. PDT must derive why its physical response lies on the non-quantum side for the same microscopic preparation, intervention, and resource window. Otherwise the quantum point remains an admissible PDT model under the current axioms.

## Prior-art boundary
Contextuality scenarios represented by hypergraphs and normalized probabilistic models are established prior art (Acin–Fritz–Leverrier–Sainz; Fritz–Leverrier–Sainz). Their framework explicitly distinguishes classical, quantum, and generalized probabilistic model sets on a common scenario. Multipartite composition of contextuality scenarios and Foulis–Randall-type products are also established. Therefore neither the hypergraph representation nor the existence of non-quantum normalized models is PDT novelty.

## Consequences for PDT-II
1. **Composition law:** OPEN. A context hypergraph still requires a justified physical composition rule; existing contextuality products cannot be relabeled PDT-native.
2. **Non-circular n=3 derivation:** FALSIFIED for the route 'n=3 context + normalization alone'. The qutrit simplex admits every diagonal Born distribution.
3. **Same-input PDT != QM:** FALSIFIED as a consequence of hypergraph+normalization alone.
4. **Resource revelation:** previous quotient results survive, but do not select probabilities.
5. **Distinctive inequalities:** OPEN only after a PDT-native selection/response principle is derived.
6. **Gravity/capacity:** untouched; no import permitted.

## Strongest surviving obligation
Derive or falsify an independently motivated PDT-native **selection functional** S(I,R,state,H) whose output is not freely replaceable by a Born-compatible point, and then test positivity, normalization, coarse-graining consistency, composition, reversible covariance, n=1..12 behavior, and same-input QM/GPT countermodels. Until such a functional exists, no experimental PDT–QM probability claim is defensible.
