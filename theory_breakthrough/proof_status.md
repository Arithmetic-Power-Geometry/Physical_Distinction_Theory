# PDT Proof-Status Matrix

This file is a guard against overclaiming. Update it whenever a theorem is strengthened, broken, or replaced.

| Claim | Status | Basis |
|---|---|---|
| Original broad PDT axioms alone imply quantum theory | **False / no-go** | Classical-simplex and superquantum GPT foils survive broad operational axioms |
| Pure-state transitivity alone implies bit symmetry | **False / no-go** | Polygon-type GPT counterexamples |
| Pure transitivity + complement isotropy imply bit symmetry | **Proved (elementary group action)** | Map first pure state, then use stabilizer transitivity on complements |
| Bit symmetry implies self-duality | **Imported theorem** | Müller & Ududec, PRL 108, 130401 (2012) |
| BQDC implies inner-product norm | **Imported classical theorem** | Jordan-von Neumann parallelogram theorem |
| Balanced reversible mixer + scaling covariance + conserved distinction power imply BQDC | **Proved conditionally** | Scaling exponent forced to 2, then mixer conservation gives parallelogram identity |
| Invariant neutral state follows from compact reversible pure-state transitivity | **Proved** | Haar averaging |
| Reversal symmetry of a distinguishable pair yields unbiased erasure map | **Proved** | Average identity and swap |
| Complete-erasure uniqueness makes distinguishable partners antipodal about neutral state | **Proved conditionally** | CEU principle + erasure-map lemma |
| Complete elementary resolution + antipodality gives radial state representation | **Proved conditionally** | Direct convex decomposition |
| Radial resolution + pure-state transitivity gives transitive entire boundary | **Proved conditionally** | Interior strict contractions; boundary equals pure set |
| Centrally symmetric convex body with transitive linear isometry action on full boundary is Euclidean ball/ellipsoid | **Proved using standard compact-group averaging lemma** | Haar-average auxiliary inner product; boundary is one Euclidean sphere orbit |
| Therefore CER + CEU + reversible symmetry imply BQDC | **Proved conditionally** | Previous rows |
| One-bit scalar capacity alone implies BQDC or ball geometry | **False / no-go** | Strictly convex `l_p` balls (`1<p<infinity`) all have capacity two under full dual effects, but parallelogram law fails for `p!=2` |
| Rank-two Bregman sufficiency implies spectrality | **Imported theorem** | Harremoës, arXiv:1707.03222 |
| Rank-two monotone Bregman divergence implies ball/spin factor | **Imported theorem** | Harremoës, arXiv:1707.03222 |
| PDT state-resolved regret is automatically a Bregman divergence | **Conditional** | True when derived from a differentiable convex optimal-value function |
| PDT regret automatically satisfies full data processing | **OPEN** | Must be proved from the chosen operational decision model and resource accounting |
| Euclidean elementary ball + local tomography + continuous reversible interaction selects `B^3` | **Imported theorem** | Masanes et al., J. Math. Phys. 55, 122203 (2014), DOI 10.1063/1.4903510 |
| `B^3` is affinely the qubit Bloch ball | **Standard representation** | `rho=(I+x·sigma)/2` |
| Suitable Jordan structure + qubit + locally tomographic composites select complex QM | **Imported reconstruction route** | Barnum-Wilce / Hanche-Olsen framework |
| Inner-product correlation representation implies Tsirelson `2 sqrt(2)` | **Proved conditionally** | Cauchy + parallelogram identity |
| Born weight follows from quadratic distinction power + exclusive coarse-graining additivity + continuity | **Proved conditionally** | Cauchy additive functional equation gives linear weight in `Q_D` |
| Exact Born rule follows once standard complex quantum state/effect trace pairing is reconstructed | **Standard consequence** | `p(E|rho)=Tr(rho E)` |
| Complex QM is derived from original `K_epsilon` alone | **Not proved** | Capacity-to-local-geometry bridge remains open |
| Local capacity measure proportional to volume under additivity, absolute continuity and vacuum symmetry | **Proved conditionally** | Radon-Nikodym density + symmetry |
| Small causal-diamond capacity defect coefficients follow from `K proportional V` | **Conditional on capacity-volume identification** | Known Gibbons-Solodukhin causal-diamond expansion |
| Exact horizon coefficient `A/(4 l_P^2 ln2)` follows from Bekenstein bound + Schwarzschild saturation | **Conditional / imported physics** | Not a PDT-only derivation |
| Einstein equation is independently derived by PDT | **No** | Jacobson limit remains an imported conditional argument |

## Current highest-value open theorem

Construct from the existing finite-resource PDT discrimination problem a state-resolved convex value function `F_R` whose Bregman regret `D_R` satisfies the precise data-processing/monotonicity hypotheses required by the rank-two rigidity theorem.

If proved:

`one-bit elementary physical distinction + resource data processing`

`=> ball/spin factor`

`=> BQDC`

`=> interaction/local tomography selects B^3`

`=> qubit`

becomes the cleanest PDT quantum-side chain.
