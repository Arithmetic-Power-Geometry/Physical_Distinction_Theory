# Cycle 204 — Dynamical closure is lumpability, not a PDT selection principle

## Status

- Conditional theorem: **PROVED**
- Claim that quotient/dynamics compatibility uniquely selects a PDT quotient: **FALSIFIED**
- Mathematical boundary: **IMPORTED/KNOWN** (Markov lumpability / probabilistic bisimulation)
- PDT-native composition law: **OPEN**
- Non-circular PDT-native n=3 derivation: **OPEN**
- Same-input PDT/QM probability separation: **OPEN**
- Breakthrough candidate: **NO**

## Question attacked

Cycle 203 showed that a deterministic microscopic map does not select the resource-relative quotient. A natural strengthening is to demand *dynamical closure*: the resource quotient must support autonomous observable dynamics. Does that requirement select the quotient?

No. In stochastic dynamics the requirement is exactly the established strong-lumpability condition, and a single microscopic process can possess several inequivalent lumpable partitions.

## Theorem 204.1 — quotient-autonomy criterion

Let `X` be a finite microscopic state set, `P(x,y)` a Markov transition kernel, and `q:X -> Y` a surjective resource observation map. Let `B_y=q^{-1}(y)` be its blocks.

An autonomous Markov kernel `K` on `Y` satisfying

`Pr[q(X_{t+1})=y' | X_t=x] = K(q(x),y')`

for every microscopic state `x` exists **iff**, for every block `B_y`, every `x,x' in B_y`, and every target block `B_z`,

`sum_{u in B_z} P(x,u) = sum_{u in B_z} P(x',u)`.

When it exists, the common block sum defines `K(y,z)`.

### Proof

Necessity follows because both sides must equal `K(y,z)` whenever `q(x)=q(x')=y`. Sufficiency follows by defining `K(y,z)` as that common block-transition probability. Nonnegativity is inherited from `P`, and summing over all target blocks gives one. QED.

This is the classical strong-lumpability criterion; it is therefore not a PDT-native theorem.

## Smallest decisive counterexample to uniqueness

Take microscopic state space `X={00,01,10,11}` and the bit-flip-symmetric random walk

`P(x,x)=1-2a`,
`P(x,x xor 01)=a`,
`P(x,x xor 10)=a`,

with `0 <= a <= 1/2`.

Two inequivalent quotient maps are simultaneously autonomous:

1. `q_parity(x)=x1 xor x2`, with two operational states.
2. `q_weight(x)=x1+x2`, with three operational states `{0,1,2}`.

For parity, each state has probability `2a` to change parity and `1-2a` to retain it, so the quotient kernel is

`[[1-2a,2a],[2a,1-2a]]`.

For Hamming weight, states `01` and `10` lie in the same block and have identical aggregate transition probabilities: from weight 1, probability `a` goes to weight 0, `a` to weight 2, and `1-2a` remains at weight 1. Hence this quotient is also strongly lumpable.

The two quotients have different cardinalities and different operational transition kernels while using the **same microscopic input P**. Therefore even requiring exact autonomous Markov dynamics does not select the PDT resource quotient.

At `a=0` the dynamics are degenerate and every partition is lumpable, strengthening rather than removing nonuniqueness. At `a=1/2` the self-loop vanishes and both displayed quotients remain valid.

## Dimension stress boundary

The witness embeds into every finite microscopic state space of size `n>=4` by adjoining states that are fixed or form symmetry-respecting blocks. Thus no test through `n=12`, nor higher-dimensional embedding, can turn quotient-autonomy alone into uniqueness. The obstruction is structural rather than numerical.

For `n<4`, uniqueness is still not generally guaranteed: identity dynamics make every partition dynamically closed. Consequently the failure is present already in degenerate dimensions and has a nondegenerate four-state witness.

## Prior-art boundary

The block-sum criterion above is strong Markov lumpability (Kemeny–Snell lineage). In labelled probabilistic systems the analogous equivalence is probabilistic bisimulation. Therefore neither the criterion nor quotient minimisation should be promoted as PDT novelty.

## Consequence for PDT-II

Adding any of the following is insufficient by itself:

- microscopic dynamics;
- quotient compatibility;
- exact Markovian closure;
- choosing a coarsest or finest compatible quotient without an independent physical reason.

A PDT-native composition derivation now requires an independently motivated **distinction-selection principle** that selects which dynamically admissible equivalence relation is physically accessible under resource `R`. Such a principle must not merely restate lumpability, bisimulation, local tomography, or minimality.

The same-input probability target remains blocked: before `P_PDT(O|I,R)` can differ defensibly from quantum theory, PDT must independently determine the event/quotient structure and response law under the same declared microscopic input and resource window.
