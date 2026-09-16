# Cycle 177 — Representation naturality forces uniformity, and full coarse-graining naturality is impossible

## Target
PDT-II targets (2) and (3): test whether a probability selector can be derived from an unlabeled finite distinction quotient by representation invariance / naturality, without importing preparation weights.

## Candidate A — isomorphism naturality
For every nonempty finite quotient Q, choose a probability distribution p_Q on Q. Require that for every bijection sigma: Q -> Q',

p_Q' = sigma_* p_Q.

## Theorem 177.1 — permutation naturality forces uniformity
For every nonempty finite Q, p_Q is uniform.

### Proof
Every permutation tau of Q is an automorphism. Naturality gives tau_* p_Q = p_Q. For any x,y in Q there is a transposition sending x to y, hence p_Q(x)=p_Q(y). Normalization then gives p_Q(x)=1/|Q| for all x.

This is exact for n=1,...,12 and all finite n. No numerical approximation is involved.

Classification: PROVED, but IMPORTED/KNOWN in substance (finite permutation invariance implies the discrete uniform distribution). Not PDT-native novelty.

## Consequence for n=3
On an unlabeled three-class quotient, the only isomorphism-natural selector is

(1/3, 1/3, 1/3).

Therefore representation invariance alone cannot encode a generic nonuniform qutrit preparation. Any nonuniform rule must contain additional preparation-dependent structure that breaks the S_3 symmetry.

Classification: PROVED boundary; general PDT-native n=3 derivation remains OPEN.

## Candidate B — naturality under every deterministic coarse-graining
A stronger proposal is to demand, for every map f: Q -> Q',

p_Q' = f_* p_Q.

This would make the selector commute with all deterministic quotient/refinement maps.

## Theorem 177.2 — no such normalized selector exists on all nonempty finite sets
Take Q={0,1} and Q'={*}. Let i_0,i_1: Q' -> Q select 0 and 1. Naturality for i_0 requires p_Q=delta_0; naturality for i_1 requires p_Q=delta_1, contradiction.

Equivalently, even the uniform family from Theorem 177.1 fails arbitrary-map naturality: for f:{1,2,3}->{a,b} with f(1)=f(2)=a and f(3)=b, pushing forward uniform_3 gives (2/3,1/3), not uniform_2.

Classification: FALSIFIED as a universal probability-selection principle. Smallest decisive counterexample uses cardinalities 1 and 2; the nonuniform-fiber witness uses 3 -> 2.

## Surviving restricted theorem
Uniform measures are preserved by maps with equal-size fibers: if f:Q->Q' is surjective and every fiber has size |Q|/|Q'|, then f_* uniform_Q = uniform_Q'. Thus a restricted naturality law survives for balanced coarse-grainings.

Classification: PROVED / IMPORTED-KNOWN.

## Resource and preparation implication
A physically useful PDT probability rule cannot be a function only of the isomorphism class of the bare distinction quotient. It must be defined on richer objects (Q,s), where s is independently operational preparation/resource data, and naturality must act simultaneously on Q and s. Otherwise symmetry forces uniformity; requiring compatibility with every coarse-graining is inconsistent.

This does not itself identify what s must be. If s is merely a probability vector, amplitude, density operator, GPT state, Gibbs weight, prior, or equivalent imported measure, target (2) has not been solved PDT-natively.

## Same-input PDT-vs-QM consequence
No same-input quantitative PDT/QM separation follows from representation invariance. On fully symmetric bare quotients PDT is forced to uniformity; on preparation-asymmetric cases the bare quotient omits exactly the information needed to select nonuniform weights. Choosing an extra symmetry-breaking weight by hand would insert the prediction.

Classification: target (3) remains OPEN; no inequality promoted.

## Composition consequence
Uniformity is compatible with Cartesian product for bare finite sets: uniform_{QxR}=uniform_Q tensor uniform_R. But this does not derive the physical PDT composite object or admissible relational resources; it only states a property after Cartesian composition is assumed.

Classification: CONDITIONAL + IMPORTED/KNOWN; target (1) remains OPEN.

## Prior-art boundary
Finite permutation invariance and uniform probability are standard. Pushforward of measures under maps is standard measure/probability theory. Categorical probability treats probability measures and deterministic maps through such pushforward/Markov-kernel structures. Therefore the two theorems above are boundary/obstruction results for PDT, not novelty claims.

## Stress-test ledger
- n=1: uniform selector unique; universal-map contradiction already appears when compared with n=2.
- n=2,...,12: S_n invariance forces exactly 1/n on each class.
- all finite n: same proof.
- degenerate singleton: consistent alone, but incompatible with universal naturality through both singleton injections into a 2-set.
- reversible groups: any transitive subgroup is sufficient for uniformity; multiple orbits leave inter-orbit weights free.
- arbitrary coarse-grainings: full naturality falsified.
- balanced surjections: uniform pushforward survives.
- pure/mixed, Markovian/non-Markovian, thermodynamic cases: bare quotient theorem is agnostic; adding these structures requires independently specified physical data and therefore cannot be claimed as derived here.

## Status
- Isomorphism-natural bare-quotient selector: PROVED -> uniform only.
- Universal deterministic-map naturality: FALSIFIED.
- Balanced coarse-graining naturality of uniform selector: PROVED / IMPORTED-KNOWN.
- PDT-native n=3 preparation law: OPEN.
- Same-input P_PDT != P_QM: OPEN.
- PDT-native composition law: OPEN.
- Gravity/capacity law: not attempted; no justified bridge.
- BREAKTHROUGH CANDIDATE: NO.

## Next strongest obligation
Search for the minimal independently physical enrichment s of a distinction quotient for which a selector p_(Q,s) is nonuniform, functorial under physically admissible maps, compositional without assuming a tensor rule, and not equivalent to importing a probability state. Attempt to prove a no-go theorem if every candidate enrichment reduces to an already-known state/measure representation.
