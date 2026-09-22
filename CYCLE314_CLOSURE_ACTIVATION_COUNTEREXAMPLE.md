# Cycle 314 — Closure Activation Destroys Generic Revelation Submodularity

## Target
PDT-II target (4): resource-refinement / revelation / conservation laws, following the open closure boundary in Cycle 313.

## Setup
Let primitive resources be E={a,b}. A resource window R does not expose only its primitive elements; instead it generates an operational closure cl(R) of admissible distinguishers. For fixed states x,y let every generated distinguisher e have score w_e(x,y)>=0 and define

    D(R;x,y)=max_{e in cl(R)} w_e(x,y),

with baseline score 0 when no nontrivial distinguisher is available.

Assume only monotone closure: R subset S implies cl(R) subset cl(S).

## Theorem 314.1 — monotonicity survives arbitrary monotone closure
If R subset S, then D(R;x,y)<=D(S;x,y).

**Status: PROVED.** The maximization domain cl(R) is contained in cl(S).

## Theorem 314.2 — submodularity does not survive closure activation
Monotone operational closure alone does not imply

    D(A)+D(B) >= D(A union B)+D(A intersection B).

**Status: FALSIFIED as a generic law / counterexample PROVED.**

Take

    cl(empty)={0},
    cl({a})={0,a},
    cl({b})={0,b},
    cl({a,b})={0,a,b,c},

where c is a jointly generated distinguisher unavailable from either primitive resource alone. Assign

    w_0=w_a=w_b=0,  w_c=1.

Then

    D(empty)=0,
    D({a})=0,
    D({b})=0,
    D({a,b})=1.

For A={a}, B={b}, submodularity would demand 0+0 >= 1+0, which is false. The smallest obstruction therefore already uses two primitive resources and one activated joint distinguisher.

The same witness falsifies diminishing returns: the marginal gain of b is 0 when added to empty, but 1 when added after a.

## Strengthened surviving statement
For closure-generated distinguishability, resource inclusion guarantees monotonicity, but neither diminishing returns nor a conservation identity follows without an additional structural condition on cl and the generated scores. Complementarity/activation can produce strict increasing returns.

A sufficient non-activation condition is the Cycle-313 regime in which every distinguisher available from A union B was already individually present in A or B, so D is a max of fixed element-wise weights. Once genuinely new joint distinguishers may be generated, that proof no longer applies.

## Dimension and model stress
The obstruction is combinatorial and dimension-independent. It can be embedded in any operational theory possessing two resources whose joint closure activates a distinguisher not generated separately. Consequently increasing dimension cannot repair the claimed generic inequality. The witness applies to n=1 through n=12 at the abstract resource-closure level and to higher dimensions by embedding; it does **not** assert that every physical model realizes such activation.

Edge cases checked analytically: empty window, zero-score primitives, duplicate zero-score probes, and strict joint activation. Replacing score 1 by any delta>0 gives the same violation magnitude delta.

## Prior-art boundary
Restricted-measurement distinguishability and resource-dependent distinguishability are established subjects. Quantum data hiding, for example, studies how discrimination power changes under restricted measurement classes; Matthews, Wehner and Winter (Commun. Math. Phys. 291, 813–843, 2009; arXiv:0810.2327) is relevant prior art. Activation/complementarity phenomena therefore must not be presented as a PDT invention merely because they defeat a candidate PDT law.

This cycle claims only the logical no-go boundary: monotone closure by itself is insufficient to derive submodularity.

## Classification
- monotonicity under monotone operational closure: **PROVED**
- generic closure-generated revelation submodularity: **FALSIFIED**
- two-resource activation counterexample: **PROVED**
- generic diminishing returns under closure: **FALSIFIED**
- physical conservation law from resource inclusion: **FALSIFIED as an inference**
- restricted-measurement / data-hiding background: **IMPORTED/KNOWN**
- PDT-native condition separating diminishing-return and activation regimes: **OPEN**
- PDT-native composition law: **OPEN**
- non-circular n=3 selector: **OPEN**
- same-input PDT/QM deviation: **OPEN**
- experimentally distinctive PDT inequality: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**

## Consequence for PDT-II
Any defensible PDT revelation theorem must explicitly specify the operational closure rule. A universal submodularity claim is now ruled out. The next viable target is to derive, rather than assume, a PDT-native closure/composition rule and determine whether it enforces a quantitative bound on activation gain that is stronger than generic GPT/resource-theory behavior.
