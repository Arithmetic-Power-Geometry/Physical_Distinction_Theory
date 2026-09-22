# PDT-II Cycle 321 — Purification selector route

## Target
Test whether adding purification to the surviving PDT-II operational/compositional desiderata supplies a PDT-native composition law, a non-circular n=3 selector, or a same-input deviation from quantum mechanics.

## Candidate principle
Every mixed state has a purification, unique up to reversible transformations on the purifying system.

## Prior-art audit
This principle is not PDT-native. Chiribella, D'Ariano and Perinotti (Phys. Rev. A 81, 062348; arXiv:0908.1583) developed probabilistic theories with purification and derived a large family of quantum-like operational consequences. Operational reconstructions of finite-dimensional quantum theory also use purification together with additional axioms. Galley and Masanes, Quantum 2, 104 (2018), show within their classified alternatives to the quantum measurement postulates that modifications of the Born rule violate purification and local tomography.

## Prove-or-falsify assessment

### Claim A
`Purification alone => unique PDT composite law.`

**Status: FALSIFIED as a PDT-native uniqueness route.**

Reason: purification is an established operational axiom and its known consequences do not by themselves constitute a new PDT composition rule. Existing reconstructions require additional structural assumptions/axioms to recover finite-dimensional complex quantum theory. Importing the full reconstruction package would import the desired composite theory rather than derive it from PDT.

### Claim B
`Purification => physical n=3.`

**Status: FALSIFIED as an inference.**

Reason: purification is formulated independently of a distinguished spatial dimension or outcome arity. Quantum systems of arbitrary finite Hilbert dimension admit purification. Therefore the principle cannot single out n=3 without an independent dimension-sensitive PDT premise.

Explicit family: for every d >= 1 and every density operator rho on C^d with spectral decomposition rho=sum_i lambda_i |i><i|, the vector |Psi_rho>=sum_i sqrt(lambda_i)|i>_S|i>_E purifies rho. Thus d=1,...,12 all satisfy the same construction, and the argument extends to every finite d.

### Claim C
`Purification => parameter-free same-input P_PDT != P_QM.`

**Status: FALSIFIED as an inference.**

Reason: ordinary finite-dimensional quantum mechanics satisfies purification. Hence imposing purification alone leaves P_PDT=P_QM available for every microscopic input/resource window. A deviation requires an independently derived PDT rule that changes a state, effect, transformation, composition, or resource restriction.

## Exact dimension stress
For d=1,...,12 choose arbitrary eigenvalues lambda_i >= 0 summing to one and define |Psi>=sum_i sqrt(lambda_i)|i,i>. Partial trace over E gives diag(lambda_1,...,lambda_d) exactly. Degenerate spectra, rank-deficient states, and pure states are included by allowing repeated and zero eigenvalues. This construction has no special behavior at d=3.

## Surviving boundary
Purification may be used only as IMPORTED/KNOWN background unless PDT independently derives it. It cannot be counted as the missing native selector. The next viable attack must introduce a genuinely PDT-native condition on correlated composites or resource-limited distinction that is not simply a standard reconstruction axiom.

## Classification
- Purification principle: **IMPORTED/KNOWN**.
- Purification construction for arbitrary finite d: **PROVED / IMPORTED-KNOWN**.
- Purification as unique PDT composition selector: **FALSIFIED as a PDT-native route**.
- Purification => n=3: **FALSIFIED**.
- Purification => same-input PDT/QM deviation: **FALSIFIED**.
- PDT-native correlated-composite selector: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Parameter-free same-input PDT/QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## References
1. G. Chiribella, G. M. D'Ariano, P. Perinotti, “Probabilistic theories with purification,” Phys. Rev. A 81, 062348 (2010), arXiv:0908.1583.
2. T. D. Galley, L. Masanes, “Any modification of the Born rule leads to a violation of the purification and local tomography principles,” Quantum 2, 104 (2018), doi:10.22331/q-2018-11-06-104.
