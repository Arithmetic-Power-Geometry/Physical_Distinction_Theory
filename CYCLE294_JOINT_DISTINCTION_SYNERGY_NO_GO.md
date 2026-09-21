# Cycle 294 — Joint-distinction synergy defeats local additive conservation

## Target
Attack PDT-II targets (1) and (4): composition and resource/revelation/conservation laws. Test whether a natural local-to-global conservation principle can bound composite distinguishability from the distinguishabilities visible in each subsystem.

## Candidate principle under test
For two hypotheses/worlds H=0,1 represented by joint distributions P0,P1 on A×B, let D_X be operational distinguishability under unrestricted observation of subsystem X, instantiated here by total-variation distance. Test the tempting composition/conservation claim

D_AB <= D_A + D_B,

or, more strongly, that the pair (D_A,D_B) determines or upper-bounds the joint distinction.

This is a candidate only; it is not assumed by PDT.

## Exact smallest counterexample
Take two binary subsystems A,B.

H=0: P0(00)=1/2, P0(11)=1/2, all other outcomes 0.
H=1: P1(01)=1/2, P1(10)=1/2, all other outcomes 0.

Both A-marginals are uniform under both hypotheses, and both B-marginals are uniform under both hypotheses. Hence

TV(P0_A,P1_A)=0,
TV(P0_B,P1_B)=0.

But the supports of P0_AB and P1_AB are disjoint, so

TV(P0_AB,P1_AB)=1.

Therefore

D_AB = 1 > 0 = D_A + D_B.

The local data reveal no distinction at all while the joint parity relation reveals the hypothesis perfectly.

## Consequences
1. Any universal PDT law asserting that composite distinction is additive/subadditive in the two marginal distinctions is false without extra hypotheses.
2. Local distinction scalars cannot determine the joint distinction. Correlation/interface structure carries operationally accessible distinction absent from either marginal.
3. This strengthens the earlier interface-composition no-go in a fully classical probability model: the obstruction does not require entanglement, noncommutativity, quantum dynamics, or exotic tensor rules.
4. A defensible conservation statement must specify what is conserved and under which map. For a fixed stochastic coarse-graining K applied to the *same* pair of distributions, total variation obeys data processing TV(KP0,KP1)<=TV(P0,P1). Marginalization is such a coarse-graining, so D_A<=D_AB and D_B<=D_AB. This one-way monotonicity survives; the reverse reconstruction from marginals does not.
5. Resource refinement is therefore naturally monotone when it means enlarging the allowed observation set, but there is no additive local accounting unless joint/correlation observables are separately represented.

## Dimension stress
The decisive example is binary×binary. It embeds in every larger finite alphabet by assigning zero probability to spectator outcomes. Thus the failure survives dimensions n=2 through n=12 and arbitrary higher finite dimension. Degenerate n=1 has no nontrivial binary hypothesis distinction and is not a counterexample requirement.

## Alternative norms/divergences
The exact disjoint-support witness also gives maximal Hellinger separation and infinite directed KL where supports mismatch, while marginals remain identical. Numerical constants/conventions differ, but the local-to-joint synergy obstruction is not peculiar to total variation. Claims involving a specific divergence must still be stated separately because not every divergence has identical tensor or coarse-graining properties.

## Prior-art boundary
This mechanism is established information-theoretic/statistical synergy: XOR/parity examples have zero information in individual variables and full information jointly. Total-variation contraction under stochastic maps is also standard data processing. Neither mechanism is PDT novelty. The PDT-relevant result is the audit boundary: a proposed PDT local additive distinction-conservation law is decisively false, and any viable composition law must explicitly account for relational/joint distinction.

## Status ledger
- D_AB <= D_A + D_B from marginals alone: **FALSIFIED**.
- (D_A,D_B) uniquely determine D_AB: **FALSIFIED**.
- binary parity counterexample with D_A=D_B=0 and D_AB=1: **PROVED**.
- embedding into n=2..12 and arbitrary larger finite alphabets: **PROVED**.
- stochastic coarse-graining cannot increase total variation: **IMPORTED/KNOWN**.
- XOR/parity synergy mechanism: **IMPORTED/KNOWN**.
- resource refinement as inclusion of allowed observations gives nondecreasing optimal distinguishability: **PROVED** (set-inclusion monotonicity; not PDT-specific).
- PDT-native quantitative law assigning/limiting genuinely joint distinction from microscopic interface resources: **OPEN**.
- same-input PDT-vs-QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next obligation
Do not use marginal-additive conservation in PDT-II. A viable PDT-native composition proposal must introduce a joint/interface distinction term or derive a constraint on it from independent microscopic resource assumptions. The strongest next attack is whether any proposed joint term is uniquely fixed by operational resource refinement rather than merely renamed classical correlation, mutual information, quantum correlation, or GPT composite structure.
