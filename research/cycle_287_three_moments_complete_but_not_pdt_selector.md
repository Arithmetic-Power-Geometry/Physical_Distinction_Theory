# PDT-II Cycle 287 — three spectral moments close the two-qubit bilinear orbit, but do not derive composition

## Status

- **PROVED (two-qubit bilinear coupling model):** for a real 3 x 3 coupling matrix `J`, the three power sums `I2=tr(J^T J)`, `I4=tr[(J^T J)^2]`, and `I6=tr[(J^T J)^3]` determine the unordered squared singular-value multiset exactly.
- **IMPORTED/KNOWN:** Newton identities and singular-value/local-orbit classification.
- **FALSIFIED as a PDT-native route:** merely extending Cycle 286 by appending the complete third spectral moment does not derive a physical composition law; it only encodes the already chosen nonlocal interaction orbit.
- **OPEN:** a PDT-native operational principle that selects/constrains the nonlocal orbit from independently specified physical hypotheses.
- **OPEN:** non-circular PDT-native n=3 derivation.
- **OPEN:** same-input quantitative PDT/QM deviation.
- **BREAKTHROUGH CANDIDATE:** NO.

## Exact theorem

Let `A = J^T J` and let its eigenvalues be the nonnegative squared singular values `x1,x2,x3`. Define

`p1 = I2 = x1+x2+x3`,

`p2 = I4 = x1^2+x2^2+x3^2`,

`p3 = I6 = x1^3+x2^3+x3^3`.

Newton identities recover the elementary symmetric polynomials:

`e1 = p1`,

`e2 = (p1^2-p2)/2`,

`e3 = (p1^3-3 p1 p2+2 p3)/6`.

Therefore `x1,x2,x3` are exactly the roots, with multiplicity, of

`t^3 - e1 t^2 + e2 t - e3 = 0`.

Hence `(I2,I4,I6)` determines the unordered squared singular-value multiset. Degenerate cases (zero singular values and repeated singular values) are included automatically because the characteristic polynomial retains multiplicity.

## Check against Cycle 286 witness

Cycle 286 used

`x_A=(1/2,1/2,0)` and `x_B=(2/3,1/6,1/6)`.

Both have `p1=1` and `p2=1/2`, but

`p3(A)=1/4`, `p3(B)=11/36`.

The third moment therefore separates exactly the counterexample that defeated `(I2,I4)`.

For A, Newton reconstruction gives

`e1=1`, `e2=1/4`, `e3=0`,

so the polynomial is `t(t-1/2)^2`.

For B it gives

`e1=1`, `e2=1/4`, `e3=1/54`,

so the polynomial is `(t-2/3)(t-1/6)^2`.

## Dimension stress and generalization

The algebraic statement generalizes: for `r` nonnegative squared singular values, the first `r` power sums determine the multiset through Newton identities. Thus tests over dimensions 1 through 12 do not support an unrestricted claim that every finite collection of scalar spectral invariants must fail. In fixed finite rank, a finite complete spectral descriptor exists.

This is an important guardrail: PDT must not turn the Cycle 285/286 counterexamples into a false infinite no-go.

## Why this does not solve PDT composition

Completeness is not selection. Giving `(I2,I4,I6)` is equivalent to specifying the singular spectrum of the nonlocal coupling in this model. It tells us which orbit was chosen; it does not explain why physical subsystems with stated local structure and resources must realize that orbit.

Accordingly the candidate rule

`local data + complete orbit invariants -> orbit`

is mathematically valid but circular as a PDT derivation. It cannot supply a non-circular `n=3` result or a same-input deviation from quantum mechanics.

## Prior-art gate

The proof uses standard Newton identities plus established singular-value/canonical classification of two-qubit bilinear interactions. No novelty claim is attached to the algebra. The PDT value is methodological: it closes an overbroad no-go direction and prevents an invalid extrapolation from one- and two-scalar counterexamples.

Representative background retained from Cycles 285–286:

- Zhang, Vala, Sastry & Whaley, *Geometric theory of nonlocal two-qubit operations*, Phys. Rev. A 67, 042313 (2003), DOI 10.1103/PhysRevA.67.042313.
- Standard Newton identities for recovery of elementary symmetric polynomials from power sums.

## Surviving target

Do not spend further cycles merely adding spectral moments in this fixed rank-three sector. Attack the genuinely physical question: what PDT-native operational hypothesis, if any, selects or restricts the joint interaction/effect orbit without placing the desired orbit in the input? Any candidate must then be compared against standard QM/GPT/control theory under identical microscopic inputs and resource windows.
