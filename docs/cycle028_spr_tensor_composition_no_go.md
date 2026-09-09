# Cycle 028 — Tensor-composition no-go for universal SPR

## Status

**PROVED + FALSIFIED + IMPORTED/KNOWN.** This cycle does **not** produce a BREAKTHROUGH CANDIDATE.

## Question attacked

Cycle 027 proposed Single-Plane Reversibility (SPR): every elementary infinitesimal reversible generator on an n-dimensional Euclidean distinction space has matrix rank at most 2. Together with noncommuting reversibility, this filters isolated SO(n) spaces to n=3. The present cycle asks whether that principle survives ordinary tensor-product composition.

## Theorem

Let subsystem A carry a nonzero single-plane generator A with rank(A)=2, and let subsystem B have dimension d_B. Under standard tensor-product composition, the local action on A lifts to

    A_comp = A \otimes I_B.

For matrices, the Kronecker-product rank identity gives

    rank(A \otimes I_B) = rank(A) rank(I_B) = 2 d_B.

Therefore

    rank(A_comp) <= 2  iff  d_B = 1.

Hence for every nontrivial spectator subsystem d_B >= 2, a perfectly ordinary local single-plane reversible operation becomes a rank-4-or-higher generator on the composite representation. Universal SPR on the full composite generator matrix is therefore incompatible with standard tensor composition.

## Explicit counterexample

Take the 2D rotation generator

    J = [[0,-1],[1,0]].

For a two-dimensional spectator,

    J \otimes I_2

has rank 4. This already falsifies universal composite SPR. Higher spectator dimension d_B produces rank 2 d_B.

## Dimensional and adversarial audit

The implementation checks local dimensions n=2..12 and spectator dimensions d_B=1..12. Every computed tensor-lift rank exactly matches 2 d_B. Unit tests extend the formula to spectator dimensions through 100, include local dimensions through 100 for the rank-2 generator itself, and test the degenerate zero-generator case. No numerical discrepancy was found in the local validation used before commit.

## Consequence for the n=3 program

The Cycle027 statement must now be narrowed: SPR+NCR can select n=3 only for an irreducible/single-system distinction representation, not as a universal rank condition imposed unchanged on standard tensor-product composites.

A possible repair is **factor-local SPR**:

    rank(A \otimes I_B) / d_B <= 2,

which exactly recovers rank(A)<=2 and is invariant under adding a spectator identity factor. This repair is mathematically consistent for local lifts, but it is currently only a candidate reformulation. It does **not** by itself derive n=3 from PDT composition, so it is classified OPEN as a PDT-native principle.

## Prior-art boundary

The proof uses the standard matrix identity rank(A \otimes B)=rank(A)rank(B), so the mathematics is not novel. A convenient reference is H. Zhang, "On the Kronecker Products and Their Applications," Journal of Applied Mathematics (2013), Article 296185. The novelty question, if any, concerns only whether a future PDT-native physical axiom naturally yields a factor-relative notion of elementary distinction rotation.

## Research decision

Do not promote universal SPR to a foundational PDT axiom in its Cycle027 form. Retain the isolated-space dimension filter as CONDITIONAL, and redirect the composition program toward factor-relative or quotient-level notions of elementary reversible support.
