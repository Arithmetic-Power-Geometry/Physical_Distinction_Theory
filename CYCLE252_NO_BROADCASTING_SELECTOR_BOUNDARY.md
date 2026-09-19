# Cycle 252 — No-broadcasting selector boundary

## Candidate
Test whether a PDT-native prohibition on universal broadcasting of distinctions could (i) determine composition or (ii) non-circularly select n=3.

## Exact hypotheses
A theory has a state space S_n and an admissible bipartite composite. A broadcasting map B has both output marginals equal to the input state for every state in a target set. Candidate selector: universal broadcasting is impossible for a nonclassical distinction space.

## Prove-or-falsify result
**FALSIFIED as an n=3 selector.** For complex quantum theory, for every n>=2 choose rho0=|0><0| and rho+=|+><+| in a two-dimensional subspace. Their commutator is nonzero (squared Frobenius norm 1/2), hence the pair is not jointly broadcastable by the quantum no-broadcasting theorem. The same obstruction embeds unchanged in every n>=2. Therefore n=2 is already a decisive competitor to n=3.

**FALSIFIED as a unique composition selector.** Generalized no-broadcasting is not uniquely quantum: Barnum, Barrett, Leifer and Wilce proved it for essentially any nonclassical finite-dimensional probabilistic model satisfying no-signalling, including superquantum models. Thus the property does not identify a unique state cone or tensor/composition rule.

**Classical control.** Every finite classical simplex admits universal broadcasting via the copying channel i -> (i,i). For p=(p_i), the joint output has P(i,j)=p_i delta_ij and both marginals equal p exactly.

## Dimension stress
`experiments/cycle252_no_broadcasting_dimension_stress.py` checks n=1..12 using exact rational arithmetic. n=1 is degenerate. For every n>=2 the fixed |0>,|+> witness has ||[rho0,rho+]||_F^2=1/2. The construction analytically embeds in every higher finite n, so randomized higher-dimensional testing would add no evidential force to this exact counterfamily.

## Prior-art boundary
Barnum, Barrett, Leifer & Wilce, *Generalized No-Broadcasting Theorem*, Phys. Rev. Lett. 99, 240501 (2007), DOI 10.1103/PhysRevLett.99.240501: generalized no-broadcasting applies to essentially any nonclassical finite-dimensional probabilistic model satisfying no-signalling, including superquantum correlations. Earlier quantum no-broadcasting is also established prior art. Therefore rebranding no-broadcasting as PDT is not novelty.

## Status ledger
- Classical universal broadcasting: **PROVED** (explicit copying map).
- Quantum nonbroadcastable witness for every n>=2: **PROVED**, conditional on the standard quantum no-broadcasting theorem for the implication from noncommutation.
- No-broadcasting as unique n=3 selector: **FALSIFIED**; smallest nontrivial competitor n=2.
- No-broadcasting as unique composition selector: **FALSIFIED** by generalized probabilistic counterfamilies.
- Generalized no-broadcasting principle: **IMPORTED/KNOWN**.
- PDT-native composition law: **OPEN**.
- Same-input P_PDT != P_QM: **OPEN**.
- Experimentally distinctive PDT inequality: **OPEN**.
- Gravity/capacity law: **OPEN**; not imported.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving requirement
A viable PDT-II principle must constrain the admissible composite more strongly than generic nonclassicality/no-broadcasting and must generate a dimension-sensitive consequence from PDT primitives without encoding n=3 in its assumptions.
