# Cycle 178 — Scalar-enrichment selector nonuniqueness

## Target attacked
The strongest surviving PDT-II probability obligation after Cycle 177: can a minimal independently physical scalar enrichment of each distinction class determine a nonuniform probability selector without importing a probability vector?

## Status
- Scalar-enrichment uniqueness: **FALSIFIED**.
- Family theorem below: **PROVED**.
- Luce/Bradley–Terry proportional-weight representation: **IMPORTED/KNOWN** (not PDT novelty).
- PDT-native probability selector: **OPEN**.
- Same-input PDT-vs-QM quantitative prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Hypotheses
Let Q={1,...,n}, n>=2, be a finite operational distinction quotient. Attach to each class a strictly positive scalar s_i>0, interpreted only as an independently measurable physical salience/intensity/resource attribute. Require a probability selector to be: (i) normalized and strictly positive; (ii) permutation equivariant; (iii) continuous in s; and (iv) scale invariant under s -> c s for c>0.

## Theorem — nonuniqueness under scalar enrichment
For every alpha>0,

    p_i^(alpha)(s) = s_i^alpha / sum_j s_j^alpha

satisfies all four hypotheses. If s is nonconstant and alpha != beta, then p^(alpha)(s) != p^(beta)(s). Therefore positive scalar enrichment + normalization + positivity + permutation equivariance + continuity + common-scale invariance does not determine a unique probability law.

### Proof
Normalization and positivity are immediate. For any permutation pi, permuting coordinates of s permutes numerator and denominator in the same way, so the selector is equivariant. Continuity follows from positivity of the denominator. Common scaling gives (c s_i)^alpha/sum_j(c s_j)^alpha = p_i^(alpha). For nonconstant s choose i,j with s_i/s_j != 1. Then p_i^(alpha)/p_j^(alpha)=(s_i/s_j)^alpha, which differs from (s_i/s_j)^beta when alpha!=beta. QED.

## Smallest decisive counterexample
n=2, s=(1,2):

- alpha=1 gives p=(1/3,2/3).
- alpha=2 gives p=(1/5,4/5).

The distinction quotient, scalar physical data, normalization, positivity, relabeling covariance, continuity and scale invariance are identical. The predictions differ.

## n=1..12 and higher-dimensional stress test
n=1 is the degenerate unique distribution. For every n>=2, choose s=(1,2,1,...,1); alpha=1 and alpha=2 remain distinct, so the obstruction holds analytically for n=2 through n=12 and every finite higher dimension. No numerical approximation is needed.

Edge cases: if all s_i are equal, every alpha gives the uniform law, recovering the Cycle-177 symmetry boundary. If zero scalars are admitted, support conventions add further structure rather than restoring uniqueness.

## Stronger boundary
A ratio axiom such as

    p_i/p_j = s_i/s_j

would select p_i=s_i/sum_j s_j, but that is an additional substantive axiom. It is mathematically the familiar Luce/Bradley–Terry proportional-weight form, so adopting it without a PDT derivation would import a known selection principle rather than solve PDT-II.

More generally, any chosen response map F can produce p_i=F(s_i)/sum_j F(s_j). The physical meaning of s does not by itself determine F.

## Consequence for n=3
For qutrit-like Q={1,2,3}, scalar enrichment does not give a non-circular PDT-native derivation. With s=(1,2,3), alpha=1 yields (1/6,2/6,3/6), while alpha=2 yields (1/14,4/14,9/14). A desired distribution cannot be selected by choosing alpha after seeing the target.

## Consequence for same-input PDT != QM
A same-input discrepancy cannot be claimed by taking a quantum microscopic input, extracting a scalar s, and arbitrarily choosing alpha or F. Unless PDT independently derives both the physical scalar and the response functional, the discrepancy is model choice rather than prediction.

## Prior-art boundary
Luce's choice axiom is a classical representation in which positive scale values v_i yield P(i|S)=v_i/sum_{j in S}v_j. Bradley–Terry and multinomial-logit/softmax families are closely related established constructions. Therefore proportional normalization of positive weights is IMPORTED/KNOWN, not a PDT breakthrough.

## Surviving strongest obligation
PDT must derive a response functional from an independently physical distinction process, or prove a stronger operational axiom that uniquely fixes it and is not equivalent to importing an existing probability/choice representation. Candidate next attacks: sequential composition/coarse-graining consistency of response maps; multiplicativity under independently composed scalar records; and whether these force a power family but leave an undetermined exponent, or force an imported Luce form.
