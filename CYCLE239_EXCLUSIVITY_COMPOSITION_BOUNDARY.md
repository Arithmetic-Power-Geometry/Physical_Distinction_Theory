# Cycle 239 — Exclusivity / Local-Orthogonality Composition Boundary

## Target
PDT-II priority (1): test whether adding event exclusivity / local orthogonality (LO) to positivity, normalization, local consistency and no-signalling can serve as a PDT-native joint-admissibility/composition selector.

## Candidate principle
For events e=(a_1...a_k|x_1...x_k), call e,e' locally exclusive when for at least one party i, x_i=x'_i but a_i != a'_i. Require for every pairwise locally-exclusive family C:

    sum_{e in C} P(e) <= 1.

A stronger copy-stable version requires the same after arbitrary finite independent composition and admissible wirings.

## Proof / falsification audit

### 1. Provenance
This candidate is not PDT-native. It is the established Local Orthogonality / Exclusivity principle. Fritz, Sainz, Augusiak, Brask, Chaves, Leverrier and Acin introduced LO as an intrinsically multipartite principle (Nature Communications 4, 2263, 2013; arXiv:1210.3018). They prove that single-copy LO is equivalent to no-signalling in bipartite Bell scenarios but becomes stricter for more than two parties; distributed copies of PR correlations can violate it. Follow-up work (Sainz et al., PRA 89, 032117, 2014) studies closure under wirings and further LO inequalities.

Therefore adopting LO/exclusivity as J_PDT would be IMPORTED/KNOWN, irrespective of whether PDT terminology rephrases local exclusivity as incompatible distinctions.

### 2. Non-uniqueness / selector failure
The established literature itself does not identify LO with the quantum set. Quantum correlations satisfy LO, while the LO constraints do not in general constitute a demonstrated unique reconstruction of all quantum composites. Hence:

    positivity + normalization + NS + LO

is not a proved unique PDT composition law.

At the bipartite single-copy level LO adds no restriction beyond NS, so Cycle 238's bipartite underdetermination is not repaired there.

### 3. Dimension audit n=1..12
Here n denotes local output alphabet size in the finite conditional-probability stress family.

- n=1: degenerate; no nontrivial distinction/exclusivity structure.
- n=2..12: ordinary independent/product local boxes are quantum/classical and hence satisfy LO. Correlated classical boxes with shared finite randomness also satisfy LO. Thus at every tested n >=2 there are multiple physically distinct admissible composites satisfying the candidate principle; LO cannot be a unique composition selector merely from local alphabet size.
- The same argument extends analytically to every finite n>=2: choose independent uniform variables versus a shared uniform variable. Both are classical (therefore quantum and LO-admissible), have the same uniform marginals, but different joint correlations.

Exact witness for every n>=2:

    P_ind(a,b)=1/n^2
    P_corr(a,b)=delta_{a,b}/n

Both have uniform marginals and satisfy all classical exclusivity constraints, while

    P_ind[a=b]=1/n
    P_corr[a=b]=1.

Thus even strengthening Cycle 238 by LO cannot select a unique joint state from the same local data.

### 4. n=3 obligation
The principle is dimension-uniform and the above multiplicity exists at n=3 as well as n=2,4,... . It therefore does not derive n=3. Any claim that multipartite LO is special because three parties are the first setting where it strengthens NS would confuse a threshold in party number with a derivation of physical state-space dimension/capacity three.

### 5. Same-input PDT-vs-QM prediction
LO is satisfied by quantum correlations. Importing it into PDT supplies no same-input probability deviation. Choosing different LO-admissible completions for PDT and QM would again change the global preparation/composite input and violates the same-input requirement.

## Status
- LO/exclusivity as PDT-native principle: **FALSIFIED** (provenance).
- LO/exclusivity mathematics: **IMPORTED/KNOWN**.
- Failure to uniquely select composition from same marginals: **PROVED** by the explicit independent/shared-randomness family.
- n=3 selection: **FALSIFIED** for this candidate.
- same-input PDT != QM prediction from this candidate: **OPEN / not obtained**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Smallest decisive witness
n=2. Uniform independent bits and perfectly correlated shared bits have identical local marginals and both are classical/LO-admissible, but P(A=B)=1/2 versus 1.

## Surviving strengthened obligation
A PDT-native J_PDT must constrain genuinely joint structure more strongly than positivity, normalization, no-signalling and established exclusivity/LO, while remaining independently derivable from PDT primitives. It must then be compared against existing contextuality/exclusivity graph principles, GPT tensor cones, causal compatibility, quantum extension/marginal constraints and information principles. No uniqueness or novelty claim is permitted until that comparison and adversarial search succeed.

## Prior-art references checked
1. T. Fritz et al., "Local orthogonality as a multipartite principle for quantum correlations," Nature Communications 4, 2263 (2013), DOI 10.1038/ncomms3263, arXiv:1210.3018.
2. A. B. Sainz et al., "Exploring the local orthogonality principle," Physical Review A 89, 032117 (2014), DOI 10.1103/PhysRevA.89.032117.
3. T. Gonda et al., "Almost Quantum Correlations are Inconsistent with Specker's Principle," Quantum 2, 87 (2018), DOI 10.22331/q-2018-08-27-87. This is a boundary warning: operational Specker principles and statistical consistent-exclusivity conditions must not be conflated.
