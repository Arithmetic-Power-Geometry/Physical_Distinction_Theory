# Cycle 251 — Continuous-reversibility selector boundary

## Target
Test whether a PDT-native candidate based on continuous reversible motion between pure distinction states can (i) determine the composite law or (ii) non-circularly select n=3.

## Exact hypotheses tested
Let S_n be the state space of a finite system with information capacity n. Candidate C251 requires that for every pair of pure states x,y in S_n there is a continuous one-parameter family of reversible transformations T_t with T_0 x=x and T_1 x=y. No dimension-dependent constant and no occurrence of the desired value 3 is permitted in C251.

## Result 251A — continuous reversibility alone is dimension-blind (PROVED)
Finite-dimensional complex quantum theory is an analytic counterfamily for every n>=2. Pure states are rays in CP^{n-1}. For any unit vectors psi and phi representing two rays, extend each to an orthonormal basis and choose a unitary U with U psi=phi. Because U(n) is path-connected, write U=V diag(exp(i theta_j)) V^dagger and define U_t=V diag(exp(i t theta_j)) V^dagger. Then U_0=I, U_1=U and rho -> U_t rho U_t^dagger is a continuous reversible path taking |psi><psi| to |phi><phi|. The n=1 case is degenerate/trivial.

Therefore C251 holds for n=1,2,3,... and cannot by itself select n=3. The requested n=1..12 stress window is covered exactly by the proof, not by numerical extrapolation. The smallest nontrivial competitor is n=2.

## Result 251B — continuous reversibility alone does not determine composition (PROVED)
C251 is a single-system symmetry/transitivity property. It contains no rule specifying the positive cone/state space of AB, no admissible entangled states/effects, and no tensor product. Consequently no unique joint-state functor J(A,B) follows from C251 alone. In particular, knowing the reversible group action on each local pure-state space does not logically specify which locally compatible bilinear functionals are admitted globally.

This is a structural underdetermination result: a local dynamical axiom cannot become a composite selector without an additional cross-system axiom.

## Result 251C — the tempting n=3 rescue is established prior art (IMPORTED/KNOWN)
Masanes and Mueller's GPT reconstruction combines three operational principles: Tomographic Locality, the Subspace Axiom, and Continuous Reversibility. Their generalized-bit analysis first yields a Euclidean ball whose dimension is not yet fixed. The n=3 Bloch-ball dimension is fixed only after imposing composite-system consistency using the other principles. Mueller's reconstruction notes explicitly emphasize this sequence.

Therefore, if PDT obtains n=3 by importing this package (or a relabelling mathematically equivalent to it), the result is not a PDT-native n=3 derivation. A genuinely PDT-native derivation must independently derive the needed cross-system/subspace constraints from PDT primitives and then show that the resulting hypotheses are not merely the known reconstruction assumptions in new vocabulary.

Relevant prior art:
- Masanes, L., Mueller, M. P., Perez-Garcia, D., & Augusiak, R., *Entanglement and the three-dimensionality of the Bloch ball*, Journal of Mathematical Physics 55, 122203 (2014), arXiv:1111.4060.
- Mueller, M. P., *Probabilistic theories and reconstructions of quantum theory*, SciPost Physics Lecture Notes 28 (2021), DOI 10.21468/SciPostPhysLectNotes.28.
- Dakic, B. & Brukner, C., reconstruction work using information capacity/locality/reversibility; continuous reversibility is an established quantum-reconstruction principle rather than a PDT-native primitive.

## Same-input prediction audit
C251 supplies no probability functional different from the Born rule. Within the complex-quantum counterfamily it is exactly compatible with ordinary unitary dynamics, so no same-input P_PDT(O|I,R) != P_QM(O|I,R) follows. Any deviation requires an independently derived PDT probability/dynamics/resource law.

## Status
- Continuous reversibility as n=3 selector: **FALSIFIED**.
- Continuous reversibility as unique composition selector: **FALSIFIED**.
- Dimension-uniform complex-QM counterfamily: **PROVED**.
- Continuous reversibility + tomography + subspace reconstruction route: **IMPORTED/KNOWN**.
- PDT-native derivation of the cross-system constraint that would force n=3: **OPEN**.
- Same-input PDT-vs-QM deviation: **OPEN**.
- Experimentally distinctive PDT inequality: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving obligation
The next viable route cannot merely add another known reconstruction axiom. It must derive, from PDT distinction primitives, a cross-system admissibility constraint strong enough to eliminate n=2 and n>=4 and to choose a composite state/effect structure. That derivation must be audited against Masanes-Mueller, Dakic-Brukner, Hardy, Chiribella-D'Ariano-Perinotti and GPT/Jordan reconstructions before any novelty claim.