# Cycle 103 — Resource-quotient splitting and the canonical-section boundary

## Question attacked

Cycle 098 left one precise PDT-II target-(4) obligation: determine whether the existing PDT resource-quotient construction itself supplies (i) no-erasure record compatibility and (ii) an inherited-space embedding under refinement, rather than postulating both.

## Exact setup

Let `V` be a finite-dimensional real distinction space. At resource window `R`, accessible linear tests are represented by `A_R`, invisible directions by

`N_R = ker(A_R)`,

and resolved directions by the quotient

`Q_R = V/N_R`.

Cycle 033 defines genuine refinement `R_c <= R_f` by

`row(A_c) subseteq row(A_f)`,

which implies `N_f subseteq N_c`.

## Result A — no-erasure records are already derived

Because `row(A_c) subseteq row(A_f)`, there exists a linear post-processing matrix `P` with

`A_c = P A_f`.

Therefore every coarse linear record is recoverable from refined records. The no-erasure/record-compatibility premise used in Cycle 098 is not an independent axiom inside this linear refinement model; it follows directly from Cycle 033's definition of refinement.

Classification: **PROVED** inside the stated model; abstract mathematics **IMPORTED/KNOWN**.

## Result B — quotient refinement points from fine to coarse

From `N_f subseteq N_c`, quotient structure canonically produces

`pi_fc : V/N_f -> V/N_c`,

`[v]_(N_f) -> [v]_(N_c)`.

This map is surjective. Quotient structure alone does not canonically provide a reverse injection.

### Smallest decisive counterexample

Take `V=R^2`, `N_f={0}`, and `N_c=span(e_2)`. Then the coarse quotient map is

`q(x,y)=x`.

For every real `a`,

`s_a(t)=(t,a t)`

is a linear section because `q s_a = id`. The quotient-preserving shear

`T_b(x,y)=(x,y+b x)`

obeys `q T_b=q` but sends `s_a` to `s_(a+b)`. Hence no section is invariant under all automorphisms that preserve the quotient data. There is therefore no canonical/natural reverse embedding determined by the quotient alone.

Classification: the claim **"nested resource quotients canonically embed coarse resolved states into fine resolved states without extra structure" is FALSIFIED**. The decisive witness already occurs in ambient dimension 2.

## Result C — a fixed metric supplies the missing split

Assume now that the refinement chain shares one fixed positive-definite inner product. Every quotient `V/N` has a unique minimum-norm representative in `N^perp`, so it is canonically relative to that metric identified with `N^perp`.

Since `N_f subseteq N_c`,

`N_c^perp subseteq N_f^perp`.

Thus the minimum-norm representatives define an isometric section

`i_cf : Q_c -> Q_f`

of `pi_fc`, and there is an orthogonal decomposition

`Q_f = i_cf(Q_c) direct-sum (N_c intersect N_f^perp)`.

Consequently,

`dim Q_f = dim Q_c + dim N_c - dim N_f`.

The second term is the exact dimension of newly revealed directions.

Classification: **PROVED, CONDITIONAL** on a fixed shared positive-definite metric; abstract mathematics **IMPORTED/KNOWN**.

## Stress tests

The exact dimension identity was checked in 110 coordinate cases across

`n=1,...,12,16,24,32,48,64,96,128`, with no failures.

A seeded random audit tested 500 nested Euclidean subspace pairs over dimensions through 64. Maximum residuals were:

- embedding reconstruction: `5.557769820395421e-15`;
- section identity: `1.1052433507716699e-14`;
- old/new orthogonality: `2.0958069697142594e-15`;
- violations above `1e-9`: `0`.

A separate 400-case record-recoverability audit had maximum `||A-PB||=0.0` and zero violations above `1e-12`.

The local Cycle-103 regression suite passes **5/5** tests.

## Prior-art boundary

Orthogonal-complement decomposition, quotient spaces, split exact sequences, rank-nullity and row-space factorization are standard mathematics. Hilbert-space orthogonal complements give unique orthogonal representatives once an inner product is fixed. No mathematical novelty is claimed for these facts.

## PDT consequence

Cycle 098 can now be sharpened:

1. **Record compatibility:** derived from the existing Cycle-033 refinement definition.
2. **Inherited-space embedding:** not available from quotient structure alone.
3. **Inherited-space embedding with fixed metric:** derived by minimum-norm/orthogonal representatives.
4. **If the metric changes with resource:** an additional metric-transport/compatibility law is still required.

This matters because PDT must not silently switch from a quotient hierarchy to nested state spaces. The direction of the canonical quotient map is fine-to-coarse; the reverse direction requires a physically justified splitting structure.

## Classification

- no-erasure record recoverability: **PROVED / IMPORTED-KNOWN** within Cycle-033 refinement;
- canonical fine-to-coarse quotient map: **PROVED / IMPORTED-KNOWN**;
- quotient-only canonical reverse embedding: **FALSIFIED**;
- fixed-metric orthogonal split: **PROVED / CONDITIONAL / IMPORTED-KNOWN**;
- dimension/random stress: **NUMERICALLY SUPPORTED**;
- PDT derivation of resource-invariant metric or metric transport: **OPEN**;
- same-input PDT-vs-QM deviation: **OPEN**;
- **BREAKTHROUGH CANDIDATE: NO**.

## Next strongest obligation

Attack whether the metric used to define minimum-resource/minimum-norm representatives is itself invariant under PDT resource refinement. If not, identify the smallest refinement in which two admissible metrics induce incompatible inherited-state embeddings. Separately, do not identify quotient innovation directions with composition-associator defect directions without an explicit PDT-native map.
