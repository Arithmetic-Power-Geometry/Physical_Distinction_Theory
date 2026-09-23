# Cycle 348 — Strong symmetry + spectrality does not select n=3

## Target
Test whether the joint structural principle

1. **Spectrality:** every normalized state decomposes into a finite frame of perfectly distinguishable pure states; and
2. **Strong symmetry:** the reversible group acts transitively on frames of any fixed size,

can supply either (i) a PDT-native composition selector or (ii) a non-circular derivation of distinguished capacity/dimension n=3.

## Exact hypothesis
Let a finite-dimensional compact convex operational state space have capacity n (maximum cardinality of a perfectly distinguishable frame). Assume spectrality and strong symmetry as above. No tensor product, Born rule, Hilbert space, or preferred n is assumed.

## Counterfamily
For every integer n >= 1, the classical n-simplex Delta_n satisfies both hypotheses:

* spectrality: every probability vector p=(p_1,...,p_n) is the convex decomposition sum_i p_i e_i into its perfectly distinguishable vertices;
* strong symmetry: the permutation group S_n acts transitively on ordered k-frames of distinct vertices for every k <= n.

Hence the hypotheses hold at n=1,2,3,... with no exceptional n=3.

Complex quantum n-level state spaces also satisfy the same two structural properties: density matrices have spectral decompositions and unitary transformations act transitively on orthonormal frames of fixed cardinality. Thus even fixing n does not identify a unique classical/quantum state geometry.

## Smallest decisive counterexample
n=2 already defeats the implication

    spectrality + strong symmetry => n=3.

A classical bit simplex and a qubit both satisfy the hypotheses but are inequivalent state spaces.

## Dimension stress n=1..12
The classical counterfamily is exact, not numerical. For each n in 1..12:

* number of pure vertices = n;
* every state has the canonical spectral decomposition in those vertices;
* S_n supplies frame transitivity;
* therefore the candidate principle accepts n.

The same construction extends to every finite n. Higher-dimensional random testing cannot rescue an n=3 selector because an analytic all-n counterfamily already exists.

## Composition consequence
These are single-system structural axioms. They do not, by themselves, choose a unique correlated composite. Therefore they cannot establish a PDT-native tensor/composition rule or a same-input probability gap P_PDT(O|I,R) != P_QM(O|I,R).

## Prior-art boundary
Barnum and Hilgert, *Strongly symmetric spectral convex bodies are Jordan algebra state spaces* (2019; arXiv:1904.03753), prove that strongly symmetric spectral compact convex state spaces are simplices or normalized state spaces of finite-dimensional simple Euclidean Jordan algebras. Thus this route is established GPT/Jordan reconstruction structure, not PDT-native novelty. Mueller and Ududec (2012) likewise show that bit symmetry yields self-duality, illustrating that reversible-symmetry principles constrain GPT geometry without selecting n=3.

## Status

| Claim | Status |
|---|---|
| Classical n-simplex satisfies spectrality for every finite n | PROVED |
| Classical n-simplex satisfies strong symmetry for every finite n | PROVED |
| Complex quantum n-level systems satisfy spectrality + frame symmetry | IMPORTED/KNOWN |
| Spectrality + strong symmetry => n=3 | FALSIFIED |
| Spectrality + strong symmetry => unique PDT composition | FALSIFIED as an inference |
| Spectrality + strong symmetry => same-input PDT/QM deviation | FALSIFIED as an inference |
| Jordan-algebra classification of strongly symmetric spectral state spaces | IMPORTED/KNOWN |
| PDT-native intrinsically joint selector | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## PDT-II consequence
Do not promote strong symmetry, spectrality, or their conjunction as the missing PDT-II principle. The surviving search must add genuinely PDT-native joint structure that is not satisfied uniformly by the classical all-n counterfamily and must still survive comparison against Jordan/GPT reconstruction results.
