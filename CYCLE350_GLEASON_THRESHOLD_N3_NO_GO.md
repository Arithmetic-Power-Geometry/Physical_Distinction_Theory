# Cycle 350 — Gleason-threshold route does not derive n=3

## Target
PDT-II target (2): test whether the dimension threshold in Gleason-type noncontextual probability representation can provide a non-circular PDT-native derivation of n=3. Consequences for targets (1) and (3) are also audited.

## Candidate principle
Let H be a finite-dimensional complex Hilbert space of dimension n. Suppose probabilities assigned to projectors are noncontextual and finitely additive on every orthogonal resolution of the identity. Candidate claim: these requirements select n=3.

## Exact hypotheses and known theorem boundary
For complex Hilbert spaces with n >= 3, Gleason's theorem represents such probability measures by a density operator rho, p(P)=Tr(rho P), under the theorem's standard hypotheses. Dimension 2 is exceptional for the original theorem. This is an imported/known quantum-Hilbert-space result; the Hilbert/projector structure is already assumed.

## Prove-or-falsify result
The selector claim is FALSIFIED. The property does not hold only at n=3: the same representation theorem applies at every n >= 3. Hence n=4 is the smallest decisive counterexample to the inference 'Gleason applicability => n=3'. Dimensions 3 through 12 all pass the threshold test, and the counterfamily continues for arbitrary finite n >= 3.

Moreover, using the threshold to derive physical spatial dimension 3 is circular for PDT-II unless PDT first derives (rather than imports) the relevant complex Hilbert/projector event structure and independently proves why physical dimension must equal the *minimum* Hilbert dimension at which this representation theorem applies. A 'choose the smallest admissible n' rule would be an extra selector, not a consequence of Gleason's theorem.

## Same-input prediction audit
Once the Gleason hypotheses and complex quantum event structure are imported, the resulting probability representation is the ordinary Born-rule form. Therefore the theorem alone supplies no same-input PDT/QM probability difference P_PDT(O|I,R) != P_QM(O|I,R). Any deviation would require a PDT-native change in event structure, admissible states/effects, dynamics, or resource-conditioned probability rule.

## Composition audit
Gleason representation is not a PDT-native composition law. It does not by itself select the admissible correlated composite cone/tensor rule. Thus it cannot close target (1).

## Dimension stress
Exact logical threshold audit n=1..12 is stored in `results/cycle350_gleason_dimension_stress.csv`. n=1,2 do not satisfy the original n>=3 theorem domain; n=3..12 do. No singular selector exists at n=3 within the theorem domain.

## Prior-art check
This route is established quantum-foundations material, not PDT-native. Gleason's theorem is the source of the n>=3 threshold. Contextual-entropy state reconstruction likewise reports reconstruction in Hilbert dimension 3 or greater and relates it to Gleason (Constantin & Doering, arXiv:1208.2046). Independent work deriving three spatial dimensions from operational/spacetime assumptions requires additional physical postulates, e.g. Pitalua-Garcia, Phys. Rev. A 104, 032220 (2021), DOI 10.1103/PhysRevA.104.032220. These checks reject novelty inflation from the threshold alone.

## Status ledger
- Original Gleason representation for complex Hilbert n>=3: IMPORTED/KNOWN.
- 'Gleason applicability => n=3': FALSIFIED; smallest decisive higher-dimensional witness n=4.
- 'Gleason threshold alone => unique PDT composition': FALSIFIED as an inference.
- 'Gleason threshold alone => same-input PDT/QM deviation': FALSIFIED as an inference.
- 'Minimum admissible dimension must be physically realized': OPEN as a separate PDT-native principle; not supplied by Gleason.
- PDT-native derivation of n=3: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Surviving lesson
A theorem whose domain begins at n=3 is not a derivation that nature must choose n=3. PDT-II must explain why higher admissible dimensions are excluded or why a PDT-native optimization/closure principle uniquely selects 3, without assuming the desired dimensionality or quantum Hilbert structure.
