# Cycle 357 — Dense-coding dimension selector no-go

## Target
Attack the strongest unresolved PDT-II obligations in order: a PDT-native composition law and a non-circular PDT-native derivation of n=3.

## Candidate principle
**DC:** A composite theory admits deterministic perfect dense coding: two local n-level systems may share a maximally correlated resource; after one local reversible encoding and transmission of one n-level subsystem, a joint distinction measurement can identify one of n^2 messages with certainty.

Question: can DC select n=3, determine a unique PDT composition rule, or force a same-input PDT/QM probability deviation?

## Exact hypotheses
For finite complex dimension d=n >= 2, let

|Phi_d> = (1/sqrt(d)) sum_{j=0}^{d-1} |j>|j>.

Define generalized Weyl operators X|j>=|j+1 mod d>, Z|j>=omega^j|j>, omega=exp(2 pi i/d), and U_ab=X^a Z^b for a,b in {0,...,d-1}. Alice encodes (a,b) by U_ab on her half. Bob measures in the d^2 states

|Phi_ab> = (U_ab tensor I)|Phi_d>.

## Proof
For message pairs (a,b),(a',b'),

<Phi_ab|Phi_a'b'> = (1/d) Tr(U_ab^dagger U_a'b').

The Weyl operators are Hilbert-Schmidt orthogonal:

Tr(U_ab^dagger U_a'b') = d delta_{a,a'} delta_{b,b'}.

Hence the d^2 encoded states are mutually orthonormal and therefore perfectly distinguishable by one joint projective measurement. The construction exists for every finite d>=2.

Consequently:

1. DC => n=3 is **FALSIFIED**. The smallest nontrivial counterexample is d=2; d=4 is the smallest higher-dimensional counterexample to uniqueness at three.
2. DC => a unique PDT composition law is **FALSIFIED as an inference**: ordinary complex quantum tensor composition already realizes DC for all d>=2, so DC cannot uniquely specify a different PDT composition.
3. DC => P_PDT(O|I,R) != P_QM(O|I,R) is **FALSIFIED as an inference**: the ideal protocol is already a QM protocol with P(correct|I,R)=1 when R includes the maximally entangled pair, Weyl encoding, one d-level transmission, and Bell-basis joint measurement.
4. There is no d=3 singularity in message count, success probability, or Weyl orthogonality.

## Dimension stress audit
The companion CSV evaluates d=1,...,12. d=1 is the trivial one-message boundary case. For every d>=2, message count is d^2 and ideal success probability is exactly 1. The theorem above extends to every finite d, so the finite audit is a regression witness rather than the basis of the proof.

## Edge/resource observations
- **Degenerate d=1:** trivial, no communication advantage.
- **Pure maximally entangled resource:** theorem applies exactly.
- **Non-maximally entangled/mixed resources:** deterministic capacity can fall; this is resource dependence, not an n=3 selector.
- **Restricted decoding/encoding:** capacities can change under declared restrictions; any PDT discriminator must therefore state R explicitly and compare the same microscopic preparation, operations and measurement restrictions.
- **Composite structure:** DC is genuinely joint—it uses an entangled resource and joint distinction measurement—so this no-go is stronger than eliminating a merely local axiom.

## Prior-art rejection
Dense coding is established quantum-information theory. Bennett and Wiesner introduced the protocol; arbitrary-dimensional/qudit deterministic dense-coding theory is established. Published work explicitly treats a maximally entangled pair of d-dimensional qudits as supporting d^2 perfectly distinguishable messages, and later work studies arbitrary dimensions and restricted resources. Therefore neither dense coding nor its all-d Weyl construction is claimed as PDT novelty.

Relevant prior-art anchors:
- Bennett & Wiesner, *Communication via one- and two-particle operators on Einstein-Podolsky-Rosen states*, Phys. Rev. Lett. 69, 2881 (1992).
- Bourdon & Gerjuoy, *Overcoming a limitation of deterministic dense coding with a nonmaximally entangled initial state*, Phys. Rev. A 81, 022314 (2010), DOI 10.1103/PhysRevA.81.022314.
- Bruß et al., *Distributed Quantum Dense Coding*, Phys. Rev. Lett. 93, 210501 (2004), DOI 10.1103/PhysRevLett.93.210501.

## Surviving theorem boundary
A viable PDT-native composition principle must do more than require a joint operational advantage already realized uniformly by QM. It must impose a resource-sensitive restriction or law on admissible joint distinctions/correlations that (i) is stated independently of the desired n=3 result, (ii) excludes d=2 and every d>=4 for a principled reason if n=3 is claimed, and/or (iii) yields a fully same-input probability or inequality differing from QM under an explicitly identical resource window.

## Status ledger
| Claim | Status |
|---|---|
| Generalized dense coding exists for every finite d>=2 | PROVED / IMPORTED-KNOWN |
| DC implies n=3 | FALSIFIED |
| DC uniquely determines PDT composition | FALSIFIED as an inference |
| DC forces a same-input PDT/QM deviation | FALSIFIED as an inference |
| Resource restrictions can change dense-coding capacity | IMPORTED/KNOWN |
| PDT-native resource-sensitive joint selector | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

No gravity/capacity law is promoted: none follows from this result without additional assumptions.
