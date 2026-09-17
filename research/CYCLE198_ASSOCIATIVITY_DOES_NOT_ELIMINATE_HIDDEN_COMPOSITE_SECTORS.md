# Cycle 198 — Associativity does not eliminate hidden composite sectors

## Target
PDT-II target (1): test whether three-system associativity, even when combined with resource refinement, forces the hidden composite sector found in Cycles 196–197 to vanish.

## Status
**PROVED (no-go)** / **FALSIFIED (associativity-is-sufficient conjecture)** / **IMPORTED/KNOWN boundary** / **OPEN (PDT-native composition law)**.

## Exact hypotheses
Let each elementary system i have a finite-dimensional accessible quotient Q_i. For every finite set S of elementary systems define a composite accessible vector space Q_S. Assume:

1. composition is associative up to the canonical relabelling/isomorphism, so Q_{(AB)C} ≅ Q_{A(BC)};
2. declared product effects from the elementary factors are represented;
3. resource refinement is monotone: adding allowed effects can distinguish more states but never identifies states already distinguished;
4. no local-tomography/minimality postulate is assumed.

Question: do 1–3 imply Q_{AB} ≅ Q_A ⊗ Q_B (equivalently, zero hidden sector)?

## Counterconstruction
They do not. For elementary systems indexed by i, choose arbitrary local spaces Q_i and for every unordered pair {i,j} choose an arbitrary finite-dimensional hidden pair sector H_{ij}. Define, for a finite composite S,

Q_S := (⊗_{i∈S} Q_i) ⊕ (⊕_{{i,j}⊆S} H_{ij}).

Declare elementary product effects to act on the first summand and annihilate every H_{ij}. Permit pair-resource refinements to add effects on the corresponding H_{ij}.

For three systems,

Q_{ABC} = Q_A⊗Q_B⊗Q_C ⊕ H_{AB} ⊕ H_{AC} ⊕ H_{BC}.

This definition depends only on the set of elementary constituents, not on parentheses. Therefore the two bracketings (AB)C and A(BC) are canonically identified by the ordinary tensor associator on the product sector and the identity/permutation of the labelled hidden sectors. Associativity therefore holds while hidden sectors remain nonzero.

Resource refinement is also monotone: the elementary product window sees only the tensor-product summand; admitting a pair effect on H_{ij} enlarges the separating dual space and cannot erase an existing distinction. Thus associativity + monotone refinement do not force H_{ij}=0.

## Smallest decisive witness
Take three one-dimensional locals Q_A=Q_B=Q_C=R and one one-dimensional hidden sector H_AB=R, with H_AC=H_BC=0. Then

- local dimensions: D_A=D_B=D_C=1;
- elementary product statistics have dimension 1;
- Q_ABC has dimension 2;
- both bracketings give the same two-dimensional composite;
- the hidden coordinate is invisible to all elementary product effects;
- a refined AB-resource can reveal it.

Hence associativity is satisfied exactly although local tomography fails.

## Dimension stress test
The construction is algebraic and dimension-independent. For local dimensions n=1,...,12 choose Q_i=R^n and any H_ij=R^h (h≥1). Then

dim Q_ABC = n^3 + 3h

when all three pair sectors have dimension h, independent of bracketing. The same construction extends to arbitrary finite n and arbitrary numbers of constituents. No numerical approximation is needed.

Degenerate cases are included: h=0 recovers the locally tomographic product; zero-dimensional optional hidden sectors are harmless; arbitrary invertible local reversible maps extend as tensor actions on the product sector together with independently chosen representations on H_ij. Norm choice does not change the linear no-go.

## Adversarial checks
- **Associativity:** survives because sectors are labelled by elementary subsets, not by parse tree.
- **Permutation of systems:** survives if equal-type hidden sectors are permuted with their labels.
- **Resource refinement:** survives by nested enlargement of the accessible dual effect span.
- **Higher arity:** one may additionally introduce H_T for triples or larger subsets T; associativity still does not remove them.
- **Attempted minimality rescue:** setting all H_T=0 is an extra minimality/local-tomography condition, already isolated in Cycle 197, not a consequence of associativity.

## Prior-art boundary
This mechanism must not be claimed as PDT novelty. Bilocal/n-local tomography and theories with holistic sectors are established GPT territory. Hardy & Wootters (2012; arXiv:1005.4870) show that real-vector-space quantum theory is bilocally tomographic while failing local tomography. Modern GPT literature explicitly defines n-local tomography and treats global parameters invisible to strictly local measurements. Therefore the present result is a no-go boundary for PDT, not a breakthrough claim.

Relevant prior art:
- L. Hardy and W. K. Wootters, “Limited Holism and Real-Vector-Space Quantum Theory,” Found. Phys. 42, 454–473 (2012), arXiv:1005.4870.
- GPT treatments of n-local tomography and tomographically nonlocal theories; real quantum theory is a standard bilocal example.

## Consequence for PDT-II
The conjecture

> three-system associativity + monotone PDT resource refinement ⇒ no hidden global distinction sector

is **FALSIFIED**.

A PDT-native composition theorem must add a physically derived constraint stronger than mere associativity/refinement. Candidate constraints must be tested against known bilocal/n-local GPTs and cannot simply rename local tomography, minimality, or no-restriction.

## Next strongest obligation
Prove-or-falsify whether a genuinely PDT-defined *resource-generation rule* can constrain which subset-labelled hidden sectors H_T are physically creatable/revealable, rather than merely declaring them absent. Any proposed rule must be checked against real quantum theory, bilocal/n-local tomography, superselection examples, and identical-input QM/GPT models.

**BREAKTHROUGH CANDIDATE: NO.**
