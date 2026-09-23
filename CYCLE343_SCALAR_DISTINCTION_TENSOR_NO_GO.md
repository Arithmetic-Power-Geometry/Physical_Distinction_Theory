# Cycle 343 — Scalar-distinction tensor law no-go

## Target attacked
PDT-II target (1): a PDT-native composition law, with implications checked against targets (2) and (3).

## Candidate hypothesis
Let the accessible binary distinction between two classical preparations be

\[
D(P,Q)=\operatorname{TV}(P,Q)=\frac12\sum_x |P(x)-Q(x)|.
\]

A tempting PDT-native scalar composition ansatz is that independent composition is determined only by the local distinction values: there exists a universal function F such that

\[
D(P_1\otimes P_2,Q_1\otimes Q_2)=F(D(P_1,Q_1),D(P_2,Q_2)).
\]

The identical-copy special case would be a universal f with
\[
D(P^{\otimes2},Q^{\otimes2})=f(D(P,Q)).
\]

## Exact counterexample
Take Bernoulli distributions. For Bernoulli(p), Bernoulli(q), local TV is |p-q|.

Pair A:
- P_A = Bernoulli(0)
- Q_A = Bernoulli(1/4)
- D(P_A,Q_A)=1/4
- exact two-copy TV D(P_A^2,Q_A^2)=7/16.

Pair B:
- P_B = Bernoulli(1/4)
- Q_B = Bernoulli(1/2)
- D(P_B,Q_B)=1/4
- exact two-copy TV D(P_B^2,Q_B^2)=5/16.

Thus the same local scalar distinction 1/4 produces two different composite distinctions, 7/16 and 5/16. Therefore no universal scalar f(D) can determine even the two-copy classical product distinction. A fortiori, no universal F based only on the two marginal scalar distinction values can determine general correlated/composite structure.

This is a smallest-alphabet witness: binary outcomes suffice. It embeds in every n-level classical system for n>=2 by assigning zero probability to the unused outcomes, hence survives the requested n=2,...,12 dimension stress and all higher finite dimensions. n=1 is degenerate.

## Surviving theorem
**Scalar Distinction Insufficiency Theorem.** Under ordinary product composition of probability distributions, total-variation distinction is not a sufficient statistic for the distinction of the product. Any PDT composition principle that uses only a single local scalar distinction D must therefore add further operational structure (for example likelihood-ratio data, a richer distinction profile, or independently specified composition data).

Proof: the two exact Bernoulli witnesses above have identical local D but unequal product D. QED.

## Adversarial interpretation
This result blocks a common circular shortcut: defining a PDT scalar distinction and then assuming that its scalar value uniquely fixes tensor composition. Even the classical subtheory disproves that inference before quantum/GPT complications enter.

It does **not** prove that a richer PDT-native distinction object cannot compose. It narrows the search: a viable PDT-native composition law must retain more than one scalar distinguishability number.

## n=3 and same-input consequences
The witness embeds without change at n=3, so this scalar route cannot select n=3. It also supplies no same-input PDT/QM probability deviation: a new prediction would require a separately justified PDT composite rule or operational restriction, not merely a scalar TV value.

## Prior-art audit
The non-tensorization of total variation is known mathematics, not PDT novelty. Bhattacharyya et al., IJCAI 2023, show that exact TV computation for product distributions is #P-complete and contrast TV with distances that tensorize directly. Kontorovich, Electronic Communications in Probability 30 (2025), studies bounds for tensorization of variational distance and shows unavoidable gaps when estimating product TV from marginal TV data. A September 17, 2026 preprint by Avital, Kontorovich, Vershynin and Zou gives an analytic proxy for TV between finite products. Therefore the mathematical non-tensorization itself is IMPORTED/KNOWN; the present cycle uses it as a falsification boundary for PDT-II.

## Status ledger
- Exact Bernoulli counterexample: **PROVED**.
- Scalar local TV uniquely determines two-copy TV: **FALSIFIED**.
- Scalar local distinction uniquely determines a PDT composition law: **FALSIFIED** for this ansatz.
- Binary witness embedding n=2,...,12 and all finite n>=2: **PROVED**.
- Selection of n=3 from scalar distinction composition: **FALSIFIED**.
- Same-input PDT/QM deviation from scalar distinction alone: **FALSIFIED as an inference**.
- Non-tensorization of TV: **IMPORTED/KNOWN**.
- Rich PDT-native distinction profile/composition selector: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Search for a richer PDT-native compositional object whose composition is defined operationally rather than assumed, then test whether it is merely a known likelihood-ratio/Blackwell/GPT object. Any candidate must survive exact low-dimensional counterexample search before being promoted.