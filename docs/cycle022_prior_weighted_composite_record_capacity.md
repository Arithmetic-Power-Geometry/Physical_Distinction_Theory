# Cycle 022 — Prior-weighted composite record capacity

## Status

**PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN.** Not a breakthrough candidate.

## Theorem

Let a classical label `X=i` occur with arbitrary prior probability `p_i` and be encoded into density operator `rho_i` on a quantum record Hilbert space of total dimension `D`. For every POVM `{M_i}` used to guess the exact label,

```text
P_success = sum_i p_i Tr(M_i rho_i) <= min(1, D p_max),
p_max = max_i p_i.
```

If the record is a standard tensor product of subsystems with dimensions `d_1,...,d_m`, then `D = product_j d_j`, so

```text
P_success <= min(1, p_max product_j d_j).
```

This extends Cycle 021 from uniform priors to arbitrary source imbalance and makes the tensor/composition resource explicit.

## Proof

Every density operator satisfies `0 <= rho_i <= I_D`. Hence for each positive POVM effect,

```text
Tr(M_i rho_i) <= Tr(M_i).
```

Since `p_i <= p_max`,

```text
P_success
 = sum_i p_i Tr(M_i rho_i)
 <= p_max sum_i Tr(M_i)
 = p_max Tr(I_D)
 = D p_max.
```

Probability is also at most one.

## One-shot entropy form

For a classical source, define

```text
H_min(X) = -log2 p_max.
```

Since the optimal guessing probability after measuring the record is at most `min(1,D p_max)`,

```text
H_min(X | measured record)
 >= max(0, H_min(X) - log2 D).
```

This is a direct finite-resource statement: a `D`-dimensional record can reduce exact-label min-entropy by at most `log2 D` bits.

## Tensor-copy corollary

For `m` standard copies of a `d`-dimensional record, `D=d^m`. For `k` equiprobable labels,

```text
P_success <= min(1, d^m/k).
```

Therefore perfect exact identification has the necessary dimension condition

```text
d^m >= k,
m >= ceil(log_d k)    (d>1).
```

This is a necessity only. State geometry may require more copies.

## Sharpness

The bound is sharp throughout the nontrivial regime `D p_max <= 1` when there are at least `k>D` labels and `1/k <= p_max <= 1/D`.

Assign the first `D` labels prior `p_max` and mutually orthogonal basis states. Distribute the residual prior `1-D p_max` over the remaining labels (each no larger than `p_max`). Measure the basis and assign zero decision effect to the tail labels. Then

```text
P_success = D p_max,
```

exactly saturating the theorem.

## Stress tests

The executable audit samples nonuniform Dirichlet priors, random mixed states, and random normalized POVMs in dimensions `1..12`, with `k=d+5` and 300 fixed-seed trials per dimension. No positive violation was found. The test suite separately verifies exact saturation families, uniform reduction to Cycle 021 through dimension 100, tensor-product dimensions, min-entropy form, and copy thresholds.

## PDT consequence

This closes another loophole in same-input claims. Prior imbalance and ordinary tensoring of a finite quantum record do not create an extra PDT-only exact-label advantage. If a PDT proposal claims

```text
P_success^PDT > D p_max
```

for identical microscopic states and the same measurement class, it must declare a changed physical ingredient: a larger/effectively different record space, nonstandard composition rule, additional side system, additional copies, altered effect set, nonlinear/non-Born probability law, postselection resource, or another explicit physical modification.

## Prior-art boundary

Historical novelty is **not claimed**. Minimum-error quantum-state discrimination with arbitrary priors is established, and guessing probability is a standard operational interpretation of conditional min-entropy. Relevant anchors include:

- R. König, R. Renner, C. Schaffner, *The Operational Meaning of Min- and Max-Entropy*, IEEE Trans. Inf. Theory 55, 4337–4347 (2009), DOI 10.1109/TIT.2009.2025545.
- K. Nakahira, T. S. Usuda, K. Kato, *Upper and lower bounds on optimal success probability of quantum state discrimination with and without inconclusive results*, Phys. Rev. A 97, 012103 (2018), DOI 10.1103/PhysRevA.97.012103.
- E. R. Loubenets, *General lower and upper bounds under minimum-error quantum state discrimination*, Phys. Rev. A 105, 032410 (2022), DOI 10.1103/PhysRevA.105.032410.

The PDT contribution here is organizational: it turns the elementary dimension bound into an explicit prior-weighted composite-record kill test and resource ledger entry.
