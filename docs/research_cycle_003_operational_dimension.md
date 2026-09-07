# PDT Breakthrough Lab — Research Cycle 003

## Result: resolution-scaled distinction capacity identifies metric dimension, but does not select n=3

**Status: IMPORTED/KNOWN mathematics + PDT operational corollary. Not a breakthrough.**

Let `M_R(epsilon)` denote the largest codebook of states that remain pairwise distinguishable at resource-relative resolution `epsilon` in a finite-dimensional Euclidean elementary body. Define

\[
K_R(\epsilon)=\log_2 M_R(\epsilon).
\]

For the Euclidean unit ball `B_2^n`, standard packing/covering-volume bounds imply, up to the usual packing-versus-covering convention,

\[
\left(\frac1\epsilon\right)^n \lesssim M_R(\epsilon)
\lesssim \left(1+\frac{2}{\epsilon}\right)^n.
\]

Therefore

\[
n\log_2(1/\epsilon)\lesssim K_R(\epsilon)
\lesssim n\log_2(1+2/\epsilon),
\]

and hence

\[
\boxed{\lim_{\epsilon\to0}
\frac{K_R(\epsilon)}{\log_2(1/\epsilon)}=n.}
\]

This gives an operational estimator for the already-existing metric dimension from a resolution sweep of distinguishable-codebook growth.

### What this does and does not do

It **does** show that the scalar distinction capacity becomes geometry-informative when considered as a *function of resolution* rather than as a single scalar at one resource window.

It **does not** derive or uniquely select `n=3`. Every finite `n` has its own asymptotic slope. A physical principle is still required to explain why a qubit-like elementary system has the observed dimension rather than another one.

### Prior-art boundary

The underlying theorem is standard metric entropy / box-counting (Minkowski) dimension mathematics. Packing and covering numbers have the same logarithmic asymptotic dimension, and Euclidean-ball entropy grows as `Theta(n log(1/epsilon))`. Accordingly, this cycle is classified as **IMPORTED/KNOWN mathematics** with a PDT-specific operational interpretation, not as a new mathematical theorem or new quantum mechanics.

It also sits near existing GPT work on operational dimensions, including signaling dimension and other notions based on distinguishability or input-output correlations. PDT should not claim novelty for the general idea that operational tasks can reveal system dimension.

### Computational audit

`pdt_dimension.py` implements conservative volumetric bounds and a finite-resolution dimension interval. `tests/test_operational_dimension.py` verifies monotone convergence of the upper ratio toward `n`, exact lower-bound slope, dimension separation at fixed resolution, and input validation.

### Research consequence

This cycle narrows the dimension-selection problem. The next useful target is no longer “can capacity reveal dimension?”—it can, asymptotically, once a metric and resolution family are supplied. The harder PDT-native question remains:

\[
\boxed{\text{Which independent physical principle forces the observed slope to be }3?}
\]

Candidate principles must be composite- or intervention-sensitive and must survive comparison with known GPT reconstruction theorems.
