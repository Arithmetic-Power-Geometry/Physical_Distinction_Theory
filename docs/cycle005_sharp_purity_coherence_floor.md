# Cycle 005 — Sharp purity-only coherence floor

## Status: PROVED and TIGHT; experimentally actionable; historical novelty OPEN

Assume the controlled-unitary, identical-conditional-output sector used by the spectral coherence-annulus theorem. Let the environment spectrum be `p_j`, let `m=p_max`, and let purity be `P=Tr(eta^2)=sum_j p_j^2`.

The previous corollary used only `P<=m`, giving the valid but non-sharp floor `|chi|>=max(0,2P-1)`.

### Theorem (sharp purity floor)

For every finite-dimensional environment in this sector,

`|chi| >= sqrt(max(0, 2P-1)).`

Moreover this is the best possible lower bound that depends only on purity: for every `P in [1/2,1]`, equality is attained by a rank-two spectrum `(m,1-m,0,...)`, with `m=(1+sqrt(2P-1))/2`, and opposite relative phases.

### Proof

If `P<=1/2`, the claimed lower bound is zero and is trivial. If `P>1/2`, necessarily `m>1/2`. Since the remaining eigenvalues are nonnegative and sum to `1-m`,

`sum_{j>1} p_j^2 <= (sum_{j>1} p_j)^2=(1-m)^2`.

Therefore

`P <= m^2+(1-m)^2`,

which for `m>=1/2` implies

`2m-1 >= sqrt(2P-1)`.

The spectral coherence-annulus theorem gives `|chi|>=2m-1`, proving the bound. For the rank-two spectrum `(m,1-m)`, purity is exactly `m^2+(1-m)^2`; choosing the two phase vectors antiparallel gives `|chi|=2m-1=sqrt(2P-1)`. Hence the purity-only bound is sharp.

### Why this improves Cycle 004

For `1/2<P<1`, `sqrt(2P-1) > 2P-1`, so the old purity witness was strictly weaker except at the endpoints. Example: `P=0.625` improves the guaranteed visibility floor from `0.25` to `0.5`.

### Stress test

`purity_coherence_sharp.py` samples random spectra in dimensions 2 through 12 and checks the sharp purity floor against the exact spectral floor. It also verifies equality across a 101-point rank-two family. Numerical roundoff at the ~1e-12 scale is tolerated in interpretation.

### Scientific interpretation

This is a stronger experimentally actionable kill test: within the stated controlled-sector assumptions, observing visibility below `sqrt(2P-1)` for `P>1/2` falsifies at least one assumption of the model. It remains QM-compatible and is not a same-input PDT-vs-QM deviation. Historical novelty remains OPEN pending dedicated prior-art review; the proof uses elementary spectral probability geometry.
