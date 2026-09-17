# Cycle 216 — Product closure + no-signalling + local tomography do not determine PDT composition

## Status

- **PROVED (conditional no-go)**: the listed axioms do not uniquely determine a composite.
- **IMPORTED/KNOWN**: the separating constructions are standard GPT/local-vs-no-signalling correlation structures.
- **FALSIFIED**: any PDT-II candidate claiming that local systems + product closure + no-signalling + local tomography uniquely force the joint distinction structure.
- **OPEN**: a genuinely PDT-native joint-admissibility law; non-circular n=3; same-input PDT-vs-QM prediction.
- **BREAKTHROUGH CANDIDATE: NO**.

## Claim attacked

Candidate composition principle:

> Given the local operational systems, require (i) all product preparations/effects, (ii) no-signalling, and (iii) local tomography. These conditions uniquely determine the composite operational state/effect structure.

This statement is false.

## Exact counterexample

Take the standard bipartite binary-input/binary-output Bell scenario. A behaviour is

\[
p(a,b\mid x,y),\qquad a,b,x,y\in\{0,1\}.
\]

Both of the following composite sets have the same local binary systems, contain product behaviours, are no-signalling, and are described entirely by joint local-setting statistics (hence are locally tomographic at the behaviour level):

1. **Local composite**: convex hull of deterministic local response functions
   \(a=f(x), b=g(y)\).
2. **No-signalling composite**: all normalized nonnegative behaviours obeying the no-signalling equalities.

They are not the same composite. Define correlators

\[
E_{xy}=\sum_{a,b}(-1)^{a+b}p(a,b\mid x,y)
\]

and CHSH

\[
S=E_{00}+E_{01}+E_{10}-E_{11}.
\]

Every deterministic local vertex has \(|S|=2\), so by convexity every local behaviour obeys \(|S|\le 2\). But the PR behaviour

\[
p(a,b\mid x,y)=\begin{cases}
1/2,&a\oplus b=xy,\\
0,&\text{otherwise}
\end{cases}
\]

is normalized and no-signalling and gives \(S=4\). Therefore the two composites satisfy the candidate structural requirements but are inequivalent.

Hence

\[
\boxed{\text{local data + product closure + no-signalling + local tomography}\not\Rightarrow\text{unique composite}.}
\]

## Why this matters for PDT-II

Cycle 215 showed that local distinction data alone do not determine the composite. Cycle 216 closes an obvious escape route: adding three powerful and physically familiar consistency requirements still does not determine it. PDT cannot obtain its composition law merely by declaring these constraints. It needs additional physical structure that selects which joint states/effects/transformations are admissible.

This also blocks a non-circular route to a distinguished `n=3`: if different joint completions survive the same local axioms, any dimension/count emerging only after choosing one completion inherits that choice unless PDT independently derives the selector.

## Prior-art boundary

This obstruction is not novel. Generalized probabilistic theory explicitly permits different composite tensor structures between minimal/local and maximal/no-signalling extremes. Local tomography is an additional axiom and does not by itself select the cone/state set. PR-box/boxworld correlations are the canonical witness that no-signalling permits correlations beyond the local polytope. Therefore this cycle is a rigorous falsification/filter, not a PDT breakthrough.

Relevant literature families to cite in PDT-II discussion: generalized probabilistic theories and minimal/maximal tensor products; Janotta & Lal (2013) on GPTs without the no-restriction hypothesis and generalized maximal tensor products; Hardy/Wootters and Barnum/Wilce on tomography/composition; standard Bell/PR-box literature.

## Stress-test scope

The binary Bell witness is already the smallest standard nontrivial correlation scenario needed for the claimed separation. Higher-dimensional embeddings are immediate: append unused local labels/outcomes/states or take direct products with spectator degrees of freedom. Such embeddings preserve the CHSH face and therefore preserve the inequivalence for dimensions through 12 and arbitrarily higher finite dimensions. This is an analytic embedding argument; no fabricated numerical outcome is claimed.

## Surviving theorem target

The next composition obligation is sharper. A PDT-native law must specify a resource-indexed joint admissibility map

\[
(\mathcal A_X,\mathcal A_Y,R)\mapsto \mathcal A_{XY,R}
\]

that is not merely one of the already-known GPT tensor choices and that has independently motivated physical content. Candidate selectors should next be attacked under stronger requirements such as purification, reversible-group closure, self-duality/spectrality, or an explicit resource-cost operational principle; each must be checked for whether it simply reconstructs known quantum/GPT axioms.
