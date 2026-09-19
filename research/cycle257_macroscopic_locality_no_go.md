# Cycle 257 — Macroscopic-locality selector no-go

## Target
Test whether macroscopic locality (ML), interpreted as recovery of Bell-local coarse-grained statistics in a many-copy macroscopic limit, can provide (i) a PDT-native composition law, (ii) a non-circular selector of n=3, or (iii) a universal PDT conservation/refinement principle.

## Exact hypotheses
H1 (IID-ML): for N independent identically distributed microscopic resources, suitably coarse-grained macroscopic fluctuations admit a local hidden-variable description in the N->infinity limit.

H2 (Universal-ML): the same conclusion holds for arbitrary microscopic preparations, including correlated/non-IID N-body preparations and collective coarse-grained measurements.

A proposed n=3 selector would require the accepted principle to hold at n=3 but fail for every competing n under the same declared resource class.

## Falsification / surviving theorem
1. H1 is not n-selective. Any fixed qubit experiment embeds isometrically into span{|0>,|1>} of C^n for every finite n>=2. Tensoring the embedding N times preserves all microscopic probabilities and hence every coarse-grained statistic constructed from those probabilities. Therefore any IID-ML property of the qubit realization survives unchanged in every n>=2. The smallest nontrivial competitor to n=3 is n=2.

2. H2 is false even inside ordinary complex quantum theory. Gallego & Dakic, Phys. Rev. Lett. 127, 120401 (2021), explicitly construct generic non-IID quantum scenarios in which Hilbert-space quantum structure survives coarse graining and collective macroscopic measurements violate a Bell inequality. Thus universal macroscopic locality cannot be imposed as a theorem of PDT if PDT is intended to contain standard quantum theory on that resource class.

3. Composition is not reconstructed. In its standard IID form ML characterizes a correlation constraint associated with the first NPA/macroscopic-locality level, a set strictly larger than the quantum correlation set in general. Hence satisfying ML does not uniquely specify the quantum composite cone/tensor product. Janotta et al. (2011) further show broad GPT state families constrained by ML-type considerations, reinforcing that the principle is not a unique composition axiom.

## Dimension stress
- n=1: degenerate; no nontrivial binary Bell witness.
- n=2: decisive nontrivial competitor.
- n=3..12: exact isometric qubit-subspace embedding preserves the full probability table, so no numerical tolerance enters.
- arbitrary finite n>=2: same analytic embedding proves dimension blindness.
- higher composite dimension: E^{\otimes N} preserves all embedded N-copy event probabilities.

## Edge/resource audit
The distinction between IID and non-IID resources is essential. A statement proved for IID copies cannot be silently promoted to arbitrary controlled-environment records, memory-bearing/non-Markovian preparations, or correlated thermodynamic ensembles. Doing so yields the explicit 2021 quantum counterexample above.

## Prior-art boundary
- Navascues & Wunderlich, Proc. R. Soc. A 466 (2010): Macroscopic Locality; its correlation set is the first NPA-type level and is larger than the quantum set in general.
- Gallego & Dakic, Phys. Rev. Lett. 127, 120401 (2021), DOI 10.1103/PhysRevLett.127.120401: non-IID quantum correlations can remain macroscopically nonlocal.
- Janotta, Gogolin, Barrett & Brunner, New J. Phys. 13, 063024 (2011), arXiv:1012.1215: relation between local GPT geometry, strong self-duality and limits on nonlocal correlations.

Therefore ML is IMPORTED/KNOWN and its universal extension is already false.

## Status
- IID qubit-subspace dimension blindness for all finite n>=2: PROVED.
- ML as non-circular n=3 selector: FALSIFIED.
- ML alone as unique PDT composition law: FALSIFIED as stated.
- Universal ML over arbitrary non-IID quantum resources: FALSIFIED by published quantum counterexample.
- Standard IID ML: IMPORTED/KNOWN.
- Same-input P_PDT(O|I,R) != P_QM(O|I,R): OPEN.
- PDT-native experimentally distinctive inequality: OPEN.
- Gravity/capacity law: OPEN; not invoked.
- BREAKTHROUGH CANDIDATE: NO.

## Surviving lesson
PDT-II must declare its resource window before asserting any macroscopic/refinement law. Any candidate invariant under isometric embedding of a two-level witness is automatically incapable of selecting n=3. More importantly, a PDT law quantified over non-IID or memory-bearing resources must be stress-tested separately: IID asymptotics cannot justify it.