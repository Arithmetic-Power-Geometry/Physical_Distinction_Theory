# Cycle 301 — Additivity + data processing do not select a unique PDT distinction

## Target
Attack the strongest surviving PDT-II composition obligation after Cycle 300: can exact independent composition plus operational monotonicity (data processing) uniquely select a scalar distinction functional?

## Candidate principle
Let D(P||Q) be a scalar distinction on finite classical experiments. Assume:

1. normalization/faithfulness on ordinary positive distributions;
2. continuity on the interior of each finite simplex;
3. independent additivity
   D(P1 x P2 || Q1 x Q2) = D(P1||Q1)+D(P2||Q2);
4. data processing under every stochastic map T,
   D(TP||TQ) <= D(P||Q).

A tempting PDT-II claim would be that these operational conditions determine one native distinction law.

## Decisive counterfamily
They do not. Classical Renyi divergences

D_alpha(P||Q) = (1/(alpha-1)) log sum_i P_i^alpha Q_i^(1-alpha)

provide distinct additive, data-processing functionals over their standard parameter ranges. In particular KL (alpha -> 1) and alpha=1/2 already disagree on generic binary inputs while both obey product additivity and stochastic data processing.

Take
P=(0.9,0.1), Q=(0.6,0.4).
Then
KL(P||Q) = sum_i P_i log(P_i/Q_i),
while
D_1/2(P||Q) = -2 log(sum_i sqrt(P_i Q_i)).
They are unequal, so the axioms do not identify a unique scalar law.

## Stronger prior-art boundary
This is not a PDT novelty. Existing characterization work is stronger: additive divergences satisfying data processing form a broad class representable through Renyi divergences (under the hypotheses of the relevant characterization theorem). Thus adding DPI to Cycle 300's tensorization requirement does not repair uniqueness.

Consequently PDT-II cannot claim a native composition law merely from independent additivity/tensorization + continuity + operational coarse-graining monotonicity. A genuinely physical PDT selector must impose an additional independently motivated condition not equivalent to choosing a known divergence family member.

## Dimension and edge stress
The binary witness embeds into every alphabet dimension n>=2 by appending identical zero coordinates (or, for strict-interior numerical tests, identical epsilon tails followed by renormalization). Hence the no-go survives n=2,...,12 and arbitrary higher finite dimension. n=1 is degenerate: all normalized distributions coincide and every faithful distinction vanishes, so it cannot select a functional.

The obstruction is classical and therefore remains available inside commuting sectors of quantum theory. Pure boundary points require the usual support conventions; the strict-interior epsilon embedding avoids singularities without restoring uniqueness.

## Consequence for same-input PDT-vs-QM prediction
Until PDT derives an additional native selector, choosing KL, Hellinger/Bhattacharyya, Chernoff/Renyi, or another known monotone is model choice rather than a PDT prediction. Therefore no same-input deviation P_PDT(O|I,R) != P_QM(O|I,R) follows from these composition axioms alone.

## Status
- Unique scalar selector from additivity + DPI: **FALSIFIED**.
- Explicit binary counterfamily/witness: **PROVED**.
- Embedding n=2,...,12 and arbitrary larger finite n: **PROVED**.
- Renyi/additive-DPI mechanism: **IMPORTED/KNOWN**.
- PDT-native extra selector: **OPEN**.
- Same-input PDT/QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Prior-art anchors checked
- Pomatto, Strack & Tamuz, *The Cost of Information*: characterization result that every additive divergence satisfying data processing is an integral of Renyi divergences (the exact theorem hypotheses must be preserved when cited).
- Standard Renyi-divergence literature: product additivity and data-processing properties.

This cycle records a no-go boundary; it does not claim novelty for the imported information-theoretic mathematics.
