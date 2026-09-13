# Cycle 115 — graded-completion economy no-go

## PDT-II targets attacked
Targets (1) and (2): whether a generic resource/economy principle can independently force same-sector composition `V x V -> V`, or select `n=3`, after Cycle 114 showed that finite associative graded completion exists in every finite dimension.

## Candidate principle tested
A natural rescue attempt is to postulate that physically admissible composition chooses the smallest standard graded completion relative to the primitive dimension. This cycle tests four dimension-only costs, none containing an `n=3` target:

- full exterior/Clifford completion: `F(n)=2^n/n`;
- even Clifford sector: `E(n)=2^(n-1)/n`;
- scalar + vector + bivector carrier: `S(n)=(1+n+C(n,2))/n=(n+1)/2+1/n`;
- vector + bivector carrier: `B(n)=(n+C(n,2))/n=(n+1)/2`.

The claim that these canonical economy functionals select `n=3`, or provide a non-circular reason for same-sector closure, is **FALSIFIED**.

## Exact minimizer theorems
For `F(n)=2^n/n`,

`F(n+1)/F(n)=2n/(n+1)`.

This ratio equals 1 only at `n=1` and exceeds 1 for every `n>1`. Hence the global positive-integer minimizers are `n=1,2`, with `F=2`. The even-sector cost is exactly `F/2`, so it has the same minimizers.

For `S(n)=(n+1)/2+1/n`, one has `S(1)=S(2)=2` and

`S(n+1)-S(n)=1/2-1/(n(n+1))>0` for every `n>=2`.

Thus its global minimizers are again `n=1,2`.

Finally `B(n)=(n+1)/2` is strictly increasing, so its unique positive-integer minimizer is `n=1`.

At `n=3`, the four costs are respectively `8/3`, `4/3`, `7/3`, and `2`; none is a minimum.

Therefore generic minimization of these standard completion dimensions does not select three dimensions.

## Validation and stress boundary
Exact rational arithmetic was checked at `n=1..12,16,24,32,48,64,96,128`. The analytic monotonicity proofs cover every positive integer dimension, so randomized state tests would not add evidence to this dimension-only claim. Local regression for the cycle implementation passed 6/6 tests.

The candidate is intentionally narrow. Different norms, reversible groups, pure/mixed states, Markovian/non-Markovian dynamics, controlled records and thermodynamic environments cannot change these four dimension counts. This cycle therefore does **not** claim to falsify every possible PDT-native resource functional; it falsifies the generic proposal that ordinary graded-carrier size or size-per-primitive-dimension is enough.

## Prior-art boundary
No graded-dimension fact is claimed as novel. Standard exterior-algebra results give `dim Lambda^k(V)=C(n,k)` and the full exterior algebra dimension `2^n`. Standard Clifford algebra references likewise give an associative algebra with vector-space dimension `2^n`. These facts are used only to define the tested economy functionals and to guard against rediscovery.

Prior-art checks:
- Encyclopedia of Mathematics, *Exterior algebra*: https://encyclopediaofmath.org/wiki/Exterior_algebra
- Encyclopedia of Mathematics, *Clifford algebra*: https://encyclopediaofmath.org/wiki/Clifford_algebra
- Wolfram MathWorld, *Clifford Algebra*: https://mathworld.wolfram.com/CliffordAlgebra.html

## Classification
- **PROVED** — the stated global minimizers of the four explicit cost functionals.
- **FALSIFIED** — these canonical graded-completion economy principles select `n=3` or force same-sector closure.
- **IMPORTED/KNOWN** — exterior/Clifford carrier dimensions and grading facts.
- **NUMERICALLY SUPPORTED** — exact repository arithmetic at the declared stress dimensions and 6/6 local regression tests agree with the proofs.
- **OPEN** — a genuinely PDT-native operational/resource cost derived independently of the desired dimension and codomain.
- **OPEN** — same-input quantitative PDT-vs-QM deviation.
- **OPEN** — experimentally distinctive inequality.
- **OPEN** — gravity/capacity law; no desired gravitational result was imported.

**BREAKTHROUGH CANDIDATE: NO.**

## Strongest surviving obligation
The next admissible route must distinguish output sectors by an independently measurable PDT quantity—not by generic carrier dimension. A successful principle would need a physically derived resource/revelation law that assigns operational consequences to scalar/vector/bivector/higher-grade outputs, survives countermodels, and only then yields same-sector closure or a dimensional restriction. Any cost engineered to have a minimum at `n=3` is inadmissible as a derivation.
