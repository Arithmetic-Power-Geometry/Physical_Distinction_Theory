# Cycle 047 — Three-axis correlation kill test

## Target
Test whether the CHSH-matching capped correlation body from the previous cycle can remain a viable full composite for an elementary `n=3` Euclidean system.

## Candidate bodies
For real correlation matrices `T` define

`C_op = {T : ||T||_op <= 1}`

and

`C_cap = {T : ||T||_op <= 1, ||T||_* <= 2}`.

The second body was useful because it is different from `C_op` while still attaining the same rank-two CHSH Tsirelson value.

## Exact three-setting functional
Let `P_r = diag(1,...,1,0,...)` have rank `r`, and define

`M_r(T) = <P_r,T> = sum_{i=1}^r T_ii`.

By duality of operator and nuclear norms,

`sup_{||T||_op<=1} |M_r(T)| = ||P_r||_* = r`.

For `C_cap`,

`|M_r(T)| <= ||P_r||_op ||T||_* <= 2`.

The bound is tight for `r>=2`, e.g. `T=diag(1,1,0,...)`. Hence

`sup_{C_cap}|M_r| = min(r,2)`.

The smallest separation is therefore `r=n=3`:

`C_op: |M_3| <= 3`, while `C_cap: |M_3| <= 2`.

## Decisive quantum witness
For the ordinary two-qubit singlet, Pauli-axis correlations obey

`<sigma_i tensor sigma_j> = -delta_ij`,

so its correlation tensor is `T_singlet=-I_3`. Thus

`||T_singlet||_op=1`, `||T_singlet||_*=3`, and `|M_3|=3`.

Therefore `T_singlet in C_op` but `T_singlet notin C_cap`.

This is a decisive falsification of `C_cap` as a candidate *full* qubit/PDT composite if PDT is required to recover the standard singlet sector. Matching CHSH alone was insufficient: a rank-three witness exposes the missing correlations immediately.

## Dimension audit
The exact audit covers `n=1..12`. No separation is possible for `n<=2`; every `n>=3` contains the same embedded rank-three witness. No numerical approximation is needed for the theorem.

## Prior-art boundary
The norm duality used in the proof is standard functional analysis; correlation-type Bell inequalities and singular-value/Tsirelson bounds are established; and the singlet identity `E(a,b)=-a dot b` is standard quantum mechanics. The PDT-specific contribution here is a falsification audit of this branch's previously proposed CHSH-matching composite, not a claim of new mathematics or new experimental physics.

## Classification
- `PROVED`: exact support-function bounds for `M_r`.
- `FALSIFIED`: `C_cap` as a viable full n=3 composite reproducing the singlet sector.
- `IMPORTED/KNOWN`: norm duality, singlet correlations, Bell/Tsirelson background.
- `BREAKTHROUGH CANDIDATE`: no.

## Consequence for PDT-II
Future composition candidates must pass at least a rank-stratified battery, not only CHSH: two-setting/rank-two agreement can conceal failures visible to three-setting/rank-three correlations. Any claimed PDT-native composite should reproduce or explicitly depart from the singlet triad with a declared same-input physical law and a falsifiable reason.
