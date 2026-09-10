# Cycle 045 — Postselection Same-Input Lock

## Target

PDT-II target (3): determine whether resource-conditioned postselection can produce a genuine quantitative deviation

\[
P_{\rm PDT}(O\mid I,R)\ne P_{\rm QM}(O\mid I,R)
\]

while keeping the microscopic experiment identical.

## Exact hypotheses

Let `O` be the outcome record and `S` the record used for postselection/resource conditioning. Assume:

1. PDT and standard QM assign the same joint microscopic distribution `p(o,s)` to `(O,S)` for the declared microscopic input `I`.
2. Both use the same physical selection event `A` in the `S` record.
3. `P(S in A)>0`.
4. Conditioning uses ordinary normalized probabilities.

No Markovianity, purity, Hilbert-space dimension, or tensor-product assumption is needed for the theorem once the common joint law is fixed.

## Theorem

Under the hypotheses above,

\[
P_{\rm PDT}(o\mid S\in A,I)=P_{\rm QM}(o\mid S\in A,I)
\]

for every outcome `o`.

### Proof

Because the joint laws are identical,

\[
p_{\rm PDT}(o,S\in A)=p_{\rm QM}(o,S\in A)
\]

and

\[
p_{\rm PDT}(S\in A)=p_{\rm QM}(S\in A)>0.
\]

Therefore both conditional distributions equal the same ratio

\[
\frac{p(o,S\in A)}{p(S\in A)}.
\]

QED.

## Decisive falsification

The proposed escape route

> same microscopic joint law + same selection mechanism + postselection alone -> new PDT conditional probability

is **FALSIFIED**.

Postselection can strongly change a reported conditional number, including under very rare-event filtering, but if the underlying joint law and selection rule are shared, it changes PDT and QM identically. An apparent anomaly generated only by conditioning is therefore not a same-input physical deviation.

## Small rare-event witness

A two-outcome/two-record distribution can be chosen with selection probability `10^-6` and

\[
P(O=1\mid \mathrm{keep})=0.999999.
\]

This dramatic conditional shift is fully compatible with zero PDT-vs-QM gap when both theories share the same joint distribution. Thus large postselected effects are not by themselves evidence for new dynamics or a new probability law.

## Stress tests

`pdt_postselection_same_input_lock.py` audits dimensions `n=1..12` with randomized joint tables and changing record alphabets. The equality is exact up to floating-point normalization. Tests also include zero-probability selection, deliberately changed joint laws, and rare-event amplification.

## Surviving escape coordinates

A genuine same-input PDT prediction must now alter at least one substantive physical element:

- the microscopic joint law/process producing `(O,S)`;
- the physical selection instrument/resource interaction;
- or the probability/conditioning rule itself.

Merely relabeling, filtering, discarding, or conditioning outcomes is insufficient.

## Prior-art boundary

This theorem uses standard probability conditioning and the established quantum-instrument/postselection framework. Quantum instruments already encode laboratory outcome probabilities operationally, and postselection is standard conditionalization on selected outcomes. Hence the underlying mathematics is **IMPORTED/KNOWN**, not a historical PDT novelty. The PDT-specific contribution is the explicit no-go placement inside the PDT-II same-input search tree.

Relevant prior art includes Dressel & Jordan, *Physical Review A* 88, 022107 (2013), on quantum instruments as an operational foundation, and the broader postselection literature. Apparent conditional violations created by postselection/fair-sampling are also known phenomena and must not be mistaken for microscopic theory disagreement.

## Classification

- **PROVED:** same-joint postselection lock.
- **FALSIFIED:** postselection-only same-input escape route.
- **IMPORTED/KNOWN:** conditioning and quantum-instrument mathematics.
- **BREAKTHROUGH CANDIDATE:** no.

## Consequence for PDT-II

Future target-(3) work should not spend cycles searching for a deviation generated solely by filtering an unchanged quantum record. The candidate must expose and test an explicit physical-law change before it can qualify as a same-input PDT prediction.
