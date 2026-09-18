# Cycle 235 — Common-refinement selector: exact prior-art/novelty boundary

## Target attacked
PDT-II target (4), with consequences for (1) and (3): can the free redundancy parameter left by Cycle 234 be fixed by defining *redundant distinction* as the greatest distinction obtainable from a single record/channel that is reproducible by post-processing every available record/channel?

## Candidate PDT rule
Let H be the latent hypothesis and let K_i: H -> X_i be the experiment/channel associated with record i. Write Q \preceq_B K_i when Q is a Blackwell degradation of K_i, i.e. Q = L_i K_i for a stochastic post-processing L_i. Define

    R_common(K_1,...,K_m;H)
      = sup_{Q: Q \preceq_B K_i for every i} D(H;Q),

for a declared distinction functional D.

Interpretation: count as redundant only distinction obtainable through one common degraded experiment simulable from each source independently.

## Exact checks
1. **Duplicate record.** K_1=K_2=K. Then K itself is feasible, so R_common >= D(H;K). Under data processing no feasible Q can exceed D(H;K); hence equality.
2. **Independent two-bit copy.** H=(A,B), X=A, Y=B with independent fair bits. Any Q that is simultaneously a degradation of the A-channel and B-channel and carries nonconstant information about H would require a nontrivial common stochastic statistic of independent coordinates. For deterministic common statistics it is constant; under the Blackwell common-degradation optimization the intended common-information construction assigns no shared decision content in this canonical case.
3. **XOR synergy witness.** H=X xor Y with X,Y fair. Each singleton channel is independent of H, so data processing forces every common degradation to have zero H-distinction, while the joint record can have one bit. Thus the rule permits pure synergy.
4. **n=1.** Degenerate.
5. **n=2..12.** The duplicate and XOR witnesses use only a binary subalphabet and therefore embed in every alphabet n>=2. No dimension-3 selection occurs.

## Proof status
The duplicate-record identity follows directly from feasibility plus data processing. The XOR zero-redundancy conclusion follows because each singleton has zero H-information and any degradation cannot increase it. These are exact, not simulation claims.

## Decisive prior-art check
This candidate is not PDT-native novelty. The information-decomposition literature already defines degradation/intersection information by maximizing mutual information over a channel Q that is a Blackwell degradation of every source channel. This is precisely the operational skeleton above when D is mutual information. The broader PID literature also explicitly distinguishes the redundancy lattice from the additional redundancy measure needed to assign its atoms.

Therefore relabelling a greatest common Blackwell degradation as a PDT physical selector would be rediscovery. Different D may create a different optimization numerically, but novelty cannot be claimed merely by replacing the monotone; a PDT-specific physical derivation and a theorem/prediction not reducible to known channel-order/resource monotones would still be required.

## Consequences
- This route can fix the Cycle-234 free parameter only by importing an existing operational selector.
- It supplies no n=3 selector: the construction is dimension-uniform and the exact binary witnesses embed for all n>=2.
- It supplies no same-input PDT-vs-QM prediction by itself. If both theories are given the same channels, retained records, post-processing class, resource window and the same operational monotone, the imported selector alone does not create a probability-law difference.
- A future PDT candidate must derive a restriction or operational quantity from PDT primitives that is not simply Blackwell degradation, more-capable/less-noisy ordering, deficiency, PID redundancy, or another known channel comparison.

## Classification
- Candidate common-degradation selector as **PDT-native novelty**: **FALSIFIED**.
- Duplicate/XOR consequences under stated hypotheses: **PROVED**.
- Blackwell-degradation/intersection construction: **IMPORTED/KNOWN**.
- PDT-native physical selector fixing redundancy: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Search for a PDT-native selector whose feasible set is derived from distinction/refinement resource constraints rather than stipulated post-processing order. Before promotion, compare it explicitly against Blackwell, less-noisy, more-capable, deficiency, common-information and PID constructions, then run exact n=1..12 and adversarial composite tests.
