# Cycle 101 — finite primitive-triad coherence certificate

## Target
PDT-II priorities (1) native composition and (2) non-circular dimension selection, following Cycle 100's proof that all two-generator rebracketing tests can pass in the nonassociative octonions.

## Exact hypotheses
Let `A = R·1 ⊕ V` be finite-dimensional with a bilinear product. Assume the associator `[x,y,z]=(xy)z-x(yz)` is alternating (in particular this holds in an alternative algebra). Let `{e_i}` span the primitive/non-scalar sector `V`, and let the unit associate trivially.

## Theorem — finite triad certificate
Under those hypotheses, global associativity is equivalent to `[e_i,e_j,e_k]=0` for every unordered primitive basis triad `i<j<k`.

Bilinearity makes the associator trilinear. Alternation makes repeated-index coefficients vanish and values on permutations differ only by sign. Expanding arbitrary `x,y,z` in the basis therefore expresses `[x,y,z]` as a linear combination of the unordered basis-triad associators. Hence all such triad coefficients vanish iff the associator vanishes everywhere.

This is a certification theorem, not a derivation of the physical premise that PDT must impose triad path-independence.

## Octonion adversarial audit
For `O = R ⊕ R^7`, there are `C(7,3)=35` unordered imaginary basis triads. Exact integer Cayley-Dickson arithmetic gives 28/35 nonzero associators and 7/35 associative Fano-line triads. Every nonzero basis-triad associator in this convention has squared norm 4; the first decisive witness is `[e1,e2,e4]=2e7`. All 210 permutation-sign checks and all 98 repeated-argument alternative checks pass exactly.

A 2,000-triple seeded random reconstruction from the 35 triad coefficients had maximum residual `5.4055e-14` and zero residuals above `1e-9`.

## Dimension stress ledger
With an alternating associator, the number of primitive unordered triad checks is `C(n,3)`. The generated ledger covers `n=1..12,16,24,32,48,64,96,128`. This is a count/certification statement only; it does not assert existence of an alternative normed algebra in each dimension.

## Prior-art boundary
The equivalence between alternativity and an alternating associator, and the alternative/nonassociative nature of the octonions, are classical. The reduction to unordered basis triads is multilinear algebra. No historical novelty is claimed.

## PDT consequence
Cycle 100 showed two-history coherence is insufficient. Cycle 101 fixes the exact next boundary: under bilinearity plus alternativity, primitive three-history path independence is sufficient to certify global associativity, but only because it kills all coefficients of the associator. It cannot be advertised as a non-circular PDT-native `n=3` derivation until PDT independently derives why every primitive triad must be path-independent.

The open task is to derive or falsify such a three-history law from resource/refinement/distinction primitives, preferably as an operational cost or falsifiable inequality rather than an axiom that merely restates associativity.

## Classification
`PROVED + CONDITIONAL + IMPORTED/KNOWN + NUMERICALLY_SUPPORTED + OPEN`

**BREAKTHROUGH CANDIDATE: NO.**
