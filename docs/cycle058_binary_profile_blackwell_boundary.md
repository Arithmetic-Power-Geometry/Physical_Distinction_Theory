# Cycle 058 — Augmented distinction profile is a canonical binary experiment

## Target
Determine whether the Cycle-057 augmented profile `(s, mu)` is genuinely PDT-native or whether it is already the canonical statistical structure of an ordinary binary experiment.

## Setup
Let `P,Q` be finite probability distributions. Define the singular mass

` s = P{i : Q_i = 0} `

and, on the regular sector `Q_i>0`, the finite likelihood ratio `lambda_i=P_i/Q_i`. Let

` mu = sum_{Q_i>0} Q_i delta_{lambda_i}. `

The pair `(s,mu)` was introduced in Cycle 057 because it recovers total variation exactly and closes under ordinary independent product composition.

## Theorem: canonicalization
Collapse every set of outcomes with the same finite likelihood ratio to one symbol, and collapse the entire `Q=0` sector to one singular symbol. The resulting binary experiment `(P_c,Q_c)` is

- for each finite likelihood ratio `lambda`: `Q_c(lambda)=mu(lambda)` and `P_c(lambda)=lambda mu(lambda)`;
- on the singular symbol: `Q_c(infty)=0` and `P_c(infty)=s`.

Then `(P,Q)` and `(P_c,Q_c)` are Blackwell-equivalent.

### Proof
The forward channel is deterministic: map each original outcome to its likelihood-ratio class, with every `Q_i=0` outcome mapped to the singular class.

For the reverse channel, condition inside each class. For a finite class `C_lambda`, set

`K(i|lambda)=Q_i / sum_{k in C_lambda} Q_k`.

Because `P_i=lambda Q_i` throughout that class, the same kernel reconstructs both hypotheses:

`Q_i = Q_c(lambda) K(i|lambda)` and `P_i = P_c(lambda) K(i|lambda)`.

On the singular class use

`K(i|infty)=P_i/s`

for `Q_i=0`; this reconstructs the singular P-mass and leaves Q zero there. Hence stochastic maps exist in both directions, so the two binary experiments are Blackwell-equivalent. QED.

## Consequence
The augmented profile `(s,mu)` is therefore not merely a convenient PDT composition summary. In the finite binary classical setting it is a complete canonical representative of the experiment up to Blackwell equivalence.

This is a decisive novelty boundary for PDT-II: any claimed breakthrough based only on `(s,mu)`, likelihood-ratio multiplication, posterior/likelihood canonicalization, or stochastic degradation of this binary profile would be a reformulation of established statistical-experiment structure unless PDT supplies an additional genuinely nonclassical state/effect/composition law.

## Exact audit
The branch script `cycle058_binary_experiment_canonical_profile.py` performs exact-rational checks. For each random pair it verifies:

1. canonicalization preserves the augmented profile;
2. arbitrary likelihood-preserving outcome splitting preserves the profile;
3. total variation is preserved under both canonicalization and splitting.

Results: 200 cases per dimension for `n=1..12`, plus 50 cases each for `n=16,24,32,48,64,96,128`; all recorded failure counts are zero. The theorem itself is algebraic; these tests are regression and adversarial implementation checks, not substitutes for proof.

## Prior-art boundary
Blackwell comparison of experiments and stochastic equivalence are established decision/statistical-experiment theory; likelihood ratios are standard sufficient statistics for binary experiments, and Le Cam/Torgersen comparison theory treats experiments modulo stochastic transformations. This cycle therefore explicitly rejects a novelty claim for the classical augmented-profile construction.

Relevant established background includes Blackwell's informativeness theorem (Blackwell 1951/1953), Le Cam's comparison/deficiency theory, and Torgersen, *Comparison of Statistical Experiments* (1991).

## Classification
- `PROVED`: finite canonicalization theorem above.
- `IMPORTED/KNOWN`: Blackwell equivalence, likelihood-ratio sufficiency/canonical experiment viewpoint.
- `FALSIFIED`: treating the classical augmented likelihood-ratio profile by itself as a PDT-native breakthrough composition law.
- `OPEN`: a genuinely PDT-native nonclassical distinction object with a composition law not reducible to an ordinary binary statistical experiment.
- `BREAKTHROUGH CANDIDATE`: no.
