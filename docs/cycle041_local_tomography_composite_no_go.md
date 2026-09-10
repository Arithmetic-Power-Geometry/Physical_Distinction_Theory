# Cycle 041 — Local tomography does not determine the composite

## Target

PDT-II target (1): derive or falsify candidate PDT-native composition principles before using them in dimension selection or experimentally distinctive predictions.

## Exact hypotheses under attack

Suppose two identical elementary operational systems each have an `(n+1)`-dimensional real vector representation (normalization plus `n` binary fiducial expectation coordinates), and suppose the composite is locally tomographic so that its ambient vector space is the tensor product with dimension `(n+1)^2`.

Candidate claim under test:

> Local tomography together with multiplicative vector-space dimension and preservation of product states determines the physical composite state space.

## Counterexample family

Use the standard `n`-input hypercube bit.  The same local systems admit at least two inequivalent composite cones/state spaces inside the same locally tomographic tensor-product vector space.

1. **Minimal tensor product:** convex mixtures of product states.  Every CHSH expression formed from two binary settings obeys `|S| <= 2`, because the extremal local deterministic assignments obey that bound and convex mixing cannot increase it.
2. **Maximal/no-signalling tensor product:** for every `n>=2`, embed a PR box in the first two settings,

   `p(a,b|x,y)=1/2` when `a xor b = x*y`, and `0` otherwise for `x,y in {0,1}`,

   while taking uniform independent outcomes on all other setting pairs.  This distribution is exactly normalized and no-signalling and gives

   `E00=E01=E10=1, E11=-1`, hence `S=4`.

Both composites use the same local vector spaces and the same locally tomographic ambient vector dimension `(n+1)^2`, yet their allowed joint states and experimentally available correlations differ.

## Smallest decisive counterexample

`n=2` binary fiducial settings per party.

- local vector dimension: `3`;
- locally tomographic composite vector dimension: `9`;
- minimal-composite CHSH maximum: `2`;
- maximal-composite PR witness: `4`.

Therefore the candidate uniqueness claim is false.

## Dimension stress test

The exact dependency-free implementation audits `n=1..12`.  `n=1` has no CHSH pair of settings and is therefore not a witness.  Every `n=2..12` contains the same embedded PR witness, with exact rational normalization and exact no-signalling marginals.  The construction extends immediately to arbitrary `n>=2` by leaving additional settings uniform.

## Surviving theorem / PDT-II consequence

**PROVED no-go.** Multiplicative scalar/vector capacity and local tomography constrain only the ambient linear representation.  They do not determine the positive cone, admissible joint state set, admissible effect set, or nonlocal correlation structure.

Hence any PDT-native composition law strong enough for PDT-II must specify or derive additional order/positivity structure (or an operational principle equivalent to it).  A scalar composition rule, even when upgraded to local tomography, cannot by itself support a unique physical prediction.

This also blocks an invalid shortcut toward target (5): one cannot infer a PDT Bell/Tsirelson-type inequality from local dimensional bookkeeping alone.  The inequality depends on which composite cone/effect structure PDT actually derives.

## Prior-art boundary

The mathematical distinction between minimal and maximal tensor products in generalized probabilistic theories and the use of boxworld/PR correlations are established prior art.  In particular, GPT literature explicitly treats the minimal composite as the convex hull of product states and the maximal composite as the largest state cone compatible with product effects/no-signalling; boxworld provides maximally nonlocal PR correlations.  Therefore **no historical novelty is claimed for this mathematics**.

The PDT-specific contribution of this cycle is only the explicit no-go boundary in the PDT-II theorem ledger: **local tomography is insufficient to finish PDT composition.**

## Classification

- `PROVED`: exact minimal-vs-maximal operational separation.
- `FALSIFIED`: uniqueness from local tomography + multiplicative dimension + product preservation.
- `IMPORTED/KNOWN`: GPT tensor-product and PR-box mathematics.
- `BREAKTHROUGH CANDIDATE`: **NO**.

## Next strongest surviving target

Derive a PDT-native principle that selects an order/effect structure between the minimal and maximal tensor products without simply importing quantum positivity, self-duality, purification, or the desired Bell bound.  Only after such a principle survives counterexample and prior-art checks can composition be used non-circularly for `n=3` selection or a same-input PDT-vs-QM prediction.
