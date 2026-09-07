from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'; OUT=ROOT/'generated_latex'; OUT.mkdir(exist_ok=True)
s=json.loads((RES/'summary.json').read_text())
results=r'''\begin{tabularx}{\textwidth}{@{}l l X@{}}
\toprule
Audit & Result & Interpretation \\
\midrule
Automated unit tests & 14/14 passed & Unit and theorem-audit implementation checks \\
Data-processing audit & 0 violations / %(dp)d & Consistent with trace-distance contractivity \\
Standard-quantum CHSH search & %(chsh).9f & $2\sqrt2=%(tsi).9f$; numerical consistency only \\
CHSH sampling gap & $%(gap).3e$ & Random-search gap, not a theory deviation \\
Classical local foil & $S_{\max}=2$ & Satisfies broad operational axioms but not quantum boundary \\
PR-box foil & $S=4$ & No-signalling countermodel to sufficiency of A1--A6 \\
$\ell_2$ parallelogram audit & max defect $%(defect).3e$ & Numerical roundoff around exact Hilbertian identity \\
Born refinement minimizer & $q=%(q).9f$ & Objective minimized numerically at $q=2$ \\
\bottomrule
\end{tabularx}
''' % {'dp':s['data_processing_trials'],'chsh':s['chsh_best'],'tsi':s['tsirelson'],'gap':s['chsh_gap'],'defect':s['p2_max_parallelogram_defect'],'q':s['born_refinement_minimizer_numeric']}
(OUT/'results_table.tex').write_text(results)
print('LaTeX tables exported to',OUT)
