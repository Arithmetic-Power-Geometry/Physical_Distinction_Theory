# Cycle 237 — Maximum-entropy composition selector no-go

## Target attacked

PDT-II target (1): derive a PDT-native composition law from the surviving requirement that genuinely joint information, rather than marginal-only resource bookkeeping, must select admissible composites.

## Candidate principle

Given local finite probability states `p_A` and `p_B`, choose the physical composite `q_AB` as the coupling with those marginals that maximizes Shannon entropy:

`q* = argmax_{q: q_A=p_A, q_B=p_B} H(q)`.

This is an attractive candidate because it is a genuine joint optimization and gives a unique coupling for fixed finite marginals.

## Exact theorem

**Theorem (fixed-marginal MaxEnt collapses to independence).** For any finite marginals `p_A,p_B`,

`H(A,B) = H(A)+H(B)-I(A;B) <= H(A)+H(B)`,

with equality iff `I(A;B)=0`, equivalently `q_AB=p_A p_B` on the support. Therefore the unique maximum-entropy coupling is the product coupling.

### Proof

The marginals are fixed, so `H(A)` and `H(B)` are constants over the coupling polytope. Non-negativity of KL divergence gives

`I(A;B)=D_KL(q_AB || p_A p_B) >= 0`,

with equality iff the two distributions agree. Substitution in the entropy identity proves the claim. QED.

## Decisive physical counterexample to using MaxEnt as a universal composition law

Take a fair binary source `X`. Let `A=X` and `B=X`. The physically prepared joint record is

`q_corr(0,0)=q_corr(1,1)=1/2`, `q_corr(0,1)=q_corr(1,0)=0`.

Both marginals are fair. The MaxEnt selector applied to only those marginals instead returns

`q_ME(a,b)=1/4` for all four pairs.

Thus the selector replaces a perfectly correlated physical preparation by an independent one. It is a rule for inference from incomplete constraints, not a law deriving which physical composite was prepared.

The witness embeds in every alphabet size `n>=2` by assigning zero probability to symbols `2,...,n-1`; `n=1` is degenerate. Hence exact dimension checks `n=1,...,12` cannot select `n=3`.

## Constraint-set dependence

If the correlation constraint `P(A=B)=1` is included, the correlated coupling is admissible and the independent product is not. If only the marginals are supplied, MaxEnt returns the product. Therefore the output is determined by which physical constraints are declared known. MaxEnt cannot generate those missing physical constraints itself.

This also closes a same-input loophole: comparing PDT's MaxEnt completion of local marginals with QM's explicitly correlated global state changes the microscopic/global input and is not an admissible `P_PDT(O|I,R) != P_QM(O|I,R)` comparison.

## Prior-art boundary

This route is not PDT-native. Jaynes' maximum-entropy principle is established statistical-inference/statistical-mechanics machinery. The fixed-marginal maximum-entropy coupling problem is established in the literature; the maximum-entropy coupling with only fixed marginals is the independent coupling. Maximum-caliber/path-entropy variants likewise move the same inferential principle to trajectories rather than supplying PDT-native physical composition data.

Representative prior art checked in this cycle:

- E. T. Jaynes, *Information Theory and Statistical Mechanics*, Physical Review 106, 620 (1957), DOI 10.1103/PhysRev.106.620.
- H. Larralde, *Maximum-entropy distributions of correlated variables with prespecified marginals*, Physical Review E 86, 061117 (2012), DOI 10.1103/PhysRevE.86.061117.
- A. Franc, M. Goulard, N. Peyrard, *Chordal Graphs to Identify Graphical Model Solutions of Maximum of Entropy Under Constraints on Marginals*, SIAM Journal on Discrete Mathematics.

## Status

- Fixed-marginal MaxEnt theorem: **PROVED**.
- MaxEnt as PDT-native provenance: **IMPORTED/KNOWN**.
- Universal physical-composition claim from local PDT data: **FALSIFIED** by the correlated binary preparation.
- Non-circular `n=3` selection: **OPEN**; this route does not select 3.
- Same-input PDT-vs-QM prediction from this selector: **FALSIFIED** unless an independently derived PDT physical constraint changes the admissible set while preserving identical microscopic input.
- BREAKTHROUGH CANDIDATE: **NO**.

## Strongest surviving obligation

PDT must derive, from PDT primitives and a declared resource window, a physical **joint admissibility constraint** `J_PDT(A,B,R)` that is not merely an inference convention. Only after `J_PDT` is independently derived may optimization over the resulting coupling/state set be physically meaningful. The next attack should test candidate `J_PDT` constraints against ordinary correlation constraints, causal compatibility, no-signalling, GPT tensor cones, thermodynamic constraints, and quantum marginal/extension conditions before any novelty claim.
