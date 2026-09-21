# Cycle 298 — Product scalar composition no-go

## Target
PDT-II target (1): test whether a PDT-native composition law can determine composite distinguishability from the two local scalar distinguishabilities alone, even after restricting to independent hypothesis-conditioned product systems.

## Candidate statement attacked
For normalized total-variation distinguishability D, suppose

P_AB^0 = P_A^0 tensor P_B^0,   P_AB^1 = P_A^1 tensor P_B^1.

Candidate: there exists a universal scalar function F such that

D(P_AB^0,P_AB^1) = F(D_A,D_B)

for all finite classical product experiments.

## Exact smallest-alphabet counterexample
All distributions below are Bernoulli on {0,1}. Write Bern(p)=(p,1-p).

Experiment X:
- A0 = Bern(0), A1 = Bern(1/4)
- B0 = Bern(0), B1 = Bern(1/4)
- D_A = D_B = 1/4
- exact product TV = 7/16.

Experiment Y:
- A0 = Bern(0), A1 = Bern(1/4)
- B0 = Bern(1/4), B1 = Bern(0)
- D_A = D_B = 1/4
- exact product TV = 1/4.

Thus the local scalar pair is identical, (D_A,D_B)=(1/4,1/4), while the composite scalar differs:

7/16 != 1/4.

Therefore no universal F(D_A,D_B) can recover product total-variation distinguishability, even for binary classical factors with conditional independence.

A frequently tempting rule,

D_AB = 1-(1-D_A)(1-D_B),

is also falsified as an equality: it gives 7/16 for both examples but Experiment Y has D_AB=1/4.

## Surviving bounds
For product distributions the standard coupling/data-processing arguments give

max(D_A,D_B) <= D_AB <= 1-(1-D_A)(1-D_B) <= D_A+D_B.

The lower bound follows by marginalization. The upper bound follows by independently coupling each factor with mismatch probabilities D_A and D_B, producing joint mismatch probability 1-(1-D_A)(1-D_B).

These are boundary constraints, not a PDT-native composition law.

## Stress-test scope
- Exact rational regression uses the two binary witnesses above.
- The obstruction embeds into every larger finite alphabet/dimension by zero-padding/spectator coordinates, hence n=2 through n=12 and arbitrary larger finite n.
- Edge cases D_A=0 or D_B=0 do not rescue scalar reconstruction in the general two-nonzero case.
- This counterexample is entirely classical and product-structured: no entanglement, non-Markovianity, hidden environment, or exotic tensor rule is needed.

## Prior-art boundary
Non-tensorization of total variation over product distributions is known. In particular, Bhattacharyya et al. (2024, arXiv:2405.08255) explicitly contrast total variation with divergences such as KL, chi-square, and Hellinger that tensorize more directly; exact TV computation for product distributions has nontrivial complexity. Trace distance is the quantum extension of TV and has standard tensor-product subadditivity/contractivity properties. Therefore the mathematical non-tensorization mechanism is IMPORTED/KNOWN, not a PDT novelty claim.

## PDT consequence
A defensible PDT composition law cannot take only local scalar distinction values as sufficient statistics. It must retain additional operational structure (at minimum distribution/channel/experiment equivalence data, or a justified PDT-native invariant rich enough to determine composition). This strengthens the earlier joint-synergy and scalar-resource no-go results because it survives even after imposing conditional product structure.

## Classification
- universal scalar law D_AB=F(D_A,D_B): **FALSIFIED**
- equality D_AB=1-(1-D_A)(1-D_B): **FALSIFIED**
- exact binary counterexample: **PROVED**
- product bounds above: **PROVED / IMPORTED-KNOWN**
- non-tensorization mechanism: **IMPORTED/KNOWN**
- PDT-native sufficient compositional invariant: **OPEN**
- non-circular PDT-native n=3 derivation: **OPEN**
- fully specified same-input PDT-vs-QM quantitative deviation: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
