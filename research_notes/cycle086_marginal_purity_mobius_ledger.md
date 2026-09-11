# Cycle 086 — Marginal-purity Möbius ledger

## Status

**PROVED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED.** Not a BREAKTHROUGH CANDIDATE.

## Exact statement

Let an N-partite density operator have local dimensions d_i and total dimension D. Under the local identity/traceless orthogonal decomposition, write

rho = sum_{S subseteq [N]} X_S,

where X_S is traceless exactly on the sites in S and proportional to identity on the complement. Define the labelled sector weight

C_S = D ||X_S||_2^2,

with C_empty = 1. For T subseteq [N], define

F(T) = D_T Tr(rho_T^2),  D_T = product_{i in T} d_i,

and F(empty)=1. Then

F(T) = sum_{S subseteq T} C_S.

Therefore Boolean-lattice Möbius inversion gives

C_S = sum_{T subseteq S} (-1)^(|S|-|T|) F(T).

Equivalently, for E_T=F(T)-1,

E_T = sum_{empty != S subseteq T} C_S.

## Proof

Take the partial trace to subsystem T. Any sector X_S with S not contained in T contains at least one traceless local factor on a traced-out site and therefore vanishes. Thus only S subseteq T survive. Surviving sectors remain Hilbert--Schmidt orthogonal after the partial trace. The maximally mixed factors on T complement supply exactly the dimension factors needed so that the normalized squared norm of the surviving S-sector is C_S. Summing orthogonal squared norms gives F(T)=sum_{S subseteq T} C_S. Möbius inversion on the Boolean subset lattice yields the second formula.

This proof requires no probability deformation, no dimension-specific assumption and no dynamics.

## Relation to Cycle 084

Cycle 084 proved that all **proper marginal states** do not universally determine the full global distinction ledger: GHZ-type coherence can change the top-order sector while every proper marginal stays fixed. The present theorem makes the boundary exact. Proper marginal purities reconstruct every proper labelled sector. To recover the top-order sector one additionally needs the global normalized purity F([N]); once that scalar is supplied, the complete labelled quadratic ledger follows by Möbius inversion.

Hence there is no contradiction. Cycle 084 is a global-completion no-go; Cycle 086 identifies precisely what scalar quadratic datum remains absent at top order.

## Regression evidence

A dense complex-state audit covered local/composite dimensions

1, 2, 3, 4, 2x2, 2x3, 3x3, 2x2x2, 2x3x2, 3x2x2 and 2x2x2x2,

using both pure and mixed states: 66 states, 294 direct-sector comparisons, maximum absolute residual 3.552713678800501e-15.

A separate diagonal/classical stress test covered qubit systems n=1 through n=12: 28 cases, 2506 sector checks, maximum absolute residual 2.232532214143919e-14. These computations are regression evidence only; the theorem is algebraic.

## Prior-art boundary

This result must not be presented as a PDT-native breakthrough. The multipartite Bloch/sector-length literature already relates purity to sector lengths and states that sector lengths can be represented through reduced-state purities and vice versa. See the 2024 Physics Reports review *Analysing quantum systems with randomised measurements*, DOI 10.1016/j.physrep.2024.09.009. The 2026 Physical Review A paper *Multiqubit monogamy relations beyond shadow inequalities*, DOI 10.1103/9fkf-hm8l, further develops reduced-purity constraints on sector lengths.

PDT may use this exact transform as accounting infrastructure, but novelty must come from a new physical law constraining the allowed sector ledger, its resource cost, dynamics, or experimentally falsifiable flow—not from the inversion itself.
