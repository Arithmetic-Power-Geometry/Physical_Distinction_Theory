# Cycle 021 — Dimension-limited exact record identification

## Status

**PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN.** This is not a PDT breakthrough candidate. The mathematics is standard minimum-error quantum-state discrimination / POVM theory.

## Theorem

Let `X` be uniformly distributed over `k` labels. Label `i` is encoded in an arbitrary density operator `rho_i` supported on the same complex Hilbert space of dimension `d`. For any measurement used to guess the exact label, with POVM effects `M_i`,

```text
P_success = (1/k) sum_i Tr(M_i rho_i) <= min(1,d/k).
```

Equivalently,

```text
P_error >= max(0,1-d/k).
```

Thus when `k>d`, exact branch identification has a nonzero error floor even before adding noise, thermodynamic limits, restricted measurements, or coarse graining.

## Proof

Every density matrix obeys `0 <= rho_i <= I`. Since every POVM effect is positive,

```text
Tr(M_i rho_i) <= Tr(M_i).
```

Therefore

```text
P_success
 <= (1/k) sum_i Tr(M_i)
 =  (1/k) Tr(sum_i M_i)
 =  Tr(I_d)/k
 =  d/k.
```

Probability also cannot exceed one, giving `min(1,d/k)`.

## Sharpness

When `k=q d`, repeat each member of an orthonormal basis exactly `q` times as distinct labels. Use effects `M_(j,a)=|j><j|/q`. They sum to identity and every label is guessed correctly with probability `1/q`. Hence

```text
P_success = 1/q = d/k,
```

so the dimension-only bound is exactly sharp for an infinite family.

## Relation to the previous Holevo cycle

Cycle 019 proved an information constraint `I(X:Y)<=log2 d`. That statement is about average accessible information. The present theorem directly controls the probability of recovering the *entire exact branch label* in one shot. This distinction matters: an information bound does not by itself equal a minimum-error discrimination bound.

## PDT consequence / kill test

For a declared unchanged `d`-dimensional quantum record carrying `k` equiprobable alternatives, any PDT model claiming

```text
P_exact > d/k
```

under the same microscopic states and allowed measurement class is incompatible with standard quantum record physics. Such a claim must identify a changed physical resource: larger state space, altered measurement/effect set, nonlinear/non-Born probability law, additional side system, repeated copies, postselection accounting, or another explicit modification. Merely redescribing hidden distinctions cannot evade the inequality.

## Stress tests

The implementation generates random mixed states and random normalized POVMs. Fixed-seed audits cover dimensions `1..12`, using `k=d+3`; no violation above floating-point tolerance is accepted. Unit tests include exact saturation families through `d=100` and heavy label-overload cases.

## Prior-art boundary

The optimization target `sum_i p_i Tr(M_i rho_i)` is the standard minimum-error quantum-state-discrimination problem. General upper/lower bounds and SDP formulations are established literature; the present `d/k` estimate follows immediately from `rho_i <= I` for equal priors. Therefore historical novelty is explicitly **not claimed**.

Useful prior-art anchors include Helstrom's quantum detection theory and modern treatments of quantum-state discrimination; e.g. Nakahira, Usuda & Kato, *Phys. Rev. A* 97, 012103 (2018), on upper/lower bounds for optimal discrimination success.
