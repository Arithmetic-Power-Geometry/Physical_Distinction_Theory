# Cycle 358 — Distinguishability-contraction refinement no-go

## Target
Attack PDT-II targets (1) composition, (2) non-circular n=3, then (4) resource-refinement/revelation laws. Candidate chosen because it is directly about physical distinction under resource-losing dynamics rather than another communication protocol.

## Candidate principle DC-R
Let D be operational binary distinguishability. A resource-losing physical map Phi must not increase distinction:

D(Phi(rho),Phi(sigma)) <= D(rho,sigma).

For finite-dimensional complex QM take D(rho,sigma)=1/2 ||rho-sigma||_1 and Phi any CPTP map.

Question: can this PDT-motivated contraction law select n=3, determine composition, or force a same-input PDT/QM deviation?

## Proof / counterfamily
Trace distance is contractive under every CPTP map. Hence the candidate law is already satisfied by ordinary complex quantum theory in every finite dimension d. In particular, d=2 is a lower-dimensional counterexample to DC-R => n=3 and d=4 is the smallest higher-dimensional counterexample to uniqueness at three.

The dimension audit d=1,...,12 therefore has no d=3 singularity. The all-d result is analytic and the CSV is only a regression witness.

A concrete saturating family also exists in every d>=2: choose two orthogonal basis states and a unitary channel. Their input trace distance is 1 and remains 1 after the channel. A strict-contraction family is supplied by the replacement channel Phi(rho)=tau Tr(rho), for which every pair is mapped to the same tau and output distance is 0. Thus the law permits the full interval from complete erasure to perfect preservation independently of d.

## Composition stress
Tensoring a fixed ancillary state does not change trace distance:

D(rho tensor tau, sigma tensor tau)=D(rho,sigma).

Therefore ancilla-stable distinction contraction is also dimension-uniform. It does not choose a unique tensor/composition rule merely from the scalar inequality.

## Markovian / non-Markovian boundary
For a CP-divisible evolution, trace distance is non-increasing along each divisible step. However, open-system non-Markovian dynamics can display trace-distance revivals; such revivals are established information-backflow diagnostics. Therefore an unconditional temporal statement 'distinction can never increase with time' is false unless the admissible dynamics/resource assumptions are stated. The surviving theorem is channel-relative contraction under CPTP processing, not universal time monotonicity.

## Same-input prediction consequence
Because standard QM obeys DC-R exactly, DC-R alone cannot entail P_PDT(O|I,R) != P_QM(O|I,R). A PDT discriminator must add a PDT-native quantitative restriction stronger than standard data processing and evaluate the same microscopic preparation, channel/record access, measurement and resource window R.

## Prior-art rejection
This is established quantum-information structure, not PDT novelty. Trace-distance contractivity/data processing under quantum channels is standard. Reeb, Kastoryano and Wolf (2011) discuss distinguishability contraction and trace-norm contraction for quantum channels. Breuer, Laine and Piilo (2009) use trace-distance increases to quantify non-Markovian information backflow. Recent work on conditional contraction coefficients with quantum side information further develops this established contraction framework. No novelty claim is made for DC-R.

Prior-art anchors:
- H.-P. Breuer, E.-M. Laine, J. Piilo, arXiv:0908.0238 (2009).
- D. Reeb, M. J. Kastoryano, M. M. Wolf, arXiv:1102.5170 (2011).
- C. Hirche, I. George, T. Nuradha, M. M. Wilde, arXiv:2608.27171 (2026).

## Smallest decisive counterexamples
- n=2: ordinary qubit CPTP dynamics satisfies DC-R, disproving DC-R => n=3.
- n=4: ordinary ququart CPTP dynamics satisfies DC-R, disproving uniqueness above three.
- Universal-time-monotonicity without CP-divisibility: falsified by known non-Markovian trace-distance revival examples.

## Surviving boundary
A viable PDT refinement/revelation theorem must specify the admissible resource preorder and record access. Standard processing monotonicity is too weak: it is dimension-uniform and already quantum. A potentially distinctive PDT law would need a stronger, independently motivated bound (for example a resource-indexed contraction/revelation rate) that survives same-input comparison and does not merely rename a known contraction coefficient.

## Status ledger
| Claim | Status |
|---|---|
| Trace distance contracts under CPTP maps | IMPORTED/KNOWN |
| DC-R holds for finite-dimensional QM for every d | PROVED / IMPORTED-KNOWN |
| DC-R implies n=3 | FALSIFIED |
| DC-R uniquely determines PDT composition | FALSIFIED as an inference |
| DC-R forces same-input PDT/QM deviation | FALSIFIED as an inference |
| Ancilla stability with fixed tensor factor | PROVED / IMPORTED-KNOWN |
| Universal temporal monotonicity without divisibility assumptions | FALSIFIED |
| Resource-indexed PDT-native stronger contraction/revelation law | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

No gravity/capacity law is promoted.