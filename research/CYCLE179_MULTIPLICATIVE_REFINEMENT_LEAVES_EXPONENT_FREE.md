# Cycle 179 — Multiplicative refinement leaves the response exponent free

## Target attacked
Strongest surviving PDT-II probability obligation after Cycle 178: whether sequential refinement plus independent-composite multiplicativity derives a unique response functional from positive distinction records.

## Status
- Continuous multiplicative-response classification: **PROVED**.
- Uniqueness of the response functional from these axioms: **FALSIFIED**.
- Power-law functional-equation result: **IMPORTED/KNOWN**.
- PDT-native value of the exponent: **OPEN**.
- PDT-native n=3 probability derivation: **OPEN**.
- Same-input PDT-vs-QM quantitative prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Hypotheses
Let each operational distinction class carry a positive independently measured scalar record s>0. Assume an unnormalized response F:(0,infinity)->(0,infinity) with:

1. continuity;
2. identical independent records compose multiplicatively at the record level, s_AB=s_A s_B;
3. independent-composite response factorization, F(s_A s_B)=F(s_A)F(s_B);
4. probabilities on a finite quotient are obtained by normalized response weights p_i=F(s_i)/sum_j F(s_j).

The normalization F(1)=1 follows from positivity and multiplicativity.

## Theorem — exact classification
Every continuous positive F satisfying F(xy)=F(x)F(y) has

    F(x)=x^alpha

for some real alpha. Conversely every real alpha satisfies the hypotheses.

### Proof
Define g(t)=log F(exp(t)). Then

    g(u+v)=log F(exp(u+v))
          =log F(exp(u)exp(v))
          =g(u)+g(v).

Continuity of F implies continuity of g. The continuous additive Cauchy equation therefore gives g(t)=alpha t for a real constant alpha. Hence log F(x)=alpha log x and F(x)=x^alpha. Conversely x^alpha is positive, continuous and multiplicative. QED.

If an additional monotonicity axiom requires larger records to have no smaller response, then alpha>=0. Strict monotonicity gives alpha>0. Neither condition selects alpha=1.

## Decisive nonuniqueness witness
Take n=2 and records s=(1,2). Both alpha=1 and alpha=2 satisfy all hypotheses, including independent-composite multiplicativity:

- alpha=1: p=(1/3,2/3);
- alpha=2: p=(1/5,4/5).

Therefore sequential/independent multiplicative composition reduces the arbitrary response F to a power family but does not determine the exponent.

## Sequential refinement consistency
For a refinement represented by positive multiplicative factors r_1,...,r_k, the final record is s prod_l r_l. The power family gives

    F(s prod_l r_l)=F(s) prod_l F(r_l),

independent of parenthesization and refinement order. Thus associativity of sequential multiplicative refinement does not remove alpha.

A stronger axiom such as F(s)=s, F'(1)=1, or a specified response to one nonunit calibration value fixes alpha, but each supplies new quantitative physical information. It cannot be inferred from multiplicativity itself.

## Dimension stress test
The obstruction is analytic rather than numerical.

- n=1: normalization makes the outcome probability trivially 1, so alpha is observationally invisible.
- Every n>=2: choose s=(1,2,1,...,1). Alpha=1 and alpha=2 yield distinct distributions while satisfying all hypotheses.
- Therefore the counterexample holds exactly for n=2,...,12 and every higher finite n.

For product systems of arbitrary finite sizes m and n, response weights factor exactly:

    (s_i t_j)^alpha=s_i^alpha t_j^alpha,

and the normalizing denominator factorizes as (sum_i s_i^alpha)(sum_j t_j^alpha). Hence the normalized joint distribution is the product of the normalized marginals for every alpha.

## Edge and degenerate cases
- Equal records: all alpha give the uniform distribution; no exponent can be identified.
- alpha=0: uniform response regardless of positive records; allowed unless strict record sensitivity is independently required.
- alpha<0: reverses record ordering; excluded only if monotonicity is separately justified.
- Records approaching zero require an extension convention; this adds boundary structure and does not select alpha on the positive domain.

## Consequence for n=3
For s=(1,2,3):

- alpha=1 gives (1/6,2/6,3/6);
- alpha=2 gives (1/14,4/14,9/14).

Both obey continuous multiplicative composition and sequential refinement. Therefore these principles do not provide the required non-circular PDT-native n=3 probability derivation.

## Consequence for same-input PDT != QM
A same-input PDT/QM discrepancy cannot be claimed by selecting alpha after comparison with the Born probabilities. Unless PDT independently derives both the record s from the microscopic input/resource window and a physical calibration fixing alpha, the exponent is a free model parameter and the discrepancy is not a PDT prediction.

## Prior-art boundary
The classification is the standard continuous multiplicative Cauchy functional equation after the logarithmic change of variables. Normalized positive-weight choice rules are also part of established Luce-type choice representations. Accordingly the power-family theorem is **IMPORTED/KNOWN**, while its role here is to delimit what PDT's proposed axioms fail to determine.

## Strongest surviving obligation
Find a PDT-native, independently measurable calibration/revelation law that fixes alpha without inserting a probability law, or prove that no such calibration follows from distinction structure. A particularly sharp next test is whether coarse-graining/refinement consistency across additive record splitting is compatible with alpha != 1; if additivity is independently physical rather than assumed for convenience, it may fix alpha=1, but that must be proved and checked for circularity and prior art before any PDT claim.