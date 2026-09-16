# Cycle 175 — Automorphism-orbit boundary for PDT probability selectors

## Target attacked
PDT-II targets (2) and (3): whether operational distinction symmetry can supply the missing preparation-sensitive probability selector without importing Hilbert amplitudes, density matrices, GPT states, or an arbitrary prior.

## Candidate principle
Let a preparation/resource specification determine a finite operational quotient Q and let G be the automorphism group preserving all declared PDT data. Candidate claim: requiring the outcome probability vector p to respect every automorphism in G uniquely selects p.

## Exact hypotheses
Let Q be finite, |Q|=n, and G act on Q by permutations. A probability p:Q->[0,1] is admissible when sum_x p(x)=1 and p(gx)=p(x) for all g in G and x in Q. No Hilbert/projector/amplitude structure is assumed.

## Theorem 175.1 — Orbit-simplex theorem
If the action of G on Q has k orbits O_1,...,O_k, then the G-invariant probability measures form a simplex of dimension k-1. Explicitly, every invariant p has

p(x)=w_j/|O_j| for x in O_j,

where w_j>=0 and sum_j w_j=1. Hence symmetry uniquely selects a probability distribution iff k=1 (the action is transitive).

### Proof
Invariance implies p is constant on each orbit: if x,y lie in the same orbit, y=gx for some g and p(y)=p(gx)=p(x). Let the common value on O_j be a_j. Normalization gives sum_j |O_j| a_j=1. Set w_j=|O_j|a_j. Conversely every probability vector w on the k orbit labels defines an invariant p by p(x)=w_j/|O_j|. Thus invariant measures are affinely isomorphic to Delta_{k-1}. QED.

## Smallest decisive counterexample
Q={0,1,2}, with G={id,(01)}. The orbits are {0,1} and {2}. Every

p_a=(a/2,a/2,1-a), 0<=a<=1,

is G-invariant. For example p=(1/4,1/4,1/2) and q=(1/3,1/3,1/3) obey the identical declared symmetry but disagree quantitatively. Therefore covariance/invariance under the full automorphism group does not in general determine probabilities.

A two-point quotient also witnesses nonuniqueness whenever the preparation breaks the swap symmetry and the stabilizer is trivial; then the full one-simplex survives. The n=3 witness is emphasized because PDT-II explicitly seeks a non-circular n=3 derivation.

## Dimension stress test
The theorem is analytic for every finite n and therefore exactly covers n=1..12 and all higher finite n. For every n>=3 choose G=S_{n-1} acting on {1,...,n-1} while fixing n. Then k=2 and the invariant family is

p_a(i)=a/(n-1) for i<n, p_a(n)=1-a.

Thus one continuous degree of probability freedom survives at every tested dimension. More generally any action with k>=2 leaves k-1 free orbit weights.

## Edge / adversarial cases
- n=1: k=1, unique delta measure; trivial.
- Transitive G: k=1, uniform distribution is uniquely forced, but only for a fully symmetry-invariant preparation/resource specification.
- Trivial G: k=n, the entire Delta_{n-1} survives.
- Pure preparation labels typically reduce the stabilizer and therefore increase, not remove, probability freedom.
- Mixed preparations do not help unless extra mixture weights are supplied; those weights are already probabilistic structure.
- Reversible groups with several operational orbits leave inter-orbit weights undetermined.
- Product/composite actions inherit orbit structure; transitivity of each local action is an additional condition and does not derive the physical composite rule.
- Different norms or metrics can alter G, but once G is fixed the theorem applies unchanged; a metric does not determine inter-orbit weights unless an additional measure principle is supplied.

## Consequence for same-input PDT vs QM
Automorphism symmetry alone cannot generate a defensible P_PDT(O|I,R) != P_QM(O|I,R). Choosing different orbit weights would stipulate the discrepancy. A quantitative PDT prediction requires an independently derived rule fixing the orbit weights for arbitrary preparations.

## Prior-art boundary
The mathematical mechanism is standard group-action/invariant-measure reasoning and is not claimed as PDT novelty. Symmetry can force equal probabilities within a transitive orbit, but it does not generally assign probability mass between distinct orbits. Quantum probability uniqueness in dimension >=3 instead uses substantially richer Hilbert/projector event structure plus additive/noncontextual measure assumptions (Gleason-type results). Importing those assumptions would not be a PDT-native n=3 derivation.

## Status
- Theorem 175.1 (orbit-simplex characterization): PROVED.
- Claim that automorphism symmetry uniquely selects arbitrary PDT preparation probabilities: FALSIFIED.
- Uniformity under a transitive preparation-preserving action: CONDITIONAL.
- Group-action/invariant-measure mathematics and Gleason-type uniqueness under Hilbert assumptions: IMPORTED/KNOWN.
- PDT-native rule fixing inter-orbit weights: OPEN.
- Same-input PDT/QM quantitative disagreement: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Strongest surviving obligation
A successful PDT-native selector must determine probability mass *between* operational symmetry orbits from independently motivated physical distinction data. Any candidate scalar/vector/tensor must be checked for whether it merely re-encodes an arbitrary prior, density matrix, amplitude, GPT state, energy Gibbs weight, or other imported measure. Attack this inter-orbit-weight problem before claiming an n=3 derivation or a PDT/QM prediction gap.