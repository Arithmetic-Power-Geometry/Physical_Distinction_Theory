# Cycle 312 — Exact branching selector collapses to Shannon

## Target attacked
PDT-II (1) PDT-native composition law, with consequences for (2) non-circular n=3 and (3) same-input PDT/QM prediction.

## Candidate
Let F assign a nonnegative real number to every finite probability vector. Assume:

1. relabelling invariance;
2. continuity on every finite simplex;
3. null-event invariance, F(p,0)=F(p);
4. exact physical branching/refinement:

   F(p_1,...,p_{k-1},p_k q_1,...,p_k q_m,p_{k+1},...,p_n)
   = F(p_1,...,p_n) + p_k F(q_1,...,q_m).

The tempting PDT claim is that these requirements furnish a new PDT-native scalar composition law and perhaps privilege arity three.

## Result
**FALSIFIED as a PDT-native novelty/arity selector.** Under the stated regularity assumptions the candidate is the classical Faddeev/Leinster characterization: F is a nonnegative constant multiple of Shannon entropy,

F(p) = c[-sum_i p_i log p_i].

Hence exact branching is mathematically strong enough to select a scalar functional, but the selected functional is imported/known information theory and exists uniformly at every finite arity. It does not select n=3 and supplies no parameter-free same-input deviation from quantum mechanics.

## Exact algebraic stress test
For Shannon H and refinement R_k(p,q),

H(R_k(p,q)) - H(p) - p_k H(q) = 0

by expanding log(p_k q_j)=log p_k+log q_j. This proof is dimension independent and includes deterministic and zero-probability branches by 0 log 0 := 0.

The accompanying script `tests/cycle312_branching_selector_stress.py` tests n=1..12, every branch, deterministic/degenerate distributions, and randomized rational probability vectors. It is a regression/stress test of the exact identity, not evidence of novelty.

## Counterexample to n=3 selection
For every n>=1, H_n is defined on Delta_{n-1} and satisfies the same branching identity. Therefore the premise set admits n=1,2,3,... simultaneously. In particular, the implication

exact branching + symmetry + continuity => n=3

is false.

## Prior-art rejection
The uniqueness result is the Faddeev characterization of Shannon entropy and modern Leinster formulations. Baez–Fritz–Leinster also characterize Shannon information loss from functoriality, convex linearity and continuity. Operadic formulations encode the same substitution/chain rule. Therefore this route must not be presented as a PDT invention.

Relevant literature checked in this cycle:
- D. K. Faddeev, *On the concept of entropy of a finite probabilistic scheme* (1956).
- J. C. Baez, T. Fritz, T. Leinster, *A Characterization of Entropy in Terms of Information Loss*, Entropy 13 (2011), 1945–1957; arXiv:1106.1791.
- Modern Faddeev/Leinster statement: relabelling invariance + continuity + chain rule imply a constant nonnegative multiple of Shannon entropy.

## Surviving theorem/status
- Exact branching identity for Shannon at arbitrary finite arity: **PROVED / IMPORTED-KNOWN**.
- Uniqueness under Faddeev-type hypotheses: **IMPORTED/KNOWN**.
- Exact branching as a genuinely PDT-native new composition law: **FALSIFIED**.
- Exact branching as an n=3 selector: **FALSIFIED**.
- Exact branching alone as a source of P_PDT != P_QM: **FALSIFIED**.
- A PDT-native composition principle not equivalent to an established entropy/divergence characterization: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Parameter-free same-input PDT/QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
Do not keep strengthening the Faddeev/Shannon route. Search for composition data that are operationally richer than one scalar branching functional—e.g. compatibility-sensitive or sequential structures—and immediately compare any candidate against existing GPT, information-geometric, categorical, and resource-theoretic composition laws before promoting it.
