# Cycle 144 — Unequal-refinement theorem and strengthened equal-split no-go

## Target attacked

PDT-II target (1), the PDT-native composition law, with direct relevance to target (4), resource refinement/revelation/conservation.

## Conditional theorem (PROVED)

Let `g:[0,∞)->[0,∞)` be a single resolved-channel resource with `g(0)=0`. Assume that for every `r>=0` and every `lambda in [0,1]`, an operationally resolved two-way split conserves total resource additively:

`g(r) = g(r*sqrt(lambda)) + g(r*sqrt(1-lambda))`.

Then `g(r)=c r^2` for some `c>=0`. If `g(1)=1`, then `g(r)=r^2`.

### Proof

Define `h(s)=g(sqrt(s))` for `s>=0`. For arbitrary `a,b>=0`, let `s=a+b`. If `s=0`, additivity is trivial. If `s>0`, choose `lambda=a/s`. The refinement identity gives

`h(a+b)=h(a)+h(b)`.

Thus `h` is additive on the nonnegative reals. Since `h>=0`, it is monotone: if `y>=x`, then `h(y)=h(x)+h(y-x)>=h(x)`. A monotone additive function on the nonnegative reals is linear, so `h(s)=c s`. Hence `g(r)=c r^2`. Calibration fixes `c=1`.

Notably, continuity is not required.

## Strengthened no-go for equal splitting (FALSIFIED implication)

Equal-amplitude refinement, even for every multiplicity, does not determine full resolved composition. A stronger zero-padding-stable counterfamily than Cycle 143 is

`R_eps(q_1,...,q_m) = sum_i q_i + eps * sum_{i<j} q_i q_j (q_i-q_j)^2`, `eps>0`.

It is nonnegative, permutation invariant and unchanged by adding zero channels. It agrees with the quadratic ledger for one active channel and for every equal active split because all pair differences vanish. It disagrees generically on unequal active channels.

Exact witness: `q=(1,3)`, `eps=0.01`. The quadratic total is `4`; the raw correction is `1*3*(1-3)^2=12`, giving `R_eps=4.12`.

Therefore

`all equal-split conservation + permutation symmetry + zero-padding stability`

does **not** imply full quadratic composition.

## Frozen numerical audit (NUMERICALLY SUPPORTED)

Dimensions/refinement arities: `1..12,16,24,32,48,64,96,128`; 570 seeded partition cases. The quadratic rule had zero partition failures with maximum relative residual `6.748117535411712e-16`. The strengthened deformation had zero equal-split failures and was separated from the quadratic ledger on 346 audited unequal partitions. Power-law controls `p=0.5,1,1.5,3` failed every nontrivial random unequal partition in this audit; `p=2` had zero failures. Five regression groups were independently executed locally and passed.

## Prior-art boundary (IMPORTED/KNOWN)

The functional-equation mechanism is not claimed as new mathematics. Gleason/frame-function literature already shows that additivity over orthogonal resolutions can force quadratic forms, and effect-space Gleason/Busch results use additive probability assignments to obtain trace-linear forms. The present PDT value is only the narrowing of the required operational bridge: arbitrary unequal resolved refinement is qualitatively stronger than all equal refinements and is sufficient, under resolved-channel additivity, to fix the radial exponent without continuity.

Relevant prior-art checks performed in this cycle include Gleason's theorem/frame functions, Parseval-frame extensions, and Gleason-type results from Cauchy's functional equation.

## Surviving PDT-native obligation (OPEN)

PDT must still derive, rather than assume, the physical statement that resolved daughter channels contribute additively under arbitrary unequal refinement, or an operationally equivalent revelation/conservation axiom. Without that bridge, this theorem is conditional and cannot be promoted to a PDT breakthrough.

## Status

- Unequal-refinement functional theorem: **PROVED / CONDITIONAL**
- Equal-split sufficiency for full composition: **FALSIFIED**
- Classical additive/frame-function mathematics: **IMPORTED/KNOWN**
- Finite stress audit: **NUMERICALLY SUPPORTED**
- PDT-native derivation of resolved additivity: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
