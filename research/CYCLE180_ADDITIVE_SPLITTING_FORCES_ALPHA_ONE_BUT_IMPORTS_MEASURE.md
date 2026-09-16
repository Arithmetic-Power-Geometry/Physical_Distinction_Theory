# Cycle 180 — Additive splitting forces alpha=1, but only by importing measure structure

## Status

- Functional theorem: **PROVED**
- PDT-native derivation: **FALSIFIED as currently motivated**
- Prior-art status: **IMPORTED/KNOWN** (finite additivity / positive measure and Luce-type normalized weights)
- Same-input PDT–QM gap: **OPEN**
- Breakthrough candidate: **NO**

## Question

Cycle 179 proved that continuity plus independent-composite multiplicativity reduces a positive response functional to

\[
F(x)=x^\alpha,
\]

but leaves \(\alpha\) undetermined. The strongest next question is whether a physically justified splitting/refinement principle fixes \(\alpha=1\) without assuming the desired probability measure.

## Candidate splitting axiom

Let \(F:\mathbb R_{>0}\to\mathbb R_{>0}\) satisfy:

1. normalization: \(F(1)=1\);
2. continuity;
3. independent composition: \(F(xy)=F(x)F(y)\);
4. additive splitting: whenever a physical record of size \(x+y\) is refined into disjoint subrecords of sizes \(x,y\),
   \[
   F(x+y)=F(x)+F(y).
   \]

## Theorem

Under hypotheses 1–4,

\[
\boxed{F(x)=x\quad\text{for all }x>0.}
\]

Hence the Cycle-179 power family has uniquely \(\alpha=1\).

### Proof

Additivity and \(F(1)=1\) give \(F(n)=n\) for every positive integer \(n\). Since

\[
1=F(1)=F(n\cdot 1/n)=F(n)F(1/n),
\]

we have \(F(1/n)=1/n\). Additivity then gives \(F(m/n)=m/n\) for positive rationals. Continuity extends this equality from the dense positive rationals to every positive real. Therefore \(F(x)=x\). QED.

The multiplicativity assumption is actually redundant once positive finite additivity, normalization, and continuity are imposed; this is important for novelty assessment.

## Counterexample search against weaker splitting principles

A weaker requirement that merely preserves total normalized probability after a split does **not** fix \(\alpha\). For any \(\alpha>0\), assigning split descendants \(x,y\) weights \(x^\alpha,y^\alpha\) and renormalizing remains a valid probability distribution. Thus the decisive content is specifically the unnormalized identity

\[
F(x+y)=F(x)+F(y),
\]

not the generic idea of refinement.

Smallest witness: split a record of size 2 into 1+1. The power family requires

\[
2^\alpha=1^\alpha+1^\alpha=2,
\]

so \(\alpha=1\). This witness already occurs before any n=3 construction.

## Dimension stress test

For any finite outcome count \(n\), including n=1,...,12, if positive record sizes \(s_i\) are additive under disjoint union, the theorem gives

\[
P_i=\frac{s_i}{\sum_j s_j}.
\]

No new dimension-dependent freedom appears. Degenerate zero-weight records require extending F continuously to 0, yielding F(0)=0. Independent composites with product record size satisfy

\[
P_{ij}=\frac{s_i t_j}{\sum_{k,l}s_k t_l}=P_iP_j.
\]

These are consistency checks, not evidence of a new physical law.

## Decisive PDT-native boundary

The theorem does **not** solve the PDT-II probability problem. The splitting axiom already says that the enriched scalar is a finitely additive measure over disjoint alternatives. Normalizing such a measure to obtain probabilities is standard measure/probability structure. Therefore using this axiom without an independent PDT derivation would import the missing measure rather than derive it from distinction geometry.

In particular, it would be circular to define \(s_i\) as probability mass, Born weight, squared amplitude, density-operator expectation, GPT effect value, Gibbs weight, or any monotone transform selected because it reproduces a desired distribution.

## Prior-art boundary

Luce-type representations already normalize positive ratio-scale values as

\[
P(i\mid S)=\frac{v(i)}{\sum_{j\in S}v(j)}.
\]

Finite additivity of disjoint-event weights is foundational probability/measure structure. Therefore the algebraic uniqueness result is **IMPORTED/KNOWN**, not a PDT breakthrough.

## Consequence for PDT-II

The strongest surviving obligation is no longer to choose an exponent. It is:

> Derive, from independently operational PDT primitives, a non-probabilistic physical quantity s that is experimentally measurable, composes under declared operations, and whose disjoint physical refinement is provably additive — without defining s through probability/amplitude/state weights.

Only then would alpha=1 follow non-circularly. Until such an s exists, no same-input quantitative PDT–QM discrepancy is defensible.

## Classification ledger

| Claim | Classification |
|---|---|
| continuous normalized additive response is F(x)=x | PROVED |
| additive splitting fixes Cycle-179 alpha to 1 | PROVED |
| generic normalized refinement alone fixes alpha | FALSIFIED |
| finite-additive weight normalization is PDT novelty | IMPORTED/KNOWN |
| PDT currently derives the required additive physical scalar from distinctions | OPEN |
| same-input P_PDT != P_QM follows | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Next attack

Test whether any candidate PDT-native scalar already present in the repository (distinction count, quotient rank, orbit size, distinguishability radius, capacity, resource cost) satisfies exact disjoint-refinement additivity while also behaving correctly under composites, coarse-graining, reversible groups, mixed states, controlled environments, and thermodynamic embeddings. The first obligation is adversarial: search for the smallest failure of additivity before attempting a probability derivation.
