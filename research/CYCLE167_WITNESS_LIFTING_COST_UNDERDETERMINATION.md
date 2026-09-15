# Cycle 167 — Witness lifting does not determine composition unless the composite cost model is independently fixed

Status: **PROVED / CONDITIONAL / FALSIFIED / IMPORTED-KNOWN / OPEN**

## Targets attacked
PDT-II (1) PDT-native composition law, with consequences for (2) non-circular n=3, (4) resource-refinement/revelation laws, and (5) quantitative inequalities.

Cycle 166 left open a proposed repair: require every locally realizable distinction witness to lift to a composite witness with an explicit resource cost. This cycle asks whether that requirement itself selects a composite law.

## Candidate principle W
For every local distinction witness w_A realizable at cost c_A(w_A), and every auxiliary system B, there exists a lifted witness L_B(w_A) on AB that preserves the A-distinction and has a finite, specified lifting cost.

The hoped-for conclusion was that such witness lifting could determine PDT composition and eventually produce quantitative constraints.

## Theorem 167A — bare finite-cost witness lifting is not composition-complete
The conclusion is false without an independently derived composite resource metric.

Take finite classical systems A and B and let a local witness w_A be any Boolean function separating two A-records. Define the canonical lift

L_B(w_A)(a,b)=w_A(a).

This preserves every local distinction for every B.

Now define two admissible cost models on the same lifted witnesses:

**Model Z (zero surcharge):**

c_AB^Z(L_B(w_A)) = c_A(w_A).

**Model S_lambda (composite surcharge):** for any fixed lambda > 0,

c_AB^(lambda)(L_B(w_A)) = c_A(w_A)+lambda.

Both models satisfy existence of a finite lift, exact preservation of the local distinction, permutation/relabeling covariance when lambda depends only on the number/type of auxiliary factors, and monotonicity in c_A. Yet they give different quantitative composite costs for identical local witness data.

More generally, any nonnegative function s(B,R_B) gives

c_AB(L_B(w_A))=c_A(w_A)+s(B,R_B),

without changing which A-distinction is lifted. Thus witness existence plus finite cost does not derive the cost law; the cost law is extra structure. QED.

## Theorem 167B — even a fixed lifting cost does not determine relational distinctions
Suppose the surcharge is fixed to zero. Two composite operational theories can still agree on every lifted local witness L_B(w_A), L_A(w_B) while disagreeing on additional relational witnesses.

For A=B={0,1}, both theories contain the coordinate witnesses a and b at the same costs. Theory P contains only Boolean functions generated from the declared local records under the allowed local postprocessing. Theory R additionally admits a primitive parity witness r(a,b)=a XOR b at an independently assigned cost. They agree on all canonical lifts and their costs but differ in the primitive/generative structure of the joint witness set.

Therefore even exact cost-preserving lifting of all local witnesses does not determine which genuinely relational witnesses exist. QED.

This is the decisive counterexample to the proposed Cycle-166 repair.

## Dimension stress
For n binary factors, canonical coordinate witnesses w_i(x)=x_i lift identically in both constructions. A relational extension can additionally admit parity XOR_i x_i, Hamming-weight predicates, or other joint functions. Hence agreement on all local witness lifts persists for n=2,...,12 and arbitrarily high n while the relational witness algebra differs.

The n=1 case is degenerate: there is no composite relational sector to test.

## Edge/resource stress
- lambda=0: exact cost-preserving lift still fails to fix relational structure (Theorem 167B).
- lambda>0: finite surcharge family shows quantitative underdetermination.
- lambda depending only on factor count: associativity can be retained by choosing an additive surcharge, e.g. s(k)=alpha(k-1), alpha>=0.
- blind/restricted relational sector: local lifts may survive while all nonlocal relational primitives are excluded.
- enriched relational sector: the same local lifts may coexist with additional joint witnesses.

Thus the failure is not an artifact of one norm, one dimension, or one extreme blind-composite rule.

## Prior-art boundary
This cycle does **not** claim witness lifting or discrimination cost as novel. Constrained local-vs-global state discrimination and resource-assisted discrimination are established quantum-information topics; LOCC restrictions can make globally distinguishable states locally indistinguishable, and entanglement/multiple-copy resources can change discrimination power. Existing literature therefore already establishes that discrimination capability depends on the allowed composite resource class. The PDT-specific contribution here is only a falsification boundary: a proposed witness-lifting axiom cannot by itself derive that resource class.

Relevant prior-art checks for this cycle include work on multicopy adaptive local discrimination (Banik et al., PRL 126, 210505, 2021), bounds on optimal local discrimination (Ha & Kim, Scientific Reports 12, 14130, 2022), and resource-efficient discrimination of multipartite bases. These reject any novelty claim based merely on 'resource cost for lifting distinguishability'.

## Consequence for PDT-II
The Cycle-166 proposed repair is closed in its bare form:

> local witness lifting + finite/explicit cost does not imply a unique PDT composite law.

A non-circular PDT-native composition result now needs an independently motivated *generation rule* for the composite witness set and an independently derived resource functional on that generated set. Merely postulating a lifting surcharge relocates rather than solves the composition problem.

This also blocks using an arbitrary lifting cost as the source of a PDT-vs-QM inequality: unless the cost is derived from independently measurable PDT primitives, any resulting quantitative discrepancy would be parameter/model choice rather than a same-input prediction.

## Classification
- Bare witness-lifting principle as a unique composition selector: **FALSIFIED**.
- Zero-vs-surcharge counterfamily: **PROVED**.
- Exact cost-preserving local lifting still leaves relational sector undetermined: **PROVED**.
- Connection to constrained/resource-assisted discrimination: **IMPORTED/KNOWN**.
- Any theorem after independently specifying a composite resource metric: **CONDITIONAL**.
- PDT-native generation rule for relational witnesses: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input PDT != QM quantitative prediction: **OPEN**.
- Experimentally distinctive PDT inequality: **OPEN**.
- Gravity/capacity law: **OPEN; not imported or asserted**.
- BREAKTHROUGH CANDIDATE: **NO**.
