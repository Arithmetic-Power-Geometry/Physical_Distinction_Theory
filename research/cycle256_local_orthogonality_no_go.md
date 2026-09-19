# Cycle 256 — Local-orthogonality / exclusivity selector no-go

## Target
Test whether a PDT-native exclusivity/local-orthogonality principle can (i) select n=3 non-circularly or (ii) uniquely determine composition.

## Hypotheses tested
For a Bell event e=(a_1...a_N|x_1...x_N), call e,e' locally orthogonal when for some party i, x_i=x'_i but a_i!=a'_i. Impose sum_{e in C} P(e)<=1 for every pairwise locally-orthogonal set C.

## Exact counterfamily
For every finite local Hilbert dimension n>=2, embed any qubit realization into span{|0>,|1>} subset C^n and extend every projector by zero (or by an arbitrary orthogonal complement completing the measurement). All probabilities of the embedded experiment are unchanged. Quantum correlations satisfy local orthogonality because mutually locally-orthogonal events correspond to orthogonal event projectors, whose sum is <= I.

Therefore LO/exclusivity is satisfied at n=2,3,... and cannot single out n=3. The smallest nontrivial decisive competitor is n=2.

Composition is also not fixed: LO constrains observable probability tables, not the underlying admissible composite state cone/tensor rule. In the bipartite scenario LO^1 is exactly no-signalling, so it is manifestly too weak there to reconstruct the quantum composite. Multipartite/copy consistency strengthens the constraint but published work explicitly reports a set still larger than the quantum set.

## Dimension stress
Analytic embedding covers all finite n>=2, hence n=2..12 without numerical approximation and all higher finite dimensions. n=1 is degenerate and cannot host the binary qubit witness.

## Prior-art boundary
Fritz, Sainz, Augusiak, Brask, Chaves, Leverrier & Acin, Nature Communications 4, 2263 (2013), introduced Local Orthogonality. They prove LO^1 equals no-signalling bipartitely, becomes stronger multipartitely, quantum correlations satisfy LO, and discuss that even the many-copy LO set remains strictly larger than the quantum set. Thus LO/exclusivity itself is IMPORTED/KNOWN and cannot be promoted as PDT-native novelty.

## Status
- Quantum LO in arbitrary finite n>=2: PROVED (standard projector argument; imported framework).
- n=3 selection from LO/exclusivity: FALSIFIED.
- Unique PDT composition from LO/exclusivity alone: FALSIFIED as stated.
- LO/exclusivity principle: IMPORTED/KNOWN.
- Same-input P_PDT != P_QM: OPEN.
- PDT-native experimentally distinctive inequality: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Surviving lesson
Any viable PDT-II selector must constrain more than event exclusivity/probability-table consistency. It must introduce a genuinely PDT-native cross-system structure that is not inherited unchanged by the qubit-subspace embedding in arbitrary n.
