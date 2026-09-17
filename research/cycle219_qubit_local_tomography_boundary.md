# PDT-II Cycle 219 — Qubit + Local Tomography Reconstruction Boundary

## Status

- **PROVED (conditional methodological no-go)**
- **IMPORTED/KNOWN**: Jordan-algebra reconstruction machinery
- **FALSIFIED**: candidate claim that spectrality/strong symmetry + local tomography + a qubit gives a PDT-native composition law or PDT-vs-QM deviation
- **OPEN**: PDT-native resource-indexed admissibility/composition law
- **BREAKTHROUGH CANDIDATE: NO**

## Target attacked

Primary: PDT-native composition law and non-circular n=3 derivation. Secondary: same-input quantitative PDT-vs-QM prediction.

## Hypotheses

Let an operational theory satisfy assumptions sufficient to place its single-system state spaces in the finite-dimensional Euclidean-Jordan family (for example spectrality + strong symmetry under the hypotheses of Barnum–Hilgert). Add a physically admissible composite rule satisfying the constraints required by the Barnum–Wilce/Hanche-Olsen route: non-signalling, local tomography, and the presence of a qubit, together with their stated natural constraints on systems/composites.

## Conditional theorem

If those imported assumptions are used to identify the operational theory with ordinary finite-dimensional complex quantum mechanics (possibly with the superselection qualifications in the cited reconstruction), then they cannot simultaneously constitute a PDT-native derivation of a distinct same-input probability law.

More explicitly, on any operational domain D on which the reconstruction identifies PDT preparations, transformations and effects with their quantum counterparts while preserving composition and probabilities,

P_PDT(O | I,R) = P_QM(O | I,R)

for every I,R,O in D. Therefore a strict same-input prediction P_PDT != P_QM requires at least one additional independently derived PDT postulate that changes the admissible operational structure or probability assignment outside the reconstructed equivalence.

### Proof

The reconstruction hypothesis supplies an operational isomorphism Phi from the PDT-labelled model on D to the corresponding complex-QM model, preserving states, effects, transformations, composites and their probability pairing. For an input I, resource specification R and outcome effect O in D, probability preservation gives

P_PDT(O|I,R) = pairing_PDT(O, process_R(I))
                  = pairing_QM(Phi(O), Phi(process_R(I)))
                  = P_QM(O|I,R)

under the declared same-input identification. Hence strict inequality is impossible unless an assumption of the operational equivalence is violated or augmented by prediction-changing PDT structure. QED.

## Why this matters for n=3

The previous cycle showed that spectrality + strong symmetry leave multiple Jordan families. Adding local tomography and a qubit can narrow the family dramatically, but then the selection is being done by established reconstruction assumptions. Any appearance of a special three-level structure after that selection is not a non-circular PDT-native derivation of n=3. PDT must independently explain why its physical distinction/resource principles entail the needed composition/admissibility structure rather than importing it.

## Counterexample logic against the candidate route

Candidate claim: "Add a qubit and local tomography to the Cycle-218 Jordan family; this supplies PDT's missing native composition law and can then yield a novel PDT-vs-QM prediction."

Result: **FALSIFIED as a methodological route.** If the added assumptions are strong enough to invoke the known Jordan-to-complex-QM reconstruction on the relevant domain, the resulting probabilities there are quantum probabilities. If the assumptions are weakened so the reconstruction no longer applies, uniqueness has not been established and the composition target remains open.

This gives a dichotomy:

1. assumptions sufficient for the known reconstruction -> complex-QM operational structure, no same-domain PDT-vs-QM deviation from those assumptions alone;
2. assumptions insufficient for the reconstruction -> no demonstrated unique composite/n=3 selection.

## Prior-art boundary

Barnum & Hilgert, *Strongly symmetric spectral convex bodies are Jordan algebra state spaces* (2019/2020), classify strongly symmetric spectral convex state spaces as simple Euclidean Jordan state spaces or simplices.

Barnum & Wilce, *Local tomography and the Jordan structure of quantum theory*, Foundations of Physics 44 (2014), using a Hanche-Olsen result, show under stated natural constraints that Jordan systems with locally tomographic composites and at least one qubit select orthodox finite-dimensional complex quantum mechanics with superselection qualifications.

Therefore neither the Jordan classification nor the qubit/local-tomography selection should be claimed as PDT novelty.

## Surviving PDT-II obligation

Derive, from PDT's own physical distinction/resource semantics, a resource-indexed joint admissibility law

(A_X, A_Y, R) -> A_XY,R

that (i) is not merely a restatement of local tomography/purification/Jordan reconstruction, (ii) fixes which holistic distinctions are physically accessible, (iii) survives restricted-resource and symmetry-protected counterexamples, and (iv) yields either a rigorous composition theorem or a falsifiable same-input departure from QM.
