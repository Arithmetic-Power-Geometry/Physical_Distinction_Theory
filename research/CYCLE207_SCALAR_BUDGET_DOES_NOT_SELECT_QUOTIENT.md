# Cycle 207 — Scalar quotient budget does not select a PDT quotient

## Status

- **PROVED (conditional no-go)**: for the natural scalar budget `cost(q)=number of quotient blocks`, microscopic dynamics + exact autonomous quotient dynamics + a fixed scalar budget does not select a unique quotient.
- **FALSIFIED**: the candidate rule “choose an exactly dynamically admissible quotient at a prescribed scalar block budget” as a unique PDT distinction-selection principle.
- **IMPORTED/KNOWN**: exact autonomous finite-state quotient dynamics is strong lumpability / probabilistic bisimulation machinery.
- **OPEN**: a PDT-native resource functional derived independently from microscopic physics that breaks the surviving quotient degeneracy without encoding the desired distinction structure.
- **BREAKTHROUGH CANDIDATE: NO**.

## Exact hypotheses

Let `X={0,1,2,3}` and let the microscopic deterministic dynamics be

`f(0)=0, f(1)=0, f(2)=2, f(3)=2`.

A partition `Pi` is dynamically admissible when every pair of states in one block is mapped by `f` into one common block. This is the deterministic specialization of strong lumpability. Define the scalar resource cost by

`c(Pi)=|Pi|`,

the number of accessible operational states/blocks. Fix budget `c=2`.

## Two same-input, same-budget admissible quotients

Partition A:

`Pi_A={{0,1},{2,3}}`.

Its induced two-state dynamics is identity: the first block maps to itself and the second block maps to itself.

Partition B:

`Pi_B={{0,1,2},{3}}`.

It is also dynamically admissible: every state in the first block maps into the first block, and state 3 also maps into the first block. Its induced two-state dynamics is constant-to-first-block.

Both have exactly the same microscopic dynamics and exactly the same scalar budget `c=2`, but their quotient dynamics are not isomorphic: the identity quotient has two fixed operational states, whereas the constant quotient has only one fixed operational state. The number of fixed points is invariant under relabelling, so no permutation of the two quotient labels identifies the two induced dynamics.

Therefore microscopic dynamics + exact lumpability + this scalar resource budget does not uniquely select the operational quotient.

## Dimension stress boundary

The witness is already nontrivial at microscopic cardinality 4. It embeds into every `n>=4` by adding states `4,...,n-1` as additional fixed points and placing all added states in the first block of both partitions. Thus the same two-block ambiguity survives exactly for `n=4,...,12` and all higher finite `n`.

For `n<4`, this specific witness is unavailable; no claim of minimality below four states is made here without exhaustive enumeration.

## What survives

A scalar budget can restrict a family of quotients, but a scalar constraint does not in general identify which distinctions are physically accessible. To obtain uniqueness PDT must derive additional structure: e.g. a resource-dependent observation/effect mechanism or a cost functional sufficiently discriminating to select among same-dynamics admissible quotients. Such a functional cannot be chosen merely to recover the desired `n=3` result without circularity.

## Consequence for PDT-II

This closes the proposed shortcut “dynamics + quotient-state-count budget => unique PDT quotient.” It does **not** establish that every conceivable real-valued PDT resource functional fails; that stronger universal statement would be false without restrictions because an injective scalar encoding could trivially label every partition. The scientifically relevant remaining obligation is therefore to derive the resource functional independently and test whether it produces nontrivial, non-circular quotient selection and eventually a same-input prediction distinct from QM.
