# Cycle 038 — Predictive-revelation synergy no-go

**Status:** **PROVED + FALSIFIED + IMPORTED/KNOWN**. This is a decisive boundary on extending the Cycle 037 linear-rank revelation law. **Not a breakthrough candidate.**

## Question attacked
Cycle 037 proved exact modularity for the dimension of a linear accessible-effect subspace. A tempting stronger PDT conjecture is that a *predictive* revelation measure should remain modular, or at least submodular, when resources are combined.

That stronger conjecture is false.

## Minimal counterexample: XOR
Let `X1,X2` be independent uniform bits and let the target physical alternative be

`Y = X1 XOR X2`.

Define the predictive revelation of a resource set `A` by

`F(A) = I(Y ; X_A)`

in bits. Then

`F({1}) = 0`,

`F({2}) = 0`,

`F({1,2}) = 1`,

`F(empty) = 0`.

Therefore the submodularity residual is

`F({1}) + F({2}) - F({1,2}) - F(empty) = -1`.

Submodularity would require this quantity to be nonnegative. Hence predictive revelation is not universally submodular, and therefore cannot be universally modular either.

### Exact proof
Because `X2` is uniform and independent of `X1`, conditioning on either value of `X1` leaves `Y=X1 XOR X2` uniform. Thus `H(Y|X1)=H(Y)=1` and `I(Y;X1)=0`; symmetrically `I(Y;X2)=0`. But `Y` is a deterministic function of `(X1,X2)`, so `H(Y|X1,X2)=0` and `I(Y;X1,X2)=H(Y)=1`.

No numerical approximation is involved.

## Higher-order parity family
For independent uniform bits `X1,...,Xm`, define

`Y = X1 XOR ... XOR Xm`.

For every strict subset `A` of `{1,...,m}`, at least one independent uniform bit remains unobserved. Flipping that hidden bit flips `Y` while leaving the observed tuple fixed, so the conditional distribution of `Y` remains uniform. Therefore

`I(Y ; X_A) = 0` for every strict subset `A`,

while

`I(Y ; X_1,...,X_m) = 1`.

Thus arbitrarily high-order pure synergy exists: no proper resource subset reveals any information about the target, yet the complete resource family reveals one full bit.

## PDT consequence
The Cycle 037 identity

`d(R∨S)+d(R∧S)=d(R)+d(S)`

remains correct for `d(R)=dim(E_R)` when resources are represented by linear effect subspaces. Cycle 038 proves that this identity cannot be promoted without additional assumptions to a target-dependent information/predictive revelation measure.

A general PDT revelation theory therefore needs at least one of the following:

1. an explicit synergy/complementarity term;
2. a restriction to linear-rank accessibility where Grassmann modularity genuinely applies;
3. structural assumptions that exclude XOR/parity-type joint observables;
4. a different composition law whose admissible joint effects are physically derived.

Any claim that resource gains are always diminishing is killed by the XOR witness.

## Stress tests
- `pdt_resource_synergy.py` implements exact entropy/mutual-information witnesses.
- `tests/test_pdt_resource_synergy.py` exhausts every strict parity subset through `m=8` and checks the `m=1..12` sweep.
- `results/cycle038_resource_synergy_audit.csv` records the deterministic `m=1..12` audit.
- `results/cycle038_resource_synergy_status.json` records theorem status and the minimal `-1 bit` submodularity residual.

## Prior-art boundary
This mathematics is established. XOR is a canonical example of synergistic information, and multivariate information decomposition/Partial Information Decomposition explicitly separates synergistic from unique and redundant information. Relevant prior art includes Williams and Beer, *Nonnegative Decomposition of Multivariate Information* (2010, arXiv:1004.2515), and the extensive subsequent PID literature. Accordingly no historical novelty is claimed for the XOR/parity theorem.

The PDT-specific value is the kill test: **linear resource-rank modularity and predictive revelation are mathematically different objects and must not be conflated.**

## Research consequence
The next composition/revelation target should not ask whether revelation is additive. It should seek a physically derived law for the synergy term itself, especially whether PDT resource restrictions bound, compose, or thermodynamically price synergistic distinction that is invisible to every proper resource subset.
