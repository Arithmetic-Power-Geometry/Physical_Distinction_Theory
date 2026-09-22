# Cycle 315 — Product Multiplicativity Does Not Determine PDT Composite Distinction

## Target
PDT-II target (1): PDT-native composition law.

## Candidate principle attacked
A tempting PDT composition axiom is that independent distinctions multiply on product differences:

    D_AB(x tensor y) = D_A(x) D_B(y).

Together with norm/convexity assumptions, one might hope this determines the distinction geometry of a composite system.

## Exact countermodel
Let local signed-difference spaces be X=Y=R^d with the Euclidean norm, d>=2. On the algebraic tensor product X tensor Y there are at least two canonical cross norms:

1. the injective norm epsilon;
2. the projective norm pi.

Both satisfy exactly, for every simple tensor,

    ||x tensor y||_epsilon = ||x||_2 ||y||_2
    ||x tensor y||_pi      = ||x||_2 ||y||_2.

Thus both obey the same independent-product composition law.

Identify X tensor Y with d by d real matrices. In this Euclidean case the injective norm is the spectral/operator norm and the projective norm is the nuclear/trace norm. For the correlated tensor

    Z_k = sum_{i=1}^k e_i tensor e_i,    2 <= k <= d,

its nonzero singular values are k copies of 1, hence

    ||Z_k||_epsilon = 1,
    ||Z_k||_pi = k.

Already for d=2 and Z_2=diag(1,1), the two admissible composite norms agree on every product tensor yet give 1 versus 2 on the same correlated tensor.

## Theorem 315.1 — product multiplicativity is compositionally incomplete
Assume only that local distinction spaces are normed and the composite distinction norm is a cross norm agreeing multiplicatively on simple tensors. Then local distinction norms plus exact product multiplicativity do not uniquely determine the composite distinction of correlated tensors.

**Status: PROVED.** The epsilon/pi construction above supplies two composite norms satisfying the identical local and product constraints but disagreeing on Z_2.

## Corollary 315.2 — arbitrarily large ambiguity
For d>=k>=2, the same local/product data permit a factor-k separation on Z_k:

    ||Z_k||_pi / ||Z_k||_epsilon = k.

Therefore the ambiguity is not a small perturbative defect; it grows with available correlated rank.

**Status: PROVED.** Directly from the singular spectrum of Z_k.

## Dimension stress
For each d=2,...,12 choose Z_d=I_d. Then epsilon(Z_d)=1 and pi(Z_d)=d exactly. For d=1 the norms coincide, so d=2 is the smallest decisive dimension. The construction extends to every finite d and the separation grows linearly with d. No randomized test is required for the theorem because the witness is exact and analytic.

Degenerate/simple-tensor edge cases are also exact: zero tensors have both norms zero; rank-one tensors have equality; disagreement begins only when genuinely non-simple tensor directions are admitted.

## Physical/GPT interpretation boundary
This is a mathematical no-go about composition axioms, not a claim that either tensor norm is automatically the physical PDT composite. To turn a norm into a physical distinguishability structure one must additionally specify the admissible composite state/effect cones and normalization. The result says that product multiplicativity alone cannot perform that selection.

The distinction is directly relevant to restricted resources: a composite theory may agree perfectly on every independently prepared/product direction while differing on correlated or entangled directions. Consequently a PDT-native composition law must constrain non-simple tensors, not merely products.

## Prior-art boundary
Injective and projective tensor norms, their extremal cross-norm role, and their use in quantum-information/entanglement theory are established mathematics and physics. In Euclidean matrix spaces, operator and nuclear norms provide the standard concrete realization. Cross-norm criteria for entanglement and injective/projective norm methods are also established. Therefore neither epsilon/pi nor the existence of tensor-norm ambiguity is claimed as a PDT invention.

The PDT contribution of this cycle is only the audited no-go boundary for the proposed route: a native composition principle cannot consist solely of product multiplicativity.

## Consequences for remaining PDT-II targets
- A PDT-native composition law must specify behavior on correlated/non-simple tensors or derive a physical cone/effect structure that selects it.
- Product multiplicativity cannot select n=3: the epsilon/pi ambiguity exists for every d>=2.
- It cannot yield a parameter-free same-input PDT/QM deviation because two admissible composite extensions already disagree before a PDT selector is supplied.
- Any experimentally distinctive inequality based on composite distinction must state which composite norm/cone is physically selected.

## Classification
- exact product multiplicativity for epsilon and pi: **PROVED / IMPORTED-KNOWN**
- product multiplicativity uniquely determines composite distinction: **FALSIFIED**
- d=2 smallest correlated witness (1 versus 2): **PROVED**
- d=2,...,12 exact factor-d witness: **PROVED**
- arbitrary finite-d factor-d extension: **PROVED**
- injective/projective tensor-norm machinery: **IMPORTED/KNOWN**
- PDT-native selector on correlated tensors: **OPEN**
- PDT-native composition law: **OPEN**
- non-circular n=3 derivation: **OPEN**
- same-input PDT/QM deviation: **OPEN**
- experimentally distinctive PDT inequality: **OPEN**
- gravity/capacity law: **OPEN; NOT ATTEMPTED WITHOUT NATIVE COMPOSITION**
- BREAKTHROUGH CANDIDATE: **NO**

## Next strongest obligation
Test whether adding natural associativity, symmetry under subsystem exchange, local reversible invariance, and monotonicity under local contractions is enough to select a unique cross norm. If not, record the smallest exact counterfamily; if a unique survivor appears, audit it against Banach tensor-norm and GPT prior art before treating it as PDT-native.
