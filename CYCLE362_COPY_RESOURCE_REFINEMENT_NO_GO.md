# Cycle 362 — Copy-resource refinement is not an n=3 selector

## Target attacked
PDT-II targets (2) non-circular n=3 derivation, (3) same-input PDT/QM quantitative deviation, and (4) resource-refinement/revelation laws.

## Candidate principle
Increasing an explicitly declared resource window by supplying additional independent records/copies should reveal previously unresolved physical distinctions. A strong operational instantiation is binary discrimination of two states from k independent copies.

## Exact hypotheses
For every finite n >= 2 let H_n = C^n and embed

|psi_n> = |0>,
|phi_n> = (1/2)|0> + (sqrt(3)/2)|1>.

Use equal priors and permit the optimal joint measurement on k copies. The microscopic input pair is identical across dimensions except for zero padding; the declared resource is exactly k copies.

## Exact calculation
The single-copy overlap is c = |<psi_n|phi_n>| = 1/2 for every n >= 2. For k copies the overlap is c^k. The Helstrom minimum error for two equiprobable pure states is therefore

P_err(k) = (1 - sqrt(1 - c^(2k)))/2
         = (1 - sqrt(1 - 4^(-k)))/2.

Consequently P_err(k+1) < P_err(k) for every finite k >= 1, and P_err(k) -> 0. The refinement law is real and quantitative, but it is exactly dimension-blind for this embedded family.

## Decisive counterexample
n=2 already realizes the complete resource-refinement curve. n=3 gives exactly the same curve, and so does every n >= 4. Therefore the principle

"more independent distinction-bearing records monotonically improve optimal distinction"

cannot imply n=3. Nor can this law by itself produce P_PDT(O|I,R) != P_QM(O|I,R), because ordinary quantum mechanics already predicts the exact curve under the same microscopic inputs and same copy resource k.

Smallest decisive nontrivial counterexample: n=2, k=1.

## n=1..12 audit
n=1 is degenerate for the specified two-state embedding. For every n=2..12 the overlap and all k-copy Helstrom probabilities are identical. See `results/cycle362_copy_resource_n1_n12.csv`.

## Higher-dimensional/asymptotic stress
The construction is an isometric embedding of a fixed two-dimensional subspace into C^n, so the no-go is analytic for every finite n >= 2, not merely numerical. As k grows, P_err(k) ~ 4^(-k)/4. No dimension-three singularity appears.

## Prior-art check
This mechanism is standard quantum hypothesis testing, not PDT novelty. Audenaert et al., Phys. Rev. Lett. 98, 160501 (2007), established the quantum Chernoff bound for asymptotically many copies. The present embedded pure-state family is an elementary exact specialization and is used only as a falsification witness.

## Surviving PDT requirement
A PDT-native revelation law capable of doing new work must depend on a resource variable that is not reducible to standard access to additional i.i.d. quantum copies/records, and it must specify a same-input operational probability that differs from the quantum optimum. Merely requiring monotone revelation with additional copies is insufficient.

## Status
- Exact k-copy Helstrom curve for the embedded family: **PROVED / IMPORTED-KNOWN**.
- Strict improvement with k: **PROVED**.
- Copy-resource refinement => n=3: **FALSIFIED**.
- Copy-resource refinement => unique PDT composition: **FALSIFIED as an inference**.
- Copy-resource refinement => same-input PDT/QM deviation: **FALSIFIED as an inference**.
- PDT-native non-QM resource-window law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.
