# PDT-II Cycle 328 — Tensor-norm selector no-go

Status: **DECISIVE FALSIFICATION / route closure**

## Candidate attacked
A possible PDT-native composition rule might try to infer the composite distinguishability structure from the local distinction norms alone, requiring a reasonable cross-norm/tensor-norm extension that agrees on product distinctions.

## Exact hypotheses tested
Let local real normed distinction spaces be `(V_A, ||.||_A)` and `(V_B, ||.||_B)`. Require a composite norm `||.||_AB` on the algebraic tensor product satisfying at minimum the product rule

`||x ⊗ y||_AB = ||x||_A ||y||_B`

and ordinary norm axioms. Ask whether these local data uniquely determine the composite norm and hence correlated-state distinguishability.

## Result
They do not. In finite-dimensional normed spaces there are canonical projective and injective cross norms,

`||z||_pi = inf sum_i ||x_i||_A ||y_i||_B`,

`||z||_epsilon = sup{|(f ⊗ g)(z)| : ||f||_* <= 1, ||g||_* <= 1}`,

both agreeing exactly on every simple tensor, but generally differing on correlated tensors.

### Small decisive witness
Take `V_A = V_B = R^2` with Euclidean norm and

`z = e1⊗e1 + e2⊗e2`.

Identifying `z` with the 2x2 identity matrix, the injective norm is its operator norm, `||z||_epsilon = 1`, while the projective norm is its nuclear norm, `||z||_pi = 2`. Thus the same local norm, same local dimensions, and exact product multiplicativity admit inequivalent correlated-composite distinction norms already for 2x2 systems.

The witness embeds block-diagonally into every local dimension `n >= 2`, including n=3 through n=12 and arbitrary higher finite dimension. Therefore there is no n=3 exception.

## Consequences for PDT-II
1. Local distinction geometry plus product multiplicativity does **not** determine correlated-composite distinction.
2. Any PDT composition law must contain an independently derived rule constraining correlated tensors/effects; choosing one tensor norm by fiat is circular.
3. No same-input `P_PDT(O|I,R) != P_QM(O|I,R)` follows from local norms and simple-tensor multiplicativity alone.
4. Restricted measurement norms/data-hiding phenomena reinforce that correlated distinguishability depends on the declared measurement/resource family, not only local state norms.

## Prior-art audit
This mechanism is known mathematics/physics, not a PDT novelty claim. Projective/injective tensor norms are standard Banach-space constructions and are used explicitly in GPT data-hiding analyses. Restricted measurement families are also known to induce different distinguishability norms. Accordingly, only the application as a PDT route-closing test is recorded here.

Relevant literature checked this cycle:
- Lami, Palazuelos & Winter, *Ultimate data hiding in quantum mechanics and beyond* (2017), arXiv:1703.03392.
- Matthews, Wehner & Winter, *Distinguishability of quantum states under restricted families of measurements with an application to quantum data hiding* (2009), arXiv:0810.2327.
- Janotta & Lal, *Generalized probabilistic theories without the no-restriction hypothesis*, Phys. Rev. A 87, 052131 (2013).

## Classification ledger
- projective/injective cross-norm constructions: **IMPORTED/KNOWN**
- explicit R^2 ⊗ R^2 witness (`epsilon=1`, `pi=2`): **PROVED**
- extension to n=2..12 and all finite n>=2 by embedding: **PROVED**
- local distinction norm + product multiplicativity => unique composite norm: **FALSIFIED**
- same assumptions => n=3: **FALSIFIED**
- same assumptions => unique same-input PDT/QM deviation: **FALSIFIED as an inference**
- independently derived PDT-native correlated-tensor selector: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**

## Next strongest target
Search for a genuinely PDT-native constraint on correlated distinctions that is not merely a renamed choice of tensor cone/norm or measurement family. Any candidate must distinguish projective vs injective (and intermediate) completions from independently stated PDT operational hypotheses before it can support a quantitative PDT prediction.
