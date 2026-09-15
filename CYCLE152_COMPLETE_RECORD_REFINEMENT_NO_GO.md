# PDT-II Cycle 152 — Complete-Record Refinement No-Go

## Target

Attack Cycle 151's strongest open bridge: can a nontrivial local refinement be proved operationally neutral for the **complete** declared resource-window record without building the desired quotient into the window?

## No-go theorem

Let `E` replace one positive resolved channel of weight `x` by `k>=2` positive daughters `x w_1,...,x w_k`, with `sum_j w_j=1`. Suppose the admissible operational family contains at least one daughter-resolving observation `D` whose outcome record distinguishes the unsplit channel from the resolved daughter tuple. Then

`pi_R(E q) != pi_R(q)`

for every resource window `R` that includes `D`.

**Proof.** `D` is, by hypothesis, an admissible observation in `R` and has different records before and after `E`. Equality of complete operational records would require equality for every admissible observation in `R`, contradicting the record difference under `D`. QED.

This is elementary but decisive: a nontrivial refinement cannot be called neutral for a *complete* operational record if the declared window can itself resolve the refinement.

Classification: **PROVED**, conditional only on inclusion of a daughter-resolving observation.

## Decisive falsification

The stronger Cycle-151 hope

> a nontrivial refinement is neutral for the complete operational record, independently of the declared window

is **FALSIFIED**.

A two-daughter witness suffices. Start with one positive channel `(x)`, `x>0`, and refine it to `(x/2,x/2)`. A coarse mass observation returns `x` in both cases, but a resolved-channel-count observation returns `1` versus `2`; equivalently, a daughter-resolving measurement returns different resolved tuples. Exact merge recovery does not erase that distinguishability while the daughters remain accessible.

## Surviving theorem

Refinement neutrality is necessarily **window-relative**. If `R_coarse` excludes all daughter-resolving observables and retains only a coarse statistic such as total mass, then the split can be neutral in that restricted quotient. If `R_fine` includes a daughter-resolving observable, neutrality fails.

Therefore Cycle 151 cannot close composition merely by calling `pi_R` the complete record. PDT must independently justify why the physically relevant resource window excludes refinement-resolving information, or derive an equivalence relation from primitive operational limitations. Otherwise the quotient risks encoding the desired invariance by construction.

## Exact audit

`cycle152_complete_record_no_go.py` uses exact rational arithmetic over dimensions `1..12,16,24,32,48,64,96,128`, random sparse vectors, and 2--5 strictly positive daughters. It checks:

- total/coarse record conservation;
- exact merge recovery;
- failure of fine-record neutrality.

The analytic theorem does not depend on the randomized audit.

## Prior-art boundary

This no-go mechanism is not claimed as novel mathematics or physics. Statistical comparison and Blackwell sufficiency distinguish fine experiments from their coarse-grainings; quantum statistical comparison likewise treats coarse-graining as loss/restriction of operational information. Resource theories of distinguishability explicitly quantify operationally accessible discrimination. The PDT contribution here is only a logical boundary on the proposed PDT-II derivation route.

Relevant prior-art families include Blackwell comparison of experiments; Buscemi's quantum statistical sufficiency/coarse-graining framework; and Wang--Wilde resource theories of distinguishability.

## Consequence for PDT-II target (1)

The composition bridge now has to satisfy a stronger non-circular obligation:

1. specify the resource window `R` from PDT primitives, before choosing the ledger;
2. prove that no admissible observation in `R` resolves the proposed refinement;
3. prove quotient-extensionality of the resource ledger on that independently derived quotient;
4. only then invoke Cycle 151 and Cycle 149.

If PDT instead permits daughter-resolving observations, the operational-neutrality route to composition is blocked and another native composition principle is required.

## Status ledger

- nontrivial refinement cannot be neutral in a window containing a resolving observable: **PROVED**
- window-independent complete-record neutrality: **FALSIFIED**
- coarse-window neutrality for mass-preserving splits: **PROVED** for the stated coarse record
- exact implementation stress audit: **NUMERICALLY SUPPORTED** once frozen output is committed
- statistical/coarse-graining mechanism: **IMPORTED/KNOWN**
- PDT-native derivation of the physically privileged restricted window: **OPEN**
- PDT-native composition law: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
