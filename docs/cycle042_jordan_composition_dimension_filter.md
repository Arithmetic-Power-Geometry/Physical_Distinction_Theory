# Cycle 042 — Jordan self-composition dimension filter

**Status:** CONDITIONAL + IMPORTED/KNOWN mathematics. **Not a PDT breakthrough.**

## Claim

Restrict attention to the associative real normed division algebras `K = R,C,H`, with real dimension `d = 1,2,4`.  The normalized state body of the two-level Hermitian Jordan model `H_2(K)` is a Euclidean ball of Bloch dimension

`n = d + 1`.

Assume additionally that the self-composite is the corresponding standard four-level Hermitian matrix model `H_4(K)` and that the composite is **locally tomographic**, i.e. the real order-unit dimension of the composite equals the product of the local order-unit dimensions.

Then local tomography forces `d=2`, hence `K=C` and `n=3`.

## Exact proof

For associative `K` of real dimension `d`,

`dim_R H_m(K) = m + C(m,2)d`.

Therefore

`dim_R H_2(K) = 2+d`

and

`dim_R H_4(K) = 4+6d`.

Local tomography of two identical systems requires

`4+6d = (2+d)^2`.

Rearrangement gives

`d(2-d)=0`.

Since `d>0`, the unique solution is `d=2`.  Thus the local normalized ball has

`n=d+1=3`.

The explicit dimension mismatches are:

- real bit (`d=1`, `n=2`): local product dimension `3^2=9`, standard real composite dimension `10`;
- complex bit (`d=2`, `n=3`): local product dimension `4^2=16`, standard complex composite dimension `16`;
- quaternionic bit (`d=4`, `n=5`): local product dimension `6^2=36`, standard quaternionic matrix dimension `28`.

The octonionic two-level spin factor (`n=9`) does not extend to a standard `H_4(O)` Euclidean Jordan matrix model, so it is outside this assumed self-composition route rather than an additional solution.

## Why this does not solve PDT-II natively

The theorem imports two large pieces of physical structure that PDT has not derived:

1. the choice of the Jordan matrix family as the composite rule;
2. local tomography.

Accordingly this result is a **composition-based conditional selector**, not a non-circular PDT-native derivation of spatial/distinction dimension three.

## Prior-art boundary

The result sits inside established Jordan/GPT reconstruction mathematics. Barnum and Wilce use Hanche-Olsen-type results to show that local tomography plus Jordan structure and a qubit strongly constrain theories to ordinary complex quantum mechanics; later work by Barnum, Graydon and Wilce studies which Euclidean Jordan algebras admit suitable composites and explicitly emphasizes failures of local tomography and restrictions on spin-factor composites. The elementary dimension calculation here is therefore not claimed as historically novel.

Useful references:

- Howard Barnum and Alexander Wilce, *Local tomography and the Jordan structure of quantum theory*, Foundations of Physics 44 (2014), arXiv:1202.4513.
- Howard Barnum, Matthew A. Graydon and Alexander Wilce, *Composites and Categories of Euclidean Jordan Algebras*, Quantum 4, 359 (2020), based on arXiv:1507.06278 and subsequent development.

## Research consequence

This cycle identifies a sharp boundary:

`Euclidean local ball + standard division-algebra Jordan self-composition + local tomography => n=3`,

but removing either the imported composite family or local tomography destroys the derivation. A genuine PDT-II advance must therefore derive an equivalent restriction from distinction/resource/composition primitives rather than assume it.
