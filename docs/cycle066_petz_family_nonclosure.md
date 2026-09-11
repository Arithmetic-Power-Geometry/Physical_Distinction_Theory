# Cycle 066 — Full Petz/Nussbaum–Szkoła scalar-family nonclosure

## Target
PDT-II target (1): determine whether a composition object richer than a single modular spectrum can retain all operational distinction information.

## Candidate
For faithful states with spectral decompositions `rho=sum_i r_i |r_i><r_i|` and `sigma=sum_j s_j |s_j><s_j|`, define the Nussbaum–Szkoła pair

`p_ij=r_i |<r_i|s_j>|^2`, `q_ij=s_j |<r_i|s_j>|^2`.

The ratio is `p_ij/q_ij=r_i/s_j`, and every Petz moment is

`Q_alpha(rho||sigma)=Tr(rho^alpha sigma^(1-alpha))=sum_ij p_ij^alpha q_ij^(1-alpha)`.

Thus fixing the complete pair `(p,q)` fixes the full cyclic relative-modular spectral measure and every Petz f-divergence/Petz-Renyi divergence.

## Exact phase construction
Take

`r=(11/20,1/4,3/20,1/20)`, `s=(1/2,1/4,3/20,1/10)`

and the complex-Hadamard family

`H(theta)=1/2 [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]`, `z=e^{i theta}`.

Set `rho_theta=H(theta) diag(r) H(theta)^dagger`, `sigma=diag(s)`.

Every entry of `H(theta)` has modulus squared `1/4`; hence the full Nussbaum–Szkoła pair is independent of `theta`. Consequently every Petz moment, and therefore the whole Petz-Renyi family, is identical for all theta.

Nevertheless trace distance changes. Numerically,

`D_tr(rho_0,sigma)=0.35437495772338456`,

`D_tr(rho_pi,sigma)=0.4274491615549574`.

The inequality is also exact, not merely floating-point evidence. For `A_theta=rho_theta-sigma`, the endpoint characteristic polynomials are

`chi_0(lambda)=lambda^4-(47/400)lambda^2-(9/4000)lambda+1/160000`,

`chi_pi(lambda)=lambda^4-(47/400)lambda^2-(9/4000)lambda+169/160000`.

Both have trace zero and positive nonzero determinant, hence each has two positive and two negative eigenvalues. If their trace distances were equal, writing the positive eigenvalues as `p1,p2`, the magnitudes of the negative eigenvalues as `q1,q2`, and `D=p1+p2=q1+q2`, the shared second and third elementary symmetric coefficients would determine `p1 p2+q1 q2` and `q1 q2-p1 p2`; equal `D` would therefore force equal products `(p1 p2)(q1 q2)=det(A)`. But the two exact determinants are different. Hence the trace distances are rigorously unequal.

Therefore

`same complete NS pair / same full Petz family  !=>  same operational trace distinction`.

## Stress tests
The 4D witness was scanned over 65 phases and embedded with an identical tail into dimensions 5–12 and 16,24,32,48,64,96,128. Dimensions 1–3 are recorded as degenerate for this particular Hadamard witness rather than falsely claimed. In every tested dimension >=4, the NS pair remained invariant to numerical precision while trace distance had positive phase spread.

## Prior-art boundary
Nussbaum–Szkoła distributions and the representation of Petz quantum f-divergences through them are established mathematics. Recent work on sufficiency of quantum Renyi families also explicitly warns that Petz-family data are not a complete invariant for quantum dichotomies. This cycle therefore makes no historical novelty claim for the underlying divergence formalism.

## Classification
- Complete NS-pair invariance of the family: **PROVED**.
- Equality of all Petz moments/Renyi divergences: **PROVED / IMPORTED-KNOWN representation mathematics**.
- Claim that the complete Petz scalar family determines trace distance or supplies an operationally complete PDT composition state: **FALSIFIED**.
- Dimension extension >=4: **PROVED by direct-sum construction; NUMERICALLY SUPPORTED regression audit**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving requirement
A viable PDT-native quantum composition object must retain genuinely operator-level relational information not reducible to the Nussbaum–Szkoła classical pair, the full Petz-Renyi family, or a one-dimensional relative-modular spectral measure.
