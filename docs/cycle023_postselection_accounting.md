# Cycle 023 — Postselection-accounted exact-label bound

## Status

**PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN.** Not a breakthrough candidate.

## Theorem

Let label `i` occur with prior `p_i` and be encoded into density operator `rho_i` on a `D`-dimensional quantum record space. Let a postselected guessing procedure have conclusive effects `N_i >= 0` with

```text
sum_i N_i <= I_D,
```

where the remainder is an inconclusive/rejected outcome. Then

```text
P(retain AND correct)
 = sum_i p_i Tr(N_i rho_i)
 <= min(1, D p_max),
```

with `p_max=max_i p_i`.

If `s=P(retain)>0`, then

```text
P(correct | retain) <= min(1, D p_max / s).
```

For `k` equiprobable labels this is

```text
s * P(correct | retain) <= min(s, D/k),
P(correct | retain) <= min(1, D/(k s)).
```

## Proof

Each density operator obeys `0 <= rho_i <= I_D`. Therefore for every positive conclusive effect,

```text
Tr(N_i rho_i) <= Tr(N_i).
```

Using `p_i <= p_max` and `sum_i N_i <= I_D`,

```text
P(retain AND correct)
 <= p_max sum_i Tr(N_i)
 <= p_max Tr(I_D)
 = D p_max.
```

Dividing by the retention probability gives the conditional form.

## Why this matters for PDT

Postselection can make a retained branch look dramatically more distinguishable than the unconditional experiment. That is not by itself a same-input PDT-vs-QM prediction. The retention probability is a resource and must be charged.

A valid same-input claim must therefore report at least the pair

```text
(retention probability s, conditional correctness C),
```

or equivalently the joint yield `s C`. If PDT and QM share the same microscopic states and admissible measurement effects, then

```text
s C <= D p_max.
```

An apparent conditional advantage `C_PDT > D p_max` is not a violation when it is obtained by taking `s<1`; the only decisive violation would be

```text
s_PDT C_PDT > D p_max
```

under the same declared physical resources.

## Explicit heralded witness

For uniform `k>=2` labels in dimension `D>=2`, encode label 1 as `|0>` and every other label as `|1>`. Keep only the outcome projector `|0><0|` and reject everything else. Then

```text
s = 1/k,
P(correct | retain) = 1,
s P(correct | retain) = 1/k.
```

Thus perfect conditional accuracy can coexist with very small yield. This is exactly why conditional accuracy alone is an invalid breakthrough metric.

## Stress test

The executable audit samples arbitrary Dirichlet priors, random mixed states, and random POVMs with one inconclusive outcome for dimensions `1..12`, using `k=d+5` and 300 fixed-seed trials per dimension. No violation of the joint bound was found. Separate unit tests verify the conditional bound, perfect-postselection witness, and formula-level scans through dimension 100.

## Prior-art boundary

Historical novelty is not claimed. Quantum-state discrimination with inconclusive outcomes, fixed failure rates, and unambiguous discrimination are established topics. Relevant anchors include:

- J. Fiurasek and M. Jezek, *Optimal discrimination of mixed quantum states involving inconclusive results*, Phys. Rev. A 67, 012321 (2003).
- E. Bagan et al., *Optimal discrimination of quantum states with a fixed rate of inconclusive outcomes*, Phys. Rev. A 86, 040303(R) (2012).
- K. Nakahira, T. S. Usuda, K. Kato, *Upper and lower bounds on optimal success probability of quantum state discrimination with and without inconclusive results*, Phys. Rev. A 97, 012103 (2018).

The PDT contribution is a strict accounting rule: conditional postselected performance is not a same-input anomaly unless its retention-weighted yield violates the physical bound.
