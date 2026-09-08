# Cycle 011 — Pairwise Calibration Closure dimension theorem

**Status: CONDITIONAL dimension theorem / PDT-native axiom candidate / group-base mathematics IMPORTED-KNOWN / NOT YET A BREAKTHROUGH**

## Motivation

Earlier dimension filters selected `n=3` only after adding algebraic Generator–Distinction Self-Duality, Generator Economy, or the finite-resolution Operational Self-Calibration inequality. This cycle asks whether PDT's primitive object — a *distinction pair* — can itself supply a more concrete calibration principle.

## Pairwise Calibration Closure (PCC)

Let the elementary distinction body be the Euclidean ball `B^n`, with full connected reversible isotropy group `SO(n)` acting in the standard way. PCC says that there exists an ordered pair of elementary reference states `(x,y)` such that the action of every connected reversible control is operationally identifiable from that pair:

`Phi_(x,y): SO(n) -> B^n x B^n`,

`Phi_(x,y)(g) = (g x, g y)`

is injective.

For a useful calibration pair, take `x,y` linearly independent. PCC is a candidate physical principle, not an established law.

## Theorem

Assume:

1. the elementary distinction body is `B^n`;
2. its full connected reversible isotropy is `SO(n)`;
3. Pairwise Calibration Closure holds;
4. connected reversible dynamics is genuinely noncommuting.

Then `n=3`.

### Proof

Two linearly independent reference vectors span a two-dimensional subspace `W`. Any rotation acting trivially on `W` and as an arbitrary element of `SO(n-2)` on `W^perp` fixes both reference vectors. Hence the pointwise stabilizer of a generic pair is isomorphic to `SO(n-2)`.

Therefore `Phi_(x,y)` is injective only if that stabilizer is trivial. For the connected special-orthogonal groups this requires `n-2 <= 1`, hence `n <= 3`.

On the other hand, `SO(1)` is trivial and `SO(2)` is abelian, while `SO(n)` is nonabelian for `n>=3`. Genuine noncommuting connected reversibility therefore requires `n>=3`.

Combining the two bounds gives

`n = 3`.

The converse calibration statement is explicit: in `R^3`, an orientation-preserving orthogonal transformation is uniquely fixed by its action on two linearly independent vectors, because the third oriented direction is determined by the first two.

## Stronger base-size statement

More generally, the minimal number of independent reference vectors needed to identify an arbitrary element of the natural `SO(n)` action is

`b_n = n - 1` for `n>=2`,

with `b_1=0` for the trivial group. If fewer than `n-1` independent references are supplied, a nontrivial `SO(n-r)` pointwise stabilizer remains; `n-1` independent vectors determine the last oriented direction and therefore the whole rotation.

Thus PCC (`b_n <= 2`) is equivalent to `n<=3`; adding noncommutativity isolates `n=3`.

## Computational and adversarial audit

`pdt_pairwise_calibration.py` records the exact stabilizer dimensions and constructs explicit nonidentity stabilizer rotations whenever `n>=4`. The test suite scans dimensions through 100 for the exact theorem and explicitly checks dimensions `4..12` by constructing rotations that fix both calibration references while changing the orthogonal complement. The manuscript-facing table is `results/cycle011_pairwise_calibration_dimension.csv`.

The scan gives exactly one dimension satisfying PCC plus genuinely noncommuting connected reversibility: `n=3`.

## Prior-art boundary

The group-theoretic concept is established: in permutation/group-action language a set whose pointwise stabilizer is trivial is a **base**, and base-size theory is a mature subject (see Bailey and Cameron, 2011, for a survey). Quantum process tomography and unitary characterization also study minimal probe sets; for example Baldwin, Kalev and Deutsch (Phys. Rev. A 90, 012110, 2014) derive reduced probe requirements for unitary maps. Existing generalized-Bloch-ball reconstructions select dimension three using composite-system, local-tomography, entanglement, or interacting-dynamics assumptions (for example Masanes et al., J. Math. Phys. 55, 122203, 2014).

The limited search in this cycle did not identify the exact PDT postulate "one primitive distinction pair must form a base for the full connected reversible isotropy group". That absence is **not** evidence of historical novelty. The mathematical theorem itself is elementary group-action geometry.

## Kill tests

1. PCC is not derived merely by naming two states; it is a substantive physical claim that a primitive distinction pair must suffice to calibrate all elementary reversible controls.
2. If calibration may use three or more independent reference states as dimension grows, PCC does not hold and the dimension conclusion disappears.
3. If the physical reversible group is a proper subgroup of `SO(n)` with base size at most two in higher dimension, PCC alone does not force `n=3`; full isotropy remains substantive.
4. If only control equivalence classes modulo a stabilizer are operationally relevant, the injectivity requirement is too strong and the theorem does not apply.
5. Existing group-base mathematics and quantum process-tomography results must not be relabeled as novel PDT mathematics.

## Research consequence

PCC is a more concrete and directly falsifiable dimension-selection principle than the entropy-exponent OSC hypothesis: prepare two noncollinear reference states, apply an unknown reversible control, and ask whether their outputs uniquely identify the control up to operational equivalence. In the full-isotropy Euclidean family, that calibration closure succeeds exactly through dimension three and fails from dimension four onward.

The remaining breakthrough requirement is to derive PCC from a deeper PDT composition/resource principle, or independently justify experimentally why *one primitive distinction pair* — rather than an arbitrarily growing reference frame — must be sufficient for an elementary system. Until then this is a strong conditional theorem, not a breakthrough claim.
