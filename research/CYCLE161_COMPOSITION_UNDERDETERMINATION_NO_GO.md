# Cycle 161 — Composition underdetermination no-go

## Priority
PDT-II target (1): PDT-native composition law; implications for target (2).

## Status
- **PROVED:** factor consistency on simple products does not uniquely determine a composite norm/resource law.
- **FALSIFIED:** the candidate claim that symmetry + factor normalization + product consistency alone force a unique PDT composite geometry (in particular Euclidean/Hilbert composition).
- **IMPORTED/KNOWN:** injective/projective tensor-norm nonuniqueness is standard Banach-space theory; local tomography and extra composition postulates are standard reconstruction ingredients.
- **OPEN:** a genuinely PDT-native axiom selecting one composite rule.
- **BREAKTHROUGH CANDIDATE:** NO.

## Exact hypotheses tested
Let finite-dimensional normed factor spaces X,Y represent candidate distinction spaces. Demand only:
1. positivity/nondegeneracy of the composite norm;
2. homogeneity and triangle inequality;
3. factor consistency on decomposable tensors, `alpha(x tensor y)=||x|| ||y||`;
4. exchange symmetry when X=Y (where applicable);
5. compatibility with reversible factor isometries.

Question: do these requirements uniquely select the composite norm and hence a PDT-native composition law?

## Theorem (composition underdetermination)
No. On X tensor Y there are, in general, distinct reasonable crossnorms satisfying factor consistency. In particular the injective norm epsilon and projective norm pi both satisfy the simple-tensor rule, while for entangled/non-decomposable tensors they can differ. Therefore agreement on every isolated factor and every product state is insufficient to determine composite geometry.

### Small decisive witness
Take X=Y=R^2 with Euclidean norm and identify u=e1 tensor e1 + e2 tensor e2 with the 2x2 identity matrix. Then

- injective norm epsilon(u) = operator norm(I_2) = 1;
- projective norm pi(u) = nuclear norm(I_2) = 2.

Both give alpha(x tensor y)=||x||_2||y||_2 on every simple tensor, both are symmetric under factor exchange, and both respect orthogonal factor isometries, yet they disagree on u. Thus the candidate uniqueness claim already fails for a 2x2 composite.

More generally for u_n=sum_{i=1}^n e_i tensor e_i in l2^n tensor l2^n,

    epsilon(u_n)=1,   pi(u_n)=n.

Hence the ambiguity grows linearly with dimension and is not a finite-size accident.

## Consequence for PDT-II
A PDT-native composition theorem cannot be obtained merely from factor-level distinction geometry, reversible symmetry, normalization, or multiplicativity on decomposable products. At least one genuinely composite PDT principle is required. Candidate principles must constrain non-decomposable states/records, e.g. a PDT-derived tomography/separation rule, an independently justified operational duality, or another primitive with testable composite consequences. Importing Hilbert tensor product, local tomography, or a preferred crossnorm would not count as a PDT-native derivation.

This also blocks a circular n=3 derivation that silently assumes the desired tensor/composite geometry before deriving its probability structure.

## Prior-art boundary
This theorem is deliberately not claimed as PDT novelty. Standard Banach-space tensor theory has distinct injective and projective reasonable crossnorms, with reasonable crossnorms lying between these extremal choices. Operational reconstructions of quantum theory add explicit composite assumptions such as tomographic locality/information locality rather than deriving the full composite structure from single-system symmetry alone.

## Next obligation
Search PDT primitives for a composite-only operational statement that (a) is not equivalent to assuming Hilbert composition/local tomography, (b) distinguishes epsilon/pi and other tensor rules on non-decomposable records, and (c) survives classical, real-quantum, complex-quantum and GPT countermodels. Until such a principle is derived, target (1) remains OPEN.
