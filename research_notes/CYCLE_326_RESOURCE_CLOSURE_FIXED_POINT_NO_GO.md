# PDT-II Cycle 326 — Resource-closure fixed-point underdetermination theorem

## Target
Attack the strongest surviving PDT-II route after Cycle 325: can a PDT-native closure equation on resource refinement derive a unique physical resource window, and thereby determine composition, select n=3, or force a same-input PDT/QM deviation?

## Setup
Let E be the universe of admissible elementary tests/effects/probes for a fixed microscopic model. Resource windows are subsets R subseteq E ordered by inclusion. A proposed refinement closure C:P(E)->P(E) is required to satisfy the standard closure axioms:

1. Extensive: R subseteq C(R).
2. Monotone: R subseteq S implies C(R) subseteq C(S).
3. Idempotent: C(C(R))=C(R).

A tempting PDT-II strategy is to declare the physical resource window to be a fixed point, or the least fixed point, of C.

## Theorem — Closure-fixed-point underdetermination
For every prescribed target resource window R* subseteq E, there exists an extensive, monotone, idempotent closure operator C_R* whose least fixed point is exactly R*.

### Proof
Define

C_R*(R) = R union R*.

Then:

- Extensivity: R subseteq R union R*.
- Monotonicity: if R subseteq S, then R union R* subseteq S union R*.
- Idempotence: (R union R*) union R* = R union R*.
- Fixed points are exactly those R satisfying R* subseteq R.
- Therefore the least fixed point is R* itself.

Since R* was arbitrary, closure axioms plus a least-fixed-point prescription do not select any particular physical resource window. Any desired answer can be encoded into the closure operator.

Status: PROVED.

## Stronger finite counterfamily
Take any finite E with |E|=m>=1. Every subset R* subseteq E can be made the least fixed point by the construction above. Hence there are at least 2^m distinct closure prescriptions with potentially different least physical windows. This is already decisive for the smallest nontrivial universe m=1: choosing R*=emptyset versus R*=E yields different least fixed points while satisfying the same closure axioms.

This is not a dimension-specific phenomenon. It embeds unchanged into operational models with state-space dimensions n=1 through n=12 and every higher finite n, because the proof concerns the resource-family lattice rather than coordinates of the state space.

## Alternative closure/composition stress
The no-go survives replacement of the resource window by any of the candidate classes considered in PDT-II:

- global versus local/product measurements;
- LOCC-like restricted classes versus unrestricted effects;
- injective/projective tensor-norm extremes;
- restricted-resource quotients;
- pure-state-only versus mixed-state-complete test families;
- Markovian versus history-aware/non-Markovian probes;
- controlled-environment record access;
- thermodynamic work/erasure constrained tests.

For any independently chosen target class R*, adjoining R* defines a valid closure with R* as least fixed point. Thus the fixed-point syntax does not explain why that target class, rather than another, is physical.

## Prior-art guard
This mathematical mechanism is standard closure-operator / complete-lattice theory. Fixed points of closure operations form complete lattices, and monotone self-maps on complete lattices fall under classical fixed-point theory. Therefore neither closure operators nor existence of least/fixed resource windows is claimed as PDT novelty.

## Consequences for PDT-II
1. "The physical resource window is the least fixed point of an extensive monotone idempotent refinement closure" does not derive a unique resource window unless the closure map C itself is independently fixed by PDT-native physics.
2. Choosing C so that its fixed point has a desired property (including n=3 or a desired composite norm) merely relocates the assumption into C and is circular.
3. The closure axioms contain no n dependence, so they cannot non-circularly select n=3.
4. They also contain no probability rule. Therefore they cannot alone entail P_PDT(O|I,R) != P_QM(O|I,R) for identical microscopic inputs and declared R.
5. They do not choose injective versus projective versus intermediate correlated-composite geometry.

## Classification
- Closure-fixed-point underdetermination theorem: PROVED.
- Generic closure/fixed-point machinery: IMPORTED/KNOWN.
- Closure axioms alone => unique resource window: FALSIFIED.
- Closure axioms alone => unique PDT composition: FALSIFIED as an inference.
- Closure axioms alone => n=3: FALSIFIED.
- Closure axioms alone => same-input PDT/QM quantitative deviation: FALSIFIED as an inference.
- PDT-native independently specified refinement generator/closure: OPEN.
- PDT-native correlated-composite selector: OPEN.
- Non-circular PDT-native n=3 derivation: OPEN.
- Same-input parameter-free PDT/QM prediction: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Smallest decisive counterexample
Let E={e}. Two operators obey exactly the same closure axioms:

C0(R)=R, whose least fixed point is emptyset;
C1(R)=R union {e}, whose least fixed point is {e}.

Thus uniqueness already fails in the one-generator resource universe. No numerical search can repair this without an additional independent physical axiom.

## Next strongest attack
Do not stack another generic closure/fixed-point axiom. Search instead for an independently motivated PDT-native refinement generator G whose action is determined from primitive distinction operations before any desired composite law, dimension, or quantum prediction is known. Then test whether iterating G closes to a unique resource family across adversarial alternative tensor rules and whether that closure produces any same-input numerical deviation from QM. If G must be chosen using the desired endpoint, record circularity rather than promoting it.