# Cycle 238 — No-signalling is not a PDT composition selector

## Target
PDT-II (1): test whether positivity + normalization + fixed local state spaces + no-signalling can supply the missing PDT-native joint-admissibility predicate/composition law.

## Exact hypothesis under test
For a bipartite operational model with binary settings x,y in {0,1}, output alphabet Z_n, fixed uniform local marginals, positivity and normalization, suppose no-signalling is imposed. Candidate claim: these conditions uniquely determine the physical joint/composite probabilities.

## Decisive counterexample
Define, for every finite n>=1,

P_prod(a,b|x,y)=1/n^2,

and

P_mod(a,b|x,y)=1/n when b-a = xy (mod n), and 0 otherwise.

Both are normalized and positive. Both have exactly uniform marginals P(a|x)=P(b|y)=1/n, hence are exactly no-signalling. For n>=2 they are distinct. For the operational event W=[b-a=xy mod n],

P_prod(W)=1/n, while P_mod(W)=1.

Thus identical local state data plus no-signalling leave multiple inequivalent joint probability models. The smallest nondegenerate witness is n=2. n=1 collapses to the unique trivial box.

## Dimension stress test
`cycle238_nonsignalling_composition_no_go.py` uses exact `fractions.Fraction` arithmetic and checks normalization, positivity, no-signalling, identical local marginals and the separating event for every n=1,...,12. The formulas prove the same result for every finite n>=2, so no randomized extrapolation is required for this family.

## Consequences
1. **Composition law:** no-signalling is a necessary compatibility condition in many operational frameworks but is not a unique composition selector.
2. **n=3:** the construction exists uniformly for every n>=2, so no-signalling cannot non-circularly select n=3.
3. **Same-input PDT/QM prediction:** declaring P_mod to be PDT and P_prod (or a quantum completion) to be the comparator does not establish a same-input prediction unless PDT independently derives an additional physical joint-admissibility rule that selects its joint model from the same microscopic preparation and resource window.
4. **Experimentally distinctive inequality:** a violation relative to a narrower theory is meaningful only after PDT independently derives its admissible correlation set. No-signalling alone supplies no PDT-specific bound.
5. **Gravity/capacity:** no gravity or capacity law follows from this result.

## Prior-art boundary
This obstruction is not PDT novelty. GPT literature explicitly admits nonunique composite constructions, including minimal/maximal tensor structures; no-signalling correlations and channels are established operational/GPT subjects. Relevant prior-art checks include Janotta & Lal, Phys. Rev. A 87, 052131 (2013), on GPT composites without the no-restriction hypothesis, and Cavalcanti et al., J. Phys. A 55, 404001 (2022), on non-signalling channels in locally tomographic GPTs. Quantum channel marginal compatibility is likewise an established problem (Hsieh et al., Phys. Rev. Research 4, 013249, 2022).

## Status ledger
- Claim “no-signalling uniquely selects PDT composition”: **FALSIFIED**.
- Counterexample and all-n finite extension: **PROVED**.
- No-signalling/GPT composite framework: **IMPORTED/KNOWN**.
- PDT-native composition selector: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input quantitative PDT != QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Strongest surviving obligation
Derive from PDT primitives an additional *joint* physical admissibility condition J_PDT(A,B,R) that is stronger than positivity + normalization + local consistency + no-signalling, then prove it is not merely an existing GPT tensor-cone, causal-compatibility, marginal-extension, information-principle, or resource-theory constraint. Only after that derivation is it legitimate to ask whether the resulting set yields a same-input quantitative separation from quantum theory.
