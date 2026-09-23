# PDT-II Cycle 354 — Teleportation is not an n=3 selector

## Status

- Perfect finite-dimensional quantum teleportation for every integer d >= 2: **PROVED / IMPORTED-KNOWN**.
- `perfect teleportation => n=3`: **FALSIFIED**.
- `perfect teleportation => unique PDT composition`: **FALSIFIED as an inference**.
- `perfect teleportation => same-input P_PDT != P_QM`: **FALSIFIED as an inference**.
- PDT-native joint selector: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Candidate principle attacked

A possible escape from the earlier local/compositional no-go results is to demand a genuinely joint operational capability:

> An arbitrary unknown n-level state can be transmitted exactly using a shared maximally correlated resource, a joint distinction measurement, classical outcome communication, and a reversible correction.

Could the existence/closure of such a protocol force n=3 or a unique PDT composition law?

## Exact construction

Let d >= 2, omega = exp(2 pi i/d), and define Weyl operators

X|j> = |j+1 mod d>,   Z|j> = omega^j |j>.

Let

|Phi_00> = (1/sqrt(d)) sum_{j=0}^{d-1} |j>|j>,
|Phi_ab> = (I tensor X^a Z^b)|Phi_00>,  a,b in {0,...,d-1}.

The d^2 states |Phi_ab> form an orthonormal maximally entangled basis. For an arbitrary input |psi>, expansion in this basis yields d^2 equiprobable outcomes. Conditional on outcome (a,b), Bob's subsystem is a known Weyl transform of |psi>; applying its inverse recovers |psi> exactly. By linearity, the induced channel is the identity channel on every density operator rho.

Therefore deterministic perfect teleportation exists for every finite d >= 2. No step singles out d=3.

## Smallest decisive counterexamples

- d=2: ordinary qubit teleportation already satisfies the proposed capability, so any claim that the capability requires d=3 is false.
- d=4: a higher-dimensional counterexample rules out interpreting d=3 as the unique nontrivial dimension.

The same construction works at d=5,...,12 and analytically for every finite d >= 2.

## Exact stress audit n=1..12

The companion CSV records the exact structural counts. For d>=2 there are d^2 generalized Bell outcomes and d^2 reversible Weyl corrections; the resulting channel is exactly the identity under the stated ideal resources. d=1 is the degenerate trivial system and is recorded separately rather than used as a physical selector.

## Why this matters for PDT-II

Teleportation is stronger than a merely local axiom: it explicitly uses a composite state, a joint measurement and conditional reversible dynamics. Nevertheless it does not determine n=3 because standard complex quantum theory realizes the same protocol uniformly in d.

It also cannot by itself produce the requested same-input discriminator P_PDT(O|I,R) != P_QM(O|I,R): ordinary QM already realizes the candidate operational capability. Any PDT deviation must add a PDT-native quantitative restriction or correction that changes a probability or achievable resource tradeoff while keeping microscopic input I and resource window R fixed.

## Prior-art boundary

This is not a PDT novelty claim. Bennett et al. introduced quantum teleportation in 1993, and arbitrary-dimensional/qudit teleportation via generalized Bell measurements is established literature. Examples include high-dimensional controlled teleportation and later arbitrary-qudit protocols. The imported protocol is used here only as a falsification family.

Sources checked:

- Bennett et al., Phys. Rev. Lett. 70, 1895 (1993), foundational teleportation protocol.
- Vaidman, Phys. Rev. A 49, 1473 (1994), teleportation and generalization context.
- Zhan You-Bang, Chin. Phys. B 16, 2557–2562 (2007), controlled teleportation of high-dimensional states with generalized Bell-state measurement, DOI 10.1088/1009-1963/16/9/010.

## Surviving theorem boundary

**Theorem (dimension-uniform teleportation no-go for n-selection).** Within finite-dimensional complex quantum theory, the existence of deterministic perfect teleportation using one maximally entangled d-level pair, a generalized Bell measurement, classical outcome communication and a conditional Weyl correction holds for every d>=2. Hence this operational capability alone cannot logically imply d=3.

This theorem is elementary/known quantum information structure and is classified **PROVED / IMPORTED-KNOWN**, not PDT-native.
