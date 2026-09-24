# Cycle 360 — Asymmetric-distinguishability resource law: prior-art / dimension no-go

## Status

- Quantum relative entropy as an asymptotic currency of asymmetric distinguishability: **IMPORTED/KNOWN**.
- Extension from state pairs to channel pairs / superchannels: **IMPORTED/KNOWN**.
- Candidate inference `resource theory of distinction => n=3`: **FALSIFIED**.
- Candidate inference `resource theory of distinction => unique PDT-native composition`: **FALSIFIED**.
- Candidate inference `resource theory of distinction => P_PDT != P_QM at same microscopic input/resource window`: **FALSIFIED AS AN INFERENCE**.
- A PDT-native restriction that changes an operational probability while fixing microscopic input and resource window: **OPEN**.
- Breakthrough candidate: **NO**.

## Candidate attacked

A natural PDT-II hypothesis is that physical distinction is a resource: pairs of physical alternatives are the resource objects, admissible physical processing cannot increase their distinguishability for free, and composition combines independent distinction resources. One might hope that this principle determines the PDT composition law, selects dimension three, or forces a quantitative departure from quantum mechanics.

This cycle treats that hope as a prove-or-falsify obligation.

## Exact hypotheses tested

Let a resource object be an ordered pair `(rho,sigma)` of finite-dimensional density operators. Let free state processing include arbitrary CPTP maps. For the asymmetric version take quantum relative entropy

`D(rho||sigma) = Tr[rho(log rho - log sigma)]`

when `supp(rho) subseteq supp(sigma)`, with the standard extended-value convention otherwise.

The candidate package is:

1. monotonicity under free processing;
2. additivity on independent tensor products;
3. operational interpretation as a distinction currency;
4. extension to channel pairs under superchannels.

## Decisive counterfamily

Ordinary finite-dimensional complex quantum theory realizes this package in every finite Hilbert dimension. In particular, dimensions 2 and 4 are decisive against a derivation of `n=3`:

- `n=2` satisfies the resource structure, so dimension three is not necessary;
- `n=4` satisfies it, so dimension three is not uniquely selected from above.

The same reasoning extends to every finite `n >= 2`; no dimension-three singularity appears.

For independent systems,

`D(rho_A tensor rho_B || sigma_A tensor sigma_B) = D(rho_A||sigma_A) + D(rho_B||sigma_B)`.

For every CPTP map Phi,

`D(Phi(rho)||Phi(sigma)) <= D(rho||sigma)`.

Consequently the resource-theoretic package is already compatible with ordinary QM itself. It therefore cannot, without an additional PDT-native axiom, imply a same-input probability difference from QM.

## Prior-art rejection

The asymmetric-distinguishability resource programme is established prior art. Wang and Wilde (2019) formulate a resource theory whose objects are pairs of quantum states, with quantum channels as free transformations, and identify quantum relative entropy as the asymptotic interconversion rate. Their companion channel theory treats pairs of channels transformed by quantum superchannels and identifies operational one-shot/asymptotic distinguishability quantities.

References checked:

- Xin Wang and Mark M. Wilde, *Resource theory of asymmetric distinguishability*, arXiv:1905.11629 (2019).
- Xin Wang and Mark M. Wilde, *Resource theory of asymmetric distinguishability for quantum channels*, arXiv:1907.06306 (2019).

Therefore neither “distinction is a resource”, relative-entropy distinction currency, nor its channel/superchannel extension is promotable as PDT novelty.

## Strongest surviving statement

A PDT-II advance must specify extra physical structure not already present in the standard resource theory of distinguishability. In particular, to meet the same-input target it must identify a PDT-native admissibility/resource rule `R` and an observable protocol for which all microscopic preparation/measurement inputs are held fixed and a numerical probability differs from the QM prediction. Merely relabelling quantum distinguishability as “physical distinction” is insufficient.

## Dimension audit

See `artifacts/cycle360_dimension_audit.csv`. The audit is structural: finite-dimensional complex QM realizes the tested package uniformly. The entries do not claim a numerical experiment.

## Counterexample catalogue entry

Smallest nontrivial decisive counterexample to `resource-distinction package => n=3`: a two-dimensional complex quantum system. Smallest higher-dimensional counterexample to uniqueness of 3: a four-dimensional complex quantum system.

## Research consequence

This closes another tempting but non-native PDT-II route. Future cycles should not spend effort trying to derive the missing composition law or `n=3` solely from generic resource monotonicity/additivity/convertibility of distinguishability. The unresolved target must add a genuinely PDT-specific joint or resource-window constraint and then survive direct comparison against QM/GPT/resource-theory models.
