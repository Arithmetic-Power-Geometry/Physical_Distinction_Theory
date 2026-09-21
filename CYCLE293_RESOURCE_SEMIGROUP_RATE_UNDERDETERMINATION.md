# Cycle 293 — Resource-semigroup rate underdetermination

## Target
Attack PDT-II target (3), the same-input quantitative deviation, by testing whether a minimal PDT-native-looking resource-composition law can determine a numerical resource-to-distinction prediction rather than merely re-label quantum/resource-theory behavior.

## Candidate principle
Let D(R) in [0,1] denote the operationally revealed distinction after resource amount R >= 0 for a fixed microscopic preparation/readout task, and define the unrevealed fraction U(R)=1-D(R). Test the hypotheses:

1. U(0)=1;
2. 0 < U(R) <= 1 for finite R;
3. U is continuous (measurability/local boundedness would also suffice for the standard Cauchy conclusion);
4. independent sequential resource segments compose homogeneously: U(R+S)=U(R)U(S).

The fourth condition is deliberately strong and is tested as a candidate, not assumed as a theorem of PDT.

## Exact derivation
Because U is positive, define g(R)=-log U(R). Then

g(R+S)=g(R)+g(S), g(0)=0.

Continuity gives the additive Cauchy solution g(R)=kappa R with kappa >= 0. Hence every candidate satisfying the hypotheses has

U(R)=exp(-kappa R),
D(R)=1-exp(-kappa R).

This derivation is dimension independent: n=1,...,12 and arbitrary finite/higher dimension do not alter the functional equation.

## Decisive underdetermination
The composition hypotheses do **not** determine kappa. For every kappa >= 0, D_kappa(R)=1-exp(-kappa R) satisfies all four assumptions. In particular, kappa=0 gives no revelation and any two positive rates kappa_1 != kappa_2 give distinct quantitative predictions while obeying exactly the same structural axioms.

Therefore

resource additivity + homogeneous independent composition + continuity + normalization

DOES NOT imply a unique numerical PDT probability/distinction law and cannot by itself produce P_PDT(O|I,R) != P_QM(O|I,R).

The smallest decisive witness is already scalar: kappa=1 and kappa=2 obey the same axioms but at R=1 predict respectively 1-e^{-1} and 1-e^{-2}.

## Stronger boundary
Even if PDT adopted this exponential form, a same-input experimental prediction would still require an independently derived/calibrated PDT-native rate kappa(I) (or a more structured generator) and a mapping from D to outcome probabilities. Fitting kappa to the same data used for comparison would not be a prior prediction. If kappa is supplied by ordinary QM/channel dynamics, the result is imported rather than PDT-native.

Conversely, dropping homogeneous independent composition enlarges rather than shrinks the admissible class (memory/non-Markovian records, state-dependent hazards, controlled environments), so it cannot rescue uniqueness without additional physical structure.

## Adversarial cases
- kappa=0: degenerate no-revelation semigroup; survives all stated axioms.
- kappa>0 arbitrary: continuum of inequivalent quantitative laws; all survive.
- sequential segmentation R=R1+...+Rm: exact product closure holds for every m and every kappa.
- composites: assigning different task-dependent rates kappa_A, kappa_B or a joint kappa_AB is not fixed by the scalar semigroup law; a composition selector is still required.
- non-Markovian/record-dependent settings: the scalar homogeneous semigroup premise can fail, so the theorem is a boundary result, not a universal dynamics claim.

## Prior-art boundary
The exponential solution of a continuous multiplicative semigroup / additive Cauchy equation is classical mathematics, and exponential survival/decay laws and one-parameter semigroups are standard. None of this is claimed as PDT novelty. The PDT-relevant result is the negative audit conclusion: these generic structural requirements leave a free rate and therefore do not close the same-input prediction target.

## Status ledger
- stated scalar semigroup hypotheses => D(R)=1-exp(-kappa R): **PROVED / IMPORTED-KNOWN mathematics**.
- same hypotheses uniquely determine kappa: **FALSIFIED**.
- same hypotheses alone yield a unique PDT-vs-QM numerical deviation: **FALSIFIED**.
- smallest kappa=1 versus kappa=2 witness: **PROVED**.
- extension to n=1..12 and arbitrary dimension: **PROVED** (dimension does not enter the functional equation).
- non-Markovian universality of the semigroup premise: **FALSIFIED as an unrestricted assumption / not asserted**.
- PDT-native derivation of kappa(I,R) or a structured generator distinct from QM: **OPEN**.
- same-input quantitative PDT-vs-QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Consequence for next cycle
Do not treat exponential resource saturation as a PDT prediction. The next viable target is to derive or falsify a PDT-native generator/rate from independently stated microscopic distinction structure, with no fitted free parameter hidden in R. Any candidate must then be checked against quantum dynamical semigroups, hypothesis-testing/error exponents, classical survival models and general resource theories before novelty can be claimed.
