# PDT Cycle 142 — Equal-splitter quadratic selector

## Result status

**PROVED (conditional theorem); FALSIFIED (binary-only uniqueness claim); IMPORTED/KNOWN (analysis ingredients and adjacent frame-function literature); NUMERICALLY SUPPORTED; OPEN (PDT-native derivation of the splitter laws).**

**BREAKTHROUGH CANDIDATE: NO.**

## Conditional theorem

Let `g:[0,∞)->[0,∞)` be continuous. Interpret `g(r)` as the resource assigned to a rank-one distinction of radial strength `r`. Assume resolved equal-amplitude splitters conserve resource in the following two cases for every `r>=0`:

1. binary splitter: `g(r)=2 g(r/sqrt(2))`;
2. ternary splitter: `g(r)=3 g(r/sqrt(3))`.

Then `g(r)=c r^2`. If `g(1)=1`, then `g(r)=r^2`.

### Proof

For `r>0`, write `r=e^t` and define

`h(t)=e^{-2t} g(e^t)`.

The binary identity implies

`h(t)=h(t-(ln 2)/2)`.

The ternary identity implies

`h(t)=h(t-(ln 3)/2)`.

Thus `h` has periods `a=(ln 2)/2` and `b=(ln 3)/2`. Their ratio is irrational: if `a/b=p/q` for nonzero integers `p,q`, then `q ln 2=p ln 3`, hence `2^q=3^p`, impossible by unique prime factorization. Integer combinations of two periods with irrational ratio are dense in `R`. Since `h` is continuous, invariance under this dense subgroup forces `h` to be constant. Therefore `g(e^t)=c e^{2t}`, so `g(r)=c r^2` for `r>0`; continuity handles `r=0`. Calibration gives `c=1`.

No Hilbert norm, Born rule, quantum dynamics, gravity law, or target exponent is inserted into the proof after the two operational splitter identities are stated.

## Decisive weakening counterexample

Binary conservation alone is not enough. For `0<eps<1`, define

`g_eps(r)=r^2[1+eps sin(4 pi log_2 r)]` for `r>0`, and `g_eps(0)=0`.

This is positive, continuous and nonlinear. Because `log_2(r/sqrt(2))=log_2 r-1/2`, the sine acquires a `-2 pi` phase and is unchanged. Therefore

`g_eps(r)=2 g_eps(r/sqrt(2))`

exactly, but the ternary law fails generically because `(ln 3)/(ln 2)` is irrational. The frozen witness uses `eps=0.05`, `r=1.23456789`: binary relative residual is `1.50e-16`, while the ternary relative residual is about `3.83e-2`.

Hence a single equal-split replication law leaves a log-periodic gauge freedom.

## Relation to Cycle 141

Cycle 141 showed that direct-sum additivity, tensor multiplicativity, reversible invariance and rank-one calibration permit the full Schatten-power family. Cycle 142 identifies a much smaller additional bridge that selects exponent 2 on the radial rank-one sector: conservation under both a 2-way and a 3-way equal-amplitude resolved splitter plus continuity.

This does **not** yet prove the full PDT composition law. It says that if PDT can independently justify those two splitter operations as resource-preserving resolved refinements, the scalar degree ambiguity is removed without assuming general pairwise additivity.

## Prior-art boundary

The dense-period continuity argument is standard real analysis. The broader theme that additive/noncontextual values over orthogonal resolutions lead to quadratic forms is classical frame-function/Gleason territory. Therefore neither that mathematical mechanism nor quadraticity by itself is claimed as PDT novelty. The only potentially PDT-specific future contribution would be an independently derived operational reason that distinction resource obeys precisely these splitter laws.

## Stress audit

The executable audit labels dimensions `n=1..12,16,24,32,48,64,96,128` and samples strengths over twelve orders of magnitude. Across the frozen run:

- quadratic law: 0 binary failures, 0 ternary failures;
- nonlinear binary-only counterfamily: 0 binary failures, 583 ternary failures;
- maximum quadratic binary residual: `4.43e-16`;
- maximum quadratic ternary residual: `4.39e-16`.

The theorem is analytic; these computations are regression checks, not its proof.

## Remaining PDT-native obligation

**OPEN:** derive, from PDT primitives and without inserting Euclidean/quadratic accounting, that a resolved equal-amplitude splitting of one distinction into 2 and into 3 orthogonal channels preserves total resource.

Until that is done, this theorem remains conditional and is not a breakthrough claim.
