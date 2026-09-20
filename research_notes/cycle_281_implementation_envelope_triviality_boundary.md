# Cycle 281 — Implementation-envelope bounds collapse without structural restrictions

Status: **DECISIVE FALSIFICATION of the unrestricted implementation-independent envelope route**

## Target attacked
Cycle 280 left two defensible routes after falsifying a universal coarse-resource map `R -> M_R`: enrich the resource object by an implementation specification `Lambda`, or seek an implementation-independent invariant/bound that survives variation over all implementations consistent with the same coarse numerical budget. This cycle attacks the second route in its strongest unrestricted form.

## Candidate claim
> A coarse PDT resource tuple `R=(E,tau,A,region,epsilon,...)`, while leaving the control/apparatus implementation `Lambda` unspecified, nevertheless determines a nontrivial universal distinguishability envelope over all implementations consistent with `R`.

This is false unless the admissible implementation class is structurally restricted.

## Exact two-level counterconstruction
Take the binary alternatives

`rho0 = |0><0|`, `rho1 = |1><1|`

on a qubit. Fix identical coarse numerical limits `R` for two implementations and suppose those limits do not specify the readout/control algebra.

Implementation `Lambda_blind`: the only admissible binary effect is proportional to identity (equivalently the apparatus is insensitive to the encoded Z degree of freedom). Then

`Delta_{R,Lambda_blind}(rho0,rho1) = 0`.

Implementation `Lambda_Z`: under the same numerical energy/time/error/spatial budget, a Z-sensitive pointer/readout is admissible. The effect `E=|0><0|` gives

`|Tr[E(rho0-rho1)]| = 1`,

so

`Delta_{R,Lambda_Z}(rho0,rho1) = 1`.

Therefore, if `C(R)` is broad enough to include both implementations,

`inf_{Lambda in C(R)} Delta_{R,Lambda}(rho0,rho1) = 0`,
`sup_{Lambda in C(R)} Delta_{R,Lambda}(rho0,rho1) = 1`.

These are the algebraically trivial bounds for a normalized binary operational distinction. No nontrivial coarse-budget-only inequality survives.

The same construction embeds into every finite dimension `n >= 2` by adding idle levels. It also survives composites by encoding the active distinction in a two-dimensional invariant sector. Hence dimension sweeps, tensoring with spectators, or increasing local dimension cannot rescue the unrestricted envelope claim.

## Stronger surviving theorem
A nontrivial implementation-independent envelope can exist only after the implementation class is restricted by additional physical structure. Let

`C(R,S) = {Lambda : Lambda satisfies coarse budget R and structural constraints S}`.

Define

`Delta_min(R,S;rho,sigma) = inf_{Lambda in C(R,S)} Delta_{R,Lambda}(rho,sigma)`,
`Delta_max(R,S;rho,sigma) = sup_{Lambda in C(R,S)} Delta_{R,Lambda}(rho,sigma)`.

If `S` is empty or too weak to exclude blind and perfectly aligned readout implementations, the envelope is `[0,1]` on an orthogonal pair and is uninformative. Any useful theorem must expose which structural assumptions make `Delta_min>0` or `Delta_max<1`.

Candidate structural restrictions include a fixed control Lie algebra/generator set, fixed coupling graph, fixed pointer model, conservation laws, locality constraints, bounded interaction norm, bandwidth/noise model, or a specified measurement architecture. But once these are included, the theorem is implementation-class relative rather than a consequence of coarse scalar resources alone.

## Prior-art boundary
This conclusion is consistent with established quantum-control theory: reachability depends on the dynamical Lie algebra and system/ancilla structure, not only scalar energy/time budgets. Resource-constrained quantum speed-limit results also require a specified Hamiltonian/control geometry. Energy-constrained discrimination likewise defines the constraint relative to a specified Hamiltonian. Thus the need for structural implementation data is not uniquely PDT.

Representative checks:
- G. Dirr et al., *Lie Theory for Quantum Control*, GAMM-Mitteilungen 31 (2008), DOI 10.1002/gamm.200890003: finite-dimensional controllability is a Lie-group/Lie-algebra reachability problem.
- D. D'Alessandro, F. Albertini, R. Romano, *Exact Algebraic Conditions for Indirect Controllability of Quantum Systems*, SIAM J. Control Optim. 53 (2015): controllability depends on the dynamical Lie algebra and auxiliary-system state/dimension.
- B. Russell and S. Stepney, *The Geometry of Speed Limiting Resources in Physical Models of Computation*, IJFCS 28 (2017), DOI 10.1142/S0129054117500204: speed limits are derived relative to resource constraints on the control geometry.
- S. Becker, N. Datta, L. Lami, C. Rouze, *Energy-Constrained Discrimination of Unitaries, Quantum Speed Limits, and a Gaussian Solovay-Kitaev Theorem*, PRL 126, 190504 (2021), DOI 10.1103/PhysRevLett.126.190504: energy-constrained channel discrimination is Hamiltonian-relative.

## Consequences for PDT-II targets
1. **Composition:** varying the joint implementation class can range from no informative joint effect to a fully resolving joint effect while coarse local budgets remain unchanged. A composition theorem therefore requires structural constraints on `Lambda_AB` or an independently derived rule for composing implementation classes.
2. **n=3:** the two-level witness embeds into all `n>=2`; the route is dimension-independent and cannot select three dimensions.
3. **Same-input PDT/QM deviation:** standard QM with the same `Lambda` reproduces the same reachability restriction. No deviation follows from taking an implementation envelope.
4. **Resource revelation:** monotonicity remains valid for nested admissible families at fixed structural specification, but coarse-resource revelation bounds are trivial if structural variation is unrestricted.
5. **Experimental inequalities:** any nontrivial inequality must state the implementation class and cannot be advertised as coarse-resource universal.
6. **Gravity:** no implication.

## Classification
- nontrivial universal coarse-`R` implementation envelope without structural restrictions: **FALSIFIED**
- exact qubit envelope witness `[0,1]`: **PROVED**
- extension to all finite `n>=2` by idle-sector embedding: **PROVED**
- useful envelope conditional on explicit structural class `S`: **CONDITIONAL / OPEN for nontrivial PDT-native choices of S**
- Lie-algebra/control dependence of reachability: **IMPORTED/KNOWN**
- coarse implementation envelope selects `n=3`: **FALSIFIED**
- same-input PDT/QM quantitative deviation: **OPEN**
- breakthrough candidate: **NO**

## Next strongest route
Stop searching for nontrivial laws invariant over an unrestricted implementation class. The composition target should now be formulated over **structured implementation objects** and ask whether PDT supplies a native composition operation

`(R_A,Lambda_A) box_D (R_B,Lambda_B) -> (R_AB,Lambda_AB,M_AB)`

that is not merely ordinary quantum/GPT/control composition in new notation. The next prove-or-falsify test should impose a minimal structural package (for example fixed local generator algebras plus a declared interaction-resource class) and determine whether resource-distinction principles uniquely constrain the admissible joint generator/effect closure. If multiple inequivalent joint closures still satisfy the same PDT data, record the smallest counterexample rather than adding another axiom silently.
