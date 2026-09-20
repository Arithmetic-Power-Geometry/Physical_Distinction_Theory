# Cycle 280 — A coarse resource tuple does not uniquely determine the admissible measurement family

Status: **DECISIVE FALSIFICATION of an overstrong PDT-native composition route; surviving theorem strengthened**

## Target attacked
Cycle 279 sharpened the missing object to a resource-to-admissible-measurement map `R -> M_R`. This cycle asks whether the PDT resource tuple itself, when it contains only coarse scalar limits such as energy, duration, spatial access, control-alphabet size/access, and error tolerance, can uniquely determine `M_R` without an apparatus/control model.

## Candidate claim
> There exists a universal apparatus-independent map from the coarse PDT resource tuple `R=(E,tau,A,region,epsilon,...)` to a unique admissible measurement/effect family `M_R`.

This claim is false in this generality.

## Exact counterconstruction
Fix a two-level target system and exactly the same numerical coarse budget `R` for two laboratories. Let the allowed interaction time, energy bound, detector resolution/error allowance, and accessible spatial region be identical.

Laboratory Z has a control/interaction algebra generated only by operators commuting with `sigma_z` (together with pointer/readout operations). Its reachable measurement family can distinguish the computational basis but cannot synthesize an `sigma_x` projective measurement solely from those controls.

Laboratory X has, under the same coarse scalar limits, an additional admissible control Hamiltonian proportional to `sigma_y` (or an equivalent basis-changing control) with strength chosen within the same energy bound. It can rotate the X basis to the Z readout basis and hence realizes an X measurement within the same declared coarse budget whenever the rotation-time bound is met.

Thus the numerical tuple is the same while the reachable measurement families differ:

`R_Z = R_X = R` but `M_R^(Z) != M_R^(X)`.

The difference is not hidden in energy or duration; it is in the **generator/control algebra and apparatus coupling topology**. Consequently a function of the coarse numerical tuple alone cannot return a unique physically correct measurement family for both implementations.

This counterexample already lives in the smallest nontrivial quantum system. Zero-padding/adding idle levels embeds it into all larger finite dimensions, so dimension sweeps cannot rescue the universal coarse-map claim and the mechanism cannot select elementary `n=3`.

## Surviving theorem: implementation-relative resource generator
Let `Lambda` denote the implementation specification needed to determine reachability: available drift/control Hamiltonians or operational generators, coupling graph/topology, pointer/readout model, conservation constraints, and any admissibility rules not encoded by the scalar budget. The defensible object is therefore

`(R, Lambda) -> M_{R,Lambda}`,

not `R -> M_R` unless `R` is explicitly enlarged so that it contains `Lambda`.

If resource windows are ordered for a **fixed implementation** so that `R1 <= R2` implies every protocol feasible at `R1` is feasible at `R2`, then

`M_{R1,Lambda} subseteq M_{R2,Lambda}`

and hence every restricted operational distinction of the form

`Delta_{R,Lambda}(rho,sigma) = sup_{E in M_{R,Lambda}} |Tr[E(rho-sigma)]|`

obeys

`Delta_{R1,Lambda}(rho,sigma) <= Delta_{R2,Lambda}(rho,sigma)`.

This monotonicity is rigorous but elementary once admissible-set nesting is assumed. It is not a new quantum law.

## Composition consequence
For two systems A and B, a PDT-native composition theorem cannot be obtained from `(R_A,R_B)` alone if those tuples omit implementation structure. The joint family depends additionally on joint generators/couplings and their resource accounting:

`(R_A,R_B,Lambda_A,Lambda_B,Lambda_AB) -> M_AB`.

In particular, whether an entangling/global effect is reachable can change when `Lambda_AB` changes while all coarse scalar budgets are held fixed. Therefore a proposed PDT composition law that silently inserts a tensor rule or a global-effect family is importing precisely the physical structure it is supposed to derive.

## Prior-art collision
The obstruction is consistent with established quantum-control and measurement-cost literature. Time-energy costs of measurements are defined relative to implementations/processes rather than by a universal scalar budget alone. Work on finite-resource projective measurement shows that measurement quality/cost depends on the system-pointer Hamiltonians and implementation, and thermodynamically consistent measurement-cost analyses explicitly model the probe/apparatus and its coupling. WAY/resource-theoretic results likewise show that conservation constraints and available resources restrict implementability. These literatures prevent promoting the general implementation-dependence observation as uniquely PDT.

Representative prior art checked in this cycle:
- C.-H. F. Fung and H. F. Chau, *Time-energy costs of quantum measurements*, Phys. Rev. A 89, 052306 (2014), DOI 10.1103/PhysRevA.89.052306.
- Y. Guryanova, N. Friis, M. Huber, *Ideal Projective Measurements Have Infinite Resource Costs*, Quantum 4, 222 (2020), DOI 10.22331/q-2020-01-13-222.
- C. L. Latune and C. Elouard, *A thermodynamically consistent approach to the energy costs of quantum measurements*, Quantum 9, 1614 (2025), DOI 10.22331/q-2025-01-28-1614.

## Same-input implication
A same-input PDT-vs-QM prediction cannot arise merely because PDT declares a coarse resource tuple and then chooses a restricted `M_R`. Standard QM supplied with the same implementation `Lambda`, preparation, controls, apparatus and resource limits can compute the same reachable measurement restrictions. A PDT-specific prediction requires an independently justified PDT law that constrains reachability **beyond** the standard microscopic/control model under identical inputs.

## Classification
- universal apparatus-independent `R_coarse -> M_R`: **FALSIFIED**
- smallest counterexample dimension: **n=2**
- extension to higher finite dimensions by idle-sector embedding: **PROVED**
- fixed-implementation nesting `R1<=R2 => M_1 subseteq M_2`: **CONDITIONAL / elementary**
- resulting restricted-distinction monotonicity: **PROVED under nesting**
- implementation/control dependence of measurement reachability/cost: **IMPORTED/KNOWN structure**
- coarse resource tuple alone selects `n=3`: **FALSIFIED**
- PDT-native `(R,Lambda) -> M_{R,Lambda}` law beyond standard reachability: **OPEN**
- same-input PDT/QM quantitative deviation: **OPEN**
- breakthrough candidate: **NO**

## Consequence for PDT-II
The breakthrough target must be sharpened again. Do not search for a universal measurement generator from scalar resource coordinates alone. Either (a) promote the implementation/control algebra into the PDT resource object and derive nontrivial consequences from that enriched object, or (b) prove a genuinely implementation-independent invariant/bound that survives variation over all implementations consistent with the same coarse budget. Any candidate in route (b) must be checked against quantum speed limits, measurement-cost bounds, WAY/resource-theory constraints and optimal-control reachability before it can be called PDT-native.