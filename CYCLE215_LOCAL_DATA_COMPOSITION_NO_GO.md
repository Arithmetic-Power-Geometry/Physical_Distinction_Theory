# Cycle 215 — Local-data composition no-go

## Target
PDT-II priority (1): determine whether the operational distinction structures of two components determine a unique composite distinction structure without importing a tensor/composition axiom.

## Status
**PROVED (conditional no-go); FALSIFIED (local-data-only unique composition); IMPORTED/KNOWN (prior-art boundary); OPEN (PDT-native selector). BREAKTHROUGH CANDIDATE: NO.**

## Definitions
For a finite system X and an admissible observation family A_X, define x ~_X x' iff a(x)=a(x') for every a in A_X. The operational quotient is Q_X=X/~_X.

A composite completion is an admissible family A_XY on X×Y whose restrictions to observations depending on X alone and Y alone reproduce the declared local families A_X and A_Y.

## Theorem — local operational data do not determine the composite quotient
There exist finite X,Y and two composite completions A_XY^(min), A_XY^(hol) with identical local operational data but non-isomorphic composite quotients.

### Exact witness
Let X=Y={0,1}. Let each local admissible family contain only constant binary observations. Hence |Q_X|=|Q_Y|=1.

Completion MIN contains only observations generated from the local constants. Every pair (x,y) is operationally equivalent, so |Q_XY^(min)|=1.

Completion HOL contains the same local observations plus the genuinely joint parity observation

    h(x,y)=x XOR y.

Its restriction cannot create a nonconstant local observation when the other subsystem is unavailable; the declared local operational structures are therefore unchanged. But h separates even from odd pairs, so |Q_XY^(hol)|=2.

Thus the same local quotients (indeed the same local observation families) admit distinct composite quotients. Therefore no rule F(Q_X,Q_Y), or rule using only the two local admissible families, can be a universally derived PDT composition law.

## Strengthening to arbitrary finite local dimension
For X=Y={0,...,n-1}, n>=2, retain trivial local families and add the joint equality indicator h_n(x,y)=1[x=y]. MIN has one composite class; HOL has two nonempty classes (diagonal/off-diagonal). Hence the obstruction persists for every n>=2. n=1 is the expected degenerate case where no nontrivial joint distinction exists.

This is an analytic all-n construction; exact code checks n=1..12.

## What is and is not proved
PROVED: local operational distinction data alone underdetermine the composite operational quotient.

FALSIFIED: any claim that PDT can obtain a unique composite distinction structure from local quotients/families alone, without an additional closure/tomography/composition principle.

NOT proved: that no PDT-native composition law can exist. A successful law may derive a physical rule specifying which joint observations/interventions are admissible.

NOT a same-input PDT-vs-QM prediction: choosing HOL rather than MIN is an extra composition choice unless PDT independently derives it.

## Prior-art boundary
The obstruction is conceptually adjacent to established failures of local tomography in generalized probabilistic theories and real-vector-space quantum theory. Hardy and Wootters (2010, arXiv:1005.4870) explicitly study theories where composite states contain information not recoverable from local statistics. Recent work likewise describes tomographically nonlocal theories as possessing holistic degrees of freedom inaccessible to local measurements (Baldijao et al., 2026, arXiv:2602.16280). Fermionic/superselection examples also exhibit non-local tomography (D'Ariano et al., 2013, arXiv:1307.7902). Therefore the no-go mechanism is **IMPORTED/KNOWN in spirit**, and is retained only to close a PDT-II logical loophole.

## Consequence for PDT-II
The strongest surviving composition obligation is no longer to guess an algebraic tensor rule. PDT must derive, from independent physical principles, a **joint admissibility/closure law** A_X,A_Y,R -> A_XY,R that decides whether holistic observations such as h are physically available. That law must survive restricted-resource, symmetry, controlled-environment and thermodynamic tests and must not encode the desired n=3 or QM deviation by construction.
